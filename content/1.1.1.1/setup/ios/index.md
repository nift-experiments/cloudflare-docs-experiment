---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/setup/ios/
  description: Configure 1.1.1.1 on iOS devices.
  full_title: Set up 1.1.1.1 on iOS · Cloudflare 1.1.1.1 docs
  head_html: <title>Set up 1.1.1.1 on iOS · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure 1.1.1.1 on iOS devices."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/setup/ios/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/setup/ios/index.md"><meta property="og:title" content="Set up 1.1.1.1 on iOS · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure 1.1.1.1 on iOS devices."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/setup/ios/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/setup/ios/#page","headline":"Set up 1.1.1.1 on iOS \u00b7 Cloudflare 1.1.1.1 docs","description":"Configure 1.1.1.1 on iOS devices.","url":"https://developers.cloudflare.com/1.1.1.1/setup/ios/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/setup/ios/
  schema: 1
---
<p>The <a href="https://apps.apple.com/us/app/1-1-1-1-faster-internet/id1423538627">1.1.1.1: Faster Internet</a> app is the recommended way to set up 1.1.1.1 on iOS. It automatically configures your device to use 1.1.1.1 on any network you connect to, including cellular networks (which cannot use a custom DNS resolver through manual iOS settings alone).</p>
<p>The app also allows you to enable encryption for DNS queries or enable <a href="/warp-client/">WARP mode</a>, which keeps all your HTTP traffic private and secure, including your DNS queries to 1.1.1.1.</p>
<p>You can select between these options in the app settings. By default, the app uses WARP mode.</p>
<h2 id="set-up-1-1-1-1-faster-internet">Set up 1.1.1.1: Faster Internet</h2>
<ol>
<li>Download <a href="https://apps.apple.com/us/app/1-1-1-1-faster-internet/id1423538627">1.1.1.1: Faster Internet from the App Store</a> for free.</li>
<li>Launch 1.1.1.1: Faster Internet and accept the Terms of Service.</li>
<li>Install the VPN profile that allows your phone to connect securely to 1.1.1.1.</li>
<li>Toggle the <strong>WARP</strong> button to <strong>Connected</strong>.</li>
</ol>
<h3 id="enable-1-1-1-1-for-families">Enable 1.1.1.1 for Families</h3>
<ol>
<li>Open 1.1.1.1: Faster Internet.</li>
<li>Tap the <strong>menu button</strong>.</li>
<li>Select <strong>Advanced</strong> &gt; <strong>Connection options</strong>.</li>
<li>In <strong>DNS settings</strong> &gt; <strong>1.1.1.1 for Families</strong>, select the option you want to use.</li>
</ol>
<h2 id="configure-1-1-1-1-manually">Configure 1.1.1.1 manually</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1787.md")
</aside>
<p>Take note of any DNS addresses you might have set up, and save them in a safe place in case you need to use them later.</p>
<ol>
<li>Go to <strong>Settings</strong> &gt; <strong>Wi-Fi</strong>.</li>
<li>Select the <strong>'i'</strong> icon next to the Wi-Fi network you are connected to.</li>
<li>Scroll down and select <strong>Configure DNS</strong>.</li>
<li>Change the configuration from <strong>Automatic</strong> to <strong>Manual</strong>.</li>
<li>Select <strong>Add Server</strong>.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv4:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1788.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1789.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1790.md")
</div></details>
<ol start="7">
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv6:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1791.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1792.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1793.md")
</div></details>
<ol start="8">
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1786.md")
</aside>
