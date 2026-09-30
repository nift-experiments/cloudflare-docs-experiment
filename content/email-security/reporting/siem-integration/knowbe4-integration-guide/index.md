---
cp9:
  canonical: https://developers.cloudflare.com/email-security/reporting/siem-integration/knowbe4-integration-guide/
  description: KnowBe4 integration guide
  full_title: KnowBe4 · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>KnowBe4 · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="KnowBe4 integration guide"><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/reporting/siem-integration/knowbe4-integration-guide/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/reporting/siem-integration/knowbe4-integration-guide/index.md"><meta property="og:title" content="KnowBe4 · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="KnowBe4 integration guide"><meta property="og:url" content="https://developers.cloudflare.com/email-security/reporting/siem-integration/knowbe4-integration-guide/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/reporting/siem-integration/knowbe4-integration-guide/
  schema: 1
---
<p>When Email security detects a <span class="nb-glossary-tooltip" title="phishing">phishing</span> email, the metadata of the detection can be sent directly to KnowBe4. For this tutorial, you will need a working KnowBe4 account with the SecurityCoach add-on. You will also need to create an organization key to use in Email security. This organization key will let you integrate KnowBe4 with Email security. Refer to <a href="https://support.knowbe4.com/hc/articles/13129840202643">KnowBe4 documentation</a> for more information on this subject.</p>
<p>After creating your organization key and authorizing Email security:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Email Configuration</strong> &gt; <strong>Domains &amp; Routing</strong> &gt; <strong>Alert Webhooks</strong>.</li>
<li>Select <strong>New Webhook</strong>.</li>
<li>In <strong>App Type</strong>, select <strong>SIEM</strong>.</li>
<li>Choose <em>KnowBe4</em> from the dropdown, and paste your organization key into the <strong>Auth Code</strong> section.</li>
<li>In <strong>Target</strong>, paste the URL that suits your organization. KnowBe4 has different URLs for different regions:</li>
</ol>
<table>
<thead>
<tr>
<th>KnowBe4 instance</th>
<th>URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>United States</td>
<td><code>https://area1.vendor.training.knowbe4.com/v1</code></td>
</tr>
<tr>
<td>European Union</td>
<td><code>https://area1.vendor.eu.knowbe4.com/v1</code></td>
</tr>
<tr>
<td>Canada</td>
<td><code>https://area1.vendor.ca.knowbe4.com/v1</code></td>
</tr>
<tr>
<td>United Kingdom</td>
<td><code>https://area1.vendor.uk.knowbe4.com/v1</code></td>
</tr>
<tr>
<td>Germany</td>
<td><code>https://area1.vendor.da.knowbe4.com/v1</code></td>
</tr>
</tbody>
</table>
8. Select _Expanded_ from the drop-down menu for **Malicious Style**, **Suspicious Style**, and **Spoof Style**.
9. Select **Publish Webhook**.
