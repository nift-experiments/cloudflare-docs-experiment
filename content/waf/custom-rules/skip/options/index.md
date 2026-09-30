---
cp9:
  canonical: https://developers.cloudflare.com/waf/custom-rules/skip/options/
  description: Available skip options for WAF custom rules.
  full_title: Available skip options · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Available skip options · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Available skip options for WAF custom rules."><link rel="canonical" href="https://developers.cloudflare.com/waf/custom-rules/skip/options/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/custom-rules/skip/options/index.md"><meta property="og:title" content="Available skip options · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available skip options for WAF custom rules."><meta property="og:url" content="https://developers.cloudflare.com/waf/custom-rules/skip/options/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/custom-rules/skip/options/#page","headline":"Available skip options \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Available skip options for WAF custom rules.","url":"https://developers.cloudflare.com/waf/custom-rules/skip/options/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/custom-rules/skip/options/
  schema: 1
---
<p>The following sections cover the available skip options in custom rules.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15475.md")
</aside>
<h2 id="skip-the-remaining-custom-rules-current-ruleset">Skip the remaining custom rules (current ruleset)</h2>
<ul>
<li>Dashboard option: <strong>All remaining custom rules</strong></li>
<li>API action parameter: <code>ruleset</code></li>
</ul>
<p>Skips the remaining rules in the current ruleset.</p>
<h2 id="skip-phases">Skip phases</h2>
<ul>
<li>Dashboard options: <strong>All rate limiting rules</strong>, <strong>All Super Bot Fight Mode rules</strong>, and <strong>All managed rules</strong></li>
<li>API action parameter: <code>phases</code></li>
</ul>
<p>Skips the execution of one or more phases. Based on the phases you can skip, this option effectively allows you to skip <a href="/waf/rate-limiting-rules/">rate limiting rules</a>, <a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode rules</a>, and/or <a href="/waf/managed-rules/">WAF Managed Rules</a>.</p>
<p>The phases you can skip are the following:</p>
<ul>
<li><code>http_ratelimit</code></li>
<li><code>http_request_sbfm</code></li>
<li><code>http_request_firewall_managed</code></li>
</ul>
<p>Refer to <a href="/ruleset-engine/about/phases/">Phases</a> for more information.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/15474.md")
</aside>
<h2 id="skip-products">Skip products</h2>
<ul>
<li>API action parameter: <code>products</code></li>
</ul>
<p>Skips specific security products that are not based on the Ruleset Engine. The products you can skip are the following:</p>
<table>
<thead>
<tr>
<th>Product name in the dashboard</th>
<th>API value</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/waf/tools/zone-lockdown/">Zone Lockdown</a></td>
<td><code>zoneLockdown</code></td>
</tr>
<tr>
<td><a href="/waf/tools/user-agent-blocking/">User Agent Blocking</a></td>
<td><code>uaBlock</code></td>
</tr>
<tr>
<td><a href="/waf/tools/browser-integrity-check/">Browser Integrity Check</a></td>
<td><code>bic</code></td>
</tr>
<tr>
<td><a href="/waf/tools/scrape-shield/hotlink-protection/">Hotlink Protection</a></td>
<td><code>hot</code></td>
</tr>
<tr>
<td><a href="/waf/tools/security-level/">Security Level</a></td>
<td><code>securityLevel</code></td>
</tr>
<tr>
<td><a href="/waf/reference/legacy/old-rate-limiting/">Rate limiting rules (Previous version)</a></td>
<td><code>rateLimit</code></td>
</tr>
<tr>
<td><a href="/waf/reference/legacy/old-waf-managed-rules/">Managed rules (Previous version)</a></td>
<td><code>waf</code></td>
</tr>
</tbody>
</table>
<p>The API values in the table are case-sensitive.</p>
<h2 id="skip-the-remaining-custom-rules-current-phase">Skip the remaining custom rules (current phase)</h2>
<ul>
<li>Dashboard option: N/A (currently only available via API)</li>
<li>API action parameter: <code>phase</code></li>
</ul>
<p>Skips all the remaining rules in the current phase. If used in a custom ruleset (at the zone level), it will skip all remaining rules in the custom ruleset, as well as all later rules in the entry point ruleset where the rule executing the custom ruleset was defined.</p>
<p>Currently, this option is only available at the zone level for the <code>http_request_firewall_custom</code> phase. You can use it in custom rulesets or entry point rulesets.</p>
<h2 id="other-options">Other options</h2>
<h3 id="log-requests-matching-the-skip-rule">Log requests matching the skip rule</h3>
<ul>
<li>Dashboard option: <strong>Log matching requests</strong></li>
<li>API action parameter: <code>logging</code> &gt; <code>enabled</code> (boolean, optional)</li>
</ul>
<p>When disabled, Cloudflare will not log any requests matching the current skip rule, and these requests will not appear in <a href="/waf/analytics/security-events/">Security Events</a>.</p>
<p>If you do not specify this option in the API, the default value is <code>true</code> for custom rules with the skip action (logs requests matching the skip rule).</p>
