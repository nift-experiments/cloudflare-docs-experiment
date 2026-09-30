---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/threat-intelligence/get-started/
  description: Create a WAF rule using Cloudforce One threat intelligence fields.
  full_title: Get started · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Get started · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a WAF rule using Cloudforce One threat intelligence fields."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/threat-intelligence/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/threat-intelligence/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a WAF rule using Cloudforce One threat intelligence fields."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/threat-intelligence/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Threat Intelligence"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/threat-intelligence/get-started/#page","headline":"Get started \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Create a WAF rule using Cloudforce One threat intelligence fields.","url":"https://developers.cloudflare.com/waf/detections/threat-intelligence/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Threat Intelligence"]}</script>
  markdown: true
  noindex: false
  route: /waf/detections/threat-intelligence/get-started/
  schema: 1
---
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>Your account must have an active <a href="/security-center/cloudforce-one/">Cloudforce One subscription</a>. Contact your account team for access.</li>
<li>The <a href="/waf/">WAF</a> must be enabled on your zone.</li>
</ul>
<h2 id="1-create-a-rule-from-threat-events"><ol>
<li>Create a rule from Threat Events</li>
</ol></h2>
<p>The fastest way to create a threat intelligence rule is from a saved view in the <a href="/security-center/cloudforce-one/">Threat Events</a> dashboard. Filter the threats you care about, then export the filters directly to a WAF rule.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15481.md")
</div>
<h2 id="2-review-matches-in-security-analytics"><ol start="2">
<li>Review matches in Security Analytics</li>
</ol></h2>
<p>Once the rule is deployed, matches appear in <a href="/waf/analytics/security-analytics/">Security Analytics</a>. You can see the threat event details — including threat actors, target industries, and countries — directly in the analytics view.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15482.md")
</div>
<p>If no matches appear after deploying the rule, contact your account team to verify your Cloudforce One subscription is active.</p>
<h2 id="3-switch-to-block-or-managed-challenge"><ol start="3">
<li>Switch to Block or Managed Challenge</li>
</ol></h2>
<p>Once you are confident in the match patterns, update the rule action from <em>Log</em> to <em>Block</em> or <em>Managed Challenge</em>.</p>
<p>For more examples, refer to <a href="/waf/detections/threat-intelligence/example-rules/">Example rules</a>. For the full field list, refer to <a href="/waf/detections/threat-intelligence/fields/">Threat intelligence fields</a>.</p>
<h2 id="4-alternative-create-a-rule-manually"><ol start="4">
<li>(Alternative) Create a rule manually</li>
</ol></h2>
<p>If you prefer to write expressions directly, you can create a rule from the dashboard or the API.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15486.md")
</div></div>
