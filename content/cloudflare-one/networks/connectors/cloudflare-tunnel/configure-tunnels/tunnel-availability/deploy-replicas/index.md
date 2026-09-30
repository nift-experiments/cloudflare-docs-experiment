---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/
  description: Deploy cloudflared replicas in Zero Trust networking.
  full_title: Deploy cloudflared replicas · Cloudflare One docs
  head_html: <title>Deploy cloudflared replicas · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy cloudflared replicas in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/index.md"><meta property="og:title" content="Deploy cloudflared replicas · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy cloudflared replicas in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/#page","headline":"Deploy cloudflared replicas \u00b7 Cloudflare One docs","description":"Deploy cloudflared replicas in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/
  schema: 1
---
<p>To deploy multiple instances of <code>cloudflared</code>, you can create and configure one tunnel and run it on multiple hosts. If your tunnel runs as a service, only one <code>cloudflared</code> instance is allowed per host.</p>
<p>You can run the same tunnel across various <code>cloudflared</code> processes for up to 100 connections (25 replicas) per tunnel. Cloudflare Load Balancers and DNS records can still point to the tunnel and its UUID. Traffic will be sent to all <code>cloudflared</code> processes associated with the tunnel.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="deploy-replicas-in-kubernetes">Deploy replicas in Kubernetes</h3>
@markup("md", "content/.markup/bodies/5379.md")
</aside>
<h2 id="remotely-managed-tunnels">Remotely-managed tunnels</h2>
<ol>
<li>To create a remotely-managed tunnel, follow the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">dashboard setup guide</a>.</li>
<li>On the <strong>Tunnels</strong> page, select your newly created tunnel. The tunnel overview page displays all active replicas.</li>
<li>Select <strong>Edit</strong>.</li>
<li>Select the operating system of the host where you want to deploy a replica.</li>
<li>Copy the installation command and run it on the host.</li>
</ol>
<p>The new replica will appear on the tunnel overview page. All replicas serve the same routes and use the same configuration parameters.</p>
<h2 id="locally-managed-tunnels">Locally-managed tunnels</h2>
<ol>
<li>
<p>To create a locally-managed tunnel, complete Steps 1 through 5 in the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/">CLI setup guide</a>.</p>
</li>
<li>
<p>Run your newly created tunnel.</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel run &lt;NAME&gt;&#10;</code></pre>
<p>This will start a <code>cloudflared</code> instance and generate a unique <code>connector_id</code>.</p>
<ol start="3">
<li>In a separate window or on another host, run the same command again:</li>
</ol>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel run &lt;NAME&gt;&#10;</code></pre>
<p>This will initialize another <code>cloudflared</code> instance and generate another <code>connector_id</code>.</p>
<ol start="4">
<li>Run <code>tunnel info</code> to show each <code>cloudflared</code> instance running your tunnel:</li>
</ol>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel info &lt;NAME&gt;&#10;</code></pre>
<p>This will output your tunnel UUID as well as two Connector IDs, one for each <code>cloudflared</code> process running your tunnel. With this command, you can also see that your tunnel is now being served by eight connections.</p>
