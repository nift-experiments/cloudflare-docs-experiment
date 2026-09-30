<p>This guide will instruct you through setting up and deploying your first application with Cloudflare AI. You will build a fully-featured AI-powered application, using tools like Workers AI, Vectorize, D1, and Cloudflare Workers.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-a-managed-option">Looking for a managed option?</h3>
@markup("md", "content/.markup/bodies/15851.md")
</aside>
<p>At the end of this tutorial, you will have built an AI tool that allows you to store information and query it using a Large Language Model. This pattern, known as Retrieval Augmented Generation, or RAG, is a useful project you can build by combining multiple aspects of Cloudflare's AI toolkit. You do not need to have experience working with AI tools to build this application.</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15852.md")
</div></details>
<p>You will also need access to <a href="/vectorize/platform/pricing/">Vectorize</a>. During this tutorial, we will show how you can optionally integrate with <a href="http://anthropic.com">Anthropic Claude</a> as well. You will need an <a href="https://docs.anthropic.com/en/api/getting-started">Anthropic API key</a> to do so.</p>
<h2 id="1-create-a-new-worker-project"><ol>
<li>Create a new Worker project</li>
</ol></h2>
<p>C3 (<code>create-cloudflare-cli</code>) is a command-line tool designed to help you setup and deploy Workers to Cloudflare as fast as possible.</p>
<p>Open a terminal window and run C3 to create your Worker project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- rag-ai-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- rag-ai-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare rag-ai-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare rag-ai-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest rag-ai-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest rag-ai-tutorial" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>JavaScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>In your project directory, C3 has generated several files.</p>
<details class="nb-details"><summary>What files did C3 create?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15853.md")
</div></details>
<p>Now, move into your newly created directory:</p>
<pre><code class="language-sh">cd rag-ai-tutorial&#10;</code></pre>
<h2 id="2-develop-with-wrangler-cli"><ol start="2">
<li>Develop with Wrangler CLI</li>
</ol></h2>
<p>The Workers command-line interface, <a href="/workers/wrangler/install-and-update/">Wrangler</a>, allows you to <a href="/workers/wrangler/commands/general/#init">create</a>, <a href="/workers/wrangler/commands/general/#dev">test</a>, and <a href="/workers/wrangler/commands/general/#deploy">deploy</a> your Workers projects. C3 will install Wrangler in projects by default.</p>
<p>After you have created your first Worker, run the <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> command in the project directory to start a local server for developing your Worker. This will allow you to test your Worker locally during development.</p>
<pre><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>You will now be able to go to <a href="http://localhost:8787">http://localhost:8787</a> to see your Worker running. Any changes you make to your code will trigger a rebuild, and reloading the page will show you the up-to-date output of your Worker.</p>
<h2 id="3-adding-the-ai-binding"><ol start="3">
<li>Adding the AI binding</li>
</ol></h2>
<p>To begin using Cloudflare's AI products, you can add the <code>ai</code> block to the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> as a <a href="/workers/local-development/#remote-bindings">remote binding</a>. This will set up a binding to Cloudflare's AI models in your code that you can use to interact with the available AI models on the platform.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15850.md")
</aside>
<p>This example features the <a href="/workers-ai/models/llama-3-8b-instruct/"><code>@cf/meta/llama-3-8b-instruct</code> model</a>, which generates text.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15854.md")
</div>
<p>Now, find the <code>src/index.js</code> file. Inside the <code>fetch</code> handler, you can query the <code>AI</code> binding:</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		const answer = await env.AI.run(&quot;@cf/meta/llama-3-8b-instruct&quot;, {&#10;			messages: [{ role: &quot;user&quot;, content: `What is the square root of 9?` }],&#10;		});&#10;&#10;		return new Response(JSON.stringify(answer));&#10;	},&#10;};&#10;</code></pre>
<p>By querying the LLM through the <code>AI</code> binding, we can interact directly with Cloudflare AI's large language models directly in our code. In this example, we are using the <a href="/workers-ai/models/llama-3-8b-instruct/"><code>@cf/meta/llama-3-8b-instruct</code> model</a>, which generates text.</p>
<p>Deploy your Worker using <code>wrangler</code>:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Making a request to your Worker will now generate a text response from the LLM, and return it as a JSON object.</p>
<pre><code class="language-sh">curl https://example.username.workers.dev&#10;</code></pre>
<pre><code class="language-sh">{&quot;response&quot;:&quot;Answer: The square root of 9 is 3.&quot;}&#10;</code></pre>
<h2 id="4-adding-embeddings-using-cloudflare-d1-and-vectorize"><ol start="4">
<li>Adding embeddings using Cloudflare D1 and Vectorize</li>
</ol></h2>
<p>Embeddings allow you to add additional capabilities to the language models you can use in your Cloudflare AI projects. This is done via <strong>Vectorize</strong>, Cloudflare's vector database.</p>
<p>To begin using Vectorize, create a new embeddings index using <code>wrangler</code>. This index will store vectors with 768 dimensions, and will use cosine similarity to determine which vectors are most similar to each other:</p>
<pre><code class="language-sh">npx wrangler vectorize create vector-index --dimensions=768 --metric=cosine&#10;</code></pre>
<p>Then, add the configuration details for your new Vectorize index to the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15855.md")
</div>
<p>A vector index allows you to store a collection of dimensions, which are floating point numbers used to represent your data. When you want to query the vector database, you can also convert your query into dimensions. <strong>Vectorize</strong> is designed to efficiently determine which stored vectors are most similar to your query.</p>
<p>To implement the searching feature, you must set up a D1 database from Cloudflare. In D1, you can store your app's data. Then, you change this data into a vector format. When someone searches and it matches the vector, you can show them the matching data.</p>
<p>Create a new D1 database using <code>wrangler</code>:</p>
<pre><code class="language-sh">npx wrangler d1 create database&#10;</code></pre>
<p>Then, paste the configuration details output from the previous command into the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15856.md")
</div>
<p>In this application, we'll create a <code>notes</code> table in D1, which will allow us to store notes and later retrieve them in Vectorize. To create this table, run a SQL command using <code>wrangler d1 execute</code>:</p>
<pre><code class="language-sh">npx wrangler d1 execute database --remote --command &quot;CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT NOT NULL)&quot;&#10;</code></pre>
<p>Now, we can add a new note to our database using <code>wrangler d1 execute</code>:</p>
<pre><code class="language-sh">npx wrangler d1 execute database --remote --command &quot;INSERT INTO notes (text) VALUES (&#x27;The best pizza topping is pepperoni&#x27;)&quot;&#10;</code></pre>
<h2 id="5-creating-a-workflow"><ol start="5">
<li>Creating a workflow</li>
</ol></h2>
<p>Before we begin creating notes, we will introduce a <a href="/workflows">Cloudflare Workflow</a>. This will allow us to define a durable workflow that can safely and robustly execute all the steps of the RAG process.</p>
<p>To begin, add a new <code>[[workflows]]</code> block to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15857.md")
</div>
<p>In <code>src/index.js</code>, add a new class called <code>RAGWorkflow</code> that extends <code>WorkflowEntrypoint</code>:</p>
<pre><code class="language-js">import { WorkflowEntrypoint } from &quot;cloudflare:workers&quot;;&#10;&#10;export class RAGWorkflow extends WorkflowEntrypoint {&#10;	async run(event, step) {&#10;		await step.do(&quot;example step&quot;, async () =&gt; {&#10;			console.log(&quot;Hello World!&quot;);&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>This class will define a single workflow step that will log &quot;Hello World!&quot; to the console. You can add as many steps as you need to your workflow.</p>
<p>On its own, this workflow will not do anything. To execute the workflow, we will call the <code>RAG_WORKFLOW</code> binding, passing in any parameters that the workflow needs to properly complete. Here is an example of how we can call the workflow:</p>
<pre><code class="language-js">env.RAG_WORKFLOW.create({ params: { text } });&#10;</code></pre>
<h2 id="6-creating-notes-and-adding-them-to-vectorize"><ol start="6">
<li>Creating notes and adding them to Vectorize</li>
</ol></h2>
<p>To expand on your Workers function in order to handle multiple routes, we will add <code>hono</code>, a routing library for Workers. This will allow us to create a new route for adding notes to our database. Install <code>hono</code> using <code>npm</code>:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i hono" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add hono" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add hono" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add hono" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Then, import <code>hono</code> into your <code>src/index.js</code> file. You should also update the <code>fetch</code> handler to use <code>hono</code>:</p>
<pre><code class="language-js">import { Hono } from &quot;hono&quot;;&#10;const app = new Hono();&#10;&#10;app.get(&quot;/&quot;, async (c) =&gt; {&#10;	const answer = await c.env.AI.run(&quot;@cf/meta/llama-3-8b-instruct&quot;, {&#10;		messages: [{ role: &quot;user&quot;, content: `What is the square root of 9?` }],&#10;	});&#10;&#10;	return c.json(answer);&#10;});&#10;&#10;export default app;&#10;</code></pre>
<p>This will establish a route at the root path <code>/</code> that is functionally equivalent to the previous version of your application.</p>
<p>Now, we can update our workflow to begin adding notes to our database, and generating the related embeddings for them.</p>
<p>This example features the <a href="/workers-ai/models/bge-base-en-v1.5/"><code>@cf/baai/bge-base-en-v1.5</code> model</a>, which can be used to create an embedding. Embeddings are stored and retrieved inside <a href="/vectorize/">Vectorize</a>, Cloudflare's vector database. The user query is also turned into an embedding so that it can be used for searching within Vectorize.</p>
<pre><code class="language-js">import { WorkflowEntrypoint } from &quot;cloudflare:workers&quot;;&#10;&#10;export class RAGWorkflow extends WorkflowEntrypoint {&#10;	async run(event, step) {&#10;		const env = this.env;&#10;		const { text } = event.payload;&#10;&#10;		const record = await step.do(`create database record`, async () =&gt; {&#10;			const query = &quot;INSERT INTO notes (text) VALUES (?) RETURNING *&quot;;&#10;&#10;			const { results } = await env.DB.prepare(query).bind(text).run();&#10;&#10;			const record = results[0];&#10;			if (!record) throw new Error(&quot;Failed to create note&quot;);&#10;			return record;&#10;		});&#10;&#10;		const embedding = await step.do(`generate embedding`, async () =&gt; {&#10;			const embeddings = await env.AI.run(&quot;@cf/baai/bge-base-en-v1.5&quot;, {&#10;				text: text,&#10;			});&#10;			const values = embeddings.data[0];&#10;			if (!values) throw new Error(&quot;Failed to generate vector embedding&quot;);&#10;			return values;&#10;		});&#10;&#10;		await step.do(`insert vector`, async () =&gt; {&#10;			return env.VECTOR_INDEX.upsert([&#10;				{&#10;					id: record.id.toString(),&#10;					values: embedding,&#10;				},&#10;			]);&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>The workflow does the following things:</p>
<ol>
<li>Accepts a <code>text</code> parameter.</li>
<li>Insert a new row into the <code>notes</code> table in D1, and retrieve the <code>id</code> of the new row.</li>
<li>Convert the <code>text</code> into a vector using the <code>embeddings</code> model of the LLM binding.</li>
<li>Upsert the <code>id</code> and <code>vectors</code> into the <code>vector-index</code> index in Vectorize.</li>
</ol>
<p>By doing this, you will create a new vector representation of the note, which can be used to retrieve the note later.</p>
<p>To complete the code, we will add a route that allows users to submit notes to the database. This route will parse the JSON request body, get the <code>note</code> parameter, and create a new instance of the workflow, passing the parameter:</p>
<pre><code class="language-js">app.post(&quot;/notes&quot;, async (c) =&gt; {&#10;	const { text } = await c.req.json();&#10;	if (!text) return c.text(&quot;Missing text&quot;, 400);&#10;	await c.env.RAG_WORKFLOW.create({ params: { text } });&#10;	return c.text(&quot;Created note&quot;, 201);&#10;});&#10;</code></pre>
<h2 id="7-querying-vectorize-to-retrieve-notes"><ol start="7">
<li>Querying Vectorize to retrieve notes</li>
</ol></h2>
<p>To complete your code, you can update the root path (<code>/</code>) to query Vectorize. You will convert the query into a vector, and then use the <code>vector-index</code> index to find the most similar vectors.</p>
<p>The <code>topK</code> parameter limits the number of vectors returned by the function. For instance, providing a <code>topK</code> of 1 will only return the <em>most similar</em> vector based on the query. Setting <code>topK</code> to 5 will return the 5 most similar vectors.</p>
<p>Given a list of similar vectors, you can retrieve the notes that match the record IDs stored alongside those vectors. In this case, we are only retrieving a single note - but you may customize this as needed.</p>
<p>You can insert the text of those notes as context into the prompt for the LLM binding. This is the basis of Retrieval-Augmented Generation, or RAG: providing additional context from data outside of the LLM to enhance the text generated by the LLM.</p>
<p>We'll update the prompt to include the context, and to ask the LLM to use the context when responding:</p>
<pre><code class="language-js">import { Hono } from &quot;hono&quot;;&#10;const app = new Hono();&#10;&#10;// Existing post route...&#10;// app.post(&#x27;/notes&#x27;, async (c) =&gt; { ... })&#10;&#10;app.get(&quot;/&quot;, async (c) =&gt; {&#10;	const question = c.req.query(&quot;text&quot;) || &quot;What is the square root of 9?&quot;;&#10;&#10;	const embeddings = await c.env.AI.run(&quot;@cf/baai/bge-base-en-v1.5&quot;, {&#10;		text: question,&#10;	});&#10;	const vectors = embeddings.data[0];&#10;&#10;	const vectorQuery = await c.env.VECTOR_INDEX.query(vectors, { topK: 1 });&#10;	let vecId;&#10;	if (&#10;		vectorQuery.matches &amp;&amp;&#10;		vectorQuery.matches.length &gt; 0 &amp;&amp;&#10;		vectorQuery.matches[0]&#10;	) {&#10;		vecId = vectorQuery.matches[0].id;&#10;	} else {&#10;		console.log(&quot;No matching vector found or vectorQuery.matches is empty&quot;);&#10;	}&#10;&#10;	let notes = [];&#10;	if (vecId) {&#10;		const query = `SELECT * FROM notes WHERE id = ?`;&#10;		const { results } = await c.env.DB.prepare(query).bind(vecId).run();&#10;		if (results) notes = results.map((vec) =&gt; vec.text);&#10;	}&#10;&#10;	const contextMessage = notes.length&#10;		? `Context:\n${notes.map((note) =&gt; `- ${note}`).join(&quot;\n&quot;)}`&#10;		: &quot;&quot;;&#10;&#10;	const systemPrompt = `When answering the question or responding, use the context provided, if it is provided and relevant.`;&#10;&#10;	const { response: answer } = await c.env.AI.run(&#10;		&quot;@cf/meta/llama-3-8b-instruct&quot;,&#10;		{&#10;			messages: [&#10;				...(notes.length ? [{ role: &quot;system&quot;, content: contextMessage }] : []),&#10;				{ role: &quot;system&quot;, content: systemPrompt },&#10;				{ role: &quot;user&quot;, content: question },&#10;			],&#10;		},&#10;	);&#10;&#10;	return c.text(answer);&#10;});&#10;&#10;app.onError((err, c) =&gt; {&#10;	return c.text(err);&#10;});&#10;&#10;export default app;&#10;</code></pre>
<h2 id="8-adding-anthropic-claude-model-optional"><ol start="8">
<li>Adding Anthropic Claude model (optional)</li>
</ol></h2>
<p>If you are working with larger documents, you have the option to use Anthropic's <a href="https://claude.ai/">Claude models</a>, which have large context windows and are well-suited to RAG workflows.</p>
<p>To begin, install the <code>@anthropic-ai/sdk</code> package:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @anthropic-ai/sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @anthropic-ai/sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @anthropic-ai/sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @anthropic-ai/sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @anthropic-ai/sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @anthropic-ai/sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @anthropic-ai/sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @anthropic-ai/sdk" aria-label="Copy to clipboard">Copy</button></div></div>
<p>In <code>src/index.js</code>, you can update the <code>GET /</code> route to check for the <code>ANTHROPIC_API_KEY</code> environment variable. If it is set, we can generate text using the Anthropic SDK. If it is not set, we'll fall back to the existing Workers AI code:</p>
<pre><code class="language-js">import Anthropic from &#x27;@anthropic-ai/sdk&#x27;;&#10;&#10;app.get(&#x27;/&#x27;, async (c) =&gt; {&#10;  // ... Existing code&#10;	const systemPrompt = `When answering the question or responding, use the context provided, if it is provided and relevant.`&#10;&#10;	let modelUsed = &quot;&quot;&#10;	let response = null&#10;&#10;	if (c.env.ANTHROPIC_API_KEY) {&#10;		const anthropic = new Anthropic({&#10;			apiKey: c.env.ANTHROPIC_API_KEY&#10;		})&#10;&#10;		const model = &quot;claude-3-5-sonnet-latest&quot;&#10;		modelUsed = model&#10;&#10;		const message = await anthropic.messages.create({&#10;			max_tokens: 1024,&#10;			model,&#10;			messages: [&#10;				{ role: &#x27;user&#x27;, content: question }&#10;			],&#10;			system: [systemPrompt, notes ? contextMessage : &#x27;&#x27;].join(&quot; &quot;)&#10;		})&#10;&#10;		response = {&#10;			response: message.content.map(content =&gt; content.text).join(&quot;\n&quot;)&#10;		}&#10;	} else {&#10;		const model = &quot;@cf/meta/llama-3.1-8b-instruct&quot;&#10;		modelUsed = model&#10;&#10;		response = await c.env.AI.run(&#10;			model,&#10;			{&#10;				messages: [&#10;					...(notes.length ? [{ role: &#x27;system&#x27;, content: contextMessage }] : []),&#10;					{ role: &#x27;system&#x27;, content: systemPrompt },&#10;					{ role: &#x27;user&#x27;, content: question }&#10;				]&#10;			}&#10;		)&#10;	}&#10;&#10;	if (response) {&#10;		c.header(&#x27;x-model-used&#x27;, modelUsed)&#10;		return c.text(response.response)&#10;	} else {&#10;		return c.text(&quot;We were unable to generate output&quot;, 500)&#10;	}&#10;})&#10;</code></pre>
<p>Finally, you'll need to set the <code>ANTHROPIC_API_KEY</code> environment variable in your Workers application. You can do this by using <code>wrangler secret put</code>:</p>
<pre><code class="language-sh">$ npx wrangler secret put ANTHROPIC_API_KEY&#10;</code></pre>
<h2 id="9-deleting-notes-and-vectors"><ol start="9">
<li>Deleting notes and vectors</li>
</ol></h2>
<p>If you no longer need a note, you can delete it from the database. Any time that you delete a note, you will also need to delete the corresponding vector from Vectorize. You can implement this by building a <code>DELETE /notes/:id</code> route in your <code>src/index.js</code> file:</p>
<pre><code class="language-js">app.delete(&quot;/notes/:id&quot;, async (c) =&gt; {&#10;	const { id } = c.req.param();&#10;&#10;	const query = `DELETE FROM notes WHERE id = ?`;&#10;	await c.env.DB.prepare(query).bind(id).run();&#10;&#10;	await c.env.VECTOR_INDEX.deleteByIds([id]);&#10;&#10;	return c.status(204);&#10;});&#10;</code></pre>
<h2 id="10-text-splitting-optional"><ol start="10">
<li>Text splitting (optional)</li>
</ol></h2>
<p>For large pieces of text, it is recommended to split the text into smaller chunks. This allows LLMs to more effectively gather relevant context, without needing to retrieve large pieces of text.</p>
<p>To implement this, we'll add a new NPM package to our project, `@langchain/textsplitters':</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @langchain/textsplitters</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @langchain/textsplitters" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @langchain/textsplitters</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @langchain/textsplitters" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @langchain/textsplitters</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @langchain/textsplitters" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @langchain/textsplitters</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @langchain/textsplitters" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The <code>RecursiveCharacterTextSplitter</code> class provided by this package will split the text into smaller chunks. It can be customized to your liking, but the default config works in most cases:</p>
<pre><code class="language-js">import { RecursiveCharacterTextSplitter } from &quot;@langchain/textsplitters&quot;;&#10;&#10;const text = &quot;Some long piece of text...&quot;;&#10;&#10;const splitter = new RecursiveCharacterTextSplitter({&#10;	// These can be customized to change the chunking size&#10;	// chunkSize: 1000,&#10;	// chunkOverlap: 200,&#10;});&#10;&#10;const output = await splitter.createDocuments([text]);&#10;console.log(output); // [{ pageContent: &#x27;Some long piece of text...&#x27; }]&#10;</code></pre>
<p>To use this splitter, we'll update the workflow to split the text into smaller chunks. We'll then iterate over the chunks and run the rest of the workflow for each chunk of text:</p>
<pre><code class="language-js">export class RAGWorkflow extends WorkflowEntrypoint {&#10;	async run(event, step) {&#10;		const env = this.env;&#10;		const { text } = event.payload;&#10;		let texts = await step.do(&quot;split text&quot;, async () =&gt; {&#10;			const splitter = new RecursiveCharacterTextSplitter();&#10;			const output = await splitter.createDocuments([text]);&#10;			return output.map((doc) =&gt; doc.pageContent);&#10;		});&#10;&#10;		console.log(&#10;			&quot;RecursiveCharacterTextSplitter generated ${texts.length} chunks&quot;,&#10;		);&#10;&#10;		for (const index in texts) {&#10;			const text = texts[index];&#10;			const record = await step.do(&#10;				`create database record: ${index}/${texts.length}`,&#10;				async () =&gt; {&#10;					const query = &quot;INSERT INTO notes (text) VALUES (?) RETURNING *&quot;;&#10;&#10;					const { results } = await env.DB.prepare(query).bind(text).run();&#10;&#10;					const record = results[0];&#10;					if (!record) throw new Error(&quot;Failed to create note&quot;);&#10;					return record;&#10;				},&#10;			);&#10;&#10;			const embedding = await step.do(&#10;				`generate embedding: ${index}/${texts.length}`,&#10;				async () =&gt; {&#10;					const embeddings = await env.AI.run(&quot;@cf/baai/bge-base-en-v1.5&quot;, {&#10;						text: text,&#10;					});&#10;					const values = embeddings.data[0];&#10;					if (!values) throw new Error(&quot;Failed to generate vector embedding&quot;);&#10;					return values;&#10;				},&#10;			);&#10;&#10;			await step.do(`insert vector: ${index}/${texts.length}`, async () =&gt; {&#10;				return env.VECTOR_INDEX.upsert([&#10;					{&#10;						id: record.id.toString(),&#10;						values: embedding,&#10;					},&#10;				]);&#10;			});&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Now, when large pieces of text are submitted to the <code>/notes</code> endpoint, they will be split into smaller chunks, and each chunk will be processed by the workflow.</p>
<h2 id="11-deploy-your-project"><ol start="11">
<li>Deploy your project</li>
</ol></h2>
<p>If you did not deploy your Worker during <a href="/workers/get-started/guide/#1-create-a-new-worker-project">step 1</a>, deploy your Worker via Wrangler, to a <code>*.workers.dev</code> subdomain, or a <a href="/workers/configuration/routing/custom-domains/">Custom Domain</a>, if you have one configured. If you have not configured any subdomain or domain, Wrangler will prompt you during the publish process to set one up.</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Preview your Worker at <code>&lt;YOUR_WORKER&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/15849.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<p>A full version of this codebase is available on GitHub. It includes a frontend UI for querying, adding, and deleting notes, as well as a backend API for interacting with the database and vector index. You can find it here: <a href="https://github.com/kristianfreeman/cloudflare-retrieval-augmented-generation-example/">github.com/kristianfreeman/cloudflare-retrieval-augmented-generation-example</a>.</p>
<p>To do more:</p>
<ul>
<li>Explore the reference diagram for a <a href="/reference-architecture/diagrams/ai/ai-rag/">Retrieval Augmented Generation (RAG) Architecture</a>.</li>
<li>Review Cloudflare's <a href="/workers-ai">AI documentation</a>.</li>
<li>Review <a href="/workers/tutorials/">Tutorials</a> to build projects on Workers.</li>
<li>Explore <a href="/workers/examples/">Examples</a> to experiment with copy and paste Worker code.</li>
<li>Understand how Workers works in <a href="/workers/reference/">Reference</a>.</li>
<li>Learn about Workers features and functionality in <a href="/workers/platform/">Platform</a>.</li>
<li>Set up <a href="/workers/wrangler/install-and-update/">Wrangler</a> to programmatically create, test, and deploy your Worker projects.</li>
</ul>
