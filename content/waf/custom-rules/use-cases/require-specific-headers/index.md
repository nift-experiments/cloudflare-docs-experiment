---
cp9:
  canonical: https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-headers/
  description: Require specific HTTP headers in incoming requests.
  full_title: Require specific HTTP headers · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Require specific HTTP headers · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Require specific HTTP headers in incoming requests."><link rel="canonical" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-headers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-headers/index.md"><meta property="og:title" content="Require specific HTTP headers · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Require specific HTTP headers in incoming requests."><meta property="og:url" content="https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-headers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Headers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-headers/#page","headline":"Require specific HTTP headers \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Require specific HTTP headers in incoming requests.","url":"https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-headers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Headers"]}</script>
  markdown: true
  noindex: false
  route: /waf/custom-rules/use-cases/require-specific-headers/
  schema: 1
---
<p>Many organizations qualify traffic based on the presence of specific HTTP request headers. Use the Rules language <a href="/ruleset-engine/rules-language/fields/reference/?field-category=Headers&amp;search-term=http.request">HTTP request header fields</a> to target requests with specific headers.</p>
<h2 id="example-1-require-presence-of-http-header">Example 1: Require presence of HTTP header</h2>
<p>This example custom rule uses the <a href="/ruleset-engine/rules-language/fields/reference/http.request.headers.names/"><code>http.request.headers.names</code></a> field to look for the presence of an <code>X-CSRF-Token</code> header. The <a href="/ruleset-engine/rules-language/functions/#lower"><code>lower()</code></a> transformation function converts the header name to lowercase so that the expression is case-insensitive.</p>
<p>When the <code>X-CSRF-Token</code> header is missing, Cloudflare blocks the request.</p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Use the expression editor:<br/>
<code>not any(lower(http.request.headers.names[*])[*] eq &quot;x-csrf-token&quot;) and (http.request.full_uri eq &quot;https://www.example.com/somepath&quot;)</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Block</em></p>
</li>
</ul>
<h2 id="example-2-require-http-header-with-a-specific-value">Example 2: Require HTTP header with a specific value</h2>
<p>This example custom rule uses the <a href="/ruleset-engine/rules-language/fields/reference/http.request.headers/"><code>http.request.headers</code></a> field to look for the presence of the <code>X-Example-Header</code> header and to get its value (if any). When the <code>X-Example-Header</code> header is missing or it does not have the value <code>example-value</code>, Cloudflare blocks the request.</p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Use the expression editor:<br/>
<code>not any(http.request.headers[&quot;x-example-header&quot;][*] eq &quot;example-value&quot;) and (http.request.uri.path eq &quot;/somepath&quot;)</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Block</em></p>
</li>
</ul>
<p>The keys in the <code>http.request.headers</code> field, corresponding to HTTP header names, are in lowercase.</p>
<p>In this example the header name is case-insensitive, but the header value is case-sensitive.</p>
