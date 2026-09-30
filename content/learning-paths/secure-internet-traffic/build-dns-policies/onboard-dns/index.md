---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/onboard-dns/
  description: Configure DNS filtering for a network.
  full_title: Onboard DNS for a network · Cloudflare Learning Paths
  head_html: <title>Onboard DNS for a network · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Configure DNS filtering for a network."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/onboard-dns/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/onboard-dns/index.md"><meta property="og:title" content="Onboard DNS for a network · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure DNS filtering for a network."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/onboard-dns/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Gateway,Cloudflare One,Data Loss Prevention,CASB,Browser Isolation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/onboard-dns/#page","headline":"Onboard DNS for a network \u00b7 Cloudflare Learning Paths","description":"Configure DNS filtering for a network.","url":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/onboard-dns/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-internet-traffic/build-dns-policies/onboard-dns/
  schema: 1
---
<p>The fastest way to start filtering DNS queries is to change your DNS resolver to use a specific Gateway endpoint. You can make this change at the browser, OS, or router level.</p>
<p>Choose this option if:</p>
<ul>
<li>You want to try out DNS filtering without installing software.</li>
<li>You do not need to filter by user identity.</li>
<li>You want to apply blanket DNS policies to all devices in a physical location, such as a retail store or office.</li>
</ul>
<h2 id="change-dns-resolver-in-browser">Change DNS resolver in browser</h2>
<p>To configure your browser to send traffic to Gateway:</p>
<ol>
<li>
<p>Obtain your DNS over HTTPS (DoH) address:</p>
<ol>
<li>Go to <strong>Gateway</strong> &gt; <strong>DNS locations</strong>.</li>
<li>Select <strong>Add a location</strong>.</li>
<li>Enter a name for the location.</li>
<li>Turn on <strong>Set as Default DNS Location</strong>.</li>
<li>Select <strong>Add location</strong>.</li>
<li>Copy your <strong>DNS over HTTPS</strong> hostname: <code>https://&lt;YOUR_DOH_SUBDOMAIN&gt;.cloudflare-gateway.com/dns-query</code></li>
</ol>
</li>
<li>
<p>Follow the configuration instructions for your browser:</p>
</li>
</ol>
<details class="nb-details"><summary>Mozilla Firefox</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10259.md")
</div></details>
<details class="nb-details"><summary>Google Chrome</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10260.md")
</div></details>
<details class="nb-details"><summary>Microsoft Edge</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10261.md")
</div></details>
<details class="nb-details"><summary>Brave</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10262.md")
</div></details>
<details class="nb-details"><summary>Safari</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10263.md")
</div></details>
<ol start="3">
<li>Verify that third-party firewall or TLS decryption software does not inspect or block traffic to the DoH endpoint: <code>https://&lt;YOUR_DOH_SUBDOMAIN&gt;.cloudflare-gateway.com/dns-query</code>.</li>
</ol>
<p>DNS filtering is now turned on for this browser.</p>
<p>To configure your router or OS, or to add additional DNS endpoints, refer to <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS locations</a>.</p>
