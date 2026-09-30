---
cp9:
  canonical: https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/geographic-locations/
  description: BCC geographic endpoint locations available for Email Security Gmail integration.
  full_title: Geographic locations · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Geographic locations · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="BCC geographic endpoint locations available for Email Security Gmail integration."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/geographic-locations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/geographic-locations/index.md"><meta property="og:title" content="Geographic locations · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="BCC geographic endpoint locations available for Email Security Gmail integration."><meta property="og:url" content="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/geographic-locations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/deployment/api/setup/gsuite-bcc-setup/geographic-locations/
  schema: 1
---
<p>Select from the following BCC addresses to process email in the correct geographic location.</p>
<table>
<thead>
<tr>
<th>Host</th>
<th>Location</th>
<th>Note</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mxrecord.io</code></td>
<td>US</td>
<td>Best option to ensure all email traffic processing happens US data centers.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-eu-primary.mxrecord.io</code></td>
<td>EU</td>
<td>Best option to ensure all email traffic processing happens in Germany, with backup to US data centers.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-eu1.mxrecord.io</code></td>
<td>EU</td>
<td>Best option to ensure all email traffic processing happens within the EU without backup to US data centers.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-bom.mxrecord.mx</code></td>
<td>India</td>
<td>Best option to ensure all email traffic processing happens within India.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-india-primary.mxrecord.mx</code></td>
<td>India</td>
<td>Same as <code>mailstream-bom.mxrecord.mx</code>, with backup to US data centers.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-asia.mxrecord.mx</code></td>
<td>India</td>
<td>Best option to ensure all email traffic processing happens in India, with Australia data centers as backup.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-syd.area1.cloudflare.net</code></td>
<td>Australia / New Zealand</td>
<td>Best option to ensure all email traffic processing happens within Australia.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-australia.area1.cloudflare.net</code></td>
<td>Australia / New Zealand</td>
<td>Best option to ensure all email traffic processing happens in Australia, with India and US data centers as backup.</td>
</tr>
</tbody>
</table>
