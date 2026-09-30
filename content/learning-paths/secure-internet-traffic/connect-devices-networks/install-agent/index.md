---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/install-agent/
  description: Install the Cloudflare One device client.
  full_title: Download and install the Cloudflare One Client · Cloudflare Learning Paths
  head_html: <title>Download and install the Cloudflare One Client · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Install the Cloudflare One device client."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/install-agent/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/install-agent/index.md"><meta property="og:title" content="Download and install the Cloudflare One Client · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Install the Cloudflare One device client."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/install-agent/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Gateway,Cloudflare One,Data Loss Prevention,CASB,Browser Isolation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/install-agent/#page","headline":"Download and install the Cloudflare One Client \u00b7 Cloudflare Learning Paths","description":"Install the Cloudflare One device client.","url":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/install-agent/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-internet-traffic/connect-devices-networks/install-agent/
  schema: 1
---
<p>Most admins test by manually downloading the Cloudflare One Client and enrolling in your organization's Cloudflare Zero Trust instance.</p>
<h2 id="install-the-cloudflare-one-client">Install the Cloudflare One Client</h2>
<ol>
<li>First, uninstall any existing third-party VPN software if possible. Sometimes products placed in a disconnected or disabled state will still interfere with the Cloudflare One Client.</li>
<li>If you are running third-party firewall or TLS decryption software, verify that it does not inspect or block traffic to the following destinations:</li>
</ol>
<ul>
<li>
<p>IPv4 API endpoints: <code>162.159.137.105</code> and <code>162.159.138.105</code></p>
</li>
<li>
<p>IPv6 API endpoints: <code>2606:4700:7::a29f:8969</code> and <code>2606:4700:7::a29f:8a69</code></p>
</li>
<li>
<p>SNIs for Cloudflare One Client version 2026.6.0 and later: <code>api.devices.cloudflare.com</code></p>
</li>
<li>
<p>SNIs for versions earlier than 2026.6.0: <code>zero-trust-client.cloudflareclient.com</code> and <code>notifications.cloudflareclient.com</code></p>
<p>For more information, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">WARP with firewall</a>.</p>
</li>
</ul>
<ol start="3">
<li>
<p>Manually install the Cloudflare One Client on the device.</p>
<pre tabindex="0"><code> &lt;details class=&quot;nb-details&quot;&gt;&lt;summary&gt;Window, macOS, and Linux&lt;/summary&gt;&lt;div class=&quot;nb-details-body&quot;&gt;&#10;</code></pre>
</li>
</ol>
@markup("md", "content/.markup/bodies/10054.md")
</div></details>
<pre tabindex="0"><code>	&lt;details class=&quot;nb-details&quot;&gt;&lt;summary&gt;iOS, Android, and ChromeOS&lt;/summary&gt;&lt;div class=&quot;nb-details-body&quot;&gt;&#10;</code></pre>
@markup("md", "content/.markup/bodies/10056.md")
</div></details>
<p>The Cloudflare One Client should show as <strong>Connected</strong>. The device is now connected to your organization and secured with Cloudflare Zero Trust.</p>
