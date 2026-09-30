---
cp9:
  canonical: https://developers.cloudflare.com/workers/tutorials/create-finetuned-chatgpt-ai-models-with-r2/
  description: In this tutorial, you will use the OpenAI API and Cloudflare R2 to create a fine-tuned model.
  full_title: Create a fine-tuned OpenAI model with R2 · Cloudflare Workers docs
  head_html: <title>Create a fine-tuned OpenAI model with R2 · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="In this tutorial, you will use the OpenAI API and Cloudflare R2 to create a fine-tuned model."><link rel="canonical" href="https://developers.cloudflare.com/workers/tutorials/create-finetuned-chatgpt-ai-models-with-r2/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/tutorials/create-finetuned-chatgpt-ai-models-with-r2/index.md"><meta property="og:title" content="Create a fine-tuned OpenAI model with R2 · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="In this tutorial, you will use the OpenAI API and Cloudflare R2 to create a fine-tuned model."><meta property="og:url" content="https://developers.cloudflare.com/workers/tutorials/create-finetuned-chatgpt-ai-models-with-r2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="R2"><meta name="pcx_tags" content="AI,Hono,TypeScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/tutorials/create-finetuned-chatgpt-ai-models-with-r2/#page","headline":"Create a fine-tuned OpenAI model with R2 \u00b7 Cloudflare Workers docs","description":"In this tutorial, you will use the OpenAI API and Cloudflare R2 to create a fine-tuned model.","url":"https://developers.cloudflare.com/workers/tutorials/create-finetuned-chatgpt-ai-models-with-r2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI","Hono","TypeScript"]}</script>
  markdown: true
  noindex: false
  route: /workers/tutorials/create-finetuned-chatgpt-ai-models-with-r2/
  schema: 1
---
<p>In this tutorial, you will use the <a href="https://openai.com">OpenAI</a> API and <a href="/r2">Cloudflare R2</a> to create a <a href="https://platform.openai.com/docs/guides/fine-tuning">fine-tuned model</a>.</p>
<p>This feature in OpenAI's API allows you to derive a custom model from OpenAI's various large language models based on a set of custom instructions and example answers. These instructions and example answers are written in a document, known as a fine-tune document. This document will be stored in R2 and dynamically provided to OpenAI's APIs when creating a new fine-tune model.</p>
<p>In order to use this feature, you will do the following tasks:</p>
<ol>
<li>Upload a fine-tune document to R2.</li>
<li>Read the R2 file and upload it to OpenAI.</li>
<li>Create a new fine-tuned model based on the document.</li>
</ol>
<p><img src="/assets/upstream/images/workers/tutorials/finetune/finetune-example.png" alt="Demo" /></p>
<p>To review the completed code for this application, refer to the <a href="https://github.com/kristianfreeman/openai-finetune-r2-example">GitHub repository for this tutorial</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you start, make sure you have:</p>
<ul>
<li>A Cloudflare account with access to R2. If you do not have a Cloudflare account, <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">sign up</a> before continuing. Then purchase R2 from your Cloudflare dashboard.</li>
<li>An OpenAI API key.</li>
<li>A fine-tune document, structured as <a href="https://jsonlines.org/">JSON Lines</a>. Use the <a href="https://github.com/kristianfreeman/openai-finetune-r2-example/blob/16ca53ca9c8589834abe317487eeedb8a24c7643/example_data.jsonl">example document</a> in the source code.</li>
</ul>
<h2 id="1-create-a-worker-application"><ol>
<li>Create a Worker application</li>
</ol></h2>
<p>First, use the <code>c3</code> CLI to create a new Cloudflare Workers project.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- finetune-chatgpt-model</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- finetune-chatgpt-model" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare finetune-chatgpt-model</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare finetune-chatgpt-model" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest finetune-chatgpt-model</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest finetune-chatgpt-model" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>The above options will create the &quot;Hello World&quot; TypeScript project.</p>
<p>Move into your newly created directory:</p>
<pre tabindex="0"><code class="language-sh">cd finetune-chatgpt-model&#10;</code></pre>
<h2 id="2-upload-a-fine-tune-document-to-r2"><ol start="2">
<li>Upload a fine-tune document to R2</li>
</ol></h2>
<p>Next, upload the fine-tune document to R2. R2 is a key-value store that allows you to store and retrieve files from within your Workers application. You will use <a href="/workers/wrangler">Wrangler</a> to create a new R2 bucket.</p>
<p>To create a new R2 bucket use the <a href="/workers/wrangler/commands/r2/#r2-bucket-create"><code>wrangler r2 bucket create</code></a> command. Note that you are logged in with your Cloudflare account. If not logged in via Wrangler, use the <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a> command.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket create &lt;BUCKET_NAME&gt;&#10;</code></pre>
<p>Replace <code>&lt;BUCKET_NAME&gt;</code> with your desired bucket name. Note that bucket names must be lowercase and can only contain dashes.</p>
<p>Next, upload a file using the <a href="/workers/wrangler/commands/r2/#r2-object-put"><code>wrangler r2 object put</code></a> command.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 object put &lt;PATH&gt; -f &lt;FILE_NAME&gt;&#10;</code></pre>
<p><code>&lt;PATH&gt;</code> is the combined bucket and file path of the file you want to upload -- for example, <code>fine-tune-ai/finetune.jsonl</code>, where <code>fine-tune-ai</code> is the bucket name. Replace <code>&lt;FILE_NAME&gt;</code> with the local filename of your fine-tune document.</p>
<h2 id="3-bind-your-bucket-to-the-worker"><ol start="3">
<li>Bind your bucket to the Worker</li>
</ol></h2>
<p>A binding is how your Worker interacts with external resources such as the R2 bucket.</p>
<p>To bind the R2 bucket to your Worker, add the following to your Wrangler file. Update the binding property to a valid JavaScript variable identifier. Replace <code>&lt;YOUR_BUCKET_NAME&gt;</code> with the name of the bucket you created in <a href="#2-upload-a-fine-tune-document-to-r2">step 2</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16078.md")
</div>
<h2 id="4-initialize-your-worker-application"><ol start="4">
<li>Initialize your Worker application</li>
</ol></h2>
<p>You will use <a href="https://hono.dev/">Hono</a>, a lightweight framework for building Cloudflare Workers applications. Hono provides an interface for defining routes and middleware functions. Inside your project directory, run the following command to install Hono:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i hono" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add hono" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add hono" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add hono" aria-label="Copy to clipboard">Copy</button></div></div>
<p>You also need to install the <a href="https://www.npmjs.com/package/openai">OpenAI Node API library</a>. This library provides convenient access to the OpenAI REST API in a Node.js project. To install the library, execute the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i openai</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i openai" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add openai</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add openai" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add openai</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add openai" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add openai</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add openai" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Next, open the <code>src/index.ts</code> file and replace the default code with the below code. Replace <code>&lt;MY_BUCKET&gt;</code> with the binding name you set in Wrangler file.</p>
<pre tabindex="0"><code class="language-typescript">import { Context, Hono } from &quot;hono&quot;;&#10;import OpenAI from &quot;openai&quot;;&#10;&#10;type Bindings = {&#10;	&lt;MY_BUCKET&gt;: R2Bucket&#10;	OPENAI_API_KEY: string&#10;}&#10;&#10;type Variables = {&#10;	openai: OpenAI&#10;}&#10;&#10;const app = new Hono&lt;{ Bindings: Bindings, Variables: Variables }&gt;()&#10;&#10;app.use(&#x27;*&#x27;, async (c, next) =&gt; {&#10;	const openai = new OpenAI({&#10;		apiKey: c.env.OPENAI_API_KEY,&#10;	})&#10;	c.set(&quot;openai&quot;, openai)&#10;	await next()&#10;})&#10;&#10;app.onError((err, c) =&gt; {&#10;	return c.text(err.message, 500)&#10;})&#10;&#10;export default app;&#10;</code></pre>
<p>In the above code, you first import the required packages and define the types. Then, you initialize <code>app</code> as a new Hono instance. Using the <code>use</code> middleware function, you add the OpenAI API client to the context of all routes. This middleware function allows you to access the client from within any route handler. <code>onError()</code> defines an error handler to return any errors as a JSON response.</p>
<h2 id="5-read-r2-files-and-upload-them-to-openai"><ol start="5">
<li>Read R2 files and upload them to OpenAI</li>
</ol></h2>
<p>In this section, you will define the route and function responsible for handling file uploads.</p>
<p>In <code>createFile</code>, your Worker reads the file from R2 and converts it to a <code>File</code> object. Your Worker then uses the OpenAI API to upload the file and return the response.</p>
<p>The <code>GET /files</code> route listens for <code>GET</code> requests with a query parameter <code>file</code>, representing a filename of an uploaded fine-tune document in R2. The function uses the <code>createFile</code> function to manage the file upload process.</p>
<p>Replace <code>&lt;MY_BUCKET&gt;</code> with the binding name you set in Wrangler file.</p>
<pre tabindex="0"><code class="language-typescript">// New import added at beginning of file&#10;import { toFile } from &#x27;openai/uploads&#x27;&#10;&#10;const createFile = async (c: Context, r2Object: R2ObjectBody) =&gt; {&#10;	const openai: OpenAI = c.get(&quot;openai&quot;)&#10;&#10;	const blob = await r2Object.blob()&#10;	const file = await toFile(blob, r2Object.key)&#10;&#10;	const uploadedFile = await openai.files.create({&#10;		file,&#10;		purpose: &quot;fine-tune&quot;,&#10;	})&#10;&#10;	return uploadedFile&#10;}&#10;&#10;app.get(&#x27;/files&#x27;, async c =&gt; {&#10;	const fileQueryParam = c.req.query(&quot;file&quot;)&#10;	if (!fileQueryParam) return c.text(&quot;Missing file query param&quot;, 400)&#10;&#10;	const file = await c.env.&lt;MY_BUCKET&gt;.get(fileQueryParam)&#10;	if (!file) return c.text(&quot;Couldn&#x27;t find file&quot;, 400)&#10;&#10;	const uploadedFile = await createFile(c, file)&#10;	return c.json(uploadedFile)&#10;})&#10;</code></pre>
<h2 id="6-create-fine-tuned-models"><ol start="6">
<li>Create fine-tuned models</li>
</ol></h2>
<p>This section includes the <code>GET /models</code> route and the <code>createModel</code> function. The function <code>createModel</code> takes care of specifying the details and initiating the fine-tuning process with OpenAI. The route handles incoming requests for creating a new fine-tuned model.</p>
<pre tabindex="0"><code class="language-typescript">const createModel = async (c: Context, fileId: string) =&gt; {&#10;	const openai: OpenAI = c.get(&quot;openai&quot;);&#10;&#10;	const body = {&#10;		training_file: fileId,&#10;		model: &quot;gpt-4o-mini&quot;,&#10;	};&#10;&#10;	return openai.fineTuning.jobs.create(body);&#10;};&#10;&#10;app.get(&quot;/models&quot;, async (c) =&gt; {&#10;	const fileId = c.req.query(&quot;file_id&quot;);&#10;	if (!fileId) return c.text(&quot;Missing file ID query param&quot;, 400);&#10;&#10;	const model = await createModel(c, fileId);&#10;	return c.json(model);&#10;});&#10;</code></pre>
<h2 id="7-list-all-fine-tune-jobs"><ol start="7">
<li>List all fine-tune jobs</li>
</ol></h2>
<p>This section describes the <code>GET /jobs</code> route and the corresponding <code>getJobs</code> function. The function interacts with OpenAI's API to fetch a list of all fine-tuning jobs. The route provides an interface for retrieving this information.</p>
<pre tabindex="0"><code class="language-typescript">const getJobs = async (c: Context) =&gt; {&#10;	const openai: OpenAI = c.get(&quot;openai&quot;);&#10;	const resp = await openai.fineTuning.jobs.list();&#10;	return resp.data;&#10;};&#10;&#10;app.get(&quot;/jobs&quot;, async (c) =&gt; {&#10;	const jobs = await getJobs(c);&#10;	return c.json(jobs);&#10;});&#10;</code></pre>
<h2 id="8-deploy-your-application"><ol start="8">
<li>Deploy your application</li>
</ol></h2>
<p>After you have created your Worker application and added the required functions, deploy the application.</p>
<p>Before you deploy, you must set the <code>OPENAI_API_KEY</code> <a href="/workers/configuration/secrets/">secret</a> for your application. Do this by running the <a href="/workers/wrangler/commands/general/#secret-put"><code>wrangler secret put</code></a> command:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler secret put OPENAI_API_KEY&#10;</code></pre>
<p>To deploy your Worker application to the Cloudflare global network:</p>
<ol>
<li>Make sure you are in your Worker project's directory, then run the <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> command:</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<ol start="2">
<li>
<p>Wrangler will package and upload your code.</p>
</li>
<li>
<p>After your application is deployed, Wrangler will provide you with your Worker's URL.</p>
</li>
</ol>
<h2 id="9-view-the-fine-tune-job-status-and-use-the-model"><ol start="9">
<li>View the fine-tune job status and use the model</li>
</ol></h2>
<p>To use your application, create a new fine-tune job by making a request to the <code>/files</code> with a <code>file</code> query param matching the filename you uploaded earlier:</p>
<pre tabindex="0"><code class="language-sh">curl https://your-worker-url.com/files?file=finetune.jsonl&#10;</code></pre>
<p>When the file is uploaded, issue another request to <code>/models</code>, passing the <code>file_id</code> query parameter. This should match the <code>id</code> returned as JSON from the <code>/files</code> route:</p>
<pre tabindex="0"><code class="language-sh">curl https://your-worker-url.com/models?file_id=file-abc123&#10;</code></pre>
<p>Finally, visit <code>/jobs</code> to see the status of your fine-tune jobs in OpenAI. Once the fine-tune job has completed, you can see the <code>fine_tuned_model</code> value, indicating a fine-tuned model has been created.</p>
<p><img src="/assets/upstream/images/workers/tutorials/finetune/finetune-jobs.png" alt="Jobs" /></p>
<p>Visit the <a href="https://platform.openai.com/playground">OpenAI Playground</a> in order to use your fine-tune model. Select your fine-tune model from the top-left dropdown of the interface.</p>
<p><img src="/assets/upstream/images/workers/tutorials/finetune/finetune-example.png" alt="Demo" /></p>
<p>Use it in any API requests you make to OpenAI's chat completions endpoints. For instance, in the below code example:</p>
<pre tabindex="0"><code class="language-javascript">openai.chat.completions.create({&#10;	messages: [{ role: &quot;system&quot;, content: &quot;You are a helpful assistant.&quot; }],&#10;	model: &quot;ft:gpt-4o-mini:my-org:custom_suffix:id&quot;,&#10;});&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>To build more with Workers, refer to <a href="/workers/tutorials">Tutorials</a>.</p>
<p>If you have any questions, need assistance, or would like to share your project, join the Cloudflare Developer community on <a href="https://discord.cloudflare.com">Discord</a> to connect with other developers and the Cloudflare team.</p>
