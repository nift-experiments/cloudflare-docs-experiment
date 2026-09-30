---
cp9:
  canonical: https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/
  description: Route Cloudflare notifications to PagerDuty.
  full_title: Configure PagerDuty · Cloudflare Notifications docs
  head_html: <title>Configure PagerDuty · Cloudflare Notifications docs</title><meta name="generator" content="Nift"><meta name="description" content="Route Cloudflare notifications to PagerDuty."><link rel="canonical" href="https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/index.md"><meta property="og:title" content="Configure PagerDuty · Cloudflare Notifications docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route Cloudflare notifications to PagerDuty."><meta property="og:url" content="https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Notifications"><meta name="algolia_product_filter" content="Notifications"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Notifications"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/#page","headline":"Configure PagerDuty \u00b7 Cloudflare Notifications docs","description":"Route Cloudflare notifications to PagerDuty.","url":"https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /notifications/get-started/configure-pagerduty/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10856.md")
</aside>
<p>Cloudflare’s Notification service supports routing notifications to PagerDuty. By sending notifications to PagerDuty you can leverage the same service definitions and escalation paths that you would for other third-party services that you connect to PagerDuty.</p>
<p>When a configuration that you have previously set up triggers a notification for PagerDuty, Cloudflare will send the notification to PagerDuty on your behalf. All of the PagerDuty services configured for the notification will receive the notification. PagerDuty will follow the service’s configuration to handle the notification appropriately. Actions like de-duping and rate limiting depend on the notification type.</p>
<p>To use PagerDuty as a connected service, you must <a href="https://www.pagerduty.com/sign-up/">sign up for a PagerDuty account</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10855.md")
</aside>
<h2 id="connect-pagerduty-to-a-cloudflare-account">Connect PagerDuty to a Cloudflare account</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Go to **Destinations**.
3. In the **Connected notification services** card, select **Connect**.
4. Log in to your [PagerDuty account](https://www.pagerduty.com/) to connect it to your Cloudflare account.
5. Choose the services you want to use and select **Connect**.
6. The browser will navigate back to your Cloudflare dashboard. Select **Continue**.
<p>Your new connected PagerDuty will appear in the <strong>Connected notification services</strong> card.</p>
<h2 id="edit-a-pagerduty-connected-service">Edit a PagerDuty connected service</h2>
<p>To edit which PagerDuty services are connected to your Cloudflare account, you must first disconnect PagerDuty from Cloudflare, make any changes you need in PagerDuty, and then reconnect it.</p>
<p>Disconnecting PagerDuty will disable any notifications being sent to PagerDuty where they are currently configured. If PagerDuty was the only configured destination, disconnecting PagerDuty may result in a notification with no destination.</p>
<p>If other delivery destinations were selected, then those notifications will still be routed as configured.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Go to **Destinations**.
3. In the **Connected notification services** card, select **View** on the PagerDuty service you want to disconnect.
4. Select **Disconnect** > **Confirm**.
5. Log in to your [PagerDuty account](https://www.pagerduty.com/) and make the required changes.
6. [Reconnect PagerDuty to Cloudflare](/notifications/get-started/configure-pagerduty/).
