---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/additional-options/cname-flattening/
  description: Choose whether a DNS-only load balancer returns the endpoint hostname as a CNAME, or resolves it to an A/AAAA record.
  full_title: CNAME flattening for endpoints · Cloudflare Load Balancing docs
  head_html: <title>CNAME flattening for endpoints · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Choose whether a DNS-only load balancer returns the endpoint hostname as a CNAME, or resolves it to an A/AAAA record."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/additional-options/cname-flattening/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/additional-options/cname-flattening/index.md"><meta property="og:title" content="CNAME flattening for endpoints · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Choose whether a DNS-only load balancer returns the endpoint hostname as a CNAME, or resolves it to an A/AAAA record."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/additional-options/cname-flattening/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/additional-options/cname-flattening/#page","headline":"CNAME flattening for endpoints \u00b7 Cloudflare Load Balancing docs","description":"Choose whether a DNS-only load balancer returns the endpoint hostname as a CNAME, or resolves it to an A/AAAA record.","url":"https://developers.cloudflare.com/load-balancing/additional-options/cname-flattening/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/additional-options/cname-flattening/
  schema: 1
---
<p>When a <a href="/load-balancing/understand-basics/proxy-modes/">DNS-only (gray-clouded)</a> load balancer selects an endpoint whose address is a hostname (for example <code>origin.example.com</code>), Cloudflare resolves that hostname to an IP address and returns an <code>A</code>/<code>AAAA</code> record to the client. This is <em>CNAME flattening</em>, and it matches how <a href="/dns/cname-flattening/">CNAME flattening works in Cloudflare DNS</a>.</p>
<p>Some use cases — such as third-party endpoints that perform their own DNS-based steering — require the load balancer to return the <code>CNAME</code> record itself instead of a resolved IP. The <code>flatten_cname</code> property on a pool endpoint lets you opt out of flattening on a per-endpoint basis.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10432.md")
</aside>
<h2 id="when-to-use-this">When to use this</h2>
<p>Turn <code>flatten_cname</code> off (<code>flatten_cname: false</code>) on an endpoint when:</p>
<ul>
<li>You want clients to receive a <code>CNAME</code> answer pointing at a third-party SaaS provider or cloud endpoint (for example <code>origin-b.example.com</code>).</li>
<li>The endpoint resolves to addresses that are dynamic, geo-aware, or client-aware downstream.</li>
<li>You are failing over between two hostname endpoints and want the client to resolve each provider's hostname directly.</li>
</ul>
<p>Leave <code>flatten_cname</code> on (<code>flatten_cname: true</code>, the default) for normal IP-based or hostname endpoints where you just want a fast <code>A</code>/<code>AAAA</code> answer.</p>
<h2 id="where-it-applies">Where it applies</h2>
<p><code>flatten_cname</code> only changes resolver output when all of the following are true:</p>
<table>
<thead>
<tr>
<th>Condition</th>
<th>Required value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Load balancer <a href="/load-balancing/understand-basics/proxy-modes/">proxy mode</a></td>
<td>DNS-only (gray-clouded). Proxied load balancers must return Cloudflare anycast IPs, so the setting is ignored.</td>
</tr>
<tr>
<td>Endpoint address</td>
<td>A hostname (CNAME target). For raw IPv4/IPv6 endpoint addresses the setting has no effect.</td>
</tr>
<tr>
<td>Load balancer hostname</td>
<td>Not the zone apex. <code>CNAME</code> records at a zone apex are not permitted, so the load balancer falls back to flattening at the apex.</td>
</tr>
<tr>
<td>The selected endpoint</td>
<td>Steering selected this specific endpoint. Setting <code>flatten_cname: false</code> on endpoint A has no effect when steering picks endpoint B in the same pool.</td>
</tr>
</tbody>
</table>
<p>If the selected endpoint has <code>flatten_cname: false</code> but any of the conditions in the preceding table is not met, the load balancer flattens the CNAME and returns <code>A</code>/<code>AAAA</code> records as if the toggle were on.</p>
<h2 id="configure-cname-flattening">Configure CNAME flattening</h2>
<p><code>flatten_cname</code> is configured per endpoint inside a pool, alongside <code>name</code>, <code>address</code>, <code>weight</code>, and other endpoint fields. You can set it in the Cloudflare dashboard, the API, or Terraform.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10437.md")
</div></div>
<h2 id="verify">Verify</h2>
<p>Query the load balancer hostname with <code>dig</code>:</p>
<pre tabindex="0"><code class="language-sh">dig lb.example.com A +short&#10;</code></pre>
<ul>
<li>If steering selected an endpoint where <code>flatten_cname</code> is <code>false</code>, the answer section contains a <code>CNAME</code> record pointing at the endpoint address (for example, <code>origin-a.example.com.</code>). The client (or its resolver) is responsible for resolving that <code>CNAME</code> further.</li>
<li>If steering selected an endpoint where <code>flatten_cname</code> is <code>true</code> (or an endpoint whose address is an IP), the answer contains the resolved <code>A</code>/<code>AAAA</code> records.</li>
</ul>
<p>Because the answer depends on which endpoint steering selects, repeated <code>dig</code> queries against the same load balancer can legitimately alternate between <code>CNAME</code> and <code>A</code>/<code>AAAA</code> answers when a pool mixes hostname endpoints with <code>flatten_cname: false</code> and IP endpoints.</p>
<h2 id="health-monitors">Health monitors</h2>
<p>Endpoint health monitors are unaffected by this setting. Cloudflare always resolves the endpoint hostname to an IP and probes the underlying service using an uncached DNS lookup. Turning off flattening only changes what is returned to the client at DNS query time — health status continues to reflect the real backend reachability.</p>
<h2 id="analytics">Analytics</h2>
<p>Per-endpoint request counts and steering decisions remain visible in <a href="/load-balancing/reference/load-balancing-analytics/">load balancing analytics</a>, keyed by endpoint name. This lets you track how traffic is distributed across <code>CNAME</code>-returning endpoints.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Proxied (orange-clouded) load balancers: <code>flatten_cname</code> is ignored. Proxied load balancers must resolve to Cloudflare anycast IPs to deliver Cloudflare's HTTP/HTTPS proxy features.</li>
<li>Zone apex load balancers: <code>flatten_cname</code> is ignored because <code>CNAME</code> records are not permitted at a zone apex.</li>
<li>IP endpoints: <code>flatten_cname</code> has no effect — there is no <code>CNAME</code> to flatten or return.</li>
<li>DNS resolver caching: As with any DNS-only load balancer, downstream resolvers may cache the returned record for the TTL. Clients that ignore TTLs may continue to use a previously cached <code>CNAME</code> or <code>A</code> answer.</li>
<li>Plan requirement: Available to Enterprise customers on the Load Balancing add-on.</li>
</ul>
<h2 id="related">Related</h2>
<ul>
<li><a href="/dns/cname-flattening/">DNS CNAME flattening</a> — the equivalent feature for non-load-balancer DNS records.</li>
<li><a href="/load-balancing/understand-basics/proxy-modes/">Proxy modes</a> — when to use DNS-only versus proxied load balancing.</li>
<li><a href="/load-balancing/load-balancers/common-configurations/">Common configurations</a> — patterns including active-active failover that benefit from CNAME-returning endpoints.</li>
</ul>
