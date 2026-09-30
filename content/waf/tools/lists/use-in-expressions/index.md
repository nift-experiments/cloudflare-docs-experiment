---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/
  description: Learn how to use lists in rule expressions.
  full_title: Use lists in expressions · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Use lists in expressions · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to use lists in rule expressions."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/index.md"><meta property="og:title" content="Use lists in expressions · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to use lists in rule expressions."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/#page","headline":"Use lists in expressions \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Learn how to use lists in rule expressions.","url":"https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/tools/lists/use-in-expressions/
  schema: 1
---
<p>In the Cloudflare dashboard, there are two options for editing <a href="/ruleset-engine/rules-language/expressions/">expressions</a>:</p>
<ul>
<li><a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-builder">Expression Builder</a>: Allows you to create expressions using drop-down lists, emphasizing a visual approach to defining an expression.</li>
<li><a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor">Expression Editor</a>: A text-only interface that supports advanced features, such as grouping symbols and functions for transforming and validating values.</li>
</ul>
<h2 id="use-a-list-in-the-expression-builder">Use a list in the Expression Builder</h2>
<p>To use a list in the Expression Builder:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15710.md")
</div>
<h2 id="use-a-list-in-the-expression-editor">Use a list in the Expression Editor</h2>
<p>To use a list in the Expression Editor, specify the <code>in</code> operator and use <code>$&lt;list_name&gt;</code> to specify the name of the list.</p>
<p>Examples:</p>
<ul>
<li>Expression matching requests from IP addresses that are in an IP list named <code>office_network</code>:</li>
</ul>
<pre tabindex="0"><code class="language-txt">ip.src in $office_network&#10;</code></pre>
<ul>
<li>Expression matching requests with a source IP address different from IP addresses in the <code>office_network</code> IP list:</li>
</ul>
<pre tabindex="0"><code class="language-txt">not ip.src in $office_network&#10;</code></pre>
<ul>
<li>Expression matching requests from IP addresses in the Cloudflare Open Proxies <a href="/waf/tools/lists/managed-lists/#managed-ip-lists">Managed IP List</a>:</li>
</ul>
<pre tabindex="0"><code class="language-txt">ip.src in $cf.open_proxies&#10;</code></pre>
