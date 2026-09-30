---
cp9:
  canonical: https://developers.cloudflare.com/email-security/reporting/siem-integration/logscale-integration-guide/
  description: Falcon LogScale integration guide
  full_title: LogScale · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>LogScale · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Falcon LogScale integration guide"><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/reporting/siem-integration/logscale-integration-guide/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/reporting/siem-integration/logscale-integration-guide/index.md"><meta property="og:title" content="LogScale · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Falcon LogScale integration guide"><meta property="og:url" content="https://developers.cloudflare.com/email-security/reporting/siem-integration/logscale-integration-guide/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/reporting/siem-integration/logscale-integration-guide/
  schema: 1
---
<p>When Email security detects a <span class="nb-glossary-tooltip" title="phishing">phishing</span> email, the metadata of the detection can be sent directly to Falcon LogScale. For this tutorial, you will need a working Falcon LogScale account. You will also need to create a new Ingest Token in your LogScale account. Ingest Tokens identify repositories and are used to configure data ingestion to your repository. Refer to <a href="https://library.humio.com/falcon-logscale-cloud/ingesting-data-tokens.html">Falcon LogScale documentation</a> for more information.</p>
<p>After creating your Ingest Token:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Email Configuration</strong> &gt; <strong>Domains &amp; Routing</strong> &gt; <strong>Alert Webhooks</strong>.</li>
<li>Select <strong>New Webhook</strong>.</li>
<li>In <strong>App Type</strong>, select <strong>SIEM</strong>.</li>
<li>Choose <em>Crowdstrike</em> from the dropdown, and paste your Ingest Token into the <strong>Auth Code</strong> section.</li>
<li>In <strong>Target</strong>, paste the URL <code>https://cloud.community.humio.com/api/v1/ingest/hec/raw</code>.</li>
<li>Select <strong>Publish Webhook</strong>.</li>
</ol>
