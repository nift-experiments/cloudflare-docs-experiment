---
cp9:
  canonical: https://developers.cloudflare.com/email-security/account-setup/manage-parent-permissions/
  description: Control the level of access a partner parent account has to your Email Security child account.
  full_title: Manage parent permissions · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Manage parent permissions · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Control the level of access a partner parent account has to your Email Security child account."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/account-setup/manage-parent-permissions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/account-setup/manage-parent-permissions/index.md"><meta property="og:title" content="Manage parent permissions · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Control the level of access a partner parent account has to your Email Security child account."><meta property="og:url" content="https://developers.cloudflare.com/email-security/account-setup/manage-parent-permissions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/account-setup/manage-parent-permissions/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8486.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="access-to-area-1">Access to Area 1</h3>
@markup("md", "content/.markup/bodies/8485.md")
</aside>
<p>When you set up Email security through a <a href="/email-security/partners/">partner</a>, that partner's account is the <strong>parent</strong> account to your <strong>child</strong> account.</p>
<p>Each child account can set the level of access allowed to their account from the parent. You may want to update this setting if you are receiving troubleshooting support from your parent account.</p>
<p>To update parent permissions:</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>Go to <strong>Delegated Accounts</strong>.</p>
</li>
<li>
<p>Select a permission level:</p>
<ul>
<li><strong>No external account access</strong>: Shuts off all access from the parent account (including Email security).</li>
<li><strong>Allow external account view-only access</strong> (default): Allows a parent user to view the customer's portal, including settings.</li>
<li><strong>Allow external account Super Admin access</strong>: Allows a parent user to administer the customer account on their behalf. By selecting this option the customer is acknowledging consent for outside administration of their account.</li>
</ul>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
