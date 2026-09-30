---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/linux/
  description: Linux in Zero Trust networking.
  full_title: Run as a service on Linux · Cloudflare One docs
  head_html: <title>Run as a service on Linux · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Linux in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/linux/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/linux/index.md"><meta property="og:title" content="Run as a service on Linux · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Linux in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/linux/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Linux"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/linux/#page","headline":"Run as a service on Linux \u00b7 Cloudflare One docs","description":"Linux in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/linux/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Linux"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/linux/
  schema: 1
---
<p>You can install <code>cloudflared</code> as a system service on Linux.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you install Cloudflare Tunnel as a service on Linux, follow Steps 1 through 4 of the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/">Tunnel CLI setup guide</a>. At this point you should have a named tunnel and a <code>config.yml</code> file in your <code>.cloudflared</code> directory.</p>
<h2 id="1-configure-cloudflared-as-a-service"><ol>
<li>Configure <code>cloudflared</code> as a service</li>
</ol></h2>
<p>By default, Cloudflare Tunnel expects all of the configuration to exist in the <code>$HOME/.cloudflared/config.yml</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/">configuration file</a>. At a minimum you must specify the following arguments to run as a service:</p>
<table>
<thead>
<tr>
<th>Argument</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>tunnel</code></td>
<td>The UUID of your tunnel</td>
</tr>
<tr>
<td><code>credentials-file</code></td>
<td>The location of the credentials file for your Tunnel</td>
</tr>
</tbody>
</table>
<h2 id="2-run-cloudflared-as-a-service"><ol start="2">
<li>Run <code>cloudflared</code> as a service</li>
</ol></h2>
<ol>
<li>Install the <code>cloudflared</code> service.</li>
</ol>
<pre tabindex="0"><code class="language-sh">cloudflared service install&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5390.md")
</aside>
<ol start="2">
<li>Start the service.</li>
</ol>
<pre tabindex="0"><code class="language-sh">systemctl start cloudflared&#10;</code></pre>
<ol start="3">
<li>(Optional) View the status of the service.</li>
</ol>
<pre tabindex="0"><code class="language-sh">systemctl status cloudflared&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>You can now <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/#5-start-routing-traffic">route traffic through your tunnel</a>. If you add IP routes or otherwise change the configuration, restart the service to load the new configuration:</p>
<pre tabindex="0"><code class="language-sh">systemctl restart cloudflared&#10;</code></pre>
