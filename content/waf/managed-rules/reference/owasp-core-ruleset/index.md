---
cp9:
  canonical: https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/
  description: Configure the Cloudflare OWASP Core Ruleset for your zone.
  full_title: Cloudflare OWASP Core Ruleset · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Cloudflare OWASP Core Ruleset · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure the Cloudflare OWASP Core Ruleset for your zone."><link rel="canonical" href="https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/index.md"><meta property="og:title" content="Cloudflare OWASP Core Ruleset · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure the Cloudflare OWASP Core Ruleset for your zone."><meta property="og:url" content="https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/#page","headline":"Cloudflare OWASP Core Ruleset \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Configure the Cloudflare OWASP Core Ruleset for your zone.","url":"https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/managed-rules/reference/owasp-core-ruleset/
  schema: 1
---
<p>The Cloudflare OWASP Core Ruleset is Cloudflare's implementation of the <a href="https://owasp.org/www-project-modsecurity-core-rule-set/">OWASP ModSecurity Core Rule Set</a> (CRS) version {owaspCrsVersion}.</p>
<p>The Cloudflare OWASP Core Ruleset is designed to work as a single entity to calculate a <a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#request-threat-score">threat score</a> and execute an action based on that score. When a rule in the ruleset matches a request, the threat score increases according to the rule score. If the final threat score is greater than the configured <a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#score-threshold">score threshold</a>, Cloudflare executes the action configured in the last rule of the ruleset.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15664.md")
</aside>
<h2 id="owasp-top-10-versus-cloudflare-rulesets">OWASP Top 10 versus Cloudflare Rulesets</h2>
<p>The Cloudflare OWASP Core Ruleset is Cloudflare's implementation of the OWASP ModSecurity Core Rule Set version {owaspCrsVersion}, which is different from the <a href="https://owasp.org/www-project-top-ten/">OWASP Top 10</a>.</p>
<p>The <a href="https://owasp.org/www-project-top-ten/">OWASP Top 10</a> is a list of the most severe application security risks, designed to raise awareness among practitioners and developers. While some risks can be addressed by a web application firewall, others require different solutions or must be mitigated during application development. Specifically:</p>
<ul>
<li>Cryptographic Failures</li>
<li>Insecure Design</li>
<li>Identification and Authentication Failures</li>
<li>Security Logging and Monitoring Failures</li>
</ul>
<p>These risks depend more on how the application is built or how the entire monitoring pipeline is set up.</p>
<h3 id="cloudflare-products-versus-owasp-top-10">Cloudflare products versus OWASP Top 10</h3>
<p>While both the Cloudflare Managed Ruleset and OWASP CRS aim to mitigate several categories of the OWASP Top 10, their approaches differ. OWASP CRS v3.3 is a generalized, &quot;scoring-based&quot; open-source ruleset that often requires manual tuning. In contrast, the Cloudflare Managed Ruleset is a proprietary, signature-heavy engine backed by Cloudflare's massive global threat intelligence. Furthermore, Cloudflare rapidly deploys protections for new CVEs through its managed ruleset, whereas the OWASP CRS remains relatively static.</p>
<p>The following table outlines how Cloudflare products map to the OWASP categories.</p>
<table>
<thead>
<tr>
<th>OWASP Top 10 category</th>
<th>OWASP Core Rule Set (v3.3)</th>
<th>Cloudflare Managed Ruleset</th>
<th>Other Cloudflare products</th>
</tr>
</thead>
<tbody>
<tr>
<td>A01: Broken Access Control</td>
<td>Targets Path Traversal (930XXX) and App Defect detection (for example, .env, .git access).</td>
<td>Uses proprietary signatures for Insecure Direct Object References and Directory Traversal.</td>
<td>Security Rules are used for granular IP/Geo/ASN enforcement.</td>
</tr>
<tr>
<td>A02: Cryptographic Failures</td>
<td>N/A</td>
<td>N/A</td>
<td>The Cloudflare platform provides platform-level controls for HTTP Strict Transport Security, Minimum TLS versions, and automated certificate management. Post-quantum encryption ready.</td>
</tr>
<tr>
<td>A03: Injection (SQLi, XSS)</td>
<td>Comprehensive: Uses Regex-based scoring for SQLi (942XXX), XSS (941XXX), and RCE (932XXX).</td>
<td>Combines fast signature matching with Attack Score to catch highly obfuscated payloads. Smart decoding pre-processing is applied to prevent obfuscation.</td>
<td>The ML-based Cloudflare Attack Score complements managed rulesets by detecting attack variations and bypasses.</td>
</tr>
<tr>
<td>A04: Insecure Design</td>
<td>N/A</td>
<td>N/A</td>
<td>API Schema Validation helps mitigate protocol enforcement that might stem from poor design (for example HTTP Method enforcement)</td>
</tr>
<tr>
<td>A05: Security Misconfiguration</td>
<td>Detects directory indexing, default error messages, and protocol violations via 920XXX.</td>
<td>Includes a broad suite of Managed Rules for hardening specific CMS platforms (such as WordPress and Magento) against known misconfigs.</td>
<td></td>
</tr>
<tr>
<td>A06: Outdated Components</td>
<td>General rules may catch exploits, but it does not maintain a database of specific software versions.</td>
<td>Proactive Virtual Patching for newly discovered CVEs (for example, Log4Shell, React2Shell) often deployed within minutes or hours of disclosure.</td>
<td>The ML-based Cloudflare Attack Score complements managed rulesets by detecting attack variations and bypasses.</td>
</tr>
<tr>
<td>A07: Identification &amp; Auth</td>
<td>N/A</td>
<td>N/A</td>
<td>Leaked Credential Check, Bot Management and Account Abuse Protection are designed to stop automated stuffing attacks and other auth-based vulnerabilities.</td>
</tr>
<tr>
<td>A08: Software &amp; Data Integrity</td>
<td>Dedicated rules for Insecure Deserialization (944XXX) and PHP injection.</td>
<td>Signatures for common serialization exploits and supply chain attack patterns (for example, SolarWinds/Mimecast).</td>
<td>Cloudflare Client-side security monitors scripts, connections, and cookies loaded by your website visitors</td>
</tr>
<tr>
<td>A09: Logging &amp; Monitoring</td>
<td>N/A</td>
<td>N/A</td>
<td>The Cloudflare platform offers integrated dashboard with real-time analytics, Logpush to SIEMs, and automated anomaly alerting. LogExplorer is Cloudflare's observability and forensics tool.</td>
</tr>
<tr>
<td>A10: SSRF</td>
<td>Rules (934XXX) block requests to internal IPs and cloud metadata services (AWS, Azure, GCP).</td>
<td>Identifies SSRF signatures and allows users to easily block outbound requests to sensitive metadata endpoints.</td>
<td>-</td>
</tr>
</tbody>
</table>
<h2 id="resources">Resources</h2>
<ul class="directory-listing"><li><a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/">Concepts</a></li><li><a href="/waf/managed-rules/reference/owasp-core-ruleset/example/">OWASP evaluation example</a></li><li><a href="/waf/managed-rules/reference/owasp-core-ruleset/configure-dashboard/">Configure in the dashboard</a></li><li><a href="/waf/managed-rules/reference/owasp-core-ruleset/configure-api/">Configure via API</a></li><li><a href="/terraform/additional-configurations/waf-managed-rulesets/#configure-the-owasp-paranoia-level-score-threshold-and-action">Configure in Terraform</a></li></ul>
