---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-02-27-radar-dns-insights/
  description: New updates and improvements at Cloudflare.
  full_title: DNS Insights in Cloudflare Radar · Changelog
  head_html: <title>DNS Insights in Cloudflare Radar · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-02-27-radar-dns-insights/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="DNS Insights in Cloudflare Radar · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-02-27-radar-dns-insights/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-27-radar-dns-insights/#page","headline":"DNS Insights in Cloudflare Radar \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-02-27-radar-dns-insights/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-02-27-radar-dns-insights/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 27, 2025</time><h2 id="post-title">DNS Insights in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> has expanded its DNS insights, providing visibility into aggregated traffic and usage trends observed by our <a href="/1.1.1.1/">1.1.1.1</a> DNS resolver.
In addition to global, location, and ASN traffic trends, we are also providing perspectives on protocol usage, query/response characteristics, and DNSSEC usage.</p>
<p>Previously limited to the <a href="/api/resources/radar/subresources/dns/subresources/top/"><code>top</code></a> locations and ASes endpoints, we have now introduced the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/dns/methods/timeseries/"><code>/dns/timeseries</code></a>: Retrieves DNS query volume over time.</li>
<li><a href="/api/resources/radar/subresources/dns/subresources/summary/"><code>/dns/summary/{dimension}</code></a>: Retrieves summaries of DNS query distribution across ten different dimensions.</li>
<li><a href="/api/resources/radar/subresources/dns/subresources/timeseries_groups/"><code>/dns/timeseries_groups/{dimension}</code></a>: Retrieves timeseries data for DNS query distribution across ten different dimensions.</li>
</ul>
<p>For the <code>summary</code> and <code>timeseries_groups</code> endpoints, the following dimensions are available, displaying the distribution of DNS queries based on:</p>
<ul>
<li><code>cache_hit</code>: Cache status (hit vs. miss).</li>
<li><code>dnsssec</code>: DNSSEC support status (secure, insecure, invalid or other).</li>
<li><code>dnsssec_aware</code>: DNSSEC client awareness (aware vs. not-aware).</li>
<li><code>dnsssec_e2e</code>: End-to-end security (secure vs. insecure).</li>
<li><code>ip_version</code>: IP version (IPv4 vs. IPv6).</li>
<li><code>matching_answer</code>: Matching answer status (match vs. no-match).</li>
<li><code>protocol</code>: Transport protocol (UDP, TLS, HTTPS or TCP).</li>
<li><code>query_type</code>: Query type (<code>A</code>, <code>AAAA</code>, <code>PTR</code>, etc.).</li>
<li><code>response_code</code>: Response code (<code>NOERROR</code>, <code>NXDOMAIN</code>, <code>REFUSED</code>, etc.).</li>
<li><code>response_ttl</code>: Response TTL.</li>
</ul>
<p>Learn more about the new Radar DNS insights in our <a href="https://blog.cloudflare.com/new-dns-section-on-cloudflare-radar/">blog post</a>, and check out the <a href="https://radar.cloudflare.com/dns">new Radar page</a>.</p>
</div></article></div>
