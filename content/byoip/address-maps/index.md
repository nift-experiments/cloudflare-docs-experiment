---
cp9:
  canonical: https://developers.cloudflare.com/byoip/address-maps/
  description: Map IP prefixes to zones and accounts with address maps.
  full_title: About address maps · Cloudflare BYOIP docs
  head_html: <title>About address maps · Cloudflare BYOIP docs</title><meta name="generator" content="Nift"><meta name="description" content="Map IP prefixes to zones and accounts with address maps."><link rel="canonical" href="https://developers.cloudflare.com/byoip/address-maps/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/byoip/address-maps/index.md"><meta property="og:title" content="About address maps · Cloudflare BYOIP docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Map IP prefixes to zones and accounts with address maps."><meta property="og:url" content="https://developers.cloudflare.com/byoip/address-maps/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="BYOIP"><meta name="algolia_product_filter" content="BYOIP"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="BYOIP"><meta name="pcx_tags" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/byoip/address-maps/#page","headline":"About address maps \u00b7 Cloudflare BYOIP docs","description":"Map IP prefixes to zones and accounts with address maps.","url":"https://developers.cloudflare.com/byoip/address-maps/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS"]}</script>
  markdown: true
  noindex: false
  route: /byoip/address-maps/
  schema: 1
---
<div class="nb-glossary-definition"><p>Address map is a data structure enabling customers with BYOIP prefixes or account-level static IPs to specify which IP addresses should be mapped to DNS records when they are proxied through Cloudflare.</p></div>
<p>By default, Cloudflare responds to DNS queries for proxied hostnames with Cloudflare-owned <a href="/fundamentals/concepts/cloudflare-ip-addresses/">anycast IP addresses</a>. Address maps allow you to override this behavior — when a zone or account is associated with an address map, Cloudflare responds with the IP addresses you specify instead.</p>
<p>To use address maps, you must first have <a href="/byoip/">BYOIP</a> prefixes or <a href="/byoip/concepts/static-ips/">static IPs</a> configured on your account. You can <a href="/fundamentals/concepts/cloudflare-ip-addresses/#customize-cloudflare-ip-addresses">customize the IPs Cloudflare uses</a> through either approach. If you are interested in address maps but do not yet have BYOIP or static IPs, contact your account manager.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3787.md")
</aside>
<hr />
<h2 id="how-address-maps-works">How Address Maps works</h2>
<p>For zones using <a href="/dns/">Cloudflare's authoritative DNS</a>, Cloudflare typically responds to DNS queries for proxied hostnames with <a href="/fundamentals/concepts/cloudflare-ip-addresses/">anycast IPs</a>. However, if you <a href="/fundamentals/concepts/cloudflare-ip-addresses/#customize-cloudflare-ip-addresses">customize the IPs Cloudflare uses</a> and use Address Maps, Cloudflare will respond with the IP address(es) on the address map.</p>
<p>Address maps do not change <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy">how Cloudflare reaches the configured origin</a>. The IP addresses defined on your zone's <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records">DNS Records</a> continue to instruct Cloudflare how to reach the origin.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3786.md")
</aside>
<h3 id="static-ips-or-byoip">Static IPs or BYOIP</h3>
<p>Leased static IPs allow you to use a set of specifically assigned Cloudflare IPs to ensure they do not change. Cloudflare creates an address map with your static IPs that you may edit. You cannot create another map using your static IPs.</p>
<p>With BYOIP, you use your IPs by bringing an address space that you lease or own and creating an address map.</p>
<hr />
<h2 id="immutable-address-maps">Immutable address maps</h2>
<p>Some customers may only proxy zones through BYOIP addresses, and are prohibited from using Cloudflare IP addresses for proxied DNS names. In this case, Cloudflare will create an immutable, account-wide address map to ensure all zones in your account receive BYOIP addresses as a fallback. These address maps cannot be deleted.</p>
<p>It is still possible to create more specific zone-level address maps with specific BYOIPs, but DNS will fall back to the account-wide address map without one.</p>
<p>To specify different addresses for certain zones, <a href="/byoip/address-maps/setup/">create a new address map</a>.</p>
<hr />
<h2 id="spectrum-compatibility">Spectrum compatibility</h2>
<p>You can use address maps to set up <a href="/byoip/address-maps/setup/#spectrum-https-applications">non-SNI support</a> for Spectrum HTTPS applications.</p>
<p>However, to control what IP address Cloudflare will use when responding to requests for your Spectrum applications, you should first refer to their respective configuration and set the <code>edge_ips</code> field as <code>static</code>, e.g.:</p>
<pre tabindex="0"><code class="language-json">&quot;edge_ips&quot;: {&#10;  &quot;type&quot;: &quot;static&quot;,&#10;  &quot;ips&quot;: [&quot;1.2.3.4&quot;]&#10;}&#10;</code></pre>
<p>For details, refer to the <a href="/api/resources/spectrum#%28resource%29%20spectrum%20%3E%20%28model%29%20edge_ips%20%3E%20%28schema%29%20%3E%20%28variant%29%201">Spectrum API</a>.</p>
