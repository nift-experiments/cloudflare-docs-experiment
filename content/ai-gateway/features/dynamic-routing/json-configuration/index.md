---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/json-configuration/
  description: Define AI Gateway dynamic routing flows using the REST API and JSON element structure.
  full_title: JSON Configuration · Cloudflare AI Gateway docs
  head_html: <title>JSON Configuration · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Define AI Gateway dynamic routing flows using the REST API and JSON element structure."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/json-configuration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/json-configuration/index.md"><meta property="og:title" content="JSON Configuration · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Define AI Gateway dynamic routing flows using the REST API and JSON element structure."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/json-configuration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/json-configuration/#page","headline":"JSON Configuration \u00b7 Cloudflare AI Gateway docs","description":"Define AI Gateway dynamic routing flows using the REST API and JSON element structure.","url":"https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/json-configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/features/dynamic-routing/json-configuration/
  schema: 1
---
<p>Instead of using the <strong>dashboard editor UI</strong> to define the route graph, you can do it using the REST API. Routes are internally represented using a simple JSON structure:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;id&quot;: &quot;&lt;route id&gt;&quot;,&#10;  &quot;name&quot;: &quot;&lt;route name&gt;&quot;,&#10;  &quot;elements&quot;: [&lt;array of elements&gt;]&#10;}&#10;</code></pre>
<h2 id="supported-elements">Supported elements</h2>
<p>Dynamic routing supports several types of elements that you can combine to create sophisticated routing flows. Each element has specific inputs, outputs, and configuration options.</p>
<h3 id="start-element">Start Element</h3>
<p>Marks the beginning of a route. Every route must start with a Start element.</p>
<ul>
<li><strong>Inputs</strong>: None</li>
<li><strong>Outputs</strong>:
<ul>
<li><code>next</code>: Forwards the unchanged request to the next element</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;	&quot;type&quot;: &quot;start&quot;,&#10;	&quot;outputs&quot;: {&#10;		&quot;next&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; }&#10;	}&#10;}&#10;</code></pre>
<h3 id="conditional-element-if-else">Conditional Element (If/Else)</h3>
<p>Evaluates a condition based on request parameters and routes the request accordingly.</p>
<ul>
<li><strong>Inputs</strong>: Request</li>
<li><strong>Outputs</strong>:
<ul>
<li><code>true</code>: Forwards request to provided element if condition evaluates to true</li>
<li><code>false</code>: Forwards request to provided element if condition evaluates to false</li>
</ul>
</li>
</ul>
<p><code>conditions</code> supports MongoDB-like operators such as <code>$eq</code>, <code>$ne</code>, <code>$in</code>, <code>$and</code>, and <code>$or</code>.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;	&quot;type&quot;: &quot;conditional&quot;,&#10;	&quot;properties&quot;: {&#10;		&quot;conditions&quot;: {&#10;			&quot;metadata.plan&quot;: { &quot;$eq&quot;: &quot;free&quot; }&#10;		}&#10;	},&#10;	&quot;outputs&quot;: {&#10;		&quot;true&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; },&#10;		&quot;false&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; }&#10;	}&#10;}&#10;</code></pre>
<h3 id="percentage-split">Percentage Split</h3>
<p>Routes requests probabilistically across multiple outputs, useful for A/B testing and gradual rollouts.</p>
<ul>
<li><strong>Inputs</strong>: Request</li>
<li><strong>Outputs</strong>: Up to 5 named percentage outputs
<ul>
<li>Each output key (for example, <code>&quot;10%&quot;</code>) is the probability for that branch, and the keys must sum to 100%</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;	&quot;type&quot;: &quot;percentage&quot;,&#10;	&quot;outputs&quot;: {&#10;		&quot;10%&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; },&#10;		&quot;40%&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; },&#10;		&quot;50%&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; }&#10;	}&#10;}&#10;</code></pre>
<h3 id="rate-budget-limit">Rate/Budget Limit</h3>
<p>Apply limits based on request metadata. Supports both count-based and cost-based limits.</p>
<ul>
<li><strong>Inputs</strong>: Request</li>
<li><strong>Outputs</strong>:
<ul>
<li><code>success</code>: Forwards request to provided element if request is not rate limited</li>
<li><code>fallback</code>: Optional output for rate-limited requests (route terminates if not provided)</li>
</ul>
</li>
</ul>
<p><strong>Properties</strong>:</p>
<ul>
<li><code>limitType</code>: &quot;count&quot; or &quot;cost&quot;</li>
<li><code>key</code>: Request field to use for rate limiting (e.g. &quot;metadata.user_id&quot;)</li>
<li><code>limit</code>: Maximum allowed requests/cost</li>
<li><code>window</code>: Time window in seconds</li>
</ul>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;	&quot;type&quot;: &quot;rate&quot;,&#10;	&quot;properties&quot;: {&#10;		&quot;limitType&quot;: &quot;count&quot;,&#10;		&quot;key&quot;: &quot;metadata.user_id&quot;,&#10;		&quot;limit&quot;: 100,&#10;		&quot;window&quot;: 3600&#10;	},&#10;	&quot;outputs&quot;: {&#10;		&quot;success&quot;: { &quot;elementId&quot;: &quot;node_model_workers_ai&quot; },&#10;		&quot;fallback&quot;: { &quot;elementId&quot;: &quot;node_model_openai_mini&quot; }&#10;	}&#10;}&#10;</code></pre>
<h3 id="model">Model</h3>
<p>Executes inference using a specified model and provider with configurable timeout and retry settings.</p>
<ul>
<li><strong>Inputs</strong>: Request</li>
<li><strong>Outputs</strong>:
<ul>
<li><code>success</code>: Forwards request to provided element if model successfully starts streaming a response</li>
<li><code>fallback</code>: Optional output if model fails after all retries or times out</li>
</ul>
</li>
</ul>
<p><strong>Properties</strong>:</p>
<ul>
<li><code>provider</code>: AI provider (e.g. &quot;openai&quot;, &quot;anthropic&quot;)</li>
<li><code>model</code>: Specific model name</li>
<li><code>timeout</code>: Request timeout in milliseconds</li>
<li><code>retries</code>: Number of retry attempts</li>
</ul>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;	&quot;type&quot;: &quot;model&quot;,&#10;	&quot;properties&quot;: {&#10;		&quot;provider&quot;: &quot;openai&quot;,&#10;		&quot;model&quot;: &quot;gpt-4o-mini&quot;,&#10;		&quot;timeout&quot;: 60000,&#10;		&quot;retries&quot;: 4&#10;	},&#10;	&quot;outputs&quot;: {&#10;		&quot;success&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; },&#10;		&quot;fallback&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; }&#10;	}&#10;}&#10;</code></pre>
<h3 id="end-element">End element</h3>
<p>Marks the end of a route. Returns the last successful model response, or an error if no model response was generated.</p>
<ul>
<li><strong>Inputs</strong>: Request</li>
<li><strong>Outputs</strong>: None (provide an empty <code>outputs</code> object)</li>
</ul>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;	&quot;type&quot;: &quot;end&quot;,&#10;	&quot;outputs&quot;: {}&#10;}&#10;</code></pre>
