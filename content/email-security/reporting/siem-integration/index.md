---
cp9:
  canonical: https://developers.cloudflare.com/email-security/reporting/siem-integration/
  description: SIEM integrations allow you to view message-level information outside of the dashboard and create your own custom reports.
  full_title: SIEM integration · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>SIEM integration · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="SIEM integrations allow you to view message-level information outside of the dashboard and create your own custom reports."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/reporting/siem-integration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/reporting/siem-integration/index.md"><meta property="og:title" content="SIEM integration · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="SIEM integrations allow you to view message-level information outside of the dashboard and create your own custom reports."><meta property="og:url" content="https://developers.cloudflare.com/email-security/reporting/siem-integration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/reporting/siem-integration/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8575.md")
</aside>
<p>With a bit of configuration, you can also bring Email security (formerly Area 1) data into your <span class="nb-glossary-tooltip" title="SIEM">Security Information and Event Management (SIEM)</span> tools to view message-level information outside of the dashboard and create your own custom reports.</p>
<h2 id="connect-a-siem-tool">Connect a SIEM tool</h2>
<p>The following steps are required to connect your SIEM tool.</p>
<h3 id="1-set-up-your-siem-tool"><ol>
<li>Set up your SIEM tool</li>
</ol></h3>
<p>For help setting up the proper configuration in your SIEM tool, refer to the following guides:</p>
<ul class="directory-listing"><li><a href="/email-security/reporting/siem-integration/knowbe4-integration-guide/">KnowBe4</a></li><li><a href="/email-security/reporting/siem-integration/logscale-integration-guide/">LogScale</a></li><li><a href="/email-security/reporting/siem-integration/splunk-integration-guide/">Splunk</a></li><li><a href="/email-security/reporting/siem-integration/sumo-logic-integration-guide/">Sumo Logic</a></li></ul>
<h3 id="2-create-a-webhook"><ol start="2">
<li>Create a webhook</li>
</ol></h3>
<p>Refer to <a href="/email-security/email-configuration/domains-and-routing/alert-webhooks/">Alert webhooks</a> to learn how to create a webhook and send data into your SIEM tool.</p>
