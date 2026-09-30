---
cp9:
  canonical: https://developers.cloudflare.com/notifications/notification-available/
  description: Browse available notification types by product.
  full_title: Available Notifications · Cloudflare Notifications docs
  head_html: <title>Available Notifications · Cloudflare Notifications docs</title><meta name="generator" content="Nift"><meta name="description" content="Browse available notification types by product."><link rel="canonical" href="https://developers.cloudflare.com/notifications/notification-available/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/notifications/notification-available/index.md"><meta property="og:title" content="Available Notifications · Cloudflare Notifications docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Browse available notification types by product."><meta property="og:url" content="https://developers.cloudflare.com/notifications/notification-available/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Notifications"><meta name="algolia_product_filter" content="Notifications"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Notifications"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/notifications/notification-available/#page","headline":"Available Notifications \u00b7 Cloudflare Notifications docs","description":"Browse available notification types by product.","url":"https://developers.cloudflare.com/notifications/notification-available/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /notifications/notification-available/
  schema: 1
---
<p>Available Notifications depend on your Cloudflare plan. Cloudflare offers a variety of Notifications for our products and services, such as <a href="/billing/">Billing</a>, <a href="/ddos-protection/">Denial of Service protection</a>, <a href="/magic-transit/">Magic Transit</a>, and <a href="/ssl/">SSL/TLS</a>.</p>
<p>Depending on your plan, you can also configure webhooks, allowing you to connect your account with external services such as Slack and Google Chat, and PagerDuty to receive Cloudflare Notifications.</p>
<h2 id="actions-available-on-receiving-a-notification">Actions available on receiving a Notification</h2>
<p>Each Notification carries different types of information about the status of your Cloudflare account, or the type of action you can take.</p>
<p>Refer to information below to understand what each Notification does and what to do when receiving one.</p>
<h2 id="billing">Billing</h2><details><summary>Usage Based Billing</summary><strong>Who is it for?</strong><p>Customers who want to receive a notification when the usage of a product goes above a set level.</p>
<strong>Other options / filters</strong><p>You can choose the product that you want to be notified about and the threshold that fires the notification. Thresholds depend on the product chosen.</p>
<p>For example:</p>
<ul>
<li>Argo Smart Routing has <strong>Notify when total bytes of traffic exceeds</strong> as a threshold.</li>
<li>Load Balancing has <strong>Notify when total number of DNS Queries exceeds</strong> as a threshold.</li>
</ul>
<strong>Included with</strong><p>Professional plans or higher.</p>
<p><strong>Note:</strong> Usage-based billing notifications are available to Pay-as-you-go accounts only. Most Enterprise contract accounts are not supported.</p>
<strong>What should you do if you receive one?</strong><p>Review your product usage and adjust the configuration and/or increase the alerting threshold.</p>
</details><h2 id="bots">Bots</h2><details><summary>Bot Detection Alert</summary><strong>Who is it for?</strong><p>Enterprise customers who want to be notified when Cloudflare detects a spike in bot traffic on their zones.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Accounts with at least one Enterprise zone.</p>
<strong>What should you do if you receive one?</strong><p>Select the <a href="/waf/analytics/security-analytics/">Security Analytics</a> link enclosed in the alert message. Contact support if additional advice is needed on how to investigate the attack further.</p>
<strong>Additional information</strong><p>After an alert is created on the dashboard, it may take up to 30 minutes before sufficient data is available to begin detecting traffic anomalies. Verified bot traffic is excluded from bot alerts.</p>
</details><details><summary>Custom Bot Detection Alert</summary><strong>Who is it for?</strong><p>Enterprise customers who want to be notified when Cloudflare detects a spike in bot traffic on their zones.</p>
<strong>Other options / filters</strong><p>Refer to the <a href="/bots/reference/alerts/#alert-logic">alert logic</a> for more information on additional filters or groupings.</p>
<strong>Included with</strong><p>Accounts with at least one Enterprise zone.</p>
<strong>What should you do if you receive one?</strong><p>Select the <a href="/waf/analytics/security-analytics/">Security Analytics</a> link enclosed in the alert message. Contact support if additional advice is needed on how to investigate the attack further.</p>
<strong>Additional information</strong><p>After an alert is created on the dashboard, it may take up to 30 minutes before sufficient data is available to begin detecting traffic anomalies. Verified bot traffic is excluded from both basic and advanced bot alerts.</p>
<p>Alerts with grouping could cause potential noise if you set them up for a high-traffic zone. Grouping alerts function as if you set up separate policies with a filter for each value. Alerts may trigger multiple values in the same group as long as the traffic for each value reaches the threshold of 200.</p>
</details><h2 id="client-side-security">Client-side security</h2><details><summary>Client-side security New Code Change Detection Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when JavaScript dependencies change in the pages of their domain.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Customers with Client-Side Security Advanced.</p>
<strong>What should you do if you receive one?</strong><p>Investigate to confirm that it is an expected change.</p>
<strong>Additional information</strong><p>Triggered daily. If configured with a zone filter, the alert is triggered immediately.</p>
</details><details><summary>Client-side security New Domain Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when resources from new host domains appear in their domain.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Business plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Investigate to confirm that it is an expected change.</p>
<strong>Additional information</strong><p>Triggered hourly. If configured with a zone filter, the alert is triggered immediately.</p>
</details><details><summary>Client-side security New Malicious Domain Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when resources from a known malicious domain appear in their domain. For more information, refer to <a href="/client-side-security/how-it-works/malicious-script-detection/">Malicious script and connection detection</a>.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Customers with Client-Side Security Advanced.</p>
<strong>What should you do if you receive one?</strong><p>Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.</p>
<p>For more information, refer to <a href="/client-side-security/detection/review-malicious-scripts/">Review scripts and connections considered malicious</a>.</p>
</details><details><summary>Client-side security New Malicious Script Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when Cloudflare classifies JavaScript dependencies in their domain as malicious. For more information, refer to <a href="/client-side-security/how-it-works/malicious-script-detection/">Malicious script and connection detection</a>.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Customers with Client-Side Security Advanced.</p>
<strong>What should you do if you receive one?</strong><p>Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.</p>
<p>For more information, refer to <a href="/client-side-security/detection/review-malicious-scripts/">Review scripts and connections considered malicious</a>.</p>
</details><details><summary>Client-side security New Malicious URL Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when resources from a known malicious URL appear in their domain. For more information, refer to <a href="/client-side-security/how-it-works/malicious-script-detection/">Malicious script and connection detection</a>.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Customers with Client-Side Security Advanced.</p>
<strong>What should you do if you receive one?</strong><p>Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.</p>
<p>For more information, refer to <a href="/client-side-security/detection/review-malicious-scripts/">Review scripts and connections considered malicious</a>.</p>
</details><details><summary>Client-side security New Resources Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when new resources appear in their domain.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Business plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Investigate to confirm that it is an expected change.</p>
<strong>Additional information</strong><p>Triggered daily. If configured with a zone filter, the alert is triggered immediately.</p>
</details><details><summary>Client-side security New Resource Exceeds Max URL Length Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when a resource's URL exceeds the maximum allowed length.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Business plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Manually check the resource.</p>
</details><h2 id="cloudflare-access">Cloudflare Access</h2><details><summary>Expiring Access Service Token Alert</summary><strong>Who is it for?</strong><p><a href="/cloudflare-one/access-controls/policies/">Access</a> customers who want to receive a notification when their service token is about to expire.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Access</p>
<strong>What should you do if you receive one?</strong><p>Extend the expiration date of the service token. For more details, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#renew-service-tokens">Renew your service token</a>.</p>
</details><h2 id="cloudflare-images">Cloudflare Images</h2><details><summary>Image Notifications</summary><strong>Who is it for?</strong><p>Customers using <a href="/images/upload-images/direct-creator-upload/">Direct creator uploads</a> to upload images.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Cloudflare images subscription.</p>
<strong>What should you do if you receive one?</strong><p>No action is needed.</p>
</details><details><summary>Image Transformation Notifications</summary><strong>Who is it for?</strong><p>Customers who are using free image transformations and want to be notified if they exceed their free quota.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>No action is needed.</p>
</details><h2 id="cloudflare-status">Cloudflare Status</h2><details><summary>Maintenance Notification</summary><strong>Who is it for?</strong><p>Customers interested in knowing about planned <a href="/support/troubleshooting/disruptive-maintenance/">Cloudflare maintenance</a> for specific data centers. The notification lets you know when maintenance has been scheduled, changed, or canceled on an entire point of presence.</p>
<strong>Other options / filters</strong><p>You can filter maintenance notifications for specific points of presence and updates (scheduled, changed, canceled).</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>If the notification is announcing new scheduled maintenance, you may want to add the maintenance to your calendar. During these maintenance windows, you may experience a slight increase in latency to the edge location which is under maintenance.</p>
</details><details><summary>Incident Alerts</summary><strong>Who is it for?</strong><p>Customers interested in knowing about Cloudflare incidents. The notification lets you know when Cloudflare incidents are created, updated, and resolved.</p>
<strong>Other options / filters</strong><p>You can filter incident alerts to specific impact levels (minor, major, critical).</p>
<p>Additionally, incident alerts can be filtered to incidents affecting specific components. By default, incident alerts will trigger a notification for incident updates across all impact levels and components.</p>
<p>The impact level and affected components of an incident may change as the incident progresses. A notification will only be sent if the configured filters match at the time of the incident update. Updates will not be sent retroactively.</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>Review your <a href="/analytics/">analytics</a> page to see if your domain is impacted.</p>
</details><h2 id="ddos-protection">DDoS Protection</h2><details><summary>HTTP DDoS Attack Alert</summary><strong>Who is it for?</strong><p><a href="/waf/">WAF</a> or <a href="/cache/">CDN</a> customers who want to receive a notification when Cloudflare has mitigated HTTP attacks that generate more than 100 requests per second.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>No action needed. Refer to <a href="/ddos-protection/reference/alerts/">DDoS alerts</a> for more information.</p>
</details><details><summary>Layer 3/4 DDoS Attack Alert</summary><strong>Who is it for?</strong><p><a href="/byoip/">BYOIP</a> and <a href="/spectrum/">Spectrum</a> customers with <a href="/analytics/network-analytics/">Network Analytics</a> who want to receive a notification when Cloudflare has mitigated attacks that generate an average of at least 12,000 packets per second over a five-second period, with a duration of one minute or more.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Magic Transit and/or BYOIP.</p>
<strong>What should you do if you receive one?</strong><p>No action needed. Refer to <a href="/ddos-protection/reference/alerts/">DDoS alerts</a> for more information.</p>
</details><details><summary>Advanced HTTP DDoS Attack Alert</summary><strong>Who is it for?</strong><p><a href="/waf/">WAF</a> or <a href="/cache/">CDN</a> customers with the <a href="/ddos-protection/">Advanced DDoS Protection</a> subscription who want to receive a notification when Cloudflare has mitigated attacks that generate more than the configured number of requests per second (100 rps by default).</p>
<strong>Other options / filters</strong><p>You can choose when to trigger a notification.</p>
<p>Available filters include:</p>
<ul>
<li>The zones in the account for which you wish to receive notifications.</li>
<li>The specific hostnames for which you wish to receive notifications.</li>
<li>The minimum requests-per-second rate that will trigger the alert (100 rps by default).</li>
</ul>
<strong>Included with</strong><p>Enterprise plans with the Advanced DDoS Protection add-on.</p>
<strong>What should you do if you receive one?</strong><p>No action needed. Refer to <a href="/ddos-protection/reference/alerts/">DDoS alerts</a> for more information.</p>
</details><details><summary>Advanced Layer 3/4 DDoS Attack Alert</summary><strong>Who is it for?</strong><p><a href="/byoip/">BYOIP</a> and <a href="/magic-transit/">Magic Transit</a> customers with <a href="/analytics/network-analytics/">Network Analytics</a> who want to receive a notification when Cloudflare has mitigated attacks that generate more than the configured number of packets per second (12,000 pps by default).</p>
<strong>Other options / filters</strong><p>You can choose when to trigger a notification.</p>
<p>Available filters include:</p>
<ul>
<li>The IP prefixes for which you wish to receive notifications.</li>
<li>The specific IP addresses for which you wish to receive notifications.</li>
<li>The minimum packets-per-second rate that will trigger the alert (12,000 pps by default).</li>
<li>The minimum megabits-per-second rate that will trigger the alert.</li>
<li>The protocols for which you wish to receive notifications (all protocols by default).</li>
</ul>
<p>If you specify multiple filters, Cloudflare applies an <code>AND</code> logic. This means the alert will only trigger if all filters you set are true. Keep this in mind when setting up this alert with more than one filter.</p>
<strong>Included with</strong><p>Purchase of Magic Transit and/or BYOIP (Enterprise plans).</p>
<strong>What should you do if you receive one?</strong><p>No action needed. Refer to <a href="/ddos-protection/reference/alerts/">DDoS alerts</a> for more information.</p>
</details><h2 id="dex">DEX</h2><details><summary>Device connectivity anomaly</summary><strong>Who is it for?</strong><p>Zero Trust customers who want to be notified when Cloudflare detects a spike or drop in the number of devices connected to the WARP client.</p>
<strong>Other options / filters</strong><ul>
<li><strong>Alert configuration</strong>: Choose when to trigger a notification. Available options are <em>Connectivity spike</em>, <em>Connectivity drop</em>, and <em>Connectivity spike or drop</em>.</li>
<li>Filters:
<ul>
<li><strong>Colo</strong>: Cloudflare data center that the device is connected to.</li>
<li><strong>Platform</strong>: Operating system of the device.</li>
<li><strong>Version</strong>: WARP client version (for example, <code>2024.3.409.0</code>).</li>
<li><strong>Mode</strong>: <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">WARP mode</a> deployed on the device.</li>
</ul>
</li>
</ul>
<strong>Included with</strong><p>All Cloudflare Zero Trust plans.</p>
<strong>What should you do if you receive one?</strong><p>Review your <a href="/cloudflare-one/insights/dex/fleet-status/">fleet status</a> to investigate why the spike or drop occurred and which devices are impacted.</p>
<strong>Additional information</strong><p>To learn more about the alert logic, refer to <a href="/cloudflare-one/insights/dex/notifications/#z-score">Z-score</a>.</p>
</details><details><summary>DEX test latency</summary><strong>Who is it for?</strong><p>Zero Trust customers who wish to receive alerts when there is a spike or drop in application latency, as measured by the HTTP test <a href="/cloudflare-one/insights/dex/tests/http/#test-results">Resource Fetch time</a> or Traceroute test <a href="/cloudflare-one/insights/dex/tests/traceroute/#test-results">Round trip time</a>. Requires setting up a <a href="/cloudflare-one/insights/dex/tests/">DEX test</a>.</p>
<strong>Other options / filters</strong><ul>
<li><strong>Alert configuration</strong>: Choose when to trigger a notification. Available options are <em>Latency spike</em>, <em>Latency drop</em>, and <em>Latency spike or drop</em>.</li>
<li>Filters:
<ul>
<li><strong>Colo</strong>: Cloudflare data center that the device is connected to.</li>
<li><strong>Platform</strong>: Operating system of the device.</li>
<li><strong>Version</strong>: WARP client version (for example, <code>2024.3.409.0</code>).</li>
<li><strong>Test name</strong>: Choose which DEX test the alert should monitor. You will receive individual notifications for each test.</li>
</ul>
</li>
</ul>
<strong>Included with</strong><p>All Cloudflare Zero Trust plans.</p>
<strong>What should you do if you receive one?</strong><p>View your <a href="/cloudflare-one/insights/dex/tests/view-results/">test results</a> to investigate why the spike occurred.</p>
<strong>Additional information</strong><p>To learn more about the alert logic, refer to <a href="/cloudflare-one/insights/dex/notifications/#z-score">Z-score</a>.</p>
</details><details><summary>DEX test low availability</summary><strong>Who is it for?</strong><p>Zero Trust customers who wish to receive alerts when the percentage of successful HTTP or traceroute requests to an application drops below the selected service-level objective (SLO). Requires setting up a <a href="/cloudflare-one/insights/dex/tests/">DEX test</a>.</p>
<strong>Other options / filters</strong><ul>
<li><strong>Service Level Objective (SLO)</strong>: Specify the availability threshold that will trigger an alert. Enter a percentage in <code>xx.x</code> format (for example, <code>98.0</code>).</li>
<li>Filters:
<ul>
<li><strong>Colo</strong>: Cloudflare data center that the device is connected to.</li>
<li><strong>Platform</strong>: Operating system of the device.</li>
<li><strong>Version</strong>: WARP client version (for example, <code>2024.3.409.0</code>).</li>
<li><strong>Test name</strong>: Choose which DEX test the alert should monitor. You will receive individual notifications for each test.</li>
</ul>
</li>
</ul>
<strong>Included with</strong><p>All Cloudflare Zero Trust plans.</p>
<strong>What should you do if you receive one?</strong><p>View your <a href="/cloudflare-one/insights/dex/tests/view-results/">test results</a> to investigate why the degradation occurred.</p>
<strong>Additional information</strong><p>To learn more about the alert logic, refer to <a href="/cloudflare-one/insights/dex/notifications/#slo">SLO</a>.</p>
</details><h2 id="dns">DNS</h2><details><summary>Secondary DNS all Primaries Failing</summary><strong>Who is it for?</strong><p>Enterprise customers who have at least one secondary zone in their account and want to receive a notification if all of their primary nameservers are failing.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Secondary DNS</p>
<strong>What should you do if you receive one?</strong><ol>
<li>Confirm that your primary nameservers are up and running.</li>
<li>Confirm that the <a href="/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/">Access Control Lists (ACLs)</a> on your primary nameservers are configured correctly.</li>
<li>Confirm that your primary nameservers are configured correctly in your Cloudflare account (correct IP, port, TSIG).</li>
</ol>
</details><details><summary>Secondary DNS Primaries Failing</summary><strong>Who is it for?</strong><p>Enterprise customers who have at least one secondary zone and want to receive a notification if at least one of their primary nameservers is failing while transfers from at least one other primary are still successful.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Secondary DNS.</p>
<strong>What should you do if you receive one?</strong><ol>
<li>Confirm that your primary nameservers are up and running.</li>
<li>Confirm that the <a href="/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/">Access Control Lists (ACLs)</a> on your primary nameservers are configured correctly.</li>
<li>Confirm that your primary nameservers are configured correctly in your Cloudflare account (correct IP, port, TSIG).</li>
</ol>
</details><details><summary>Secondary DNS Successfully Updated</summary><strong>Who is it for?</strong><p>Enterprise customers who have at least one secondary zone in their account and want to receive a notification on successful zone transfers.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Secondary DNS.</p>
<strong>What should you do if you receive one?</strong><p>No action needed. Everything is working correctly.</p>
</details><details><summary>Secondary DNS Warning</summary><strong>Who is it for?</strong><p>Customers who are using Cloudflare for Secondary DNS and want to receive notifications about warnings issued by the transferred zone.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><p>Actions for failure notifications will depend on the type of failure.</p>
</details><h2 id="health-checks">Health Checks</h2><details><summary>Health Checks status notification</summary><strong>Who is it for?</strong><p>Customers who want to be warned about changes to server health as determined by <a href="/health-checks/">health checks</a>.</p>
<strong>Other options / filters</strong><p>Available filters include:</p>
<ul>
<li>You can search for and add health checks from your list of health checks.</li>
<li>You can choose a trigger to fire the notification when your server becomes <strong>unhealthy</strong>, <strong>healthy</strong>, or <strong>either healthy or unhealthy</strong>.</li>
</ul>
<strong>Included with</strong><p>Professional plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Review your <a href="/health-checks/health-checks-analytics/#common-error-codes">health check analytics</a>.</p>
</details><h2 id="load-balancing">Load Balancing</h2><details><summary>Pool Enablement</summary><strong>Who is it for?</strong><p>Customers who want to be warned about status changes (enabled/disabled) in their pools.</p>
<strong>Other options / filters</strong><p>Available filters include:</p>
<ul>
<li>You can search for and add pools from your list of pools. If no pools are selected, the alert will apply to all pools in the account.</li>
<li>You can also choose the trigger that fires the notification when the Load Balancing pool is <strong>enabled</strong>, <strong>disabled</strong>, and <strong>either enabled or disabled</strong>.</li>
</ul>
<strong>Included with</strong><p>Purchase of <a href="/load-balancing/get-started/enable-load-balancing/">Load Balancing</a>.</p>
<strong>What should you do if you receive one?</strong><p>No action is needed.</p>
</details><details><summary>Load Balancing Health Alert</summary><strong>Who is it for?</strong><p>Customers who want to be warned about <a href="/load-balancing/understand-basics/health-details/">changes in health status</a> in their pools or origins.</p>
<strong>Other options / filters</strong><p>Available filters include:</p>
<ul>
<li>You can search for and add pools from your list of pools, as well as <strong>Include future pools</strong> (if all pools are selected).</li>
<li>You can choose the trigger that fires the notification when the health status becomes <strong>unhealthy</strong>, <strong>healthy</strong>, or <strong>either unhealthy or healthy</strong></li>
<li>You can choose the trigger that fires the notification when the event source health status changes in <strong>pool</strong>, <strong>origin</strong>, or <strong>either pool or origin</strong>.</li>
</ul>
<strong>Included with</strong><p>Purchase of <a href="/load-balancing/get-started/enable-load-balancing/">Load Balancing</a>.</p>
<strong>What should you do if you receive one?</strong><p>Evaluate <a href="/load-balancing/reference/load-balancing-analytics/">load balancing analytics</a> to review changes in health status over time.</p>
</details><h2 id="logpush">Logpush</h2><details><summary>Failing Logpush Job Disabled</summary><strong>Who is it for?</strong><p>Enterprise customers who use <a href="/logs/">Logpush</a> and want to monitor their job health.</p>
<strong>Other options / filters</strong><ul>
<li>Notification Name: A custom name for the notification.</li>
<li>Description (optional): A custom description for the notification.</li>
<li>Notification Email (can be multiple emails): The email address of the recipient for the notification.</li>
</ul>
<strong>Included with</strong><p>Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><p>In the email for the notification, you can find the destination name for the failing Logpush job. With this destination name, you should be able to figure out which zone this relates to. There can be multiple reasons why a job fails, but it is best to test that the destination endpoint is healthy, and that necessary credentials are still working. You can also check that the destination has allowlisted <a href="https://www.cloudflare.com/ips/">Cloudflare IPs</a>.</p>
</details><h2 id="magic-transit">Magic Transit</h2><details><summary>Network Flow - Auto Advertisement</summary><strong>Who is it for?</strong><p><a href="/magic-transit/on-demand/">Magic Transit on-demand</a> customers who use Flow-Based Monitoring and want alerts when Magic Transit is automatically enabled.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Magic Transit.</p>
<strong>What should you do if you receive one?</strong><p>No action is needed. You can go to the <a href="https://dash.cloudflare.com/?to=/:account/magic-transit">Cloudflare dashboard</a> to review the health and status of your tunnels.</p>
</details><details><summary>Network Flow - DDoS Attack</summary><strong>Who is it for?</strong><p><a href="/byoip/">BYOIP</a> and <a href="/spectrum/">Spectrum</a> customers with <a href="/analytics/network-analytics/">Network Analytics</a> who want to receive a notification when Cloudflare has mitigated attacks that generate an average of at least 12,000 packets per second over a five-second period, with a duration of one minute or more.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Magic Transit and/or BYOIP.</p>
<strong>What should you do if you receive one?</strong><p>No action needed. Refer to <a href="/ddos-protection/reference/alerts/">DDoS alerts</a> for more information.</p>
</details><details><summary>Network Flow - Volumetric Attack</summary><strong>Who is it for?</strong><p><a href="/magic-transit/on-demand/">Magic Transit on-demand</a> customers who are using Flow-Based Monitoring to detect attacks when Magic Transit is disabled.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Magic Transit.</p>
<strong>What should you do if you receive one?</strong><p>If you do not have auto advertisement enabled, you need to advertise your IP prefixes to enable Magic Transit. For more information, refer to <a href="/byoip/concepts/dynamic-advertisement/">Dynamic advertisement</a>.</p>
</details><details><summary>Magic Tunnel Health Check Alert</summary><strong>Who is it for?</strong><p>Magic Transit and Cloudflare WAN customers who wish to receive alerts when the percentage of tunnel states meeting the selected service-level objective (SLO) drops below the defined threshold for a Magic Tunnel.</p>
<strong>Other options / filters</strong><ul>
<li>Notification Name: A custom name for the notification.</li>
<li>Description (optional): A custom description for the notification.</li>
<li>Notification Email (can be multiple emails): The email address of recipient for the notification.</li>
<li>Webhooks</li>
<li>Tunnels: Choose one or more tunnels to monitor.</li>
<li>SLO: Define SLO threshold for Magic Tunnel health alerts. Available options are <em>High</em>, <em>Medium</em>, and <em>Low</em>.</li>
</ul>
<strong>Included with</strong><p>Purchase of Magic Transit and Cloudflare WAN.</p>
<strong>What should you do if you receive one?</strong><p>Refer to the <a href="/magic-transit/network-health/check-tunnel-health-dashboard/">Magic Transit tunnel health</a> or <a href="/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/">Cloudflare WAN IPsec/GRE tunnel health</a> for more information on what the issue might be.</p>
</details><h2 id="network-interconnect">Network Interconnect</h2><details><summary>Connection Maintenance Alert</summary><strong>Who is it for?</strong><p><a href="/network-interconnect/classic-cni/">Classic CNI</a> customers who want to be alerted to maintenance events that might affect Classic CNI.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Cloudflare Network Interconnect (CNI).</p>
<strong>What should you do if you receive one?</strong><p>No action is needed.</p>
</details><h2 id="pages">Pages</h2><details><summary>Project updates</summary><strong>Who is it for?</strong><p>Customers who want to receive notifications about project-level events in <a href="/pages/">Cloudflare Pages</a>.</p>
<strong>Other options / filters</strong><p>Available filters include:</p>
<ul>
<li>Pages projects</li>
<li>Environments</li>
<li>Different events: <strong>Deployment started</strong>, <strong>Deployment failed</strong>, or <strong>Deployment success</strong></li>
</ul>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>For failed deployments, review our <a href="/pages/configuration/debugging-pages/#check-your-build-log">debugging guide</a>.</p>
</details><h2 id="radar">Radar</h2><details><summary>Radar Alerts</summary><strong>Who is it for?</strong><p>Customers who want to receive a notification when traffic anomalies, outages, route hijacks, or route leaks are impacting one or more countries, regions, or autonomous systems (ASNs) of interest.</p>
<strong>Other options / filters</strong><p>Filters include:</p>
<ul>
<li>Notification type (anomaly, outage, route hijack, route leak)</li>
<li>Location (country or region)</li>
<li>Autonomous systems (ASNs)</li>
</ul>
<p>You have the option to send the notification via email, webhook, or PagerDuty.</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>Further action will depend on your role. Refer to the <a href="/radar/">Radar documentation</a> for more information.</p>
</details><h2 id="route-leak-detection">Route Leak Detection</h2><details><summary>Route Leak Detection Alert</summary><strong>Who is it for?</strong><p><a href="/byoip/">BYOIP customers</a> who want to receive a notification when their prefixes are advertised in places they should not be.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of BYOIP.</p>
<strong>What should you do if you receive one?</strong><p>Confirm your traffic is healthy. Reach out to your transit providers to ensure you are behaving as expected and ask them to follow up with any providers accepting the unauthorized routes.</p>
</details><h2 id="ssl-tls">SSL/TLS</h2><details><summary>Access mTLS Certificate Expiration Alert</summary><strong>Who is it for?</strong><p><a href="/cloudflare-one/access-controls/policies/">Access</a> customers that use client certificates for mutual TLS authentication. This notification will be sent 30 and 14 days before the expiration of the certificate.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">Access</a> and/or <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/">Cloudflare for SaaS</a>.</p>
<strong>What should you do if you receive one?</strong><p>Upload a <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#add-mtls-authentication-to-your-access-configuration">renewed certificate</a>.</p>
</details><details><summary>Advanced Certificate Alert</summary><strong>Who is it for?</strong><p>Customers with <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificates</a> that want to be alerted on validation, issuance, renewal, and expiration of certificates.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>When an advanced certificate is validated, issued, renewed, or expired.</p>
<strong>What should you do if you receive one?</strong><p>Action only needed if notification is about a certificate that failed to be issued. Refer to <a href="/ssl/troubleshooting/version-cipher-mismatch/">SSL expired or SSL mismatch errors</a> for more information.</p>
</details><details><summary>Hostname-level Authenticated Origin Pulls Certificate Expiration Alert</summary><strong>Who is it for?</strong><p>Customers that upload their own certificate to use with hostname-level Authenticated Origin Pull (AOP) to secure connections from Cloudflare to their origin server.
AOP certificate expiration notifications are sent 30 days and 14 days before the certificate expiry.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Authenticated Origin Pull.</p>
<strong>What should you do if you receive one?</strong><p>Upload a renewed certificate to use for <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">hostname-level AOP</a>.</p>
</details><details><summary>SSL for SaaS Custom Hostnames Alert</summary><strong>Who is it for?</strong><p>Customers with custom hostname certificates who want to receive a notification on validation, issuance, renewal, and expiration of certificates. For more details around data formatting for webhooks, refer to the <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/webhook-definitions/">Cloudflare for SaaS docs</a>.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a>.</p>
<strong>What should you do if you receive one?</strong><p>You only need to take action if you are notified that you have a certificate that failed. You can find the reasons why a certificate is not being issued in <a href="/ssl/troubleshooting/general-ssl-errors/">Troubleshooting SSL errors</a>.</p>
</details><details><summary>Universal SSL Alert</summary><strong>Who is it for?</strong><p>Customers with universal certificates who want to receive a notification on validation, issuance, renewal, and expiration notices.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>You only need to take action if you are notified that you have a certificate that failed. You can find the reasons why a certificate is not being issued in <a href="/ssl/troubleshooting/general-ssl-errors/">Troubleshooting SSL errors</a>.</p>
</details><details><summary>Zone-level Authenticated Origin Pulls Certificate Expiration Alert</summary><strong>Who is it for?</strong><p>Customers that upload their own certificate to use with zone-level Authenticated Origin Pull (AOP) to secure connections from Cloudflare to their origin server.
AOP certificate expiration notifications are sent 30 days and 14 days before the certificate expiry.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Authenticated Origin Pull.</p>
<strong>What should you do if you receive one?</strong><p>Upload a renewed certificate to use for <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/">zone-level AOP</a>.</p>
</details><details><summary>mTLS Certificate Store Certificate Expiration Alert</summary><strong>Who is it for?</strong><p>Customers that upload their own client certificates for mTLS via <a href="/ssl/client-certificates/byo-ca/">bring your own CA</a>.</p>
<p>This notification will be sent 30 and 14 days before the expiration of the certificate.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p><a href="/ssl/client-certificates/byo-ca/">Bring your own CA</a>.</p>
<p>The mTLS Certificate Store refers to customer uploaded certificates and does not include client certificates generated with the <a href="/ssl/client-certificates/#how-it-works">Cloudflare CA</a>.</p>
<strong>What should you do if you receive one?</strong><p>Upload a renewed certificate.</p>
</details><h2 id="security-center">Security Center</h2><details><summary>Brand Protection Alerts</summary><strong>Who is it for?</strong><p>Customers who want a summary of activity related to <a href="/security-center/brand-protection/">Brand Protection</a>.</p>
<strong>Other options / filters</strong><p>You can set up Brand Protection Alerts on individual monitored queries. For more details, refer to <a href="/security-center/brand-protection/#brand-protection-alerts">Brand Protection Alerts</a>.</p>
<strong>Included with</strong><p>Professional plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Investigate and potentially block any suspicious domains that may be trying to impersonate your brand.</p>
</details><details><summary>Brand Protection Digest</summary><strong>Who is it for?</strong><p>Customers who want a summary of activity related to <a href="/security-center/brand-protection/">Brand Protection</a>.</p>
<strong>Other options / filters</strong><p>You can set up Brand Protection Digest on individual monitored queries. For more details, refer to <a href="/security-center/brand-protection/#brand-protection-alerts">Brand Protection Alerts</a>.</p>
<strong>Included with</strong><p>Professional plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Investigate and potentially block any suspicious domains that may be trying to impersonate your brand.</p>
</details><details><summary>Logo Match Alerts</summary><strong>Who is it for?</strong><p>Customers who want to receive a notification when the <a href="/security-center/brand-protection/">Brand Protection</a> system detects a new domain which is using the uploaded logo and might be infringing copyright.</p>
<strong>Other options / filters</strong><p>You can select the query that you want to be alerted on.</p>
<strong>Included with</strong><p>Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><p>Review the domains and URLs that are potentially impersonating your brand.</p>
</details><details><summary>Security Insights</summary><strong>Who is it for?</strong><p>Customers who want to receive notifications based on security insights findings.</p>
<strong>Other options / filters</strong><p>You can select the insight(s) you want to be alerted on.</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>Review the insight and decide whether you want to resolve it, archive it, or export it.</p>
</details><details><summary>Abuse report</summary><strong>Who is it for?</strong><p>Customers who want to be alerted in the event that an abuse report is filed against their website.</p>
<strong>Other options / filters</strong><p>You can filter the reports based on date, report status, report type, and domain.</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>View our guidance on <a href="/fundamentals/reference/report-abuse/abuse-report-obligations/">customer abuse report obligations</a> and more information on how to <a href="/fundamentals/reference/report-abuse/submit-report/">view and submit abuse reports</a>.</p>
</details><h2 id="stream">Stream</h2><details><summary>Stream Live Notifications</summary><strong>Who is it for?</strong><p>Customers who are using <a href="/stream/">Stream</a> and want to receive webhooks with the status of their videos.</p>
<strong>Other options / filters</strong><p>You can input Stream Live IDs to receive notifications only about those inputs. If left blank, you will receive a list for all inputs.</p>
<p>The following input states will fire notifications. You can toggle them on or off:</p>
<ul>
<li><code>live_input.connected</code></li>
<li><code>live_input.disconnected</code></li>
</ul>
<strong>Included with</strong><p>Stream subscription.</p>
<strong>What should you do if you receive one?</strong><p>Stream notifications are entirely customizable by the customer. Action will depend on the customizations enabled.</p>
</details><h2 id="traffic-monitoring">Traffic Monitoring</h2><details><summary>Advanced Error Rate Alert</summary><strong>Who is it for?</strong><p>Enterprise customers who want to receive a notification when Cloudflare detects edge and/or origin errors. Refer to <a href="/notifications/reference/traffic-alerts/">HTTP Traffic Alerts</a> for more information.</p>
<strong>Other options / filters</strong><p>Available filters include:</p>
<ul>
<li>You can search and add domains from your list of domains.</li>
<li>You can filter alerts by <strong>edge status code</strong>, <strong>origin status code</strong>, and the <strong>IP Address</strong>.</li>
<li>You can also choose the trigger that fires the notification. Available triggers are <strong>low sensitivity</strong>, <strong>medium sensitivity</strong>, <strong>high sensitivity</strong>, or <strong>very high sensitivity</strong>.</li>
</ul>
<p>You can also toggle Alert Grouping to receive separate alerts for your domain, edge status code, and/or origin status code.</p>
<strong>Included with</strong><p>Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><ol>
<li>Use the link in the notification you received to see which error codes Cloudflare is seeing.</li>
<li>Depending on the statuses you are alerting on, refer to <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">Troubleshooting Cloudflare 5XX errors</a>.</li>
</ol>
<strong>Limitations</strong><p>Traffic Monitoring alerts are not sent for each individual events, but only when a spike in traffic reaches the threshold for an alert to be sent.</p>
<p>These thresholds cannot be configured. Service level objectives (SLOs) are used to determine the threshold.</p>
</details><details><summary>Origin Error Rate Alert</summary><strong>Who is it for?</strong><p>Enterprise customers who want to receive a notification when Cloudflare is unable to access their origin server. Refer to <a href="/notifications/reference/traffic-alerts/">HTTP Traffic Alerts</a> for more information.</p>
<strong>Other options / filters</strong><p>Multiple filters available:</p>
<ul>
<li>You can search and add domains from your list of domains.</li>
<li>You can also choose the trigger that fires the notification. Available triggers are <strong>low sensitivity</strong>, <strong>medium sensitivity</strong>, <strong>high sensitivity</strong>, or <strong>very high sensitivity</strong>.</li>
</ul>
<strong>Included with</strong><p>Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><ol>
<li>Use the link in the Notification you received to see which error codes Cloudflare is seeing from your origin.</li>
<li>Refer to <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">Troubleshooting Cloudflare 5XX errors</a> to learn how to troubleshoot these errors.</li>
</ol>
<strong>Limitations</strong><p>Traffic Monitoring alerts are not sent for each individual events, but only when a spike in traffic reaches the threshold for an alert to be sent.</p>
<p>These thresholds cannot be configured. Service level objectives (SLOs) are used to determine the threshold.</p>
</details><details><summary>Traffic Anomalies Alert</summary><strong>Who is it for?</strong><p>Enterprise customers who want to receive a notification when one zone is experiencing an unexpected spike or drop in traffic. Refer to <a href="/notifications/reference/traffic-alerts/">HTTP Traffic Alerts</a> for more information.</p>
<strong>Other options / filters</strong><p>Multiple filters available:</p>
<ul>
<li>You can search and add domains from your list of domains.</li>
<li>You can include or exclude traffic mitigated by the <a href="/waf/">Web Application Firewall (WAF)</a>.</li>
<li>You can choose whether to be notified of either spikes or drops in traffic.</li>
</ul>
<strong>Included with</strong><p>Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><p>Use the link in the Notification you received to view if the spike or drop is significant enough to require further actions.</p>
<strong>Limitations</strong><p>Traffic Monitoring alerts are not sent for each individual events, but only when a spike in traffic reaches the threshold for an alert to be sent.</p>
<p>These thresholds cannot be configured. Z-score is used to determine the threshold.</p>
</details><h2 id="trust-and-safety-blocks">Trust and Safety Blocks</h2><details><summary>Block Review Rejection</summary><strong>Who is it for?</strong><p>Customers who want to be notified when Cloudflare Trust &amp; Safety rejects a request for block removal.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>Take care of any abuse on your website. Then, go to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and request a review.</p>
</details><details><summary>New Blocks</summary><strong>Who is it for?</strong><p>Customers who want to be notified when Cloudflare Trust &amp; Safety places a block on their website.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>Take care of any abuse on your website. Then, go to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and request a review.</p>
</details><details><summary>Removed Blocks</summary><strong>Who is it for?</strong><p>Customers who want to be notified when Cloudflare Trust &amp; Safety removes a block from their website.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>This is informational follow up.</p>
</details><h2 id="tunnel">Tunnel</h2><details><summary>Tunnel Creation or Deletion Event</summary><strong>Who is it for?</strong><p>Customers who want to receive a notification when Cloudflare Tunnels are created or deleted in their account.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>All Cloudflare Zero Trust plans.</p>
<strong>What should you do if you receive one?</strong><p>No action is needed.</p>
</details><details><summary>Tunnel Health Alert</summary><strong>Who is it for?</strong><p>Customers who want to be warned about changes in health status for their Cloudflare Tunnels.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>All Cloudflare Zero Trust plans.</p>
<strong>What should you do if you receive one?</strong><p>Monitor tunnel health over time and consider deploying <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/"><code>cloudflared</code> replicas or load balancers</a>.</p>
<strong>Additional information</strong><p>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status">Tunnel status</a> to review the list of possible tunnel statuses (<code>Healthy</code>, <code>Inactive</code>, <code>Down</code> and <code>Degraded</code>).</p>
</details><h2 id="web-analytics">Web Analytics</h2><details><summary>Weekly summary</summary><strong>Who is it for?</strong><p>Customers using <a href="/web-analytics/">Web Analytics</a> to monitor their website's performance.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>No action is needed. This notification is a weekly summary with reports from your Web Analytics account. Refer to <a href="https://dash.cloudflare.com/?to=/:account/notifications">Notifications</a> in the Cloudflare dashboard to refine your notifications settings.</p>
</details><h2 id="web-application-firewall-waf">Web Application Firewall (WAF)</h2><details><summary>Advanced Security Events Alert</summary><strong>Who is it for?</strong><p>Enterprise customers who want to receive alerts about spikes in specific services that generate log entries in <a href="/waf/analytics/security-events/">Security Events</a>. For more information, refer to <a href="/waf/reference/alerts/">WAF alerts</a>.</p>
<strong>Other options / filters</strong><p>A mandatory <a href="/api/resources/alerting/subresources/policies/methods/create/"><code>filters</code></a> selection is needed when you create a notification policy which includes the list of services and zones that you want to be alerted on.</p>
<ul>
<li>You can search for and add domains from your list of Enterprise zones.</li>
<li>You can choose which services the alert should monitor (Managed Firewall, Rate Limiting, etc.).</li>
<li>You can filter events by a targeted action.</li>
</ul>
<strong>Included with</strong><p>Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><p>Review the information in <a href="/waf/analytics/security-events/">Security Events</a> to identify any possible attack or misconfiguration.</p>
<strong>Additional information</strong><p>The mean time to detection is five minutes.</p>
<p>When setting up this alert, you can select the services that will be monitored. Each selected service is monitored separately and can be selected as a filter.</p>
<strong>Limitations</strong><p>Security Events (WAF) alerts are not sent for each individual events, but only when a spike in traffic reaches the threshold for an alert to be sent.</p>
<p>These thresholds cannot be configured. Z-score is used to determine the threshold.</p>
</details><details><summary>Security Events Alert</summary><strong>Who is it for?</strong><p>Business and Enterprise customers who want to receive alerts about spikes across all services that generate log entries in <a href="/waf/analytics/security-events/">Security Events</a>. For more information, refer to <a href="/waf/reference/alerts/">WAF alerts</a>.</p>
<strong>Other options / filters</strong><p>A mandatory <a href="/api/resources/alerting/subresources/policies/methods/create/"><code>filters</code></a> selection is needed when you create a notification policy which includes the list of zones that you want to be alerted on.</p>
<ul>
<li>You can also search for and add domains from your list of business or enterprise zones. The notification will be sent for the domains chosen.</li>
<li>You can filter events by a targeted action.</li>
</ul>
<strong>Included with</strong><p>Business and Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><p>Review the information in <a href="/waf/analytics/security-events/">Security Events</a> to identify any possible attack or misconfiguration.</p>
<strong>Additional information</strong><p>The mean time to detection is five minutes.</p>
<p>When setting up this alert, you can select the services that will be monitored. Each selected service is monitored separately.</p>
<strong>Limitations</strong><p>Security Events (WAF) alerts are not sent for each individual events, but only when a spike in traffic reaches the threshold for an alert to be sent.</p>
<p>These thresholds cannot be configured. Z-score is used to determine the threshold.</p>
</details>
