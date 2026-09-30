---
cp9:
  canonical: https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/macos/
  description: Install and run cloudflared as a launch agent on macOS.
  full_title: Run as a service on macOS · Cloudflare Docs
  head_html: <title>Run as a service on macOS · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="Install and run cloudflared as a launch agent on macOS."><link rel="canonical" href="https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/macos/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/macos/index.md"><meta property="og:title" content="Run as a service on macOS · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Install and run cloudflared as a launch agent on macOS."><meta property="og:url" content="https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/macos/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Tunnel"><meta name="algolia_product_filter" content="Cloudflare Tunnel"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Tunnel"><meta name="pcx_tags" content="MacOS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/macos/#page","headline":"Run as a service on macOS \u00b7 Cloudflare Docs","description":"Install and run cloudflared as a launch agent on macOS.","url":"https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/macos/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["MacOS"]}</script>
  markdown: true
  noindex: false
  route: /tunnel/features/locally-managed-tunnels/as-a-service/macos/
  schema: 1
---
<p>You can install <code>cloudflared</code> as a system service on macOS.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you install Cloudflare Tunnel as a service on your OS, follow Steps 1 through 4 of the <a href="/tunnel/features/locally-managed-tunnels/create-local-tunnel/">Tunnel CLI setup guide</a>. At this point you should have a named tunnel and a <code>config.yml</code> file in your <code>$HOME/.cloudflared</code> directory.</p>
<h2 id="1-configure-cloudflared-as-a-service"><ol>
<li>Configure <code>cloudflared</code> as a service</li>
</ol></h2>
<p>By default, Cloudflare Tunnel expects all of the configuration to exist in the <code>$HOME/.cloudflared/config.yml</code> <a href="/tunnel/features/locally-managed-tunnels/configuration-file/">configuration file</a>. At a minimum you must specify the following arguments to run as a service:</p>
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
<td>The location of the credentials file for your tunnel</td>
</tr>
</tbody>
</table>
<h2 id="2-run-cloudflared-as-a-service"><ol start="2">
<li>Run <code>cloudflared</code> as a service</li>
</ol></h2>
<p>You can install the service to either run at login or at boot.</p>
<h3 id="run-at-login">Run at login</h3>
<p>Open a terminal window and run the following command:</p>
<pre tabindex="0"><code class="language-sh">cloudflared service install&#10;</code></pre>
<p>Cloudflare Tunnel will be installed as a launch agent and start whenever you log in, using your local user configuration found in <code>~/.cloudflared/</code>.</p>
<h3 id="run-at-boot">Run at boot</h3>
<p>Open a terminal window and run the following command:</p>
<pre tabindex="0"><code class="language-sh">sudo cloudflared service install&#10;</code></pre>
<p>Cloudflare Tunnel will be installed as a launch daemon and start whenever your system boots, using your configuration found in <code>/etc/cloudflared</code>.</p>
<h2 id="3-manually-start-the-service"><ol start="3">
<li>Manually start the service</li>
</ol></h2>
<p>Run the following command:</p>
<pre tabindex="0"><code class="language-sh">sudo launchctl start com.cloudflare.cloudflared&#10;</code></pre>
<p>The output will be logged to <code>/Library/Logs/com.cloudflare.cloudflared.err.log</code> and <code>/Library/Logs/com.cloudflare.cloudflared.out.log</code>.</p>
<h2 id="next-steps">Next steps</h2>
<p>You can now <a href="/tunnel/features/locally-managed-tunnels/create-local-tunnel/#5-start-routing-traffic">route traffic through your tunnel</a>. If you add IP routes or otherwise change the configuration, restart the service to load the new configuration:</p>
<pre tabindex="0"><code class="language-sh">sudo launchctl stop com.cloudflare.cloudflared&#10;sudo launchctl start com.cloudflare.cloudflared&#10;</code></pre>
