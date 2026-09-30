---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/
  description: Configure a tunnel resources and guides for Zero Trust networking.
  full_title: Configure a tunnel · Cloudflare One docs
  head_html: <title>Configure a tunnel · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure a tunnel resources and guides for Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/index.md"><meta property="og:title" content="Configure a tunnel · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure a tunnel resources and guides for Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/#page","headline":"Configure a tunnel \u00b7 Cloudflare One docs","description":"Configure a tunnel resources and guides for Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/
  schema: 1
---
<p>After <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/">creating your Cloudflare Tunnel</a>, you can configure various aspects of how <code>cloudflared</code> runs and connects your infrastructure to Cloudflare's network. This section covers advanced configuration options to optimize tunnel performance, security, and availability.</p>
<ul class="directory-listing"><li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">Tunnel with firewall</a><p>Configure firewall rules to allow `cloudflared` egress traffic while blocking all ingress, implementing a positive security model.
</p></li><li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">Tunnel availability and failover</a><p>Deploy multiple `cloudflared` replicas for high availability and automatic failover across your infrastructure.
</p></li><li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/">Tunnel run parameters</a><p>Modify tunnel service parameters to control how `cloudflared` runs on your system, including logging, connection settings, and protocol options.
</p></li><li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/">Origin parameters</a><p>Reference information for Origin parameters in Zero Trust networking.</p></li><li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/">Tunnel permissions</a><p>Manage tunnel tokens and control who can run your remotely-managed tunnels.
</p></li><li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cipher-suites/">Cipher suites</a><p>Review the TLS cipher suites supported by `cloudflared` for secure connections between your origin and Cloudflare&#x27;s network.
</p></li></ul>
<h2 id="common-configuration-scenarios">Common configuration scenarios</h2>
<h3 id="optimize-for-production">Optimize for production</h3>
<p>For production deployments, consider the following steps:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/">Deploy replicas</a> - Run multiple <code>cloudflared</code> instances for redundancy.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#loglevel">Configure logging</a> - Set appropriate log levels for monitoring and troubleshooting.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/">Review system requirements</a> - Ensure your infrastructure meets performance needs.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">Configure firewall rules</a> - Implement egress-only traffic patterns for security.</li>
</ul>
<h3 id="secure-your-tunnel">Secure your tunnel</h3>
<p>All tunnel connections between <code>cloudflared</code> and Cloudflare's network are secured with TLS 1.3 and post-quantum encryption by default, ensuring your traffic is protected against current and future cryptographic threats.</p>
<p>Enhance tunnel security with:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/">Tunnel token management</a> - Control access to your tunnel credentials.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">Egress-only firewall rules</a> - Allow only necessary outbound connections.</li>
<li>Least privilege permissions - Run <code>cloudflared</code> as a non-root user with minimal permissions needed for tunnel operation.</li>
</ul>
<h3 id="improve-reliability">Improve reliability</h3>
<p>Maximize tunnel uptime with:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/#cloudflared-replicas">Multiple replicas</a> - Deploy <code>cloudflared</code> across different hosts.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/notifications/">Health alerts</a> - Get notified when your tunnel is degraded or goes down.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#metrics">Health metrics</a> - Monitor tunnel resource usage to identify potential bottlenecks.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/#cloudflare-load-balancers/">Load balancing</a> - Distribute traffic across tunnel connections.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">Automatic failover</a> - Leverage built-in connection redundancy.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/">Monitor your tunnels</a> to track performance and troubleshoot issues.</li>
<li><a href="/cloudflare-one/networks/routes/add-routes/">Configure routes</a> to control how traffic reaches your applications.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">Set up private networks</a> for internal resource access.</li>
</ul>
