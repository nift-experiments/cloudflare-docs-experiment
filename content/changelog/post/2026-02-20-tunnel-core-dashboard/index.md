---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-20-tunnel-core-dashboard/
  description: New updates and improvements at Cloudflare.
  full_title: Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard · Changelog
  head_html: <title>Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-20-tunnel-core-dashboard/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-20-tunnel-core-dashboard/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-20-tunnel-core-dashboard/#page","headline":"Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-20-tunnel-core-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-20-tunnel-core-dashboard/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 20, 2026</time><h2 id="post-title">Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard</h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> is now available in the main Cloudflare Dashboard at <a href="https://dash.cloudflare.com/?to=/:account/tunnels">Networking &gt; Tunnels</a>, bringing first-class Tunnel management to developers using Tunnel for securing origin servers.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-core-dashboard.gif" alt="Manage Tunnels in the Core Dashboard" /></p>
<p>This new experience provides everything you need to manage Tunnels for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a>, including:</p>
<ul>
<li><strong>Full Tunnel lifecycle management</strong>: Create, configure, delete, and monitor all your Tunnels in one place.</li>
<li><strong>Native integrations</strong>: View Tunnels by name when configuring <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS records</a> and <a href="/workers-vpc/">Workers VPC</a> — no more copy-pasting UUIDs.</li>
<li><strong>Real-time visibility</strong>: Monitor <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">replicas</a> and Tunnel <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status">health status</a> directly in the dashboard.</li>
<li><strong>Routing map</strong>: Manage all ingress routes for your Tunnel, including <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a>, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostnames</a>, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">private CIDRs</a>, and <a href="/workers-vpc/">Workers VPC services</a>, from a single interactive interface.</li>
</ul>
<h4 id="choose-the-right-dashboard-for-your-use-case">Choose the right dashboard for your use case</h4>
<p><strong>Core Dashboard</strong>: Navigate to <a href="https://dash.cloudflare.com/?to=/:account/tunnels">Networking &gt; Tunnels</a> to manage Tunnels for:</p>
<ul>
<li>Securing origin servers and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a> with CDN, WAF, Load Balancing, and DDoS protection</li>
<li>Connecting <a href="/workers-vpc/">Workers to private services</a> via Workers VPC</li>
</ul>
<p><strong>Cloudflare One Dashboard</strong>: Navigate to <a href="https://one.dash.cloudflare.com/?to=/:account/networks/connectors">Zero Trust &gt; Networks &gt; Connectors</a> to manage Tunnels for:</p>
<ul>
<li>Securing your public applications with <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Zero Trust access policies</a></li>
<li>Connecting users to <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private applications</a></li>
<li>Building a <a href="/reference-architecture/architectures/sase/#connecting-networks">private mesh network</a></li>
</ul>
<p>Both dashboards provide complete Tunnel management capabilities — choose based on your primary workflow.</p>
<h4 id="get-started">Get started</h4>
<p>New to Tunnel? Learn how to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">get started with Cloudflare Tunnel</a> or explore advanced use cases like <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/">securing SSH servers</a> or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/kubernetes/">running Tunnels in Kubernetes</a>.</p>
</div></article></div>
