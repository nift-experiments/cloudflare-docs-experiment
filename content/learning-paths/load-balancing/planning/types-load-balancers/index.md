---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/load-balancing/planning/types-load-balancers/
  description: Compare Layer 7, DNS-only, and Layer 4 balancing.
  full_title: Types of load balancers · Cloudflare Learning Paths
  head_html: <title>Types of load balancers · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Compare Layer 7, DNS-only, and Layer 4 balancing."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/load-balancing/planning/types-load-balancers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/load-balancing/planning/types-load-balancers/index.md"><meta property="og:title" content="Types of load balancers · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Compare Layer 7, DNS-only, and Layer 4 balancing."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/load-balancing/planning/types-load-balancers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/load-balancing/planning/types-load-balancers/#page","headline":"Types of load balancers \u00b7 Cloudflare Learning Paths","description":"Compare Layer 7, DNS-only, and Layer 4 balancing.","url":"https://developers.cloudflare.com/learning-paths/load-balancing/planning/types-load-balancers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/load-balancing/planning/types-load-balancers/
  schema: 1
---
<p>With Cloudflare, you can choose between three types of load balancers:</p>
<ul>
<li><a href="#layer-7-load-balancing">Layer 7 (HTTP/HTTPS)</a> (most common)</li>
<li><a href="#dns-only-load-balancing">DNS-only</a></li>
<li><a href="#layer-4-load-balancing">Layer 4 (TCP)</a></li>
</ul>
<hr />
<h2 id="layer-7-load-balancing">Layer 7 load balancing</h2>
<p>Layer 7 load balancers direct traffic to specific endpoints based on information present in each HTTP/HTTPS request (HTTP headers, URI, cookies, type of data, etc.).</p>
<p>When a client visits your application, Cloudflare directs their request to a healthy endpoint (determined by your <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">traffic steering policy</a> and <a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/#weights">endpoint weights</a>).</p>
<p>Cloudflare performs layer 7 load balancing when traffic to your hostname is <strong>proxied</strong> through Cloudflare. In the <strong>Load Balancing</strong> dashboard, these load balancers are marked with an orange cloud.</p>
<p><img src="/assets/upstream/images/load-balancing/proxied-load-balancer.png" alt="DNS-only load balancers are marked with an orange cloud" /></p>
<aside class="nb-aside warning">
@markup("md", "content/.markup/bodies/9816.md")
</aside>
<h3 id="benefits">Benefits</h3>
<p>In comparison to DNS-only load balancing, layer 7 load balancing:</p>
<ul>
<li>Protects endpoints from DDoS attacks by hiding their IP addresses.</li>
<li>Offers faster failover and more accurate routing, which can otherwise be affected by DNS caching.</li>
<li>Integrates with other Cloudflare features such as caching, Workers, and the WAF.</li>
<li>Reduces authoritative queries against Cloudflare, which can potentially save money for customers with usage-based billing.</li>
<li>Supports customized <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a> and <a href="/load-balancing/understand-basics/session-affinity/#endpoint-drain">endpoint drain</a>.</li>
<li>More accurately geo-locates traffic, using the data center associated with the user making the request instead of the data center associated with a user's recursive resolver.</li>
<li>Supports private IP addresses with <a href="/load-balancing/private-network/">Private Network Load Balancing</a>.</li>
</ul>
<hr />
<h2 id="dns-only-load-balancing">DNS-only load balancing</h2>
<p>DNS-only load balancers route traffic by returning specific IP addresses in response to a client's DNS query.</p>
<p>When a client visits your application, Cloudflare provides the address for a healthy endpoint (determined by your <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">traffic steering policy</a> and <a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/">endpoint-level steering policy</a>). However, Cloudflare relies on DNS resolvers respecting the short TTL to re-query Cloudflare's DNS for an updated list of healthy addresses. If a client has a cached DNS response, they will go to their previous destination, potentially ignoring your load balancer.</p>
<p>Cloudflare performs DNS-only load balancing when traffic to your hostname is <strong>not proxied</strong> through Cloudflare. In the <strong>Load Balancing</strong> dashboard, these load balancers are marked with a gray cloud.</p>
<p><img src="/assets/upstream/images/load-balancing/dns-only-load-balancer.png" alt="DNS-only load balancers are marked with a gray cloud" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9815.md")
</aside>
<h3 id="benefits-1">Benefits</h3>
<p>If your load balancer is attached to a hostname used for an <a href="/load-balancing/additional-options/additional-dns-records/"><code>MX</code> or <code>SRV</code> record</a> — and not an <code>A</code>, <code>AAAA</code>, or <code>CNAME</code> record — its proxy mode should be <strong>DNS-only</strong>.
<br/></p>
<h3 id="limitations">Limitations</h3>
<p>In comparison to proxied, layer 7 load balancing, DNS-only load balancing:</p>
<ul>
<li>Does not hide the IP addresses of your endpoints, leaving them vulnerable to DDoS attacks.</li>
<li>Performs slower failover and less accurate routing, because it has to rely on DNS resolvers and cache settings.</li>
<li>Cannot integrate with other Cloudflare features such as caching, Workers, and the WAF.</li>
<li>Increases authoritative queries against Cloudflare, which can potentially cost more for customers with usage-based billing.</li>
<li>Does not support <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a>. Alternatively, you can use <a href="/load-balancing/additional-options/dns-persistence/">DNS persistence</a>.</li>
<li>Geo-locates traffic based on the data center associated with the ECS source address, if available. If not available, geo-locates based on a user's recursive resolver, which can sometimes cause issues with <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/dynamic-steering/">latency-based steering</a>.</li>
<li>Does not support <a href="/load-balancing/private-network/">Private Network Load Balancing</a>.</li>
</ul>
<hr />
<h2 id="layer-4-load-balancing">Layer 4 load balancing</h2>
<p>Layer 4 load balancers route traffic by forwarding traffic to certain ports or IP addresses.</p>
<p>Cloudflare currently only supports layer 4 load balancing as part of <a href="/spectrum/about/load-balancer/">Cloudflare Spectrum</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9814.md")
</aside>
