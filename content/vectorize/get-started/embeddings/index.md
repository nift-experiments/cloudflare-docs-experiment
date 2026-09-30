---
cp9:
  canonical: https://developers.cloudflare.com/vectorize/get-started/embeddings/
  description: Generate vector embeddings with Workers AI and store them in a Vectorize index.
  full_title: Vectorize and Workers AI · Cloudflare Vectorize docs
  head_html: <title>Vectorize and Workers AI · Cloudflare Vectorize docs</title><meta name="generator" content="Nift"><meta name="description" content="Generate vector embeddings with Workers AI and store them in a Vectorize index."><link rel="canonical" href="https://developers.cloudflare.com/vectorize/get-started/embeddings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/vectorize/get-started/embeddings/index.md"><meta property="og:title" content="Vectorize and Workers AI · Cloudflare Vectorize docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Generate vector embeddings with Workers AI and store them in a Vectorize index."><meta property="og:url" content="https://developers.cloudflare.com/vectorize/get-started/embeddings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Vectorize"><meta name="algolia_product_filter" content="Vectorize"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Vectorize,Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/vectorize/get-started/embeddings/#page","headline":"Vectorize and Workers AI \u00b7 Cloudflare Vectorize docs","description":"Generate vector embeddings with Workers AI and store them in a Vectorize index.","url":"https://developers.cloudflare.com/vectorize/get-started/embeddings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /vectorize/get-started/embeddings/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="vectorize-is-now-generally-available">Vectorize is now Generally Available</h3>
@markup("md", "content/.markup/bodies/15276.md")
</aside>
<p>Vectorize allows you to generate <a href="/vectorize/reference/what-is-a-vector-database/">vector embeddings</a> using a machine-learning model, including the models available in <a href="/workers-ai/">Workers AI</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="new-to-vectorize">New to Vectorize?</h3>
@markup("md", "content/.markup/bodies/15275.md")
</aside>
<p>This guide will instruct you through:</p>
<ul>
<li>Creating a Vectorize index.</li>
<li>Connecting a <a href="/workers/">Cloudflare Worker</a> to your index.</li>
<li>Using <a href="/workers-ai/">Workers AI</a> to generate vector embeddings.</li>
<li>Using Vectorize to query those vector embeddings.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<p>To continue:</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a> if you have not already.</li>
<li>Install <a href="https://docs.npmjs.com/getting-started"><code>npm</code></a>.</li>
<li>Install <a href="https://nodejs.org/en/"><code>Node.js</code></a>. Use a Node version manager like <a href="https://volta.sh/">Volta</a> or <a href="https://github.com/nvm-sh/nvm">nvm</a> to avoid permission issues and change Node.js versions. <a href="/workers/wrangler/install-and-update/">Wrangler</a> requires a Node version of <code>16.17.0</code> or later.</li>
</ol>
<h2 id="1-create-a-worker"><ol>
<li>Create a Worker</li>
</ol></h2>
<p>You will create a new project that will contain a Worker script, which will act as the client application for your Vectorize index.</p>
<p>Open your terminal and create a new project named <code>embeddings-tutorial</code> by running the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- embeddings-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- embeddings-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare embeddings-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare embeddings-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest embeddings-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest embeddings-tutorial" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>This will create a new <code>embeddings-tutorial</code> directory. Your new <code>embeddings-tutorial</code> directory will include:</p>
<ul>
<li>A <code>&quot;Hello World&quot;</code> <a href="/workers/get-started/guide/#3-write-code">Worker</a> at <code>src/index.ts</code>.</li>
<li>A <a href="/workers/wrangler/configuration/"><code>wrangler.jsonc</code></a> configuration file. <code>wrangler.jsonc</code> is how your <code>embeddings-tutorial</code> Worker will access your index.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15274.md")
</aside>
<h2 id="2-create-an-index"><ol start="2">
<li>Create an index</li>
</ol></h2>
<p>A vector database is distinct from a traditional SQL or NoSQL database. A vector database is designed to store vector embeddings, which are representations of data, but not the original data itself.</p>
<p>To create your first Vectorize index, change into the directory you just created for your Workers project:</p>
<pre tabindex="0"><code class="language-sh">cd embeddings-tutorial&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="using-legacy-vectorize-v1-indexes">Using legacy Vectorize (V1) indexes?</h3>
@markup("md", "content/.markup/bodies/15273.md")
</aside>
<p>To create an index, use the <code>wrangler vectorize create</code> command and provide a name for the index. A good index name is:</p>
<ul>
<li>A combination of lowercase and/or numeric ASCII characters, shorter than 32 characters, starts with a letter, and uses dashes (-) instead of spaces.</li>
<li>Descriptive of the use-case and environment. For example, &quot;production-doc-search&quot; or &quot;dev-recommendation-engine&quot;.</li>
<li>Only used for describing the index, and is not directly referenced in code.</li>
</ul>
<p>In addition, define both the <code>dimensions</code> of the vectors you will store in the index, as well as the distance <code>metric</code> used to determine similar vectors when creating the index. <strong>This configuration cannot be changed later</strong>, as a vector database is configured for a fixed vector configuration.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wrangler-version-3-71-0-required">Wrangler version 3.71.0 required</h3>
@markup("md", "content/.markup/bodies/15272.md")
</aside>
<p>Run the following <code>wrangler vectorize</code> command, ensuring that the <code>dimensions</code> are set to <code>768</code>: this is important, as the Workers AI model used in this tutorial outputs vectors with 768 dimensions.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler vectorize create embeddings-index --dimensions=768 --metric=cosine&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">✅ Successfully created index &#x27;embeddings-index&#x27;&#10;&#10;[[vectorize]]&#10;binding = &quot;VECTORIZE&quot; # available in your Worker on env.VECTORIZE&#10;index_name = &quot;embeddings-index&quot;&#10;</code></pre>
<p>This will create a new vector database, and output the <a href="/workers/runtime-apis/bindings/">binding</a> configuration needed in the next step.</p>
<h2 id="3-bind-your-worker-to-your-index"><ol start="3">
<li>Bind your Worker to your index</li>
</ol></h2>
<p>You must create a binding for your Worker to connect to your Vectorize index. <a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to access resources, like Vectorize or R2, from Cloudflare Workers. You create bindings by updating your Wrangler file.</p>
<p>To bind your index to your Worker, add the following to the end of your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15277.md")
</div>
<p>Specifically:</p>
<ul>
<li>The value (string) you set for <code>&lt;BINDING_NAME&gt;</code> will be used to reference this database in your Worker. In this tutorial, name your binding <code>VECTORIZE</code>.</li>
<li>The binding must be <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables">a valid JavaScript variable name</a>. For example, <code>binding = &quot;MY_INDEX&quot;</code> or <code>binding = &quot;PROD_SEARCH_INDEX&quot;</code> would both be valid names for the binding.</li>
<li>Your binding is available in your Worker at <code>env.&lt;BINDING_NAME&gt;</code> and the Vectorize <a href="/vectorize/reference/client-api/">client API</a> is exposed on this binding for use within your Workers application.</li>
</ul>
<h2 id="4-set-up-workers-ai"><ol start="4">
<li>Set up Workers AI</li>
</ol></h2>
<p>Before you deploy your embedding example, ensure your Worker uses your model catalog, including the <a href="/workers-ai/models/?tasks=Text+Embeddings">text embedding model</a> built-in.</p>
<p>From within the <code>embeddings-tutorial</code> directory, open your Wrangler file in your editor and add the new <code>[[ai]]</code> binding to make Workers AI's models available in your Worker:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15278.md")
</div>
<p>With Workers AI ready, you can write code in your Worker.</p>
<h2 id="5-write-code-in-your-worker"><ol start="5">
<li>Write code in your Worker</li>
</ol></h2>
<p>To write code in your Worker, go to your <code>embeddings-tutorial</code> Worker and open the <code>src/index.ts</code> file. The <code>index.ts</code> file is where you configure your Worker's interactions with your Vectorize index.</p>
<p>Clear the content of <code>index.ts</code>. Paste the following code snippet into your <code>index.ts</code> file. On the <code>env</code> parameter, replace <code>&lt;BINDING_NAME&gt;</code> with <code>VECTORIZE</code>:</p>
<pre tabindex="0"><code class="language-typescript">export interface Env {&#10;	VECTORIZE: Vectorize;&#10;	AI: Ai;&#10;}&#10;interface EmbeddingResponse {&#10;	shape: number[];&#10;	data: number[][];&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		let path = new URL(request.url).pathname;&#10;		if (path.startsWith(&quot;/favicon&quot;)) {&#10;			return new Response(&quot;&quot;, { status: 404 });&#10;		}&#10;&#10;		// You only need to generate vector embeddings once (or as&#10;		// data changes), not on every request&#10;		if (path === &quot;/insert&quot;) {&#10;			// In a real-world application, you could read content from R2 or&#10;			// a SQL database (like D1) and pass it to Workers AI&#10;			const stories = [&#10;				&quot;This is a story about an orange cloud&quot;,&#10;				&quot;This is a story about a llama&quot;,&#10;				&quot;This is a story about a hugging emoji&quot;,&#10;			];&#10;			const modelResp: EmbeddingResponse = await env.AI.run(&#10;				&quot;@cf/baai/bge-base-en-v1.5&quot;,&#10;				{&#10;					text: stories,&#10;				},&#10;			);&#10;&#10;			// Convert the vector embeddings into a format Vectorize can accept.&#10;			// Each vector needs an ID, a value (the vector) and optional metadata.&#10;			// In a real application, your ID would be bound to the ID of the source&#10;			// document.&#10;			let vectors: VectorizeVector[] = [];&#10;			let id = 1;&#10;			modelResp.data.forEach((vector) =&gt; {&#10;				vectors.push({ id: `${id}`, values: vector });&#10;				id++;&#10;			});&#10;&#10;			let inserted = await env.VECTORIZE.upsert(vectors);&#10;			return Response.json(inserted);&#10;		}&#10;&#10;		// Your query: expect this to match vector ID. 1 in this example&#10;		let userQuery = &quot;orange cloud&quot;;&#10;		const queryVector: EmbeddingResponse = await env.AI.run(&#10;			&quot;@cf/baai/bge-base-en-v1.5&quot;,&#10;			{&#10;				text: [userQuery],&#10;			},&#10;		);&#10;&#10;		let matches = await env.VECTORIZE.query(queryVector.data[0], {&#10;			topK: 1,&#10;		});&#10;		return Response.json({&#10;			// Expect a vector ID. 1 to be your top match with a score of&#10;			// ~0.89693683&#10;			// This tutorial uses a cosine distance metric, where the closer to one,&#10;			// the more similar.&#10;			matches: matches,&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h2 id="6-deploy-your-worker"><ol start="6">
<li>Deploy your Worker</li>
</ol></h2>
<p>Before deploying your Worker globally, log in with your Cloudflare account by running:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login&#10;</code></pre>
<p>You will be directed to a web page asking you to log in to the Cloudflare dashboard. After you have logged in, you will be asked if Wrangler can make changes to your Cloudflare account. Scroll down and select <strong>Allow</strong> to continue.</p>
<p>From here, deploy your Worker to make your project accessible on the Internet. To deploy your Worker, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Preview your Worker at <code>https://embeddings-tutorial.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>.</p>
<h2 id="7-query-your-index"><ol start="7">
<li>Query your index</li>
</ol></h2>
<p>You can now visit the URL for your newly created project to insert vectors and then query them.</p>
<p>With the URL for your deployed Worker (for example,<code>https://embeddings-tutorial.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/</code>), open your browser and:</p>
<ol>
<li>Insert your vectors first by visiting <code>/insert</code>.</li>
<li>Query your index by visiting the index route - <code>/</code>.</li>
</ol>
<p>This should return the following JSON:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;matches&quot;: {&#10;		&quot;count&quot;: 1,&#10;		&quot;matches&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;1&quot;,&#10;				&quot;score&quot;: 0.89693683&#10;			}&#10;		]&#10;	}&#10;}&#10;</code></pre>
<p>Extend this example by:</p>
<ul>
<li>Adding more inputs and generating a larger set of vectors.</li>
<li>Accepting a custom query parameter passed in the URL, for example via <code>URL.searchParams</code>.</li>
<li>Creating a new index with a different <a href="/vectorize/best-practices/create-indexes/#distance-metrics">distance metric</a> and observing how your scores change in response to your inputs.</li>
</ul>
<p>By finishing this tutorial, you have successfully created a Vectorize index, used Workers AI to generate vector embeddings, and deployed your project globally.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Build a <a href="/workers-ai/guides/tutorials/build-a-retrieval-augmented-generation-ai/">generative AI chatbot</a> using Workers AI and Vectorize.</li>
<li>Learn more about <a href="/vectorize/reference/what-is-a-vector-database/">how vector databases work</a>.</li>
<li>Read <a href="/vectorize/reference/client-api/">examples</a> on how to use the Vectorize API from Cloudflare Workers.</li>
</ul>
