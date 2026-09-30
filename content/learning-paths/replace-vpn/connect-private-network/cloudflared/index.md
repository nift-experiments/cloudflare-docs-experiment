---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflared/
  description: Create a tunnel to your private network.
  full_title: Connect with Cloudflare Tunnel · Cloudflare Learning Paths
  head_html: <title>Connect with Cloudflare Tunnel · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Create a tunnel to your private network."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflared/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflared/index.md"><meta property="og:title" content="Connect with Cloudflare Tunnel · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a tunnel to your private network."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflared/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare One,Access,Cloudflare Tunnel,Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflared/#page","headline":"Connect with Cloudflare Tunnel \u00b7 Cloudflare Learning Paths","description":"Create a tunnel to your private network.","url":"https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflared/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/replace-vpn/connect-private-network/cloudflared/
  schema: 1
---
<p>Cloudflare Tunnel is an outbound-only daemon service that can run on nearly any host machine and proxies local traffic once validated from the Cloudflare network. User traffic initiated from the Cloudflare One Client onramps to Cloudflare, passes down your Cloudflare Tunnel connections, and terminates automatically in your local network. Traffic reaching your internal applications or services will carry the local source IP address of the host machine running the <code>cloudflared</code> daemon.</p>
<h2 id="create-a-tunnel">Create a tunnel</h2>
<p>To connect your private network:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9904.md")
</div></div>
<p>All internal applications and services in this IP range are now connected to Cloudflare.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9894.md")
</aside>
<h2 id="best-practices">Best practices</h2>
<ul>
<li>Segregate production and staging traffic among different Cloudflare tunnels.</li>
<li>Add a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/"><code>cloudflared</code> replica</a> to another host machine for an additional point of availability.</li>
<li>Distribute access to critical services (for example, private DNS, Active Directory, and other critical systems) across different tunnels for blast-radius reduction in the event of a server-side outage.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/notifications/">Enable notifications</a> in the Cloudflare dashboard to monitor tunnel health.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/">Monitor performance metrics</a> to identify potential bottlenecks.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/update-cloudflared/">Update <code>cloudflared</code></a> regularly.</li>
</ul>
