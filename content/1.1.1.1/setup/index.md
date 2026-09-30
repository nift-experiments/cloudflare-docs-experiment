---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/setup/
  description: Learn how to set up Cloudflare's 1.1.1.1 DNS resolver for enhanced security and privacy. Protect against malware and adult content with easy configuration.
  full_title: Set up Cloudflare 1.1.1.1 resolver · Cloudflare 1.1.1.1 docs
  head_html: <title>Set up Cloudflare 1.1.1.1 resolver · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to set up Cloudflare&#x27;s 1.1.1.1 DNS resolver for enhanced security and privacy. Protect against malware and adult content with easy configuration."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/setup/index.md"><meta property="og:title" content="Set up Cloudflare 1.1.1.1 resolver · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to set up Cloudflare&#x27;s 1.1.1.1 DNS resolver for enhanced security and privacy. Protect against malware and adult content with easy configuration."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_tags" content="Phishing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/setup/#page","headline":"Set up Cloudflare 1.1.1.1 resolver \u00b7 Cloudflare 1.1.1.1 docs","description":"Learn how to set up Cloudflare's 1.1.1.1 DNS resolver for enhanced security and privacy. Protect against malware and adult content with easy configuration.","url":"https://developers.cloudflare.com/1.1.1.1/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Phishing"]}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/setup/
  schema: 1
---
<p>By default, your devices use a <a href="https://www.cloudflare.com/learning/dns/what-is-dns/">DNS server</a> provided by your Internet service provider (ISP). You can change this to use 1.1.1.1 instead, which gives you faster and more private DNS resolution. Some <a href="/1.1.1.1/infrastructure/network-operators/">ISPs and network equipment providers</a> already partner with Cloudflare to offer this.</p>
<p>If your provider does not use Cloudflare, follow the instructions for your device or router below.</p>
<details class="nb-details"><summary>Device or router specific guides</summary><div class="nb-details-body">
@input("content/.markup/bodies/1795.md")
</div></details>
<p>You can also set up <a href="#1111-for-families">1.1.1.1 for Families</a> for additional protection against malware and adult content on your home network. 1.1.1.1 for Families uses the same <a href="/1.1.1.1/privacy/public-dns-resolver/">privacy commitments</a> as the standard 1.1.1.1 resolver.</p>
<hr />
<h2 id="1-1-1-1-for-families">1.1.1.1 for Families</h2>
<p>1.1.1.1 for Families automatically blocks DNS queries to domains associated with malware, phishing, or (optionally) adult content.</p>
<p>1.1.1.1 for Families has two options:</p>
<details class="nb-details"><summary>Block malware</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1796.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1797.md")
</div></details>
<p>When a queried domain is classified as malicious, Cloudflare returns the address <code>0.0.0.0</code> instead of the real address. This prevents your device from connecting to the blocked site.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="domain-miscategorization">Domain miscategorization</h3>
@markup("md", "content/.markup/bodies/1794.md")
</aside>
<h3 id="test-1-1-1-1-for-families">Test 1.1.1.1 for Families</h3>
<p>After configuring 1.1.1.1 for Families, verify that filtering is working with the following test URLs:</p>
<ul>
<li><a href="https://malware.testcategory.com/">https://malware.testcategory.com/</a> — Tests whether known malware domains are blocked.</li>
<li><a href="https://nudity.testcategory.com/">https://nudity.testcategory.com/</a> — Tests whether adult content and malware domains are blocked.</li>
</ul>
<h3 id="dns-over-https-doh">DNS over HTTPS (DoH)</h3>
<p>DNS over HTTPS (DoH) encrypts your DNS queries by sending them as HTTPS requests. This prevents anyone between your device and the resolver — such as your ISP or a network attacker — from seeing which domains you look up. For more information, refer to the <a href="https://www.cloudflare.com/learning/dns/dns-over-tls/">Learning Center article on DNS encryption</a>.</p>
<p>To configure an encrypted DoH connection to 1.1.1.1 for Families, enter one of the following URLs in your DoH-compatible client or router:</p>
<details class="nb-details"><summary>Block malware</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1798.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1799.md")
</div></details>
<h3 id="dns-over-tls-dot">DNS over TLS (DoT)</h3>
<p>DNS over TLS (DoT) encrypts DNS queries using TLS on a dedicated port (<code>853</code>). Like DoH, it prevents eavesdropping on your DNS traffic. For more information, refer to the <a href="https://www.cloudflare.com/learning/dns/dns-over-tls/">Learning Center article on DNS encryption</a>.</p>
<p>To configure an encrypted DoT connection to 1.1.1.1 for Families, enter one of the following hostnames in your DoT-compatible client or router:</p>
<details class="nb-details"><summary>Block malware</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1800.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1801.md")
</div></details>
