---
cp9:
  canonical: https://developers.cloudflare.com/waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user/
  description: Use JWT claims and attack scores to protect admin users.
  full_title: Issue challenge for admin user in JWT claim based on attack score · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Issue challenge for admin user in JWT claim based on attack score · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Use JWT claims and attack scores to protect admin users."><link rel="canonical" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user/index.md"><meta property="og:title" content="Issue challenge for admin user in JWT claim based on attack score · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use JWT claims and attack scores to protect admin users."><meta property="og:url" content="https://developers.cloudflare.com/waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="JSON web token (JWT)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user/#page","headline":"Issue challenge for admin user in JWT claim based on attack score \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Use JWT claims and attack scores to protect admin users.","url":"https://developers.cloudflare.com/waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JSON web token (JWT)"]}</script>
  markdown: true
  noindex: false
  route: /waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15470.md")
</aside>
<p>This example configures additional protection for requests with a JSON Web Token (JWT) with a user claim of <code>admin</code>, based on the request's <a href="/waf/detections/attack-score/">attack score</a>.</p>
<p><a href="/waf/custom-rules/create-dashboard/">Create a custom rule</a> that issues a Managed Challenge if the user claim in a JWT is <code>admin</code> and the attack score is below 40.</p>
<ul>
<li>
<p><strong>When incoming requests match</strong></p>
<p>Use the expression editor:<br/>
<code>(lookup_json_string(http.request.jwt.claims[&quot;&lt;TOKEN_CONFIGURATION_ID&gt;&quot;][0], &quot;user&quot;) eq &quot;admin&quot; and cf.waf.score &lt; 40)</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Managed Challenge</em></p>
</li>
</ul>
<p>In this example, <code>&lt;TOKEN_CONFIGURATION_ID&gt;</code> is your <a href="/api-shield/security/jwt-validation/api/">token configuration ID</a> found in JWT Validation and <code>user</code> is the JWT claim.</p>
