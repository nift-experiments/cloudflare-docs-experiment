---
cp9:
  canonical: https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/stale-response/
  description: Fix stale DNS responses from upstream resolvers.
  full_title: Stale response for upstream DNS resolution · Cloudflare DNS docs
  head_html: <title>Stale response for upstream DNS resolution · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Fix stale DNS responses from upstream resolvers."><link rel="canonical" href="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/stale-response/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/stale-response/index.md"><meta property="og:title" content="Stale response for upstream DNS resolution · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Fix stale DNS responses from upstream resolvers."><meta property="og:url" content="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/stale-response/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/stale-response/#page","headline":"Stale response for upstream DNS resolution \u00b7 Cloudflare DNS docs","description":"Fix stale DNS responses from upstream resolvers.","url":"https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/stale-response/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/manage-dns-records/troubleshooting/stale-response/
  schema: 1
---
<p>In one of the scenarios below, you notice that stale DNS responses are used. Depending on the scenario and other aspects of your configuration, this can cause wrong content or no content to be returned.</p>
<ul>
<li>A <span class="nb-glossary-tooltip" title="proxy status">proxied</span> CNAME record (<a href="/dns/cname-flattening/">flattened by default</a>).</li>
<li>A DNS-only CNAME record that has flattening turned on. This can happen either via the specific record configuration or as a consequence of the <a href="/dns/cname-flattening/set-up-cname-flattening/">zone settings</a>.</li>
<li>A <a href="/workers/">Workers</a> script making a subrequest to an external hostname<sup><a href="#footnote-1">1</a></sup>.</li>
</ul>
<h2 id="cause">Cause</h2>
<p>In the event that an upstream DNS server takes too long to respond, or the upstream returns a SERVFAIL, Cloudflare will use the expired DNS response from the cache and then attempt to update that cache asynchronously.</p>
<h2 id="solutions">Solutions</h2>
<ul>
<li>
<p>If possible, temporarily replace the proxied CNAME with a proxied A record. This may not always be possible, especially if the upstream target is a load balancer or if it returns dynamic responses.</p>
</li>
<li>
<p>Report the issues to the zone owner or DNS provider for the upstream target that is unresponsive.</p>
</li>
<li>
<p>You can also raise the issue through the DNS Operations Analysis and Research Center (DNS OARC). Consider its <a href="https://www.dns-oarc.net/oarc/services/chat">chat platform</a> or <a href="https://www.dns-oarc.net/oarc/lists">email lists</a>.</p>
</li>
</ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">A hostname that is not using Cloudflare as its [authoritative DNS provider](/dns/concepts/#authoritative-dns).</li></ol></section>
