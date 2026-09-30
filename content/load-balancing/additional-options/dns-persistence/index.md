---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/additional-options/dns-persistence/
  description: Maintain consistent DNS responses for load balanced hostnames.
  full_title: DNS persistence · Cloudflare Load Balancing docs
  head_html: <title>DNS persistence · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Maintain consistent DNS responses for load balanced hostnames."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/additional-options/dns-persistence/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/additional-options/dns-persistence/index.md"><meta property="og:title" content="DNS persistence · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Maintain consistent DNS responses for load balanced hostnames."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/additional-options/dns-persistence/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/additional-options/dns-persistence/#page","headline":"DNS persistence \u00b7 Cloudflare Load Balancing docs","description":"Maintain consistent DNS responses for load balanced hostnames.","url":"https://developers.cloudflare.com/load-balancing/additional-options/dns-persistence/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/additional-options/dns-persistence/
  schema: 1
---
<p>This guide explains how to achieve DNS persistence when using Cloudflare Load Balancing, similar to functionality provided by traditional DNS-based load balancers.</p>
<p>DNS persistence ensures that subsequent DNS requests from the same local DNS server receive the same IP address. This is useful for applications that require session consistency, such as VPN connections or authentication systems.</p>
<p>Cloudflare Load Balancing can achieve DNS persistence using different configuration approaches for DNS-only load balancing.</p>
<hr />
<h2 id="dns-only-load-balancing-persistence">DNS-only load balancing persistence</h2>
<p>For DNS-only load balancing, Cloudflare offers three methods to achieve DNS persistence:</p>
<h3 id="method-1-geo-steering-based-on-pop-location-recommended">Method 1: Geo-steering based on PoP location (Recommended)</h3>
<p>This method uses geographic steering based on the Cloudflare Point of Presence (PoP) that receives the DNS request.</p>
<h4 id="configuration-steps">Configuration steps</h4>
<ol>
<li>Create a pool for each endpoint. Do not apply load shedding to either pool.</li>
<li>Create a DNS-only load balancer and add both pools. Ensure <code>pool_1</code> is ordered before <code>pool_2</code>.</li>
<li>Under <strong>Traffic Steering</strong>, select <strong>Geo Steering</strong>.</li>
<li>Create a geo-steering rule for a region (for example, <strong>Eastern North America</strong>) and select the same pools but in reverse order (<code>pool_2</code> first, then <code>pool_1</code>).</li>
<li>Use <strong>Never prefer ECS</strong> and <strong>PoP location</strong> to determine the source of the request.</li>
</ol>
<h4 id="how-it-works">How it works</h4>
<p>All requests received at Cloudflare PoPs in the specified region are sent to one endpoint, while requests from other regions are sent to the other endpoint.</p>
<h4 id="why-this-is-recommended">Why this is recommended</h4>
<p>Using the Cloudflare PoP that received the request as criteria for steering is more stable than IP hashing or splitting IP space, as it is not affected by recursive DNS providers using different egress IPs.</p>
<h3 id="method-2-load-shedding-with-ip-hash">Method 2: Load shedding with IP hash</h3>
<p>This method uses load shedding to distribute traffic based on the source IP address of the recursive DNS resolver.</p>
<h4 id="configuration-steps-1">Configuration steps</h4>
<ol>
<li>Create a pool for each endpoint (for example, <code>pool_1</code> with <code>endpoint_1</code> and <code>pool_2</code> with <code>endpoint_2</code>).</li>
<li>On the first pool, select <strong>Hash</strong> under <strong>Endpoint Steering</strong>.</li>
<li>Configure <strong>Load Shedding</strong>:
<ul>
<li><strong>Policy</strong>: IP Hash</li>
<li><strong>Shed %</strong>: 50% (to split traffic evenly between two pools)</li>
</ul>
</li>
<li>Create a DNS-only load balancer and add both pools. Ensure <code>pool_1</code> is ordered before <code>pool_2</code>.</li>
<li>Do not configure additional traffic steering or rules.</li>
</ol>
<h4 id="how-it-works-1">How it works</h4>
<p>This configuration sheds half of the requests to the second pool using an IP hash and respects session affinity per source IP of the recursive resolver.</p>
<h4 id="limitations">Limitations</h4>
<p>Some recursive DNS providers (like Google DNS 8.8.8.8 or Quad9 9.9.9.9) may use different egress IPs randomly, which can reduce persistence stability.</p>
<h3 id="method-3-custom-rules-with-ip-source-filtering">Method 3: Custom rules with IP source filtering</h3>
<p>This method uses custom rules to split traffic based on IP address ranges.</p>
<h4 id="configuration-steps-2">Configuration steps</h4>
<ol>
<li>Create a pool for each endpoint. Do not apply load shedding to either pool.</li>
<li>Create a DNS-only load balancer and add both pools. Ensure <code>pool_1</code> is ordered before <code>pool_2</code>.</li>
<li>Do not configure traffic steering.</li>
<li>Create a <strong>Custom Rule</strong> with:
<ul>
<li><strong>Field</strong>: IP Source Address</li>
<li><strong>Operator</strong>: is in</li>
<li><strong>Value</strong>: A subset of IP space (for example, <code>0.0.0.0/1</code> for the lower half of IPv4 space)</li>
</ul>
</li>
<li>For the rule action, choose <strong>Override</strong> &gt; <strong>Endpoints</strong> and set the pools in reverse order (<code>pool_2</code>, <code>pool_1</code>).</li>
</ol>
<h4 id="how-it-works-2">How it works</h4>
<p>Traffic with source IPs in the lower half of IPv4 space is sent to one endpoint, while traffic in the upper half is sent to the other endpoint.</p>
<h4 id="limitations-1">Limitations</h4>
<p>Similar to Method 2, this approach may be less stable with recursive DNS providers that use varying egress IPs.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/load-balancing/understand-basics/session-affinity/">Session Affinity</a></li>
<li><a href="/load-balancing/additional-options/load-shedding/">Load Shedding</a></li>
<li><a href="/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/">Geo Steering</a></li>
<li><a href="/load-balancing/additional-options/load-balancing-rules/">Custom Rules</a></li>
</ul>
