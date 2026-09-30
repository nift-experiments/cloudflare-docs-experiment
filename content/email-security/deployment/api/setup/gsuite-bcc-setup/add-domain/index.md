---
cp9:
  canonical: https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/add-domain/
  description: Locate your Email Security BCC address and add your domain for Gmail integration.
  full_title: Find BCC address and add domain · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Find BCC address and add domain · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Locate your Email Security BCC address and add your domain for Gmail integration."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/add-domain/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/add-domain/index.md"><meta property="og:title" content="Find BCC address and add domain · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Locate your Email Security BCC address and add your domain for Gmail integration."><meta property="og:url" content="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/add-domain/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/deployment/api/setup/gsuite-bcc-setup/add-domain/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8521.md")
</aside>
<p>To set up Email security (formerly Area 1) for Gmail:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security (formerly Area 1) dashboard</a>.</li>
<li>Select the question mark, where you will be able to find your BCC address.</li>
<li>Once you found your address, select <strong>Settings</strong> (the gear icon), then select <strong>New Domain</strong>.</li>
<li>Fill in the information needed to add your domain:</li>
</ol>
<ul>
<li><strong>Domain</strong>: Enter the domain you want to set up BCC from Google.</li>
<li><strong>Configured As</strong>: Select Hops, enter <code>2</code>.</li>
<li><strong>Forwarding To</strong>: Enter <code>google.com</code>.</li>
<li><strong>Outbound TLS</strong>: Select <strong>Forward all messages over TLS</strong>.</li>
<li><strong>Quarantine policy</strong>: Ensure no policy is selected.</li>
</ul>
<ol start="5">
<li>Select <strong>Publish Domain</strong>.</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<p>Now that you have found your BCC address and added your domain, continue with <a href="/email-security/deployment/api/setup/gsuite-bcc-setup/bcc-rules-to-area1/">Add BCC rules</a> to add BCC rules to Email security.</p>
