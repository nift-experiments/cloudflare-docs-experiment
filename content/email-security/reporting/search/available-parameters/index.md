---
cp9:
  canonical: https://developers.cloudflare.com/email-security/reporting/search/available-parameters/
  description: Search parameters available for querying Email security message detections, including sender, subject, and disposition fields.
  full_title: Available parameters · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Available parameters · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Search parameters available for querying Email security message detections, including sender, subject, and disposition fields."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/reporting/search/available-parameters/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/reporting/search/available-parameters/index.md"><meta property="og:title" content="Available parameters · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Search parameters available for querying Email security message detections, including sender, subject, and disposition fields."><meta property="og:url" content="https://developers.cloudflare.com/email-security/reporting/search/available-parameters/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/reporting/search/available-parameters/
  schema: 1
---
<p>You can pull information for a message in <a href="/email-security/reporting/search/">search detections</a> using the following parameters:</p>
<ul>
<li>From (<code>envelope_from</code>)</li>
<li>From Name</li>
<li>To (any) (<code>envelope_to</code>)</li>
<li>To Name (any)</li>
<li>Cc (any)</li>
<li>ReplyTo</li>
<li>Subject (any)</li>
<li>Sent DateTime (formatted as <code>YYYY-MM-DDTHH:MM:SS</code>)</li>
<li>Received DateTime (formatted as <code>YYYY-MM-DDTHH:MM:SS</code>)</li>
<li>final_disposition</li>
<li>alert_id</li>
<li>sha256 (attachments)</li>
<li>ssdeep (attachments)</li>
<li>name (attachments)</li>
<li>md5 (attachments)</li>
<li>Message-ID</li>
<li>smtp_helo_server_ip</li>
<li>smtp_previous_hop_ip</li>
<li>x_originating_ip</li>
<li>Reason(s) for Detection</li>
</ul>
<h2 id="search-terms">Search terms</h2>
<p>In addition to the message parameters above, you can use these additional detection search strings:</p>
<ul>
<li>phish_submission</li>
<li>phish_submission_response</li>
<li>user_submission</li>
<li>team_submission</li>
<li>auto-retraction</li>
<li>browser_isolation_rewrite</li>
</ul>
<p>For <span class="nb-glossary-tooltip" title="disposition">disposition</span>-specific submission searches, refer to <a href="https://horizon.area1security.com/support/service-addresses">Service Addresses</a> in the Email security dashboard.</p>
<h2 id="data-retention">Data retention</h2>
<p>For Email security Horizon Enterprise customers, detections search would index for a period of 12 months and rotate over to a rolling 12-month period.</p>
<p>For Email security Horizon Advantage customers, detections search would index for three months and rotate over to a rolling 3-month period.</p>
<h2 id="scope-of-data-retained">Scope of data retained</h2>
<p>For messages that are not detected, the body of the message itself is not retained. Only the metadata such as sender, recipient, subject, message_id, and delivery log will be retained. It is also possible to view the messages as the preview image.</p>
<p>For detections, full messages are retained, including attachments, in addition to the metadata described above. The raw message including attachments can be downloaded as an <code>.eml</code> file.</p>
