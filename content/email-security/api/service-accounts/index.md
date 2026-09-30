---
cp9:
  canonical: https://developers.cloudflare.com/email-security/api/service-accounts/
  description: Create and manage API service account credentials for Email Security.
  full_title: Service accounts · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Service accounts · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and manage API service account credentials for Email Security."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/api/service-accounts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/api/service-accounts/index.md"><meta property="og:title" content="Service accounts · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and manage API service account credentials for Email Security."><meta property="og:url" content="https://developers.cloudflare.com/email-security/api/service-accounts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/api/service-accounts/
  schema: 1
---
<p>A <strong>service account</strong> allows admins to create and maintain API credentials separate from a single username and password combination. It also allows you to create and control additional API access for different use cases.</p>
<p>When you connect to the <a href="/email-security/api/">Email security (formerly Area 1) API</a>, the <strong>Public Key</strong> is used for the <em>username</em> and the <strong>Private Key</strong> for the <em>password</em>.</p>
<h2 id="create-service-account">Create service account</h2>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Service Accounts</strong>.</li>
<li>Select <strong>Add Service Account</strong>.</li>
<li>Add a <strong>Name</strong>.</li>
<li>Select <strong>Create Service Account</strong>.</li>
<li>You will see your account's <strong>Private Key</strong> in a pop-up message (which will never be displayed again) and <strong>Public Key</strong> in the list of service accounts. Make sure to copy both values and store in a secure location.</li>
</ol>
<hr />
<h2 id="rotate-private-key">Rotate private key</h2>
<p>If you lose your private key or need to rotate it for security reasons, you can generate a new private key:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Service Accounts</strong>.</li>
<li>On a specific account, select <strong>...</strong> &gt; <strong>Refresh key</strong>.</li>
</ol>
