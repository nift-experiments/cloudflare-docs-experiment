---
cp9:
  canonical: https://developers.cloudflare.com/dns/manage-dns-records/how-to/round-robin-dns/
  description: Distribute traffic across multiple origins with round-robin DNS.
  full_title: Round-robin DNS · Cloudflare DNS docs
  head_html: <title>Round-robin DNS · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Distribute traffic across multiple origins with round-robin DNS."><link rel="canonical" href="https://developers.cloudflare.com/dns/manage-dns-records/how-to/round-robin-dns/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/manage-dns-records/how-to/round-robin-dns/index.md"><meta property="og:title" content="Round-robin DNS · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Distribute traffic across multiple origins with round-robin DNS."><meta property="og:url" content="https://developers.cloudflare.com/dns/manage-dns-records/how-to/round-robin-dns/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/manage-dns-records/how-to/round-robin-dns/#page","headline":"Round-robin DNS \u00b7 Cloudflare DNS docs","description":"Distribute traffic across multiple origins with round-robin DNS.","url":"https://developers.cloudflare.com/dns/manage-dns-records/how-to/round-robin-dns/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/manage-dns-records/how-to/round-robin-dns/
  schema: 1
---
<p>To randomly distribute traffic across multiple servers, set up multiple DNS <code>A</code> or <code>AAAA</code> records for the same hostname.</p>
<p>Use this setup for simple, <a href="https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/">round-robin load balancing</a>. If you need more fine-grained control over traffic distribution — including automatic failover, intelligent routing, and more — set up our <a href="/load-balancing/">add-on load balancing service</a>.</p>
<h2 id="example-scenario">Example scenario</h2>
<p>The following example illustrates how you would distribute traffic intended for <code>www.example.com</code>. Though the example uses <code>A</code> records, you could also use <code>AAAA</code> records.</p>
<p>After <a href="/fundamentals/account/create-account/">creating an account</a> and <a href="/dns/zone-setups/full-setup/setup/">updating your nameservers</a> for <code>example.com</code>, you might <a href="/dns/manage-dns-records/how-to/create-dns-records/">create multiple subdomain DNS records</a> for <code>www</code>:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>IPv4 address</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td><code>www</code></td>
<td><code>192.0.2.1</code></td>
</tr>
<tr>
<td>A</td>
<td><code>www</code></td>
<td><code>192.0.2.2</code></td>
</tr>
<tr>
<td>A</td>
<td><code>www</code></td>
<td><code>192.0.2.3</code></td>
</tr>
</tbody>
</table>
<p>The exact behavior of your DNS routing would depend on the <a href="/dns/proxy-status/">proxy status</a> of each record.</p>
<h3 id="all-records-unproxied">All records unproxied</h3>
<p>If all associated records were unproxied, any request to Cloudflare's nameservers would return the three <code>A</code> records you previously added.</p>
<p>Each client (oftentimes a browser), would decide which IP address to send the request to. If one IP address fails, the client would choose another option. All requests would be sent directly to the origin server (either <code>192.0.2.1</code>, <code>192.0.2.2</code>, or <code>192.0.2.3</code>, using the example above).</p>
<h3 id="all-records-proxied-recommended">All records proxied (recommended)</h3>
<p>If all associated records were proxied, any request to Cloudflare's nameservers would return two <code>A</code> records from Cloudflare's list of IP addresses.</p>
<p>Each client (oftentimes a browser) would decide which Cloudflare IP address to send the request to. Cloudflare would then receive that request and — if Cloudflare needed to contact your origin server — we would pick one of the three IP addresses specified in your DNS records (either <code>192.0.2.1</code>, <code>192.0.2.2</code>, or <code>192.0.2.3</code>, using the example above).</p>
<p>Beyond reducing requests to your origin server, this setup allows your application to take advantage of Cloudflare's <a href="/fundamentals/security/protect-your-origin-server/#zero-downtime-failover">Zero downtime failover</a>. When a request to one IP address fails, Cloudflare automatically retries the request to other IP addresses associated with the same hostname. This behavior prevents end users from experiencing downtime.</p>
<h3 id="unproxied-and-proxied-records">Unproxied and proxied records</h3>
<p>If you have a mix of proxied and unproxied records associated with the same hostname, requests happen as if you had <a href="#all-records-proxied-recommended">all proxied records</a>.</p>
<p>This approach is not typically recommended because it can lead to unexpected behavior. For example, if you had two unproxied records and one proxied record, Cloudflare would treat all records as proxied. However, if you deleted the single proxied record, your remaining two unproxied records would immediately be treated as unproxied.</p>
<p>We recommend either using all proxied or all unproxied records to avoid surprises when you make changes to your DNS records.</p>
