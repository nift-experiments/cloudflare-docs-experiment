---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-locations/
  description: Set up Gateway DNS locations.
  full_title: Gateway locations · Cloudflare Learning Paths
  head_html: <title>Gateway locations · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Set up Gateway DNS locations."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-locations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-locations/index.md"><meta property="og:title" content="Gateway locations · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Gateway DNS locations."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-locations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Gateway,Email security (formerly Area 1),Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-locations/#page","headline":"Gateway locations \u00b7 Cloudflare Learning Paths","description":"Set up Gateway DNS locations.","url":"https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-locations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/cybersafe/gateway-onboarding/gateway-locations/
  schema: 1
---
<div class="nb-glossary-definition"><p>DNS locations are a collection of DNS endpoints which can be mapped to physical entities such as offices, homes, or data centers.</p></div>
<p>The fastest way to start filtering DNS queries from a location is by changing the DNS resolvers at the router.</p>
<h2 id="add-a-dns-location">Add a DNS location</h2>
<p>To add a DNS location to Gateway:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Networks</strong> &gt; <strong>Resolvers &amp; Proxies</strong> &gt; <strong>DNS locations</strong>.</li>
<li>Select <strong>Add a location</strong>.</li>
<li>Choose a name for your DNS location.</li>
<li>Choose at least one <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#dns-endpoints">DNS endpoint</a> to resolve your organization's DNS queries.</li>
<li>(Optional) Toggle the following settings:
<ul>
<li><strong>Enable EDNS client subnet</strong> sends a user's IP geolocation to authoritative DNS nameservers. <span class="nb-glossary-tooltip" title="EDNS Client Subnet (ECS)">EDNS Client Subnet (ECS)</span> helps reduce latency by routing the user to the closest origin server. Cloudflare enables EDNS in a privacy preserving way by not sending the user's exact IP address but rather the first <code>/24</code> range of the larger range that contains their IP address. This <code>/24</code> range will share the same geographic location as the user's exact IP address.</li>
<li><strong>Set as Default DNS Location</strong> sets this location as the default DoH endpoint for DNS queries.</li>
</ul>
</li>
<li>Select <strong>Continue</strong>.</li>
<li>(Optional) Turn on source IP filtering for your configured endpoints, then add any source IPv4/IPv6 addresses to validate.
<ul>
<li>Endpoint authentication is required for standard IPv4 addresses and optional for dedicated IPv4 addresses.</li>
<li><strong>DoH endpoint filtering &amp; authentication</strong> lets you restrict DNS resolution to only valid identities or user tokens in addition to IPv4/IPv6 addresses.</li>
</ul>
</li>
<li>Select <strong>Continue</strong>.</li>
<li>Review the settings for your DNS location, then choose <strong>Done</strong>.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="captive-portal-limitation">Captive portal limitation</h3>
@markup("md", "content/.markup/bodies/9711.md")
</aside>
