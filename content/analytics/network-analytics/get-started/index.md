---
cp9:
  canonical: https://developers.cloudflare.com/analytics/network-analytics/get-started/
  description: Learn how to view and use data from Network Analytics.
  full_title: Get started with Network Analytics · Cloudflare Analytics docs
  head_html: <title>Get started with Network Analytics · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to view and use data from Network Analytics."><link rel="canonical" href="https://developers.cloudflare.com/analytics/network-analytics/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/network-analytics/get-started/index.md"><meta property="og:title" content="Get started with Network Analytics · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to view and use data from Network Analytics."><meta property="og:url" content="https://developers.cloudflare.com/analytics/network-analytics/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/network-analytics/get-started/#page","headline":"Get started with Network Analytics \u00b7 Cloudflare Analytics docs","description":"Learn how to view and use data from Network Analytics.","url":"https://developers.cloudflare.com/analytics/network-analytics/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/network-analytics/get-started/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="requirements">Requirements</h3>
@markup("md", "content/.markup/bodies/3127.md")
</aside>
<h2 id="view-the-network-analytics-dashboard">View the Network Analytics dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Network Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select an account that has access to Magic Transit or Spectrum.</li>
<li>Configure the displayed data. You can <a href="/analytics/network-analytics/configure/time-range/">adjust the time range</a>, <a href="/analytics/network-analytics/configure/displayed-data/#select-high-level-metric">select the main metric</a> (total packets or total bytes), <a href="/analytics/network-analytics/configure/displayed-data/#apply-filters">apply filters</a>, and more.</li>
</ol>
<h2 id="get-network-analytics-data-via-api">Get Network Analytics data via API</h2>
<p>Use the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> to query data using the available <a href="/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/">Network Analytics nodes</a>.</p>
<h2 id="send-network-analytics-logs-to-a-third-party-service">Send Network Analytics logs to a third-party service</h2>
<p><a href="/logs/logpush/logpush-job/enable-destinations/">Create a Logpush job</a> that sends Network analytics logs to your storage service, <span class="nb-glossary-tooltip" title="SIEM">SIEM solution</span>, or log management provider.</p>
<h2 id="limitations">Limitations</h2>
<p>Users with the <code>Analytics</code> role will have visibility to IDs but will not see the following on the Network Analytics dashboard:</p>
<ul>
<li>Tunnel names</li>
<li>Prefix names</li>
<li><a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> rules</li>
<li><a href="/ddos-protection/managed-rulesets/">DDoS managed rulesets</a></li>
<li>Override names</li>
</ul>
