---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-cloudflared-authentication/
  description: Connect to SSH with client-side cloudflared in Zero Trust networking.
  full_title: Connect to SSH with client-side cloudflared · Cloudflare One docs
  head_html: <title>Connect to SSH with client-side cloudflared · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect to SSH with client-side cloudflared in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-cloudflared-authentication/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-cloudflared-authentication/index.md"><meta property="og:title" content="Connect to SSH with client-side cloudflared · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect to SSH with client-side cloudflared in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-cloudflared-authentication/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SSH"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-cloudflared-authentication/#page","headline":"Connect to SSH with client-side cloudflared \u00b7 Cloudflare One docs","description":"Connect to SSH with client-side cloudflared in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-cloudflared-authentication/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SSH"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-cloudflared-authentication/
  schema: 1
---
<p>End users can connect to an SSH server without the Cloudflare One Client by authenticating through <code>cloudflared</code> in their native terminal. This method requires having <code>cloudflared</code> installed on both the server machine and on the client machine, as well as an active zone on Cloudflare. The traffic is proxied over this connection, and the user logs in to the server with their Cloudflare Access credentials.</p>
<p>Client-side <code>cloudflared</code> can be used in conjunction with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-device-client/">the Cloudflare One Client</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Access for Infrastructure</a> so that there are multiple ways to connect to the server. You can reuse the same Cloudflare Tunnel when configuring each connection method.</p>
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
<p>Choose a domain from the drop-down menu and specify any subdomain (for example, <code>ssh.example.com</code>).</p>
</li>
<li>
<p>For <strong>Service</strong>, select <em>SSH</em> and enter <code>localhost:22</code>. If the SSH server is on a different machine from where you installed the tunnel, enter <code>&lt;server IP&gt;:22</code>.</p>
</li>
<li>
<p>Select <strong>Add route</strong>.</p>
</li>
<li>
<p>(Recommended) Add a <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application</a> to Cloudflare Access in order to manage access to your server.</p>
</li>
</ol>
<h2 id="2-connect-as-a-user"><ol start="2">
<li>Connect as a user</li>
</ol></h2>
<ol>
<li>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">Install <code>cloudflared</code></a> on the client machine.</p>
</li>
<li>
<p>Make a one-time change to your SSH configuration file:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">vim ~/.ssh/config&#10;</code></pre>
<ol start="3">
<li>Input the following values; replacing <code>ssh.example.com</code> with the hostname you created.</li>
</ol>
<pre tabindex="0"><code class="language-txt">Host ssh.example.com&#10;ProxyCommand /usr/local/bin/cloudflared access ssh --hostname %h&#10;</code></pre>
<p>The <code>cloudflared</code> path may be different depending on your OS and package manager. For example, if you installed <code>cloudflared</code> on macOS with Homebrew, check its path by running <code>brew --prefix cloudflared</code>.</p>
<ol start="4">
<li>You can now test the connection by running a command to reach the service:</li>
</ol>
<pre tabindex="0"><code class="language-sh">ssh &lt;username&gt;@ssh.example.com&#10;</code></pre>
<p>When the command is run, <code>cloudflared</code> will launch a browser window to prompt you to authenticate with your identity provider before establishing the connection from your terminal.</p>
