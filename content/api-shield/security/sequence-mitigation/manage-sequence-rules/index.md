---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/security/sequence-mitigation/manage-sequence-rules/
  description: Create and manage sequence rules in the dashboard or via WAF custom rules.
  full_title: Manage sequence rules · Cloudflare API Shield docs
  head_html: <title>Manage sequence rules · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and manage sequence rules in the dashboard or via WAF custom rules."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/security/sequence-mitigation/manage-sequence-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/security/sequence-mitigation/manage-sequence-rules/index.md"><meta property="og:title" content="Manage sequence rules · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and manage sequence rules in the dashboard or via WAF custom rules."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/security/sequence-mitigation/manage-sequence-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="API Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/api-shield/security/sequence-mitigation/manage-sequence-rules/#page","headline":"Manage sequence rules \u00b7 Cloudflare API Shield docs","description":"Create and manage sequence rules in the dashboard or via WAF custom rules.","url":"https://developers.cloudflare.com/api-shield/security/sequence-mitigation/manage-sequence-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /api-shield/security/sequence-mitigation/manage-sequence-rules/
  schema: 1
---
<p>Cloudflare recommends creating sequence rules using WAF custom rules. Refer to the <a href="/api-shield/security/sequence-mitigation/custom-rules/">sequence custom rules documentation</a> for more information.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3251.md")
</aside>
<h2 id="create-a-sequence-rule">Create a sequence rule</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3252.md")
</div>
<h2 id="edit-a-sequence-rule">Edit a sequence rule</h2>
<p>You also have the option to edit an existing rule by selecting it on the rule list. You can rename your rule, adjust the starting and ending endpoint order, modify the endpoint, and change the action of the rule.</p>
<h2 id="reprioritize-a-sequence-rule">Reprioritize a sequence rule</h2>
<p>You can change the priority order of your rules by selecting and dragging the rules on the list.</p>
<p>You can also explicitly set a priority order by selecting the three dots on your rule and choosing <strong>Move to…</strong> where you can set the new priority in the resulting modal window.</p>
