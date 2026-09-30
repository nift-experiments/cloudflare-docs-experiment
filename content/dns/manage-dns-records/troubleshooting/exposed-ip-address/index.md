---
cp9:
  canonical: https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/exposed-ip-address/
  description: Understand and resolve warnings about DNS records that expose your origin server IP address.
  full_title: Exposed IP addresses · Cloudflare DNS docs
  head_html: <title>Exposed IP addresses · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand and resolve warnings about DNS records that expose your origin server IP address."><link rel="canonical" href="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/exposed-ip-address/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/exposed-ip-address/index.md"><meta property="og:title" content="Exposed IP addresses · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand and resolve warnings about DNS records that expose your origin server IP address."><meta property="og:url" content="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/exposed-ip-address/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="DNS"><meta name="pcx_tags" content="Proxying"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/exposed-ip-address/#page","headline":"Exposed IP addresses \u00b7 Cloudflare DNS docs","description":"Understand and resolve warnings about DNS records that expose your origin server IP address.","url":"https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/exposed-ip-address/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Proxying"]}</script>
  markdown: true
  noindex: false
  route: /dns/manage-dns-records/troubleshooting/exposed-ip-address/
  schema: 1
---
<p>When your DNS records are <span class="nb-glossary-tooltip" title="proxy status">proxied</span>, Cloudflare speeds up and protects your site.</p>
<p>A <code>dig</code> query against your proxied apex domain returns a Cloudflare IP address. This way, your origin server's IP address remains concealed from the public. Proxy benefits only apply to HTTP traffic.</p>
<p>When your server's IP address is exposed, your server is more vulnerable to direct attacks. It is still possible (but more difficult) for attackers to determine your origin server IP address when proxying traffic to Cloudflare.</p>
<hr />
<h2 id="dashboard-warnings">Dashboard warnings</h2>
<p>The Cloudflare dashboard displays warnings when DNS records may expose your origin server's IP address. These warnings do not block or affect traffic to your site.</p>
<p>When your zone has DNS records that are not proxied, the <strong>DNS Records</strong> page displays the following banner:</p>
<p><code>Proxying is required for most security and performance features. Set your DNS records to proxied by clicking &quot;Edit&quot; in the table below, to benefit from DDoS protection, security rules, caching, and more.</code></p>
<p>Individual DNS records may also display warnings. The specific message depends on whether the record can be proxied.</p>
<hr />
<h2 id="dns-records-that-should-be-proxied">DNS records that should be proxied</h2>
<p>Cloudflare recommends <span class="nb-glossary-tooltip" title="proxy status">proxying</span> any record that handles HTTP traffic so that a <code>dig</code> query returns a Cloudflare IP address instead of your origin server IP address.</p>
<p>To take advantage of Cloudflare's performance and security benefits, proxy <code>A</code>, <code>AAAA</code>, and <code>CNAME</code> records.</p>
<hr />
<h2 id="dns-records-that-should-be-dns-only">DNS records that should be DNS-only</h2>
<p>Some DNS records need to remain DNS-only. For example, you may have to host multiple services (for example, a website and email) on the same physical server.</p>
<p>When a DNS-only record points to the same origin server as a proxied record, a <code>dig</code> query against that record reveals your origin server's IP address. This makes it easier for potential attackers to target your origin server directly.</p>
<p>To mitigate this risk:</p>
<ul>
<li>Analyze the impact of hosting multiple services on the same origin server in cases when you cannot avoid having DNS-only records.</li>
<li>Proxy all records that share the same origin IP address as your apex domain and can be safely proxied through Cloudflare.</li>
</ul>
