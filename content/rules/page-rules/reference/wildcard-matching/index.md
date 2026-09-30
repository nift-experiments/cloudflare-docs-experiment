---
cp9:
  canonical: https://developers.cloudflare.com/rules/page-rules/reference/wildcard-matching/
  description: How wildcard and pattern matching works in Page Rules URLs.
  full_title: Wildcard matching in Page Rules · Cloudflare Rules docs
  head_html: <title>Wildcard matching in Page Rules · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="How wildcard and pattern matching works in Page Rules URLs."><link rel="canonical" href="https://developers.cloudflare.com/rules/page-rules/reference/wildcard-matching/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/page-rules/reference/wildcard-matching/index.md"><meta property="og:title" content="Wildcard matching in Page Rules · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How wildcard and pattern matching works in Page Rules URLs."><meta property="og:url" content="https://developers.cloudflare.com/rules/page-rules/reference/wildcard-matching/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/page-rules/reference/wildcard-matching/#page","headline":"Wildcard matching in Page Rules \u00b7 Cloudflare Rules docs","description":"How wildcard and pattern matching works in Page Rules URLs.","url":"https://developers.cloudflare.com/rules/page-rules/reference/wildcard-matching/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/page-rules/reference/wildcard-matching/
  schema: 1
---
<p>You can use the asterisk (<code>*</code>) in any URL segment to match certain patterns. For example, <code>example.com/t*st</code> would match:</p>
<ul>
<li><code>example.com/test</code></li>
<li><code>example.com/toast</code></li>
<li><code>example.com/trust</code></li>
</ul>
<p><code>example.com/foo/* </code>does not match <code>example.com/foo</code>, but <code>example.com/foo*</code> does match.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13097.md")
</aside>
<h2 id="helpful-tips">Helpful tips</h2>
<ul>
<li>To match both <code>http</code> and <code>https</code>, write <code>example.com</code>. Writing <code>*example.com</code> is unnecessary.</li>
<li>To match every page on a domain, write <code>example.com/*</code>. Writing <code>example.com</code> will not work.</li>
<li>To match every page on a domain and its subdomains, write <code>*example.com/*</code>. Writing <code>example.com</code> will not work.</li>
<li>A wildcard (<code>*</code>) in a page rule URL will match even if no characters are present and may include any part of the URL, including the query string.</li>
</ul>
<h2 id="reference-wildcard-matches">Reference wildcard matches</h2>
<p>You can reference a matched wildcard later using the <code>$&lt;X&gt;</code> syntax, where <code>&lt;X&gt;</code> indicates the index of a glob pattern. For example, <code>$1</code> represents the first wildcard match and <code>$2</code> represents the second wildcard match.</p>
<p>The <code>$&lt;X&gt;</code> syntax is especially useful with the <em>Forwarding URL</em> setting. For example, you could forward <code>http://*.example.com/*</code> to <code>http://example.com/images/$1/$2.jpg</code>.</p>
<p>This rule would match <code>http://cloud.example.com/flare.jpg</code>, which would be forwarded to <code>http://example.com/images/cloud/flare.jpg</code>.</p>
<p>To add a <code>$</code> character in the forwarding URL, escape it by adding a backslash <code>\</code> in front like <code>\$</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13096.md")
</aside>
