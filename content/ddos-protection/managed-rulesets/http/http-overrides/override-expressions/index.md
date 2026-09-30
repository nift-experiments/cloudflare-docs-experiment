---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/override-expressions/
  description: Expression fields and operators for scoping HTTP DDoS Attack Protection overrides.
  full_title: Override expressions for HTTP DDoS Attack Protection · Cloudflare DDoS Protection docs
  head_html: <title>Override expressions for HTTP DDoS Attack Protection · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Expression fields and operators for scoping HTTP DDoS Attack Protection overrides."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/override-expressions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/override-expressions/index.md"><meta property="og:title" content="Override expressions for HTTP DDoS Attack Protection · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Expression fields and operators for scoping HTTP DDoS Attack Protection overrides."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/override-expressions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DDoS Protection"><meta name="pcx_tags" content="Headers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/override-expressions/#page","headline":"Override expressions for HTTP DDoS Attack Protection \u00b7 Cloudflare DDoS Protection docs","description":"Expression fields and operators for scoping HTTP DDoS Attack Protection overrides.","url":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/override-expressions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Headers"]}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/managed-rulesets/http/http-overrides/override-expressions/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7519.md")
</aside>
<p>Set an override expression for the HTTP DDoS Attack Protection managed ruleset to define a specific scope for <a href="/ddos-protection/managed-rulesets/http/override-parameters/#sensitivity-level">sensitivity level</a> or <a href="/ddos-protection/managed-rulesets/http/override-parameters/#action">action</a> adjustments.</p>
<p>For example, you can set different sensitivity levels for different request URI paths: a medium sensitivity level for URI path <code>A</code> and a low sensitivity level for URI path <code>B</code>.</p>
<h2 id="available-expression-fields">Available expression fields</h2>
<p>You can use the following fields in override expressions:</p>
<ul>
<li><code>cf.bot_management.ja3_hash</code></li>
<li><code>cf.bot_management.ja4</code></li>
<li><code>cf.client.bot</code></li>
<li><code>cf.tls_cipher</code></li>
<li><code>cf.tls_client_auth.cert_verified</code></li>
<li><code>cf.tls_version</code></li>
<li><code>cf.verified_bot_category</code></li>
<li><code>http.cookie</code></li>
<li><code>http.host</code></li>
<li><code>http.referer</code></li>
<li><code>http.request.headers</code></li>
<li><code>http.request.headers.names</code></li>
<li><code>http.request.headers.truncated</code></li>
<li><code>http.request.headers.values</code></li>
<li><code>http.request.uri</code></li>
<li><code>http.request.uri.path</code></li>
<li><code>http.request.uri.path.extension</code></li>
<li><code>http.request.uri.query</code></li>
<li><code>http.request.full_uri</code></li>
<li><code>http.request.method</code></li>
<li><code>http.request.version</code></li>
<li><code>http.request.cookies</code></li>
<li><code>http.user_agent</code></li>
<li><code>http.x_forwarded_for</code></li>
<li><code>ip.src</code></li>
<li><code>ip.src.asnum</code></li>
<li><code>ip.src.continent</code></li>
<li><code>ip.src.country</code></li>
<li><code>ip.src.is_in_european_union</code></li>
<li><code>ssl</code></li>
</ul>
<p>Refer to the <a href="/ruleset-engine/rules-language/fields/reference/">Fields reference</a> in the Rules language documentation for more information.</p>
