---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/application-profiles/get-started/
  description: Learn a Schema Profile and safely configure mitigation.
  full_title: Get started · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Get started · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn a Schema Profile and safely configure mitigation."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/application-profiles/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/application-profiles/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn a Schema Profile and safely configure mitigation."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/application-profiles/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/application-profiles/get-started/#page","headline":"Get started \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Learn a Schema Profile and safely configure mitigation.","url":"https://developers.cloudflare.com/waf/detections/application-profiles/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/detections/application-profiles/get-started/
  schema: 1
---
<p>Create a learned Schema Profile for one operation. Then review its detections before configuring mitigation.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15545.md")
</aside>
<h2 id="review-learning-requirements">Review learning requirements</h2>
<p>Cloudflare learns profiles weekly from qualifying traffic during the previous seven days. Only requests that received a <code>2xx</code> response qualify.</p>
<p>An operation needs 1,000 qualifying requests for the field-learning threshold. It needs 10,000 qualifying requests for the boundary-learning threshold.</p>
<p>After meeting the field-learning threshold, Cloudflare can learn request fields. After meeting the boundary-learning threshold, Cloudflare can learn constraints such as numeric ranges and string lengths.</p>
<p>The first profile appears after the next weekly learning run. This can take up to seven days after meeting the relevant threshold.</p>
<h2 id="learn-and-review-a-profile">Learn and review a profile</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15546.md")
</div>
<p>After the profile becomes available, Cloudflare runs an <strong>always-on detection</strong>. It does not mitigate requests without a Custom Rule.</p>
<p>If no learned schema appears, confirm that you selected <strong>Learn profile</strong>. Cloudflare may still be collecting enough qualifying traffic.</p>
<p>For learning details and limitations, refer to <a href="/waf/detections/application-profiles/schema-profiles/">Schema Profiles</a>.</p>
<h2 id="use-an-uploaded-schema">Use an uploaded schema</h2>
<p>If you have an OpenAPI schema, upload it through <a href="/api-shield/security/schema-validation/">Schema validation</a>. Uploaded schemas produce detections through <code>cf.schema_validation.uploaded.violated</code>.</p>
<p>The API Shield reference covers upload formats, OpenAPI requirements, API configuration, Terraform configuration, and limitations.</p>
