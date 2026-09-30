---
cp9:
  canonical: https://developers.cloudflare.com/magic-transit/network-health/
  description: Monitor Magic Transit tunnel and endpoint health.
  full_title: Network health · Cloudflare Magic Transit docs
  head_html: <title>Network health · Cloudflare Magic Transit docs</title><meta name="generator" content="Nift"><meta name="description" content="Monitor Magic Transit tunnel and endpoint health."><link rel="canonical" href="https://developers.cloudflare.com/magic-transit/network-health/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/magic-transit/network-health/index.md"><meta property="og:title" content="Network health · Cloudflare Magic Transit docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Monitor Magic Transit tunnel and endpoint health."><meta property="og:url" content="https://developers.cloudflare.com/magic-transit/network-health/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Magic Transit"><meta name="algolia_product_filter" content="Magic Transit"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Magic Transit"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/magic-transit/network-health/#page","headline":"Network health \u00b7 Cloudflare Magic Transit docs","description":"Monitor Magic Transit tunnel and endpoint health.","url":"https://developers.cloudflare.com/magic-transit/network-health/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /magic-transit/network-health/
  schema: 1
---
<p>Magic Transit uses health check probes to determine the status of tunnels. Cloudflare uses this information to steer traffic through the best available route and warn you about potential issues with a tunnel. Service-level indicators (SLIs) and service-level objectives (SLOs) combine to determine when Cloudflare sends you tunnel health alerts. Refer to <a href="/magic-transit/reference/how-cloudflare-calculates-tunnel-health-alerts/">How Cloudflare calculates tunnel health alerts</a> for more information about SLIs and SLOs.</p>
<p>There are two types of health checks available: endpoint and tunnel health checks.</p>
<ul>
<li>
<p>Endpoint health checks evaluate connectivity from Cloudflare distributed data centers to your origin network. Endpoint probes flow over available tunnels to provide a broad picture of Internet health and do not inform tunnel selection or steering logic.</p>
<p>Cloudflare global network servers issue endpoint health checks outside of customer network namespaces and typically target endpoints beyond the tunnel-terminating border router.</p>
<p>During onboarding, you specify IP addresses to configure endpoint health checks.</p>
</li>
<li>
<p>Tunnel health checks monitor the status of the tunnels that route traffic from Cloudflare to your origin network. Magic Transit relies on health checks to steer traffic to the best available routes.</p>
<p>During onboarding, you specify the tunnel endpoints or tunnel health check targets that the tunnel probes from Cloudflare's global network will monitor.</p>
<p>You can access tunnel health check results through the API. Cloudflare aggregates these results from individual health check results on Cloudflare servers.</p>
</li>
</ul>
<p>Refer to <a href="/magic-transit/reference/tunnel-health-checks/">Tunnel health checks</a> for a deep dive into the different types of health checks, what they do, and how they work.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10639.md")
</aside>
<p>Refer to the following pages for details on how to use the various network health checks available.</p>
<ul class="directory-listing"><li><a href="/magic-transit/network-health/run-endpoint-health-checks/">Run endpoint health checks (beta)</a></li><li><a href="/magic-transit/network-health/check-tunnel-health-dashboard/">Check tunnel health in the dashboard</a></li><li><a href="/magic-transit/network-health/update-tunnel-health-checks-frequency/">Update tunnel health checks frequency</a></li><li><a href="/magic-transit/network-health/configure-tunnel-health-alerts/">Configure tunnel health alerts</a></li><li><a href="/magic-transit/reference/how-cloudflare-calculates-tunnel-health-alerts/">How Cloudflare calculates tunnel health alerts</a></li></ul>
