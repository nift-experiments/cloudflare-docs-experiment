---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-bindings/
  description: Provide human feedback on AI Gateway evaluations programmatically using Worker bindings.
  full_title: Add human feedback using Worker Bindings · Cloudflare AI Gateway docs
  head_html: <title>Add human feedback using Worker Bindings · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Provide human feedback on AI Gateway evaluations programmatically using Worker bindings."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-bindings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-bindings/index.md"><meta property="og:title" content="Add human feedback using Worker Bindings · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Provide human feedback on AI Gateway evaluations programmatically using Worker bindings."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-bindings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-bindings/#page","headline":"Add human feedback using Worker Bindings \u00b7 Cloudflare AI Gateway docs","description":"Provide human feedback on AI Gateway evaluations programmatically using Worker bindings.","url":"https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-bindings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/evaluations/add-human-feedback-bindings/
  schema: 1
---
<p>This guide explains how to provide human feedback for AI Gateway evaluations using Worker bindings.</p>
<h2 id="1-run-an-ai-evaluation"><ol>
<li>Run an AI Evaluation</li>
</ol></h2>
<p>Start by sending a prompt to the AI model through your AI Gateway.</p>
<pre tabindex="0"><code class="language-javascript">const resp = await env.AI.run(&#10;	&quot;@cf/meta/llama-3.1-8b-instruct&quot;,&#10;	{&#10;		prompt: &quot;tell me a joke&quot;,&#10;	},&#10;	{&#10;		gateway: {&#10;			id: &quot;my-gateway&quot;,&#10;		},&#10;	},&#10;);&#10;&#10;const myLogId = env.AI.aiGatewayLogId;&#10;</code></pre>
<p>Let the user interact with or evaluate the AI response. This interaction will inform the feedback you send back to the AI Gateway.</p>
<h2 id="2-send-human-feedback"><ol start="2">
<li>Send Human Feedback</li>
</ol></h2>
<p>Use the <a href="/ai-gateway/usage/worker-binding-methods/#patchlog"><code>patchLog()</code></a> method to provide feedback for the AI evaluation.</p>
<pre tabindex="0"><code class="language-javascript">await env.AI.gateway(&quot;my-gateway&quot;).patchLog(myLogId, {&#10;	feedback: 1, // all fields are optional; set values that fit your use case&#10;	score: 100,&#10;	metadata: {&#10;		user: &quot;123&quot;, // Optional metadata to provide additional context&#10;	},&#10;});&#10;</code></pre>
<h2 id="feedback-parameters-explanation">Feedback parameters explanation</h2>
<ul>
<li><code>feedback</code>: is either <code>-1</code> for negative or <code>1</code> to positive, <code>0</code> is considered not evaluated.</li>
<li><code>score</code>: A number between 0 and 100.</li>
<li><code>metadata</code>: An object containing additional contextual information.</li>
</ul>
<h3 id="patchlog-send-feedback">patchLog: Send Feedback</h3>
<p>The <code>patchLog</code> method allows you to send feedback, score, and metadata for a specific log ID. All object properties are optional, so you can include any combination of the parameters:</p>
<pre tabindex="0"><code class="language-javascript">gateway.patchLog(&quot;my-log-id&quot;, {&#10;	feedback: 1,&#10;	score: 100,&#10;	metadata: {&#10;		user: &quot;123&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>Returns: <code>Promise&lt;void&gt;</code> (Make sure to <code>await</code> the request.)</p>
