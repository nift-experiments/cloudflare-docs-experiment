---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/non-identity/
  description: Non-identity on-ramps in Browser Isolation.
  full_title: Non-identity on-ramps · Cloudflare One docs
  head_html: <title>Non-identity on-ramps · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Non-identity on-ramps in Browser Isolation."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/non-identity/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/non-identity/index.md"><meta property="og:title" content="Non-identity on-ramps · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Non-identity on-ramps in Browser Isolation."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/non-identity/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/non-identity/#page","headline":"Non-identity on-ramps \u00b7 Cloudflare One docs","description":"Non-identity on-ramps in Browser Isolation.","url":"https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/non-identity/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/remote-browser-isolation/setup/non-identity/
  schema: 1
---
<p>On-ramps are the methods used to route traffic from your network to Cloudflare for inspection. With Cloudflare One, you can isolate HTTP traffic from on-ramps such as <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints</a> (which your browser connects to via PAC files to send traffic through Gateway) or <a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Cloudflare WAN</a> (formerly Magic WAN, which connects your network to Cloudflare through GRE or IPsec tunnels). Since these on-ramps do not require users to log in to the Cloudflare One Client, <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity-based policies</a> are not supported.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5887.md")
</aside>
<h2 id="set-up-non-identity-browser-isolation">Set up non-identity browser isolation</h2>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">Install a Cloudflare certificate</a> on your devices.</li>
<li>Connect your infrastructure to Gateway using one of the following on-ramps:
<ul>
<li>Configure your browser to forward traffic to a Gateway proxy endpoint with <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">PAC files</a> (Proxy Auto-Configuration files that tell the browser which traffic to route through the proxy).</li>
<li>Connect your enterprise site router to Gateway with the <a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">anycast GRE or IPsec tunnel on-ramp to Cloudflare WAN</a> (site-to-site encrypted tunnels between your network and Cloudflare).</li>
</ul>
</li>
<li>Enable non-identity browser isolation:
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Browser isolation</strong> &gt; <strong>Browser isolation settings</strong>.</li>
<li>Turn on <strong>Allow isolated HTTP traffic when user identity is unknown</strong>.</li>
</ol>
</li>
<li>Build a non-identity <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">HTTP policy</a> to isolate websites in a remote browser.</li>
</ol>
