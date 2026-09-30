---
cp9:
  canonical: https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/
  description: Configure Gmail BCC rules to route email copies to Email Security for phishing detection.
  full_title: Setup Gmail with Email security (formerly Area 1) · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Setup Gmail with Email security (formerly Area 1) · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Gmail BCC rules to route email copies to Email Security for phishing detection."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/index.md"><meta property="og:title" content="Setup Gmail with Email security (formerly Area 1) · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Gmail BCC rules to route email copies to Email Security for phishing detection."><meta property="og:url" content="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/deployment/api/setup/gsuite-bcc-setup/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8520.md")
</aside>
<p>For customers using Gmail, setting up Email security via BCC is quick and easy. All you need to do is create a content compliance filter to send emails to Email security through BCC. The following email flow shows how this works:</p>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/gmail/gmail-bcc-flow.png" alt="Email flow when setting up a phishing assessment risk for Gmail with Email security." /></p>
<p>To set up Gmail with Email security:</p>
<ol>
<li><a href="/email-security/deployment/api/setup/gsuite-bcc-setup/add-domain/">Find your BCC address and add a domain</a>.</li>
<li><a href="/email-security/deployment/api/setup/gsuite-bcc-setup/bcc-rules-to-area1/">Add BCC rules</a>.</li>
<li><a href="/email-security/deployment/api/setup/gsuite-bcc-setup/create-project-gcp/">Create a project on Google Cloud Console</a>.</li>
<li><a href="/email-security/deployment/api/setup/gsuite-bcc-setup/create-service-account/">Create a service account</a>.</li>
<li><a href="/email-security/deployment/api/setup/gsuite-bcc-setup/add-retraction/">Add retraction</a>.</li>
</ol>
