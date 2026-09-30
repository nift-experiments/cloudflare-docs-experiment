---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication/
  description: Connect to RDP with client-side cloudflared in Zero Trust networking.
  full_title: Connect to RDP with client-side cloudflared · Cloudflare One docs
  head_html: <title>Connect to RDP with client-side cloudflared · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect to RDP with client-side cloudflared in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication/index.md"><meta property="og:title" content="Connect to RDP with client-side cloudflared · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect to RDP with client-side cloudflared in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="RDP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication/#page","headline":"Connect to RDP with client-side cloudflared \u00b7 Cloudflare One docs","description":"Connect to RDP with client-side cloudflared in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["RDP"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication/
  schema: 1
---
<p>End users can connect to an RDP server without the Cloudflare One Client by authenticating through <code>cloudflared</code> in their native terminal. This method requires having <code>cloudflared</code> installed on both the server machine and on the client machine, as well as an active zone on Cloudflare. The traffic is proxied over this connection, and the user logs in to the server with their Cloudflare Access credentials.</p>
<p>Client-side <code>cloudflared</code> can be used in conjunction with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-device-client/">the Cloudflare One Client</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Browser-based RDP</a> so that there are multiple ways to connect to the server. You can reuse the same Cloudflare Tunnel when configuring each connection method.</p>
<h2 id="1-connect-the-server-to-cloudflare"><ol>
<li>Connect the server to Cloudflare</li>
</ol></h2>
<ol>
<li>
<p>Create a Cloudflare Tunnel by following our <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">dashboard setup guide</a>.</p>
</li>
<li>
<p>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong> and select your tunnel.</p>
</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>
<p>On the <strong>Routes</strong> tab, select <strong>Add route</strong>, then select <strong>Published application</strong>.</p>
</li>
<li>
<p>Choose a domain from the drop-down menu and specify any subdomain (for example, <code>rdp.example.com</code>).</p>
</li>
<li>
<p>For <strong>Service</strong>, select <em>RDP</em> and enter the <a href="https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/change-listening-port">RDP listening port</a> of your server (for example, <code>localhost:3389</code>). It will likely be port <code>3389</code>.</p>
</li>
<li>
<p>Select <strong>Add route</strong>.</p>
</li>
</ol>
<h2 id="2-recommended-create-an-access-application"><ol start="2">
<li>(Recommended) Create an Access application</li>
</ol></h2>
<p>By default, anyone on the Internet can connect to the server using the hostname of the published application. To allow or block specific users, create a <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application</a> in Cloudflare Access.</p>
<h2 id="3-connect-as-a-user"><ol start="3">
<li>Connect as a user</li>
</ol></h2>
<ol>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">Install <code>cloudflared</code></a> on the client machine.</li>
<li>Run this command to open an RDP listening port:</li>
</ol>
<pre tabindex="0"><code class="language-sh">cloudflared access rdp --hostname rdp.example.com --url rdp://localhost:3389&#10;</code></pre>
<p>This process will need to be configured to stay alive and autostart. If the process is killed, users will not be able to connect.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5498.md")
</aside>
<ol start="3">
<li>While <code>cloudflared access</code> is running, connect from an RDP client such as Microsoft Remote Desktop:
<ol>
<li>Open Microsoft Remote Desktop and select <strong>Add a PC</strong>.</li>
<li>For <strong>PC name</strong>, enter <code>localhost:3389</code>.</li>
<li>For <strong>User account</strong>, enter your RDP server username and password.</li>
<li>Double-click the newly added PC.</li>
<li>When asked if you want to continue, select <strong>Continue</strong>.</li>
</ol>
</li>
</ol>
<p>When the client launches, a browser window will open and prompt the user to authenticate with Cloudflare Access.</p>
