---
cp9:
  canonical: https://developers.cloudflare.com/client-side-security/alerts/
  description: Cloudflare client-side resource alerts notify you when new scripts are detected on your domain or when Cloudflare detects resources that are likely malicious.
  full_title: Alerts · Client-side security docs
  head_html: <title>Alerts · Client-side security docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare client-side resource alerts notify you when new scripts are detected on your domain or when Cloudflare detects resources that are likely malicious."><link rel="canonical" href="https://developers.cloudflare.com/client-side-security/alerts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/client-side-security/alerts/index.md"><meta property="og:title" content="Alerts · Client-side security docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare client-side resource alerts notify you when new scripts are detected on your domain or when Cloudflare detects resources that are likely malicious."><meta property="og:url" content="https://developers.cloudflare.com/client-side-security/alerts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Client-side security"><meta name="algolia_product_filter" content="Client-side security"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Client-side security"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/client-side-security/alerts/#page","headline":"Alerts \u00b7 Client-side security docs","description":"Cloudflare client-side resource alerts notify you when new scripts are detected on your domain or when Cloudflare detects resources that are likely malicious.","url":"https://developers.cloudflare.com/client-side-security/alerts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /client-side-security/alerts/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4016.md")
</aside>
<p>Once you have activated client-side security's resource monitoring, you can set up one or more alerts informing you of relevant client-side changes on your zones.</p>
<p>You can configure unscoped or scoped alerts:</p>
<ul>
<li>
<p><strong>Unscoped alert</strong>: Covers all zones in your Cloudflare account. Unscoped alerts are triggered either daily, hourly, or immediately, depending on the <a href="/client-side-security/alerts/alert-types/">alert type</a>.</p>
</li>
<li>
<p><strong>Scoped alert</strong>: Covers one or more specific zones. Requires <a href="/client-side-security/rules/">content security rules</a> configured in those zones. Scoped alerts are triggered immediately and only notify you about resources that are covered by your rules. <a href="/client-side-security/rules/violations/">Rule violations</a> do not trigger these alerts. For more information, refer to <a href="#scoped-alerts">Scoped alerts</a>.</p>
</li>
</ul>
<p>For alerts sent at regular intervals, you might experience a delay between adding a new script and receiving an alert.</p>
<p>For instructions on configuring alerts, refer to <a href="/client-side-security/alerts/configure/">Configure an alert</a>.</p>
<h2 id="scoped-alerts">Scoped alerts</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4015.md")
</aside>
<p>If you have configured <a href="/client-side-security/rules/">content security rules</a> in a zone, you can filter alert notifications according to those rules. These alerts are called scoped alerts.</p>
<p>When you create a scoped alert using the <strong>Policies of these zones</strong> alert filter, you will only receive the most relevant notifications based on the rules you configured.</p>
<p>For each scoped alert, Cloudflare does the following:</p>
<ol>
<li>Check which content security rules are enabled in a zone, either in allow or in log mode.</li>
<li>For every enabled rule, compare the URL of the new or changed resource against the allowed sources in the rule.</li>
<li>If the resource is allowed by the rule, check if the new or modified resource should trigger the current alert.</li>
<li>If the alert should trigger, send an alert notification to the configured destinations.</li>
</ol>
<p>When you create a scoped alert you will not receive notifications for resources that are not allowed by a content security rule (either <a href="/client-side-security/rules/#rule-actions">in allow or in log mode</a>). These are <a href="/client-side-security/rules/violations/">rule violations</a> that you can review in the dashboard, through GraphQL, or via Logpush.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4014.md")
</aside>
<p>For unscoped alerts, you will receive notifications for all resources detected across your zones. Some of these resources may also violate your configured content security rules.</p>
