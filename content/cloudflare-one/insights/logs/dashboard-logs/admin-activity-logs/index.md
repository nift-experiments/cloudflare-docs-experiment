---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/admin-activity-logs/
  description: Monitor when a member on your account creates, updates, or deletes configurations.
  full_title: Admin activity logs · Cloudflare One docs
  head_html: <title>Admin activity logs · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Monitor when a member on your account creates, updates, or deletes configurations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/admin-activity-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/admin-activity-logs/index.md"><meta property="og:title" content="Admin activity logs · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Monitor when a member on your account creates, updates, or deletes configurations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/admin-activity-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Logging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/admin-activity-logs/#page","headline":"Admin activity logs \u00b7 Cloudflare One docs","description":"Monitor when a member on your account creates, updates, or deletes configurations.","url":"https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/admin-activity-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Logging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/logs/dashboard-logs/admin-activity-logs/
  schema: 1
---
<p>Admin activity logs record configuration changes made by members of your Cloudflare account. These logs are useful for auditing who changed a policy or setting and investigating unexpected configuration changes. Use these logs to monitor when a member creates, updates, or deletes configurations in your <a href="/cloudflare-one/setup/#create-a-zero-trust-organization">Zero Trust organization</a>.</p>
<p>To view admin activity logs, log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Admin activity logs</strong>.</p>
<h2 id="explanation-of-the-fields">Explanation of the fields</h2>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
<th>Example Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Email</td>
<td>User who performed the action</td>
<td><a href="mailto:josephli@cloudflare.com">josephli@cloudflare.com</a></td>
</tr>
<tr>
<td>Product</td>
<td>Cloudflare product being modified</td>
<td>Tunnel</td>
</tr>
<tr>
<td>Resource</td>
<td>Specific resource type within the product</td>
<td>Route</td>
</tr>
<tr>
<td>Event</td>
<td>Action performed (Create, Update, Delete)</td>
<td>Create</td>
</tr>
<tr>
<td>Date</td>
<td>Timestamp of when the action occurred</td>
<td>April 30, 2026 • 12:19 AM</td>
</tr>
<tr>
<td>User IP Address</td>
<td>IP address of the user who made the change</td>
<td>2a09:bac6:6447:523::83:30</td>
</tr>
<tr>
<td>Interface</td>
<td>How the change was initiated</td>
<td>API</td>
</tr>
<tr>
<td>Audit record</td>
<td>Unique identifier for the audit log entry</td>
<td>caf1a547-17cc-484a-b4ce-5d3b32771a8f</td>
</tr>
<tr>
<td>Old value</td>
<td>Previous configuration state (empty for creates)</td>
<td>{}</td>
</tr>
<tr>
<td>New value</td>
<td>New configuration state after the change</td>
<td>JSON object with fields like comment, network, tun_type, tunnel_id, virtual_network_id</td>
</tr>
</tbody>
</table>
<h2 id="export-admin-activity-logs">Export admin activity logs</h2>
<p>Enterprise users can export admin activity logs to a third-party storage destination or SIEM using <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>. For a list of all available fields, refer to <a href="/logs/logpush/logpush-job/datasets/account/audit_logs_v2/">Audit Logs V2</a>.</p>
