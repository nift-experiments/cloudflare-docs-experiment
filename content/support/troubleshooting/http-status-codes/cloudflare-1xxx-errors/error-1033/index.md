---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1033/
  description: Troubleshoot Cloudflare 1033 error code.
  full_title: Error 1033 · Cloudflare Support docs
  head_html: <title>Error 1033 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Cloudflare 1033 error code."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1033/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1033/index.md"><meta property="og:title" content="Error 1033 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Cloudflare 1033 error code."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1033/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1033/#page","headline":"Error 1033 \u00b7 Cloudflare Support docs","description":"Troubleshoot Cloudflare 1033 error code.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1033/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1033/
  schema: 1
---
<h2 id="error-1033-cloudflare-tunnel-error">Error 1033: Cloudflare Tunnel error</h2>
<p>This error indicates an issue with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>.</p>
<h3 id="common-cause">Common cause</h3>
<p>You have requested a page on a website (<code>tunnel.example.com</code>) that is on the Cloudflare network. The host (<code>tunnel.example.com</code>) is configured with Cloudflare Tunnel, and Cloudflare is currently unable to resolve it.</p>
<h3 id="resolution">Resolution</h3>
<p>A <code>1033</code> error indicates your tunnel is not connected to Cloudflare's network because Cloudflare's network cannot find a healthy <code>cloudflared</code> instance to receive the traffic.</p>
<p>First, review whether your tunnel is listed as <code>Active</code> in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> by going to <strong>Networking</strong> &gt; <strong>Tunnels</strong> or run <code>cloudflared tunnel list</code>. If the tunnel is not <code>Active</code>, review the following and take the action necessary for your tunnel status:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Meaning</th>
<th>Recommended Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Healthy</strong></td>
<td>The tunnel is active and serving traffic through four connections to the Cloudflare global network.</td>
<td>No action is required. Your tunnel is running correctly.</td>
</tr>
<tr>
<td><strong>Inactive</strong></td>
<td>The tunnel has been created (via the API or dashboard) but the <code>cloudflared</code> connector has never been run to establish a connection.</td>
<td>Install and run <code>cloudflared</code> on your origin server to connect the tunnel to Cloudflare. You can find the installation command in the Cloudflare dashboard under <strong>Networking</strong> &gt; <strong>Tunnels</strong> — select your tunnel, then on the <strong>Overview</strong> tab select <strong>Add a replica</strong>. For API-based setup, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/#4-install-and-run-the-tunnel">Install and run the tunnel</a>.</td>
</tr>
<tr>
<td><strong>Down</strong></td>
<td>The tunnel was previously connected but is currently disconnected because the <code>cloudflared</code> process has stopped.</td>
<td>1. Ensure the <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/">service</a> or process is actively running on your server. <br /> 2. Check for server-side issues, such as the machine being powered off, an application crash, or recent network changes.</td>
</tr>
<tr>
<td><strong>Degraded</strong></td>
<td>The <code>cloudflared</code> connector is running and the tunnel is serving traffic, but at least one individual connection has failed. Further degradation in <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">tunnel availability</a> could risk the tunnel going down and failing to serve traffic.</td>
<td>1. Review your <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">logs</a> for connection failures or error messages. <br /> 2. Investigate local network and firewall rules to ensure they are not blocking connections to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">Cloudflare Tunnel IPs and ports</a>. <br /></td>
</tr>
</tbody>
</table>
