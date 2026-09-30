---
cp9:
  canonical: https://developers.cloudflare.com/rules/transform/request-header-modification/reference/fields-functions/
  description: Available fields and functions for request header modification rules.
  full_title: Available fields and functions · Cloudflare Rules docs
  head_html: <title>Available fields and functions · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Available fields and functions for request header modification rules."><link rel="canonical" href="https://developers.cloudflare.com/rules/transform/request-header-modification/reference/fields-functions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/transform/request-header-modification/reference/fields-functions/index.md"><meta property="og:title" content="Available fields and functions · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available fields and functions for request header modification rules."><meta property="og:url" content="https://developers.cloudflare.com/rules/transform/request-header-modification/reference/fields-functions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/transform/request-header-modification/reference/fields-functions/#page","headline":"Available fields and functions \u00b7 Cloudflare Rules docs","description":"Available fields and functions for request header modification rules.","url":"https://developers.cloudflare.com/rules/transform/request-header-modification/reference/fields-functions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/transform/request-header-modification/reference/fields-functions/
  schema: 1
---
<p>The available fields when setting an HTTP request header value using an expression are the following:</p>
<ul>
<li><code>cf.bot_management.*</code></li>
<li><code>cf.client.bot</code></li>
<li><code>cf.verified_bot_category</code></li>
<li><code>cf.edge.server_ip</code></li>
<li><code>cf.edge.server_port</code></li>
<li><code>cf.edge.client_port</code></li>
<li><code>cf.edge.client_tcp</code></li>
<li><code>cf.edge.l4.delivery_rate</code></li>
<li><code>cf.hostname.metadata</code></li>
<li><code>cf.zone.name</code></li>
<li><code>cf.random_seed</code></li>
<li><code>cf.ray_id</code></li>
<li><code>cf.timings.client_quic_rtt_msec</code></li>
<li><code>cf.timings.client_tcp_rtt_msec</code></li>
<li><code>cf.tls_version</code></li>
<li><code>cf.tls_cipher</code></li>
<li><code>cf.tls_client_hello_length</code></li>
<li><code>cf.tls_client_random</code></li>
<li><code>cf.tls_client_extensions_sha1</code></li>
<li><code>cf.tls_client_extensions_sha1_le</code></li>
<li><code>cf.tls_client_ciphers_sha1</code></li>
<li><code>cf.tls_client_auth.*</code></li>
<li><code>cf.worker.upstream_zone</code></li>
<li><code>cf.fraud.email_risk</code></li>
<li><code>http.cookie</code></li>
<li><code>http.host</code></li>
<li><code>http.referer</code></li>
<li><code>http.request.accepted_languages</code></li>
<li><code>http.request.cookies</code></li>
<li><code>http.request.headers</code></li>
<li><code>http.request.headers.*</code></li>
<li><code>http.request.method</code></li>
<li><code>http.request.body.form</code></li>
<li><code>http.request.body.form.*</code></li>
<li><code>http.request.body.multipart</code></li>
<li><code>http.request.body.multipart.*</code></li>
<li><code>http.request.body.raw</code></li>
<li><code>http.request.body.size</code></li>
<li><code>http.request.body.truncated</code></li>
<li><code>http.request.timestamp.sec</code></li>
<li><code>http.request.timestamp.msec</code></li>
<li><code>http.request.full_uri</code></li>
<li><code>http.request.uri</code></li>
<li><code>http.request.uri.*</code></li>
<li><code>http.request.version</code></li>
<li><code>raw.http.request.full_uri</code></li>
<li><code>raw.http.request.uri</code></li>
<li><code>raw.http.request.uri.*</code></li>
<li><code>raw.http.request.headers</code></li>
<li><code>raw.http.request.headers.*</code></li>
<li><code>http.user_agent</code></li>
<li><code>http.x_forwarded_for</code></li>
<li><code>ip.src</code></li>
<li><code>ip.src.lat</code></li>
<li><code>ip.src.lon</code></li>
<li><code>ip.src.asnum</code></li>
<li><code>ip.src.city</code></li>
<li><code>ip.src.country</code></li>
<li><code>ip.src.continent</code></li>
<li><code>ip.src.metro_code</code></li>
<li><code>ip.src.postal_code</code></li>
<li><code>ip.src.region</code></li>
<li><code>ip.src.region_code</code></li>
<li><code>ip.src.is_in_european_union</code></li>
<li><code>ip.src.subdivision_1_iso_code</code></li>
<li><code>ip.src.subdivision_2_iso_code</code></li>
<li><code>ssl</code></li>
<li><code>http.request.jwt.claims</code></li>
<li><code>http.request.jwt.claims.*</code></li>
<li><code>cf.fraud_detection.disposable_email</code></li>
<li><code>cf.sequence.current_op</code></li>
<li><code>cf.sequence.msec_since_op</code></li>
<li><code>cf.sequence.previous_ops</code></li>
<li><code>cf.waf.auth_detected</code></li>
<li><code>cf.waf.credential_check.*</code></li>
<li><code>cf.waf.score</code></li>
<li><code>cf.waf.score.*</code></li>
</ul>
<p>Refer to <a href="/ruleset-engine/rules-language/fields/reference/">Fields</a> for reference information on these fields.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/13181.md")
</aside>
<p>For information on the available functions, refer to <a href="/ruleset-engine/rules-language/functions/">Functions</a>.</p>
