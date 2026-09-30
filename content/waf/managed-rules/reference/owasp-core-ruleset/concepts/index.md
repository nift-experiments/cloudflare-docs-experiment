---
cp9:
  canonical: https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/concepts/
  description: Concepts for the OWASP ModSecurity Core Ruleset on Cloudflare.
  full_title: OWASP ruleset concepts · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>OWASP ruleset concepts · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Concepts for the OWASP ModSecurity Core Ruleset on Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/concepts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/concepts/index.md"><meta property="og:title" content="OWASP ruleset concepts · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Concepts for the OWASP ModSecurity Core Ruleset on Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/concepts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/concepts/#page","headline":"OWASP ruleset concepts \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Concepts for the OWASP ModSecurity Core Ruleset on Cloudflare.","url":"https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/concepts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/managed-rules/reference/owasp-core-ruleset/concepts/
  schema: 1
---
<h2 id="paranoia-level">Paranoia level</h2>
<p>The paranoia level (PL) classifies OWASP rules according to their aggressiveness. Paranoia levels vary from PL1 to PL4, where PL4 is the most strict level:</p>
<ul>
<li>PL1 (default value)</li>
<li>PL2</li>
<li>PL3</li>
<li>PL4</li>
</ul>
<p>Each rule in the OWASP managed ruleset is associated with a paranoia level. Rules associated with higher paranoia levels are considered more aggressive and provide increased protection. However, they might cause more legitimate traffic to get blocked due to false positives.</p>
<p>When you configure the paranoia level of the OWASP ruleset, you are enabling all the rules belonging to all paranoia levels up to the level you select. For example, if you configure the ruleset paranoia level to PL3, you are enabling rules belonging to paranoia levels PL1, PL2, and PL3.</p>
<p>When you set the ruleset paranoia level, the WAF enables the corresponding rules in bulk. You then can disable specific rules individually or by tag, if needed. If you use the highest paranoia level (PL4) you will probably need to disable some of its rules for applications that need to receive complex input patterns.</p>
<h2 id="request-threat-score">Request threat score</h2>
<p>Each OWASP rule that matches the current request has an associated score. The request threat score is the sum of the individual scores of all OWASP rules that matched the request.</p>
<h2 id="score-threshold">Score threshold</h2>
<p>The score threshold (or anomaly threshold) defines the minimum cumulative score — obtained from matching OWASP rules — for the WAF to apply the configured OWASP ruleset action.</p>
<p>The available score thresholds are the following:</p>
<ul>
<li><em>Low – 60 and higher</em></li>
<li><em>Medium – 40 and higher</em> (default value)</li>
<li><em>High – 25 and higher</em></li>
</ul>
<p>Each threshold (<em>Low</em>, <em>Medium</em>, and <em>High</em>) has an associated value (<em>60</em>, <em>40</em>, and <em>25</em>, respectively). Configuring a <em>Low</em> threshold means that more rules will have to match the current request for the WAF to apply the configured ruleset action.</p>
<p>When the OWASP Anomaly Score Threshold is set to <em>High</em>, file uploads may trigger the <code>949110: Inbound Anomaly Score Exceeded</code> rule due to the lower amount of scoring rules needed. Consider <a href="/waf/managed-rules/reference/owasp-core-ruleset/configure-dashboard/#ruleset-level-configuration">adjusting the score threshold</a>, <a href="/waf/managed-rules/reference/owasp-core-ruleset/configure-dashboard/#rule-level-configuration">adjusting individual rules</a> in the ruleset, or <a href="/waf/managed-rules/waf-exceptions/">creating an exception</a> if excessive false positives occur.</p>
<p>For an example, refer to <a href="/waf/managed-rules/reference/owasp-core-ruleset/example/">OWASP evaluation example</a>.</p>
