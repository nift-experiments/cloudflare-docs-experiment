---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/
  description: Create cache rules in the Cloudflare dashboard.
  full_title: Create a cache rule in the dashboard · Cloudflare Cache (CDN) docs
  head_html: <title>Create a cache rule in the dashboard · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Create cache rules in the Cloudflare dashboard."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/index.md"><meta property="og:title" content="Create a cache rule in the dashboard · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create cache rules in the Cloudflare dashboard."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/#page","headline":"Create a cache rule in the dashboard \u00b7 Cloudflare Cache (CDN) docs","description":"Create cache rules in the Cloudflare dashboard.","url":"https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/cache-rules/create-dashboard/
  schema: 1
---
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Cache Rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong>.</li>
<li>(Optional) Select one of the rule templates that address common use cases. Then, review and adjust the proposed rule configuration.</li>
<li>Enter a descriptive name for the rule in <strong>Rule name</strong>.</li>
<li>Under <strong>When incoming requests match</strong>, select <strong>All incoming requests</strong> if you want the rule to apply to all traffic or <strong>Custom filter expression</strong> if you want the rule to only apply to traffic matching the custom expression.</li>
<li>If you selected <strong>Custom filter expression</strong>, under <strong>When incoming requests match</strong>, define the <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-builder">rule expression</a>. Use the <strong>Field</strong> drop-down list to choose an HTTP property and select an <strong>Operator</strong>. Refer to <a href="/cache/how-to/cache-rules/settings/">Available settings</a> for the list of available fields and operators.</li>
</ol>
<div class="medium-img">
<p><img src="/assets/upstream/images/cache/select-fields.png" alt="Select fields in the Expression Builder." /></p>
</div>
<ol start="8">
<li>Following the selection of the field and operator, enter the corresponding value that will trigger the Cache Rule. For example, if the selected field is <code>Hostname</code> and the operator is <code>equals</code>, a value of <code>cloudflare.com</code> would mean the rule matches any request to that hostname.</li>
</ol>
<div class="medium-img">
<p><img src="/assets/upstream/images/cache/example-rule.png" alt="Example rule" /></p>
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3908.md")
</aside>
<ol start="9">
<li>
<p>Under <strong>Then</strong>, in the <strong>Cache eligibility</strong> section, select <a href="/cache/how-to/cache-rules/settings/#bypass-cache"><strong>Bypass cache</strong></a> if you want matching requests to not be cacheable, or <strong>Eligible for cache</strong> if you want Cloudflare to attempt to cache them. Note that <a href="/cache/concepts/cache-control/">cache-control headers</a> can also impact cache eligibility.</p>
</li>
<li>
<p>If you selected <strong>Eligible for cache</strong> in the previous step, you can customize the options described in the <a href="/cache/how-to/cache-rules/settings/">Available settings</a> section.</p>
</li>
<li>
<p>Under <strong>Place at</strong>, from the dropdown, you can select the order of your rule. From the main page, you can also change the order of the rules you have created.</p>
</li>
<li>
<p>To save and deploy your rule, select <strong>Deploy</strong>. If you are not ready to deploy your rule, select <strong>Save as Draft</strong>.</p>
</li>
</ol>
<p>If you are matching a hostname in your rule expression, you may be prompted to create a proxied DNS record for that hostname. Refer to <a href="/rules/reference/troubleshooting/#this-rule-may-not-apply-to-your-traffic">Troubleshooting</a> for more information.</p>
