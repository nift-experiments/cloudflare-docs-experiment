---
cp9:
  canonical: https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-wan/
  description: Proxy public hostnames to private origins through a Cloudflare WAN IPsec tunnel.
  full_title: Set up a private origin via Cloudflare WAN · Cloudflare DNS docs
  head_html: <title>Set up a private origin via Cloudflare WAN · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Proxy public hostnames to private origins through a Cloudflare WAN IPsec tunnel."><link rel="canonical" href="https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-wan/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-wan/index.md"><meta property="og:title" content="Set up a private origin via Cloudflare WAN · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Proxy public hostnames to private origins through a Cloudflare WAN IPsec tunnel."><meta property="og:url" content="https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-wan/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="DNS"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-wan/#page","headline":"Set up a private origin via Cloudflare WAN \u00b7 Cloudflare DNS docs","description":"Proxy public hostnames to private origins through a Cloudflare WAN IPsec tunnel.","url":"https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-wan/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /dns/private-origins/set-up-via-cloudflare-wan/
  schema: 1
---
<p>This guide walks you through proxying public hostnames to origins on a private network. The private network is reachable through a <a href="/cloudflare-wan/">Cloudflare WAN</a> (formerly Magic WAN) IPsec tunnel. The CDN, WAF, Cache, and other proxied features apply to this traffic the same way they apply to traffic destined for public origins.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="closed-beta">Closed beta</h3>
@markup("md", "content/.markup/bodies/7597.md")
</aside>
<h2 id="before-you-begin">Before you begin</h2>
<p>Confirm the following before you start:</p>
<ul>
<li><strong>Active Cloudflare WAN subscription</strong>: This capability requires a Cloudflare WAN subscription on your account.</li>
<li><strong>Access to private origins enabled on your account</strong>: This is a separate entitlement from standard authoritative DNS access. Contact your Cloudflare account team to request access.</li>
<li><strong>IPsec tunnels configured</strong>: Set up two anycast IPsec tunnels for redundancy, each with a different Cloudflare anycast endpoint. Refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a>. Two settings are important for this use case:
<ul>
<li>Leave <strong>Automatic return routing</strong> disabled. It does not apply to the public-to-private origin traffic pattern, where requests originate on the Internet and reach your origin through Cloudflare's reverse proxy.</li>
<li>Keep the default <strong>Health check</strong> settings (type <code>reply</code>, direction <code>bidirectional</code>, rate <code>mid</code>). These defaults are required for tunnel health to track correctly in this use case.</li>
</ul>
</li>
<li><strong>Static routes configured</strong>: Add two static routes for the private prefix you want to reach — one per tunnel — with different priorities so traffic fails over to the backup tunnel if the primary goes down. For example, set priority <code>100</code> on the route through your primary tunnel and <code>101</code> on the route through your backup tunnel (lower numbers are higher priority). Refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/">Configure routes</a>.</li>
<li><strong>Cloudflare Source IP set to a private range</strong>: The Cloudflare Source IP is the IP that Cloudflare uses when sending proxied requests into your private network. If it is left as a public range, your network cannot route the return traffic back through the tunnel and requests time out. Refer to <a href="/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/">Configure Cloudflare source IPs</a>.</li>
</ul>
<h2 id="1-verify-your-cloudflare-source-ip-allocation"><ol>
<li>Verify your Cloudflare Source IP allocation</li>
</ol></h2>
<p>A misconfigured Cloudflare Source IP is the most common cause of failure. If the Source IP is left as a public range, the network where your origin lives has no return route and requests time out before reaching the application.</p>
<p>Go to <a href="/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/">Configure Cloudflare source IPs</a> and verify that the Source IP is set to a private range, such as <code>100.64.0.0/12</code> (the default) or another private <code>/12</code> you have selected.</p>
<h2 id="2-create-a-dns-record-with-private-network-routing"><ol start="2">
<li>Create a DNS record with private network routing</li>
</ol></h2>
<p>Create an <code>A</code> or <code>AAAA</code> record that points to the private IP address of your origin, with proxy status enabled and <strong>Use private network routing</strong> turned on. This tells Cloudflare to send traffic for the hostname through your Cloudflare WAN tunnel instead of over the public Internet.</p>
<p>For the dashboard and API steps, refer to <a href="/dns/private-origins/private-network-routing/">Private network routing</a>.</p>
<h2 id="3-verify-end-to-end-connectivity"><ol start="3">
<li>Verify end-to-end connectivity</li>
</ol></h2>
<p>After the DNS record is in place, validate the path from the Cloudflare network through your tunnel to the origin.</p>
<h3 id="check-tunnel-health">Check tunnel health</h3>
<p>In the Cloudflare dashboard, confirm that your IPsec tunnel is healthy. Refer to <a href="/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/">Check tunnel health on the dashboard</a>.</p>
<h3 id="send-a-request-from-an-external-client">Send a request from an external client</h3>
<p>From a machine outside your private network, send an HTTPS request to the proxied hostname:</p>
<pre tabindex="0"><code class="language-bash">curl -v https://&lt;YOUR_DOMAIN&gt;/&#10;</code></pre>
<p>A successful response confirms that Cloudflare accepted the request, applied your proxied features, and reached the origin through the tunnel.</p>
<h3 id="confirm-traffic-on-the-origin">Confirm traffic on the origin</h3>
<p>On the origin VM, verify that requests are arriving from the Cloudflare Source IP range. For example, to watch for incoming traffic from <code>100.64.0.0/12</code> on port <code>443</code>:</p>
<pre tabindex="0"><code class="language-bash">sudo tcpdump -n -i any &#x27;src net 100.64.0.0/12 and dst port 443&#x27;&#10;</code></pre>
<p>Replace <code>100.64.0.0/12</code> with the Source IP range configured for your account, and adjust the port to match the listener on your origin.</p>
<h2 id="common-pitfalls">Common pitfalls</h2>
<table>
<thead>
<tr>
<th>Symptom</th>
<th>Cause and fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>Connection timeouts from clients</td>
<td>Cloudflare Source IP is set to a public range. Set it to a private <code>/12</code>.</td>
</tr>
<tr>
<td>Request times out, no response on the origin</td>
<td>The network where your origin lives has no return route for the Cloudflare Source IP range. Add a route that sends that range back through the tunnel.</td>
</tr>
<tr>
<td>Tunnel shows IKE established but health checks fail</td>
<td>ICMP is blocked on the path or the health check is misconfigured. Allow ICMP between the tunnel endpoints and confirm the health check direction is <code>bidirectional</code> and type is <code>reply</code>.</td>
</tr>
<tr>
<td>Traffic tries to route over the public Internet</td>
<td>The <strong>Use private network routing</strong> toggle is not turned on for the DNS record. Edit the record and turn the toggle on.</td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/cloudflare-wan/configuration/common-settings/configure-tunnel-health-alerts/">Configure tunnel health alerts</a> to get notified when a tunnel goes down.</li>
<li>Review the <a href="/dns/private-origins/private-network-routing/">Private network routing</a> reference for dashboard and API details.</li>
<li>If you run into tunnel issues, refer to <a href="/cloudflare-wan/troubleshooting/tunnel-health/">Tunnel health troubleshooting</a> and <a href="/cloudflare-wan/troubleshooting/ipsec-troubleshoot/">IPsec troubleshooting</a>.</li>
</ul>
