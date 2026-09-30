---
cp9:
  canonical: https://developers.cloudflare.com/warp-client/get-started/macos/
  description: Install and configure WARP on macOS.
  full_title: macOS desktop client · Cloudflare WARP client docs
  head_html: <title>macOS desktop client · Cloudflare WARP client docs</title><meta name="generator" content="Nift"><meta name="description" content="Install and configure WARP on macOS."><link rel="canonical" href="https://developers.cloudflare.com/warp-client/get-started/macos/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/warp-client/get-started/macos/index.md"><meta property="og:title" content="macOS desktop client · Cloudflare WARP client docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Install and configure WARP on macOS."><meta property="og:url" content="https://developers.cloudflare.com/warp-client/get-started/macos/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WARP Client"><meta name="algolia_product_filter" content="WARP Client"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="WARP Client"><meta name="pcx_tags" content="MacOS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/warp-client/get-started/macos/#page","headline":"macOS desktop client \u00b7 Cloudflare WARP client docs","description":"Install and configure WARP on macOS.","url":"https://developers.cloudflare.com/warp-client/get-started/macos/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["MacOS"]}</script>
  markdown: true
  noindex: false
  route: /warp-client/get-started/macos/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-zero-trust">Looking for Zero Trust?</h3>
@markup("md", "content/.markup/bodies/15769.md")
</aside>
<ol>
<li><a href="https://downloads.cloudflareclient.com/v1/download/macos/ga">Download</a> Cloudflare WARP for macOS.</li>
<li>Go to your predefined download folder and open the <code>.pkg</code> file.</li>
<li>Follow the instructions to complete installation. Cloudflare WARP will automatically launch and appear in your menu bar with the Cloudflare logo.</li>
<li>Select <strong>Next</strong> and <strong>Accept</strong> Cloudflare's privacy policy.</li>
<li>Turn on the toggle to enable WARP.</li>
</ol>
<p>WARP is now running and protecting your Internet connection.</p>
<h2 id="warp-modes">WARP modes</h2>
<p>The WARP app has two main modes of operation: WARP and 1.1.1.1.</p>
<p>In WARP mode, all traffic leaving your computer is encrypted and sent over WARP, including DNS traffic. In 1.1.1.1 mode, the WARP app only encrypts DNS traffic to the 1.1.1.1 resolver.</p>
<p>WARP mode is the default and the recommended mode of operation. However, if you only want to use the 1.1.1.1 resolver mode:</p>
<ol>
<li>Select the WARP app icon.</li>
<li>Select the cog icon, and choose your preferred mode of operation for WARP.</li>
</ol>
<h2 id="warp-options">WARP options</h2>
<p>Beyond the two modes of operation, the WARP app lets you configure additional options to better suit your needs. You can change the protocol used to connect to Cloudflare or enable <a href="/1.1.1.1/setup/#1111-for-families">1.1.1.1 for Families</a>, for example. To access these options:</p>
<ol>
<li>Select the WARP app icon.</li>
<li>Select the <strong>cog icon</strong> &gt; <strong>Preferences</strong>.</li>
</ol>
<p>The following is a list of options you can configure in the <strong>Connection</strong> tab:</p>
<ul>
<li><strong>Disable for all Wi-Fi / wired networks</strong>: Check the box corresponding to the network where you want to prevent WARP from working on.</li>
<li><strong>DNS Protocol</strong>: The available options depend on the WARP mode you have enabled:
<ul>
<li><strong>WARP</strong>: Only available when you have the WARP mode enabled. All DNS traffic encrypted and <a href="/warp-client/warp-modes/#1111-with-warp">sent to Cloudflare's global network</a>.</li>
<li><strong>HTTPS</strong>: All DNS traffic is sent outside the tunnel via <a href="/1.1.1.1/encryption/dns-over-https/">DNS over HTTPS</a>.</li>
<li><strong>TLS</strong>: All DNS traffic is sent outside the tunnel via <a href="/1.1.1.1/encryption/dns-over-tls/">encrypted TLS</a>.</li>
</ul>
</li>
<li><strong>1.1.1.1 for Families</strong>: Allows you to <a href="/1.1.1.1/setup/#1111-for-families">enable 1.1.1.1 for Families</a> and choose between blocking malware, or blocking malware and adult content.</li>
</ul>
<p>For the <strong>Advanced</strong> options, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/">Exclude or include network traffic with WARP</a> for more information.</p>
<h2 id="what-cloudflare-places-on-your-device">What Cloudflare places on your device</h2>
<h3 id="cloudflare-warp-app">Cloudflare WARP.app</h3>
<p>This is the main GUI application that you interact with. You can find it in<code>/Applications/Cloudflare WARP.app</code>.</p>
<h3 id="cloudflare-warp-daemon">Cloudflare WARP Daemon</h3>
<p>This is the daemon service responsible for establishing the wireguard tunnel and all interaction between our service endpoint and the Cloudflare WARP application. Here is where you can find:</p>
<ul>
<li><strong>Service</strong>: <code>/Applications/Cloudflare WARP.app/Contents/Resources/CloudflareWARP</code></li>
<li><strong>Definition</strong>: <code>/Library/LaunchDaemons/com.cloudflare.1dot1dot1dot1.macos.warp.daemon.plist</code></li>
</ul>
<h3 id="log-files">Log files</h3>
<p>The macOS application places log files in two locations based on what part of the app is logging information. These logs are included with a feedback submission, when you select the checkbox in <strong>Feedback</strong> &gt; <strong>Share debug information</strong>.</p>
<ul>
<li><strong>Daemon and install logs</strong>: <code>/Library/Application Support/Cloudflare</code>.</li>
<li><strong>Application GUI logs</strong>: <code>/Users/&lt;your local username&gt;/Library/Logs/Cloudflare</code>.</li>
</ul>
<h2 id="how-to-remove-the-application">How to remove the application</h2>
<p>We include an uninstall script as part of the macOS package you install. Type the following in a terminal window to uninstall WARP:</p>
<pre tabindex="0"><code class="language-sh">cd /Applications/Cloudflare\ WARP.app/Contents/Resources&#10;./uninstall.sh&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/15768.md")
</aside>
