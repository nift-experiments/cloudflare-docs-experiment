---
cp9:
  canonical: https://developers.cloudflare.com/email-security/deployment/api/setup/
  description: Connect your mail environment to Email Security using API deployment setup guides.
  full_title: Setup - API deployment · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Setup - API deployment · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect your mail environment to Email Security using API deployment setup guides."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/deployment/api/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/deployment/api/setup/index.md"><meta property="og:title" content="Setup - API deployment · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect your mail environment to Email Security using API deployment setup guides."><meta property="og:url" content="https://developers.cloudflare.com/email-security/deployment/api/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/deployment/api/setup/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8515.md")
</aside>
<p>When you first get started with Email security (formerly Area 1), you will need to set up a way to connect your current mail environment with Email security.</p>
<h2 id="bcc-setup">BCC setup</h2>
<p>Send messages to Email security via BCC configurations within your email provider:</p>
<ul>
<li><a href="/email-security/deployment/api/setup/gsuite-bcc-setup/">Google Workspace BCC setup</a></li>
<li><a href="/email-security/deployment/api/setup/exchange-bcc-setup/">Microsoft Exchange BCC setup</a></li>
</ul>
<h2 id="journaling-setup">Journaling setup</h2>
<p>Send messages to Email security via a Journaling configuration within your email provider:</p>
<ul>
<li><a href="/email-security/deployment/api/setup/office365-journaling/">Office 365 journaling setup</a></li>
</ul>
<h2 id="microsoft-graph-api">Microsoft Graph API</h2>
<p>Send messages to Email security via a Microsoft Graph API configuration within your email provider:</p>
<ul>
<li><a href="/email-security/deployment/api/setup/office365-graph-api/">Office 365 Microsoft Graph API setup</a></li>
</ul>
<h2 id="next-steps">Next steps</h2>
<p>Regardless of your setup (BCC, journaling or MS Graph API), you may also want to set up either manual or automatic <a href="/email-security/email-configuration/retract-settings/">retraction</a> to take post-delivery actions against suspicious messages.</p>
