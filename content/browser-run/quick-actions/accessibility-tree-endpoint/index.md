---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/quick-actions/accessibility-tree-endpoint/
  description: Capture the accessibility tree from a webpage after JavaScript execution using the Browser Run /accessibilityTree endpoint.
  full_title: /accessibilityTree - Capture accessibility tree · Cloudflare Browser Run docs
  head_html: <title>/accessibilityTree - Capture accessibility tree · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Capture the accessibility tree from a webpage after JavaScript execution using the Browser Run /accessibilityTree endpoint."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/quick-actions/accessibility-tree-endpoint/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/quick-actions/accessibility-tree-endpoint/index.md"><meta property="og:title" content="/accessibilityTree - Capture accessibility tree · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Capture the accessibility tree from a webpage after JavaScript execution using the Browser Run /accessibilityTree endpoint."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/quick-actions/accessibility-tree-endpoint/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/quick-actions/accessibility-tree-endpoint/#page","headline":"/accessibilityTree - Capture accessibility tree \u00b7 Cloudflare Browser Run docs","description":"Capture the accessibility tree from a webpage after JavaScript execution using the Browser Run /accessibilityTree endpoint.","url":"https://developers.cloudflare.com/browser-run/quick-actions/accessibility-tree-endpoint/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/quick-actions/accessibility-tree-endpoint/
  schema: 1
---
<p>The <code>/accessibilityTree</code> endpoint instructs the browser to navigate to a website and capture the page's accessibility tree after JavaScript execution. The accessibility tree includes accessibility-related information such as roles, names, values, states, and hierarchy.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-run/accessibilityTree&#10;</code></pre>
<h2 id="required-fields">Required fields</h2>
<p>You must provide either <code>url</code> or <code>html</code>:</p>
<ul>
<li><code>url</code> (string)</li>
<li><code>html</code> (string)</li>
</ul>
<h2 id="common-use-cases">Common use cases</h2>
<ul>
<li>Provide AI agents with a structured page representation for navigation and browser automation workflows</li>
<li>Check roles, accessible names, values, and states exposed to assistive technologies</li>
<li>Identify interactive elements, such as buttons, links, menus, and form fields, that an automation workflow can act on</li>
</ul>
<h2 id="basic-usage">Basic usage</h2>
<h3 id="capture-the-accessibility-tree-from-a-url">Capture the accessibility tree from a URL</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3652.md")
</div></div>
<h2 id="optional-parameters">Optional parameters</h2>
<p>The following optional parameters can be used in your <code>/accessibilityTree</code> request, in addition to the required <code>url</code> or <code>html</code> parameter.</p>
<table>
<thead>
<tr>
<th>Optional parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>interestingOnly</code></td>
<td>Boolean</td>
<td>When <code>true</code>, returns only semantically meaningful nodes. Defaults to <code>true</code>. If <code>root</code> is set and <code>interestingOnly</code> is omitted, defaults to <code>false</code>.</td>
</tr>
<tr>
<td><code>root</code></td>
<td>String</td>
<td>CSS selector that anchors the accessibility tree to a subtree. If the selector does not match an element, <code>accessibilityTree</code> returns <code>null</code>. To return only semantically meaningful nodes within the subtree, set <code>interestingOnly</code> to <code>true</code> explicitly.</td>
</tr>
</tbody>
</table>
<h2 id="advanced-usage">Advanced usage</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-more-parameters">Looking for more parameters?</h3>
@markup("md", "content/.markup/bodies/3648.md")
</aside>
<h3 id="include-all-nodes">Include all nodes</h3>
<p>By default, <code>interestingOnly</code> is <code>true</code>, which filters the response to semantically meaningful nodes. Set <code>interestingOnly</code> to <code>false</code> to include every node in the accessibility tree, including generic and presentational nodes.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-run/accessibilityTree&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com/&quot;,&#10;    &quot;interestingOnly&quot;: false&#10;}&#x27;&#10;</code></pre>
<details class="nb-details"><summary>Response example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3653.md")
</div></details>
<h3 id="capture-a-subtree">Capture a subtree</h3>
<p>Set <code>root</code> to a CSS selector string to return the accessibility tree for a specific part of the page.</p>
<p>When <code>root</code> is set and <code>interestingOnly</code> is not provided, <code>interestingOnly</code> defaults to <code>false</code>. To filter a subtree to semantically meaningful nodes, set <code>interestingOnly</code> to <code>true</code> explicitly.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-run/accessibilityTree&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com/&quot;,&#10;    &quot;root&quot;: &quot;h1&quot;,&#10;    &quot;interestingOnly&quot;: true&#10;}&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;accessibilityTree&quot;: {&#10;			&quot;role&quot;: &quot;heading&quot;,&#10;			&quot;name&quot;: &quot;Example Domain&quot;,&#10;			&quot;level&quot;: 1&#10;		}&#10;	},&#10;	&quot;meta&quot;: {&#10;		&quot;status&quot;: 200,&#10;		&quot;title&quot;: &quot;Example Domain&quot;&#10;	}&#10;}&#10;</code></pre>
<h3 id="handle-a-root-selector-with-no-match">Handle a root selector with no match</h3>
<p>If <code>root</code> does not match any element on the page, the request returns HTTP <code>200</code> and <code>accessibilityTree</code> is <code>null</code>.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-run/accessibilityTree&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com/&quot;,&#10;    &quot;root&quot;: &quot;#does-not-exist&quot;&#10;}&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;accessibilityTree&quot;: null&#10;	},&#10;	&quot;meta&quot;: {&#10;		&quot;status&quot;: 200,&#10;		&quot;title&quot;: &quot;Example Domain&quot;&#10;	}&#10;}&#10;</code></pre>
<h3 id="handling-javascript-heavy-pages">Handling JavaScript-heavy pages</h3>
<p>For JavaScript-heavy pages or Single Page Applications (SPAs), the default page load behavior may return empty or incomplete results. This happens because the browser considers the page loaded before JavaScript has finished rendering the content.</p>
<p>The simplest solution is to use the <code>gotoOptions.waitUntil</code> parameter set to <code>networkidle0</code> or <code>networkidle2</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;url&quot;: &quot;https://example.com&quot;,&#10;	&quot;gotoOptions&quot;: {&#10;		&quot;waitUntil&quot;: &quot;networkidle0&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For faster responses, advanced users can use <code>waitForSelector</code> to wait for a specific element instead of waiting for all network activity to stop. This requires knowing which CSS selector indicates the content you need has loaded. For more details, refer to <a href="/browser-run/reference/timeouts/">Quick Actions timeouts</a>.</p>
<h3 id="set-a-custom-user-agent">Set a custom user agent</h3>
<p>You can change the user agent at the page level by passing <code>userAgent</code> as a top-level parameter in the JSON body. This is useful if the target website serves different content based on the user agent.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3647.md")
</aside>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
