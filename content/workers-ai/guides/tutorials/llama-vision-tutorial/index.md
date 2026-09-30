---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/guides/tutorials/llama-vision-tutorial/
  description: Learn how to use the Llama 3.2 11B Vision Instruct model on Cloudflare Workers AI.
  full_title: Llama 3.2 11B Vision Instruct model on Cloudflare Workers AI · Cloudflare Workers AI docs
  head_html: <title>Llama 3.2 11B Vision Instruct model on Cloudflare Workers AI · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to use the Llama 3.2 11B Vision Instruct model on Cloudflare Workers AI."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/guides/tutorials/llama-vision-tutorial/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/guides/tutorials/llama-vision-tutorial/index.md"><meta property="og:title" content="Llama 3.2 11B Vision Instruct model on Cloudflare Workers AI · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to use the Llama 3.2 11B Vision Instruct model on Cloudflare Workers AI."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/guides/tutorials/llama-vision-tutorial/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Workers AI"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/guides/tutorials/llama-vision-tutorial/#page","headline":"Llama 3.2 11B Vision Instruct model on Cloudflare Workers AI \u00b7 Cloudflare Workers AI docs","description":"Learn how to use the Llama 3.2 11B Vision Instruct model on Cloudflare Workers AI.","url":"https://developers.cloudflare.com/workers-ai/guides/tutorials/llama-vision-tutorial/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /workers-ai/guides/tutorials/llama-vision-tutorial/
  schema: 1
---
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, ensure you have the following:</p>
<ol>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a> with Workers and Workers AI enabled.</li>
<li>Your <code>CLOUDFLARE_ACCOUNT_ID</code> and <code>CLOUDFLARE_AUTH_TOKEN</code>.
<ul>
<li>You can generate an API token in your Cloudflare dashboard under API Tokens.</li>
</ul>
</li>
<li>Node.js installed for working with Cloudflare Workers (optional but recommended).</li>
</ol>
<h2 id="1-agree-to-meta-s-license"><ol>
<li>Agree to Meta's license</li>
</ol></h2>
<p>The first time you use the <a href="/workers-ai/models/llama-3.2-11b-vision-instruct">Llama 3.2 11B Vision Instruct</a> model, you need to agree to Meta's License and Acceptable Use Policy.</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/meta/llama-3.2-11b-vision-instruct \&#10;  &#45;X POST \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot; \&#10;  &#45;d &#x27;{ &quot;prompt&quot;: &quot;agree&quot; }&#x27;&#10;</code></pre>
<p>Replace <code>$CLOUDFLARE_ACCOUNT_ID</code> and <code>$CLOUDFLARE_AUTH_TOKEN</code> with your actual account ID and token.</p>
<h2 id="2-set-up-your-cloudflare-worker"><ol start="2">
<li>Set up your Cloudflare Worker</li>
</ol></h2>
<ol>
<li>
<p>Create a Worker Project
You will create a new Worker project using the <code>create-cloudflare</code> CLI (<code>C3</code>). This tool simplifies setting up and deploying new applications to Cloudflare.</p>
<p>Run the following command in your terminal:</p>
</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- llama-vision-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- llama-vision-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare llama-vision-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare llama-vision-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest llama-vision-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest llama-vision-tutorial" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>JavaScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>After completing the setup, a new directory called <code>llama-vision-tutorial</code> will be created.</p>
<ol start="2">
<li>Navigate to your application directory
Change into the project directory:</li>
</ol>
<pre tabindex="0"><code class="language-bash">cd llama-vision-tutorial&#10;</code></pre>
<ol start="3">
<li>Project structure
Your <code>llama-vision-tutorial</code> directory will include:
<ul>
<li>A &quot;Hello World&quot; Worker at <code>src/index.ts</code>.</li>
<li>A <code>wrangler.json</code> configuration file for managing deployment settings.</li>
</ul>
</li>
</ol>
<h2 id="3-write-the-worker-code"><ol start="3">
<li>Write the Worker code</li>
</ol></h2>
<p>Edit the <code>src/index.ts</code> (or <code>index.js</code> if you are not using TypeScript) file and replace the content with the following code:</p>
<pre tabindex="0"><code class="language-javascript">export interface Env {&#10;  AI: Ai;&#10;}&#10;&#10;export default {&#10;  async fetch(request, env): Promise&lt;Response&gt; {&#10;    const messages = [&#10;      { role: &quot;system&quot;, content: &quot;You are a helpful assistant.&quot; },&#10;      { role: &quot;user&quot;, content: &quot;Describe the image I&#x27;m providing.&quot; },&#10;    ];&#10;&#10;    // Replace this with your image data encoded as base64 or a URL&#10;    const imageBase64 = &quot;data:image/png;base64,IMAGE_DATA_HERE&quot;;&#10;&#10;    const response = await env.AI.run(&quot;@cf/meta/llama-3.2-11b-vision-instruct&quot;, {&#10;      messages,&#10;      image: imageBase64,&#10;    });&#10;&#10;    return Response.json(response);&#10;  },&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h2 id="4-bind-workers-ai-to-your-worker"><ol start="4">
<li>Bind Workers AI to your Worker</li>
</ol></h2>
<ol>
<li>Open the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> and add the following configuration:</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15842.md")
</div>
<ol start="2">
<li>Save the file.</li>
</ol>
<h2 id="5-deploy-the-worker"><ol start="5">
<li>Deploy the Worker</li>
</ol></h2>
<p>Run the following command to deploy your Worker:</p>
<pre tabindex="0"><code class="language-bash">wrangler deploy&#10;</code></pre>
<h2 id="6-test-your-worker"><ol start="6">
<li>Test Your Worker</li>
</ol></h2>
<ol>
<li>After deployment, you will receive a unique URL for your Worker (e.g., <code>https://llama-vision-tutorial.&lt;your-subdomain&gt;.workers.dev</code>).</li>
<li>Use a tool like <code>curl</code> or Postman to send a request to your Worker:</li>
</ol>
<pre tabindex="0"><code class="language-bash">curl -X POST https://llama-vision-tutorial.&lt;your-subdomain&gt;.workers.dev \&#10;  &#45;d &#x27;{ &quot;image&quot;: &quot;BASE64_ENCODED_IMAGE&quot; }&#x27;&#10;</code></pre>
<p>Replace <code>BASE64_ENCODED_IMAGE</code> with an actual base64-encoded image string.</p>
<h2 id="7-verify-the-response"><ol start="7">
<li>Verify the response</li>
</ol></h2>
<p>The response will include the output from the model, such as a description or answer to your prompt based on the image provided.</p>
<p>Example response:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: &quot;This is a golden retriever sitting in a grassy park.&quot;&#10;}&#10;</code></pre>
