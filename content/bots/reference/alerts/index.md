---
cp9:
  canonical: https://developers.cloudflare.com/bots/reference/alerts/
  description: Set up notifications for spikes in bot traffic on your domain.
  full_title: Bot Detection Alerts · Cloudflare bot solutions docs
  head_html: <title>Bot Detection Alerts · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up notifications for spikes in bot traffic on your domain."><link rel="canonical" href="https://developers.cloudflare.com/bots/reference/alerts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/reference/alerts/index.md"><meta property="og:title" content="Bot Detection Alerts · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up notifications for spikes in bot traffic on your domain."><meta property="og:url" content="https://developers.cloudflare.com/bots/reference/alerts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Bots"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/reference/alerts/#page","headline":"Bot Detection Alerts \u00b7 Cloudflare bot solutions docs","description":"Set up notifications for spikes in bot traffic on your domain.","url":"https://developers.cloudflare.com/bots/reference/alerts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /bots/reference/alerts/
  schema: 1
---
<p>Bot alerts inform you when Cloudflare detects spikes in your traffic with any of the following characteristics:</p>
<ul>
<li>A global spike in traffic that has a bot score of less than 30.</li>
<li>An increase in traffic on available dimensions in <a href="#set-up-a-bot-detection-alert">Set up a bot detection alert</a>.</li>
<li>Filters of your choosing in <a href="#set-up-a-bot-detection-alert">Set up a bot detection alert</a>.</li>
</ul>
<hr />
<h2 id="alert-types">Alert types</h2>
<details><summary>Bot Detection Alert</summary><strong>Who is it for?</strong><p>Enterprise customers who want to be notified when Cloudflare detects a spike in bot traffic on their zones.</p>
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
</details>
<h3 id="set-up-a-bot-detection-alert">Set up a bot detection alert</h3>
<p>To receive Bot alerts, you must <a href="/notifications/get-started/">configure a notification</a>. Notifications help you stay up to date with your Cloudflare account through email, PagerDuty, or webhooks, depending on your Cloudflare plan.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3470.md")
</div>
<hr />
<h2 id="alert-logic">Alert logic</h2>
<p>The Bot Detection Alert notifies you when Cloudflare detects an abnormal spike to your zone where the <a href="https://blog.cloudflare.com/introducing-thresholds-in-security-event-alerting-a-z-score-love-story/">Z-score</a> exceeds 3.5 and bot requests exceed 200 per 5 minutes (bot score below 30). A Z-score measures how far a value deviates from the average, so a Z-score above 3.5 indicates a statistically unusual traffic spike.</p>
<p>The Z-score is calculated using a six-hour baseline window and a five-minute observation window.</p>
<p>Bot Detection Alerts are delivered with Cloudflare’s Notifications system via email, webhook, or Pager Duty.</p>
<p>You will not receive duplicate alerts within the same one-hour time frame, except in rare cases where different alert values simultaneously trigger alerts.</p>
<p>In addition to the information above, Custom Bot Detection Alerts allow you to include or exclude certain conditions:</p>
<ul>
<li>User-agent</li>
<li>Hostname</li>
<li>URI Path</li>
<li>IP Source Address</li>
<li>Autonomous System Number (AS Num)</li>
<li>JA3 Fingerprint</li>
<li>JA4 Fingerprint</li>
<li>Bot Detection IDs</li>
</ul>
<p>You can also choose to group by the following dimensions so that they can be alerted of volumetric anomalies based on:</p>
<ul>
<li>JA4 Fingerprint (removes the filter of bot score &lt; 30)</li>
<li>AS Num</li>
<li>Bot Detection IDs</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3469.md")
</aside>
