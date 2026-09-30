---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/manage-pii/
  description: How Manage PII works in Zero Trust analytics.
  full_title: Manage PII · Cloudflare One docs
  head_html: <title>Manage PII · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How Manage PII works in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/manage-pii/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/manage-pii/index.md"><meta property="og:title" content="Manage PII · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Manage PII works in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/manage-pii/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Privacy"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/manage-pii/#page","headline":"Manage PII \u00b7 Cloudflare One docs","description":"How Manage PII works in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/manage-pii/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Privacy"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/logs/dashboard-logs/gateway-logs/manage-pii/
  schema: 1
---
<p>Cloudflare Gateway gives you multiple ways to safely handle your employees' personally identifiable information (PII) in activity logs:</p>
<ul>
<li><strong>Redact PII</strong> (default) — PII is stored in logs but hidden from view. Only the Super Administrator and users with the <a href="/cloudflare-one/roles-permissions/#cloudflare-zero-trust-pii">Cloudflare Zero Trust PII role</a> can view redacted PII. The underlying data is preserved — redaction only controls who can see it.</li>
<li><strong><a href="#exclude-pii">Exclude PII</a></strong> — PII is not stored in logs at all. No user, including the Super Administrator, can retrieve it.</li>
</ul>
<p>Only the Super Administrator can assign roles and determine who has permission to view PII. To add or remove the Cloudflare Zero Trust PII role for a user in your organization, refer to <a href="/fundamentals/manage-members/roles/">Roles</a>.</p>
<h2 id="types-of-pii">Types of PII</h2>
<p>Cloudflare Gateway can log the following types of PII:</p>
<ul>
<li>Source IP</li>
<li>User email</li>
<li>User ID</li>
<li>Device ID</li>
<li>URL</li>
<li>Referer</li>
<li>User agent</li>
</ul>
<h2 id="exclude-pii">Exclude PII</h2>
<p>When you exclude PII, Gateway logs activity without storing any employee PII. This differs from the default redaction behavior — excluded PII is not stored and cannot be retrieved by any role, including the Super Administrator.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4987.md")
</aside>
<p>Changes to this setting do not affect PII already stored in previous logs.</p>
<p>To turn on the setting to exclude PII:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>In <strong>Traffic logging</strong>, turn on <strong>Exclude personally identifiable information (PII) from logs</strong>.</li>
</ol>
