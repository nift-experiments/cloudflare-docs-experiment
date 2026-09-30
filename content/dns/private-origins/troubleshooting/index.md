---
cp9:
  canonical: https://developers.cloudflare.com/dns/private-origins/troubleshooting/
  description: Troubleshoot common private network routing and private origin issues.
  full_title: Troubleshooting · Cloudflare DNS docs
  head_html: <title>Troubleshooting · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot common private network routing and private origin issues."><link rel="canonical" href="https://developers.cloudflare.com/dns/private-origins/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/private-origins/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot common private network routing and private origin issues."><meta property="og:url" content="https://developers.cloudflare.com/dns/private-origins/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="DNS"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/private-origins/troubleshooting/#page","headline":"Troubleshooting \u00b7 Cloudflare DNS docs","description":"Troubleshoot common private network routing and private origin issues.","url":"https://developers.cloudflare.com/dns/private-origins/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /dns/private-origins/troubleshooting/
  schema: 1
---
<h2 id="error-1002-dns-points-to-prohibited-ip">Error 1002: DNS points to prohibited IP</h2>
<p>This error occurs when you proxy a private IP address without the necessary entitlement. Contact your account team to request access.</p>
<h2 id="setting-seems-off-but-traffic-routes-through-tunnel">Setting seems off but traffic routes through tunnel</h2>
<p>Check for other records on the same name.</p>
<p>Private network routing applies per name, not per record. If you have multiple <code>A</code> or <code>AAAA</code> records on the same name and at least one of them has private network routing enabled, all records on that name will use private network routing.</p>
<h2 id="traffic-not-reaching-origin">Traffic not reaching origin</h2>
<p>If traffic is not reaching your private origin:</p>
<ol>
<li>Verify your tunnel is active and healthy in the Cloudflare dashboard.</li>
<li>Confirm the origin IP is routable within your private network.</li>
<li>Check that <code>private_routing</code> is set to <code>true</code> on the DNS record.</li>
<li>Verify the record has proxy status enabled.</li>
</ol>
<h2 id="connection-timeouts-from-clients">Connection timeouts from clients</h2>
<p>Cloudflare Source IP is set to a public range. Set it to a private <code>/12</code>. Refer to <a href="/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/">Configure Cloudflare source IPs</a>.</p>
<h2 id="request-times-out-with-no-response-on-the-origin">Request times out with no response on the origin</h2>
<p>The network where your origin lives has no return route for the Cloudflare Source IP range. Add a route that sends that range back through the tunnel.</p>
<h2 id="tunnel-shows-ike-established-but-health-checks-fail">Tunnel shows IKE established but health checks fail</h2>
<p>ICMP is blocked on the path or the health check is misconfigured. Allow ICMP between the tunnel endpoints and confirm the health check direction is <code>bidirectional</code> and type is <code>reply</code>.</p>
<h2 id="traffic-tries-to-route-over-the-public-internet">Traffic tries to route over the public Internet</h2>
<p>The <strong>Use private network routing</strong> toggle is not turned on for the DNS record. Edit the record and turn the toggle on. Refer to <a href="/dns/private-origins/private-network-routing/">Private network routing</a> for dashboard and API steps.</p>
