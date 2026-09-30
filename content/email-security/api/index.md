---
cp9:
  canonical: https://developers.cloudflare.com/email-security/api/
  description: Access Email Security phishing campaign rulesets and indicators through the API.
  full_title: API · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>API · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Access Email Security phishing campaign rulesets and indicators through the API."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/api/index.md"><meta property="og:title" content="API · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Access Email Security phishing campaign rulesets and indicators through the API."><meta property="og:url" content="https://developers.cloudflare.com/email-security/api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/api/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8481.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="access-to-area-1">Access to Area 1</h3>
@markup("md", "content/.markup/bodies/8480.md")
</aside>
<p>Email security offers Application Programming Interfaces (APIs) to expose our <span class="nb-glossary-tooltip" title="phishing">phishing</span> campaign rulesets. These APIs both aid research and provide a set of indicators to block using network security edge devices.</p>
<p>All API requests are initiated using normal HTTP requests (<code>GET</code>/<code>POST</code>/<code>DELETE</code>) and responses are returned in JSON. Authentication to the APIs uses HTTP Basic Authentication over HTTPS.</p>
<p>For more details, refer to our <a href="/email-security/static/api_documentation_1.38.1.pdf">API documentation (PDF)</a>.</p>
