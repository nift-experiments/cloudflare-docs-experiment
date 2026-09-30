---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/
  description: Push logs in near real-time to storage or SIEM.
  full_title: Logpush · Cloudflare Logs docs
  head_html: <title>Logpush · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Push logs in near real-time to storage or SIEM."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/index.md"><meta property="og:title" content="Logpush · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Push logs in near real-time to storage or SIEM."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/#page","headline":"Logpush \u00b7 Cloudflare Logs docs","description":"Push logs in near real-time to storage or SIEM.","url":"https://developers.cloudflare.com/logs/logpush/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/
  schema: 1
---
<p>Logpush delivers logs in batches as quickly as possible, with no minimum batch size, potentially delivering files more than once per minute. This capability enables Cloudflare to provide information almost in real time, in smaller file sizes.</p>
<p>The push frequency is automatic and cannot be adjusted—Cloudflare pushes logs in batches as soon as possible. However, users can configure the batch size <a href="/logs/logpush/logpush-job/api-configuration/#max-upload-parameters">using the API</a> for improved control in case the log destination has specific requirements.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important-limitation">Important limitation</h3>
@markup("md", "content/.markup/bodies/10475.md")
</aside>
<p>Logpush does not offer storage or search functionality for logs; its primary aim is to send logs as quickly as they arrive.</p>
<p>Cloudflare Logpush supports pushing logs to storage services, SIEMs, and log management providers via the Cloudflare dashboard or API.</p>
<p>Cloudflare aims to support additional services in the future. Interested in a particular service? Take this <a href="https://goo.gl/forms/0KpMfae63WMPjBmD2">survey</a>.</p>
<h2 id="estimating-log-volume">Estimating log volume</h2>
<p>Before setting up a Logpush job, you can estimate the total volume of data that will be pushed to your destination. The volume depends on your traffic, selected fields, and compression.</p>
<h3 id="quick-sizing-for-http-requests">Quick sizing for HTTP Requests</h3>
<p>A quick sizing estimate for an <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP Requests</a> dataset:</p>
<ul>
<li>~100–250 bytes per request (compressed, depending on fields selected)</li>
<li>1M requests/day → ~100–250 MB/day</li>
<li>30M requests/month → ~3–7.5 GB/month</li>
</ul>
<h3 id="daily-storage-by-traffic-volume">Daily storage by traffic volume</h3>
<ul>
<li>100k req/day → ~25–50 MB/day</li>
<li>1M req/day → ~250–500 MB/day</li>
<li>10M req/day → ~2.5–5 GB/day</li>
<li>100M req/day → ~25–50 GB/day</li>
</ul>
<p>These ranges reflect field selection, compression, and whether you include extra fields or <a href="/logs/logpush/logpush-job/custom-fields/">custom fields</a>. Other datasets (Firewall, Workers, Load Balancing) add volume separately.</p>
<p>For precise estimates, you can <a href="/logs/logpull/additional-details/#estimating-daily-data-volume">sample your logs via Logpull</a> using a 1-hour sample.</p>
<h2 id="limits">Limits</h2>
<p>There is currently a max limit of <strong>4 Logpush jobs per zone</strong>. Trying to create a job once the limit has been reached will result in an error message: <code>creating a new job is not allowed: exceeded max jobs allowed</code>.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10474.md")
</aside>
