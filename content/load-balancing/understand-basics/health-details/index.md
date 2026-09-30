---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/understand-basics/health-details/
  description: How endpoints and pools become unhealthy.
  full_title: How endpoints and pools become unhealthy · Cloudflare Load Balancing docs
  head_html: <title>How endpoints and pools become unhealthy · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="How endpoints and pools become unhealthy."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/understand-basics/health-details/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/understand-basics/health-details/index.md"><meta property="og:title" content="How endpoints and pools become unhealthy · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How endpoints and pools become unhealthy."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/understand-basics/health-details/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/understand-basics/health-details/#page","headline":"How endpoints and pools become unhealthy \u00b7 Cloudflare Load Balancing docs","description":"How endpoints and pools become unhealthy.","url":"https://developers.cloudflare.com/load-balancing/understand-basics/health-details/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/understand-basics/health-details/
  schema: 1
---
<p>When we talk about dynamic load balancing, that means your load balancer only directs requests to endpoints that can handle the traffic.</p>
<p>But how does your load balancer <em>know</em> which endpoints can handle the traffic? We determine that through a system of monitors, health monitors, and pools.</p>
<hr />
<h2 id="dynamic-load-balancing">Dynamic load balancing</h2>
<p>Dynamic load balancing happens through a combination of <span class="nb-glossary-tooltip" title="pool">pools</span>, <span class="nb-glossary-tooltip" title="monitor">monitors</span>, and <span class="nb-glossary-tooltip" title="health check">health checks</span>.</p>
<pre tabindex="0"><code class="language-mermaid">    flowchart RL&#10;      accTitle: Load balancing monitor flow&#10;      accDescr: Monitors issue health monitor requests, which validate the current status of servers within each pool.&#10;      Monitor -- Health Monitor ----&gt; Endpoint2&#10;      Endpoint2 -- Response ----&gt; Monitor&#10;      subgraph Pool&#10;      Endpoint1((Endpoint 1))&#10;      Endpoint2((Endpoint 2))&#10;      end&#10;</code></pre>
<hr />
<h2 id="how-an-endpoint-becomes-unhealthy">How an endpoint becomes unhealthy</h2>
<div class="nb-glossary-definition"><p>Health checks are requests issued by a monitor at regular interval and — depending on the monitor settings — return a <strong>pass</strong> or <strong>fail</strong> value to make sure an endpoint is still able to receive traffic.</p>
<p>Each health monitor request is trying to answer two questions:</p>
<ol>
<li><strong>Is the endpoint offline?</strong>: Does the endpoint respond to the health monitor request at all? If so, does it respond quickly enough (as specified in the monitor's <strong>Timeout</strong> field)?</li>
<li><strong>Is the endpoint working as expected?</strong>: Does the endpoint respond with the expected HTTP response codes? Does it include specific information in the response body?</li>
</ol>
<p>If the answer to either of these questions is &quot;No&quot;, then the endpoint fails the health monitor request.</p></div>
<p>For each option selected in a pool's <strong>Health Monitor Regions</strong>, Cloudflare sends health monitor requests from three separate data centers in that region.</p>
<p><img src="/assets/upstream/images/load-balancing/health-check-component.png" alt="Health monitor requests come from three data centers within each selected region." /></p>
<p>If the majority of data centers for that region pass the health monitor requests, that region is considered healthy. If the majority of regions is healthy, then the endpoint itself will be considered healthy.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10324.md")
</aside>
<p>Load balancing analytics and logs will only show global health changes.</p>
<p>For greater accuracy and consistency when changing endpoint health status, you can also set the <code>consecutive_up</code> and <code>consecutive_down</code> parameters via the <a href="/api/resources/load_balancers/subresources/monitors/methods/create/">Create Monitor API endpoint</a>. To change from healthy to unhealthy, an endpoint will have to be marked healthy a consecutive number of times (specified by <code>consecutive_down</code>). The same applies — from unhealthy to healthy — for <code>consecutive_up</code>.</p>
<hr />
<h2 id="how-a-pool-becomes-unhealthy">How a pool becomes unhealthy</h2>
<p>When an <a href="#how-an-endpoint-becomes-unhealthy">individual endpoint becomes unhealthy</a>, that may affect the health status of any associated pools (visible in the dashboard):</p>
<ul>
<li><strong>Healthy</strong>: All endpoints are healthy.</li>
<li><strong>Degraded</strong>: At least one endpoint is unhealthy, but the pool is still considered healthy and could be receiving traffic.</li>
<li><strong>Critical</strong>: The pool has fallen below the number of available endpoints specified in its <strong>Health Threshold</strong> and will not receive traffic from your load balancer (unless other pools are also unhealthy and this pool is marked as the <a href="#fallback-pools"><strong>Fallback Pool</strong></a>).</li>
<li><strong>Health unknown</strong>: There are either no monitors attached to pool endpoints or the monitors have not yet determined endpoint health.</li>
<li><strong>No health</strong>: Reserved for your load balancer's <a href="#fallback-pools"><strong>Fallback Pool</strong></a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10323.md")
</aside>
<h3 id="traffic-distribution">Traffic distribution</h3>
<p>When a pool reaches <strong>Critical</strong> health, your load balancer will begin diverting traffic according to its <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">Traffic steering policy</a>:</p>
<ul>
<li>
<p><strong>Off</strong>:</p>
<ul>
<li>If the active pool becomes unhealthy, traffic goes to the next pool in order.</li>
<li>If an inactive pool becomes unhealthy, traffic continues to go to the active pool (but would skip over the unhealthy pool in the failover order).</li>
</ul>
</li>
<li>
<p><strong>All other methods</strong>: Traffic is distributed across all remaining pools according to the traffic steering policy.</p>
</li>
</ul>
<h3 id="fallback-pools">Fallback pools</h3>
<p>This pool is meant to be the pool of last resort, meaning that its health is not taken into account when directing traffic.</p>
<p>Fallback pools are important because traffic still might be coming to your load balancer even when all the pools are unreachable (disabled or unhealthy). Your load balancer needs somewhere to route this traffic, so it will send it to the fallback pool.</p>
<hr />
<h2 id="how-a-load-balancer-becomes-unhealthy">How a load balancer becomes unhealthy</h2>
<p>When one or more pools become unhealthy, your load balancer might also show a different status in the dashboard:</p>
<ul>
<li><strong>Healthy</strong>: All pools are healthy.</li>
<li><strong>Degraded</strong>: At least one pool is unhealthy, but traffic is not yet going to the <a href="#fallback-pools">Fallback Pool</a>.</li>
<li><strong>Critical</strong>: All pools are unhealthy and traffic is going to the <a href="#fallback-pools">Fallback Pool</a>.</li>
</ul>
<p>If a load balancer reaches <strong>Critical</strong> health and the pool serving as your fallback pool is also disabled:</p>
<ul>
<li>If Cloudflare proxies your hostname, you will see a 530 HTTP/1016 Origin DNS failure.</li>
<li>If Cloudflare does not proxy your hostname, you will see the SOA record.</li>
</ul>
