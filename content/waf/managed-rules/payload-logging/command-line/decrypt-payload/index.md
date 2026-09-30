---
cp9:
  canonical: https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/decrypt-payload/
  description: Decrypt matched rule payloads using the command-line tool.
  full_title: Decrypt the payload content in the command line · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Decrypt the payload content in the command line · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Decrypt matched rule payloads using the command-line tool."><link rel="canonical" href="https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/decrypt-payload/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/decrypt-payload/index.md"><meta property="og:title" content="Decrypt the payload content in the command line · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Decrypt matched rule payloads using the command-line tool."><meta property="og:url" content="https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/decrypt-payload/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="CLI,Logging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/decrypt-payload/#page","headline":"Decrypt the payload content in the command line \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Decrypt matched rule payloads using the command-line tool.","url":"https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/decrypt-payload/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["CLI","Logging"]}</script>
  markdown: true
  noindex: false
  route: /waf/managed-rules/payload-logging/command-line/decrypt-payload/
  schema: 1
---
<p>Use the <code>matched-data-cli</code> tool to decrypt a payload in the command line.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15663.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15662.md")
</aside>
<h2 id="example">Example</h2>
<p>The following example creates two files — one with the private key and another one with the encrypted payload — and runs the <code>matched-data-cli</code> tool to decrypt the payload in the <code>encrypted_payload.txt</code> file:</p>
<pre tabindex="0"><code class="language-sh">~ cd matched-data-cli&#10;&#10;printf &quot;uBS5eBttHrqkdY41kbZPdvYnNz8Vj0TvKIUpjB1y/GA=&quot; &gt; private_key.txt &amp;&amp; chmod 400 private_key.txt&#10;&#10;printf &quot;AzTY6FHajXYXuDMUte82wrd+1n5CEHPoydYiyd3FMg5IEQAAAAAAAAA0lOhGXBclw8pWU5jbbYuepSIJN5JohTtZekLliJBlVWk=&quot; &gt; encrypted_payload.txt&#10;&#10;decrypt -k private_key.txt encrypted_payload.txt&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">test matched data&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="encryption-formats">Encryption formats</h3>
@markup("md", "content/.markup/bodies/15661.md")
</aside>
