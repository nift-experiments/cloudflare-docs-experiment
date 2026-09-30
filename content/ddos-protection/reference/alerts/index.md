---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/reference/alerts/
  description: Configure DDoS attack notifications via email, webhook, or PagerDuty.
  full_title: DDoS alerts · Cloudflare DDoS Protection docs
  head_html: <title>DDoS alerts · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure DDoS attack notifications via email, webhook, or PagerDuty."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/reference/alerts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/reference/alerts/index.md"><meta property="og:title" content="DDoS alerts · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure DDoS attack notifications via email, webhook, or PagerDuty."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/reference/alerts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/reference/alerts/#page","headline":"DDoS alerts \u00b7 Cloudflare DDoS Protection docs","description":"Configure DDoS attack notifications via email, webhook, or PagerDuty.","url":"https://developers.cloudflare.com/ddos-protection/reference/alerts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/reference/alerts/
  schema: 1
---
<p>Configure notifications to receive real-time alerts (within ~1 minute) about L3/4 and L7 DDoS attacks on your Internet properties, depending on your plan and services. You can choose from different delivery methods.</p>
<p>Each notification email includes the following information:</p>
<ul>
<li>Description</li>
<li>Detection and mitigation time of attack</li>
<li>Attack type</li>
<li>Maximum rate of attack</li>
<li>Attack target (zone, host, or IP address)</li>
<li>Rule that matched the attack (ID and description)</li>
<li>Rule override, if any</li>
</ul>
<p>Cloudflare automatically sends weekly summaries of detected and mitigated DDoS attacks to Magic Transit and Spectrum BYOIP customers. Monthly application security reports are available for WAF/CDN customers. For more information, refer to <a href="/ddos-protection/reference/reports/">DDoS reports</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7457.md")
</aside>
<h2 id="set-up-a-notification-for-ddos-alerts">Set up a notification for DDoS alerts</h2>
<p>To set up a notification:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7458.md")
</div>
<h2 id="edit-an-existing-notification">Edit an existing notification</h2>
<p>To edit, delete, or disable a notification, go to your <a href="https://dash.cloudflare.com/?to=/:account/notifications">account notifications</a>.</p>
<hr />
<h2 id="alert-types">Alert types</h2>
<p>Cloudflare can issue notifications for different types of DDoS attack alerts.</p>
<h3 id="standard-alerts">Standard alerts</h3>
<details><summary>HTTP DDoS Attack Alert</summary><strong>Who is it for?</strong><p><a href="/waf/">WAF</a> or <a href="/cache/">CDN</a> customers who want to receive a notification when Cloudflare has mitigated HTTP attacks that generate more than 100 requests per second.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>No action needed. Refer to <a href="/ddos-protection/reference/alerts/">DDoS alerts</a> for more information.</p>
</details>
<details><summary>Layer 3/4 DDoS Attack Alert</summary><strong>Who is it for?</strong><p><a href="/byoip/">BYOIP</a> and <a href="/spectrum/">Spectrum</a> customers with <a href="/analytics/network-analytics/">Network Analytics</a> who want to receive a notification when Cloudflare has mitigated attacks that generate an average of at least 12,000 packets per second over a five-second period, with a duration of one minute or more.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Magic Transit and/or BYOIP.</p>
<strong>What should you do if you receive one?</strong><p>No action needed. Refer to <a href="/ddos-protection/reference/alerts/">DDoS alerts</a> for more information.</p>
</details>
<h3 id="advanced-alerts">Advanced alerts</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7456.md")
</aside>
<p>Advanced DDoS attack alerts support additional configuration, allowing you to filter the notifications you wish to receive.</p>
<details><summary>Advanced HTTP DDoS Attack Alert</summary><strong>Who is it for?</strong><p><a href="/waf/">WAF</a> or <a href="/cache/">CDN</a> customers with the <a href="/ddos-protection/">Advanced DDoS Protection</a> subscription who want to receive a notification when Cloudflare has mitigated attacks that generate more than the configured number of requests per second (100 rps by default).</p>
<strong>Other options / filters</strong><p>You can choose when to trigger a notification.</p>
<p>Available filters include:</p>
<ul>
<li>The zones in the account for which you wish to receive notifications.</li>
<li>The specific hostnames for which you wish to receive notifications.</li>
<li>The minimum requests-per-second rate that will trigger the alert (100 rps by default).</li>
</ul>
<strong>Included with</strong><p>Enterprise plans with the Advanced DDoS Protection add-on.</p>
<strong>What should you do if you receive one?</strong><p>No action needed. Refer to <a href="/ddos-protection/reference/alerts/">DDoS alerts</a> for more information.</p>
</details>
<details><summary>Advanced Layer 3/4 DDoS Attack Alert</summary><strong>Who is it for?</strong><p><a href="/byoip/">BYOIP</a> and <a href="/magic-transit/">Magic Transit</a> customers with <a href="/analytics/network-analytics/">Network Analytics</a> who want to receive a notification when Cloudflare has mitigated attacks that generate more than the configured number of packets per second (12,000 pps by default).</p>
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
</details>
<p>You will also receive alerts for rules with a <em>Log</em> action, containing information on what triggered the alert.</p>
<h2 id="availability">Availability</h2>
<p>The available alerts depend on your Cloudflare plan and subscribed services:</p>
<table>
<thead>
<tr>
<th>Alert type</th>
<th align="center">WAF/CDN</th>
<th align="center">Spectrum</th>
<th align="center">Spectrum BYOIP</th>
<th align="center">Magic Transit</th>
</tr>
</thead>
<tbody>
<tr>
<td>HTTP DDoS Attack Alert</td>
<td align="center">Yes</td>
<td align="center">–</td>
<td align="center">–</td>
<td align="center">–</td>
</tr>
<tr>
<td>Advanced HTTP DDoS Attack Alert</td>
<td align="center">Yes<sup>1</sup></td>
<td align="center">–</td>
<td align="center">–</td>
<td align="center">–</td>
</tr>
<tr>
<td>Layer 3/4 DDoS Attack Alert</td>
<td align="center">–</td>
<td align="center">Yes<sup>2, 3</sup></td>
<td align="center">Yes</td>
<td align="center">Yes<sup>3</sup></td>
</tr>
<tr>
<td>Advanced Layer 3/4 DDoS Attack Alert</td>
<td align="center">–</td>
<td align="center">–</td>
<td align="center">Yes<sup>2</sup></td>
<td align="center">Yes<sup>2</sup></td>
</tr>
</tbody>
</table>
<p><sup>1</sup> <em>Only available to Enterprise customers with the Advanced DDoS
Protection subscription.</em> <br />
<sup>2</sup> <em>Only available on an Enterprise plan.</em> <br />
<sup>3</sup> <em>Refer to <a href="#final-remarks">Final remarks</a> for additional notes.</em></p>
<h2 id="example-notification">Example notification</h2>
<p>The following image shows an example notification delivered via email:</p>
<p><img src="/assets/upstream/images/ddos-protection/ddos-notification-example.png" alt="Example notification email of a DDoS attack" /></p>
<p>To investigate a possibly ongoing attack, select <strong>View Dashboard</strong>. To go to the rule details in the Cloudflare dashboard, select <strong>View Rule</strong>.</p>
<h2 id="final-remarks">Final remarks</h2>
<ul>
<li>Spectrum and Magic Transit customers using <a href="/magic-transit/cloudflare-ips/">assigned Cloudflare IP addresses</a> will receive layer 3/4 DDoS attack alerts where the attacked target is the Cloudflare IP or prefix. If you have <a href="/byoip/">brought your own IP (BYOIP)</a> to Cloudflare Spectrum or Magic Transit, you will see your own IP addresses or prefixes as the attacked target.</li>
<li>In some cases, HTTP DDoS attack alerts will reference the attacked zone name instead of the attacked hostname. This occurs when the attack signature does not include information on the attacked hostname because it is not a strong indicator for identifying attack requests. For more information on attack signatures, refer to <a href="/ddos-protection/about/how-ddos-protection-works/">How DDoS protection works</a>.</li>
<li>DDoS alerts are currently only available for DDoS attacks detected and mitigated by the <a href="/ddos-protection/managed-rulesets/">DDoS managed rulesets</a>. Alerts are not yet available for DDoS attacks detected and mitigated by the <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a>, the <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a>, or the <a href="/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/">Programmable Flow Protection</a> system.</li>
<li>You will not receive duplicate DDoS alerts within the same one-hour time frame.</li>
<li>If you configure more than one alert type for the same kind of attack (for example, both an HTTP DDoS Attack Alert and an Advanced HTTP DDoS Attack Alert) you may get more than one notification when an attack occurs. To avoid receiving duplicate notifications, delete one of the configured alerts.</li>
</ul>
