---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/uninstall/
  description: Uninstall the Cloudflare One Client in Zero Trust.
  full_title: Uninstall the Cloudflare One Client · Cloudflare One docs
  head_html: <title>Uninstall the Cloudflare One Client · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Uninstall the Cloudflare One Client in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/uninstall/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/uninstall/index.md"><meta property="og:title" content="Uninstall the Cloudflare One Client · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Uninstall the Cloudflare One Client in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/uninstall/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/uninstall/#page","headline":"Uninstall the Cloudflare One Client \u00b7 Cloudflare One docs","description":"Uninstall the Cloudflare One Client in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/uninstall/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/uninstall/
  schema: 1
---
<p>The following procedures will uninstall the Cloudflare One Client (formerly WARP) from your device. If you used the Cloudflare One Client to deploy a root certificate, the certificate will also be removed.</p>
<h2 id="windows">Windows</h2>
<ol>
<li>Go to Windows Settings (Windows Key + I).</li>
<li>Select <strong>Apps</strong>.</li>
<li>Select <strong>Installed Apps</strong>.</li>
<li>Scroll to find the Cloudflare One Client application, click the three dots (...), and select <strong>Uninstall</strong>.</li>
</ol>
<h2 id="macos">macOS</h2>
<p>We include an uninstall script as part of the macOS package that you originally used.</p>
<ol>
<li>To find and run the uninstall script, run the following commands:</li>
</ol>
<pre tabindex="0"><code class="language-sh">cd /Applications/Cloudflare\ WARP.app/Contents/Resources&#10;./uninstall.sh&#10;</code></pre>
<ol start="2">
<li>If prompted, enter your admin credentials to proceed with the uninstall.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6051.md")
</aside>
<h2 id="linux">Linux</h2>
<p>On CentOS 8, RHEL 8:</p>
<pre tabindex="0"><code class="language-sh">sudo yum remove cloudflare-warp&#10;</code></pre>
<p>On Ubuntu 18.04, Ubuntu 20.04, Ubuntu 22.04, Debian 9, Debian 10, Debian 11:</p>
<pre tabindex="0"><code class="language-sh">sudo apt remove cloudflare-warp&#10;</code></pre>
<h2 id="ios-and-android">iOS and Android</h2>
<ol>
<li>Find the Cloudflare One Agent application (or the legacy 1.1.1.1 application) on the home screen.</li>
<li>Select and hold the application tile, and then select <strong>Remove App</strong>.</li>
<li>Select <strong>Delete App</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6050.md")
</aside>
