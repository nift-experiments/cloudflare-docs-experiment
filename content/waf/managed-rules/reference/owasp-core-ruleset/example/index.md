---
cp9:
  canonical: https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/example/
  description: Example of how OWASP paranoia level and score threshold interact.
  full_title: OWASP evaluation example · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>OWASP evaluation example · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Example of how OWASP paranoia level and score threshold interact."><link rel="canonical" href="https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/example/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/example/index.md"><meta property="og:title" content="OWASP evaluation example · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Example of how OWASP paranoia level and score threshold interact."><meta property="og:url" content="https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/example/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/example/#page","headline":"OWASP evaluation example \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Example of how OWASP paranoia level and score threshold interact.","url":"https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/example/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/managed-rules/reference/owasp-core-ruleset/example/
  schema: 1
---
<p>The following example calculates the OWASP request threat score for an incoming request. The OWASP managed ruleset configuration is the following:</p>
<ul>
<li>OWASP Anomaly Score Threshold: <em>High - 25 and higher</em></li>
<li>OWASP Paranoia Level: <em>PL3</em></li>
<li>OWASP Action: <em>Managed Challenge</em></li>
</ul>
<p>This table shows the progress of the OWASP ruleset evaluation:</p>
<table>
<thead>
<tr>
<th>Rule ID</th>
<th>Paranoia level</th>
<th>Rule matched?</th>
<th align="right">Rule score</th>
<th align="right">Cumulative<br/>threat score</th>
</tr>
</thead>
<tbody>
<tr>
<td>–</td>
<td>–</td>
<td>–</td>
<td align="right">–</td>
<td align="right">0</td>
</tr>
<tr>
<td><code>...1813a269</code></td>
<td>PL3</td>
<td>Yes</td>
<td align="right">+5</td>
<td align="right">5</td>
</tr>
<tr>
<td><code>...ccc02be6</code></td>
<td>PL3</td>
<td>No</td>
<td align="right">–</td>
<td align="right">5</td>
</tr>
<tr>
<td><code>...96bfe867</code></td>
<td>PL2</td>
<td>Yes</td>
<td align="right">+5</td>
<td align="right">10</td>
</tr>
<tr>
<td><code>...48b74690</code></td>
<td>PL1</td>
<td>Yes</td>
<td align="right">+5</td>
<td align="right">15</td>
</tr>
<tr>
<td><code>...3297003f</code></td>
<td>PL2</td>
<td>Yes</td>
<td align="right">+3</td>
<td align="right">18</td>
</tr>
<tr>
<td><code>...317f28e1</code></td>
<td>PL1</td>
<td>No</td>
<td align="right">–</td>
<td align="right">18</td>
</tr>
<tr>
<td><code>...682bb405</code></td>
<td>PL2</td>
<td>Yes</td>
<td align="right">+5</td>
<td align="right">23</td>
</tr>
<tr>
<td><code>...56bb8946</code></td>
<td>PL2</td>
<td>No</td>
<td align="right">–</td>
<td align="right">23</td>
</tr>
<tr>
<td><code>...e5f94216</code></td>
<td>PL3</td>
<td>Yes</td>
<td align="right">+3</td>
<td align="right">26</td>
</tr>
<tr>
<td>(...)</td>
<td>(...)</td>
<td>(...)</td>
<td align="right">(...)</td>
<td align="right">(...)</td>
</tr>
<tr>
<td><code>...f3b37cb1</code></td>
<td>PL4</td>
<td>(not evaluated)</td>
<td align="right">–</td>
<td align="right">26</td>
</tr>
</tbody>
</table>
<p>Final request threat score: <code>26</code></p>
<p>Since <code>26</code> &gt;= <code>25</code> — that is, the threat score is greater than the configured score threshold — Cloudflare will apply the configured action (<em>Managed Challenge</em>). If you had configured a score threshold of <em>Medium - 40 and higher</em>, Cloudflare would not apply the action, since the request threat score would be lower than the score threshold (<code>26</code> &lt; <code>40</code>).</p>
<p><a href="/waf/analytics/security-events/#sampled-logs"><strong>Sampled logs</strong> in Security Events</a> would display the following details for the example incoming request handled by the OWASP Core Ruleset:</p>
<p><img src="/assets/upstream/images/waf/owasp-example-event-log.png" alt="Event log for example incoming request mitigated by the OWASP Core Ruleset" /></p>
<p>In sampled logs, the rule associated with requests mitigated by the Cloudflare OWASP Core Ruleset is the last rule in this managed ruleset: <code>949110: Inbound Anomaly Score Exceeded</code>, with rule ID <code class="nb-rule-id" title="6179ae15870a4bb7b2d480d4843b323c">843b323c</code>. To get the scores of individual rules contributing to the final request threat score, expand <strong>Additional logs</strong> in the event details.</p>
