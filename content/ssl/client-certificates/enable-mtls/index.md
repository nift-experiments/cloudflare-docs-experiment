---
cp9:
  canonical: https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/
  description: Enable mutual TLS to require client certificates for your host.
  full_title: Enable mTLS · Cloudflare SSL/TLS docs
  head_html: <title>Enable mTLS · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable mutual TLS to require client certificates for your host."><link rel="canonical" href="https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/index.md"><meta property="og:title" content="Enable mTLS · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable mutual TLS to require client certificates for your host."><meta property="og:url" content="https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="mTLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/#page","headline":"Enable mTLS \u00b7 Cloudflare SSL/TLS docs","description":"Enable mutual TLS to require client certificates for your host.","url":"https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["mTLS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/client-certificates/enable-mtls/
  schema: 1
---
<p>You can enable mutual Transport Layer Security (mTLS) for any hostname. For more information, refer to the <a href="/ssl/client-certificates/">Client certificates overview</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cloudflare-issued-or-byoca">Cloudflare-issued or BYOCA</h3>
@markup("md", "content/.markup/bodies/14026.md")
</aside>
<p>To enable mTLS for a host from the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Client Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>On the <strong>Hosts</strong> section of the <strong>Client Certificates</strong> card, select <strong>Edit</strong>.</li>
<li>Enter the name of a host in your current domain.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14025.md")
</aside>
4. Select **Save** to confirm.
<h2 id="cas-in-use">CAs in use</h2>
<p>As explained in the <a href="/ssl/client-certificates/#how-it-works">Client certificates overview</a>, Cloudflare validates client certificates against CAs set at account level. This means that these certificates can be used for validation across multiple zones/domains (<code>example.com</code>), as long as the zones are under the same Cloudflare account and you have enabled mTLS for the host.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="bring-your-own-ca">Bring your own CA</h3>
@markup("md", "content/.markup/bodies/14024.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<p>After enabling mTLS for your host, you can:</p>
<ul>
<li>Enforce mTLS with a WAF custom rule. Select <strong>Create mTLS Rule</strong> on the dashboard to use a template, or refer to our <a href="/learning-paths/mtls/mtls-app-security/#3-validate-the-client-certificate-in-the-waf">mTLS at Cloudflare learning path</a> for further guidance.</li>
<li>Enforce mTLS with <a href="/api-shield/security/mtls/configure/">API Shield</a>. While API Shield is <strong>not required</strong> to use mTLS, many teams may use mTLS to protect their APIs.</li>
</ul>
