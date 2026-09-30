---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-device/
  description: Create a secure connection between two devices using Cloudflare Mesh and Cloudflare's network.
  full_title: Device to device · Cloudflare One docs
  head_html: <title>Device to device · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a secure connection between two devices using Cloudflare Mesh and Cloudflare&#x27;s network."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-device/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-device/index.md"><meta property="og:title" content="Device to device · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a secure connection between two devices using Cloudflare Mesh and Cloudflare&#x27;s network."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-device/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-device/#page","headline":"Device to device \u00b7 Cloudflare One docs","description":"Create a secure connection between two devices using Cloudflare Mesh and Cloudflare's network.","url":"https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-device/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/setup/replace-vpn/device-to-device/
  schema: 1
---
<p>Create a secure connection between two devices so they can communicate directly through Cloudflare's network, without needing to be on the same physical network. This is useful when you need to remotely access a specific device, for example connecting to a home computer from a laptop at a coffee shop.</p>
<p>To explore other connection scenarios, refer to <a href="/cloudflare-one/setup/replace-vpn/">Replace your VPN</a>.</p>
<h2 id="how-it-works">How it works</h2>
<p>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> is an app that you install on each device you want to connect. When you enroll a device in your Cloudflare account, it is assigned a <a href="/cloudflare-one/networks/routes/reserved-ips/#device-ips">Mesh IP</a>.</p>
<p>Devices use their Mesh IPs to communicate with each other through Cloudflare's network. This works for most common types of network traffic, including web requests, remote desktop, file sharing, and ping.</p>
<p>Only devices enrolled in your Cloudflare account can reach these addresses, so they are not accessible to anyone outside your organization. No tunnel infrastructure or network configuration is required, and the connection does not disrupt existing traffic on your network.</p>
<p>For more details, refer to <a href="/mesh/guides/connect-client-devices/">Connect client devices</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a></li>
<li>Two Linux, Windows, macOS, Android, or iOS devices you want to connect together.</li>
</ul>
<h2 id="step-1-enroll-your-first-device">Step 1: Enroll your first device</h2>
<p>Enrollment permissions control which users can connect devices to your account. In this step, you set an enrollment email and download the Cloudflare One Client. The email you provide becomes the first allowed login for your organization, and anyone with that email address can enroll a device.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Mesh</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add a node</strong>, then follow the wizard. The wizard configures enrollment permissions and Mesh connectivity automatically.</li>
<li>Download the Cloudflare One Client on your first device from the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">downloads page</a>.</li>
<li>Open the client, enter your team name, and sign in with your email.</li>
</ol>
<h2 id="step-2-enroll-your-second-device">Step 2: Enroll your second device</h2>
<p>Both devices must be enrolled in your Cloudflare account for the connection to work.</p>
<ol>
<li>Download the Cloudflare One Client on your second device.</li>
<li>Open the client, enter the same team name, and sign in.</li>
<li>The client should show as <strong>Connected</strong> on both devices.</li>
</ol>
<h2 id="step-3-verify-your-connection">Step 3: Verify your connection</h2>
<p>Both devices are now connected through Cloudflare's network using their assigned Mesh IPs.</p>
<p>To view your device's assigned Mesh IP:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Mesh</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Your connected devices appear with their Mesh IPs.</li>
</ol>
<p>To test connectivity, <code>ping</code> the Mesh IP of one device from the other.</p>
<h2 id="recommended-next-steps">Recommended next steps</h2>
<p>After verifying your connection, consider securing your connected devices with policies and access controls:</p>
<ul>
<li><strong>Set up Gateway policies</strong>: By default, all enrolled devices can reach each other over the Mesh IP space. Gateway policies let you scan, filter, and log traffic between your devices. For more information, refer to <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies</a>, <a href="/cloudflare-one/traffic-policies/network-policies/">Network policies</a>, and <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>.</li>
<li><strong>Create an Access application</strong>: Restrict access to specific destinations on enrolled devices with identity-based rules. For more information, refer to <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Secure a private IP or hostname</a>.</li>
</ul>
<p>For in-depth guidance on policy design and device posture checks, refer to the <a href="/learning-paths/replace-vpn/concepts/">Replace your VPN learning path</a>.</p>
<h2 id="troubleshoot">Troubleshoot</h2>
<p>If you have issues connecting, try these steps:</p>
<ul>
<li><strong>Windows users</strong>: Windows Firewall blocks device-to-device traffic by default. You may need to add a firewall rule that allows incoming traffic from <code>100.96.0.0/12</code>. For details, refer to <a href="/mesh/guides/connect-client-devices/">Connect client devices</a>.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/">Troubleshoot the Cloudflare One Client</a>: resolve connection and enrollment issues.</li>
</ul>
