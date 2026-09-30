---
cp9:
  canonical: https://developers.cloudflare.com/waf/managed-rules/payload-logging/
  description: Log the request content that triggered a managed ruleset match.
  full_title: Log the payload of matched rules · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Log the payload of matched rules · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Log the request content that triggered a managed ruleset match."><link rel="canonical" href="https://developers.cloudflare.com/waf/managed-rules/payload-logging/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/managed-rules/payload-logging/index.md"><meta property="og:title" content="Log the payload of matched rules · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Log the request content that triggered a managed ruleset match."><meta property="og:url" content="https://developers.cloudflare.com/waf/managed-rules/payload-logging/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Logging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/managed-rules/payload-logging/#page","headline":"Log the payload of matched rules \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Log the request content that triggered a managed ruleset match.","url":"https://developers.cloudflare.com/waf/managed-rules/payload-logging/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Logging"]}</script>
  markdown: true
  noindex: false
  route: /waf/managed-rules/payload-logging/
  schema: 1
---
<p>The WAF allows you to log the request information that triggered a specific rule of a managed ruleset. This information is known as the payload. Payload information includes the specific string that triggered the rule, along with the text that appears immediately before and after the match.</p>
<p>Payload logging is especially useful when diagnosing the behavior of WAF rules. Since the values that triggered a rule may contain sensitive data, they are encrypted with a customer-provided public key so that only you can examine them later.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15630.md")
</aside>
<h2 id="turn-on-payload-logging">Turn on payload logging</h2>
<p>Each managed ruleset has its own payload logging configuration. To turn on payload logging, configure a public key to encrypt the logged payload by doing one of the following:</p>
<ul>
<li>Generate a key pair directly in the Cloudflare dashboard</li>
<li>Use your own public key</li>
</ul>
<p>Once enabled, the WAF saves the payload of rule matches for the managed ruleset configured with payload logging, encrypting the payload with your public key. If multiple rules checking the same request field match (for example, for the field <code>http.cookie</code>), the logged payload for that field will refer to the last matched rule.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/15629.md")
</aside>
<p>For more information, refer to <a href="/waf/managed-rules/payload-logging/configure/">Configure payload logging in the dashboard</a> or <a href="/waf/managed-rules/payload-logging/configure-api/">Configure payload logging via API</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important-1">Important</h3>
@markup("md", "content/.markup/bodies/15628.md")
</aside>
<h2 id="view-payload-content">View payload content</h2>
<p>To view the content of the payload in clear text, do one of the following:</p>
<ul>
<li>In the <a href="/waf/analytics/security-events/">Security Events</a> page, enter your private key to decrypt the payload of a log entry directly in the browser. Refer to <a href="/waf/managed-rules/payload-logging/view/">View the payload content in the dashboard</a> for details.</li>
<li>Decrypt the payload in the command line using the <code>matched-data-cli</code> tool. Refer to <a href="/waf/managed-rules/payload-logging/command-line/decrypt-payload/">Decrypt the payload content in the command line</a> for details.</li>
<li>Decrypt the matched payload in your <a href="/logs/logpush/">Logpush</a> job using a Worker before storing the logs in your <span class="nb-glossary-tooltip" title="SIEM">SIEM system</span>. Refer to <a href="/waf/managed-rules/payload-logging/decrypt-in-logs/">Store decrypted matched payloads in logs</a> for details.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important-2">Important</h3>
@markup("md", "content/.markup/bodies/15627.md")
</aside>
<h2 id="user-role-requirements">User role requirements</h2>
<p>Only users with the <a href="/fundamentals/manage-members/roles/">Super Administrator role</a> can enable payload logging or edit the payload logging configuration.</p>
