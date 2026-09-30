---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/setup/macos/
  description: Configure 1.1.1.1 on macOS.
  full_title: Set up 1.1.1.1 on macOS · Cloudflare 1.1.1.1 docs
  head_html: <title>Set up 1.1.1.1 on macOS · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure 1.1.1.1 on macOS."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/setup/macos/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/setup/macos/index.md"><meta property="og:title" content="Set up 1.1.1.1 on macOS · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure 1.1.1.1 on macOS."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/setup/macos/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/setup/macos/#page","headline":"Set up 1.1.1.1 on macOS \u00b7 Cloudflare 1.1.1.1 docs","description":"Configure 1.1.1.1 on macOS.","url":"https://developers.cloudflare.com/1.1.1.1/setup/macos/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/setup/macos/
  schema: 1
---
<p>These steps configure 1.1.1.1 as the DNS resolver for a specific network service (such as Wi-Fi or Ethernet) on your Mac.</p>
<p>Take note of any DNS addresses you might have set up, and save them in a safe place in case you need to use them later.</p>
<ol>
<li>Go to <strong>System Settings</strong>. You can find it by pressing <code>CMD + Space</code> on your keyboard and typing <code>System Settings</code>.</li>
<li>Go to <strong>Network</strong>.</li>
<li>Select a network service.</li>
<li>Select <strong>Details</strong>.</li>
<li>Go to <strong>DNS</strong>.</li>
<li>Under <strong>DNS Servers</strong>, select <strong>Add</strong>.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv4:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1766.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1767.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1768.md")
</div></details>
<ol start="8">
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv6:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1769.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1770.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1771.md")
</div></details>
<ol start="9">
<li>Select <strong>OK</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1765.md")
</aside>
<h2 id="encrypt-your-dns-queries">Encrypt your DNS queries</h2>
<p>1.1.1.1 supports DNS over TLS (DoT) and DNS over HTTPS (DoH), two standards developed for encrypting plaintext DNS traffic. This prevents untrustworthy entities from interpreting and manipulating your queries. For more information on how to encrypt your DNS queries, please refer to the <a href="/1.1.1.1/encryption/">Encrypted DNS documentation</a>.</p>
