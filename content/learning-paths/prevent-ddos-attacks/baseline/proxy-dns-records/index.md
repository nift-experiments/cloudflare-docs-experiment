---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/proxy-dns-records/
  description: Proxy DNS records through Cloudflare.
  full_title: Proxy DNS records · Cloudflare Learning Paths
  head_html: <title>Proxy DNS records · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Proxy DNS records through Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/proxy-dns-records/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/proxy-dns-records/index.md"><meta property="og:title" content="Proxy DNS records · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Proxy DNS records through Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/proxy-dns-records/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="DDoS Protection,WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/proxy-dns-records/#page","headline":"Proxy DNS records \u00b7 Cloudflare Learning Paths","description":"Proxy DNS records through Cloudflare.","url":"https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/proxy-dns-records/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/prevent-ddos-attacks/baseline/proxy-dns-records/
  schema: 1
---
<p>The first - and often easiest - step of DDoS protection is making sure your DNS records are <a href="/dns/proxy-status/">proxied</a> through Cloudflare.</p>
<h2 id="how-it-works">How it works</h2>
<h3 id="without-cloudflare">Without Cloudflare</h3>
<p>Without Cloudflare, DNS lookups for your application's URL return the IP address of your <a href="https://www.cloudflare.com/learning/cdn/glossary/origin-server/">origin server</a>.</p>
<table>
<thead>
<tr>
<th>URL</th>
<th>Returned IP address</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>example.com</code></td>
<td><code>192.0.2.1</code></td>
</tr>
</tbody>
</table>
<p>When using Cloudflare with <a href="/dns/proxy-status/">unproxied DNS records</a>, DNS lookups for unproxied domains or subdomains also return your origin's IP address.</p>
<p>Another way of thinking about this concept is that visitors directly connect with your origin server.</p>
<pre tabindex="0"><code class="language-mermaid">        flowchart LR&#10;        accTitle: Connections without Cloudflare&#10;        A[Visitor] &lt;-- Connection --&gt; B[Origin server]&#10;</code></pre>
<h3 id="with-cloudflare">With Cloudflare</h3>
<p>With Cloudflare — meaning your domain or subdomain is using <a href="/dns/proxy-status/">proxied DNS records</a> — DNS lookups for your application's URL will resolve to <a href="https://www.cloudflare.com/ips/">Cloudflare anycast IPs</a> instead of their original DNS target.</p>
<table>
<thead>
<tr>
<th>URL</th>
<th>Returned IP address</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>example.com</code></td>
<td><code>104.16.77.250</code></td>
</tr>
</tbody>
</table>
<p>All requests intended for proxied hostnames are directed to Cloudflare first and then forwarded to your origin server.</p>
<pre tabindex="0"><code class="language-mermaid">        flowchart LR&#10;        accTitle: Connections with Cloudflare&#10;        A[Visitor] &lt;-- Connection --&gt; B[Cloudflare global network] &lt;-- Connection --&gt; C[Origin server]&#10;</code></pre>
<p>Cloudflare assigns specific anycast IPs to your domain dynamically and these IPs may change at any time. This is an expected part of the operation of our anycast network and does not affect the proxy behavior described above.</p>
<h2 id="how-it-helps">How it helps</h2>
<h3 id="ddos-protection">DDoS protection</h3>
<p>When your traffic is proxied through Cloudflare, Cloudflare can automatically stop <a href="/ddos-protection/about/">DDoS attacks</a> from ever reaching your application (and your origin server).</p>
<h3 id="caching">Caching</h3>
<p>Proxied traffic also benefits from the default optimizations of the Cloudflare <a href="/cache/">cache</a>. Cloudflare caches <a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">certain types of resources</a> automatically, which both speeds up your application's performance and reduces the overall number of requests.</p>
<h3 id="hides-origin-ip-address">Hides origin IP address</h3>
<p>Proxying your DNS records in Cloudflare also hides the IP address of your origin server (because requests to your application resolve to Cloudflare anycast IP addresses instead).</p>
<p>This obscurity makes it harder for someone to connect directly to your origin, which - by extension - also makes it harder to target your origin with a DDoS attack.</p>
<h2 id="how-to-do-it">How to do it</h2>
<p>Before proxying your records, you should likely <a href="/fundamentals/concepts/cloudflare-ip-addresses/">allow Cloudflare IP addresses</a> at your origin to prevent requests from being blocked.</p>
<p>Then, <a href="/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records">update your Cloudflare DNS records</a> so their <strong>Proxy status</strong> is <strong>Proxied</strong>.</p>
<p><img src="/assets/upstream/images/dns/proxy-status-screenshot.png" alt="Proxy status affects how Cloudflare treats traffic intended for specific DNS records" /></p>
