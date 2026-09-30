---
cp9:
  canonical: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/
  description: Detect login requests using credentials from known data breaches.
  full_title: Check for exposed credentials · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Check for exposed credentials · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Detect login requests using credentials from known data breaches."><link rel="canonical" href="https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/index.md"><meta property="og:title" content="Check for exposed credentials · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Detect login requests using credentials from known data breaches."><meta property="og:url" content="https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Authentication,Account takeover"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/#page","headline":"Check for exposed credentials \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Detect login requests using credentials from known data breaches.","url":"https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Authentication","Account takeover"]}</script>
  markdown: true
  noindex: false
  route: /waf/managed-rules/check-for-exposed-credentials/
  schema: 1
---
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/15649.md")
</aside>
<p>Many web applications have suffered <span class="nb-glossary-tooltip" title="credential stuffing">credential stuffing</span> attacks in the recent past. In these attacks there is a massive number of login attempts using username/password pairs from databases of <span class="nb-glossary-tooltip" title="leaked credentials">exposed credentials</span>.</p>
<p>Cloudflare offers you automated checks for exposed credentials using Cloudflare Web Application Firewall (WAF).</p>
<p>The WAF provides two mechanisms for this check:</p>
<ul>
<li>
<p>The <a href="/waf/managed-rules/reference/exposed-credentials-check/">Exposed Credentials Check Managed Ruleset</a>, which contains predefined rules for popular CMS applications. By enabling this ruleset for a given zone, you immediately enable checks for exposed credentials for these well-known applications. The managed ruleset is available to all paid plans.</p>
</li>
<li>
<p>The ability to <a href="#exposed-credentials-checks-in-custom-rules">write custom rules</a> at the account level that check for exposed credentials according to your criteria. This configuration option is available to Enterprise customers with a paid add-on.</p>
</li>
</ul>
<p>Cloudflare updates the databases of exposed credentials supporting the exposed credentials check feature on a regular basis.</p>
<p>The username and password credentials in clear text never leave the Cloudflare network. The WAF only uses an anonymized version of the username and password when determining if there are previously exposed credentials. Cloudflare follows the approach based on the <em>k</em>-Anonymity mathematical property described in the following blog post: <a href="https://blog.cloudflare.com/validating-leaked-passwords-with-k-anonymity/">Validating Leaked Passwords with k-Anonymity</a>.</p>
<h2 id="available-actions">Available actions</h2>
<p>The WAF can perform one of the following actions when it detects exposed credentials:</p>
<ul>
<li><strong>Exposed-Credential-Check Header</strong>: Adds a new HTTP header to HTTP requests with exposed credentials. Your application at the origin can then force a password reset, start a two-factor authentication process, or perform any other action. The name of the added HTTP header is <code>Exposed-Credential-Check</code> and its value is <code>1</code>. The action name is <code>Rewrite</code> in <a href="/waf/analytics/security-events/">Security Events</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15648.md")
</aside>
<ul>
<li><strong>Non-Interactive Challenge</strong>: Presents a non-interactive challenge to the clients making HTTP requests with exposed credentials.</li>
<li><strong>Managed Challenge</strong>: Helps reduce the lifetimes of human time spent solving CAPTCHAs across the Internet. Depending on the characteristics of a request, Cloudflare will dynamically choose the appropriate type of challenge based on specific criteria.</li>
<li><strong>Block</strong>: Blocks HTTP requests containing exposed credentials.</li>
<li><strong>Log</strong>: Only available on Enterprise plans. Logs requests with exposed credentials in the Cloudflare logs. Recommended for validating a rule before committing to a more severe action.</li>
<li><strong>Interactive Challenge</strong>: Presents an interactive challenge to the clients making HTTP requests with exposed credentials.</li>
</ul>
<p>The default action for the rules in the Exposed Credentials Check Managed Ruleset is <em>Exposed-Credential-Check Header</em> (named <code>rewrite</code> in the API).</p>
<p>Cloudflare recommends that you only use the following actions: <em>Exposed-Credential-Check Header</em> (named <code>rewrite</code> in the API) and <em>Log</em> (<code>log</code>).</p>
<h2 id="exposed-credentials-checks-in-custom-rules">Exposed credentials checks in custom rules</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15647.md")
</aside>
<p>Besides enabling the <a href="/waf/managed-rules/reference/exposed-credentials-check/">Exposed Credentials Check Managed Ruleset</a>, you can also check for exposed credentials in <a href="/waf/custom-rules/">custom rules</a>. One common use case is to create custom rules on the end user authentication endpoints of your application to check for exposed credentials. Rules that check for exposed credentials run before rate limiting rules.</p>
<p>To check for exposed credentials in a custom rule, include the exposed credentials check in the rule definition at the account level and specify how to obtain the username and password values from the HTTP request. For more information, refer to <a href="/waf/managed-rules/check-for-exposed-credentials/configure-api/#create-a-custom-rule-checking-for-exposed-credentials">Create a custom rule checking for exposed credentials</a>.</p>
