---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/
  description: Configure the IPv4 range Gateway uses to assign initial resolved IPs for hostname-based traffic.
  full_title: Configure initial resolved IPs · Cloudflare One docs
  head_html: <title>Configure initial resolved IPs · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure the IPv4 range Gateway uses to assign initial resolved IPs for hostname-based traffic."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/index.md"><meta property="og:title" content="Configure initial resolved IPs · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure the IPv4 range Gateway uses to assign initial resolved IPs for hostname-based traffic."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/#page","headline":"Configure initial resolved IPs \u00b7 Cloudflare One docs","description":"Configure the IPv4 range Gateway uses to assign initial resolved IPs for hostname-based traffic.","url":"https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/routes/configure-initial-resolved-ips/
  schema: 1
---
<p><span class="nb-glossary-tooltip" title="initial resolved IP">Initial resolved IPs</span> (also called token IPs) are ephemeral addresses that Gateway assigns to DNS queries so it can associate hostname-based traffic with the correct policy or tunnel at the network layer, where hostname information is not usually available. Refer to <a href="/cloudflare-one/networks/routes/reserved-ips/#gateway-initial-resolved-ips">Gateway initial resolved IPs</a> for a list of features that depend on this range.</p>
<p>By default, initial resolved IPs are assigned from:</p>
<ul>
<li><strong>IPv4</strong>: <code>172.64.128.0/20</code></li>
<li><strong>IPv6</strong>: <code>2606:4700:0cf1:4000::/64</code></li>
</ul>
<p>This is the default range. You can <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">configure a custom initial resolved IP range</a> for IPv4 if it conflicts with your existing network.</p>
<p>The IPv6 range is not configurable.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5116.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>You have the <a href="/fundamentals/api/reference/permissions/">Cloudflare One Networks Write</a> permission (for API access), or dashboard access to <strong>Networking</strong> &gt; <strong>IP addresses</strong> &gt; <strong>Address space</strong> &gt; <strong>Custom IPs</strong>.</li>
<li>Your new range does not conflict with existing routes or other reserved <a href="/cloudflare-one/networks/routes/reserved-ips/">Cloudflare One subnets</a> in your account.</li>
</ul>
<h2 id="check-your-current-range">Check your current range</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5120.md")
</div></div>
<h2 id="update-your-range">Update your range</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5123.md")
</div></div>
<p>The new CIDR must not conflict with existing private routes or other reserved subnets in your account. If it does, the request fails and the response describes the conflicting route or subnet.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5115.md")
</aside>
<p>The default IPv4 range is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges">automatically routed through the Cloudflare One Client</a> and does not require any Split Tunnel configuration. If you configure a custom range, update your <a href="/cloudflare-one/networks/routes/reserved-ips/#split-tunnel-configuration">Split Tunnel configuration</a> so that traffic to the new range routes through the Cloudflare One Client, and remove the old range if it is no longer used by any other reserved IP purpose.</p>
<p>Initial resolved IPs have a TTL of approximately 10 minutes. DNS queries resolved before you change your range continue to use the previous range until that TTL expires. After that, new DNS queries receive an initial resolved IP from the new range.</p>
