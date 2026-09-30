---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/
  description: Create HTTP DDoS Attack Protection overrides in the Cloudflare dashboard.
  full_title: Configure HTTP DDoS Attack Protection in the dashboard · Cloudflare DDoS Protection docs
  head_html: <title>Configure HTTP DDoS Attack Protection in the dashboard · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Create HTTP DDoS Attack Protection overrides in the Cloudflare dashboard."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/index.md"><meta property="og:title" content="Configure HTTP DDoS Attack Protection in the dashboard · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create HTTP DDoS Attack Protection overrides in the Cloudflare dashboard."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/#page","headline":"Configure HTTP DDoS Attack Protection in the dashboard \u00b7 Cloudflare DDoS Protection docs","description":"Create HTTP DDoS Attack Protection overrides in the Cloudflare dashboard.","url":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/
  schema: 1
---
<p>Configure the HTTP DDoS Attack Protection managed ruleset by defining <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">overrides</a> in the Cloudflare dashboard. DDoS overrides allow you to customize the <strong>action</strong> and <strong>sensitivity</strong> of one or more rules in the managed ruleset.</p>
<p>For more information on the available parameters and allowed values, refer to <a href="/ddos-protection/managed-rulesets/http/override-parameters/">Ruleset parameters</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="number-of-available-overrides">Number of available overrides</h3>
@markup("md", "content/.markup/bodies/7531.md")
</aside>
<p>Create multiple rules in the <code>ddos_l7</code> phase entry point ruleset to define different overrides for different sets of incoming requests. Set each rule expression according to the traffic whose HTTP DDoS protection you wish to customize.</p>
<p>Rules in the phase entry point ruleset, where you create overrides, are evaluated in order until there is a match for a rule expression and sensitivity level, and Cloudflare will apply the first rule that matches the request. Therefore, the rule order in the entry point ruleset is very important.</p>
<h2 id="access">Access</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7532.md")
</div>
<h3 id="create-a-ddos-override">Create a DDoS override</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7535.md")
</div>
<h3 id="delete-a-ddos-override">Delete a DDoS override</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7536.md")
</div>
