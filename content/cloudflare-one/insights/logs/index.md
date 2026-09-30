---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/logs/
  description: Logs resources and guides for Zero Trust analytics.
  full_title: Zero Trust logs · Cloudflare One docs
  head_html: <title>Zero Trust logs · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Logs resources and guides for Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/logs/index.md"><meta property="og:title" content="Zero Trust logs · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Logs resources and guides for Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/cloudflare-one/insights/logs/#page","headline":"Zero Trust logs \u00b7 Cloudflare One docs","description":"Logs resources and guides for Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/logs/
  schema: 1
---
<p>Review detailed logs for your Zero Trust organization.</p>
<ul class="directory-listing"><li><a href="/cloudflare-one/insights/logs/dashboard-logs/">Dashboard logs</a></li><li><a href="/cloudflare-one/insights/logs/logpush/">Logpush integration</a></li></ul>
<h2 id="log-retention">Log retention</h2>
<p>Cloudflare stores Zero Trust logs for different periods of time based on the service and plan type:</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Standard</th>
<th>Access</th>
<th>Gateway</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Admin logs</strong></td>
<td>18 months</td>
<td>18 months</td>
<td>18 months</td>
<td>18 months</td>
<td>18 months</td>
</tr>
<tr>
<td><strong>Access logs</strong></td>
<td>24 hours</td>
<td>30 days</td>
<td>30 days</td>
<td>24 hours</td>
<td>180 days</td>
</tr>
<tr>
<td><strong>DNS logs</strong></td>
<td>24 hours</td>
<td>30 days</td>
<td>24 hours</td>
<td>30 days</td>
<td>180 days<sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td><strong>Network logs</strong></td>
<td>24 hours</td>
<td>30 days</td>
<td>24 hours</td>
<td>30 days</td>
<td>30 days</td>
</tr>
<tr>
<td><strong>HTTP logs</strong></td>
<td>24 hours</td>
<td>30 days</td>
<td>24 hours</td>
<td>30 days</td>
<td>30 days</td>
</tr>
<tr>
<td><strong>DEX logs</strong></td>
<td>7 days</td>
<td>7 days</td>
<td>7 days</td>
<td>7 days</td>
<td>7 days</td>
</tr>
<tr>
<td><strong>Device posture logs</strong></td>
<td>30 days</td>
<td>30 days</td>
<td>30 days</td>
<td>30 days</td>
<td>30 days</td>
</tr>
</tbody>
</table>
<h2 id="log-explorer">Log Explorer <span class="nb-badge">Beta</span></h2>
<p>Log Explorer users can store Zero Trust logs directly within Cloudflare in an <a href="/r2/">R2 bucket</a> and access them with the dashboard or API. Log Explorer supports the following Zero Trust datasets:</p>
<ul>
<li><a href="/logs/logpush/logpush-job/datasets/account/access_requests/">Access requests</a> (<code>FROM access_requests</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/casb_findings/">CASB Findings</a> (<code>FROM casb_findings</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/device_posture_results/">Device posture results</a> (<code>FROM device_posture_results</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/">Gateway DNS</a> (<code>FROM gateway_dns</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/gateway_http/">Gateway HTTP</a> (<code>FROM gateway_http</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/gateway_network/">Gateway Network</a> (<code>FROM gateway_network</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a> (<code>FROM zero_trust_network_sessions</code>)</li>
</ul>
<p>For more information, refer to <a href="/log-explorer/">Log Explorer</a>.</p>
<h2 id="customer-metadata-boundary">Customer Metadata Boundary</h2>
<p>You can use Cloudflare Zero Trust with the Data Localization Suite to restrict data storage to a specific geographic region. For more information, refer to <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary</a>.</p>
<h2 id="data-privacy">Data privacy</h2>
<p>For more information on how we use this data, refer to our <a href="https://www.cloudflare.com/application/privacypolicy/">Privacy Policy</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Enterprise users on per query plans cannot store DNS logs via Cloudflare. You can still export logs via [Logpush](/cloudflare-one/insights/logs/logpush/). For more information, contact your account team.</li></ol></section>
