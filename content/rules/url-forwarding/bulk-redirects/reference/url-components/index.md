---
cp9:
  canonical: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/
  description: URL components used in Bulk Redirect source and target URLs.
  full_title: Supported URL components in Bulk Redirects · Cloudflare Rules docs
  head_html: <title>Supported URL components in Bulk Redirects · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="URL components used in Bulk Redirect source and target URLs."><link rel="canonical" href="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/index.md"><meta property="og:title" content="Supported URL components in Bulk Redirects · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="URL components used in Bulk Redirect source and target URLs."><meta property="og:url" content="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/#page","headline":"Supported URL components in Bulk Redirects \u00b7 Cloudflare Rules docs","description":"URL components used in Bulk Redirect source and target URLs.","url":"https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects"]}</script>
  markdown: true
  noindex: false
  route: /rules/url-forwarding/bulk-redirects/reference/url-components/
  schema: 1
---
<p>The source and target URLs of a URL redirect support different URL components.</p>
<p>The provided URL component examples in the reference table are based on the following URL:</p>
<pre tabindex="0"><code class="language-txt">https://user:password@www.example.com:443/search?q=term#results&#10;</code></pre>
<table>
<thead>
<tr>
<th>URL component</th>
<th>Supported in source URL <sup><a href="#footnote-1">1</a></sup></th>
<th>Supported in target URL</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Scheme</strong><br/>For example:<br/><code>https</code></td>
<td>Yes, <code>http</code> or <code>https</code> only<br/>(optional)</td>
<td>Yes</td>
</tr>
<tr>
<td><strong>User information</strong><br/>For example:<br/><code>user:password</code></td>
<td>No</td>
<td>Yes (optional)</td>
</tr>
<tr>
<td><strong>Host</strong><br/>For example:<br/><code>www.example.com</code></td>
<td>Yes</td>
<td>Yes (optional)</td>
</tr>
<tr>
<td><strong>Port</strong><br/>For example:<br/><code>443</code></td>
<td>No</td>
<td>Yes (optional)</td>
</tr>
<tr>
<td><strong>Path</strong><br/>For example:<br/><code>/search</code></td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td><strong>Query string</strong><br/>For example:<br/><code>q=term</code></td>
<td>No</td>
<td>Yes, if <a href="/rules/url-forwarding/bulk-redirects/reference/parameters/#preserve-query-string"><strong>Preserve query string</strong></a> is <code>false</code> (optional)<br/><br/>You can only add a query string to the target URL if you do not keep the original query string (that is, if <strong>Preserve query string</strong> is <code>false</code>). If you set <strong>Preserve query string</strong> to <code>true</code>, the query string of the request will be passed along <a href="/rules/url-forwarding/bulk-redirects/how-it-works/#matching-the-source-url-of-redirects">when there is a match for the source URL</a>.</td>
</tr>
<tr>
<td><strong>Fragment</strong><br/>For example:<br/><code>results</code></td>
<td>No</td>
<td>Yes (optional)</td>
</tr>
</tbody>
</table>
<p>Bulk Redirects also support target URLs without an authority component <sup><a href="#footnote-2">2</a></sup>, like the following URL:</p>
<pre tabindex="0"><code class="language-txt">magnet:?xt=urn:btih:2bd9d334e8d1e5bd7768755173222db5c6dea13b&amp;dn=archlinux-2021.07.01-x86_64.iso&#10;</code></pre>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">**Supported in source URL** = **No** means that you cannot include the component in the source URL to match against the URL of incoming requests.</li>
<li id="footnote-2">The URL authority is the combination of user information, host, and port components.</li></ol></section>
