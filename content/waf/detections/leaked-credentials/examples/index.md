---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/leaked-credentials/examples/
  description: Examples of rules for mitigating requests containing leaked credentials.
  full_title: Leaked credentials example mitigation rules · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Leaked credentials example mitigation rules · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Examples of rules for mitigating requests containing leaked credentials."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/leaked-credentials/examples/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/leaked-credentials/examples/index.md"><meta property="og:title" content="Leaked credentials example mitigation rules · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Examples of rules for mitigating requests containing leaked credentials."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/leaked-credentials/examples/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Leaked credentials detection"><meta name="pcx_tags" content="Account takeover"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/leaked-credentials/examples/#page","headline":"Leaked credentials example mitigation rules \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Examples of rules for mitigating requests containing leaked credentials.","url":"https://developers.cloudflare.com/waf/detections/leaked-credentials/examples/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Account takeover"]}</script>
  markdown: true
  noindex: false
  route: /waf/detections/leaked-credentials/examples/
  schema: 1
---
<h2 id="rate-limit-suspicious-logins-with-leaked-credentials">Rate limit suspicious logins with leaked credentials</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15535.md")
</aside>
<p><a href="/waf/rate-limiting-rules/create-zone-dashboard/">Create a rate limiting rule</a> using <a href="/bots/additional-configurations/detection-ids/account-takeover-detections/">account takeover (ATO) detection</a> and leaked credentials fields to limit volumetric attacks from particular IP addresses, JA4 Fingerprints, or countries.</p>
<p>The following example rule applies rate limiting to requests with a specific <a href="/bots/additional-configurations/detection-ids/account-takeover-detections/">ATO detection ID</a> (corresponding to <code>Observes all login traffic to the zone</code>) that contain a previously leaked username and password:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/15536.md")
</div>
<h2 id="challenge-requests-containing-leaked-credentials">Challenge requests containing leaked credentials</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15534.md")
</aside>
<p><a href="/waf/custom-rules/create-dashboard/">Create a custom rule</a> that challenges requests containing a previously leaked set of credentials (username and password).</p>
<ul>
<li><strong>Expression</strong>: If you use the Expression Builder, configure the following expression:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>User and Password Leaked</td>
<td>equals</td>
<td>True</td>
</tr>
</tbody>
</table>
<p>If you use the Expression Editor, enter the following expression:</p>
<pre tabindex="0"><code class="language-txt">(cf.waf.credential_check.username_and_password_leaked)&#10;</code></pre>
<ul>
<li><strong>Action</strong>: <em>Managed Challenge</em></li>
</ul>
<hr />
