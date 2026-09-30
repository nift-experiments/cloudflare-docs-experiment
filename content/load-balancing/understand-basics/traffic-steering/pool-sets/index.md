---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/
  description: Use pool sets to define location-specific pools, steering policies, weights, and fallback behavior through the API.
  full_title: Pool sets · Cloudflare Load Balancing docs
  head_html: <title>Pool sets · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Use pool sets to define location-specific pools, steering policies, weights, and fallback behavior through the API."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/index.md"><meta property="og:title" content="Pool sets · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use pool sets to define location-specific pools, steering policies, weights, and fallback behavior through the API."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/#page","headline":"Pool sets \u00b7 Cloudflare Load Balancing docs","description":"Use pool sets to define location-specific pools, steering policies, weights, and fallback behavior through the API.","url":"https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/understand-basics/traffic-steering/pool-sets/
  schema: 1
---
<p>Pool sets allow you to combine geographic steering with other traffic steering policies. For example, you can apply Dynamic Latency steering within a specific region or country. For load balancers managed through the API, pool sets can replace Geo steering.</p>
<p>With pool sets you can:</p>
<ul>
<li>Apply any supported steering policy within a single location</li>
<li>Set pool weights that apply only to that location</li>
<li>Assign a fallback pool for that location instead of the global fallback pool</li>
<li>Return a fixed HTTP response for matched proxied traffic</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10449.md")
</aside>
<h2 id="how-pool-sets-are-evaluated">How pool sets are evaluated</h2>
<p>Pool sets are stored as an ordered array on the load balancer. Cloudflare evaluates them in array order and stops at the first pool set whose <code>match</code> succeeds. That pool set then supplies the pools, steering policy, weights, and fallback pool for the request.</p>
<p>A pool set matching a single data center does not automatically take priority over one matching a region. Order the array from most specific to least specific.</p>
<p>Place a default pool set last by setting <code>match.default</code> to <code>true</code>. The <code>default</code> match applies to every request. Since pool sets use first-match wins, this pool set handles requests that did not match an earlier pool set:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;pool_sets&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;sjc-only&quot;,&#10;			&quot;match&quot;: { &quot;topology&quot;: { &quot;pops&quot;: [&quot;SJC&quot;] } },&#10;			&quot;overrides&quot;: { &quot;pools&quot;: [&quot;17b5962d775c646f3f9725cbc7a53df4&quot;] }&#10;		},&#10;		{&#10;			&quot;name&quot;: &quot;default&quot;,&#10;			&quot;match&quot;: { &quot;default&quot;: true },&#10;			&quot;overrides&quot;: { &quot;pools&quot;: [&quot;ff02c959d17f7bb2b1184a202e3c0af7&quot;] }&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>A pool set with <code>disabled</code> set to <code>true</code> is skipped.</p>
<h2 id="match-conditions">Match conditions</h2>
<p>The <code>match</code> object decides which requests a pool set applies to. Set either <code>default</code> or <code>topology</code> — the two cannot be combined. A pool set with no <code>match</code> at all applies to every request.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>default</code></td>
<td>When <code>true</code>, matches every request. Cannot be combined with <code>topology</code>.</td>
</tr>
<tr>
<td><code>topology</code></td>
<td>Matches by location. Requires at least one of <code>pops</code>, <code>countries</code>, <code>regions</code>.</td>
</tr>
</tbody>
</table>
<h3 id="topology-matching">Topology matching</h3>
<p>Within <code>topology</code>, each field takes a list of location codes:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Values</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pops</code></td>
<td>Cloudflare data center codes, matched against the data center handling the request</td>
</tr>
<tr>
<td><code>countries</code></td>
<td>ISO 3166-1 alpha-2 country codes</td>
</tr>
<tr>
<td><code>regions</code></td>
<td>Cloudflare <a href="/load-balancing/reference/region-mapping-api/#list-of-load-balancer-regions">region codes</a>, such as <code>WNAM</code></td>
</tr>
</tbody>
</table>
<p>Entries within a single field are combined with OR. A request from Germany matches <code>&quot;countries&quot;: [&quot;FR&quot;, &quot;DE&quot;, &quot;GB&quot;]</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10448.md")
</aside>
<p>For example, this topology sets multiple values in all three fields:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;match&quot;: {&#10;		&quot;topology&quot;: {&#10;			&quot;pops&quot;: [&quot;SJC&quot;, &quot;IAD&quot;],&#10;			&quot;countries&quot;: [&quot;US&quot;, &quot;CA&quot;],&#10;			&quot;regions&quot;: [&quot;WNAM&quot;, &quot;ENAM&quot;]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>A request matches when its data center is <code>SJC</code> or <code>IAD</code>, its country is <code>US</code> or <code>CA</code>, <strong>and</strong> its region hierarchy includes <code>WNAM</code> or <code>ENAM</code>.</p>
<p>Set one field per <code>topology</code> unless you specifically want that AND behavior.</p>
<p>A <code>regions</code> entry matches if it appears anywhere in the request's region hierarchy, so a broader region code can match a request from a narrower one.</p>
<p>Country matching uses the location resolved for the request. When the client location cannot be resolved, country matching falls back to the country of the Cloudflare data center handling the request.</p>
<h2 id="overrides">Overrides</h2>
<p>The <code>overrides</code> object holds the routing behavior applied on a match. Its fields are optional, but a pool set without <code>fixed_response</code> must set <code>overrides.pools</code>.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pools</code></td>
<td>Pool IDs to route to. Replaces the load balancer's pool selection entirely for this request.</td>
</tr>
<tr>
<td><code>pool_weights</code></td>
<td>Per-pool weights, applied only within this pool set</td>
</tr>
<tr>
<td><code>pool_default_weight</code></td>
<td>Weight for any pool in <code>pools</code> without an entry in <code>pool_weights</code></td>
</tr>
<tr>
<td><code>fallback_pool</code></td>
<td>Pool of last resort for this pool set. When omitted, the load balancer's fallback pool is used.</td>
</tr>
<tr>
<td><code>steering_policy</code></td>
<td>Steering policy applied to <code>pools</code></td>
</tr>
</tbody>
</table>
<p><code>pools</code> is a flat list rather than a map of locations to pools. The matched pool set defines the whole set of candidate pools for the request.</p>
<h3 id="steering-policies-within-a-pool-set">Steering policies within a pool set</h3>
<p>These steering policies are supported within a pool set:</p>
<table>
<thead>
<tr>
<th>Policy</th>
<th>Behavior within the pool set</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>off</code></td>
<td>Use <code>pools</code> in failover order</td>
</tr>
<tr>
<td><code>random</code></td>
<td>Select a pool at random, honoring <code>pool_weights</code></td>
</tr>
<tr>
<td><code>dynamic_latency</code></td>
<td>Select the pool with the lowest round trip time</td>
</tr>
<tr>
<td><code>proximity</code></td>
<td>Select the pool closest to the request by latitude and longitude</td>
</tr>
<tr>
<td><code>least_outstanding_requests</code></td>
<td>Select a pool by weights and outstanding request counts</td>
</tr>
<tr>
<td><code>least_connections</code></td>
<td>Select a pool by weights and open connection counts</td>
</tr>
</tbody>
</table>
<p><code>pool_weights</code> and <code>pool_default_weight</code> apply to <code>random</code>, <code>least_outstanding_requests</code>, and <code>least_connections</code>. These weights are separate from the load balancer's <code>random_steering</code> weights, so each pool set can weight its pools independently.</p>
<p>Omitting <code>steering_policy</code> leaves the pool set using failover order.</p>
<h3 id="fixed-responses">Fixed responses</h3>
<p>For proxied zone load balancers, a pool set can return a <code>fixed_response</code> instead of using <code>overrides.pools</code>. Use this option to return an HTTP status or redirect for a matched location:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;pool_sets&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;redirect-region&quot;,&#10;			&quot;match&quot;: { &quot;topology&quot;: { &quot;countries&quot;: [&quot;US&quot;] } },&#10;			&quot;fixed_response&quot;: {&#10;				&quot;status_code&quot;: 302,&#10;				&quot;location&quot;: &quot;https://example.com/service-unavailable&quot;&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Do not use <code>fixed_response</code> with DNS-only load balancers. DNS responses cannot carry HTTP status, body, or redirect fields. A matching fixed response returns <code>NOERROR</code> with no records.</p>
<p>A pool set must specify either <code>overrides.pools</code> or <code>fixed_response</code>. A pool set with neither is rejected, because it would match traffic and then have nowhere to send it.</p>
<h2 id="relationship-to-other-steering-settings">Relationship to other steering settings</h2>
<p>Pool sets are independent of the standard steering fields. Adding pool sets does not read from or write to <code>default_pools</code>, <code>region_pools</code>, <code>country_pools</code>, <code>pop_pools</code>, <code>steering_policy</code>, <code>random_steering</code>, or <code>fallback_pool</code>, and configuring those fields does not create pool sets.</p>
<p>Because a matched pool set replaces pool selection for the request, the standard fields have no effect on requests that a pool set matches. Requests that match no pool set fall through to your standard steering configuration.</p>
<p><code>default_pools</code> remains required on every load balancer, even when you expect every request to match a pool set. It is the destination for requests that match no pool set.</p>
<h3 id="custom-rules">Custom rules</h3>
<p>Pool sets are evaluated before <a href="/load-balancing/additional-options/load-balancing-rules/">custom rules</a>. A matched pool set establishes the routing decision, and custom rules then apply their overrides on top of it.</p>
<p>A pool set that returns a <code>fixed_response</code> is the complete response, so custom rules are not evaluated for that request.</p>
<h2 id="dns-only-load-balancers">DNS-only load balancers</h2>
<p>Country matching depends on the top-level steering policy and <code>location_strategy</code>. With a configured strategy, Geo and Proximity steering can use EDNS Client Subnet (ECS), the resolver IP address, or the responding Cloudflare data center. Without a configured strategy, Proximity uses ECS when available, while Geo uses the responding data center. Other top-level policies use the responding data center.</p>
<p>A pool set applies <code>overrides.steering_policy</code> after evaluating its match. The override therefore cannot change the location used for country matching. For more information, refer to <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/#edns-client-subnet-ecs-support">EDNS Client Subnet (ECS) support</a>.</p>
<h2 id="limits">Limits</h2>
<p>Pool sets are subject to the following limits:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pool sets per load balancer</td>
<td>1,000</td>
</tr>
<tr>
<td>Characters in <code>name</code></td>
<td>200</td>
</tr>
<tr>
<td>Entries per <code>pops</code>, <code>countries</code>, or <code>regions</code> list</td>
<td>1,000</td>
</tr>
</tbody>
</table>
<p>Duplicate entries within a single <code>pops</code>, <code>countries</code>, or <code>regions</code> list are rejected.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10447.md")
</aside>
<h2 id="configure-pool-sets-via-the-api">Configure pool sets via the API</h2>
<p>Pool sets are managed through the <code>pool_sets</code> field on the <a href="/api/resources/load_balancers/methods/edit/">Update Load Balancer</a> endpoint. When you send a <code>PATCH</code> request:</p>
<ul>
<li>Omitting <code>pool_sets</code> leaves existing pool sets unchanged</li>
<li>Sending <code>&quot;pool_sets&quot;: []</code> removes all pool sets</li>
<li>Sending <code>&quot;pool_sets&quot;: null</code> makes no change</li>
</ul>
<h3 id="example-request">Example request</h3>
<p>Before using this example, create the referenced pools. Replace each example pool ID with an ID from your account.</p>
<p>This request splits Western North American traffic across two pools by weight and uses a regional fallback pool. It selects the lowest-latency pool for German traffic. A default pool set handles all remaining traffic. The load balancer uses a separate global fallback pool.</p>
<p>Send a <code>PATCH</code> request to <code>/zones/{zone_id}/load_balancers/{load_balancer_id}</code> with the following body:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;fallback_pool&quot;: &quot;6f1ed002ab5595859014ebf0951522d9&quot;,&#10;	&quot;pool_sets&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;wnam-active-active&quot;,&#10;			&quot;match&quot;: { &quot;topology&quot;: { &quot;regions&quot;: [&quot;WNAM&quot;] } },&#10;			&quot;overrides&quot;: {&#10;				&quot;pools&quot;: [&#10;					&quot;17b5962d775c646f3f9725cbc7a53df4&quot;,&#10;					&quot;9290f38c5d07c2e2f4df57b1f61d4196&quot;&#10;				],&#10;				&quot;pool_weights&quot;: {&#10;					&quot;17b5962d775c646f3f9725cbc7a53df4&quot;: 0.5,&#10;					&quot;9290f38c5d07c2e2f4df57b1f61d4196&quot;: 0.5&#10;				},&#10;				&quot;steering_policy&quot;: &quot;random&quot;,&#10;				&quot;fallback_pool&quot;: &quot;2a28d35d1c00f000540fe739a04b3230&quot;&#10;			}&#10;		},&#10;		{&#10;			&quot;name&quot;: &quot;de-lowest-latency&quot;,&#10;			&quot;match&quot;: { &quot;topology&quot;: { &quot;countries&quot;: [&quot;DE&quot;] } },&#10;			&quot;overrides&quot;: {&#10;				&quot;pools&quot;: [&#10;					&quot;0930eec54a4c7ae6616985b79f678210&quot;,&#10;					&quot;c8b4f5a6d7e84910a2b3c4d5e6f70819&quot;&#10;				],&#10;				&quot;steering_policy&quot;: &quot;dynamic_latency&quot;&#10;			}&#10;		},&#10;		{&#10;			&quot;name&quot;: &quot;default&quot;,&#10;			&quot;match&quot;: { &quot;default&quot;: true },&#10;			&quot;overrides&quot;: {&#10;				&quot;pools&quot;: [&quot;ff02c959d17f7bb2b1184a202e3c0af7&quot;],&#10;				&quot;steering_policy&quot;: &quot;off&quot;&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<h3 id="resulting-behavior">Resulting behavior</h3>
<p>After the request completes, the load balancer routes traffic with this configuration:</p>
<table>
<thead>
<tr>
<th>Order</th>
<th>Match</th>
<th>Pools</th>
<th>Steering policy</th>
<th>Fallback pool</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Western North America (<code>WNAM</code>)</td>
<td><code>17b5962d775c646f3f9725cbc7a53df4</code>, <code>9290f38c5d07c2e2f4df57b1f61d4196</code></td>
<td>Random, 50% each</td>
<td><code>2a28d35d1c00f000540fe739a04b3230</code></td>
</tr>
<tr>
<td>2</td>
<td>Germany (<code>DE</code>)</td>
<td><code>0930eec54a4c7ae6616985b79f678210</code>, <code>c8b4f5a6d7e84910a2b3c4d5e6f70819</code></td>
<td>Dynamic Latency</td>
<td>Global fallback</td>
</tr>
<tr>
<td>3</td>
<td>All remaining traffic</td>
<td><code>ff02c959d17f7bb2b1184a202e3c0af7</code></td>
<td>Failover order</td>
<td>Global fallback</td>
</tr>
</tbody>
</table>
<p>The global fallback pool is <code>6f1ed002ab5595859014ebf0951522d9</code>.</p>
<h2 id="validation-errors">Validation errors</h2>
<p>Invalid Pool Sets configurations return HTTP status <code>400</code> and API error code <code>1002</code>. The error message explains the problem and can include one of these identifiers:</p>
<table>
<thead>
<tr>
<th>Message identifier</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>POOL_SETS_TOO_LARGE</code></td>
<td>More than 1,000 pool sets on one load balancer</td>
</tr>
<tr>
<td><code>POOL_SET_NO_INTENT</code></td>
<td>A pool set specifies neither <code>overrides.pools</code> nor <code>fixed_response</code></td>
</tr>
<tr>
<td><code>POOL_SET_DEFAULT_WITH_MATCH</code></td>
<td>A <code>match</code> combines <code>default</code> with <code>topology</code></td>
</tr>
<tr>
<td><code>POOL_SET_EMPTY_TOPOLOGY</code></td>
<td>A <code>topology</code> sets none of <code>pops</code>, <code>countries</code>, or <code>regions</code></td>
</tr>
<tr>
<td><code>POOL_SET_TOPOLOGY_TOO_LARGE</code></td>
<td>A <code>topology</code> list exceeds 1,000 entries</td>
</tr>
<tr>
<td><code>POOL_SET_POP_ENTITLEMENT</code></td>
<td>The account is not entitled to data center steering</td>
</tr>
<tr>
<td><code>POOL_SET_REGION_ENTITLEMENT</code></td>
<td>The account is not entitled to region steering</td>
</tr>
<tr>
<td><code>POOL_SET_COUNTRY_ENTITLEMENT</code></td>
<td>The account is not entitled to country steering</td>
</tr>
</tbody>
</table>
