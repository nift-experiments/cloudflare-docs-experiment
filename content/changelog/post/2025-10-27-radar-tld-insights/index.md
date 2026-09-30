---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-10-27-radar-tld-insights/
  description: New updates and improvements at Cloudflare.
  full_title: TLD Insights in Cloudflare Radar · Changelog
  head_html: <title>TLD Insights in Cloudflare Radar · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-10-27-radar-tld-insights/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="TLD Insights in Cloudflare Radar · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-10-27-radar-tld-insights/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-27-radar-tld-insights/#page","headline":"TLD Insights in Cloudflare Radar \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-10-27-radar-tld-insights/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-10-27-radar-tld-insights/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 27, 2025</time><h2 id="post-title">TLD Insights in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now introduces Top-Level Domain (TLD) insights, providing visibility into popularity based on the DNS magnitude metric, detailed TLD information including its type, manager, DNSSEC support, RDAP support, and WHOIS data, and trends such as DNS query volume and geographic distribution observed by the <a href="/1.1.1.1/">1.1.1.1</a> DNS resolver.</p>
<p>The following dimensions were added to the Radar DNS API, specifically, to the <a href="/api/resources/radar/subresources/dns/methods/summary_v2/"><code>/dns/summary/{dimension}</code></a> and <a href="/api/resources/radar/subresources/dns/methods/timeseries_groups_v2/"><code>/dns/timeseries_groups/{dimension}</code></a> endpoints:</p>
<ul>
<li><code>tld</code>: Top-level domain extracted from DNS queries; can also be used as a filter.</li>
<li><code>tld_dns_magnitude</code>: Top-level domain ranking by <a href="/radar/glossary#dns-magnitude">DNS magnitude</a>.</li>
</ul>
<p>And the following endpoints were added:</p>
<ul>
<li><a href="/api/resources/radar/subresources/tlds/methods/list/"><code>/tlds</code></a> - Lists all TLDs.</li>
<li><a href="/api/resources/radar/subresources/tlds/methods/get/"><code>/tlds/{tld}</code></a> - Retrieves information about a specific TLD.</li>
</ul>
<p><img src="/assets/upstream/images/radar/tld-ranking-by-dns-magnitude.png" alt="Screenshot of the TLD ranking by DNS magnitude" /></p>
<p>Learn more about the new Radar DNS insights in our <a href="https://blog.cloudflare.com/introducing-tld-insights-on-cloudflare-radar/">blog post</a>, and check out the <a href="https://radar.cloudflare.com/tlds">new Radar page</a>.</p>
</div></article></div>
