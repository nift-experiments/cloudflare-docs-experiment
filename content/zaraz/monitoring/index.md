---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/monitoring/
  description: Monitor Zaraz tool loading and event delivery.
  full_title: Monitoring · Cloudflare Zaraz docs
  head_html: <title>Monitoring · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Monitor Zaraz tool loading and event delivery."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/monitoring/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/monitoring/index.md"><meta property="og:title" content="Monitoring · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Monitor Zaraz tool loading and event delivery."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/monitoring/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/monitoring/#page","headline":"Monitoring \u00b7 Cloudflare Zaraz docs","description":"Monitor Zaraz tool loading and event delivery.","url":"https://developers.cloudflare.com/zaraz/monitoring/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/monitoring/
  schema: 1
---
<p>Zaraz Monitoring shows you different metrics regarding Zaraz. This helps you to detect issues when they occur. For example, if a third-party analytics provider stops collecting data, you can use the information presented by Zaraz Monitoring to find where in the workflow the problem occurred.</p>
<p>You can also check activity data in the <strong>Activity last 24hr</strong> section, when you access <a href="/zaraz/get-started/">tools</a>, <a href="/zaraz/custom-actions/">actions</a> and <a href="/zaraz/custom-actions/create-trigger/">triggers</a> in the dashboard.</p>
<p>To use Zaraz Monitoring:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Monitoring</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
3. Select one of the options (Loads, Events, Triggers, Actions). Zaraz Monitoring will show you how the traffic for that section evolved for the time period selected.
<h2 id="zaraz-monitoring-options">Zaraz Monitoring options</h2>
<ul>
<li><strong>Loads</strong>: Counts how many times Zaraz was loaded on pages of your website. When <a href="/zaraz/reference/settings/#single-page-application-support">Single Page Application support</a> is enabled, Loads will count every change of navigation as well.</li>
<li><strong>Events</strong>: Counts how many times a specific event was tracked by Zaraz. It includes the <a href="/zaraz/get-started/">Pageview event</a>, <a href="/zaraz/web-api/track/">Track events</a>, and <a href="/zaraz/web-api/ecommerce/">E-commerce events</a>.</li>
<li><strong>Triggers</strong>: Counts how many times a specific trigger was activated. It includes the built-in <a href="/zaraz/custom-actions/create-trigger/">Pageview trigger</a> and any other trigger you set in Zaraz.</li>
<li><strong>Actions</strong>: Counts how many times a <a href="/zaraz/custom-actions/">specific action</a> was activated. It includes the pre-configured Pageview action, and any other actions you set in Zaraz.</li>
<li><strong>Server-side requests</strong>: tracks the status codes returned from server-side requests that Zaraz makes to your third-party tools.</li>
</ul>
