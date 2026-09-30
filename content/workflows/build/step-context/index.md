---
cp9:
  canonical: https://developers.cloudflare.com/workflows/build/step-context/
  description: Access runtime information in Workflows steps using the WorkflowStepContext object, including step name and retry attempt.
  full_title: Step context · Cloudflare Workflows docs
  head_html: <title>Step context · Cloudflare Workflows docs</title><meta name="generator" content="Nift"><meta name="description" content="Access runtime information in Workflows steps using the WorkflowStepContext object, including step name and retry attempt."><link rel="canonical" href="https://developers.cloudflare.com/workflows/build/step-context/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workflows/build/step-context/index.md"><meta property="og:title" content="Step context · Cloudflare Workflows docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Access runtime information in Workflows steps using the WorkflowStepContext object, including step name and retry attempt."><meta property="og:url" content="https://developers.cloudflare.com/workflows/build/step-context/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workflows"><meta name="algolia_product_filter" content="Workflows"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workflows"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workflows/build/step-context/#page","headline":"Step context \u00b7 Cloudflare Workflows docs","description":"Access runtime information in Workflows steps using the WorkflowStepContext object, including step name and retry attempt.","url":"https://developers.cloudflare.com/workflows/build/step-context/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workflows/build/step-context/
  schema: 1
---
<p>Every <code>step.do</code> callback receives a <strong>context object</strong> (<code>WorkflowStepContext</code>) as its first argument. The context gives your step code runtime information about the step itself, the current retry attempt, and the resolved configuration for that step.</p>
<h2 id="workflowstepcontext">WorkflowStepContext</h2>
<pre tabindex="0"><code class="language-ts">type WorkflowStepContext = {&#10;	step: {&#10;		name: string;&#10;		count: number;&#10;	};&#10;	attempt: number;&#10;	config: WorkflowStepConfig;&#10;};&#10;</code></pre>
<h3 id="properties">Properties</h3>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>step.name</code></td>
<td><code>string</code></td>
<td>The name you passed to <code>step.do</code>.</td>
</tr>
<tr>
<td><code>step.count</code></td>
<td><code>number</code></td>
<td>How many times <code>step.do</code> has been called with this name so far in the current Workflow run. Starts at <code>1</code> for the first call with a given name.</td>
</tr>
<tr>
<td><code>attempt</code></td>
<td><code>number</code></td>
<td>The current attempt number (1-indexed). <code>1</code> on the first try, <code>2</code> on the first retry, and so on.</td>
</tr>
<tr>
<td><code>config</code></td>
<td><a href="/workflows/build/workers-api/#workflowstepconfig"><code>WorkflowStepConfig</code></a></td>
<td>The resolved retry and timeout configuration for this step, including any defaults applied by the runtime.</td>
</tr>
</tbody>
</table>
<p>If a step config's <code>retries.delay</code> is a function, the dynamic delay is not exposed on <code>ctx.config.retries.delay</code>. The delay function receives its own context object with the current step context and the error that caused the retry.</p>
<h2 id="access-the-context">Access the context</h2>
<p>Pass a parameter to your <code>step.do</code> callback to receive the context object:</p>
<pre tabindex="0"><code class="language-ts">await step.do(&quot;my-step&quot;, async (ctx) =&gt; {&#10;	console.log(ctx.step.name); // &quot;my-step&quot;&#10;	console.log(ctx.step.count); // 1&#10;	console.log(ctx.attempt); // 1 on first try, 2 on first retry, etc.&#10;	console.log(ctx.config); // { retries: { limit: 5, ... }, timeout: &quot;10 minutes&quot; }&#10;});&#10;</code></pre>
<p>The context is also available when you pass a custom <code>WorkflowStepConfig</code>:</p>
<pre tabindex="0"><code class="language-ts">await step.do(&#10;	&quot;call an API&quot;,&#10;	{&#10;		retries: {&#10;			limit: 10,&#10;			delay: &quot;10 seconds&quot;,&#10;			backoff: &quot;exponential&quot;,&#10;		},&#10;		timeout: &quot;30 minutes&quot;,&#10;	},&#10;	async (ctx) =&gt; {&#10;		console.log(ctx.config.retries.limit); // 10&#10;		console.log(ctx.config.timeout); // &quot;30 minutes&quot;&#10;	},&#10;);&#10;</code></pre>
<p>To configure delay functions, refer to <a href="/workflows/build/sleeping-and-retrying/#set-a-dynamic-retry-delay">Set a dynamic retry delay</a>.</p>
<h2 id="examples">Examples</h2>
<h3 id="adjust-behavior-based-on-retry-attempt">Adjust behavior based on retry attempt</h3>
<p>Use <code>ctx.attempt</code> to change how your step behaves on retries. For example, you might use a fallback endpoint after a certain number of retries:</p>
<pre tabindex="0"><code class="language-ts">await step.do(&#10;	&quot;fetch data&quot;,&#10;	{ retries: { limit: 5, delay: &quot;5 seconds&quot;, backoff: &quot;linear&quot; } },&#10;	async (ctx) =&gt; {&#10;		const url =&#10;			ctx.attempt &lt;= 3&#10;				? &quot;https://api.example.com/primary&quot;&#10;				: &quot;https://api.example.com/fallback&quot;;&#10;&#10;		const response = await fetch(url);&#10;		if (!response.ok) {&#10;			throw new Error(`Request failed with status ${response.status}`);&#10;		}&#10;		return await response.json();&#10;	},&#10;);&#10;</code></pre>
<h3 id="log-step-metadata-for-observability">Log step metadata for observability</h3>
<p>Use <code>ctx.step</code> to add structured metadata to your logs:</p>
<pre tabindex="0"><code class="language-ts">await step.do(&quot;process-order&quot;, async (ctx) =&gt; {&#10;	console.log(&#10;		JSON.stringify({&#10;			step: ctx.step.name,&#10;			stepCount: ctx.step.count,&#10;			attempt: ctx.attempt,&#10;			retryLimit: ctx.config.retries?.limit,&#10;		}),&#10;	);&#10;&#10;	// Your step logic here&#10;});&#10;</code></pre>
