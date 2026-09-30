---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/
  description: Identify and address API vulnerabilities with discovery, schema validation, and abuse detection.
  full_title: Overview · Cloudflare API Shield docs
  head_html: <title>Overview · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Identify and address API vulnerabilities with discovery, schema validation, and abuse detection."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/index.md"><meta property="og:title" content="Overview · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Identify and address API vulnerabilities with discovery, schema validation, and abuse detection."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="API Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/api-shield/#page","headline":"Overview \u00b7 Cloudflare API Shield docs","description":"Identify and address API vulnerabilities with discovery, schema validation, and abuse detection.","url":"https://developers.cloudflare.com/api-shield/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /api-shield/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/1530.md")
</div>
<div class="nb-plan">
<p>Enterprise-only paid add-on</p>
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1529.md")
</aside>
<h2 id="why-care-about-api-security">Why care about API security?</h2>
<p>APIs have become the <a href="https://blog.postman.com/intro-to-apis-history-of-apis/">backbone of popular web services</a>, helping the Internet become more accessible and useful.</p>
<p>As APIs have become more prevalent, however, so have their problems:</p>
<ul>
<li>Many companies have <a href="/api-shield/security/api-discovery/">thousands of APIs</a>, including ones they do not even know about.</li>
<li>To support a large base of users, many APIs are protected by a negative security model that makes them vulnerable to credential-stuffing attacks and automated scanning tools.</li>
<li>With so many endpoints and users, it is difficult to recognize brute-force attacks against <a href="/api-shield/security/volumetric-abuse-detection/">specific endpoints</a>.</li>
<li>Sophisticated attacks are even harder to recognize, often because even development teams are unaware of common and uncommon <a href="/api-shield/security/sequence-analytics/">usage patterns</a>.</li>
</ul>
<p>Refer to the <a href="/api-shield/get-started/">Get started</a> guide to set up API Shield.</p>
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1531.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1532.md")
</div>
<h2 id="use-schema-profiles">Use Schema Profiles</h2>
<p><a href="/waf/detections/application-profiles/">Application Profiles</a> provides a shared detection, analytics, and mitigation model. Schema Profile is its only current profile type.</p>
<p>API Shield provides two Schema Profile sources. <a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">Schema Learning</a> learns from traffic, while <a href="/api-shield/security/schema-validation/">Schema Validation</a> uses uploaded OpenAPI schemas.</p>
<p>Use API Shield for API inventory, OpenAPI governance, profile export, automation, and higher-scale API workflows. Use the WAF Application Profiles pages for Profile Analysis and Custom Rule enforcement.</p>
<h2 id="availability">Availability</h2>
<p>Cloudflare API Security products are available to Enterprise customers only. Anyone can set up <a href="/api-shield/security/mtls/">Mutual TLS</a> with a Cloudflare-managed certificate authority.</p>
<p>The full API Shield security suite is available as an Enterprise paid add-on. Refer to <a href="/api-shield/plans/">API Shield plans</a> for feature-specific availability.</p>
<p>Customers with API Security already have access to Schema Profiles through Schema Learning and Schema Validation. Cloudflare is opening a closed beta to invited Enterprise customers without API Security. Interested customers can contact their account team to express interest. Closed beta access does not imply future plan availability or pricing.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1528.md")
</aside>
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1533.md")
</div>
