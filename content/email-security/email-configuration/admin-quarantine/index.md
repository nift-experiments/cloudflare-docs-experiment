---
cp9:
  canonical: https://developers.cloudflare.com/email-security/email-configuration/admin-quarantine/
  description: Quarantine incoming messages based on Email security dispositions to prevent threats from reaching inboxes.
  full_title: Admin Quarantine · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Admin Quarantine · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Quarantine incoming messages based on Email security dispositions to prevent threats from reaching inboxes."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/email-configuration/admin-quarantine/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/email-configuration/admin-quarantine/index.md"><meta property="og:title" content="Admin Quarantine · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Quarantine incoming messages based on Email security dispositions to prevent threats from reaching inboxes."><meta property="og:url" content="https://developers.cloudflare.com/email-security/email-configuration/admin-quarantine/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/email-configuration/admin-quarantine/
  schema: 1
---
<p>Admin Quarantine allows you to automatically prevent incoming messages from reaching a recipient's inbox based on the <span class="nb-glossary-tooltip" title="disposition">disposition</span> assigned by Email security.</p>
<p>The messages sent to Admin Quarantine are determined by your <a href="/email-security/email-configuration/domains-and-routing/domains/">domain settings</a>.</p>
<h2 id="quarantine-emails-by-disposition">Quarantine emails by disposition</h2>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>Select <strong>Email Configuration</strong> &gt; <strong>Domains</strong>.</p>
</li>
<li>
<p>Select the three dots on the domain that you want to configure admin quarantine for, and choose <strong>Edit</strong>.</p>
</li>
<li>
<p>In <strong>Quarantine Policy</strong> choose the dispositions you want to enable quarantine for that domain.</p>
</li>
<li>
<p>Select <strong>Update Domain</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/8477.md")
</aside>
<h2 id="access-admin-quarantine">Access Admin Quarantine</h2>
<p>You can view and potentially release emails that were sent to <strong>Admin Quarantine</strong>:</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Email</strong> &gt; <strong>Admin Quarantine</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/admin-quarantine/access-quarantine.png" alt="Access Admin Quarantine to review emails" /></p>
<ol start="3">
<li>Review emails as needed.</li>
</ol>
<h2 id="release-quarantined-emails">Release quarantined emails</h2>
<p>From <strong>Admin Quarantine</strong>, you can also release quarantined emails by selecting one or more messages:</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Email</strong> &gt; <strong>Admin Quarantine</strong>.</p>
</li>
<li>
<p>Find the email you want to release.</p>
</li>
<li>
<p>Select <strong>...</strong> &gt; <strong>Release</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/admin-quarantine/release-emails.png" alt="Select release to remove emails from quarantine" /></p>
<ol start="5">
<li>
<p>Select <strong>Release</strong> to confirm that you want to release the selected email.</p>
</li>
<li>
<p>(Optional) You can also release multiple messages, by selecting the box next to each message you want to release.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8476.md")
</aside>
