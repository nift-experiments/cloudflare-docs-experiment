---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/setup/android/
  description: Learn how to set up Cloudflare's 1.1.1.1 DNS resolver on Android devices. Encrypt DNS queries with DoT or DoH, and enable 1.1.1.1 for Families.
  full_title: Set up 1.1.1.1 on Android · Cloudflare 1.1.1.1 docs
  head_html: <title>Set up 1.1.1.1 on Android · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to set up Cloudflare&#x27;s 1.1.1.1 DNS resolver on Android devices. Encrypt DNS queries with DoT or DoH, and enable 1.1.1.1 for Families."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/setup/android/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/setup/android/index.md"><meta property="og:title" content="Set up 1.1.1.1 on Android · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to set up Cloudflare&#x27;s 1.1.1.1 DNS resolver on Android devices. Encrypt DNS queries with DoT or DoH, and enable 1.1.1.1 for Families."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/setup/android/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/setup/android/#page","headline":"Set up 1.1.1.1 on Android \u00b7 Cloudflare 1.1.1.1 docs","description":"Learn how to set up Cloudflare's 1.1.1.1 DNS resolver on Android devices. Encrypt DNS queries with DoT or DoH, and enable 1.1.1.1 for Families.","url":"https://developers.cloudflare.com/1.1.1.1/setup/android/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/setup/android/
  schema: 1
---
<p>The <a href="https://play.google.com/store/apps/details?id=com.cloudflare.onedotonedotonedotone">1.1.1.1: Faster Internet</a> app is the recommended way to set up 1.1.1.1 on Android. It automatically configures your phone to use 1.1.1.1 on any network you connect to.</p>
<p>The app also allows you to enable encryption for DNS queries or enable <a href="/warp-client/">WARP mode</a>, which keeps all your HTTP traffic private and secure, including your DNS queries to 1.1.1.1.</p>
<p>You can select between these options in the app settings. By default, the app uses WARP mode.</p>
<h2 id="set-up-1-1-1-1-faster-internet">Set up 1.1.1.1: Faster Internet</h2>
<ol>
<li>Download <a href="https://play.google.com/store/apps/details?id=com.cloudflare.onedotonedotonedotone">1.1.1.1: Faster Internet from Google Play</a> for free.</li>
<li>Launch 1.1.1.1: Faster Internet and accept the Terms of Service.</li>
<li>Toggle the <strong>WARP</strong> button to <strong>Connected</strong>.</li>
<li>Install the VPN profile that allows your phone to connect securely to 1.1.1.1.</li>
</ol>
<p>Your connection to the Internet and your DNS queries are now protected.</p>
<h3 id="enable-1-1-1-1-for-families">Enable 1.1.1.1 for Families</h3>
<ol>
<li>Open 1.1.1.1: Faster Internet.</li>
<li>Tap the <strong>menu button</strong>.</li>
<li>Select <strong>Advanced</strong> &gt; <strong>Connection options</strong>.</li>
<li>In <strong>DNS settings</strong> &gt; <strong>1.1.1.1 for Families</strong>, select the option you want to use.</li>
</ol>
<h2 id="configure-1-1-1-1-manually">Configure 1.1.1.1 manually</h2>
<h3 id="android-9-and-later">Android 9 and later</h3>
<p>Android 9 and later support encrypted DNS through a feature called Private DNS, which uses DNS-over-TLS (DoT), or DNS-over-HTTP/3. When you configure Private DNS, your device uses that DNS resolver on all networks — including cellular.</p>
<ol>
<li>Go to <strong>Settings</strong> &gt; <strong>Network &amp; internet</strong>.</li>
<li>Select <strong>Advanced</strong> &gt; <strong>Private DNS</strong>.</li>
<li>Select the <strong>Private DNS provider hostname</strong> option.</li>
<li>Enter one of the following hostnames and select <strong>Save</strong>.</li>
</ol>
  <details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1804.md")
</div></details>
  <details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1805.md")
</div></details>
  <details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1806.md")
</div></details>
<h3 id="previous-android-versions">Previous Android versions</h3>
<p>Before making changes, take note of any DNS addresses you might have and save them in a safe place in case you need to use them later.</p>
<ol>
<li>Open <strong>Settings</strong> &gt; <strong>Wi-Fi</strong>.</li>
<li>Press down and hold the name of the network you are currently connected to.</li>
<li>Select <strong>Modify Network</strong>.</li>
<li>Select the checkbox <strong>Show Advanced Options</strong>.</li>
<li>Change the IP Settings to <strong>Static</strong>.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv4:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1807.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1808.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1809.md")
</div></details>
<ol start="7">
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv6:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1810.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1811.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1812.md")
</div></details>
<ol start="8">
<li>Select <strong>Save</strong>. You may need to disconnect from the Wi-Fi and reconnect for the changes to take effect.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1803.md")
</aside>
