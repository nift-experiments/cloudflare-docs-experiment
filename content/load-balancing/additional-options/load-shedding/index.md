---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/additional-options/load-shedding/
  description: Use load shedding to prevent an at-risk endpoint from becoming unhealthy and starting the failover process.
  full_title: Load shedding · Cloudflare Load Balancing docs
  head_html: <title>Load shedding · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Use load shedding to prevent an at-risk endpoint from becoming unhealthy and starting the failover process."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/additional-options/load-shedding/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/additional-options/load-shedding/index.md"><meta property="og:title" content="Load shedding · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use load shedding to prevent an at-risk endpoint from becoming unhealthy and starting the failover process."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/additional-options/load-shedding/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/additional-options/load-shedding/#page","headline":"Load shedding \u00b7 Cloudflare Load Balancing docs","description":"Use load shedding to prevent an at-risk endpoint from becoming unhealthy and starting the failover process.","url":"https://developers.cloudflare.com/load-balancing/additional-options/load-shedding/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/additional-options/load-shedding/
  schema: 1
---
<p>Use load shedding to prevent an at-risk endpoint from <a href="/load-balancing/understand-basics/health-details/">becoming unhealthy</a> and starting the failover process.</p>
<p>Once you configure load shedding on a pool, that pool will begin diverting traffic to other pools according to your load shedding settings and the load balancer's <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">steering policy</a>.</p>
<h2 id="step-1-identify-at-risk-endpoints">Step 1 — Identify at-risk endpoints</h2>
<p>Using your internal metrics, identify endpoints at risk of reaching their failure threshold.</p>
<ul>
<li>If your endpoint is seeing increased traffic but is not yet at risk of failure, start with <a href="#step-2--shed-default-traffic-from-a-pool">Step 2</a>.</li>
<li>If your endpoint is about to fail, start with <a href="#step-4--shed-additional-traffic-optional">Step 4</a>.</li>
</ul>
<h2 id="step-2-shed-default-traffic-from-a-pool">Step 2 — Shed default traffic from a pool</h2>
<p>Once you have identified an at-risk endpoint, shed a small amount of <strong>Default</strong> traffic from that endpoint's pool. This traffic is not affiliated with existing <a href="/load-balancing/understand-basics/session-affinity/">Session affinity</a> sessions.</p>
<p>Configure load shedding via the <a href="#configure-via-dashboard">dashboard</a> or the <a href="#configure-via-api">API</a>.</p>
<h3 id="configure-via-dashboard">Configure via dashboard</h3>
<p>To enable load shedding for a specific pool via the dashboard:</p>
<ol>
<li>Go to <strong>Load Balancing</strong>.</li>
<li>Select the <strong>Pools</strong> tab.</li>
<li>On a pool, select <strong>Edit</strong>.</li>
<li>Open the <strong>Configure Load Shedding</strong> dropdown.</li>
<li>For <strong>Default traffic</strong>, select a <strong>Policy</strong> and a <strong>Shed %</strong>:</li>
</ol>
<details class="nb-details"><summary>Policy options</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10429.md")
</div></details>
<details class="nb-details"><summary>Shed %</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10430.md")
</div></details>
<h3 id="configure-via-api">Configure via API</h3>
<p>To enable load shedding for a specific pool via the API, <a href="/api/resources/load_balancers/subresources/pools/methods/update/">update the values</a> for the pool's <code>load_shedding</code> object.</p>
<details class="nb-details"><summary>Example request</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10431.md")
</div></details>
<p>For more guidance on choosing a shedding policy, see <a href="#shedding-policies">Shedding policies</a>.</p>
<h2 id="step-3-monitor-traffic">Step 3 — Monitor traffic</h2>
<p>Once you have started shedding default traffic, evaluate the effects by reviewing the <a href="/load-balancing/reference/load-balancing-analytics/"><strong>Overview</strong> metrics</a> in Load Balancing analytics. Based on these numbers and your internal metrics, you will know whether you need to divert additional traffic from the pool.</p>
<p>If you see increased traffic to a pool, you may need to shed additional traffic. Pools shed a percentage of total traffic, so any increase in total traffic will also increase the traffic reaching your pool.</p>
<h2 id="step-4-shed-additional-traffic-optional">Step 4 — Shed additional traffic (optional)</h2>
<p>If you need to shed additional pool traffic:</p>
<ol>
<li>Follow the steps outlined in <a href="#step-2--shed-default-traffic-from-a-pool">Step 2</a>.
<ul>
<li>In the dashboard, increase the <strong>Shed %</strong> for <strong>Default traffic</strong> and/or <strong>Session affinity traffic</strong>.</li>
<li>For the API, increase the value for <code>default_percent</code> and/or <code>session_percent</code>.</li>
</ul>
</li>
</ol>
<p>Since shedding <strong>Session Affinity traffic</strong> will disrupt <a href="/load-balancing/understand-basics/session-affinity/">existing sessions</a> and may degrade the customer experience, only enable this option if your pool is in imminent danger of becoming unhealthy or your pool has a high percentage of traffic related to existing sessions. For more guidance, see <a href="#shedding-policies">Shedding policies</a>.</p>
<h2 id="step-5-disable-load-shedding">Step 5 — Disable load shedding</h2>
<p>Once an endpoint is no longer at risk, remove load shedding from the pool.</p>
<p>To remove load shedding in the dashboard, perform the same steps as <a href="#configure-via-dashboard">Configure load shedding via the dashboard</a> but set the <strong>Shed %</strong> to <code>0</code> for both <strong>Default traffic</strong> and <strong>Session affinity traffic</strong>.</p>
<p>To remove load shedding via the API, perform the same steps as <a href="#configure-via-api">Configure load shedding via the API</a> but set the <code>load_shedding</code> object to <code>null</code>.</p>
<h2 id="additional-notes">Additional notes</h2>
<h3 id="shedding-policies">Shedding policies</h3>
<p>For <strong>Default traffic</strong>, you have two choices for shedding policy.</p>
<p>A <em>Random</em> policy:</p>
<ul>
<li>Randomly sheds the percentage of requests specified in the <em>Shed %</em>.</li>
<li>Distributes traffic more accurately because it sheds at the request level.</li>
<li>May cause requests from the same IP to hit different endpoints, potentially leading to cache misses, inconsistent latency, or session disruption for <a href="/load-balancing/understand-basics/proxy-modes/#dns-only-load-balancing">DNS-only load balancers</a>.</li>
</ul>
<p>An <em>IP hash</em> policy:</p>
<ul>
<li>Sheds the percentage of IP address hash space specified in the <em>Shed %</em>.</li>
<li>Ensures requests from the same IP will hit the same endpoint, which will increase cache hits, provide consistent latency, and preserve sessions.</li>
<li>Can over- or under-shed requests, since hashing does not guarantee a perfectly even IP distribution and individual IPs may be responsible for different percentages of your requests.</li>
</ul>
<p>Choose a <em>Random</em> policy when you want a more accurate distribution of raw requests and an <em>IP hash</em> policy when you want to prevent a single IP from flapping between different endpoints.</p>
<p>For <strong>Session Affinity traffic</strong>, you can only use an <em>IP hash</em> policy since these requests relate to existing sessions. Only increase the <em>Shed %</em> if you are comfortable disrupting <a href="/load-balancing/understand-basics/session-affinity/">existing sessions</a>.</p>
<h3 id="fallback-pools">Fallback pools</h3>
<p>If all pools within a load balancer have <em>Load shedding</em> enabled, some traffic will go to the fallback pool. To prevent any traffic from reaching the fallback pool, ensure at least one pool within the load balancer <strong>does not</strong> have load shedding enabled.</p>
<h3 id="pools-in-multiple-load-balancers">Pools in multiple load balancers</h3>
<p>If you enable load shedding on a pool, it will shed the same percentage of traffic across all your load balancers. If you need an endpoint to shed different percentages of traffic for different load balancers, put that endpoint in multiple pools.</p>
