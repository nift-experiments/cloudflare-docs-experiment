---
cp9:
  canonical: https://developers.cloudflare.com/rules/compression-rules/
  description: Customize response compression algorithms for specific content types and file extensions.
  full_title: Compression Rules · Cloudflare Rules docs
  head_html: <title>Compression Rules · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Customize response compression algorithms for specific content types and file extensions."><link rel="canonical" href="https://developers.cloudflare.com/rules/compression-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/compression-rules/index.md"><meta property="og:title" content="Compression Rules · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Customize response compression algorithms for specific content types and file extensions."><meta property="og:url" content="https://developers.cloudflare.com/rules/compression-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/compression-rules/#page","headline":"Compression Rules \u00b7 Cloudflare Rules docs","description":"Customize response compression algorithms for specific content types and file extensions.","url":"https://developers.cloudflare.com/rules/compression-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/compression-rules/
  schema: 1
---
<p>Use Compression Rules to customize the compression applied to responses from Cloudflare's global network to your website visitors, based on the file extension and content type. Compression Rules are powered by the <a href="/ruleset-engine/">Ruleset Engine</a>.</p>
<p>Cloudflare <a href="/speed/optimization/content/compression/">compresses some responses by default</a>, based on the content type. With Compression Rules, you can customize the default behavior, which includes defining preferred compression algorithms for particular file types.</p>
<p>When a compression rule matches and lists several compression algorithms (such as gzip and Brotli), Cloudflare selects the first algorithm from your list that the visitor's browser supports. Cloudflare determines browser support from the <code>accept-encoding</code> HTTP request header, which browsers send automatically to indicate which compression formats they can decompress. If multiple compression rules match the same request, the last matching rule takes precedence.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13027.md")
</aside>
<h2 id="get-started">Get started</h2>
<p>Cloudflare provides you with rules templates for common use cases.</p>
<ol>
<li>In the Cloudflare dashboard, go to the Rules <strong>Overview</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Templates</strong>, and then select one of the available templates.</li>
</ol>
<p>You can also refer to the <a href="/rules/examples/">Examples gallery</a> in the developer docs.</p>
<p>Alternatively, follow the instructions in the following pages to get started:</p>
<ul>
<li><a href="/rules/compression-rules/create-dashboard/">Create a compression rule in the dashboard</a></li>
<li><a href="/rules/compression-rules/create-api/">Create a compression rule via Cloudflare API</a></li>
</ul>
<hr />
<h2 id="availability">Availability</h2>
<p>Compression Rules are available in all Cloudflare plans.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Number of rules</td>
<td>10</td>
<td>25</td>
<td>50</td>
<td>300</td>
</tr>
</tbody>
</table>
<h2 id="relevant-fields">Relevant fields</h2>
<p>The following fields are commonly used in expressions of compression rules:</p>
<table>
<thead>
<tr>
<th>Field in <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-builder">Expression Builder</a></th>
<th>Field name</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Media Type</em></td>
<td><a href="/ruleset-engine/rules-language/fields/reference/http.response.content_type.media_type/"><code>http.response.content_type.media_type</code></a></td>
</tr>
<tr>
<td><em>File extension</em></td>
<td><a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.path.extension/"><code>http.request.uri.path.extension</code></a></td>
</tr>
<tr>
<td>N/A</td>
<td><a href="/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.path.extension/"><code>raw.http.request.uri.path.extension</code></a></td>
</tr>
</tbody>
</table>
<h2 id="important-remarks">Important remarks</h2>
<ul>
<li>
<p>If a compression rule matches but the visitor's browser does not support any of the compression algorithms configured in the rule (based on the <code>accept-encoding</code> request header), the response will not be compressed.</p>
</li>
<li>
<p>If a compression rule matches but the origin server's response includes a <code>cache-control: no-transform</code> HTTP header, the compression rule will not modify the response. Origin servers use this header to indicate that intermediaries (like Cloudflare) should not alter the response body.</p>
</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>When troubleshooting Compression Rules, use <a href="/rules/trace-request/">Cloudflare Trace</a> to determine if a rule is triggering for a specific URL.</p>
