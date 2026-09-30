---
cp9:
  canonical: https://developers.cloudflare.com/network/ipv6-compatibility/
  description: Configure IPv6 compatibility for your Cloudflare domain.
  full_title: IPv6 compatibility · Cloudflare Network settings docs
  head_html: <title>IPv6 compatibility · Cloudflare Network settings docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure IPv6 compatibility for your Cloudflare domain."><link rel="canonical" href="https://developers.cloudflare.com/network/ipv6-compatibility/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network/ipv6-compatibility/index.md"><meta property="og:title" content="IPv6 compatibility · Cloudflare Network settings docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure IPv6 compatibility for your Cloudflare domain."><meta property="og:url" content="https://developers.cloudflare.com/network/ipv6-compatibility/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network"><meta name="algolia_product_filter" content="Network"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Network"><meta name="pcx_tags" content="IPv6"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network/ipv6-compatibility/#page","headline":"IPv6 compatibility \u00b7 Cloudflare Network settings docs","description":"Configure IPv6 compatibility for your Cloudflare domain.","url":"https://developers.cloudflare.com/network/ipv6-compatibility/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["IPv6"]}</script>
  markdown: true
  noindex: false
  route: /network/ipv6-compatibility/
  schema: 1
---
<p>Cloudflare enables IPv6 on all domains without requiring additional configuration or hardware (as long as your host provides IPv6 support).</p>
<p>When IPv6 compatibility is turned on, Cloudflare auto generates <a href="/dns/manage-dns-records/reference/dns-record-types/#a-and-aaaa"><code>AAAA</code> DNS records</a> to allow IPv6 clients to connect. On the other hand, when IPv6 compatibility is turned off, Cloudflare does not automatically generate and advertise <code>AAAA</code> DNS for the zone. Client software will determine whether to use IPv4 or IPv6 to connect to a hostname that supports both methods.</p>
<p>For <a href="/dns/proxy-status/">proxied DNS records</a> that have both an IPv6 and IPv4 origin address, Cloudflare will prefer the IPv4 address when connecting to your origin server.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Can customize</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="enable-ipv6-compatibility">Enable IPv6 compatibility</h2>
<p>By default, IPv6 compatibility is turned on for your domain and will apply to all domains and subdomains covered by <a href="/dns/proxy-status/">proxied DNS records</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/677.md")
</aside>
<h2 id="disable-ipv6-compatibility">Disable IPv6 compatibility</h2>
<p>If your origin web server only understands IPv4 formatted IP addresses, non-Enterprise customers should <a href="/network/pseudo-ipv4/">configure Pseudo IPv4</a>.</p>
<p>Alternatively, customers with an Enterprise account can turn off Cloudflare's IPv6 compatibility.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/676.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/680.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/675.md")
</aside>
<hr />
<h2 id="troubleshoot-an-ipv6-network-issue">Troubleshoot an IPv6 network issue</h2>
<p>Provide the following information to <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> if you experience issues with IPv6 connectivity:</p>
<ul>
<li>A <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#perform-a-traceroute">traceroute</a> that demonstrates the IPv6 connection issues.</li>
<li>The <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#identify-the-cloudflare-data-center-serving-your-request">Cloudflare data center serving your request</a> when the IPv6 issues occur.</li>
<li>Confirmation of whether <a href="#disable-ipv6-compatibility">disabling IPv6 Compatibility</a> resolves the issue.</li>
</ul>
