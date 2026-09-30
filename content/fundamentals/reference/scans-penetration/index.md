---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/scans-penetration/
  description: Understand Cloudflare's policy for conducting vulnerability scans and penetration tests on your own zones and assets.
  full_title: Scans and penetration testing policy · Cloudflare Fundamentals docs
  head_html: <title>Scans and penetration testing policy · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand Cloudflare&#x27;s policy for conducting vulnerability scans and penetration tests on your own zones and assets."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/scans-penetration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/scans-penetration/index.md"><meta property="og:title" content="Scans and penetration testing policy · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand Cloudflare&#x27;s policy for conducting vulnerability scans and penetration tests on your own zones and assets."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/scans-penetration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/scans-penetration/#page","headline":"Scans and penetration testing policy \u00b7 Cloudflare Fundamentals docs","description":"Understand Cloudflare's policy for conducting vulnerability scans and penetration tests on your own zones and assets.","url":"https://developers.cloudflare.com/fundamentals/reference/scans-penetration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/scans-penetration/
  schema: 1
---
<p>Customers may conduct scans and penetration tests (with certain restrictions) on application and network-layer aspects of their own assets, such as their <a href="/fundamentals/concepts/accounts-and-zones/#zones">zones</a> within their Cloudflare accounts, provided they adhere to Cloudflare's policy.</p>
<h2 id="permitted-targets">Permitted targets</h2>
<p>All scans or testing must be limited to the following:</p>
<ul>
<li>Customer-owned IPs</li>
<li>Cloudflare's designated public IPs</li>
<li>The customer's registered DNS entries</li>
</ul>
<p>Targets like <code>*.cloudflare.com</code> or other Cloudflare-owned destinations are only allowed as part of Cloudflare's Public Bug Bounty program. Refer to the <a href="#additional-resources">Additional resources</a> section for more information.</p>
<h2 id="scans">Scans</h2>
<ul>
<li><strong>Throttling</strong>: Scans should be throttled to a reasonable rate to prevent disruptions and ensure stable system performance.</li>
<li><strong>Scope and intent</strong>: Scans should identify the presence of vulnerabilities without attempting to actively exploit any detected weaknesses.</li>
<li><strong>Exclusions</strong>: It is recommended to exclude <a href="/fundamentals/reference/cdn-cgi-endpoint/"><code>/cdn-cgi/</code> endpoints</a> from scans to avoid false positives or irrelevant results.</li>
<li><strong>Compliance checks</strong>: Customers may conduct <a href="/fundamentals/security/pci-scans/">PCI compliance scans</a> or verify that <a href="/ssl/reference/compliance-and-vulnerabilities/#known-vulnerabilities-mitigations">known vulnerabilities</a> have been addressed.</li>
</ul>
<h2 id="penetration-tests">Penetration tests</h2>
<p>Before starting a penetration test on your <a href="/fundamentals/concepts/accounts-and-zones/#zones">zones</a>, set the following application security configurations for each zone you will run the test on:</p>
<ol>
<li>
<p><a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/#deploy-in-the-dashboard">Deploy the Cloudflare Managed Ruleset</a> and
<a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/#ruleset-level-configuration">enable all rules</a> in the ruleset by setting <strong>Ruleset status</strong> to <strong>Enabled</strong>.</p>
</li>
<li>
<p><a href="/waf/managed-rules/reference/owasp-core-ruleset/configure-dashboard/#deploy-in-the-dashboard">Deploy the Cloudflare OWASP Core Ruleset</a> and set the following <a href="/waf/managed-rules/reference/owasp-core-ruleset/configure-dashboard/#ruleset-level-configuration">ruleset configuration</a>:</p>
<ul>
<li><strong>Paranoia Level</strong>: <em>PL4</em></li>
<li><strong>Score threshold</strong>: <em>High - 25 and higher</em></li>
</ul>
</li>
<li>
<p><a href="/waf/custom-rules/create-dashboard/">Create a custom rule</a> based on the <a href="/waf/detections/attack-score/">WAF attack score</a> to block requests considered as an attack (WAF attack score between 1 and 20). Refer to the <a href="/waf/detections/attack-score/#1-create-a-custom-rule">WAF attack score</a> documentation for an example.</p>
</li>
<li>
<p><a href="/waf/custom-rules/create-dashboard/">Create a custom rule</a> based on <a href="/waf/detections/malicious-uploads/">malicious uploads detection</a> to block requests containing <span class="nb-glossary-tooltip" title="content object">content objects</span> considered malicious. Refer to <a href="/waf/detections/malicious-uploads/example-rules/#block-requests-to-uri-path-with-a-malicious-content-object">Example rules</a> for examples of custom rules used to mitigate this kind of threat.</p>
</li>
<li>
<p>On Pro and Business plans without Bot Management, <a href="/bots/get-started/super-bot-fight-mode/#enable-super-bot-fight-mode">enable Super Bot Fight Mode</a>.<br/>
Customers with access to Bot Management should make sure that <a href="/bots/get-started/bot-management/#enable-bot-management-for-enterprise">Bot Management is enabled</a> (it is enabled by default on entitled zones).</p>
</li>
<li>
<p><a href="/waf/rate-limiting-rules/create-zone-dashboard/">Create rate limiting rules</a> to protect key endpoints of the zone being tested. Refer to <a href="/waf/rate-limiting-rules/use-cases/">Rate limiting rule examples</a> and <a href="/waf/rate-limiting-rules/best-practices/">Rate limiting best practices</a> for example configurations.</p>
</li>
</ol>
<p>Be aware that other Cloudflare security and performance features, configurations, and rules active on your account or zone can influence test results.</p>
<p>After completing the test, it is recommended that you review your security posture and make any necessary adjustments based on the findings.</p>
<h3 id="important-remarks">Important remarks</h3>
<ul>
<li>
<p>Cloudflare's <a href="/fundamentals/concepts/how-cloudflare-works/">anycast network</a> will report ports other than <code>80</code> and <code>443</code> as open due to its shared infrastructure and the nature of Cloudflare's proxy. The reporting is expected behavior and does not indicate a vulnerability.</p>
</li>
<li>
<p>Tools like Netcat may list <a href="/fundamentals/reference/network-ports/">non-standard HTTP ports</a> as open; however, these ports are open solely for Cloudflare's routing purposes and do not necessarily indicate that a connection can be established with the customer's origin over those ports.</p>
</li>
<li>
<p><strong>Known false positives</strong>: Any findings related to the <a href="/ssl/reference/compliance-and-vulnerabilities/#return-of-bleichenbachers-oracle-threat-robot">ROBOT vulnerability</a> are false positives when the customer's assets are behind Cloudflare.</p>
</li>
</ul>
<h2 id="denial-of-service-dos-tests">Denial-of-Service (DoS) tests</h2>
<p>For guidelines on required notification and necessary information, refer to <a href="/ddos-protection/reference/simulate-ddos-attack/">Simulating test DDoS attacks</a>. Customers should also familiarize themselves with Cloudflare's <a href="/ddos-protection/best-practices/">DDoS protection best practices</a>.</p>
<h2 id="additional-resources">Additional resources</h2>
<ul>
<li>Customers can download the latest Penetration Test Report of Cloudflare via the <a href="/fundamentals/reference/policies-compliances/compliance-docs/">dashboard</a>.</li>
<li>For information about Cloudflare's Public Bug Bounty program, visit <a href="https://hackerone.com/cloudflare">HackerOne</a>.</li>
</ul>
