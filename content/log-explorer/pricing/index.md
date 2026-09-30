---
cp9:
  canonical: https://developers.cloudflare.com/log-explorer/pricing/
  description: Understand Log Explorer billing and usage.
  full_title: Pricing and managing usage · Cloudflare Log Explorer docs
  head_html: <title>Pricing and managing usage · Cloudflare Log Explorer docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand Log Explorer billing and usage."><link rel="canonical" href="https://developers.cloudflare.com/log-explorer/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/log-explorer/pricing/index.md"><meta property="og:title" content="Pricing and managing usage · Cloudflare Log Explorer docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand Log Explorer billing and usage."><meta property="og:url" content="https://developers.cloudflare.com/log-explorer/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Log Explorer"><meta name="algolia_product_filter" content="Log Explorer"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Log Explorer"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/log-explorer/pricing/#page","headline":"Pricing and managing usage \u00b7 Cloudflare Log Explorer docs","description":"Understand Log Explorer billing and usage.","url":"https://developers.cloudflare.com/log-explorer/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /log-explorer/pricing/
  schema: 1
---
<p>Log Explorer billing is based on the volume of logs ingested and stored, measured in gigabytes (GB). Your charges scale with the amount of log data you choose to retain in Log Explorer.</p>
<p>Unlike query-based billing models, charges are not based on how often you search or scan your data. Once logs are ingested and stored, you can query them without additional cost.</p>
<h2 id="availability">Availability</h2>
<p>Log Explorer is available as a paid add-on for any Application Services or Zero Trust purchase. There is no free version or trial available at this time.</p>
<h2 id="billable-usage">Billable usage</h2>
<p>Log Explorer billing is strictly consumption-based, calculated by the GBs ingested and stored.</p>
<h3 id="attack-traffic">Attack traffic</h3>
<p>Because Log Explorer is a forensics product, attack traffic is considered valuable data for analysis and is included in your billable usage.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/819.md")
</aside>
<h2 id="estimate-usage">Estimate usage</h2>
<p>To estimate your Log Explorer usage, review your request volumes in <strong>Analytics</strong> for specific Cloudflare log datasets.</p>
<h3 id="record-size-by-dataset">Record size by dataset</h3>
<p>The following table provides average and maximum record sizes for each dataset to help you estimate potential storage needs:</p>
<table>
<thead>
<tr>
<th>Dataset</th>
<th>Average Record Size</th>
<th>Maximum Record Size</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>audit_logs</code></td>
<td>2.69 kB</td>
<td>172 kB</td>
</tr>
<tr>
<td><code>email_security_alerts</code></td>
<td>6.74 kB</td>
<td>74.9 kB</td>
</tr>
<tr>
<td><code>firewall_events</code></td>
<td>1.36 kB</td>
<td>47.2 kB</td>
</tr>
<tr>
<td><code>audit_logs_v2</code></td>
<td>1.73 kB</td>
<td>28.5 kB</td>
</tr>
<tr>
<td><code>zaraz_events</code></td>
<td>7.30 kB</td>
<td>11.7 kB</td>
</tr>
<tr>
<td><code>http_requests</code></td>
<td>1.56 kB</td>
<td>9.76 kB</td>
</tr>
<tr>
<td><code>gateway_dns</code></td>
<td>1.44 kB</td>
<td>6.23 kB</td>
</tr>
<tr>
<td><code>dex_application_tests</code></td>
<td>3.29 kB</td>
<td>5.67 kB</td>
</tr>
<tr>
<td><code>casb_findings</code></td>
<td>2.67 kB</td>
<td>3.80 kB</td>
</tr>
<tr>
<td><code>gateway_http</code></td>
<td>1.47 kB</td>
<td>2.60 kB</td>
</tr>
<tr>
<td><code>dex_device_state_events</code></td>
<td>1.98 kB</td>
<td>2.57 kB</td>
</tr>
<tr>
<td><code>page_shield_events</code></td>
<td>443 B</td>
<td>2.02 kB</td>
</tr>
<tr>
<td><code>network_analytics_logs</code></td>
<td>1.31 kB</td>
<td>1.87 kB</td>
</tr>
<tr>
<td><code>zero_trust_network_sessions</code></td>
<td>1.21 kB</td>
<td>1.52 kB</td>
</tr>
<tr>
<td><code>gateway_network</code></td>
<td>877 B</td>
<td>1.17 kB</td>
</tr>
<tr>
<td><code>device_posture_results</code></td>
<td>730 B</td>
<td>944 B</td>
</tr>
<tr>
<td><code>spectrum_events</code></td>
<td>685 B</td>
<td>925 B</td>
</tr>
<tr>
<td><code>sinkhole_http_logs</code></td>
<td>705 B</td>
<td>705 B</td>
</tr>
<tr>
<td><code>access_requests</code></td>
<td>446 B</td>
<td>541 B</td>
</tr>
<tr>
<td><code>dns_firewall_logs</code></td>
<td>387 B</td>
<td>469 B</td>
</tr>
<tr>
<td><code>dns_logs</code></td>
<td>199 B</td>
<td>409 B</td>
</tr>
<tr>
<td><code>magic_ids_detections</code></td>
<td>334 B</td>
<td>349 B</td>
</tr>
<tr>
<td><code>warp_toggle_changes</code></td>
<td>327 B</td>
<td>335 B</td>
</tr>
<tr>
<td><code>ipsec_logs</code></td>
<td>207 B</td>
<td>260 B</td>
</tr>
<tr>
<td><code>nel_reports</code></td>
<td>204 B</td>
<td>224 B</td>
</tr>
</tbody>
</table>
<h2 id="monitor-usage">Monitor usage</h2>
<p>Cloudflare provides three primary ways to track your consumption and maintain financial oversight:</p>
<ul>
<li><strong>In-product quick indicator</strong>: View your current month's usage directly within the Log Explorer interface at the top of the <strong>Log Search</strong> and <strong>Manage Datasets</strong> sections.</li>
<li><strong>Account-level billing</strong>: Access a detailed view of current and previous months' cumulative usage under <strong>Manage Account</strong> &gt; <strong>Billing</strong>.</li>
<li><strong>Usage alerts</strong>: Set up automated notifications to trigger when billable usage exceeds a defined threshold.</li>
</ul>
<h3 id="configure-a-usage-alert">Configure a usage alert</h3>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select <strong>Manage account</strong>.</li>
<li>Go to <strong>Notifications</strong> &gt; <strong>Add</strong>.</li>
<li>Select <strong>Usage-based Billing</strong>.</li>
<li>Define your threshold and the notification destination (email, PagerDuty, or webhooks).</li>
</ol>
<h2 id="deactivate-log-explorer">Deactivate Log Explorer</h2>
<p>To stop using Log Explorer and end associated charges, you must complete both of the following steps:</p>
<h3 id="1-stop-log-ingestion"><ol>
<li>Stop log ingestion</li>
</ol></h3>
<p>Disabling datasets stops additional ingestion charges immediately.</p>
<ol>
<li>Go to the <a href="https://dash.cloudflare.com/?to=/:account/log-explorer/manage-sources">Manage datasets</a> page at the account level.</li>
<li>Use the toggle to turn off each dataset you no longer need.</li>
<li>Select <strong>Stop ingesting logs</strong> to confirm.</li>
</ol>
<h3 id="2-cancel-the-subscription"><ol start="2">
<li>Cancel the subscription</li>
</ol></h3>
<p>This prevents the subscription from renewing at the next billing cycle.</p>
<ol>
<li>Go to the <a href="https://dash.cloudflare.com/?to=/:account/billing">Billing</a> page.</li>
<li>In the <strong>Subscriptions</strong> tab, find the <strong>Log Explorer</strong> subscription and select <strong>Cancel</strong>.</li>
</ol>
