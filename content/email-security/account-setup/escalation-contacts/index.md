---
cp9:
  canonical: https://developers.cloudflare.com/email-security/account-setup/escalation-contacts/
  description: Configure escalation contacts in Cloudflare Email security to prioritize alerts for phishing threats and email irregularities. Set up SOC, Triage, Analyst, and Executive contacts.
  full_title: Escalation contacts · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Escalation contacts · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure escalation contacts in Cloudflare Email security to prioritize alerts for phishing threats and email irregularities. Set up SOC, Triage, Analyst, and Executive contacts."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/account-setup/escalation-contacts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/account-setup/escalation-contacts/index.md"><meta property="og:title" content="Escalation contacts · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure escalation contacts in Cloudflare Email security to prioritize alerts for phishing threats and email irregularities. Set up SOC, Triage, Analyst, and Executive contacts."><meta property="og:url" content="https://developers.cloudflare.com/email-security/account-setup/escalation-contacts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/account-setup/escalation-contacts/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8492.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="access-to-area-1">Access to Area 1</h3>
@markup("md", "content/.markup/bodies/8491.md")
</aside>
<p>Whenever Email security (formerly Area 1) finds an exceptional <span class="nb-glossary-tooltip" title="phishing">phishing</span> threat or Email Service irregularity behavior (compromised email servers at a partner or vendor, wire fraud tactics, and more), we try to reach out to our customers.</p>
<p>There are four types of contacts available to configure, each with a priority type:</p>
<ul>
<li><strong>SOC Contact</strong>: P1 priority.</li>
<li><strong>Triage Analyst</strong>: P2 priority.</li>
<li><strong>In-Depth Analyst</strong>: P3 priority.</li>
<li><strong>Executive Contact</strong>: P4 priority.</li>
</ul>
<p>Email security will start by reaching out to P1-level contacts. If they do not respond, we will then try reaching out to the other contacts down the list until we receive a reply from one of these groups.</p>
<p>You can enable these special notifications through an opt-in process:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security (formerly Area 1) dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Subscriptions</strong> &gt; <strong>Escalation Contacts</strong>.</li>
<li>Select <strong>Add Contact</strong>.</li>
<li>Fill out the form.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8490.md")
</aside>
