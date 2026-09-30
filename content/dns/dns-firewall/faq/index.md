---
cp9:
  canonical: https://developers.cloudflare.com/dns/dns-firewall/faq/
  description: Find answers to common questions about Cloudflare's DNS Firewall, including cache behavior, EDNS support, and setting PTR records.
  full_title: FAQs — DNS Firewall · Cloudflare DNS docs
  head_html: <title>FAQs — DNS Firewall · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Find answers to common questions about Cloudflare&#x27;s DNS Firewall, including cache behavior, EDNS support, and setting PTR records."><link rel="canonical" href="https://developers.cloudflare.com/dns/dns-firewall/faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/dns-firewall/faq/index.md"><meta property="og:title" content="FAQs — DNS Firewall · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Find answers to common questions about Cloudflare&#x27;s DNS Firewall, including cache behavior, EDNS support, and setting PTR records."><meta property="og:url" content="https://developers.cloudflare.com/dns/dns-firewall/faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="DNS Firewall"><meta name="pcx_tags" content="Caching"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/dns-firewall/faq/#page","headline":"FAQs \u2014 DNS Firewall \u00b7 Cloudflare DNS docs","description":"Find answers to common questions about Cloudflare's DNS Firewall, including cache behavior, EDNS support, and setting PTR records.","url":"https://developers.cloudflare.com/dns/dns-firewall/faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Caching"]}</script>
  markdown: true
  noindex: false
  route: /dns/dns-firewall/faq/
  schema: 1
---
<p>Consider the answers for frequently asked questions about Cloudflare DNS Firewall.</p>
<h2 id="how-does-dns-firewall-choose-a-backend-nameserver-to-query-upstream">How does DNS Firewall choose a backend nameserver to query upstream?</h2>
<p>DNS Firewall alternates between a customer's nameservers, using an algorithm that is more likely to send queries to the faster upstream nameservers than slower nameservers.</p>
<h2 id="how-long-does-dns-firewall-cache-a-stale-object">How long does DNS Firewall cache a stale object?</h2>
<p>DNS Firewall sets cache longevity according to allocated memory.</p>
<p>As long as there is enough allocated memory, Cloudflare does not clear items from the cache forcefully, even when the TTL expires. This feature allows Cloudflare to serve stale objects from cache if your nameservers are offline.</p>
<h2 id="does-the-dns-firewall-cache-servfail">Does the DNS Firewall cache SERVFAIL?</h2>
<p>Yes. <code>SERVFAIL</code> is treated like any other negative answer for caching purposes. The default TTL is 30 seconds. You can set a different negative cache TTL on your cluster in the Cloudflare dashboard, or via the <a href="/api/resources/dns_firewall/methods/edit/">API</a> (<code>negative_cache_ttl</code> parameter).</p>
<h2 id="does-dns-firewall-support-edns-client-subnet-ecs">Does DNS Firewall support EDNS Client Subnet (ECS)?</h2>
<p>Yes. Often, DNS providers want to see a client's IP via <span class="nb-glossary-tooltip" title="EDNS Client Subnet (ECS)">EDNS Client Subnet (ECS)</span> (<a href="https://www.rfc-editor.org/rfc/rfc7871.html">RFC 7871</a>) because they serve geographically specific DNS answers based on the client's IP. With EDNS Client Subnet enabled, the DNS Firewall will forward the client's IP subnet along with the DNS query to the upstream nameserver.</p>
<p>When EDNS is enabled, the DNS Firewall gives out the geographically correct answer in cache based on the client IP subnet. To do this, the DNS Firewall segments its cache. For example:</p>
<ol>
<li>A resolver says it is looking for an answer for client <code>192.0.2.0/24</code>.</li>
<li>The DNS Firewall will proxy the request to the upstream nameserver for the answer.</li>
<li>The DNS Firewall will cache the answer from the upstream nameserver, but only for that <code>/24</code>.</li>
<li><code>203.0.113.0/24</code> now asks the same DNS question and the answer is again returned from the upstream nameserver instead of the cache.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7703.md")
</aside>
<p>Some resolvers might not be sending any EDNS data. When you enable ECS fallback on your cluster in the Cloudflare dashboard — or set the <code>ecs_fallback</code> parameter to <code>true</code> via the <a href="/api/resources/dns_firewall/methods/edit/">API</a> — DNS Firewall will forward the IP subnet of the resolver instead, only if there is no EDNS data present in the incoming DNS query.</p>
<h2 id="does-dns-firewall-cache-negative-answers">Does DNS Firewall cache negative answers?</h2>
<p>Yes. The default TTL is 30 seconds. You can configure the negative cache TTL on your cluster in the Cloudflare dashboard, or via the <a href="/api/resources/dns_firewall/methods/edit/">API</a> (<code>negative_cache_ttl</code> parameter). This will affect the TTL of responses with status <code>REFUSED</code>, <code>NXDOMAIN</code>, or <code>SERVFAIL</code>.</p>
<h2 id="how-can-i-set-ptr-records-for-nameserver-hostnames">How can I set PTR records for nameserver hostnames?</h2>
<p>To set up PTR records for the DNS Firewall cluster IPs that point to your nameserver hostnames, use the following API endpoints:</p>
<ul>
<li><a href="/api/resources/dns_firewall/subresources/reverse_dns/methods/get/">Show DNS Firewall Cluster Reverse DNS</a></li>
<li><a href="/api/resources/dns_firewall/subresources/reverse_dns/methods/edit/">Update DNS Firewall Cluster Reverse DNS</a></li>
</ul>
