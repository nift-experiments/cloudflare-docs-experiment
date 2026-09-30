<aside class="nb-aside note">
<h3 class="nb-aside-title" id="vectorize-is-now-generally-available">Vectorize is now Generally Available</h3>
@markup("md", "content/.markup/bodies/15270.md")
</aside>
<p>Vectorize is Cloudflare's vector database. Vector databases allow you to use machine learning (ML) models to perform semantic search, recommendation, classification and anomaly detection tasks, as well as provide context to LLMs (Large Language Models).</p>
<p>This guide will instruct you through:</p>
<ul>
<li>Creating your first Vectorize index.</li>
<li>Connecting a <a href="/workers/">Cloudflare Worker</a> to your index.</li>
<li>Inserting and performing a similarity search by querying your index.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-free-or-paid-plans-required">Workers Free or Paid plans required</h3>
@markup("md", "content/.markup/bodies/15269.md")
</aside>
<p>To continue, you will need:</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a> if you have not already.</li>
<li>Install <a href="https://docs.npmjs.com/getting-started"><code>npm</code></a>.</li>
<li>Install <a href="https://nodejs.org/en/"><code>Node.js</code></a>. Use a Node version manager like <a href="https://volta.sh/">Volta</a> or <a href="https://github.com/nvm-sh/nvm">nvm</a> to avoid permission issues and change Node.js versions. <a href="/workers/wrangler/install-and-update/">Wrangler</a> requires a Node version of <code>16.17.0</code> or later.</li>
</ol>
<h2 id="1-create-a-worker"><ol>
<li>Create a Worker</li>
</ol></h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="new-to-workers">New to Workers?</h3>
@markup("md", "content/.markup/bodies/15268.md")
</aside>
<p>You will create a new project that will contain a Worker, which will act as the client application for your Vectorize index.</p>
<p>Create a new project named <code>vectorize-tutorial</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- vectorize-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- vectorize-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare vectorize-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare vectorize-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest vectorize-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest vectorize-tutorial" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>This will create a new <code>vectorize-tutorial</code> directory. Your new <code>vectorize-tutorial</code> directory will include:</p>
<ul>
<li>A <code>&quot;Hello World&quot;</code> <a href="/workers/get-started/guide/#3-write-code">Worker</a> at <code>src/index.ts</code>.</li>
<li>A <a href="/workers/wrangler/configuration/"><code>wrangler.jsonc</code></a> configuration file. <code>wrangler.jsonc</code> is how your <code>vectorize-tutorial</code> Worker will access your index.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15267.md")
</aside>
<h2 id="2-create-an-index"><ol start="2">
<li>Create an index</li>
</ol></h2>
<p>A vector database is distinct from a traditional SQL or NoSQL database. A vector database is designed to store vector embeddings, which are representations of data, but not the original data itself.</p>
<p>To create your first Vectorize index, change into the directory you just created for your Workers project:</p>
<pre><code class="language-sh">cd vectorize-tutorial&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="using-legacy-vectorize-v1-indexes">Using legacy Vectorize (V1) indexes?</h3>
@markup("md", "content/.markup/bodies/15266.md")
</aside>
<p>To create an index, you will need to use the <code>wrangler vectorize create</code> command and provide a name for the index. A good index name is:</p>
<ul>
<li>A combination of lowercase and/or numeric ASCII characters, shorter than 32 characters, starts with a letter, and uses dashes (-) instead of spaces.</li>
<li>Descriptive of the use-case and environment. For example, &quot;production-doc-search&quot; or &quot;dev-recommendation-engine&quot;.</li>
<li>Only used for describing the index, and is not directly referenced in code.</li>
</ul>
<p>In addition, you will need to define both the <code>dimensions</code> of the vectors you will store in the index, as well as the distance <code>metric</code> used to determine similar vectors when creating the index. A <code>metric</code> can be euclidean, cosine, or dot product. <strong>This configuration cannot be changed later</strong>, as a vector database is configured for a fixed vector configuration.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wrangler-version-3-71-0-required">Wrangler version 3.71.0 required</h3>
@markup("md", "content/.markup/bodies/15265.md")
</aside>
<p>Run the following <code>wrangler vectorize</code> command:</p>
<pre><code class="language-sh">npx wrangler vectorize create tutorial-index --dimensions=32 --metric=euclidean&#10;</code></pre>
<pre><code class="language-sh">🚧 Creating index: &#x27;tutorial-index&#x27;&#10;✅ Successfully created a new Vectorize index: &#x27;tutorial-index&#x27;&#10;📋 To start querying from a Worker, add the following binding configuration into &#x27;wrangler.toml&#x27;:&#10;&#10;[[vectorize]]&#10;binding = &quot;VECTORIZE&quot; # available in your Worker on env.VECTORIZE&#10;index_name = &quot;tutorial-index&quot;&#10;</code></pre>
<p>The command above will create a new vector database, and output the <a href="/workers/runtime-apis/bindings/">binding</a> configuration needed in the next step.</p>
<h2 id="3-bind-your-worker-to-your-index"><ol start="3">
<li>Bind your Worker to your index</li>
</ol></h2>
<p>You must create a binding for your Worker to connect to your Vectorize index. <a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to access resources, like Vectorize or R2, from Cloudflare Workers. You create bindings by updating the worker's Wrangler file.</p>
<p>To bind your index to your Worker, add the following to the end of your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15271.md")
</div>
<p>Specifically:</p>
<ul>
<li>The value (string) you set for <code>&lt;BINDING_NAME&gt;</code> will be used to reference this database in your Worker. In this tutorial, name your binding <code>VECTORIZE</code>.</li>
<li>The binding must be <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables">a valid JavaScript variable name</a>. For example, <code>binding = &quot;MY_INDEX&quot;</code> or <code>binding = &quot;PROD_SEARCH_INDEX&quot;</code> would both be valid names for the binding.</li>
<li>Your binding is available in your Worker at <code>env.&lt;BINDING_NAME&gt;</code> and the Vectorize <a href="/vectorize/reference/client-api/">client API</a> is exposed on this binding for use within your Workers application.</li>
</ul>
<h2 id="4-optional-create-metadata-indexes"><ol start="4">
<li>[Optional] Create metadata indexes</li>
</ol></h2>
<p>Vectorize allows you to add up to 10KiB of metadata per vector into your index, and also provides the ability to filter on that metadata while querying vectors. To do so you would need to specify a metadata field as a &quot;metadata index&quot; for your Vectorize index.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="when-to-create-metadata-indexes">When to create metadata indexes?</h3>
@markup("md", "content/.markup/bodies/15264.md")
</aside>
<p>To enable vector filtering on a metadata field during a query, use a command like:</p>
<pre><code class="language-sh">npx wrangler vectorize create-metadata-index tutorial-index --property-name=url --type=string&#10;</code></pre>
<pre><code class="language-sh">📋 Creating metadata index...&#10;✅ Successfully enqueued metadata index creation request. Mutation changeset identifier: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.&#10;</code></pre>
<p>Here <code>url</code> is the metadata field on which filtering would be enabled. The <code>--type</code> parameter defines the data type for the metadata field; <code>string</code>, <code>number</code> and <code>boolean</code> types are supported.</p>
<p>It typically takes a few seconds for the metadata index to be created. You can check the list of metadata indexes for your Vectorize index by running:</p>
<pre><code class="language-sh">npx wrangler vectorize list-metadata-index tutorial-index&#10;</code></pre>
<pre><code class="language-sh">📋 Fetching metadata indexes...&#10;┌──────────────┬────────┐&#10;│ propertyName │ type   │&#10;├──────────────┼────────┤&#10;│ url          │ String │&#10;└──────────────┴────────┘&#10;</code></pre>
<p>You can create up to 10 metadata indexes per Vectorize index.</p>
<p>For metadata indexes of type <code>number</code>, the indexed number precision is that of float64.</p>
<p>For metadata indexes of type <code>string</code>, each vector indexes the first 64B of the string data truncated on UTF-8 character boundaries to the longest well-formed UTF-8 substring within that limit, so vectors are filterable on the first 64B of their value for each indexed property.</p>
<p>See <a href="/vectorize/platform/limits/">Vectorize Limits</a> for a complete list of limits.</p>
<h2 id="5-insert-vectors"><ol start="5">
<li>Insert vectors</li>
</ol></h2>
<p>Before you can query a vector database, you need to insert vectors for it to query against. These vectors would be generated from data (such as text or images) you pass to a machine learning model. However, this tutorial will define static vectors to illustrate how vector search works on its own.</p>
<p>First, go to your <code>vectorize-tutorial</code> Worker and open the <code>src/index.ts</code> file. The <code>index.ts</code> file is where you configure your Worker's interactions with your Vectorize index.</p>
<p>Clear the content of <code>index.ts</code>, and paste the following code snippet into your <code>index.ts</code> file. On the <code>env</code> parameter, replace <code>&lt;BINDING_NAME&gt;</code> with <code>VECTORIZE</code>:</p>
<pre><code class="language-typescript">export interface Env {&#10;	// This makes your vector index methods available on env.VECTORIZE.*&#10;	// For example, env.VECTORIZE.insert() or query()&#10;	VECTORIZE: Vectorize;&#10;}&#10;&#10;// Sample vectors: 32 dimensions wide.&#10;//&#10;// Vectors from popular machine-learning models are typically ~100 to 1536 dimensions&#10;// wide (or wider still).&#10;const sampleVectors: Array&lt;VectorizeVector&gt; = [&#10;	{&#10;		id: &quot;1&quot;,&#10;		values: [&#10;			0.12, 0.45, 0.67, 0.89, 0.23, 0.56, 0.34, 0.78, 0.12, 0.9, 0.24, 0.67,&#10;			0.89, 0.35, 0.48, 0.7, 0.22, 0.58, 0.74, 0.33, 0.88, 0.66, 0.45, 0.27,&#10;			0.81, 0.54, 0.39, 0.76, 0.41, 0.29, 0.83, 0.55,&#10;		],&#10;		metadata: { url: &quot;/products/sku/13913913&quot; },&#10;	},&#10;	{&#10;		id: &quot;2&quot;,&#10;		values: [&#10;			0.14, 0.23, 0.36, 0.51, 0.62, 0.47, 0.59, 0.74, 0.33, 0.89, 0.41, 0.53,&#10;			0.68, 0.29, 0.77, 0.45, 0.24, 0.66, 0.71, 0.34, 0.86, 0.57, 0.62, 0.48,&#10;			0.78, 0.52, 0.37, 0.61, 0.69, 0.28, 0.8, 0.53,&#10;		],&#10;		metadata: { url: &quot;/products/sku/10148191&quot; },&#10;	},&#10;	{&#10;		id: &quot;3&quot;,&#10;		values: [&#10;			0.21, 0.33, 0.55, 0.67, 0.8, 0.22, 0.47, 0.63, 0.31, 0.74, 0.35, 0.53,&#10;			0.68, 0.45, 0.55, 0.7, 0.28, 0.64, 0.71, 0.3, 0.77, 0.6, 0.43, 0.39, 0.85,&#10;			0.55, 0.31, 0.69, 0.52, 0.29, 0.72, 0.48,&#10;		],&#10;		metadata: { url: &quot;/products/sku/97913813&quot; },&#10;	},&#10;	{&#10;		id: &quot;4&quot;,&#10;		values: [&#10;			0.17, 0.29, 0.42, 0.57, 0.64, 0.38, 0.51, 0.72, 0.22, 0.85, 0.39, 0.66,&#10;			0.74, 0.32, 0.53, 0.48, 0.21, 0.69, 0.77, 0.34, 0.8, 0.55, 0.41, 0.29,&#10;			0.7, 0.62, 0.35, 0.68, 0.53, 0.3, 0.79, 0.49,&#10;		],&#10;		metadata: { url: &quot;/products/sku/418313&quot; },&#10;	},&#10;	{&#10;		id: &quot;5&quot;,&#10;		values: [&#10;			0.11, 0.46, 0.68, 0.82, 0.27, 0.57, 0.39, 0.75, 0.16, 0.92, 0.28, 0.61,&#10;			0.85, 0.4, 0.49, 0.67, 0.19, 0.58, 0.76, 0.37, 0.83, 0.64, 0.53, 0.3,&#10;			0.77, 0.54, 0.43, 0.71, 0.36, 0.26, 0.8, 0.53,&#10;		],&#10;		metadata: { url: &quot;/products/sku/55519183&quot; },&#10;	},&#10;];&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		let path = new URL(request.url).pathname;&#10;		if (path.startsWith(&quot;/favicon&quot;)) {&#10;			return new Response(&quot;&quot;, { status: 404 });&#10;		}&#10;&#10;		// You only need to insert vectors into your index once&#10;		if (path.startsWith(&quot;/insert&quot;)) {&#10;			// Insert some sample vectors into your index&#10;			// In a real application, these vectors would be the output of a machine learning (ML) model,&#10;			// such as Workers AI, OpenAI, or Cohere.&#10;			const inserted = await env.VECTORIZE.insert(sampleVectors);&#10;&#10;			// Return the mutation identifier for this insert operation&#10;			return Response.json(inserted);&#10;		}&#10;&#10;		return Response.json({ text: &quot;nothing to do... yet&quot; }, { status: 404 });&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>In the code above, you:</p>
<ol>
<li>Define a binding to your Vectorize index from your Workers code. This binding matches the <code>binding</code> value you set in the <code>wrangler.jsonc</code> file under the <code>&quot;vectorise&quot;</code> key.</li>
<li>Specify a set of example vectors that you will query against in the next step.</li>
<li>Insert those vectors into the index and confirm it was successful.</li>
</ol>
<p>In the next step, you will expand the Worker to query the index and the vectors you insert.</p>
<h2 id="6-query-vectors"><ol start="6">
<li>Query vectors</li>
</ol></h2>
<p>In this step, you will take a vector representing an incoming query and use it to search your index.</p>
<p>First, go to your <code>vectorize-tutorial</code> Worker and open the <code>src/index.ts</code> file. The <code>index.ts</code> file is where you configure your Worker's interactions with your Vectorize index.</p>
<p>Clear the content of <code>index.ts</code>. Paste the following code snippet into your <code>index.ts</code> file. On the <code>env</code> parameter, replace <code>&lt;BINDING_NAME&gt;</code> with <code>VECTORIZE</code>:</p>
<pre><code class="language-typescript">export interface Env {&#10;	// This makes your vector index methods available on env.VECTORIZE.*&#10;	// For example, env.VECTORIZE.insert() or query()&#10;	VECTORIZE: Vectorize;&#10;}&#10;&#10;// Sample vectors: 32 dimensions wide.&#10;//&#10;// Vectors from popular machine-learning models are typically ~100 to 1536 dimensions&#10;// wide (or wider still).&#10;const sampleVectors: Array&lt;VectorizeVector&gt; = [&#10;	{&#10;		id: &quot;1&quot;,&#10;		values: [&#10;			0.12, 0.45, 0.67, 0.89, 0.23, 0.56, 0.34, 0.78, 0.12, 0.9, 0.24, 0.67,&#10;			0.89, 0.35, 0.48, 0.7, 0.22, 0.58, 0.74, 0.33, 0.88, 0.66, 0.45, 0.27,&#10;			0.81, 0.54, 0.39, 0.76, 0.41, 0.29, 0.83, 0.55,&#10;		],&#10;		metadata: { url: &quot;/products/sku/13913913&quot; },&#10;	},&#10;	{&#10;		id: &quot;2&quot;,&#10;		values: [&#10;			0.14, 0.23, 0.36, 0.51, 0.62, 0.47, 0.59, 0.74, 0.33, 0.89, 0.41, 0.53,&#10;			0.68, 0.29, 0.77, 0.45, 0.24, 0.66, 0.71, 0.34, 0.86, 0.57, 0.62, 0.48,&#10;			0.78, 0.52, 0.37, 0.61, 0.69, 0.28, 0.8, 0.53,&#10;		],&#10;		metadata: { url: &quot;/products/sku/10148191&quot; },&#10;	},&#10;	{&#10;		id: &quot;3&quot;,&#10;		values: [&#10;			0.21, 0.33, 0.55, 0.67, 0.8, 0.22, 0.47, 0.63, 0.31, 0.74, 0.35, 0.53,&#10;			0.68, 0.45, 0.55, 0.7, 0.28, 0.64, 0.71, 0.3, 0.77, 0.6, 0.43, 0.39, 0.85,&#10;			0.55, 0.31, 0.69, 0.52, 0.29, 0.72, 0.48,&#10;		],&#10;		metadata: { url: &quot;/products/sku/97913813&quot; },&#10;	},&#10;	{&#10;		id: &quot;4&quot;,&#10;		values: [&#10;			0.17, 0.29, 0.42, 0.57, 0.64, 0.38, 0.51, 0.72, 0.22, 0.85, 0.39, 0.66,&#10;			0.74, 0.32, 0.53, 0.48, 0.21, 0.69, 0.77, 0.34, 0.8, 0.55, 0.41, 0.29,&#10;			0.7, 0.62, 0.35, 0.68, 0.53, 0.3, 0.79, 0.49,&#10;		],&#10;		metadata: { url: &quot;/products/sku/418313&quot; },&#10;	},&#10;	{&#10;		id: &quot;5&quot;,&#10;		values: [&#10;			0.11, 0.46, 0.68, 0.82, 0.27, 0.57, 0.39, 0.75, 0.16, 0.92, 0.28, 0.61,&#10;			0.85, 0.4, 0.49, 0.67, 0.19, 0.58, 0.76, 0.37, 0.83, 0.64, 0.53, 0.3,&#10;			0.77, 0.54, 0.43, 0.71, 0.36, 0.26, 0.8, 0.53,&#10;		],&#10;		metadata: { url: &quot;/products/sku/55519183&quot; },&#10;	},&#10;];&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		let path = new URL(request.url).pathname;&#10;		if (path.startsWith(&quot;/favicon&quot;)) {&#10;			return new Response(&quot;&quot;, { status: 404 });&#10;		}&#10;&#10;		// You only need to insert vectors into your index once&#10;		if (path.startsWith(&quot;/insert&quot;)) {&#10;			// Insert some sample vectors into your index&#10;			// In a real application, these vectors would be the output of a machine learning (ML) model,&#10;			// such as Workers AI, OpenAI, or Cohere.&#10;			let inserted = await env.VECTORIZE.insert(sampleVectors);&#10;&#10;			// Return the mutation identifier for this insert operation&#10;			return Response.json(inserted);&#10;		}&#10;&#10;		// return Response.json({text: &quot;nothing to do... yet&quot;}, { status: 404 })&#10;&#10;		// In a real application, you would take a user query. For example, &quot;what is a&#10;		// vector database&quot; - and transform it into a vector embedding first.&#10;		//&#10;		// In this example, you will construct a vector that should&#10;		// match vector id #4&#10;		const queryVector: Array&lt;number&gt; = [&#10;			0.13, 0.25, 0.44, 0.53, 0.62, 0.41, 0.59, 0.68, 0.29, 0.82, 0.37, 0.5,&#10;			0.74, 0.46, 0.57, 0.64, 0.28, 0.61, 0.73, 0.35, 0.78, 0.58, 0.42, 0.32,&#10;			0.77, 0.65, 0.49, 0.54, 0.31, 0.29, 0.71, 0.57,&#10;		]; // vector of dimensions 32&#10;&#10;		// Query your index and return the three (topK = 3) most similar vector&#10;		// IDs with their similarity score.&#10;		//&#10;		// By default, vector values are not returned, as in many cases the&#10;		// vector id and scores are sufficient to map the vector back to the&#10;		// original content it represents.&#10;		const matches = await env.VECTORIZE.query(queryVector, {&#10;			topK: 3,&#10;			returnValues: true,&#10;			returnMetadata: &quot;all&quot;,&#10;		});&#10;&#10;		return Response.json({&#10;			// This will return the closest vectors: the vectors are arranged according&#10;			// to their scores. Vectors that are more similar would show up near the top.&#10;			// In this example, Vector id #4 would turn out to be the most similar to the queried vector.&#10;			// You return the full set of matches so you can check the possible scores.&#10;			matches: matches,&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>You can also use the Vectorize <code>queryById()</code> operation to search for vectors similar to a vector that is already present in the index.</p>
<h2 id="7-deploy-your-worker"><ol start="7">
<li>Deploy your Worker</li>
</ol></h2>
<p>Before deploying your Worker globally, log in with your Cloudflare account by running:</p>
<pre><code class="language-sh">npx wrangler login&#10;</code></pre>
<p>You will be directed to a web page asking you to log in to the Cloudflare dashboard. After you have logged in, you will be asked if Wrangler can make changes to your Cloudflare account. Scroll down and select <strong>Allow</strong> to continue.</p>
<p>From here, you can deploy your Worker to make your project accessible on the Internet. To deploy your Worker, run:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Once deployed, preview your Worker at <code>https://vectorize-tutorial.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>.</p>
<h2 id="8-query-your-index"><ol start="8">
<li>Query your index</li>
</ol></h2>
<p>To insert vectors and then query them, use the URL for your deployed Worker, such as <code>https://vectorize-tutorial.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/</code>. Open your browser and:</p>
<ol>
<li>Insert your vectors first by visiting <code>/insert</code>. This should return the below JSON:</li>
</ol>
<pre><code class="language-json">// https://vectorize-tutorial.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/insert&#10;{&#10;	&quot;mutationId&quot;: &quot;xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&quot;&#10;}&#10;</code></pre>
<p>The mutationId here refers to a unique identifier that corresponds to this asynchronous insert operation. Typically it takes a few seconds for inserted vectors to be available for querying.</p>
<p>You can use the index info operation to check the last processed mutation:</p>
<pre><code class="language-sh">npx wrangler vectorize info tutorial-index&#10;</code></pre>
<pre><code class="language-sh">📋 Fetching index info...&#10;┌────────────┬─────────────┬──────────────────────────────────────┬──────────────────────────┐&#10;│ dimensions │ vectorCount │ processedUpToMutation                │ processedUpToDatetime    │&#10;├────────────┼─────────────┼──────────────────────────────────────┼──────────────────────────┤&#10;│ 32         │ 5           │ xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx │ YYYY-MM-DDThh:mm:ss.SSSZ │&#10;└────────────┴─────────────┴──────────────────────────────────────┴──────────────────────────┘&#10;</code></pre>
<p>Subsequent inserts using the same vector ids will return a mutation id, but it would not change the index vector count since the same vector ids cannot be inserted twice. You will need to use an <code>upsert</code> operation instead to update the vector values for an id that already exists in an index.</p>
<ol start="2">
<li>Query your index - expect your query vector of <code>[0.13, 0.25, 0.44, ...]</code> to be closest to vector ID <code>4</code> by visiting the root path of <code>/</code> . This query will return the three (<code>topK: 3</code>) closest matches, as well as their vector values and metadata.</li>
</ol>
<p>You will notice that <code>id: 4</code> has a <code>score</code> of <code>0.46348256</code>. Because you are using <code>euclidean</code> as our distance metric, the closer the score to <code>0.0</code>, the closer your vectors are.</p>
<pre><code class="language-json">// https://vectorize-tutorial.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/&#10;{&#10;	&quot;matches&quot;: {&#10;		&quot;count&quot;: 3,&#10;		&quot;matches&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;4&quot;,&#10;				&quot;score&quot;: 0.46348256,&#10;				&quot;values&quot;: [&#10;					0.17, 0.29, 0.42, 0.57, 0.64, 0.38, 0.51, 0.72, 0.22, 0.85, 0.39,&#10;					0.66, 0.74, 0.32, 0.53, 0.48, 0.21, 0.69, 0.77, 0.34, 0.8, 0.55, 0.41,&#10;					0.29, 0.7, 0.62, 0.35, 0.68, 0.53, 0.3, 0.79, 0.49&#10;				],&#10;				&quot;metadata&quot;: {&#10;					&quot;url&quot;: &quot;/products/sku/418313&quot;&#10;				}&#10;			},&#10;			{&#10;				&quot;id&quot;: &quot;3&quot;,&#10;				&quot;score&quot;: 0.52920616,&#10;				&quot;values&quot;: [&#10;					0.21, 0.33, 0.55, 0.67, 0.8, 0.22, 0.47, 0.63, 0.31, 0.74, 0.35, 0.53,&#10;					0.68, 0.45, 0.55, 0.7, 0.28, 0.64, 0.71, 0.3, 0.77, 0.6, 0.43, 0.39,&#10;					0.85, 0.55, 0.31, 0.69, 0.52, 0.29, 0.72, 0.48&#10;				],&#10;				&quot;metadata&quot;: {&#10;					&quot;url&quot;: &quot;/products/sku/97913813&quot;&#10;				}&#10;			},&#10;			{&#10;				&quot;id&quot;: &quot;2&quot;,&#10;				&quot;score&quot;: 0.6337869,&#10;				&quot;values&quot;: [&#10;					0.14, 0.23, 0.36, 0.51, 0.62, 0.47, 0.59, 0.74, 0.33, 0.89, 0.41,&#10;					0.53, 0.68, 0.29, 0.77, 0.45, 0.24, 0.66, 0.71, 0.34, 0.86, 0.57,&#10;					0.62, 0.48, 0.78, 0.52, 0.37, 0.61, 0.69, 0.28, 0.8, 0.53&#10;				],&#10;				&quot;metadata&quot;: {&#10;					&quot;url&quot;: &quot;/products/sku/10148191&quot;&#10;				}&#10;			}&#10;		]&#10;	}&#10;}&#10;</code></pre>
<p>From here, experiment by passing a different <code>queryVector</code> and observe the results: the matches and the <code>score</code> should change based on the change in distance between the query vector and the vectors in our index.</p>
<p>In a real-world application, the <code>queryVector</code> would be the vector embedding representation of a query from a user or system, and our <code>sampleVectors</code> would be generated from real content. To build on this example, read the <a href="/vectorize/get-started/embeddings/">vector search tutorial</a> that combines Workers AI and Vectorize to build an end-to-end application with Workers.</p>
<p>By finishing this tutorial, you have successfully created and queried your first Vectorize index, a Worker to access that index, and deployed your project globally.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/vectorize/get-started/embeddings/">Build an end-to-end vector search application</a> using Workers AI and Vectorize.</li>
<li>Learn more about <a href="/vectorize/reference/what-is-a-vector-database/">how vector databases work</a>.</li>
<li>Read <a href="/vectorize/reference/client-api/">examples</a> on how to use the Vectorize API from Cloudflare Workers.</li>
<li><a href="https://www.baeldung.com/cs/euclidean-distance-vs-cosine-similarity">Euclidean Distance vs Cosine Similarity</a>.</li>
<li><a href="https://en.wikipedia.org/wiki/Dot_product">Dot product</a>.</li>
</ul>
