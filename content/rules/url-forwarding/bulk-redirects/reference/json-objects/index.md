---
cp9:
  canonical: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/json-objects/
  description: JSON object structure for Bulk Redirect API requests.
  full_title: Bulk Redirects API JSON objects · Cloudflare Rules docs
  head_html: <title>Bulk Redirects API JSON objects · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="JSON object structure for Bulk Redirect API requests."><link rel="canonical" href="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/json-objects/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/json-objects/index.md"><meta property="og:title" content="Bulk Redirects API JSON objects · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="JSON object structure for Bulk Redirect API requests."><meta property="og:url" content="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/json-objects/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/json-objects/#page","headline":"Bulk Redirects API JSON objects \u00b7 Cloudflare Rules docs","description":"JSON object structure for Bulk Redirect API requests.","url":"https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/json-objects/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects"]}</script>
  markdown: true
  noindex: false
  route: /rules/url-forwarding/bulk-redirects/reference/json-objects/
  schema: 1
---
<h2 id="bulk-redirect-rule">Bulk Redirect Rule</h2>
<p>A fully populated Bulk Redirect Rule object has the following JSON structure:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;action&quot;: &quot;redirect&quot;,&#10;	&quot;expression&quot;: &quot;http.request.full_uri in $&lt;LIST_NAME&gt;&quot;,&#10;	&quot;action_parameters&quot;: {&#10;		&quot;from_list&quot;: {&#10;			&quot;name&quot;: &quot;&lt;LIST_NAME&gt;&quot;,&#10;			&quot;key&quot;: &quot;http.request.full_uri&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>The JSON object properties must comply with the following:</p>
<ul>
<li>
<p><code>action</code> must be <code>redirect</code></p>
</li>
<li>
<p><code>action_parameters</code> must contain a <code>from_list</code> object with additional settings.</p>
</li>
<li>
<p><code>from_list</code> must contain the following properties:</p>
<ul>
<li><code>name</code>: The name of an existing Bulk Redirect List to associate with the current Bulk Redirect Rule.</li>
<li><code>key</code>: An expression that defines the value that will be matched against the configured URL redirect's source URL values, following the rules of the <a href="/rules/url-forwarding/bulk-redirects/how-it-works/#url-matching-algorithm">URL matching algorithm</a>. Refer to <a href="/rules/url-forwarding/bulk-redirects/concepts/#bulk-redirect-rules">Bulk Redirects concepts</a> for more information.</li>
</ul>
</li>
<li>
<p><code>expression</code> must reference the request field used in the <code>key</code> property. Refer to <a href="/rules/url-forwarding/bulk-redirects/concepts/#bulk-redirect-rules">Bulk Redirects concepts</a> for more information.</p>
</li>
</ul>
<h2 id="url-redirect-list-item">URL redirect list item</h2>
<p>A fully populated URL redirect list item object has the following JSON structure:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;id&quot;: &quot;7c5dae5552338874e5053f2534d2767a&quot;,&#10;	&quot;redirect&quot;: {&#10;		&quot;source_url&quot;: &quot;https://example.com/blog&quot;,&#10;		&quot;target_url&quot;: &quot;https://example.com/blog/latest&quot;,&#10;		&quot;status_code&quot;: 301,&#10;		&quot;include_subdomains&quot;: false,&#10;		&quot;subpath_matching&quot;: false,&#10;		&quot;preserve_query_string&quot;: false,&#10;		&quot;preserve_path_suffix&quot;: true&#10;	},&#10;	&quot;created_on&quot;: &quot;2021-10-11T12:39:02Z&quot;,&#10;	&quot;modified_on&quot;: &quot;2021-10-11T12:39:02Z&quot;&#10;}&#10;</code></pre>
<p>For details on the <code>redirect</code> object properties, refer to <a href="/rules/url-forwarding/bulk-redirects/reference/parameters/">URL redirect parameters</a>.</p>
