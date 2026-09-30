---
cp9:
  canonical: https://developers.cloudflare.com/r2/tutorials/summarize-pdf/
  description: Use event notification to summarize PDF files on upload. Use Workers AI to summarize the PDF and store the summary as a text file.
  full_title: Use event notification to summarize PDF files on upload · Cloudflare R2 docs
  head_html: <title>Use event notification to summarize PDF files on upload · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Use event notification to summarize PDF files on upload. Use Workers AI to summarize the PDF and store the summary as a text file."><link rel="canonical" href="https://developers.cloudflare.com/r2/tutorials/summarize-pdf/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/tutorials/summarize-pdf/index.md"><meta property="og:title" content="Use event notification to summarize PDF files on upload · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use event notification to summarize PDF files on upload. Use Workers AI to summarize the PDF and store the summary as a text file."><meta property="og:url" content="https://developers.cloudflare.com/r2/tutorials/summarize-pdf/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Workers,Queues,Workers AI"><meta name="pcx_tags" content="TypeScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/tutorials/summarize-pdf/#page","headline":"Use event notification to summarize PDF files on upload \u00b7 Cloudflare R2 docs","description":"Use event notification to summarize PDF files on upload. Use Workers AI to summarize the PDF and store the summary as a text file.","url":"https://developers.cloudflare.com/r2/tutorials/summarize-pdf/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TypeScript"]}</script>
  markdown: true
  noindex: false
  route: /r2/tutorials/summarize-pdf/
  schema: 1
---
<p>In this tutorial, you will learn how to use <a href="/r2/buckets/event-notifications/">event notifications</a> to process a PDF file when it is uploaded to an R2 bucket. You will use <a href="/workers-ai/">Workers AI</a> to summarize the PDF and store the summary as a text file in the same bucket.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To continue, you will need:</p>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a> with access to R2.</li>
<li>Have an existing R2 bucket. Refer to <a href="/r2/get-started/#2-create-a-bucket">Get started tutorial for R2</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ul>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11357.md")
</div></details>
<h2 id="1-create-a-new-project"><ol>
<li>Create a new project</li>
</ol></h2>
<p>You will create a new Worker project that will use <a href="/workers/static-assets/">Static Assets</a> to serve the front-end of your application. A user can upload a PDF file using this front-end, which will then be processed by your Worker.</p>
<p>Create a new Worker project by running the following commands:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- pdf-summarizer</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- pdf-summarizer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare pdf-summarizer</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare pdf-summarizer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest pdf-summarizer</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest pdf-summarizer" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Navigate to the <code>pdf-summarizer</code> directory:</p>
<pre tabindex="0"><code class="language-sh">cd pdf-summarizer&#10;</code></pre>
<h2 id="2-create-the-front-end"><ol start="2">
<li>Create the front-end</li>
</ol></h2>
<p>Using Static Assets, you can serve the front-end of your application from your Worker. To use Static Assets, you need to add the required bindings to your Wrangler file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11358.md")
</div>
<p>Next, create a <code>public</code> directory and add an <code>index.html</code> file. The <code>index.html</code> file should contain the following HTML code:</p>
<details>
<summary>
Select to view the HTML code
</summary>
<pre tabindex="0"><code class="language-html">&lt;!doctype html&gt;&#10;&lt;html lang=&quot;en&quot;&gt;&#10;	&lt;head&gt;&#10;		&lt;meta charset=&quot;UTF-8&quot; /&gt;&#10;		&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot; /&gt;&#10;		&lt;title&gt;PDF Summarizer&lt;/title&gt;&#10;		&lt;style&gt;&#10;			body {&#10;				font-family: Arial, sans-serif;&#10;				display: flex;&#10;				flex-direction: column;&#10;				min-height: 100vh;&#10;				margin: 0;&#10;				background-color: #fefefe;&#10;			}&#10;			.content {&#10;				flex: 1;&#10;				display: flex;&#10;				justify-content: center;&#10;				align-items: center;&#10;			}&#10;			.upload-container {&#10;				background-color: #f0f0f0;&#10;				padding: 20px;&#10;				border-radius: 8px;&#10;				box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);&#10;			}&#10;			.upload-button {&#10;				background-color: #4caf50;&#10;				color: white;&#10;				padding: 10px 15px;&#10;				border: none;&#10;				border-radius: 4px;&#10;				cursor: pointer;&#10;				font-size: 16px;&#10;			}&#10;			.upload-button:hover {&#10;				background-color: #45a049;&#10;			}&#10;			footer {&#10;				background-color: #f0f0f0;&#10;				color: white;&#10;				text-align: center;&#10;				padding: 10px;&#10;				width: 100%;&#10;			}&#10;			footer a {&#10;				color: #333;&#10;				text-decoration: none;&#10;				margin: 0 10px;&#10;			}&#10;			footer a:hover {&#10;				text-decoration: underline;&#10;			}&#10;		&lt;/style&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;		&lt;div class=&quot;content&quot;&gt;&#10;			&lt;div class=&quot;upload-container&quot;&gt;&#10;				&lt;h2&gt;Upload PDF File&lt;/h2&gt;&#10;				&lt;form id=&quot;uploadForm&quot; onsubmit=&quot;return handleSubmit(event)&quot;&gt;&#10;					&lt;input&#10;						type=&quot;file&quot;&#10;						id=&quot;pdfFile&quot;&#10;						name=&quot;pdfFile&quot;&#10;						accept=&quot;.pdf&quot;&#10;						required&#10;					/&gt;&#10;					&lt;button type=&quot;submit&quot; id=&quot;uploadButton&quot; class=&quot;upload-button&quot;&gt;&#10;						Upload&#10;					&lt;/button&gt;&#10;				&lt;/form&gt;&#10;			&lt;/div&gt;&#10;		&lt;/div&gt;&#10;&#10;		&lt;footer&gt;&#10;			&lt;a&#10;				href=&quot;https://developers.cloudflare.com/r2/buckets/event-notifications/&quot;&#10;				target=&quot;_blank&quot;&#10;				&gt;R2 Event Notification&lt;/a&#10;			&gt;&#10;			&lt;a&#10;				href=&quot;https://developers.cloudflare.com/queues/get-started/#3-create-a-queue&quot;&#10;				target=&quot;_blank&quot;&#10;				&gt;Cloudflare Queues&lt;/a&#10;			&gt;&#10;			&lt;a href=&quot;https://developers.cloudflare.com/workers-ai/&quot; target=&quot;_blank&quot;&#10;				&gt;Workers AI&lt;/a&#10;			&gt;&#10;			&lt;a&#10;				href=&quot;https://github.com/harshil1712/pdf-summarizer-r2-event-notification&quot;&#10;				target=&quot;_blank&quot;&#10;				&gt;GitHub Repo&lt;/a&#10;			&gt;&#10;		&lt;/footer&gt;&#10;&#10;		&lt;script&gt;&#10;			handleSubmit = async (event) =&gt; {&#10;				event.preventDefault();&#10;&#10;				// Disable the upload button and show a loading message&#10;				const uploadButton = document.getElementById(&quot;uploadButton&quot;);&#10;				uploadButton.disabled = true;&#10;				uploadButton.textContent = &quot;Uploading...&quot;;&#10;&#10;				// get form data&#10;				const formData = new FormData(event.target);&#10;				const file = formData.get(&quot;pdfFile&quot;);&#10;&#10;				if (file) {&#10;					// call /api/upload endpoint and send the file&#10;					await fetch(&quot;/api/upload&quot;, {&#10;						method: &quot;POST&quot;,&#10;						body: formData,&#10;					});&#10;&#10;					event.target.reset();&#10;				} else {&#10;					console.log(&quot;No file selected&quot;);&#10;				}&#10;				uploadButton.disabled = false;&#10;				uploadButton.textContent = &quot;Upload&quot;;&#10;			};&#10;		&lt;/script&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
</details>
<p>To view the front-end of your application, run the following command and navigate to the URL displayed in the terminal:</p>
<pre tabindex="0"><code class="language-sh">npm run dev&#10;</code></pre>
<pre tabindex="0"><code class="language-txt"> ⛅️ wrangler 3.80.2&#10;&#45;------------------&#10;&#10;⎔ Starting local server...&#10;[wrangler:inf] Ready on http://localhost:8787&#10;╭───────────────────────────╮&#10;│  [b] open a browser       │&#10;│  [d] open devtools        │&#10;│  [l] turn off local mode  │&#10;│  [c] clear console        │&#10;│  [x] to exit              │&#10;╰───────────────────────────╯&#10;</code></pre>
<p>When you open the URL in your browser, you will see that there is a file upload form. If you try uploading a file, you will notice that the file is not uploaded to the server. This is because the front-end is not connected to the back-end. In the next step, you will update your Worker that will handle the file upload.</p>
<h2 id="3-handle-file-upload"><ol start="3">
<li>Handle file upload</li>
</ol></h2>
<p>To handle the file upload, you will first need to add the R2 binding. In the Wrangler file, add the following code:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11359.md")
</div>
<p>Replace <code>&lt;R2_BUCKET_NAME&gt;</code> with the name of your R2 bucket.</p>
<p>Next, update the <code>src/index.ts</code> file. The <code>src/index.ts</code> file should contain the following code:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Get the pathname from the request&#10;		const pathname = new URL(request.url).pathname;&#10;&#10;		if (pathname === &quot;/api/upload&quot; &amp;&amp; request.method === &quot;POST&quot;) {&#10;			// Get the file from the request&#10;			const formData = await request.formData();&#10;			const file = formData.get(&quot;pdfFile&quot;) as File;&#10;&#10;			// Upload the file to Cloudflare R2&#10;			const upload = await env.MY_BUCKET.put(file.name, file);&#10;			return new Response(&quot;File uploaded successfully&quot;, { status: 200 });&#10;		}&#10;&#10;		return new Response(&quot;incorrect route&quot;, { status: 404 });&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>The above code does the following:</p>
<ul>
<li>Check if the request is a POST request to the <code>/api/upload</code> endpoint. If it is, it gets the file from the request and uploads it to Cloudflare R2 using the <a href="/r2/api/workers/">Workers API</a>.</li>
<li>If the request is not a POST request to the <code>/api/upload</code> endpoint, it returns a 404 response.</li>
</ul>
<p>Since the Worker code is written in TypeScript, you should run the following command to add the necessary type definitions. While this is not required, it will help you avoid errors.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="prevent-potential-errors-when-accessing-request-body">Prevent potential errors when accessing request.body</h3>
@markup("md", "content/.markup/bodies/11356.md")
</aside>
<pre tabindex="0"><code class="language-sh">npm run cf-typegen&#10;</code></pre>
<p>You can restart the developer server to test the changes:</p>
<pre tabindex="0"><code class="language-sh">npm run dev&#10;</code></pre>
<h2 id="4-create-a-queue"><ol start="4">
<li>Create a queue</li>
</ol></h2>
<p>Event notifications capture changes to data in your R2 bucket. You will need to create a new queue <code>pdf-summarize</code> to receive notifications:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler queues create pdf-summarizer&#10;</code></pre>
<p>Add the binding to the Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11360.md")
</div>
<h2 id="5-handle-event-notifications"><ol start="5">
<li>Handle event notifications</li>
</ol></h2>
<p>Now that you have a queue to receive event notifications, you need to update the Worker to handle the event notifications. You will need to add a Queue handler that will extract the textual content from the PDF, use Workers AI to summarize the content, and then save it in the R2 bucket.</p>
<p>Update the <code>src/index.ts</code> file to add the Queue handler:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// No changes in the fetch handler&#10;	},&#10;	async queue(batch, env) {&#10;		for (let message of batch.messages) {&#10;			console.log(`Processing the file: ${message.body.object.key}`);&#10;		}&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>The above code does the following:</p>
<ul>
<li>The <code>queue</code> handler is called when a new message is added to the queue. It loops through the messages in the batch and logs the name of the file.</li>
</ul>
<p>For now the <code>queue</code> handler is not doing anything. In the next steps, you will update the <code>queue</code> handler to extract the textual content from the PDF, use Workers AI to summarize the content, and then add it to the bucket.</p>
<h2 id="6-extract-the-textual-content-from-the-pdf"><ol start="6">
<li>Extract the textual content from the PDF</li>
</ol></h2>
<p>To extract the textual content from the PDF, the Worker will use the <a href="https://github.com/unjs/unpdf">unpdf</a> library. The <code>unpdf</code> library provides utilities to work with PDF files.</p>
<p>Install the <code>unpdf</code> library by running the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i unpdf</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i unpdf" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add unpdf</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add unpdf" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add unpdf</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add unpdf" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add unpdf</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add unpdf" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Update the <code>src/index.ts</code> file to import the required modules from the <code>unpdf</code> library:</p>
<pre tabindex="0"><code class="language-ts">import { extractText, getDocumentProxy } from &quot;unpdf&quot;;&#10;</code></pre>
<p>Next, update the <code>queue</code> handler to extract the textual content from the PDF:</p>
<pre tabindex="0"><code class="language-ts">async queue(batch, env) {&#10;  for(let message of batch.messages) {&#10;    console.log(`Processing file: ${message.body.object.key}`);&#10;    // Get the file from the R2 bucket&#10;    const file = await env.MY_BUCKET.get(message.body.object.key);&#10;    if (!file) {&#10;				console.error(`File not found: ${message.body.object.key}`);&#10;				continue;&#10;			}&#10;    // Extract the textual content from the PDF&#10;    const buffer = await file.arrayBuffer();&#10;    const document = await getDocumentProxy(new Uint8Array(buffer));&#10;&#10;    const {text} = await extractText(document, {mergePages: true});&#10;    console.log(`Extracted text: ${text.substring(0, 100)}...`);&#10;    }&#10;}&#10;</code></pre>
<p>The above code does the following:</p>
<ul>
<li>The <code>queue</code> handler gets the file from the R2 bucket.</li>
<li>The <code>queue</code> handler extracts the textual content from the PDF using the <code>unpdf</code> library.</li>
<li>The <code>queue</code> handler logs the textual content.</li>
</ul>
<h2 id="7-use-workers-ai-to-summarize-the-content"><ol start="7">
<li>Use Workers AI to summarize the content</li>
</ol></h2>
<p>To use Workers AI, you will need to add the Workers AI binding to the Wrangler file. The Wrangler file should contain the following code:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11361.md")
</div>
<p>Execute the following command to add the AI type definition:</p>
<pre tabindex="0"><code class="language-sh">npm run cf-typegen&#10;</code></pre>
<p>Update the <code>src/index.ts</code> file to use Workers AI to summarize the content:</p>
<pre tabindex="0"><code class="language-ts">async queue(batch, env) {&#10;  for(let message of batch.messages) {&#10;    // Extract the textual content from the PDF&#10;    const {text} = await extractText(document, {mergePages: true});&#10;    console.log(`Extracted text: ${text.substring(0, 100)}...`);&#10;&#10;    // Use Workers AI to summarize the content&#10;    const result: AiSummarizationOutput = await env.AI.run(&#10;    &quot;@cf/facebook/bart-large-cnn&quot;,&#10;      {&#10;        input_text: text,&#10;      }&#10;    );&#10;    const summary = result.summary;&#10;    console.log(`Summary: ${summary.substring(0, 100)}...`);&#10;  }&#10;}&#10;</code></pre>
<p>The <code>queue</code> handler now uses Workers AI to summarize the content.</p>
<h2 id="8-add-the-summary-to-the-r2-bucket"><ol start="8">
<li>Add the summary to the R2 bucket</li>
</ol></h2>
<p>Now that you have the summary, you need to add it to the R2 bucket. Update the <code>src/index.ts</code> file to add the summary to the R2 bucket:</p>
<pre tabindex="0"><code class="language-ts">async queue(batch, env) {&#10;  for(let message of batch.messages) {&#10;    // Extract the textual content from the PDF&#10;    // ...&#10;    // Use Workers AI to summarize the content&#10;    // ...&#10;&#10;    // Add the summary to the R2 bucket&#10;    const upload = await env.MY_BUCKET.put(`${message.body.object.key}-summary.txt`, summary, {&#10;					httpMetadata: {&#10;						contentType: &#x27;text/plain&#x27;,&#10;					},&#10;		});&#10;		console.log(`Summary added to the R2 bucket: ${upload.key}`);&#10;  }&#10;}&#10;</code></pre>
<p>The queue handler now adds the summary to the R2 bucket as a text file.</p>
<h2 id="9-enable-event-notifications"><ol start="9">
<li>Enable event notifications</li>
</ol></h2>
<p>Your <code>queue</code> handler is ready to handle incoming event notification messages. You need to enable event notifications with the <a href="/workers/wrangler/commands/r2/#r2-bucket-notification-create"><code>wrangler r2 bucket notification create</code> command</a> for your bucket. The following command creates an event notification for the <code>object-create</code> event type for the <code>pdf</code> suffix:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket notification create &lt;R2_BUCKET_NAME&gt; --event-type object-create --queue pdf-summarizer --suffix &quot;pdf&quot;&#10;</code></pre>
<p>Replace <code>&lt;R2_BUCKET_NAME&gt;</code> with the name of your R2 bucket.</p>
<p>An event notification is created for the <code>pdf</code> suffix. When a new file with the <code>pdf</code> suffix is uploaded to the R2 bucket, the <code>pdf-summarizer</code> queue is triggered.</p>
<h2 id="10-deploy-your-worker"><ol start="10">
<li>Deploy your Worker</li>
</ol></h2>
<p>To deploy your Worker, run the <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> command:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>In the output of the <code>wrangler deploy</code> command, copy the URL. This is the URL of your deployed application.</p>
<h2 id="11-test"><ol start="11">
<li>Test</li>
</ol></h2>
<p>To test the application, navigate to the URL of your deployed application and upload a PDF file. Alternatively, you can use the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> to upload a PDF file.</p>
<p>To view the logs, you can use the <a href="/workers/wrangler/commands/general/#tail"><code>wrangler tail</code></a> command.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler tail&#10;</code></pre>
<p>You will see the logs in your terminal. You can also navigate to the Cloudflare dashboard and view the logs in the Workers Logs section.</p>
<p>If you check your R2 bucket, you will see the summary file.</p>
<h2 id="conclusion">Conclusion</h2>
<p>In this tutorial, you learned how to use R2 event notifications to process an object on upload. You created an application to upload a PDF file, and created a consumer Worker that creates a summary of the PDF file. You also learned how to use Workers AI to summarize the content of the PDF file, and upload the summary to the R2 bucket.</p>
<p>You can use the same approach to process other types of files, such as images, videos, and audio files. You can also use the same approach to process other types of events, such as object deletion, and object update.</p>
<p>If you want to view the code for this tutorial, you can find it on <a href="https://github.com/harshil1712/pdf-summarizer-r2-event-notification">GitHub</a>.</p>
