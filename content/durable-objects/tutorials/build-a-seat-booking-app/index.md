<p>In this tutorial, you will learn how to build a seat reservation app using Durable Objects. This app will allow users to book a seat for a flight. The app will be written in TypeScript and will use the new <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite storage backend in Durable Object</a> to store the data.</p>
<p>Using Durable Objects, you can write reusable code that can handle coordination and state management for multiple clients. Moreover, writing data to SQLite in Durable Objects is synchronous and uses local disks, therefore all queries are executed with great performance. You can learn more about SQLite storage in Durable Objects in the <a href="https://blog.cloudflare.com/sqlite-in-durable-objects">SQLite in Durable Objects blog post</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sqlite-in-durable-objects">SQLite in Durable Objects</h3>
@markup("md", "content/.markup/bodies/8088.md")
</aside>
<p>The application will function as follows:</p>
<ul>
<li>A user navigates to the application with a flight number passed as a query parameter.</li>
<li>The application will create a new Durable Object for the flight number, if it does not already exist.</li>
<li>If the Durable Object already exists, the application will retrieve the seats information from the SQLite database.</li>
<li>If the Durable Object does not exist, the application will create a new Durable Object and initialize the SQLite database with the seats information. For the purpose of this tutorial, the seats information is hard-coded in the application.</li>
<li>When a user selects a seat, the application asks for their name. The application will then reserve the seat and store the name in the SQLite database.</li>
<li>The application also broadcasts any changes to the seats to all clients.</li>
</ul>
<p>Let's get started!</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8089.md")
</div></details>
<h2 id="1-create-a-new-project"><ol>
<li>Create a new project</li>
</ol></h2>
<p>Create a new Worker project to create and deploy your app.</p>
<ol>
<li>Create a Worker named <code>seat-booking</code> by running:</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- seat-booking</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- seat-booking" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare seat-booking</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare seat-booking" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest seat-booking</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest seat-booking" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker + Durable Objects</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<ol start="2">
<li>Change into your new project directory to start developing:</li>
</ol>
<pre><code class="language-sh">cd seat-booking&#10;</code></pre>
<h2 id="2-create-the-frontend"><ol start="2">
<li>Create the frontend</li>
</ol></h2>
<p>The frontend of the application is a simple HTML page that allows users to select a seat and enter their name. The application uses <a href="/workers/static-assets/binding/">Workers Static Assets</a> to serve the frontend.</p>
<ol>
<li>
<p>Create a new directory named <code>public</code> in the project root.</p>
</li>
<li>
<p>Create a new file named <code>index.html</code> in the <code>public</code> directory.</p>
</li>
<li>
<p>Add the following HTML code to the <code>index.html</code> file:</p>
</li>
</ol>
<details class="nb-details"><summary>public/index.html</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8090.md")
</div></details>
<ul>
<li>The frontend makes an HTTP <code>GET</code> request to the <code>/seats</code> endpoint to retrieve the available seats for the flight.</li>
<li>It also uses a WebSocket connection to receive updates about the available seats.</li>
<li>When a user clicks on a seat, the <code>bookSeat()</code> function is called that prompts the user to enter their name and then makes a <code>POST</code> request to the <code>/book-seat</code> endpoint.</li>
</ul>
<ol start="4">
<li>Update the bindings in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to configure <code>assets</code> to serve the <code>public</code> directory.</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8091.md")
</div>
<ol start="5">
<li>If you start the development server using the following command, the frontend will be served at <code>http://localhost:8787</code>. However, it will not work because the backend is not yet implemented.</li>
</ol>
<pre><code class="language-bash">npm run dev&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-static-assets">Workers Static Assets</h3>
@markup("md", "content/.markup/bodies/8087.md")
</aside>
<h2 id="3-create-table-for-each-flight"><ol start="3">
<li>Create table for each flight</li>
</ol></h2>
<p>The application already has the binding for the Durable Objects class configured in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. If you update the name of the Durable Objects class in <code>src/index.ts</code>, make sure to also update the binding in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<ol>
<li>Update the binding to use the SQLite storage in Durable Objects. In the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, replace <code>new_classes=[&quot;Flight&quot;]</code> with <code>new_sqlite_classes=[&quot;Flight&quot;]</code>, <code>name = &quot;FLIGHT&quot;</code> with <code>name = &quot;FLIGHT&quot;</code>, and <code>class_name = &quot;MyDurableObject&quot;</code> with <code>class_name = &quot;Flight&quot;</code>. your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> should look similar to this:</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8092.md")
</div>
<p>Your application can now use the SQLite storage in Durable Objects.</p>
<ol start="2">
<li>Add the <code>initializeSeats()</code> function to the <code>Flight</code> class. This function will be called when the Durable Object is initialized. It will check if the table exists, and if not, it will create it. It will also insert seats information in the table.</li>
</ol>
<p>For this tutorial, the function creates an identical seating plan for all the flights. However, in production, you would want to update this function to insert seats based on the flight type.</p>
<p>Replace the <code>Flight</code> class with the following code:</p>
<pre><code class="language-ts">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class Flight extends DurableObject {&#10;	sql = this.ctx.storage.sql;&#10;&#10;	constructor(ctx: DurableObjectState, env: Env) {&#10;		super(ctx, env);&#10;		this.initializeSeats();&#10;	}&#10;&#10;	private initializeSeats() {&#10;		const cursor = this.sql.exec(`PRAGMA table_list`);&#10;&#10;		// Check if a table exists.&#10;		if ([...cursor].find((t) =&gt; t.name === &quot;seats&quot;)) {&#10;			console.log(&quot;Table already exists&quot;);&#10;			return;&#10;		}&#10;&#10;		this.sql.exec(`&#10;				  CREATE TABLE IF NOT EXISTS seats (&#10;					seatId TEXT PRIMARY KEY,&#10;					occupant TEXT&#10;				  )&#10;				`);&#10;&#10;		// For this demo, we populate the table with 60 seats.&#10;		// Since SQLite in DOs is fast, we can do a query per INSERT instead of batching them in a transaction.&#10;		for (let row = 1; row &lt;= 10; row++) {&#10;			for (let col = 0; col &lt; 6; col++) {&#10;				const seatNumber = `${row}${String.fromCharCode(65 + col)}`;&#10;				this.sql.exec(`INSERT INTO seats VALUES (?, null)`, seatNumber);&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<ol start="3">
<li>Add a <code>fetch</code> handler to the <code>Flight</code> class. This handler will return a text response. In <a href="#5-handle-websocket-connections">Step 5</a> You will update the <code>fetch</code> handler to handle the WebSocket connection.</li>
</ol>
<pre><code class="language-ts">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class Flight extends DurableObject {&#10;  ...&#10;  async fetch(request: Request): Promise&lt;Response&gt; {&#10;    return new Response(&quot;Hello from Durable Object!&quot;, { status: 200 });&#10;  }&#10;}&#10;</code></pre>
<ol start="4">
<li>Next, update the Worker's fetch handler to create a unique Durable Object for each flight.</li>
</ol>
<pre><code class="language-ts">export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Get flight id from the query parameter&#10;		const url = new URL(request.url);&#10;		const flightId = url.searchParams.get(&quot;flightId&quot;);&#10;&#10;		if (!flightId) {&#10;			return new Response(&#10;				&quot;Flight ID not found. Provide flightId in the query parameter&quot;,&#10;				{ status: 404 },&#10;			);&#10;		}&#10;&#10;		const stub = env.FLIGHT.getByName(flightId);&#10;		return stub.fetch(request);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Using the flight ID, from the query parameter, a unique Durable Object is created. This Durable Object is initialized with a table if it does not exist.</p>
<h2 id="4-add-methods-to-the-durable-object"><ol start="4">
<li>Add methods to the Durable Object</li>
</ol></h2>
<ol>
<li>Add the <code>getSeats()</code> function to the <code>Flight</code> class. This function returns all the seats in the table.</li>
</ol>
<pre><code class="language-ts">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class Flight extends DurableObject {&#10;    ...&#10;&#10;	private initializeSeats() {&#10;		...&#10;	}&#10;&#10;	// Get all seats.&#10;	getSeats() {&#10;		let results = [];&#10;&#10;		// Query returns a cursor.&#10;		let cursor = this.sql.exec(`SELECT seatId, occupant FROM seats`);&#10;&#10;		// Cursors are iterable.&#10;		for (let row of cursor) {&#10;			// Each row is an object with a property for each column.&#10;			results.push({ seatNumber: row.seatId, occupant: row.occupant });&#10;		}&#10;&#10;		return results;&#10;	}&#10;}&#10;</code></pre>
<ol start="2">
<li>Add the <code>assignSeat()</code> function to the <code>Flight</code> class. This function will assign a seat to a passenger. It takes the seat number and the passenger name as parameters.</li>
</ol>
<pre><code class="language-ts">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class Flight extends DurableObject {&#10;	...&#10;&#10;	private initializeSeats() {&#10;		...&#10;	}&#10;&#10;	// Get all seats.&#10;	getSeats() {&#10;		...&#10;	}&#10;&#10;	// Assign a seat to a passenger.&#10;	assignSeat(seatId: string, occupant: string) {&#10;		// Check that seat isn&#x27;t occupied.&#10;		let cursor = this.sql.exec(&#10;			`SELECT occupant FROM seats WHERE seatId = ?`,&#10;			seatId,&#10;		);&#10;		let result = cursor.toArray()[0]; // Get the first result from the cursor.&#10;&#10;		if (!result) {&#10;			return {message: &#x27;Seat not available&#x27;,  status: 400 };&#10;		}&#10;		if (result.occupant !== null) {&#10;			return {message: &#x27;Seat not available&#x27;,  status: 400 };&#10;		}&#10;&#10;		// If the occupant is already in a different seat, remove them.&#10;		this.sql.exec(&#10;			`UPDATE seats SET occupant = null WHERE occupant = ?`,&#10;			occupant,&#10;		);&#10;&#10;		// Assign the seat. Note: We don&#x27;t have to worry that a concurrent request may&#10;		// have grabbed the seat between the two queries, because the code is synchronous&#10;		// (no `await`s) and the database is private to this Durable Object. Nothing else&#10;		// could have changed since we checked that the seat was available earlier!&#10;		this.sql.exec(&#10;			`UPDATE seats SET occupant = ? WHERE seatId = ?`,&#10;			occupant,&#10;			seatId,&#10;		);&#10;&#10;		// Broadcast the updated seats.&#10;		this.broadcastSeats();&#10;		return {message: `Seat ${seatId} booked successfully`, status: 200 };&#10;	}&#10;}&#10;</code></pre>
<p>The above function uses the <code>broadcastSeats()</code> function to broadcast the updated seats to all the connected clients. In the next section, we will add the <code>broadcastSeats()</code> function.</p>
<h2 id="5-handle-websocket-connections"><ol start="5">
<li>Handle WebSocket connections</li>
</ol></h2>
<p>All the clients will connect to the Durable Object using WebSockets. The Durable Object will broadcast the updated seats to all the connected clients. This allows the clients to update the UI in real time.</p>
<ol>
<li>Add the <code>handleWebSocket()</code> function to the <code>Flight</code> class. This function handles the WebSocket connections.</li>
</ol>
<pre><code class="language-ts">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class Flight extends DurableObject {&#10;	...&#10;&#10;	private initializeSeats() {&#10;		...&#10;	}&#10;&#10;	// Get all seats.&#10;	getSeats() {&#10;		...&#10;	}&#10;&#10;	// Assign a seat to a passenger.&#10;	assignSeat(seatId: string, occupant: string) {&#10;		...&#10;	}&#10;&#10;  private handleWebSocket(request: Request) {&#10;		console.log(&#x27;WebSocket connection requested&#x27;);&#10;		const [client, server] = Object.values(new WebSocketPair());&#10;&#10;		this.ctx.acceptWebSocket(server);&#10;		console.log(&#x27;WebSocket connection established&#x27;);&#10;&#10;		return new Response(null, { status: 101, webSocket: client });&#10;	}&#10;}&#10;</code></pre>
<ol start="2">
<li>Add the <code>broadcastSeats()</code> function to the <code>Flight</code> class. This function will broadcast the updated seats to all the connected clients.</li>
</ol>
<pre><code class="language-ts">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class Flight extends DurableObject {&#10;	...&#10;&#10;	private initializeSeats() {&#10;		...&#10;	}&#10;&#10;	// Get all seats.&#10;	getSeats() {&#10;		...&#10;	}&#10;&#10;	// Assign a seat to a passenger.&#10;	assignSeat(seatId: string, occupant: string) {&#10;		...&#10;	}&#10;&#10;  private handleWebSocket(request: Request) {&#10;		...&#10;	}&#10;&#10;  private broadcastSeats() {&#10;		this.ctx.getWebSockets().forEach((ws) =&gt; ws.send(this.getSeats()));&#10;	}&#10;}&#10;</code></pre>
<ol start="3">
<li>Next, update the <code>fetch</code> handler in the <code>Flight</code> class. This handler will handle all the incoming requests from the Worker and handle the WebSocket connections using the <code>handleWebSocket()</code> method.</li>
</ol>
<pre><code class="language-ts">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class Flight extends DurableObject {&#10;	...&#10;&#10;	private initializeSeats() {&#10;		...&#10;	}&#10;&#10;	// Get all seats.&#10;	getSeats() {&#10;		...&#10;	}&#10;&#10;	// Assign a seat to a passenger.&#10;	assignSeat(seatId: string, occupant: string) {&#10;		...&#10;	}&#10;&#10;  private handleWebSocket(request: Request) {&#10;		...&#10;	}&#10;&#10;  private broadcastSeats() {&#10;		...&#10;	}&#10;&#10;  async fetch(request: Request) {&#10;		return this.handleWebSocket(request);&#10;	}&#10;}&#10;</code></pre>
<ol start="4">
<li>Finally, update the <code>fetch</code> handler of the Worker.</li>
</ol>
<pre><code class="language-ts">export default {&#10;	...&#10;&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Get flight id from the query parameter&#10;		...&#10;&#10;		if (request.method === &quot;GET&quot; &amp;&amp; url.pathname === &quot;/seats&quot;) {&#10;			return new Response(JSON.stringify(await stub.getSeats()), {&#10;				headers: { &#x27;Content-Type&#x27;: &#x27;application/json&#x27; },&#10;			});&#10;		} else if (request.method === &quot;POST&quot; &amp;&amp; url.pathname === &quot;/book-seat&quot;) {&#10;			const { seatNumber, name } = (await request.json()) as {&#10;				seatNumber: string;&#10;				name: string;&#10;			};&#10;			const result = await stub.assignSeat(seatNumber, name);&#10;			return new Response(JSON.stringify(result));&#10;		} else if (request.headers.get(&quot;Upgrade&quot;) === &quot;websocket&quot;) {&#10;			return stub.fetch(request);&#10;		}&#10;&#10;		return new Response(&quot;Not found&quot;, { status: 404 });&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>The <code>fetch</code> handler in the Worker now calls appropriate Durable Object function to handle the incoming request. If the request is a <code>GET</code> request to <code>/seats</code>, the Worker returns the seats from the Durable Object. If the request is a <code>POST</code> request to <code>/book-seat</code>, the Worker calls the <code>bookSeat</code> method of the Durable Object to assign the seat to the passenger. If the request is a WebSocket connection, the Durable Object handles the WebSocket connection.</p>
<h2 id="6-test-the-application"><ol start="6">
<li>Test the application</li>
</ol></h2>
<p>You can test the application locally by running the following command:</p>
<pre><code class="language-sh">npm run dev&#10;</code></pre>
<p>This starts a local development server that runs the application. The application is served at <code>http://localhost:8787</code>.</p>
<p>Navigate to the application at <code>http://localhost:8787</code> in your browser. Since the flight ID is not specified, the application displays an error message.</p>
<p>Update the URL with the flight ID as <code>http://localhost:8787?flightId=1234</code>. The application displays the seats for the flight with the ID <code>1234</code>.</p>
<h2 id="7-deploy-the-application"><ol start="7">
<li>Deploy the application</li>
</ol></h2>
<p>To deploy the application, run the following command:</p>
<pre><code class="language-sh">npm run deploy&#10;</code></pre>
<pre><code class="language-sh"> ⛅️ wrangler 3.78.8&#10;&#45;------------------&#10;&#10;🌀 Building list of assets...&#10;🌀 Starting asset upload...&#10;🌀 Found 1 new or modified file to upload. Proceeding with upload...&#10;&#43; /index.html&#10;Uploaded 1 of 1 assets&#10;✨ Success! Uploaded 1 file (1.93 sec)&#10;&#10;Total Upload: 3.45 KiB / gzip: 1.39 KiB&#10;Your worker has access to the following bindings:&#10;&#45; Durable Objects:&#10;  &#45; FLIGHT: Flight&#10;Uploaded seat-book (12.12 sec)&#10;Deployed seat-book triggers (5.54 sec)&#10;  [DEPLOYED_APP_LINK]&#10;Current Version ID: [BINDING_ID]&#10;</code></pre>
<p>Navigate to the <code>[DEPLOYED_APP_LINK]</code> to see the application. Again, remember to pass the flight ID as a query string parameter.</p>
<h2 id="summary">Summary</h2>
<p>In this tutorial, you have:</p>
<ul>
<li>used the SQLite storage backend in Durable Objects to store the seats for a flight.</li>
<li>created a Durable Object class to manage the seat booking.</li>
<li>deployed the application to Cloudflare Workers!</li>
</ul>
<p>The full code for this tutorial is available on <a href="https://github.com/harshil1712/seat-booking-app">GitHub</a>.</p>
