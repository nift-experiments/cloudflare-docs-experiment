---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/attack-score/
  description: Machine learning scores that classify each request for attack likelihood.
  full_title: WAF attack score · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>WAF attack score · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Machine learning scores that classify each request for attack likelihood."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/attack-score/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/attack-score/index.md"><meta property="og:title" content="WAF attack score · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Machine learning scores that classify each request for attack likelihood."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/attack-score/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/attack-score/#page","headline":"WAF attack score \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Machine learning scores that classify each request for attack likelihood.","url":"https://developers.cloudflare.com/waf/detections/attack-score/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/detections/attack-score/
  schema: 1
---
<p>The attack score <a href="/waf/concepts/#detection-versus-mitigation">traffic detection</a> classifies each request using a machine learning algorithm, assigning a score from 1 to 99 based on the likelihood that the request is malicious. This detection complements <a href="/waf/managed-rules/">WAF Managed Rules</a>.</p>
<p><a href="/waf/managed-rules/">Managed Rules</a> match requests against known attack signatures — specific patterns of established attack vectors. They have a very low rate of false positives. However, attackers can modify known payloads, for example by using fuzzing techniques (a testing technique that sends modified inputs to find vulnerabilities), to evade exact signature matches.</p>
<p>Attack score addresses this gap. You can use the score to identify potentially malicious traffic that is not an exact match to any of the rules in WAF Managed Rules.</p>
<p>To maximize protection, Cloudflare recommends that you use both Managed Rules and attack score.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15389.md")
</aside>
<h2 id="available-scores">Available scores</h2>
<p>The Cloudflare WAF provides the following attack score fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
<th>Required plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>WAF Attack Score <br/> [<code>cf.waf.score</code>][1] <br/> <span class="nb-type">Number</span></td>
<td>A global score from 1–99 that combines the score of each WAF attack vector into a single score.</td>
<td>Enterprise</td>
</tr>
<tr>
<td>WAF SQLi Attack Score <br/> [<code>cf.waf.score.sqli</code>][2] <br/> <span class="nb-type">Number</span></td>
<td>A score from 1–99 classifying the [SQL injection][6] (SQLi) attack vector.</td>
<td>Enterprise</td>
</tr>
<tr>
<td>WAF XSS Attack Score <br/> [<code>cf.waf.score.xss</code>][3] <br/> <span class="nb-type">Number</span></td>
<td>A score from 1–99 classifying the [cross-site scripting][7] (XSS) attack vector.</td>
<td>Enterprise</td>
</tr>
<tr>
<td>WAF RCE Attack Score <br/> [<code>cf.waf.score.rce</code>][4] <br/> <span class="nb-type">Number</span></td>
<td>A score from 1–99 classifying the command injection or [remote code execution][8] (RCE) attack vector.</td>
<td>Enterprise</td>
</tr>
<tr>
<td>WAF Attack Score Class <br/> [<code>cf.waf.score.class</code>][5] <br/> <span class="nb-type">String</span></td>
<td>The attack score class of the current request, based on the WAF attack score. <br/> Possible values: <code>attack</code>, <code>likely_attack</code>, <code>likely_clean</code>, and <code>clean</code>.</td>
<td>Business or above</td>
</tr>
</tbody>
</table>
<p>You can use these fields in expressions of <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/rate-limiting-rules/">rate limiting rules</a>. Numeric score fields range from <code>1</code> to <code>99</code>:</p>
<ul>
<li>A score of <code>1</code> indicates that the request is almost certainly malicious.</li>
<li>A score of <code>99</code> indicates that the request is likely clean.</li>
</ul>
<p>A score of <code>100</code> means the request reached the WAF attack score system, but the system decided not to score it.</p>
<p>In <a href="/logs/logpush/">Logpush</a> data, a score of <code>0</code> means the request did not reach the attack score stage — for example, because a previous rule or protection system already mitigated it. The value <code>0</code> does not appear in the Cloudflare dashboard.</p>
<p>The global WAF Attack Score is mathematically derived from individual attack scores (for example, from SQLi Attack Score and XSS Attack Score), reflecting their interdependence. However, the global score is not a sum of individual scores. A low global score usually indicates medium to low individual scores, while a high global score suggests higher individual scores.</p>
<p>The WAF Attack Score Class field can have one of the following values, depending on the calculated request attack score:</p>
<table>
<thead>
<tr>
<th>Dashboard label</th>
<th>Field value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Attack</em></td>
<td><code>attack</code></td>
<td>Attack score between <code>1</code> and <code>20</code>.</td>
</tr>
<tr>
<td><em>Likely attack</em></td>
<td><code>likely_attack</code></td>
<td>Attack score between <code>21</code> and <code>50</code>.</td>
</tr>
<tr>
<td><em>Likely clean</em></td>
<td><code>likely_clean</code></td>
<td>Attack score between <code>51</code> and <code>80</code>.</td>
</tr>
<tr>
<td><em>Clean</em></td>
<td><code>clean</code></td>
<td>Attack score between <code>81</code> and <code>99</code>.</td>
</tr>
</tbody>
</table>
<p>Requests with the special attack score <code>100</code> will show a WAF Attack Score Class of <em>Unscored</em> in the Cloudflare dashboard, but you cannot use this class value in rule expressions.</p>
<p>Attack score automatically detects and decodes Base64, JavaScript (Unicode escape sequences), and URL encoded content anywhere in the request: URL, headers, and body.</p>
<h2 id="rule-recommendations">Rule recommendations</h2>
<p>Blocking traffic solely based on attack score for all values below <code>50</code> is not recommended. The <em>Likely attack</em> range (scores <code>21</code>–<code>50</code>) can include legitimate requests incorrectly flagged as malicious (false positives). If you want to block traffic based on attack score, do one of the following:</p>
<ul>
<li>
<p>Use a more strict WAF Attack Score value in your expression. For example, block traffic with a WAF attack score below <code>20</code> or below <code>15</code> (you may need to adjust the exact threshold).</p>
</li>
<li>
<p>Combine a higher WAF Attack Score threshold with additional filters when blocking incoming traffic. For example, include a check for a specific URI path in your expression or use bot score as part of your criteria.</p>
</li>
</ul>
<hr />
<h2 id="start-using-waf-attack-score">Start using WAF attack score</h2>
<h3 id="1-create-a-custom-rule"><ol>
<li>Create a custom rule</li>
</ol></h3>
<p>Enterprise customers can <a href="/waf/custom-rules/create-dashboard/">create a custom rule</a> that blocks requests with a <strong>WAF Attack Score</strong> less than or equal to <code>20</code> (recommended initial threshold). For example:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>WAF Attack Score</td>
<td>less than or equal to</td>
<td><code>20</code></td>
</tr>
</tbody>
</table>
<ul>
<li>Equivalent rule expression: <code>cf.waf.score le 20</code></li>
<li>Action: <em>Block</em></li>
</ul>
<p>Business customers must create a custom rule with the <strong>WAF Attack Score Class</strong> field instead. For example, use this field to block incoming requests with a score class of <em>Attack</em>:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>WAF Attack Score Class</td>
<td>equals</td>
<td><code>Attack</code></td>
</tr>
</tbody>
</table>
<ul>
<li>Equivalent rule expression: <code>cf.waf.score.class eq &quot;attack&quot;</code></li>
<li>Action: <em>Block</em></li>
</ul>
<h3 id="2-monitor-domain-traffic"><ol start="2">
<li>Monitor domain traffic</li>
</ol></h3>
<p>Monitor the rule you created, especially in the first few days, to make sure you entered an appropriate threshold (or class) for your traffic. Update the rule if required.</p>
<h3 id="3-update-the-rule-action"><ol start="3">
<li>Update the rule action</li>
</ol></h3>
<p>If you are an Enterprise customer and you created a rule with <em>Log</em> action, change the rule action to a more severe one, like <em>Managed Challenge</em> or <em>Block</em>.</p>
<hr />
<h2 id="additional-remarks">Additional remarks</h2>
<p>WAF attack score and <a href="/bots/concepts/bot-score/">bot score</a> serve different purposes. Attack score identifies variations of attacks that WAF Managed Rules do not catch. Bot score identifies whether a request comes from automated traffic.</p>
