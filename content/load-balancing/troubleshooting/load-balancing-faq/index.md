---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/troubleshooting/load-balancing-faq/
  description: Answers to common Load Balancing questions.
  full_title: FAQs · Cloudflare Load Balancing docs
  head_html: <title>FAQs · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Answers to common Load Balancing questions."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/troubleshooting/load-balancing-faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/troubleshooting/load-balancing-faq/index.md"><meta property="og:title" content="FAQs · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Answers to common Load Balancing questions."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/troubleshooting/load-balancing-faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/troubleshooting/load-balancing-faq/#page","headline":"FAQs \u00b7 Cloudflare Load Balancing docs","description":"Answers to common Load Balancing questions.","url":"https://developers.cloudflare.com/load-balancing/troubleshooting/load-balancing-faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/troubleshooting/load-balancing-faq/
  schema: 1
---
<h2 id="overview">Overview</h2>
<p>For more detailed information about Load Balancing — including how-to guides, tutorials, and other reference information — check out our <a href="/load-balancing/">product documentation</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10329.md")
</aside>
<hr />
<h2 id="why-is-my-origin-receiving-so-many-health-monitor-requests">Why is my origin receiving so many health monitor requests?</h2>
<p>This issue may be caused by a combination of two issues.</p>
<h3 id="multiple-health-monitor-regions">Multiple Health Monitor Regions</h3>
<p>When you <a href="/load-balancing/monitors/create-monitor/#create-a-monitor">attach a monitor to a pool</a>, you can specify the <strong>Health Monitor Regions</strong> that Cloudflare uses to monitor your endpoint health.</p>
<p>If you select multiple regions or choose <strong>All Data Centers (Enterprise Only)</strong>, you may <a href="/load-balancing/understand-basics/health-details/#how-an-endpoint-becomes-unhealthy">dramatically increase traffic</a> to that pool and its associated endpoints. Each region sends individual health monitor requests from 3 data centers. Using <strong>All Data Centers</strong> sends individual health monitor requests from all existing Cloudflare data centers (and that number of data centers is growing all the time).</p>
<p>To reduce traffic, reduce the number of selected regions or choose an option besides <strong>All Data Centers</strong>.</p>
<h3 id="low-intervals-for-health-monitor-requests">Low intervals for health monitor requests</h3>
<p>If you have a low interval for your health monitor requests, you may increase the traffic sent to your endpoints.</p>
<hr />
<h2 id="why-is-my-endpoint-or-pool-considered-unhealthy">Why is my endpoint or pool considered unhealthy?</h2>
<p>To learn more about how endpoints and pools become unhealthy, refer to <a href="/load-balancing/understand-basics/health-details">Endpoint and pool health</a>.</p>
<p>If you know that your endpoint is healthy but load balancing is reporting it as unhealthy, check the following settings on the <a href="/load-balancing/monitors">monitor</a>:</p>
<ul>
<li>Perform a <code>curl</code> request against the configured endpoint. Make sure the response you are seeing matches your settings for the monitor.</li>
<li>Ensure your firewall or web server does not block or rate limit <a href="/fundamentals/reference/cloudflare-site-crawling/#specific-products">our health monitors</a> and accepts requests from <a href="/fundamentals/concepts/cloudflare-ip-addresses/">Cloudflare IP addresses</a>.</li>
<li>If you are looking for a specific value in the <strong>Response Body</strong>, make sure that value is relatively static and within the first 10 KB of the HTML page.</li>
<li>If your endpoint responds with a <code>301</code> or <code>302</code> status code, make sure <strong>Follow Redirects</strong> is selected.</li>
<li>Try increasing the <strong>Timeout</strong> value.</li>
<li>Review the <strong>Host Header</strong> for the health monitor.</li>
<li>If you are using <a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pulls (mTLS)</a>, <a href="/argo-smart-routing/">Argo Smart Routing</a>, <a href="/ssl/client-certificates/byo-ca/">Bring your own CA (mTLS)</a>, <a href="/smart-shield/configuration/dedicated-egress-ips/">Dedicated CDN Egress IPs</a>, or require <a href="/speed/optimization/protocol/http2-to-origin/">HTTP/2 to Origin</a>, make sure that you entered a zone value for <strong>Simulate Zone</strong> corresponding to the zone with these features configured.</li>
</ul>
<hr />
<h2 id="why-does-my-load-balancer-route-traffic-to-a-secondary-pool-when-the-primary-pool-is-still-healthy">Why does my load balancer route traffic to a secondary pool when the primary pool is still healthy?</h2>
<p>You occasionally might see traffic routed away from a pool if a health monitor request fails from a specific data center (even if the endpoint is still healthy). That data center may direct a small number of requests to another pool that is considered healthy by that data center.</p>
<p>To learn more about how endpoints and pools become unhealthy, refer to <a href="/load-balancing/understand-basics/health-details">Endpoint and pool health</a>.</p>
<hr />
<h2 id="what-happens-when-a-pool-or-endpoint-becomes-unhealthy">What happens when a pool or endpoint becomes unhealthy?</h2>
<p>When a pool or endpoint becomes unhealthy, traffic may be rerouted to other healthy pools or endpoints based on your configuration. You might experience this behavior when using:</p>
<p>1 - Pools with <strong>All-Datacenters</strong> monitoring and the monitor fails in a specific data center. In this case, all traffic will be steered away from impacted endpoints in that datacenter until the monitor succeeds again. These instances are reflected in LB request analytics as steering away from an unhealthy endpoint or pool.</p>
<p>2 - Pools with FQDN endpoint addresses and the recursive DNS lookup fails in a specific data center. In this case, only requests for which the DNS request fails will be steered away from impacted endpoints. This could be sporadic, especially if upstream authoritative resolvers occasionally time out or fail, when the local DNS cache TTL expires and a remote lookup is required in the hot path. This also appears in LB request analytics as steering away from an unhealthy endpoint, and the resolved endpoint IP will be missing from the request log.</p>
<p>To avoid these scenarios:</p>
<p>1 - Do not use <strong>All-Datacenters</strong> monitoring.</p>
<p>2 - Use IP addresses for endpoint configurations. If that is not feasible, use domains for which Cloudflare is authoritative (primary or secondary).</p>
<p>To learn more about how endpoints and pools become unhealthy, refer to <a href="/load-balancing/understand-basics/health-details">Endpoint and pool health</a>.</p>
<hr />
<h2 id="what-is-the-difference-between-load-balancing-and-health-checks">What is the difference between Load Balancing and Health Checks?</h2>
<p><a href="/load-balancing/">Cloudflare Load Balancing</a> helps monitor endpoints health and — based on that and other information — route incoming requests accordingly. Individual endpoints have monitors attached, which issue monitor requests at regular intervals.</p>
<p><a href="/health-checks/">Cloudflare Health Checks</a> are identical to monitors within a load balancer, but only meant for probing server health (and not distributing traffic).</p>
<hr />
<h2 id="why-do-i-see-different-numbers-of-requests-in-load-balancing-analytics">Why do I see different numbers of requests in Load Balancing Analytics?</h2>
<p>You may see different numbers of requests when reviewing <a href="/load-balancing/reference/load-balancing-analytics/">Load Balancing Analytics</a>, especially when compared to other Cloudflare dashboards (Caching, etc.).</p>
<p>Load balancing <strong>requests</strong> are the number of uncached requests made by your load balancer. By default, Cloudflare caches resolved IP addresses for up to five seconds. This built-in caching is often the cause of an discrepancies.</p>
<hr />
<h2 id="i-m-seeing-a-specific-error-code-for-my-load-balancer-or-monitor">I'm seeing a specific error code for my load balancer or monitor.</h2>
<p>For a list of specific error codes and next steps, refer to <a href="/load-balancing/troubleshooting">Load Balancing Troubleshooting</a>.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/load-balancing/understand-basics/health-details">Endpoint and pool health</a></li>
<li><a href="/load-balancing/monitors">Monitors</a></li>
<li><a href="/load-balancing/reference/load-balancing-analytics/">Load Balancing Analytics</a></li>
</ul>
