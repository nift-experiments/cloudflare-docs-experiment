---
cp9:
  canonical: https://developers.cloudflare.com/waf/managed-rules/
  description: Documentation for the previous version of WAF managed rules.
  full_title: WAF managed rules (previous version) · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>WAF managed rules (previous version) · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Documentation for the previous version of WAF managed rules."><link rel="canonical" href="https://developers.cloudflare.com/waf/managed-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/reference/legacy/old-waf-managed-rules/index.md"><meta property="og:title" content="WAF managed rules (previous version) · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Documentation for the previous version of WAF managed rules."><meta property="og:url" content="https://developers.cloudflare.com/waf/reference/legacy/old-waf-managed-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/managed-rules/#page","headline":"WAF managed rules (previous version) \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Documentation for the previous version of WAF managed rules.","url":"https://developers.cloudflare.com/waf/managed-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/reference/legacy/old-waf-managed-rules/
  schema: 1
---
<p>Managed rules, a feature of Cloudflare WAF (Web Application Firewall), identifies and removes suspicious activity for HTTP <code>GET</code> and <code>POST</code> requests.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15688.md")
</aside>
<p>Examples of <a href="https://www.cloudflare.com/learning/security/what-is-web-application-security/">malicious content</a> that managed rules identify include:</p>
<ul>
<li>Common keywords used in comment spam (<code>XX</code>, <code>Rolex</code>, <code>Viagra</code>, etc.)</li>
<li>Cross-site scripting attacks (XSS)</li>
<li>SQL injections (SQLi)</li>
</ul>
<p>WAF managed rules (previous version) are available to Pro, Business, and Enterprise plans for any <a href="/dns/proxy-status/">subdomains proxied to Cloudflare</a>. Control managed rules settings in <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Managed rules</strong>. </p>
<p>Managed rules includes three packages:</p>
<ul>
<li><a href="#cloudflare-managed-ruleset">Cloudflare Managed Ruleset</a></li>
<li><a href="#owasp-modsecurity-core-rule-set">OWASP ModSecurity Core Rule Set</a></li>
<li>Customer requested rules</li>
</ul>
<p>You can use the sampled logs in the <a href="/waf/analytics/security-events/">Security Events</a> dashboard to review threats blocked by WAF managed rules.</p>
<hr />
<h2 id="cloudflare-managed-ruleset">Cloudflare Managed Ruleset</h2>
<p>The Cloudflare Managed Ruleset contains security rules written and curated by Cloudflare. Select a ruleset name under <strong>Group</strong> to reveal the rule descriptions.</p>
<p><strong>Cloudflare Specials</strong> is a group that provides core firewall security against <a href="https://www.cloudflare.com/learning/security/what-is-web-application-security/">common attacks</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15687.md")
</aside>
<p>When viewing a ruleset, Cloudflare shows default actions for each rule listed under <strong>Default mode</strong>. The <strong>Mode</strong> available for individual rules within a specific <strong>Cloudflare Managed Ruleset</strong> are:</p>
<ul>
<li><strong>Default</strong>: Takes the default action listed under <strong>Default mode</strong> when viewing a specific rule.</li>
<li><strong>Disable</strong>: Turns off the specific rule within the group.</li>
<li><strong>Block</strong>: Discards the request.</li>
<li><strong>Interactive Challenge</strong>: The visitor receives a challenge page that requires interaction.</li>
<li><strong>Simulate</strong>: The request is allowed through but is logged in <a href="/waf/analytics/security-events/#sampled-logs">sampled logs</a>.</li>
</ul>
<p>Cloudflare's <a href="/waf/change-log/">WAF changelog</a> allows customers to monitor ongoing changes to the Cloudflare Managed Ruleset.</p>
<hr />
<h2 id="owasp-modsecurity-core-rule-set">OWASP ModSecurity Core Rule Set</h2>
<p>The OWASP ModSecurity Core Rule Set package assigns a score to each request based on how many OWASP rules trigger. Some OWASP rules have a higher sensitivity score than others.</p>
<p>After OWASP evaluates a request, Cloudflare compares the final score to the <strong>Sensitivity</strong> configured for the zone.  If the score exceeds the sensitivity, the request is actioned based on the <strong>Action</strong> configured within <strong>Package: OWASP ModSecurity Core Rule Set</strong>:</p>
<ul>
<li><strong>Block</strong>: The request is discarded.</li>
<li><strong>Challenge</strong>: The visitor receives an interactive challenge page.</li>
<li><strong>Simulate</strong>: The request is allowed through but is logged in <a href="/waf/analytics/security-events/#sampled-logs">sampled logs</a>.</li>
</ul>
<p>The sensitivity score required to trigger the WAF for a specific <strong>Sensitivity</strong> is as follows:</p>
<ul>
<li><strong>Low</strong>: 60 and higher</li>
<li><strong>Medium</strong>: 40 and higher</li>
<li><strong>High</strong>: 25 and higher</li>
</ul>
<p>For AJAX requests, the following scores are applied instead:</p>
<ul>
<li><strong>Low</strong>: 120 and higher</li>
<li><strong>Medium</strong>: 80 and higher</li>
<li><strong>High</strong>: 65 and higher</li>
</ul>
<p>Review the entry in <a href="/waf/analytics/security-events/#sampled-logs">sampled logs</a> for the final score and for the individual triggered rules.</p>
<h3 id="control-the-owasp-package">Control the OWASP package</h3>
<p>The OWASP ModSecurity Core Rule Set package contains several rules from the <a href="https://www.owasp.org/index.php/Category:OWASP_ModSecurity_Core_Rule_Set_Project">OWASP project</a>. Cloudflare does not write or curate OWASP rules. Unlike the Cloudflare Managed Ruleset, specific OWASP rules are either turned <em>On</em> or <em>Off.</em></p>
<p>To manage OWASP thresholds, set the <strong>Sensitivity</strong> to <em>Low</em>, <em>Medium</em>, or <em>High</em> under <strong>Package: OWASP ModSecurity Core Rule Set</strong>.</p>
<p>Setting the <strong>Sensitivity</strong> to <em>Off</em> will disable the entire OWASP package including all its rules. Determining the appropriate <strong>Sensitivity</strong> depends on your business industry and operations. For instance, a <em>Low</em> setting is appropriate for:</p>
<ul>
<li>Certain business industries more likely to trigger the WAF.</li>
<li>Large file uploads.</li>
</ul>
<p>With a high sensitivity, large file uploads will trigger the WAF.</p>
<p>Cloudflare recommends initially setting the sensitivity to <em>Low</em> and reviewing for false positives before further increasing the sensitivity.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15686.md")
</aside>
<hr />
<h2 id="important-remarks">Important remarks</h2>
<ul>
<li>
<p>Managed rules introduce a limited amount of latency.</p>
</li>
<li>
<p>Changes to WAF managed rules take about 30 seconds to update globally.</p>
</li>
<li>
<p>Cloudflare uses proprietary rules to filter traffic.</p>
</li>
<li>
<p>Established Websockets do not trigger managed rules for subsequent requests.</p>
</li>
<li>
<p>Managed rules parse JSON responses to identify vulnerabilities targeted at APIs. JSON payload parsing is limited to 128 KB.</p>
</li>
<li>
<p>Managed rules mitigate padding techniques. Cloudflare recommends the following:</p>
<ol>
<li>
<p>Turn on rule with ID <code>100048</code>. This rule protects against padding type attacks, but it is not deployed by default because there is a high probability of causing false positives in customer environments. It is, however, important that customers tune their managed rules configuration.</p>
</li>
<li>
<p>Create a WAF custom rule using the <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor">Expression Editor</a> depending on the need to check headers and/or body to block larger payloads (&gt; 128 KB). Use the following fields for this purpose:</p>
<ul>
<li><a href="/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/"><code>http.request.body.truncated</code></a></li>
<li><a href="/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/"><code>http.request.headers.truncated</code></a></li>
</ul>
<p>You should test your rule in <em>Log</em> mode first (if available), since the rule might generate false positives.</p>
</li>
</ol>
</li>
<li>
<p>There are a handful of managed rules that Cloudflare does not disable even if you turn off <strong>Managed rules</strong> in the Cloudflare dashboard, such as rules with IDs <code>WP0025B</code>, <code>100043A</code>, and <code>100030</code>.</p>
</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/waf/reference/legacy/old-waf-managed-rules/troubleshooting/">Troubleshoot WAF managed rules (previous version)</a></li>
<li><a href="/waf/analytics/security-events/">Security Events</a></li>
<li><a href="/waf/">Cloudflare WAF</a></li>
<li><a href="/waf/change-log/">Cloudflare's WAF changelog</a></li>
<li><a href="/waf/custom-rules/">WAF custom rules</a></li>
</ul>
