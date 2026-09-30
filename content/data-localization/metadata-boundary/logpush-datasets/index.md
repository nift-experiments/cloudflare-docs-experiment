---
cp9:
  canonical: https://developers.cloudflare.com/data-localization/metadata-boundary/logpush-datasets/
  description: Logpush datasets that support Customer Metadata Boundary by region.
  full_title: Logpush datasets · Cloudflare Data Localization Suite docs
  head_html: <title>Logpush datasets · Cloudflare Data Localization Suite docs</title><meta name="generator" content="Nift"><meta name="description" content="Logpush datasets that support Customer Metadata Boundary by region."><link rel="canonical" href="https://developers.cloudflare.com/data-localization/metadata-boundary/logpush-datasets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/data-localization/metadata-boundary/logpush-datasets/index.md"><meta property="og:title" content="Logpush datasets · Cloudflare Data Localization Suite docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Logpush datasets that support Customer Metadata Boundary by region."><meta property="og:url" content="https://developers.cloudflare.com/data-localization/metadata-boundary/logpush-datasets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Data Localization Suite"><meta name="algolia_product_filter" content="Data Localization Suite"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Data Localization Suite"><meta name="pcx_tags" content="Logging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/data-localization/metadata-boundary/logpush-datasets/#page","headline":"Logpush datasets \u00b7 Cloudflare Data Localization Suite docs","description":"Logpush datasets that support Customer Metadata Boundary by region.","url":"https://developers.cloudflare.com/data-localization/metadata-boundary/logpush-datasets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Logging"]}</script>
  markdown: true
  noindex: false
  route: /data-localization/metadata-boundary/logpush-datasets/
  schema: 1
---
<p><a href="/logs/logpush/">Logpush</a> is a service that automatically streams your Cloudflare log data to a storage destination you control (such as a cloud storage bucket or SIEM).</p>
<p>The table below lists the Logpush <a href="/logs/logpush/logpush-job/datasets/">datasets</a> (categories of log data) that support zones or accounts with Customer Metadata Boundary (CMB) enabled.</p>
<ul>
<li><strong>Level</strong> — Whether this log type is collected per-zone (a single domain on your account) or per-account (across all domains).</li>
<li><strong>Respects CMB</strong> — Whether enabling CMB causes this dataset's logs to be stored only in your selected region. If ✅, logs are localized. If ✘, this dataset is not affected by CMB and may be stored outside your selected region.</li>
<li><strong>Available with US/EU CMB region</strong> — Whether you can receive this dataset when CMB is set to US or EU.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7428.md")
</aside>
<table>
<thead>
<tr>
<th>Dataset name</th>
<th>Level</th>
<th>Respects CMB</th>
<th>Available with US CMB region</th>
<th>Available with EU CMB region</th>
</tr>
</thead>
<tbody>
<tr>
<td>Access Requests</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>AI Gateway Events</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Audit Logs v1</td>
<td>Account</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>Audit Logs v2</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Browser Isolation User Actions</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>CASB Findings</td>
<td>Account</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>Client-side security (formerly Page Shield)</td>
<td>Zone</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>DEX Application Tests</td>
<td>Account</td>
<td>✅</td>
<td>✘</td>
<td>✅</td>
</tr>
<tr>
<td>DEX Device State Events</td>
<td>Account</td>
<td>✅</td>
<td>✘</td>
<td>✅</td>
</tr>
<tr>
<td>Device Posture Results</td>
<td>Account</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>DLP Forensic Copies</td>
<td>Account</td>
<td>N/A<sup><a href="#footnote-1">1</a></sup></td>
<td>✘</td>
<td>✘</td>
</tr>
<tr>
<td>DNS Firewall logs</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>DNS logs</td>
<td>Zone</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Email security Alerts</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Firewall events</td>
<td>Zone</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Gateway DNS</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Gateway HTTP</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Gateway Network</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>HTTP requests</td>
<td>Zone</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>IPSec Logs</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Magic IDS Detections</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>NEL reports</td>
<td>Zone</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>Network Analytics Logs</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Sinkhole Events</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Spectrum events</td>
<td>Zone</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>WARP Config Changes</td>
<td>Account</td>
<td>✅</td>
<td>✘</td>
<td>✅</td>
</tr>
<tr>
<td>WARP Toggle Changes</td>
<td>Account</td>
<td>✅</td>
<td>✘</td>
<td>✅</td>
</tr>
<tr>
<td>Workers Trace Events</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Zaraz Events</td>
<td>Zone</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Zero Trust Sessions</td>
<td>Account</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Customer Metadata Boundary does not apply in this case, as these logs are sent directly from the processing location to your configured destination.</li></ol></section>
