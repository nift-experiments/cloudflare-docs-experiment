---
cp9:
  canonical: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/
  description: Upgrade from exposed credentials checks to leaked credentials detection.
  full_title: Upgrade to leaked credentials detection · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Upgrade to leaked credentials detection · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Upgrade from exposed credentials checks to leaked credentials detection."><link rel="canonical" href="https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/index.md"><meta property="og:title" content="Upgrade to leaked credentials detection · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upgrade from exposed credentials checks to leaked credentials detection."><meta property="og:url" content="https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Migration"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/#page","headline":"Upgrade to leaked credentials detection \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Upgrade from exposed credentials checks to leaked credentials detection.","url":"https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Migration"]}</script>
  markdown: true
  noindex: false
  route: /waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/
  schema: 1
---
<p>This guide describes the general steps to upgrade your <a href="/waf/managed-rules/check-for-exposed-credentials/">Exposed Credentials Check</a> configuration to the new <a href="/waf/detections/leaked-credentials/">leaked credentials detection</a>.</p>
<p>Cloudflare recommends that customers update their configuration to use the new leaked credentials detection, which offers the following advantages:</p>
<ul>
<li>Uses a comprehensive database of leaked credentials, containing over 15 billion passwords.</li>
<li>After enabling the detection, you can review the amount of incoming requests containing leaked credentials in Security Analytics, even before creating any mitigation rules.</li>
<li>You can take action on the requests containing leaked credentials using WAF features like rate limiting rules or custom rules.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15638.md")
</aside>
<h2 id="1-turn-off-exposed-credentials-check"><ol>
<li>Turn off Exposed Credentials Check</li>
</ol></h2>
<p>If you had deployed the Cloudflare Exposed Credentials Check managed ruleset:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15639.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15637.md")
</aside>
<h2 id="2-turn-on-leaked-credentials-detection"><ol start="2">
<li>Turn on leaked credentials detection</li>
</ol></h2>
<p>On Free plans, the leaked credentials detection is enabled by default, and no action is required. On paid plans, you can turn on the detection in the Cloudflare dashboard, via API, or using Terraform.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashNewNav"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15644.md")
</div></div>
<h2 id="3-configure-the-actions-to-take"><ol start="3">
<li>Configure the actions to take</li>
</ol></h2>
<p>Based on your previous configuration, do one of the following:</p>
<ul>
<li>If you were using the <a href="/waf/managed-rules/check-for-exposed-credentials/#available-actions">default action</a> in Exposed Credentials Check: Turn on the <a href="/rules/transform/managed-transforms/reference/#add-leaked-credentials-checks-header"><strong>Add Leaked Credentials Checks Header</strong> managed transform</a> that adds the <code>Exposed-Credential-Check</code> header to incoming requests containing leaked credentials. Even though the header name is the same as in Exposed Credentials Check, the header values in the new implementation will vary between <code>1</code> and <code>4</code>.</li>
<li>If you were using a different action: Create a <a href="/waf/custom-rules/">custom rule</a> with an action equivalent to the one you were using. The rule should match <code>User and password leaked is true</code> (if you are using the expression editor, enter <code>(cf.waf.credential_check.username_and_password_leaked)</code>).</li>
</ul>
<hr />
<h2 id="more-resources">More resources</h2>
<ul>
<li>Check for the results of leaked credentials detection in <a href="/waf/analytics/security-analytics/">Security Analytics</a>.</li>
<li>Refer to <a href="/waf/detections/leaked-credentials/examples/">Example mitigation rules</a> for example mitigation strategies you can use when detecting leaked credentials.</li>
</ul>
