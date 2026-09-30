---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/
  description: Use load balancing analytics to evaluate traffic flow, assess the health of endpoints, and review health changes over time.
  full_title: Load balancing analytics · Cloudflare Load Balancing docs
  head_html: <title>Load balancing analytics · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Use load balancing analytics to evaluate traffic flow, assess the health of endpoints, and review health changes over time."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/index.md"><meta property="og:title" content="Load balancing analytics · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use load balancing analytics to evaluate traffic flow, assess the health of endpoints, and review health changes over time."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Load Balancing"><meta name="pcx_tags" content="Analytics,GraphQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/#page","headline":"Load balancing analytics \u00b7 Cloudflare Load Balancing docs","description":"Use load balancing analytics to evaluate traffic flow, assess the health of endpoints, and review health changes over time.","url":"https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Analytics","GraphQL"]}</script>
  markdown: true
  noindex: false
  route: /load-balancing/reference/load-balancing-analytics/
  schema: 1
---
<p>Using load balancing analytics, you can:</p>
<ul>
<li>Evaluate traffic flow.</li>
<li>Assess the health status of endpoints in your pools.</li>
<li>Review changes in pools and pool health over time.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10332.md")
</aside>
<h2 id="dashboard-analytics">Dashboard Analytics</h2>
<h3 id="overview-metrics">Overview metrics</h3>
<p>To view <strong>Overview</strong> metrics for your load balancer, go to <strong>Traffic</strong> &gt; <strong>Load Balancing Analytics</strong>.</p>
<p>These metrics show the number of requests routed to specific pools within a load balancer, helping you:</p>
<ul>
<li>Evaluate the effects of adding or removing a pool.</li>
<li>Decide when to create new pools.</li>
<li>Plan for peak traffic demands and future infrastructure needs.</li>
</ul>
<p>Add additional filters for specific pools, times, regions, and endpoints.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10331.md")
</aside>
<h3 id="latency">Latency</h3>
<p><strong>Latency</strong> metrics show an interactive map, helping you identify regions with <strong>Unhealthy</strong> or <strong>Slow</strong> pools.</p>
<p>To view latency information for your load balancer, go to <strong>Traffic</strong> &gt; <strong>Load Balancing Analytics</strong> &gt; <strong>Latency</strong>.</p>
<h3 id="logs">Logs</h3>
<p><strong>Logs</strong> provide a history of all endpoint status changes and how they affect your load balancing pools. Load Balancing only logs events that represent a status change for an endpoint, from healthy to unhealthy or vice versa.</p>
<p>When a Monitor Group is attached to a pool, each logged health event includes the <code>monitors</code> field.
This field lists the individual monitors within the group and their results, making it easier to see which monitor contributed to a status change.</p>
<p>Example event (truncated):</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;id&quot;: &lt;id&gt;,&#10;	&quot;timestamp&quot;: &quot;2025-09-22 19:22:00&quot;,&#10;	&quot;pool&quot;: {&#10;		&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;		&quot;name&quot;: &quot;example-monitor-group-test-pool-us&quot;,&#10;		&quot;healthy&quot;: true,&#10;		&quot;changed&quot;: false,&#10;		&quot;minimum_origins&quot;: 1&#10;	},&#10;	&quot;origins&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;origin-a&quot;,&#10;			&quot;ip&quot;: &quot;192.0.2.10&quot;,&#10;			&quot;enabled&quot;: true,&#10;			&quot;healthy&quot;: true,&#10;			&quot;failure_reason&quot;: &quot;No failures&quot;,&#10;			&quot;response_code&quot;: 200,&#10;			&quot;monitors&quot;: [&#10;				{&#10;					&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;					&quot;healthy&quot;: true,&#10;					&quot;failure_reason&quot;: &quot;No failures&quot;,&#10;					&quot;response_code&quot;: 200,&#10;					&quot;must_be_healthy&quot;: true,&#10;					&quot;monitoring_only&quot;: false&#10;				},&#10;				{&#10;					&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;					&quot;healthy&quot;: true,&#10;					&quot;failure_reason&quot;: &quot;No failures&quot;,&#10;					&quot;response_code&quot;: 200,&#10;					&quot;must_be_healthy&quot;: true,&#10;					&quot;monitoring_only&quot;: false&#10;				},&#10;				{&#10;					&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;					&quot;healthy&quot;: false,&#10;					&quot;failure_reason&quot;: &quot;HTTP timeout occurred&quot;,&#10;					&quot;must_be_healthy&quot;: false,&#10;					&quot;monitoring_only&quot;: true&#10;				}&#10;			]&#10;		},&#10;		{&#10;			&quot;name&quot;: &quot;origin-b&quot;,&#10;			&quot;ip&quot;: &quot;198.51.100.25&quot;,&#10;			&quot;enabled&quot;: true,&#10;			&quot;healthy&quot;: false,&#10;			&quot;failure_reason&quot;: &quot;TCP connection failed&quot;,&#10;			&quot;changed&quot;: true,&#10;			&quot;monitors&quot;: [&#10;				{&#10;					&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;					&quot;healthy&quot;: false,&#10;					&quot;failure_reason&quot;: &quot;TCP connection failed&quot;,&#10;					&quot;must_be_healthy&quot;: true,&#10;					&quot;monitoring_only&quot;: false&#10;				},&#10;				{&#10;					&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;					&quot;healthy&quot;: true,&#10;					&quot;failure_reason&quot;: &quot;No failures&quot;,&#10;					&quot;response_code&quot;: 200,&#10;					&quot;must_be_healthy&quot;: true,&#10;					&quot;monitoring_only&quot;: false&#10;				},&#10;				{&#10;					&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;					&quot;healthy&quot;: false,&#10;					&quot;failure_reason&quot;: &quot;HTTP timeout occurred&quot;,&#10;					&quot;must_be_healthy&quot;: false,&#10;					&quot;monitoring_only&quot;: true&#10;				}&#10;			]&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>In this example:</p>
<ul>
<li>Each origin includes a <code>monitors</code> array listing all monitors within the attached group.</li>
<li>Fields such as <code>must_be_healthy</code> <code>and monitoring_only</code> indicate each monitor's role in determining the origin's overall health.</li>
<li>The <code>healthy</code> and <code>failure_reason</code> fields show which individual monitor checks succeeded or failed.</li>
</ul>
<p>To access logs in the dashboard, go to <strong>Traffic</strong> &gt; <strong>Load Balancing Analytics</strong>.</p>
<h2 id="graphql-analytics">GraphQL Analytics</h2>
<p>For more flexibility, get load balancing metrics directly from the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>.</p>
<p>Get started with a sample query:</p>
<details class="nb-details"><summary>Requests per pool</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10333.md")
</div></details>
<details class="nb-details"><summary>Requests per data center</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10334.md")
</div></details>
