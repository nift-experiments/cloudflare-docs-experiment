---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/setup/windows/
  description: Configure 1.1.1.1 on Windows.
  full_title: Set up 1.1.1.1 on Windows · Cloudflare 1.1.1.1 docs
  head_html: <title>Set up 1.1.1.1 on Windows · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure 1.1.1.1 on Windows."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/setup/windows/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/setup/windows/index.md"><meta property="og:title" content="Set up 1.1.1.1 on Windows · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure 1.1.1.1 on Windows."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/setup/windows/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/setup/windows/#page","headline":"Set up 1.1.1.1 on Windows \u00b7 Cloudflare 1.1.1.1 docs","description":"Configure 1.1.1.1 on Windows.","url":"https://developers.cloudflare.com/1.1.1.1/setup/windows/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/setup/windows/
  schema: 1
---
<h2 id="windows-10">Windows 10</h2>
<p>Take note of any DNS addresses you might have set up, and save them in a safe place in case you need to use them later.</p>
<ol>
<li>Select the <strong>Start menu</strong> &gt; <strong>Settings</strong>.</li>
<li>On <strong>Network and Internet</strong>, select <strong>Change Adapter Options</strong>.</li>
<li>Right-click on the Ethernet or Wi-Fi network you are connected to and select <strong>Properties</strong>.</li>
<li>Select <strong>Internet Protocol Version 4</strong>.</li>
<li>Select <strong>Properties</strong> &gt; <strong>Use the following DNS server addresses</strong>.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv4:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1747.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1748.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1749.md")
</div></details>
<ol start="7">
<li>Select <strong>OK</strong>.</li>
<li>Select <strong>Internet Protocol Version 6</strong>.</li>
<li>Select <strong>Properties</strong> &gt; <strong>Use the following DNS server addresses</strong>.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv6:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1750.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1751.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1752.md")
</div></details>
<ol start="11">
<li>Select <strong>OK</strong>.</li>
</ol>
<h2 id="windows-11">Windows 11</h2>
<p>Take note of any DNS addresses you might have set up, and save them in a safe place in case you need to use them later.</p>
<ol>
<li>Select the <strong>Start menu</strong> &gt; <strong>Settings</strong>.</li>
<li>On <strong>Network and Internet</strong>, select the adapter you want to configure — such as your Ethernet adapter or Wi-Fi card.</li>
<li>Scroll to <strong>DNS server assignment</strong> and select <strong>Edit</strong>.</li>
<li>Select the <strong>Automatic (DHCP)</strong> drop-down menu &gt; <strong>Manual</strong>.</li>
<li>Select the <strong>IPv4</strong> toggle to turn it on.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv4:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1753.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1754.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1755.md")
</div></details>
<ol start="7">
<li>Select the <strong>IPv6</strong> toggle.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv6:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1756.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1757.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1758.md")
</div></details>
<ol start="9">
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1746.md")
</aside>
<h2 id="encrypt-your-dns-queries">Encrypt your DNS queries</h2>
<p>1.1.1.1 supports DNS over TLS (DoT) and DNS over HTTPS (DoH), two standards developed for encrypting plaintext DNS traffic. This prevents untrustworthy entities from interpreting and manipulating your queries. For more information on how to encrypt your DNS queries, please refer to the <a href="/1.1.1.1/encryption/">Encrypted DNS documentation</a>.</p>
