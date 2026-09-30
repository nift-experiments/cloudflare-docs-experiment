---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/
  description: Review frequently asked questions about tunnels in Cloudflare Zero Trust.
  full_title: Tunnels FAQ · Cloudflare One docs
  head_html: <title>Tunnels FAQ · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Review frequently asked questions about tunnels in Cloudflare Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/index.md"><meta property="og:title" content="Tunnels FAQ · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review frequently asked questions about tunnels in Cloudflare Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="WebSockets,DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/#page","headline":"Tunnels FAQ \u00b7 Cloudflare One docs","description":"Review frequently asked questions about tunnels in Cloudflare Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["WebSockets","DNS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/faq/cloudflare-tunnels-faq/
  schema: 1
---
<p><a href="/cloudflare-one/faq/">❮ Back to FAQ</a></p>
<h2 id="can-i-create-a-tunnel-for-an-apex-domain">​Can I create a Tunnel for an apex domain?</h2>
<p>Yes. With <a href="https://blog.cloudflare.com/argo-tunnels-that-live-forever/">Named Tunnels</a> you can create a CNAME at the apex that points to the named tunnel.</p>
<h2 id="does-cloudflare-tunnel-support-websockets">​Does Cloudflare Tunnel support Websockets?</h2>
<p>Yes. Cloudflare Tunnel has full support for Websockets.</p>
<h2 id="does-cloudflare-tunnel-support-grpc">​Does Cloudflare Tunnel support gRPC?</h2>
<p>Yes.
Cloudflare Tunnel supports gRPC traffic via <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">private subnet routing</a>. Public hostname deployments are not currently supported.</p>
<h2 id="how-can-tunnel-be-used-with-partial-dns-cname-setup">How can Tunnel be used with Partial DNS (CNAME Setup)?</h2>
<p>Cloudflare offers two modes of setup: <a href="/dns/zone-setups/full-setup/">Full Setup</a>, in which the domain uses Cloudflare DNS nameservers, and <a href="/dns/zone-setups/partial-setup/">Partial Setup</a> (also known as CNAME setup) in which the domain uses non-Cloudflare DNS servers.</p>
<p>The best experience with Cloudflare Tunnel is using Full Setup because Cloudflare manages DNS for the domain and can automatically configure DNS records for newly started Tunnels.</p>
<p>You can still use Tunnel with Partial Setup. You will need to create a new DNS record with your current DNS provider for each new hostname connected through Cloudflare Tunnel. The DNS record should be of type CNAME or ALIAS if it is on the root of the domain. The name of the record should be the subdomain it corresponds to (e.g. <code>example.com</code> or <code>tunnel.example.com</code>) and the value of the record should be <code>subdomain.domain.tld.cdn.cloudflare.net</code>. (e.g. <code>example.com.cdn.cloudflare.net</code> or <code>tunnel.example.com.cdn.cloudflare.net</code>)</p>
<p>For a complete walkthrough of using Access with a partial CNAME setup, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/#partial-cname-setup">Publish a self-hosted application to the Internet</a>.</p>
<h2 id="how-can-origin-servers-be-secured-when-using-tunnel">How can origin servers be secured when using Tunnel?</h2>
<p>Tunnel can expose web applications to the Internet that sit behind a NAT or firewall. Thus, you can keep your web server otherwise completely locked down. To double check that your origin web server is not responding to requests outside Cloudflare while Tunnel is running you can run netcat in the command line:</p>
<pre tabindex="0"><code class="language-sh">netcat -zv [your-server&#x27;s-ip-address] 80&#10;netcat -zv [your-server&#x27;s-ip-address] 443&#10;</code></pre>
<p>If your server is still responding on those ports, you will see:</p>
<pre tabindex="0"><code class="language-txt">[ip-address] 80 (http) open&#10;</code></pre>
<p>If your server is correctly locked down, you will see:</p>
<pre tabindex="0"><code class="language-txt">[ip-address] 443 (https): Connection refused&#10;</code></pre>
<h2 id="large-file-and-streaming-traffic-through-tunnel">Large-file and streaming traffic through Tunnel</h2>
<p>It depends on how you route the traffic.</p>
<p>Public hostname routes make applications available on the Internet through Cloudflare's reverse proxy. On Free, Pro, and Business plans, the <a href="https://www.cloudflare.com/service-specific-terms-application-services/#content-delivery-network-free-pro-or-business">service-specific terms</a> require you to use a specific paid service to serve video and other large files.</p>
<p>Refer to <a href="/fundamentals/reference/policies-compliances/delivering-videos-with-cloudflare/">Delivering videos with Cloudflare</a> for available options, such as <a href="/stream/">Stream</a>.</p>
<p>Private network routes do not publish applications to the Internet, and this restriction does not apply. Users and networks can reach these routes through the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>, <a href="/mesh/">Cloudflare Mesh</a>, or <a href="/cloudflare-one/networks/connectors/cloudflare-wan/">Cloudflare WAN</a>.</p>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">Private networks</a>.</p>
<h2 id="what-records-are-created-for-routing-to-a-named-tunnel-s-hostname">What records are created for routing to a Named Tunnel's hostname?</h2>
<p>Named Tunnels can be routed via DNS records, in which case we use CNAME records to point to the <code>&lt;UUID&gt;.cfargotunnel.com</code>; Or as Load Balancing endpoints, which also point to <code>&lt;UUID&gt;.cfargotunnel.com</code>.</p>
<h2 id="does-cloudflare-tunnel-send-visitor-ips-to-my-origin">Does Cloudflare Tunnel send visitor IPs to my origin?</h2>
<p>No. When using Cloudflare Tunnel, all requests to the origin are made internally between <code>cloudflared</code> and the origin.</p>
<p>To log external visitor IPs, you will need to <a href="/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/">configure an alternative method</a>.</p>
<h2 id="why-does-the-name-warp-and-argo-appear-in-some-legacy-materials">Why does the name 'warp' and 'argo' appear in some legacy materials?</h2>
<p>Cloudflare Tunnel was previously named Warp during the beta phase. As Warp was added to the Argo product family, we changed the name to Argo Tunnel to match. Once we no longer required users to purchase Argo to create Tunnels, we renamed Argo Tunnel to Cloudflare Tunnel.</p>
<h2 id="is-it-possible-to-restore-a-deleted-tunnel">Is it possible to restore a deleted tunnel?</h2>
<p>No. You cannot undo a tunnel deletion. If the tunnel was locally-managed, its <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/tunnel-useful-terms/#configuration-file"><code>config.yaml</code> file</a> will still be present and you can create a new tunnel with the same configuration. If the tunnel was remotely-managed, both the tunnel and its configuration are permanently deleted.</p>
<h2 id="how-do-i-contact-support">How do I contact support?</h2>
<p>Before contacting the Cloudflare support team:</p>
<ol>
<li>
<p>Take note of any specific error messages and/or problematic behaviors.</p>
</li>
<li>
<p>Make sure that <code>cloudflared</code> is updated to the <a href="https://github.com/cloudflare/cloudflared">latest version</a>.</p>
</li>
<li>
<p>Gather any relevant error/access logs from your server.</p>
</li>
<li>
<p>If needed set <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#loglevel"><code>--loglevel</code></a> to <code>debug</code>, so the Cloudflare support team can get more info from the <code>cloudflared.log</code> file.</p>
</li>
<li>
<p>Include your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/">Cloudflare Tunnel diagnostic logs</a> (<code>cloudflared-diag-YYYY-MM-DDThh-mm-ss.zip</code>).</p>
</li>
</ol>
