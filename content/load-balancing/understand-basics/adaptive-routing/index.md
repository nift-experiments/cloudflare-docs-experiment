---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/understand-basics/adaptive-routing/
  description: Route traffic based on origin health and latency.
  full_title: Adaptive routing · Cloudflare Load Balancing docs
  head_html: <title>Adaptive routing · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Route traffic based on origin health and latency."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/understand-basics/adaptive-routing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/understand-basics/adaptive-routing/index.md"><meta property="og:title" content="Adaptive routing · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route traffic based on origin health and latency."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/understand-basics/adaptive-routing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/understand-basics/adaptive-routing/#page","headline":"Adaptive routing \u00b7 Cloudflare Load Balancing docs","description":"Route traffic based on origin health and latency.","url":"https://developers.cloudflare.com/load-balancing/understand-basics/adaptive-routing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/understand-basics/adaptive-routing/
  schema: 1
---
<p>Adaptive routing controls features that modify the routing of requests to pools and endpoints in response to dynamic conditions, such as during the interval between active health monitoring requests.
Zero-downtime failover will trigger a single retry only if there is another healthy endpoint in the pool and a <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/">521, 522, 523, 525 or 526 error code</a> is occurring. No other error codes will trigger a zero-downtime failover operation.</p>
<h2 id="failover-across-pools">Failover across pools</h2>
<p>When there are no healthy endpoints in the same pool, failover across pools extend the zero-downtime failover of requests to healthy endpoints in alternate pools according to the failover order defined by traffic and endpoint steering.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="geo-steering-limitation">Geo-steering limitation</h3>
@markup("md", "content/.markup/bodies/10328.md")
</aside>
<h3 id="enable-failover-across-pools">Enable failover across pools</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Load Balancing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Navigate to your Load Balancers and select <strong>Edit</strong>.</li>
<li>From <strong>Adaptive Routing</strong>, enable <strong>Failover across pools</strong>.</li>
</ol>
<h2 id="http-2-goaway-handling">HTTP/2 GOAWAY handling</h2>
<p>When an origin sends a GOAWAY frame, Cloudflare stops sending new requests on that connection but does not mark the endpoint as unhealthy. Safe-to-retry requests (typically GET) are automatically retried on a new connection. Non-idempotent requests (such as POST or PUT) may not be retried unless the request was not yet sent on the closing connection.</p>
