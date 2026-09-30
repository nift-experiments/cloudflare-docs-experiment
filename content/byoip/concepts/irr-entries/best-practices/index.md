---
cp9:
  canonical: https://developers.cloudflare.com/byoip/concepts/irr-entries/best-practices/
  description: Create and maintain IRR entries for your IP prefixes.
  full_title: Manage IRR entries · Cloudflare BYOIP docs
  head_html: <title>Manage IRR entries · Cloudflare BYOIP docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and maintain IRR entries for your IP prefixes."><link rel="canonical" href="https://developers.cloudflare.com/byoip/concepts/irr-entries/best-practices/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/byoip/concepts/irr-entries/best-practices/index.md"><meta property="og:title" content="Manage IRR entries · Cloudflare BYOIP docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and maintain IRR entries for your IP prefixes."><meta property="og:url" content="https://developers.cloudflare.com/byoip/concepts/irr-entries/best-practices/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="BYOIP"><meta name="algolia_product_filter" content="BYOIP"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="BYOIP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/byoip/concepts/irr-entries/best-practices/#page","headline":"Manage IRR entries \u00b7 Cloudflare BYOIP docs","description":"Create and maintain IRR entries for your IP prefixes.","url":"https://developers.cloudflare.com/byoip/concepts/irr-entries/best-practices/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /byoip/concepts/irr-entries/best-practices/
  schema: 1
---
<p>You must keep your <span class="nb-glossary-tooltip" title="Internet Routing Registry (IRR)">Internet Routing Registry (IRR)</span> entries up to date so that it is public information that Cloudflare has permission to advertise your prefix or prefixes, and to ensure that your traffic can be properly routed on the Internet.</p>
<h2 id="configure-an-irr-entry">Configure an IRR entry</h2>
<p>You can add or update an IRR entry by following the directions of your routing registry. Each routing registry has its own set of instructions to configure an IRR entry.</p>
<p>The recommended registries are AFRINIC, APNIC, ARIN, LACNIC, and RIPE. Refer to the table below for more information.</p>
<table>
<thead>
<tr>
<th>Route registry</th>
<th>URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>AFRINIC</td>
<td><a href="https://afrinic.net/internet-routing-registry#guide">https://afrinic.net/internet-routing-registry#guide</a></td>
</tr>
<tr>
<td>APNIC</td>
<td><a href="https://www.apnic.net/manage-ip/apnic-services/routing-registry/">https://www.apnic.net/manage-ip/apnic-services/routing-registry/</a></td>
</tr>
<tr>
<td>ARIN</td>
<td><a href="https://www.arin.net/resources/manage/irr/quickstart/">https://www.arin.net/resources/manage/irr/quickstart/</a></td>
</tr>
<tr>
<td>LACNIC</td>
<td><a href="https://lacnic.zendesk.com/hc/articles/360038667154-What-are-a-route-and-a-route-6-objects">https://lacnic.zendesk.com/hc/articles/360038667154-What-are-a-route-and-a-route-6-objects</a></td>
</tr>
<tr>
<td>RIPE</td>
<td><a href="https://www.ripe.net/manage-ips-and-asns/db/support/managing-route-objects-in-the-irr">https://www.ripe.net/manage-ips-and-asns/db/support/managing-route-objects-in-the-irr</a></td>
</tr>
</tbody>
</table>
<h2 id="verify-an-irr-entry">Verify an IRR entry</h2>
<p>Verify your Internet Routing Registry (IRR) entries to ensure that the IP prefixes Cloudflare advertises for you match the correct <span class="nb-glossary-tooltip" title="autonomous system numbers (ASNs)">autonomous system numbers (ASNs)</span>.</p>
<p>Each IRR entry record must include the following information:</p>
<ul>
<li><strong>Route</strong>: Each IP prefix Cloudflare advertises for you.</li>
<li><strong>Origin ASN</strong>: The Cloudflare ASN (AS13335) or your own ASN.</li>
<li><strong>Source</strong>: The name of the routing registry (for example, ARIN).</li>
</ul>
<p>Add or update IRR entries when they meet any of these criteria:</p>
<ul>
<li>The entry is missing.</li>
<li>The entry is incomplete or inaccurate — for example, when the route object does not show the correct origin.</li>
<li>The entry is complete but requires updating — for example, when they correspond to supernets but need to correspond to subnets used in Magic Transit.</li>
</ul>
<h3 id="subnet-prefix-verification">Subnet prefix verification</h3>
<p>Use <a href="https://irrexplorer.nlnog.net">IRR Explorer</a> to verify which ASN is associated with a subnet prefix.</p>
<p><strong>Method:</strong> Search for the subnet prefix IP, for example, <code>162.211.156.0/24</code>.</p>
<p><strong>Output:</strong> List of ASN numbers, source (route registry), and any associated errors.</p>
<h3 id="asn-verification">ASN verification</h3>
<p>Use <a href="https://irrexplorer.nlnog.net">IRR Explorer</a> to verify which prefixes are associated with an ASN.</p>
<p><strong>Method:</strong> Search for the ASN, for example <code>AS13335</code>.</p>
<p><strong>Output:</strong> List of prefixes, source, and any associated errors.</p>
<h3 id="whois-lookup">WHOIS lookup</h3>
<p>Use WHOIS lookup to verify your origin ASN and routing data.</p>
<p><strong>Method:</strong> In a terminal, use the following <code>whois</code> command, replacing <code>&lt;NETWORK_PREFIX&gt;</code> with your network prefix. The host <code>rr.ntt.net</code> is the primary server for the Global IP network.</p>
<pre tabindex="0"><code class="language-sh">whois -h rr.ntt.net &lt;NETWORK_PREFIX&gt;&#10;</code></pre>
<p><strong>Output:</strong> IRR route, origin, and source information.</p>
<details class="nb-details"><summary>WHOIS output example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3791.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3788.md")
</aside>
