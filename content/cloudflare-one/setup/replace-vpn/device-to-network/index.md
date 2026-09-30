---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-network/
  description: Connect a remote device to a private network using Cloudflare Tunnel and the Cloudflare One Client.
  full_title: Device to network · Cloudflare One docs
  head_html: <title>Device to network · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect a remote device to a private network using Cloudflare Tunnel and the Cloudflare One Client."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-network/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-network/index.md"><meta property="og:title" content="Device to network · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect a remote device to a private network using Cloudflare Tunnel and the Cloudflare One Client."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-network/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-network/#page","headline":"Device to network \u00b7 Cloudflare One docs","description":"Connect a remote device to a private network using Cloudflare Tunnel and the Cloudflare One Client.","url":"https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-network/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/setup/replace-vpn/device-to-network/
  schema: 1
---
<p>Connect a remote device to a private network so your users can securely access internal applications and services from anywhere, without the security risks and performance bottlenecks of a traditional VPN.</p>
<p>To explore other connection scenarios, refer to <a href="/cloudflare-one/setup/replace-vpn/">Replace your VPN</a>.</p>
<p>This guide follows the same steps as the <strong>Get Started</strong> onboarding wizard in the <a href="https://one.dash.cloudflare.com">Cloudflare One dashboard</a>.</p>
<h2 id="how-it-works">How it works</h2>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> is a network connector that creates an outbound-only connection between your private network and Cloudflare. No open inbound ports or firewall changes are required.</p>
<p>The <span class="nb-glossary-tooltip" title="Cloudflare One Client"><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a></span> is an app that you install on each user's device. It routes traffic through Cloudflare and into the tunnel, so users can reach internal resources from anywhere.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A Cloudflare account with a Zero Trust organization. If you have not set this up, refer to <a href="/cloudflare-one/setup/">Get started</a>.</li>
<li>A Linux, Windows, or macOS device on your private network to run the tunnel.</li>
<li>A Linux, Windows, or macOS device to install the Cloudflare One Client on.</li>
</ul>
<h2 id="step-1-assign-a-tunnel">Step 1: Assign a Tunnel</h2>
<p>Cloudflare Tunnel establishes an outbound connection between your resources and Cloudflare. This is how new devices can reach your private network. You can install Tunnel on any Windows, Mac, or Linux device currently in your private network.</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, select the <strong>Get Started</strong> tab.</li>
<li>For <strong>Replace my client-based or site-to-site VPN</strong>, select <strong>Get started</strong>.</li>
<li>For <strong>Device to network</strong>, select <strong>Continue</strong>.</li>
<li>On the <strong>Connect a remote device to a private network</strong> screen, select <strong>Continue</strong>.</li>
<li>On the <strong>Assign a Tunnel</strong> screen, use the dropdown to choose an existing tunnel or create a new one.</li>
<li>Select <strong>Continue</strong>.</li>
</ol>
<h2 id="step-2-set-your-tunnel-s-ip-range">Step 2: Set your Tunnel's IP range</h2>
<p>Add the IP range of your private network to the tunnel. This defines which internal resources your remote users can reach. Your tunnel accepts traffic to this range from devices enrolled in your Zero Trust organization.</p>
<ol>
<li>Enter your IP range (for example, <code>10.0.1.0/24</code>).</li>
<li>Select <strong>Continue</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5950.md")
</aside>
<h2 id="step-3-deploy-your-tunnel">Step 3: Deploy your Tunnel</h2>
<p>Install the <code>cloudflared</code> connector on a device in your private network and run the tunnel. This service creates the secure connection between your network and Cloudflare.</p>
<ol>
<li>
<p>Select your device's operating system and architecture.</p>
</li>
<li>
<p>Copy the install command and run it on your device. For Windows, open Command Prompt as an administrator. For all other operating systems, use a terminal window.</p>
<p>For macOS, the command looks similar to:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">brew install cloudflared &amp;&amp; sudo cloudflared service install &lt;YOUR_TUNNEL_TOKEN&gt;&#10;</code></pre>
<p>For Windows and Linux, the dashboard provides a download link and install command for your selected architecture. For more download options, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">Downloads</a>.</p>
<ol start="3">
<li>After <code>cloudflared</code> connects, the dashboard confirms the tunnel is active.</li>
<li>Select <strong>Continue</strong>.</li>
</ol>
<h2 id="step-4-enroll-your-devices">Step 4: Enroll your devices</h2>
<p>Device enrollment controls which users can connect their devices to your private network through Cloudflare. In this step, you register your first device by providing an email address and installing the Cloudflare One Client.</p>
<ol>
<li>Enter the email you want to use to enroll your first device.</li>
<li>Select your device's operating system.</li>
<li>Select <strong>Download to continue</strong> to download the Cloudflare One Client, or copy the download link to send to a different device.</li>
<li>Select <strong>Continue</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5949.md")
</aside>
<h2 id="step-5-complete-cloudflare-one-client-setup">Step 5: Complete Cloudflare One Client setup</h2>
<p>On your device, complete the Cloudflare One Client installation wizard. Then connect the Cloudflare One Client to your Zero Trust organization. For comprehensive OS-specific instructions, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">Manual deployment</a>.</p>
<ol>
<li>Open the Cloudflare One Client. On macOS, select the Cloudflare icon in your status bar. On Windows, select the Cloudflare icon in your system tray.</li>
<li>Go to <strong>Preferences</strong> &gt; <strong>Account</strong> &gt; <strong>Login to Cloudflare Zero Trust</strong>.</li>
<li>Enter your team name when prompted. Your team name is the unique identifier for your Zero Trust organization and was set when the organization was created. The dashboard displays your team name on this screen for easy reference.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5948.md")
</aside>
<ol start="4">
<li>Complete the authentication steps.</li>
<li>The Cloudflare One Client should show as <strong>Connected</strong>.</li>
<li>Select <strong>Continue</strong> in the dashboard.</li>
</ol>
<h2 id="step-6-verify-your-connection">Step 6: Verify your connection</h2>
<p>The dashboard confirms that you are securely connected. You now have remote access between your device and your private network resources.</p>
<p>To verify connectivity, try reaching a resource on your private network (for example, <code>http://10.0.1.100</code> or <code>ssh 10.0.1.50</code>).</p>
<h2 id="recommended-next-steps">Recommended next steps</h2>
<p>After verifying your connection, consider securing your private network with policies and access controls:</p>
<ul>
<li><strong>Set up Gateway policies</strong>: By default, all enrolled devices can reach your entire private network. Gateway policies let you scan, filter, and log traffic between your devices and your private network. For more information, refer to <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies</a>, <a href="/cloudflare-one/traffic-policies/network-policies/">Network policies</a>, and <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>.</li>
<li><strong>Create an Access application</strong>: Restrict access to specific applications or hostnames on your private network with identity-based rules. For more information, refer to <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Secure a private IP or hostname</a>.</li>
<li><strong>Explore more with Zero Trust</strong>: Review your tunnel, policies, and connected devices in the <a href="https://one.dash.cloudflare.com">Cloudflare One dashboard</a>.</li>
</ul>
<p>For in-depth guidance on policy design and device posture checks, refer to the <a href="/learning-paths/replace-vpn/concepts/">Replace your VPN learning path</a>.</p>
<h2 id="troubleshoot">Troubleshoot</h2>
<p>If you have issues connecting, refer to these resources:</p>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/">Troubleshoot WARP</a>: resolve Cloudflare One Client connection and enrollment issues.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/">Troubleshoot tunnels</a>: diagnose tunnel connectivity and routing problems.</li>
</ul>
