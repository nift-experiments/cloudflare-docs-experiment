<p>In this tutorial, you will use <a href="/workers/">Cloudflare Workers</a> and <a href="https://airtable.com">Airtable</a> to persist form submissions from a front-end user interface. Airtable is a free-to-use spreadsheet solution that has an approachable API for developers. Workers will handle incoming form submissions and use Airtable's <a href="https://airtable.com/api">REST API</a> to asynchronously persist the data in an Airtable base (Airtable's term for a spreadsheet) for later reference.</p>
<p><img src="/images/workers/tutorials/airtable/example.gif" alt="GIF of a complete Airtable and serverless function integration" /></p>
<h2 id="before-you-start">Before you start</h2>
<p>All of the tutorials assume you have already completed the <a href="/workers/get-started/guide/">Get started guide</a>, which gets you set up with a Cloudflare Workers account, <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a>, and <a href="/workers/wrangler/install-and-update/">Wrangler</a>.</p>
<h2 id="1-create-a-form"><ol>
<li>Create a form</li>
</ol></h2>
<p>For this tutorial, you will be building a Workers function that handles input from a contact form. The form this tutorial references will collect a first name, last name, email address, phone number, message subject, and a message.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="build-a-form">Build a form</h3>
@markup("md", "content/.markup/bodies/16067.md")
</aside>
<p>Review a simplified example of the form used in this tuttorial. Note that the <code>action</code> parameter of the <code>&lt;form&gt;</code> tag should point to the deployed Workers application that you will build in this tutorial.</p>
<pre><code class="language-html">&lt;form action=&quot;https://workers-airtable-form.signalnerve.workers.dev/submit&quot; method=&quot;POST&quot;&gt;&#10;  &lt;div&gt;&#10;    &lt;label for=&quot;first_name&quot;&gt;First name&lt;/label&gt;&#10;    &lt;input type=&quot;text&quot; name=&quot;first_name&quot; id=&quot;first_name&quot; autocomplete=&quot;given-name&quot; placeholder=&quot;Ellen&quot; required /&gt;&#10;  &lt;/div&gt;&#10;&#10;  &lt;div&gt;&#10;    &lt;label for=&quot;last_name&quot;&gt;Last name&lt;/label&gt;&#10;    &lt;input type=&quot;text&quot; name=&quot;last_name&quot; id=&quot;last_name&quot; autocomplete=&quot;family-name&quot; placeholder=&quot;Ripley&quot; required /&gt;&#10;  &lt;/div&gt;&#10;&#10;  &lt;div&gt;&#10;    &lt;label for=&quot;email&quot;&gt;Email&lt;/label&gt;&#10;      &lt;input id=&quot;email&quot; name=&quot;email&quot; type=&quot;email&quot; autocomplete=&quot;email&quot; placeholder=&quot;eripley@nostromo.com&quot; required /&gt;&#10;    &lt;/div&gt;&#10;  &lt;/div&gt;&#10;&#10;  &lt;div&gt;&#10;    &lt;label for=&quot;phone&quot;&gt;&#10;      Phone&#10;      &lt;span&gt;Optional&lt;/span&gt;&#10;    &lt;/label&gt;&#10;    &lt;input type=&quot;text&quot; name=&quot;phone&quot; id=&quot;phone&quot; autocomplete=&quot;tel&quot; placeholder=&quot;+1 (123) 456-7890&quot; /&gt;&#10;  &lt;/div&gt;&#10;&#10;  &lt;div&gt;&#10;    &lt;label for=&quot;subject&quot;&gt;Subject&lt;/label&gt;&#10;    &lt;input type=&quot;text&quot; name=&quot;subject&quot; id=&quot;subject&quot; placeholder=&quot;Your example subject&quot; required /&gt;&#10;  &lt;/div&gt;&#10;&#10;  &lt;div&gt;&#10;    &lt;label for=&quot;message&quot;&gt;&#10;      Message&#10;      &lt;span&gt;Max 500 characters&lt;/span&gt;&#10;    &lt;/label&gt;&#10;    &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;4&quot; placeholder=&quot;Tenetur quaerat expedita vero et illo. Tenetur explicabo dolor voluptatem eveniet. Commodi est beatae id voluptatum porro laudantium. Quam placeat accusamus vel officiis vel. Et perferendis dicta ut perspiciatis quos iste. Tempore autem molestias voluptates in sapiente enim doloremque.&quot; required&gt;&lt;/textarea&gt;&#10;  &lt;/div&gt;&#10;&#10;  &lt;div&gt;&#10;    &lt;button type=&quot;submit&quot;&gt;&#10;      Submit&#10;    &lt;/button&gt;&#10;  &lt;/div&gt;&#10;&lt;/form&gt;&#10;</code></pre>
<h2 id="2-create-a-worker-project"><ol start="2">
<li>Create a Worker project</li>
</ol></h2>
<p>To handle the form submission, create and deploy a Worker that parses the incoming form data and prepares it for submission to Airtable.</p>
<p>Create a new <code>airtable-form-handler</code> Worker project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- airtable-form-handler</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- airtable-form-handler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare airtable-form-handler</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare airtable-form-handler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest airtable-form-handler</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest airtable-form-handler" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>JavaScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Then, move into the newly created directory:</p>
<pre><code class="language-sh">cd airtable-form-handler&#10;</code></pre>
<h2 id="3-configure-an-airtable-base"><ol start="3">
<li>Configure an Airtable base</li>
</ol></h2>
<p>When your Worker is complete, it will send data up to an Airtable base via Airtable's REST API.</p>
<p>If you do not have an Airtable account, create one (the free plan is sufficient to complete this tutorial). In Airtable's dashboard, create a new base by selecting <strong>Start from scratch</strong>.</p>
<p>After you have created a new base, set it up for use with the front-end form. Delete the existing columns, and create six columns, with the following field types:</p>
<table>
<thead>
<tr>
<th>Field name</th>
<th>Airtable field type</th>
</tr>
</thead>
<tbody>
<tr>
<td>First Name</td>
<td>&quot;Single line text&quot;</td>
</tr>
<tr>
<td>Last Name</td>
<td>&quot;Single line text&quot;</td>
</tr>
<tr>
<td>Email</td>
<td>&quot;Email&quot;</td>
</tr>
<tr>
<td>Phone Number</td>
<td>&quot;Phone number&quot;</td>
</tr>
<tr>
<td>Subject</td>
<td>&quot;Single line text&quot;</td>
</tr>
<tr>
<td>Message</td>
<td>&quot;Long text&quot;</td>
</tr>
</tbody>
</table>
<p>Note that the field names are case-sensitive. If you change the field names, you will need to exactly match your new field names in the API request you make to Airtable later in the tutorial. Finally, you can optionally rename your table -- by defaulte it will have a name like Table 1. In the below code, we assume the table has been renamed with a more descriptive name, like <code>Form Submissions</code>.</p>
<p>Next, navigate to <a href="https://airtable.com/api">Airtable's API page</a> and select your new base. Note that you must be logged into Airtable to see your base information. In the API documentation page, find your <strong>Airtable base ID</strong>.</p>
<p>You will also need to create a <strong>Personal access token</strong> that you'll use to access your Airtable base. You can do so by visiting the <a href="https://airtable.com/create/tokens">Personal access tokens</a> page on Airtable's website and creating a new token. Make sure that you configure the token in the following way:</p>
<ul>
<li>Scope: the <code>data.records:write</code> scope must be set on the token</li>
<li>Access: access should be granted to the base you have been working with in this tutorial</li>
</ul>
<p>The results access token should now be set in your application. To make the token available in your codebase, use the <a href="/workers/wrangler/commands/general/#secret"><code>wrangler secret</code></a> command. The <code>secret</code> command encrypts and stores environment variables for use in your function, without revealing them to users.</p>
<p>Run <code>wrangler secret put</code>, passing <code>AIRTABLE_ACCESS_TOKEN</code> as the name of your secret:</p>
<pre><code class="language-sh">npx wrangler secret put AIRTABLE_ACCESS_TOKEN&#10;</code></pre>
<pre><code class="language-sh">Enter the secret text you would like assigned to the variable AIRTABLE_ACCESS_TOKEN on the script named airtable-form-handler:&#10;&#42;*****&#10;🌀  Creating the secret for script name airtable-form-handler&#10;✨  Success! Uploaded secret AIRTABLE_ACCESS_TOKEN.&#10;</code></pre>
<p>Before you continue, review the keys that you should have from Airtable:</p>
<ol>
<li><strong>Airtable Table Name</strong>: The name for your table, like Form Submissions.</li>
<li><strong>Airtable Base ID</strong>: The alphanumeric base ID found at the top of your base's API page.</li>
<li><strong>Airtable Access Token</strong>: A Personal Access Token created by the user to access information about your new Airtable base.</li>
</ol>
<h2 id="4-submit-data-to-airtable"><ol start="4">
<li>Submit data to Airtable</li>
</ol></h2>
<p>With your Airtable base set up, and the keys and IDs you need to communicate with the API ready, you will now set up your Worker to persist data from your form into Airtable.</p>
<p>In your Worker project's <code>index.js</code> file, replace the default code with a Workers fetch handler that can respond to requests. When the URL requested has a pathname of <code>/submit</code>, you will handle a new form submission, otherwise, you will return a <code>404 Not Found</code> response.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		const url = new URL(request.url);&#10;		if (url.pathname === &quot;/submit&quot;) {&#10;			await submitHandler(request, env);&#10;		}&#10;		return new Response(&quot;Not found&quot;, { status: 404 });&#10;	},&#10;};&#10;</code></pre>
<p>The <code>submitHandler</code> has two functions. First, it will parse the form data coming from your HTML5 form. Once the data is parsed, use the Airtable API to persist a new row (a new form submission) to your table:</p>
<pre><code class="language-js">async function submitHandler(request, env) {&#10;	if (request.method !== &quot;POST&quot;) {&#10;		return new Response(&quot;Method Not Allowed&quot;, {&#10;			status: 405,&#10;		});&#10;	}&#10;	const body = await request.formData();&#10;&#10;	const { first_name, last_name, email, phone, subject, message } =&#10;		Object.fromEntries(body);&#10;&#10;	// The keys in &quot;fields&quot; are case-sensitive, and&#10;	// should exactly match the field names you set up&#10;	// in your Airtable table, such as &quot;First Name&quot;.&#10;	const reqBody = {&#10;		fields: {&#10;			&quot;First Name&quot;: first_name,&#10;			&quot;Last Name&quot;: last_name,&#10;			Email: email,&#10;			&quot;Phone Number&quot;: phone,&#10;			Subject: subject,&#10;			Message: message,&#10;		},&#10;	};&#10;	await createAirtableRecord(env, reqBody);&#10;}&#10;&#10;// Existing code&#10;// export default ...&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="prevent-potential-errors-when-accessing-request-body">Prevent potential errors when accessing request.body</h3>
@markup("md", "content/.markup/bodies/16066.md")
</aside>
<p>While the majority of this function is concerned with parsing the request body (the data being sent as part of the request), there are two important things to note. First, if the HTTP method sent to this function is not <code>POST</code>, you will return a new response with the status code of <a href="https://httpstatuses.com/405"><code>405 Method Not Allowed</code></a>.</p>
<p>The variable <code>reqBody</code> represents a collection of fields, which are key-value pairs for each column in your Airtable table. By formatting <code>reqBody</code> as an object with a collection of fields, you are creating a new record in your table with a value for each field.</p>
<p>Then you call <code>createAirtableRecord</code> (the function you will define next). The <code>createAirtableRecord</code> function accepts a <code>body</code> parameter, which conforms to the Airtable API's required format — namely, a JavaScript object containing key-value pairs under <code>fields</code>, representing a single record to be created on your table:</p>
<pre><code class="language-js">async function createAirtableRecord(env, body) {&#10;	try {&#10;		const result = fetch(&#10;			`https://api.airtable.com/v0/${env.AIRTABLE_BASE_ID}/${encodeURIComponent(env.AIRTABLE_TABLE_NAME)}`,&#10;			{&#10;				method: &quot;POST&quot;,&#10;				body: JSON.stringify(body),&#10;				headers: {&#10;					Authorization: `Bearer ${env.AIRTABLE_ACCESS_TOKEN}`,&#10;					&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;				},&#10;			},&#10;		);&#10;		return result;&#10;	} catch (error) {&#10;		console.error(error);&#10;	}&#10;}&#10;&#10;// Existing code&#10;// async function submitHandler&#10;// export default ...&#10;</code></pre>
<p>To make an authenticated request to Airtable, you need to provide four constants that represent data about your Airtable account, base, and table name. You have already set <code>AIRTABLE_ACCESS_TOKEN</code> using <code>wrangler secret</code>, since it is a value that should be encrypted. The <strong>Airtable base ID</strong> and <strong>table name</strong>, and <code>FORM_URL</code> are values that can be publicly shared in places like GitHub. Use Wrangler's <a href="/workers/wrangler/migration/v1-to-v2/wrangler-legacy/configuration/#vars"><code>vars</code></a> feature to pass public environment variables from your Wrangler file.</p>
<p>Add a <code>vars</code> table at the end of your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16068.md")
</div>
<p>With all these fields submitted, it is time to deploy your Workers serverless function and get your form communicating with it. First, publish your Worker:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Your Worker project will deploy to a unique URL — for example, <code>https://workers-airtable-form.cloudflare.workers.dev</code>. This represents the first part of your front-end form's <code>action</code> attribute — the second part is the path for your form handler, which is <code>/submit</code>. In your front-end UI, configure your <code>form</code> tag as seen below:</p>
<pre><code class="language-html">&lt;form&#10;	action=&quot;https://workers-airtable-form.cloudflare.workers.dev/submit&quot;&#10;	method=&quot;POST&quot;&#10;	class=&quot;...&quot;&#10;&gt;&#10;	&lt;!-- The rest of your HTML form --&gt;&#10;&lt;/form&gt;&#10;</code></pre>
<p>After you have deployed your new form (refer to the <a href="/pages/tutorials/forms">HTML forms</a> tutorial if you need help creating a form), you should be able to submit a new form submission and see the value show up immediately in Airtable:</p>
<p><img src="/images/workers/tutorials/airtable/example.gif" alt="Example GIF of complete Airtable and serverless function integration" /></p>
<h2 id="conclusion">Conclusion</h2>
<p>With this tutorial completed, you have created a Worker that can accept form submissions and persist them to Airtable. You have learned how to parse form data, set up environment variables, and use the <code>fetch</code> API to make requests to external services outside of your Worker.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/tutorials/build-a-slackbot">Build a Slackbot</a></li>
<li><a href="/workers/tutorials/build-a-jamstack-app">Build a To-Do List Jamstack App</a></li>
<li><a href="/pages/tutorials/build-a-blog-using-nuxt-and-sanity">Build a blog using Nuxt.js and Sanity.io on Cloudflare Pages</a></li>
<li><a href="https://www.youtube.com/watch?v=tFQ2kbiu1K4">James Quick's video on building a Cloudflare Workers + Airtable integration</a></li>
</ul>
