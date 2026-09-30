---
cp9:
  canonical: https://developers.cloudflare.com/network-flow/rules/rule-notifications/
  description: Configure notifications for Network Flow rule matches.
  full_title: Configure rule notifications · Cloudflare Network Flow docs
  head_html: <title>Configure rule notifications · Cloudflare Network Flow docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure notifications for Network Flow rule matches."><link rel="canonical" href="https://developers.cloudflare.com/network-flow/rules/rule-notifications/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-flow/rules/rule-notifications/index.md"><meta property="og:title" content="Configure rule notifications · Cloudflare Network Flow docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure notifications for Network Flow rule matches."><meta property="og:url" content="https://developers.cloudflare.com/network-flow/rules/rule-notifications/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network Flow"><meta name="algolia_product_filter" content="Network Flow"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Network Flow"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network-flow/rules/rule-notifications/#page","headline":"Configure rule notifications \u00b7 Cloudflare Network Flow docs","description":"Configure notifications for Network Flow rule matches.","url":"https://developers.cloudflare.com/network-flow/rules/rule-notifications/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /network-flow/rules/rule-notifications/
  schema: 1
---
<p>Network Flow (formerly Magic Network Monitoring) can notify you by email, webhook, or PagerDuty when a rule is triggered. When a rule detects a traffic anomaly, notifications alert your team so you can respond — or, if you use Magic Transit with auto-advertisement, Cloudflare can begin mitigating the attack automatically.</p>
<p>For more information on the notification platform, refer to <a href="/notifications/">Notifications documentation</a>. You can also:</p>
<ul>
<li><a href="/notifications/get-started/">Configure Cloudflare notifications</a></li>
<li><a href="/notifications/get-started/configure-pagerduty/">Configure PagerDuty</a></li>
<li><a href="/notifications/get-started/configure-webhooks/">Configure webhooks</a></li>
<li><a href="/notifications/get-started/#test-a-notification">Test a notification</a></li>
<li><a href="/notifications/notification-history/">Notification History</a></li>
</ul>
<h2 id="notification-configuration-fields">Notification configuration fields</h2>
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Notification name</strong></td>
<td align="left">A label to identify this notification in your notifications list.</td>
</tr>
<tr>
<td align="left"><strong>Description (optional)</strong></td>
<td align="left">The description of the notification.</td>
</tr>
<tr>
<td align="left"><strong>Webhooks</strong></td>
<td align="left">One or more webhooks to deliver the notification to.</td>
</tr>
<tr>
<td align="left"><strong>Notification email</strong></td>
<td align="left">One or more email addresses to deliver the notification to.</td>
</tr>
</tbody>
</table>
<h2 id="rule-auto-advertisement-notifications">Rule Auto-Advertisement notifications</h2>
<p>Webhook, PagerDuty, and email notifications are sent following an auto-advertisement attempt for all prefixes inside the flagged rule.</p>
<p>You will receive the status of the advertisement for each prefix with the following available statuses:</p>
<ul>
<li><strong>Advertised</strong>: The prefix was successfully advertised.</li>
<li><strong>Already Advertised</strong>: The prefix was advertised prior to the auto advertisement attempt.</li>
<li><strong>Delayed</strong>: The prefix cannot currently be advertised but will attempt advertisement. After the prefix can be advertised, a new notification is sent with the updated status.</li>
<li><strong>Locked</strong>: The prefix is locked and cannot be advertised.</li>
<li><strong>Could not Advertise</strong>: Cloudflare was unable to advertise the prefix. This status can occur for multiple reasons, but usually occurs when you are not allowed to advertise a prefix.</li>
<li><strong>Error</strong>: A general error occurred during prefix advertisement.</li>
</ul>
<h2 id="configure-rule-notifications">Configure rule notifications</h2>
<p>To configure notifications for Network Flow rules:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add</strong>.</li>
<li>Select <em>Magic Transit</em> from the product drop-down menu.</li>
<li>Find the appropriate Network Flow alert and select <strong>Select</strong>:
<ul>
<li><strong>Network Flow: Volumetric Attack</strong> - for static threshold and dynamic threshold notifications</li>
<li><strong>Network Flow: DDoS Attack</strong> - for sFlow DDoS attack notifications</li>
</ul>
</li>
<li>Fill in the notification configuration details.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
