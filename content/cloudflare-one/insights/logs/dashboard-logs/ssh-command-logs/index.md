---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs/
  description: Review SSH commands a user ran on a target.
  full_title: SSH command logs · Cloudflare One docs
  head_html: <title>SSH command logs · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Review SSH commands a user ran on a target."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs/index.md"><meta property="og:title" content="SSH command logs · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review SSH commands a user ran on a target."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Logging,SSH"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs/#page","headline":"SSH command logs \u00b7 Cloudflare One docs","description":"Review SSH commands a user ran on a target.","url":"https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Logging","SSH"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs/
  schema: 1
---
<p>SSH command logs record the commands that users run on infrastructure targets protected by <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Access for Infrastructure</a>. Use these logs to audit user activity on your SSH servers and investigate specific sessions.</p>
<p>To view SSH command logs, log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>SSH command logs</strong>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To generate SSH command logs, you must:</p>
<ol>
<li>Set up <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Access for Infrastructure</a> for your SSH servers.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#ssh-command-logs">Enable SSH command logging</a> by uploading an encryption public key. Cloudflare uses this key to encrypt your logs so that only you can read their contents.</li>
</ol>
<h2 id="view-ssh-logs">View SSH logs</h2>
<p>SSH command logs displayed in the dashboard are encrypted using the public key you provided during setup. The logs are not readable in the dashboard — you must download and decrypt them locally. To view the contents of the logs:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>SSH command logs</strong>.</li>
<li>Filter the logs using the name of your SSH application.</li>
<li>Select the SSH session for which you want to export command logs.</li>
<li>In the side panel, scroll down to <strong>SSH logs</strong> and select <strong>Download</strong>.</li>
<li>Decrypt the log using the <a href="https://github.com/cloudflare/ssh-log-cli/">SSH Logging CLI</a> and the private key that corresponds to the public key you uploaded.</li>
</ol>
<h2 id="log-fields">Log fields</h2>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Session ID</strong></td>
<td>Unique identifier for the SSH session.</td>
</tr>
<tr>
<td><strong>User email</strong></td>
<td>Email address of the user who initiated the SSH session.</td>
</tr>
<tr>
<td><strong>Target ID</strong></td>
<td>Identifier of the infrastructure target being accessed. Corresponds to the target you configured in Access for Infrastructure.</td>
</tr>
<tr>
<td><strong>Client address</strong></td>
<td>Source IP address of the SSH connection.</td>
</tr>
<tr>
<td><strong>Server address</strong></td>
<td>Destination IP address of the SSH server.</td>
</tr>
<tr>
<td><strong>Session start datetime</strong></td>
<td>Timestamp when the SSH session started.</td>
</tr>
<tr>
<td><strong>Session finish datetime</strong></td>
<td>Timestamp when the SSH session ended.</td>
</tr>
<tr>
<td><strong>Program type</strong></td>
<td>Type of SSH program: <code>shell</code> (interactive terminal), <code>exec</code> (single command execution), <code>x11</code>, <code>direct-tcpip</code>, or <code>forwarded-tcpip</code>. Note that <code>x11</code>, <code>direct-tcpip</code>, and <code>forwarded-tcpip</code> correspond to SSH features that are <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#known-limitations">not currently supported</a> by Access for Infrastructure.</td>
</tr>
<tr>
<td><strong>Payload</strong></td>
<td>Captured request/response data in <a href="https://docs.asciinema.org/manual/asciicast/v2/">asciicast v2</a> format, a structured terminal recording format. Includes commands for <code>exec</code> programs.</td>
</tr>
<tr>
<td><strong>Error</strong></td>
<td>SSH error message, if an error occurred during the session.</td>
</tr>
</tbody>
</table>
<h2 id="export-ssh-logs-with-logpush">Export SSH logs with Logpush</h2>
<p>Enterprise users can export SSH command logs to external storage or analysis destinations using <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>. Unlike dashboard logs, Logpush payloads are not encrypted with a customer-provided public key — secure access to your storage destination accordingly.</p>
<p>For a list of all available fields, refer to <a href="/logs/logpush/logpush-job/datasets/account/ssh_logs/">SSH Logs</a>.</p>
