---
cp9:
  canonical: https://developers.cloudflare.com/warp-client/get-started/linux/
  description: Install and configure WARP on Linux.
  full_title: Linux desktop client · Cloudflare WARP client docs
  head_html: <title>Linux desktop client · Cloudflare WARP client docs</title><meta name="generator" content="Nift"><meta name="description" content="Install and configure WARP on Linux."><link rel="canonical" href="https://developers.cloudflare.com/warp-client/get-started/linux/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/warp-client/get-started/linux/index.md"><meta property="og:title" content="Linux desktop client · Cloudflare WARP client docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Install and configure WARP on Linux."><meta property="og:url" content="https://developers.cloudflare.com/warp-client/get-started/linux/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WARP Client"><meta name="algolia_product_filter" content="WARP Client"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="WARP Client"><meta name="pcx_tags" content="Linux,CLI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/warp-client/get-started/linux/#page","headline":"Linux desktop client \u00b7 Cloudflare WARP client docs","description":"Install and configure WARP on Linux.","url":"https://developers.cloudflare.com/warp-client/get-started/linux/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Linux","CLI"]}</script>
  markdown: true
  noindex: false
  route: /warp-client/get-started/linux/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-zero-trust">Looking for Zero Trust?</h3>
@markup("md", "content/.markup/bodies/15772.md")
</aside>
<p>You have two ways of installing WARP on Linux, depending on the distro you are using:</p>
<ul>
<li>Find the latest WARP client in the <a href="https://pkg.cloudflareclient.com/">package repository</a>.</li>
<li>Install the <code>cloudflare-warp</code> package that suits your distro:
<ul>
<li><strong>apt-based OS</strong> (like Ubuntu): <code>sudo apt install cloudflare-warp</code>.</li>
<li><strong>yum-based OS</strong> (like CentOS or RHEL): <code>sudo yum install cloudflare-warp</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15771.md")
</aside>
<h2 id="using-warp">Using WARP</h2>
<p>The command line interface is the primary way to use WARP.</p>
<h3 id="initial-connection">Initial connection</h3>
<p>To connect for the very first time:</p>
<ol>
<li>Register the client <code>warp-cli registration new</code>.</li>
<li>Connect <code>warp-cli connect</code>.</li>
<li>Run <code>curl https://www.cloudflare.com/cdn-cgi/trace</code> and verify that <code>warp=on</code>.</li>
</ol>
<h3 id="switch-modes">Switch modes</h3>
<p>You can use <code>warp-cli mode --help</code> to get a list of modes to switch between. For example:</p>
<ul>
<li><strong>DNS only mode via DoH:</strong> <code>warp-cli mode doh</code></li>
<li><strong>WARP with DoH:</strong> <code>warp-cli mode warp+doh</code></li>
</ul>
<h3 id="switch-tunnel-protocol">Switch tunnel protocol</h3>
<p>You can switch the protocol that WARP uses to route traffic from the device to Cloudflare.</p>
<ul>
<li><strong>WireGuard:</strong> <code>warp-cli tunnel protocol set WireGuard</code></li>
<li><strong>MASQUE:</strong> (default) <code>warp-cli tunnel protocol set MASQUE</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15770.md")
</aside>
<p>For information on WireGuard versus MASQUE, refer to our <a href="https://blog.cloudflare.com/zero-trust-warp-with-a-masque">blog post</a>.</p>
<h3 id="using-1-1-1-1-for-families">Using 1.1.1.1 for Families</h3>
<p>The Linux client supports all 1.1.1.1 for Families modes, in either WARP on DNS-only mode:</p>
<ul>
<li><strong>Families mode off:</strong> <code>warp-cli dns families off</code></li>
<li><strong>Malware protection:</strong> <code>warp-cli dns families malware</code></li>
<li><strong>Malware and adult content:</strong> <code>warp-cli dns families full</code></li>
</ul>
<h3 id="enable-warp-unlimited">Enable WARP+ Unlimited</h3>
<p>To enable <a href="/warp-client/warp-modes/#warp-unlimited">WARP+ Unlimited</a> on Linux, you will need an iOS or Android device that has an existing WARP+ Unlimited subscription.</p>
<ol>
<li>On your iOS or Android device, launch the <strong>1.1.1.1 Faster Internet</strong> app.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Account</strong> and copy the <strong>Key</strong> value.</li>
<li>On your Linux device, run the following command:</li>
</ol>
<pre tabindex="0"><code class="language-sh">warp-cli registration license &lt;KEY&gt;&#10;</code></pre>
<ol start="4">
<li>Verify the new registration:</li>
</ol>
<pre tabindex="0"><code class="language-sh">warp-cli registration show&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Account type: Unlimited&#10;...&#10;</code></pre>
<p>Your WARP+ Unlimited subscription is now active on this device.</p>
<h3 id="additional-commands">Additional commands</h3>
<p>A complete list of all supported commands can be found by running:</p>
<pre tabindex="0"><code class="language-sh">warp-cli --help&#10;</code></pre>
<h2 id="feedback">Feedback</h2>
<p>You can find logs required to debug WARP issues by running <code>sudo warp-diag</code>. This will place a <code>warp-debugging-info.zip</code> file in the path from which you ran the command.</p>
<p>To report bugs or provide feedback to the team use the command <code>sudo warp-diag feedback</code>. This will submit a support ticket.</p>
