---
cp9:
  canonical: https://developers.cloudflare.com/waf/managed-rules/troubleshooting/
  description: Troubleshoot WAF managed rules false positives and configuration issues.
  full_title: Troubleshoot managed rules · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Troubleshoot managed rules · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot WAF managed rules false positives and configuration issues."><link rel="canonical" href="https://developers.cloudflare.com/waf/managed-rules/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/managed-rules/troubleshooting/index.md"><meta property="og:title" content="Troubleshoot managed rules · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot WAF managed rules false positives and configuration issues."><meta property="og:url" content="https://developers.cloudflare.com/waf/managed-rules/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/managed-rules/troubleshooting/#page","headline":"Troubleshoot managed rules \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Troubleshoot WAF managed rules false positives and configuration issues.","url":"https://developers.cloudflare.com/waf/managed-rules/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /waf/managed-rules/troubleshooting/
  schema: 1
---
<p>By default, WAF's managed rulesets are compatible with most websites and web applications. However, false positives and false negatives may occur:</p>
<ul>
<li><strong>False positives</strong>: Legitimate requests detected and mitigated as malicious.</li>
<li><strong>False negatives</strong>: Malicious requests that were not mitigated and reached your origin server.</li>
</ul>
<h2 id="troubleshoot-false-positives">Troubleshoot false positives</h2>
<p>You can use <a href="/waf/analytics/security-events/">Security Events</a> to help you identify what caused legitimate requests to get blocked. Add filters and adjust the report duration as needed.</p>
<p>To get more detail about which part of a request matched a managed rule, enable <a href="/waf/managed-rules/payload-logging/">payload logging</a> for the affected managed ruleset. Payload logging records the specific string that triggered each rule (encrypted with a key pair that you provide), which helps you confirm whether a match was a false positive. If you have not set it up yet, <a href="/waf/managed-rules/payload-logging/configure/">configure payload logging</a> so that the matched payload is available the next time you investigate a false positive. Payload logging is available on Enterprise plans.</p>
<p>If you encounter a false positive caused by a managed rule, do one of the following:</p>
<ul>
<li>
<p><strong>Add an exception</strong>: <a href="/waf/managed-rules/waf-exceptions/">Exceptions</a> allow you to skip the execution of WAF managed rulesets or some of their rules for certain requests.</p>
</li>
<li>
<p><strong>Adjust the OWASP managed ruleset</strong>: A request blocked by the rule with ID <code class="nb-rule-id" title="6179ae15870a4bb7b2d480d4843b323c">843b323c</code> and description <code>949110: Inbound Anomaly Score Exceeded</code> refers to the <a href="/waf/managed-rules/reference/owasp-core-ruleset/">Cloudflare OWASP Core Ruleset</a>. To resolve the issue, <a href="/waf/managed-rules/reference/owasp-core-ruleset/configure-dashboard/">configure the OWASP managed ruleset</a>.</p>
</li>
<li>
<p><strong>Disable the corresponding managed rule(s)</strong>: Create an override to disable specific rules. This may avoid false positives, but you will also reduce the overall site security. Refer to the <a href="/waf/managed-rules/deploy-zone-dashboard/#configure-a-managed-ruleset">dashboard instructions</a> on configuring a managed ruleset, or to the <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">API instructions</a> on creating an override.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15375.md")
</aside>
<h3 id="additional-recommendations">Additional recommendations</h3>
<ul>
<li>
<p>If one specific rule causes false positives, disable that specific rule and not the entire ruleset.</p>
</li>
<li>
<p>For false positives with the administrator area of your website, add an <a href="/waf/managed-rules/waf-exceptions/">exception</a> disabling a managed rule for the admin section of your site resources. You can use an expression similar to the following:</p>
<p><code>http.host eq &quot;example.com&quot; and starts_with(http.request.uri.path, &quot;/admin&quot;)</code></p>
</li>
<li>
<p>WAF managed rulesets are designed to inspect standard HTTP request content. Requests that upload binary content (for example, file uploads) can resemble attack payloads and cause false positives. To scan file uploads for malicious content, use <a href="/waf/detections/malicious-uploads/">Malicious uploads detection</a> instead of relying on managed rules for that traffic.</p>
</li>
</ul>
<h2 id="troubleshoot-false-negatives">Troubleshoot false negatives</h2>
<p>To identify false negatives, review the HTTP logs on your origin server.</p>
<p>To reduce false negatives, use the following checklist:</p>
<ul>
<li>
<p>Are DNS records that serve HTTP traffic <a href="/dns/proxy-status/">proxied through Cloudflare</a>?<br/>
Cloudflare only mitigates requests in proxied traffic.</p>
</li>
<li>
<p>Have you deployed any of the <a href="/waf/managed-rules/#available-managed-rulesets">WAF managed rulesets</a> in your zone?<br/>
You must <a href="/waf/managed-rules/deploy-zone-dashboard/#deploy-a-managed-ruleset">deploy a managed ruleset</a> to apply its rules.</p>
</li>
<li>
<p>Are Managed Rules being skipped via an <a href="/waf/managed-rules/waf-exceptions/">exception</a>?<br/>
Use <a href="/waf/analytics/security-events/">Security Events</a> to search for requests being skipped. If necessary, adjust the exception expression so that it matches the attack traffic that should have been blocked.</p>
</li>
<li>
<p>Have you enabled any necessary managed rules that are not enabled by default?<br/>
Not all rules of WAF managed rulesets are enabled by default, so you should review individual managed rules.</p>
<ul>
<li>For example, Cloudflare allows requests with empty user agents by default. To block requests with an empty user agent, enable the rule with ID <code class="nb-rule-id" title="b57df4f17f7f4ea4b8db33e20a6dbbd3">0a6dbbd3</code> in the Cloudflare Managed Ruleset.</li>
<li>Another example: If you want to block unmitigated SQL injection (SQLi) attacks, make sure the relevant managed rules tagged with <code>sqli</code> are enabled in the Cloudflare Managed Ruleset.</li>
</ul>
<p>For instructions, refer to <a href="/waf/managed-rules/deploy-zone-dashboard/#configure-a-managed-ruleset">Configure a managed ruleset</a>.</p>
</li>
<li>
<p>Is the attack traffic matching a custom rule <a href="/waf/custom-rules/skip/">skipping all Managed Rules</a>?<br/>
If necessary, adjust the custom rule expression so that it does not apply to the attack traffic.</p>
</li>
<li>
<p>Is the attack traffic matching an allowed ASN, IP range, or IP address in <a href="/waf/tools/ip-access-rules/">IP Access rules</a>?<br/>
Review your IP Access rules and make sure that any allow rules do not match the attack traffic.</p>
</li>
<li>
<p>Is the malicious traffic reaching your origin IP addresses directly, therefore bypassing Cloudflare protection?<br/>
Block all traffic except from <a href="/fundamentals/concepts/cloudflare-ip-addresses/">Cloudflare's IP addresses</a> at your origin server.</p>
</li>
</ul>
<h3 id="additional-recommendations-1">Additional recommendations</h3>
<p>If WAF's managed rulesets do not detect a specific attack pattern after verifying the above, consider the following:</p>
<ul>
<li>
<p>Use <a href="/waf/detections/attack-score/">WAF attack score</a> to complement signature-based managed rules with machine-learning detection. Attack score classifies each request with a score indicating the likelihood it is malicious, even when no managed rule matches.</p>
</li>
<li>
<p>Create a <a href="/waf/custom-rules/">custom rule</a> to block the specific attack pattern. Use fields such as URI path, query string, or HTTP request headers to match the malicious requests.</p>
</li>
</ul>
