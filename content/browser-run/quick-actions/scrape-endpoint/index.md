---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/quick-actions/scrape-endpoint/
  description: Extract structured data from specific webpage elements using the Browser Run /scrape endpoint.
  full_title: /scrape - Scrape HTML elements · Cloudflare Browser Run docs
  head_html: <title>/scrape - Scrape HTML elements · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Extract structured data from specific webpage elements using the Browser Run /scrape endpoint."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/quick-actions/scrape-endpoint/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/quick-actions/scrape-endpoint/index.md"><meta property="og:title" content="/scrape - Scrape HTML elements · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Extract structured data from specific webpage elements using the Browser Run /scrape endpoint."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/quick-actions/scrape-endpoint/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/quick-actions/scrape-endpoint/#page","headline":"/scrape - Scrape HTML elements \u00b7 Cloudflare Browser Run docs","description":"Extract structured data from specific webpage elements using the Browser Run /scrape endpoint.","url":"https://developers.cloudflare.com/browser-run/quick-actions/scrape-endpoint/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/quick-actions/scrape-endpoint/
  schema: 1
---
<p>The <code>/scrape</code> endpoint extracts structured data from specific elements on a webpage, returning details such as element dimensions and inner HTML.</p>
<p>You can use this endpoint in two ways:</p>
<ul>
<li><strong>REST API</strong>: <a href="/fundamentals/api/get-started/create-token/">Create a custom API Token</a> with <code>Browser Rendering - Edit</code> permission.</li>
<li><strong>Workers Bindings</strong>: Call the endpoint directly from a <a href="/workers/">Cloudflare Worker</a> using the <a href="/browser-run/reference/wrangler/#bindings">Workers Bindings</a>. No API token is needed.</li>
</ul>
<p>For more information, refer to <a href="/browser-run/quick-actions/#before-you-begin">Quick Actions: Before you begin</a>.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/scrape&#10;</code></pre>
<h2 id="required-fields">Required fields</h2>
<p>You must provide <code>elements</code> and exactly one of <code>url</code> or <code>html</code>:</p>
<ul>
<li><code>url</code> (string)</li>
<li><code>html</code> (string)</li>
<li><code>elements</code> (array of objects) — each object must include <code>selector</code> (string)</li>
</ul>
<h2 id="common-use-cases">Common use cases</h2>
<ul>
<li>Extract headings, links, prices, or other repeated content with CSS selectors</li>
<li>Collect metadata (for example, titles, descriptions, canonical links)</li>
</ul>
<h2 id="basic-usage">Basic usage</h2>
<h3 id="extract-headings-and-links-from-a-url">Extract headings and links from a URL</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3608.md")
</div></div>
<p>Many more options exist, like setting HTTP credentials using <code>authenticate</code>, setting <code>cookies</code>, and using <code>gotoOptions</code> to control page load behaviour - check the endpoint <a href="/api/resources/browser_rendering/subresources/scrape/methods/create/">reference</a> for all available parameters.</p>
<h3 id="response-fields">Response fields</h3>
<ul>
<li><code>results</code> <em>(array of objects)</em> - Contains extracted data for each selector.
<ul>
<li><code>selector</code> <em>(string)</em> - The CSS selector used.</li>
<li><code>results</code> <em>(array of objects)</em> - List of extracted elements matching the selector.
<ul>
<li><code>text</code> <em>(string)</em> - Inner text of the element.</li>
<li><code>html</code> <em>(string)</em> - Inner HTML of the element.</li>
<li><code>attributes</code> <em>(array of objects)</em> - List of extracted attributes such as <code>href</code> for links.</li>
<li><code>height</code>, <code>width</code>, <code>top</code>, <code>left</code> <em>(number)</em> - Position and dimensions of the element.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 id="advanced-usage">Advanced usage</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-more-parameters">Looking for more parameters?</h3>
@markup("md", "content/.markup/bodies/3604.md")
</aside>
<h3 id="handling-javascript-heavy-pages">Handling JavaScript-heavy pages</h3>
<p>For JavaScript-heavy pages or Single Page Applications (SPAs), the default page load behavior may return empty or incomplete results. This happens because the browser considers the page loaded before JavaScript has finished rendering the content.</p>
<p>The simplest solution is to use the <code>gotoOptions.waitUntil</code> parameter set to <code>networkidle0</code> or <code>networkidle2</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;url&quot;: &quot;https://example.com&quot;,&#10;	&quot;gotoOptions&quot;: {&#10;		&quot;waitUntil&quot;: &quot;networkidle0&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For faster responses, advanced users can use <code>waitForSelector</code> to wait for a specific element instead of waiting for all network activity to stop. This requires knowing which CSS selector indicates the content you need has loaded. For more details, refer to <a href="/browser-run/reference/timeouts/">Quick Actions timeouts</a>.</p>
<h3 id="set-a-custom-user-agent">Set a custom user agent</h3>
<p>You can change the user agent at the page level by passing <code>userAgent</code> as a top-level parameter in the JSON body. This is useful if the target website serves different content based on the user agent.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3603.md")
</aside>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
