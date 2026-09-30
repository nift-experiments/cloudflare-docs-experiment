---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-update-local-resolver/
  description: Learn about update local dns resolver in this guide.
  full_title: Update local DNS resolver · Cloudflare Learning Paths
  head_html: <title>Update local DNS resolver · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Learn about update local dns resolver in this guide."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-update-local-resolver/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-update-local-resolver/index.md"><meta property="og:title" content="Update local DNS resolver · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about update local dns resolver in this guide."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-update-local-resolver/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Gateway,Email security (formerly Area 1),Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-update-local-resolver/#page","headline":"Update local DNS resolver \u00b7 Cloudflare Learning Paths","description":"Learn about update local dns resolver in this guide.","url":"https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-update-local-resolver/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/cybersafe/gateway-onboarding/gateway-update-local-resolver/
  schema: 1
---
<p>With a Gateway location created, you have the ability to send traffic to your environment. You can test without risk by changing your DNS resolvers in your browser or network settings.</p>
<h2 id="change-dns-resolver-at-the-network-level">Change DNS resolver at the network level</h2>
<p>To configure your device to send traffic to Gateway:</p>
<details class="nb-details"><summary>macOS</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9701.md")
</div></details>
<details class="nb-details"><summary>Windows</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9702.md")
</div></details>
<details class="nb-details"><summary>Linux</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9703.md")
</div></details>
<details class="nb-details"><summary>iPhone</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9704.md")
</div></details>
<details class="nb-details"><summary>Android</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9705.md")
</div></details>
<h2 id="change-dns-resolver-in-the-browser">Change DNS resolver in the browser</h2>
<p>To configure your browser to send traffic to Gateway:</p>
<ol>
<li>
<p>Obtain your DNS over HTTPS (DoH) address:</p>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>DNS locations</strong>.</li>
<li>Select the default location.</li>
<li>Copy your <strong>DNS over HTTPS</strong> hostname: <code>https://&lt;YOUR_DOH_SUBDOMAIN&gt;.cloudflare-gateway.com/dns-query</code></li>
</ol>
</li>
<li>
<p>Follow the configuration instructions for your browser:</p>
</li>
</ol>
<details class="nb-details"><summary>Mozilla Firefox</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9706.md")
</div></details>
<details class="nb-details"><summary>Google Chrome</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9707.md")
</div></details>
<details class="nb-details"><summary>Microsoft Edge</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9708.md")
</div></details>
<details class="nb-details"><summary>Brave</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9709.md")
</div></details>
<details class="nb-details"><summary>Safari</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9710.md")
</div></details>
<ol start="3">
<li>Verify that third-party firewall or TLS decryption software does not inspect or block traffic to the DoH endpoint: <code>https://&lt;YOUR_DOH_SUBDOMAIN&gt;.cloudflare-gateway.com/dns-query</code>.</li>
</ol>
<h2 id="more-locations">More locations</h2>
<p>To configure your router or OS, or to add additional DNS endpoints, refer to <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS locations</a>.</p>
