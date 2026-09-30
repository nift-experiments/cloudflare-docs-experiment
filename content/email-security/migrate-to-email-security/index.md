---
cp9:
  canonical: https://developers.cloudflare.com/email-security/migrate-to-email-security/
  description: Migrate from Area 1 to Cloudflare Email Security, including equivalent actions and updated terminology.
  full_title: Migrate to Email security · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Migrate to Email security · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Migrate from Area 1 to Cloudflare Email Security, including equivalent actions and updated terminology."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/migrate-to-email-security/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/migrate-to-email-security/index.md"><meta property="og:title" content="Migrate to Email security · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Migrate from Area 1 to Cloudflare Email Security, including equivalent actions and updated terminology."><meta property="og:url" content="https://developers.cloudflare.com/email-security/migrate-to-email-security/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/migrate-to-email-security/
  schema: 1
---
<p>This page aims at showing you how to perform Area 1 actions in <a href="/cloudflare-one/email-security/">Zero Trust Email security</a>, and new terminology introduced in Email security.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1055.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="access-to-area-1">Access to Area 1</h3>
@markup("md", "content/.markup/bodies/1054.md")
</aside>
<h2 id="contact-support">Contact support</h2>
<p>In Area 1, you can reach out to support via the following email addresses:</p>
<ul>
<li><a href="mailto:support@area1security.com">support@area1security.com</a></li>
<li><a href="mailto:phishguard@area1security.com">phishguard@area1security.com</a> (for PhishGuard customers only)</li>
</ul>
<p>In Email security, you can raise a ticket by contacting <a href="https://dash.cloudflare.com/?to=/:account/support">technical support</a> on the Cloudflare dashboard:</p>
<ol>
<li>Select your account and choose <strong>Technical support</strong>.</li>
<li>In <strong>Solve your issue</strong>, answer the following questions:
<ul>
<li>What type of question do you have? Select <strong>Technical - Other Products</strong></li>
<li>In what area can we help you? Select <strong>Email security</strong></li>
<li>What feature, service or problem is this related to? Choose among <strong>Configuration</strong>, <strong>Detections</strong> or <strong>PhishGuard</strong>.</li>
</ul>
</li>
</ol>
<h2 id="invite-users">Invite users</h2>
<p>In Area 1, you <a href="/email-security/account-setup/manage-account-members/#add-user">invite users</a> by logging in to the Area 1 portal and inviting members.</p>
<p>To invite users in Zero Trust Email security:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Go to <strong>Manage Account</strong>.</li>
<li>Select <strong>Members</strong> &gt; <strong>Invite</strong> &gt; <a href="/fundamentals/manage-members/manage/#add-account-members">Add account members</a>.</li>
</ol>
<p>Once you have added new account members, you will have to assign each member an <a href="/cloudflare-one/roles-permissions/#email-security-roles">Email security role</a>.</p>
<table>
<thead>
<tr>
<th>Area 1</th>
<th>Email security</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>N/A</td>
<td>Cloudflare Zero Trust</td>
<td>Can edit Cloudflare <a href="/cloudflare-one/">Zero Trust</a>. Has administrator access to all Zero Trust products including Access, Gateway, the Cloudflare One Client, Tunnel, Browser Isolation, CASB, DLP, DEX, and Email security.</td>
</tr>
<tr>
<td>Super Admin</td>
<td>Email security Analyst + Email security Configuration Admin = Super Admin</td>
<td>Has full access to all admin features in Email security</td>
</tr>
<tr>
<td>Configuration Admin</td>
<td>Email security Configuration Admin</td>
<td>Has administrator access. Cannot take actions on emails, or read emails</td>
</tr>
<tr>
<td>SOC Analyst</td>
<td>Email security Analyst</td>
<td>Has analyst access. Can take action on emails and read emails.</td>
</tr>
<tr>
<td>Viewer</td>
<td>Email security Reporting</td>
<td>Can read metrics</td>
</tr>
<tr>
<td>N/A</td>
<td>Cloudflare Zero Trust PII</td>
<td>Can read PII in Zero Trust (this includes Email security)</td>
</tr>
<tr>
<td>N/A</td>
<td>Email security Policy Admin</td>
<td>Can read all settings, but only write allow policies, trusted domains, and blocked senders</td>
</tr>
</tbody>
</table>
<h2 id="create-webhooks">Create webhooks</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1053.md")
</aside>
<p>In Area 1, you can <a href="/email-security/email-configuration/domains-and-routing/alert-webhooks/#create-an-alert-webhook">create alert webhooks</a>.</p>
<p>In Zero Trust Email security, webhooks are instead referred to as logs. You can enable <a href="/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-detection-logs">detection logs</a> and/or <a href="/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-user-action-logs">user action logs</a>. Additionally, you can enable <a href="/cloudflare-one/email-security/outbound-dlp/">Outbound Data Loss Prevention</a> to protect sensitive information in outbound emails.</p>
<h2 id="set-up-system-alerts">Set up system alerts</h2>
<p>You can check the Area 1 and Email security status in the <a href="https://www.cloudflarestatus.com/">Cloudflare System Status</a>.</p>
<p>To view Area 1 status:</p>
<ul>
<li>Search for <strong>Email security (Area1)</strong> and check that the status is set to <strong>Operational</strong>. This means that emails are being processed.</li>
<li>Search for <strong>Area 1 - Dash</strong> to check the status of the Area 1 dashboard.</li>
<li>Search for <strong>Area 1 - API</strong> to check the status of the API endpoints.</li>
</ul>
<p>To view Email security status:</p>
<ul>
<li>Search for <strong>Email security (Zero Trust)</strong> and check that the status is set to <strong>Operational</strong>. This means that emails are being processed.</li>
<li>Search for <strong>Zero Trust Dashboard</strong> to check the status of the Zero Trust dashboard.</li>
<li>Search for <strong>API</strong> to check the status of the API endpoints.</li>
</ul>
<p>You can also check the status of APIs through the <a href="https://www.cloudflarestatus.com/api">Cloudflare Status API</a> and configure <a href="/notifications/get-started/#configure-notifications">Cloudflare Notifications</a>.</p>
<h2 id="email-reports">Email reports</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1052.md")
</aside>
<p>In Area 1, you receive daily or weekly updates of the number of emails dispositioned.</p>
<p>In Email security, you can view <a href="/cloudflare-one/email-security/monitoring/">email monitoring</a> over the last 90, 30, 7, 3, 1 day(s).</p>
<h2 id="email-alerts-for-detections">Email alerts for detections</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1051.md")
</aside>
<p>In Area 1, you receive an email when an email is assigned a disposition.</p>
<p>In Email security, you enable <a href="/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-detection-logs">Logpush</a> to enable detection logs.</p>
<h2 id="search-emails">Search emails</h2>
<p>In Area 1, you can perform two types of search: <a href="/email-security/reporting/search/#fielded-search">Fielded Search</a> and <a href="/email-security/reporting/search/#freeform-search">Freeform Search</a>.</p>
<p>In Email security, the ability to search emails has been expanded. You can use three different <a href="/cloudflare-one/email-security/investigation/search-email/#screen-criteria">screen criteria</a> to search emails:</p>
<ul>
<li><a href="/cloudflare-one/email-security/investigation/search-email/#advanced-screen">Advanced screen</a></li>
<li><a href="/cloudflare-one/email-security/investigation/search-email/#regular-screen">Regular screen</a></li>
<li><a href="/cloudflare-one/email-security/investigation/search-email/#popular-screen">Popular screen</a></li>
</ul>
<h2 id="check-metrics">Check metrics</h2>
<p>In Area 1, you can check <a href="/email-security/reporting/statistics-overview/">statistics</a> in your Home section.</p>
<p>In Email security, you can check your metrics in the <a href="/cloudflare-one/email-security/monitoring/">Monitoring</a> section in the dashboard.</p>
<h2 id="move-messages-to-a-specific-folder">Move messages to a specific folder</h2>
<p>Area 1 allows you to set up <a href="/email-security/email-configuration/retract-settings/">message retraction</a> to move messages to specific folders. This is known as <strong>retraction</strong>.</p>
<p>Moving messages to a specific folder is known as <a href="/cloudflare-one/email-security/settings/auto-moves/">auto-moves</a> in Zero Trust Email security.</p>
<h2 id="create-policies">Create policies</h2>
<p>This table displays the difference in terminology used when creating policies:</p>
<table>
<thead>
<tr>
<th>Area 1</th>
<th>Email security</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/email-security/email-configuration/lists/allowed-patterns/">Allowed patterns</a></td>
<td><a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">Allow policies</a></td>
</tr>
<tr>
<td><a href="/email-security/email-configuration/lists/block-list/">Block lists</a></td>
<td><a href="/cloudflare-one/email-security/settings/detection-settings/blocked-senders/">Blocked senders</a></td>
</tr>
<tr>
<td><a href="/email-security/email-configuration/lists/trusted-domains/">Trusted domains</a></td>
<td><a href="/cloudflare-one/email-security/settings/detection-settings/trusted-domains/">Trusted domains</a></td>
</tr>
<tr>
<td><a href="/email-security/email-configuration/email-policies/text-addons/">Text add-ons</a></td>
<td><a href="/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/">Text add-ons</a></td>
</tr>
<tr>
<td><a href="/email-security/email-configuration/email-policies/link-actions/">Link actions</a></td>
<td><a href="/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/">Link actions</a></td>
</tr>
<tr>
<td><a href="/email-security/email-configuration/enhanced-detections/added-detections/">Added detections</a></td>
<td><a href="/cloudflare-one/email-security/settings/detection-settings/additional-detections/">Additional detections</a></td>
</tr>
</tbody>
</table>
<h2 id="submissions">Submissions</h2>
<p>This table displays the difference in terminology used when finding emails whose disposition is incorrect:</p>
<table>
<thead>
<tr>
<th>Area 1</th>
<th>Email security</th>
</tr>
</thead>
<tbody>
<tr>
<td>Report <a href="/email-security/email-configuration/phish-submissions/#false-negatives">false negative</a>/<a href="/email-security/email-configuration/phish-submissions/#false-positives">false positive</a></td>
<td><a href="/cloudflare-one/email-security/submissions/#submit-messages-for-review">Submit messages for review</a></td>
</tr>
<tr>
<td>N/A</td>
<td>Escalate user submissions</td>
</tr>
<tr>
<td><a href="/email-security/email-configuration/phish-submissions/#how-to-submit-phish">Team submission</a></td>
<td><a href="/cloudflare-one/email-security/submissions/team-submissions/">Team submissions</a></td>
</tr>
<tr>
<td><a href="/email-security/email-configuration/phish-submissions/#how-to-submit-phish">User submission</a></td>
<td><a href="/cloudflare-one/email-security/submissions/user-submissions/">User submissions</a></td>
</tr>
</tbody>
</table>
<h2 id="business-email-compromise">Business Email Compromise</h2>
<p>In Area 1, you can set up a <a href="/email-security/email-configuration/enhanced-detections/business-email-compromise/">Business email compromise (BEC)</a> list to protect against attackers who try to impersonate executives.</p>
<p>In Email security, this feature is known as <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/">impersonation registry</a>.</p>
<h2 id="synchronize-directories">Synchronize directories</h2>
<p>In Area 1, you can <a href="/email-security/email-configuration/enhanced-detections/business-email-compromise/#integrating-a-directory">integrate directories</a> in your email provider.</p>
<p>In Email security, you can add and sync <a href="/cloudflare-one/email-security/directories/">directories</a>.</p>
<h2 id="api">API</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1050.md")
</aside>
<p>To access Area 1 API, go to the <a href="https://developers.cloudflare.com/email-security/static/api_documentation_1.38.1.pdf">API Documentation</a>. You can set up a <a href="https://developers.cloudflare.com/email-security/api/service-accounts/">service account</a> to configure API tokens.</p>
<p>To access Email security API, go to <a href="https://developers.cloudflare.com/api/resources/email_security/">Email security API</a>. You can set up an <a href="/fundamentals/api/get-started/create-token/">API token</a> to use the Email security API.</p>
