---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/application-profiles/
  description: Compare requests with application-specific expected structures.
  full_title: Application Profiles · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Application Profiles · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Compare requests with application-specific expected structures."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/application-profiles/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/application-profiles/index.md"><meta property="og:title" content="Application Profiles · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Compare requests with application-specific expected structures."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/application-profiles/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/waf/detections/application-profiles/#page","headline":"Application Profiles \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Compare requests with application-specific expected structures.","url":"https://developers.cloudflare.com/waf/detections/application-profiles/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/detections/application-profiles/
  schema: 1
---
<p>Application Profiles define application-specific expectations and classify requests against them. They add a positive-security model to your existing protections.</p>
<p>Schema Profile is the only current profile type. It models supported request fields, types, formats, ranges, and values.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15544.md")
</aside>
<h2 id="understand-the-profile-lifecycle">Understand the profile lifecycle</h2>
<p>A Schema Profile can come from observed traffic or an uploaded <a href="/api-shield/security/schema-validation/">OpenAPI schema</a>. Both sources produce the same profile type.</p>
<p>An operation is Cloudflare's term for an endpoint identified by HTTP method, hostname pattern, and path pattern. <a href="/security/web-assets/">Web Assets</a> continuously discovers operations, and you can add operations manually.</p>
<p>Discovery and manual creation only add operations to your inventory. Profiling starts when you select <strong>Learn profile</strong> for an operation.</p>
<p>After the profile becomes available, Cloudflare runs an <strong>always-on detection</strong>. The detection classifies requests but does not mitigate traffic.</p>
<p>Review results in <strong>Profile Analysis</strong> before creating a <a href="/waf/custom-rules/">Custom Rule</a>. This keeps detection, investigation, and mitigation as separate steps.</p>
<h2 id="complement-existing-detections">Complement existing detections</h2>
<p>Positive security identifies requests outside your expected application structure. A non-conforming request does not need to match an attack signature.</p>
<p>Application Profiles complement <a href="/waf/managed-rules/">Managed Rules</a>, <a href="/waf/detections/attack-score/">Attack Score</a>, and other negative-security detections. You can combine these signals in Custom Rules.</p>
<h2 id="explore-application-profiles">Explore Application Profiles</h2>
<ul class="directory-listing"><li><a href="/waf/detections/application-profiles/get-started/">Get started</a></li><li><a href="/waf/detections/application-profiles/schema-profiles/">Schema Profiles</a></li><li><a href="/waf/detections/application-profiles/analyze-profile-detections/">Analyze profile detections</a></li><li><a href="/waf/detections/application-profiles/enforce-profiles-with-custom-rules/">Enforce profiles with Custom Rules</a></li><li><a href="/waf/detections/application-profiles/fields/">Fields</a></li></ul>
<h2 id="see-also">See also</h2>
<ul>
<li><a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">Schema learning</a></li>
<li><a href="/api-shield/security/schema-validation/">Schema validation</a></li>
</ul>
