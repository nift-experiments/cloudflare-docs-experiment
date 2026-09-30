<p><a href="https://turso.tech/">Turso</a> is an edge-hosted, distributed database based on <a href="https://libsql.org/">libSQL</a>, an open-source fork of SQLite. Turso was designed to minimize query latency for applications where queries comes from anywhere in the world.</p>
<h2 id="set-up-an-integration-with-turso">Set up an integration with Turso</h2>
<p>To set up an integration with Turso:</p>
<ol>
<li>You need to install Turso CLI to create and populate a database. Use one of the following two commands in your terminal to install the Turso CLI:</li>
</ol>
<pre><code class="language-sh">&#35; On macOS and linux with homebrew&#10;brew install tursodatabase/tap/turso&#10;&#10;&#35; Manual scripted installation&#10;curl -sSfL https://get.tur.so/install.sh | bash&#10;</code></pre>
<p>Next, run the following command to make sure the Turso CLI is installed:</p>
<pre><code class="language-sh">turso --version&#10;</code></pre>
<ol start="2">
<li>Before you create your first Turso database, you have to authenticate with your GitHub account by running:</li>
</ol>
<pre><code class="language-sh">turso auth login&#10;</code></pre>
<pre><code class="language-sh">Waiting for authentication...&#10;✔  Success! Logged in as &lt;YOUR_GITHUB_USERNAME&gt;&#10;</code></pre>
<p>After you have authenticated, you can create a database using the command <code>turso db create &lt;DATABASE_NAME&gt;</code>. Turso will create a database and automatically choose a location closest to you.</p>
<pre><code class="language-sh">turso db create my-db&#10;</code></pre>
<pre><code class="language-sh">&#10;&#35; Example:&#10;Creating database my-db in Amsterdam, Netherlands (ams)&#10;&#10;&#35; Once succeeded:&#10;Created database my-db in Amsterdam, Netherlands (ams) in 13 seconds.&#10;</code></pre>
<p>With the first database created, you can now connect to it directly and execute SQL queries against it.</p>
<pre><code class="language-sh">turso db shell my-db&#10;</code></pre>
<ol start="3">
<li>Copy the following SQL query into the shell you just opened:</li>
</ol>
<pre><code class="language-sql">CREATE TABLE elements (&#10;  id INTEGER NOT NULL,&#10;  elementName TEXT NOT NULL,&#10;  atomicNumber INTEGER NOT NULL,&#10;  symbol TEXT NOT NULL&#10;);&#10;&#10;INSERT INTO elements (id, elementName, atomicNumber, symbol)&#10;VALUES (1, &#x27;Hydrogen&#x27;, 1, &#x27;H&#x27;),&#10;  (2, &#x27;Helium&#x27;, 2, &#x27;He&#x27;),&#10;  (3, &#x27;Lithium&#x27;, 3, &#x27;Li&#x27;),&#10;  (4, &#x27;Beryllium&#x27;, 4, &#x27;Be&#x27;),&#10;  (5, &#x27;Boron&#x27;, 5, &#x27;B&#x27;),&#10;  (6, &#x27;Carbon&#x27;, 6, &#x27;C&#x27;),&#10;  (7, &#x27;Nitrogen&#x27;, 7, &#x27;N&#x27;),&#10;  (8, &#x27;Oxygen&#x27;, 8, &#x27;O&#x27;),&#10;  (9, &#x27;Fluorine&#x27;, 9, &#x27;F&#x27;),&#10;  (10, &#x27;Neon&#x27;, 10, &#x27;Ne&#x27;);&#10;</code></pre>
<ol start="4">
<li>
<p>Configure the Turso database credentials in your Worker:</p>
<p>You need to add your Turso database URL and authentication token as secrets to your Worker. First, get your database URL and create an authentication token:</p>
</li>
</ol>
<pre><code class="language-sh">&#35; Get your database URL&#10;turso db show my-db --url&#10;&#10;&#35; Create an authentication token&#10;turso db tokens create my-db&#10;</code></pre>
<p>Then add these as secrets to your Worker using Wrangler:</p>
<pre><code class="language-sh">&#35; Add the database URL as a secret&#10;npx wrangler secret put TURSO_URL&#10;&#35; When prompted, paste your database URL&#10;&#10;&#35; Add the authentication token as a secret  &#10;npx wrangler secret put TURSO_AUTH_TOKEN&#10;&#35; When prompted, paste your authentication token&#10;</code></pre>
<ol start="5">
<li>In your Worker, install the Turso client library:</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @libsql/client</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @libsql/client" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @libsql/client</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @libsql/client" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @libsql/client</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @libsql/client" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @libsql/client</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @libsql/client" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="6">
<li>The following example shows how to make a query to your Turso database in a Worker. The credentials needed to connect to Turso have been added as <a href="/workers/configuration/secrets/">secrets</a> to your Worker.</li>
</ol>
<pre><code class="language-ts">import { Client as LibsqlClient, createClient } from &quot;@libsql/client/web&quot;;&#10;&#10;export interface Env {&#10;	TURSO_URL?: string;&#10;	TURSO_AUTH_TOKEN?: string;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		const client = buildLibsqlClient(env);&#10;&#10;		try {&#10;			const res = await client.execute(&quot;SELECT * FROM elements&quot;);&#10;			return new Response(JSON.stringify(res), {&#10;				status: 200,&#10;				headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;			});&#10;		} catch (error) {&#10;			console.error(&quot;Error executing SQL query:&quot;, error);&#10;			return new Response(&#10;				JSON.stringify({ error: &quot;Internal Server Error&quot; }),&#10;				{&#10;					status: 500,&#10;				},&#10;			);&#10;		}&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;&#10;function buildLibsqlClient(env: Env): LibsqlClient {&#10;	const url = env.TURSO_URL?.trim();&#10;	if (url === undefined) {&#10;		throw new Error(&quot;TURSO_URL env var is not defined&quot;);&#10;	}&#10;&#10;	const authToken = env.TURSO_AUTH_TOKEN?.trim();&#10;	if (authToken == undefined) {&#10;		throw new Error(&quot;TURSO_AUTH_TOKEN env var is not defined&quot;);&#10;	}&#10;&#10;	return createClient({ url, authToken });&#10;}&#10;</code></pre>
<ul>
<li>The libSQL client library import <code>@libsql/client/web</code> must be imported exactly as shown when working with Cloudflare Workers. The non-web import will not work in the Workers environment.</li>
<li>The <code>Env</code> interface contains the <a href="/workers/configuration/environment-variables/">environment variable</a> and <a href="/workers/configuration/secrets/">secret</a> defined when you added the Turso integration in step 4.</li>
<li>The <code>Env</code> interface also caches the libSQL client object and router, which was created on the first request to the Worker.</li>
<li>The Worker uses <code>buildLibsqlClient</code> to query the <code>elements</code> database and returns the response as a JSON object.</li>
</ul>
<p>With your environment configured and your code ready, you can now test your Worker locally before you deploy.</p>
<p>To learn more about Turso, refer to <a href="https://docs.turso.tech">Turso's official documentation</a>.</p>
