---
cp9:
  canonical: https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/bcc-rules-to-area1/
  description: Add Gmail content compliance BCC rules to forward inbound email to Email Security for scanning.
  full_title: Add BCC rules · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Add BCC rules · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Add Gmail content compliance BCC rules to forward inbound email to Email Security for scanning."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/bcc-rules-to-area1/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/bcc-rules-to-area1/index.md"><meta property="og:title" content="Add BCC rules · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add Gmail content compliance BCC rules to forward inbound email to Email Security for scanning."><meta property="og:url" content="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/bcc-rules-to-area1/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/deployment/api/setup/gsuite-bcc-setup/bcc-rules-to-area1/
  schema: 1
---
<ol>
<li>In the <a href="https://admin.google.com/">Google Admin console</a>, go to <strong>Menu</strong> &gt; <strong>Apps</strong> &gt; <strong>Google Workspace</strong> &gt; <strong>Gmail</strong> &gt; <strong>Compliance</strong>.</li>
<li>Go to <strong>Content Compliance</strong> &gt; Select <strong>Edit</strong>.</li>
<li>Add a <strong>Content Compliance</strong> filter, and name it <code>Email security (Area 1) - BCC</code>.</li>
<li>In <strong>Email messages to affect</strong>, select <strong>Inbound</strong>.</li>
<li>Select the recipients you want to send emails to Email security (formerly Area 1) via BCC. Under <strong>Add expressions that describe the content you want to search for in each message</strong>:
<ul>
<li>Select <strong>If ANY of the following match the message</strong>.</li>
<li>Select <strong>Add</strong> to configure the expression.
<ul>
<li>Select <strong>Advanced content match</strong>.</li>
<li>In <strong>Location</strong>, select <strong>Headers + Body</strong>.</li>
<li>In <strong>Match type</strong>, select <strong>Matches regex</strong>.</li>
<li>In <strong>Regexp</strong> input <code>.*</code>. You can customize the regex as needed and test within the admin page or on sites like <a href="https://regexr.com/">Regexr</a>.</li>
<li>Select <strong>SAVE</strong>.</li>
</ul>
</li>
</ul>
</li>
<li>In <strong>If the above expressions match, do the following</strong>:
<ul>
<li>Select <strong>Modify message</strong>.
<ul>
<li>Ensure that <strong>Envelope recipient</strong> &gt; <strong>Change envelope recipient</strong> is unselected, to ensure that emails will not be dropped as an unintended consequence. You will select this option at a later stage.</li>
<li>Go to <strong>Also deliver to</strong>, select <strong>Add more recipients</strong> &gt; <strong>ADD</strong> &gt; Choose <strong>Advanced</strong>.
<ul>
<li>Under <strong>Envelope recipient</strong>, select <strong>Change envelope recipient</strong> &gt; <strong>Replace recipient</strong> &gt; Enter the email of the recipient.</li>
<li>Under <strong>Spam and delivery options</strong>, select <strong>Suppress bounces from this recipient</strong>.</li>
<li>Under <strong>Headers</strong>, select <strong>Add X-Gm-Spam and X-Gm-Phishy headers</strong>.</li>
<li>Select <strong>SAVE</strong>.</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>In <strong>Account types to affect</strong>, select <strong>Users</strong> and <strong>Groups</strong>.</li>
<li>Select <strong>SAVE</strong>.</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<p>Now that you have added BCC rules on the Area 1 portal, you need to <a href="/email-security/deployment/api/setup/gsuite-bcc-setup/create-project-gcp/">create a project on Google Cloud Console</a>.</p>
