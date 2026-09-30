---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/application-profiles/enforce-profiles-with-custom-rules/
  description: Mitigate profile violations with scoped Custom Rules.
  full_title: Enforce profiles with Custom Rules · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Enforce profiles with Custom Rules · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Mitigate profile violations with scoped Custom Rules."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/application-profiles/enforce-profiles-with-custom-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/application-profiles/enforce-profiles-with-custom-rules/index.md"><meta property="og:title" content="Enforce profiles with Custom Rules · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Mitigate profile violations with scoped Custom Rules."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/application-profiles/enforce-profiles-with-custom-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/application-profiles/enforce-profiles-with-custom-rules/#page","headline":"Enforce profiles with Custom Rules \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Mitigate profile violations with scoped Custom Rules.","url":"https://developers.cloudflare.com/waf/detections/application-profiles/enforce-profiles-with-custom-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/detections/application-profiles/enforce-profiles-with-custom-rules/
  schema: 1
---
<p>Application Profiles separate detection from mitigation. Cloudflare runs an <strong>always-on detection</strong> after a profile becomes available.</p>
<p>A violation does not block a request automatically. Use a <a href="/waf/custom-rules/">Custom Rule</a> when you are ready to mitigate traffic.</p>
<h2 id="select-a-detection-field">Select a detection field</h2>
<p>Use this expression for learned Schema Profiles:</p>
<pre tabindex="0"><code class="language-txt">cf.schema_validation.learned.violated&#10;</code></pre>
<p>Use this expression for uploaded Schema Profiles:</p>
<pre tabindex="0"><code class="language-txt">cf.schema_validation.uploaded.violated&#10;</code></pre>
<p>Monitor the selected field in <a href="/waf/analytics/security-analytics/">Security Analytics</a> before creating a blocking rule.</p>
<h2 id="scope-by-application">Scope by application</h2>
<p>Limit mitigation to the intended hostname and path:</p>
<pre tabindex="0"><code class="language-txt">cf.schema_validation.learned.violated and http.host eq &quot;api.example.com&quot; and starts_with(http.request.uri.path, &quot;/v1/orders/&quot;)&#10;</code></pre>
<p>Scope mitigation to an operation using its complete identity. Include the HTTP method, hostname, and path:</p>
<pre tabindex="0"><code class="language-txt">cf.schema_validation.learned.violated and http.request.method eq &quot;POST&quot; and http.host eq &quot;api.example.com&quot; and http.request.uri.path eq &quot;/v1/orders&quot;&#10;</code></pre>
<h2 id="combine-security-signals">Combine security signals</h2>
<p>Combine a profile violation with <a href="/waf/detections/attack-score/">Attack Score</a>:</p>
<pre tabindex="0"><code class="language-txt">cf.schema_validation.learned.violated and cf.waf.score lt 20&#10;</code></pre>
<p>Combine an uploaded profile violation with <a href="/bots/concepts/bot-score/">Bot Score</a>:</p>
<pre tabindex="0"><code class="language-txt">cf.schema_validation.uploaded.violated and cf.bot_management.score lt 10&#10;</code></pre>
<h2 id="roll-out-mitigation">Roll out mitigation</h2>
<p>Review production traffic and sampled violation reasons first. Then <a href="/waf/custom-rules/create-dashboard/">create a Custom Rule</a> with a suitable action.</p>
<p>Follow these rollout practices:</p>
<ul>
<li>Start with monitoring in Security Analytics.</li>
<li>Limit the first rule to one operation.</li>
<li>Review the effect before expanding scope.</li>
<li>Recheck profiles after application releases.</li>
<li>Recheck violations after client changes.</li>
</ul>
<p>For field details, refer to <a href="/waf/detections/application-profiles/fields/">Application Profile fields</a>.</p>
