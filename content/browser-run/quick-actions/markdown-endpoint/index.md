---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/quick-actions/markdown-endpoint/
  description: Convert webpage content to Markdown format using the Browser Run /markdown endpoint.
  full_title: /markdown - Extract Markdown from a webpage · Cloudflare Browser Run docs
  head_html: <title>/markdown - Extract Markdown from a webpage · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Convert webpage content to Markdown format using the Browser Run /markdown endpoint."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/quick-actions/markdown-endpoint/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/quick-actions/markdown-endpoint/index.md"><meta property="og:title" content="/markdown - Extract Markdown from a webpage · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Convert webpage content to Markdown format using the Browser Run /markdown endpoint."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/quick-actions/markdown-endpoint/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/quick-actions/markdown-endpoint/#page","headline":"/markdown - Extract Markdown from a webpage \u00b7 Cloudflare Browser Run docs","description":"Convert webpage content to Markdown format using the Browser Run /markdown endpoint.","url":"https://developers.cloudflare.com/browser-run/quick-actions/markdown-endpoint/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/quick-actions/markdown-endpoint/
  schema: 1
---
<p>The <code>/markdown</code> endpoint retrieves a webpage's content and converts it into Markdown format. You can specify a URL and optional parameters to refine the extraction process.</p>
<p>You can use this endpoint in two ways:</p>
<ul>
<li><strong>REST API</strong>: <a href="/fundamentals/api/get-started/create-token/">Create a custom API Token</a> with <code>Browser Rendering - Edit</code> permission.</li>
<li><strong>Workers Bindings</strong>: Call the endpoint directly from a <a href="/workers/">Cloudflare Worker</a> using the <a href="/browser-run/reference/wrangler/#bindings">Workers Bindings</a>. No API token is needed.</li>
</ul>
<p>For more information, refer to <a href="/browser-run/quick-actions/#before-you-begin">Quick Actions: Before you begin</a>.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/markdown&#10;</code></pre>
<h2 id="required-fields">Required fields</h2>
<p>You must provide either <code>url</code> or <code>html</code>:</p>
<ul>
<li><code>url</code> (string)</li>
<li><code>html</code> (string)</li>
</ul>
<h2 id="common-use-cases">Common use cases</h2>
<ul>
<li>Normalize content for downstream processing (summaries, diffs, embeddings)</li>
<li>Save articles or docs for editing or storage</li>
<li>Strip styling/scripts and keep readable content + links</li>
</ul>
<h2 id="basic-usage">Basic usage</h2>
<h3 id="convert-a-url-to-markdown">Convert a URL to Markdown</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3621.md")
</div></div>
<h3 id="convert-raw-html-to-markdown">Convert raw HTML to Markdown</h3>
<p>Instead of fetching the content by specifying the URL, you can provide raw HTML content directly.</p>
<pre tabindex="0"><code class="language-bash">curl -X &#x27;POST&#x27; &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/markdown&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;html&quot;: &quot;&lt;div&gt;Hello World&lt;/div&gt;&quot;&#10;  }&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: &quot;Hello World&quot;&#10;}&#10;</code></pre>
<h2 id="advanced-usage">Advanced usage</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-more-parameters">Looking for more parameters?</h3>
@markup("md", "content/.markup/bodies/3617.md")
</aside>
<h3 id="exclude-unwanted-requests-for-example-css">Exclude unwanted requests (for example, CSS)</h3>
<p>You can refine the Markdown extraction by using the <code>rejectRequestPattern</code> parameter. In this example, requests matching the given regex pattern (such as CSS files) are excluded.</p>
<pre tabindex="0"><code class="language-bash">curl -X &#x27;POST&#x27; &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/markdown&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;,&#10;    &quot;rejectRequestPattern&quot;: [&quot;/^.*\\.(css)/&quot;]&#10;  }&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: &quot;# Example Domain\n\nThis domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.\n\n[More information...](https://www.iana.org/domains/example)&quot;&#10;}&#10;</code></pre>
<h3 id="handling-javascript-heavy-pages">Handling JavaScript-heavy pages</h3>
<p>For JavaScript-heavy pages or Single Page Applications (SPAs), the default page load behavior may return empty or incomplete results. This happens because the browser considers the page loaded before JavaScript has finished rendering the content.</p>
<p>The simplest solution is to use the <code>gotoOptions.waitUntil</code> parameter set to <code>networkidle0</code> or <code>networkidle2</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;url&quot;: &quot;https://example.com&quot;,&#10;	&quot;gotoOptions&quot;: {&#10;		&quot;waitUntil&quot;: &quot;networkidle0&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For faster responses, advanced users can use <code>waitForSelector</code> to wait for a specific element instead of waiting for all network activity to stop. This requires knowing which CSS selector indicates the content you need has loaded. For more details, refer to <a href="/browser-run/reference/timeouts/">Quick Actions timeouts</a>.</p>
<h3 id="set-a-custom-user-agent">Set a custom user agent</h3>
<p>You can change the user agent at the page level by passing <code>userAgent</code> as a top-level parameter in the JSON body. This is useful if the target website serves different content based on the user agent.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3616.md")
</aside>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
<h2 id="other-markdown-conversion-features">Other Markdown conversion features</h2>
<ul>
<li>Workers AI <a href="/workers-ai/features/markdown-conversion/">AI.toMarkdown()</a> supports multiple document types and summarization.</li>
<li><a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> allows real-time document conversion for Cloudflare zones using content negotiation headers.</li>
</ul>
