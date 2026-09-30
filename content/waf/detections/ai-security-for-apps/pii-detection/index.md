---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/pii-detection/
  description: Detect personally identifiable information in AI request and response bodies.
  full_title: PII detection · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>PII detection · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Detect personally identifiable information in AI request and response bodies."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/pii-detection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/pii-detection/index.md"><meta property="og:title" content="PII detection · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Detect personally identifiable information in AI request and response bodies."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/pii-detection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/ai-security-for-apps/pii-detection/#page","headline":"PII detection \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Detect personally identifiable information in AI request and response bodies.","url":"https://developers.cloudflare.com/waf/detections/ai-security-for-apps/pii-detection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /waf/detections/ai-security-for-apps/pii-detection/
  schema: 1
---
<p>AI Security for Apps (formerly Firewall for AI) can detect personally identifiable information (PII) in incoming LLM prompts. There are two approaches to PII detection, and you can use them together for layered protection:</p>
<ul>
<li><a href="#ai-based-pii-detection">AI-based detection</a> — AI Security for Apps uses an AI model to identify common PII types in the prompt content. This approach catches PII even when it appears in natural language or unexpected formats.</li>
<li><a href="#exact-pii-detection-regex">Exact detection (regex)</a> — You write a WAF custom rule with a regular expression on the raw request body. This approach is ideal for organization-specific identifiers with a known, predictable format.</li>
</ul>
<h2 id="ai-based-pii-detection">AI-based PII detection</h2>
<p>When AI Security for Apps is enabled and a request arrives at a <code>cf-llm</code> labeled endpoint, it scans the prompt for PII and populates two fields:</p>
<ul>
<li><strong>LLM PII detected</strong> (<a href="/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_detected/"><code>cf.llm.prompt.pii_detected</code></a>) — <code>true</code> if any PII was found.</li>
<li><strong>LLM PII categories</strong> (<a href="/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/"><code>cf.llm.prompt.pii_categories</code></a>) — An array of the specific PII types found.</li>
</ul>
<p>The detection is powered by an AI-based Named Entity Recognition (NER) model. Refer to the <a href="/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/"><code>cf.llm.prompt.pii_categories</code> field reference</a> for the full list of recognized categories.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="detecting-pii-in-responses">Detecting PII in responses</h3>
@markup("md", "content/.markup/bodies/15563.md")
</aside>
<details class="nb-details"><summary>Supported PII categories</summary><div class="nb-details-body">
@input("content/.markup/bodies/15564.md")
</div></details>
<h3 id="be-specific-to-reduce-false-positives">Be specific to reduce false positives</h3>
<p>The <code>cf.llm.prompt.pii_detected</code> field returns <code>true</code> when any PII category is detected — including broad categories like <code>PERSON</code>, <code>DATE_TIME</code>, and <code>LOCATION</code> that frequently appear in normal conversation. Blocking based on this field alone will produce a high false-positive rate for most applications.</p>
<p>Instead, build rules against <code>cf.llm.prompt.pii_categories</code> and list only the categories that matter for your use case. For example, a customer support chatbot may need to block credit card numbers and SSNs but can safely ignore person names and dates. Start with the narrowest set of categories, monitor matches in <a href="/waf/analytics/security-analytics/">Security Analytics</a>, and expand only as needed.</p>
<h3 id="example-rules-ai-based-detection">Example rules — AI-based detection</h3>
<h4 id="block-any-request-containing-pii">Block any request containing PII</h4>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
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
<td>LLM PII Detected</td>
<td>equals</td>
<td>True</td>
</tr>
</tbody>
</table>
<p>Expression when using the editor:<br/>
<code>(cf.llm.prompt.pii_detected)</code></p>
<ul>
<li><strong>Action</strong>: <em>Block</em></li>
</ul>
<h4 id="block-only-specific-pii-categories">Block only specific PII categories</h4>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
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
<td>LLM PII Categories</td>
<td>is in</td>
<td><code>Credit Card</code></td>
</tr>
</tbody>
</table>
<p>Expression when using the editor:<br/>
<code>(any(cf.llm.prompt.pii_categories[*] in {&quot;CREDIT_CARD&quot;}))</code></p>
<ul>
<li><strong>Action</strong>: <em>Block</em></li>
</ul>
<h4 id="log-email-addresses-but-block-credit-cards-and-ssns">Log email addresses but block credit cards and SSNs</h4>
<p>Create two <a href="/waf/custom-rules/create-dashboard/">custom rules</a>:</p>
<ol>
<li>
<p>A rule with action <em>Block</em> and the following expression:<br/>
<code>(any(cf.llm.prompt.pii_categories[*] in {&quot;CREDIT_CARD&quot; &quot;US_SSN&quot;}))</code></p>
</li>
<li>
<p>A rule with action <em>Log</em> and the following expression:<br/>
<code>(any(cf.llm.prompt.pii_categories[*] in {&quot;EMAIL_ADDRESS&quot;}))</code></p>
</li>
</ol>
<h2 id="exact-pii-detection-regex">Exact PII detection (regex)</h2>
<p>If you need to detect <strong>custom PII formats</strong> specific to your organization — such as internal employee IDs, patient record numbers, or proprietary account identifiers — you can create a WAF <a href="/waf/custom-rules/">custom rule</a> using a regex match on the raw body (<a href="/ruleset-engine/rules-language/fields/reference/http.request.body.raw/"><code>http.request.body.raw</code></a> field).</p>
<p>This approach complements AI-based detection by matching predefined patterns, including organization-specific identifiers.</p>
<h3 id="example-detect-employee-ids">Example: Detect employee IDs</h3>
<p>In the following example, an organization uses employee IDs in the format <code>EMP-</code> followed by exactly six digits (for example, <code>EMP-482910</code>).</p>
<p><a href="/waf/custom-rules/create-dashboard/">Create a custom rule</a> with the following configuration:</p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
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
<td>Raw request body</td>
<td>matches regex</td>
<td><code>EMP-[0-9]{6}</code></td>
</tr>
</tbody>
</table>
<p>Expression when using the editor:<br/>
<code>(http.request.body.raw matches &quot;EMP-[0-9]{6}&quot;)</code></p>
<ul>
<li><strong>Action</strong>: <em>Block</em></li>
<li><strong>With response type</strong>: Custom JSON</li>
<li><strong>Response body</strong>: <code>{ &quot;error&quot;: &quot;Request blocked: employee ID detected in prompt.&quot; }</code></li>
</ul>
<details class="nb-details"><summary>Scope to a specific endpoint</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15565.md")
</div></details>
<h3 id="more-regex-examples">More regex examples</h3>
<table>
<thead>
<tr>
<th>Custom PII type</th>
<th>Example format</th>
<th>Regex pattern</th>
</tr>
</thead>
<tbody>
<tr>
<td>Employee ID</td>
<td><code>EMP-482910</code></td>
<td><code>EMP-[0-9]{6}</code></td>
</tr>
<tr>
<td>Patient record number</td>
<td><code>PAT/2024/00391</code></td>
<td><code>PAT/[0-9]{4}/[0-9]{5}</code></td>
</tr>
<tr>
<td>Internal account ID</td>
<td><code>ACCT-XX-99999</code></td>
<td><code>ACCT-[A-Z]{2}-[0-9]{5}</code></td>
</tr>
<tr>
<td>Custom API key prefix</td>
<td><code>sk_live_abc123...</code></td>
<td><code>sk_live_[a-zA-Z0-9]{20,}</code></td>
</tr>
</tbody>
</table>
<h3 id="considerations-for-regex-rules">Considerations for regex rules</h3>
<ul>
<li><strong>Cloudflare Plan requirement.</strong> Regex operators (<code>matches</code> and <code>~</code>) require a Business or Enterprise plan.</li>
<li><strong>Body size limit.</strong> The <code>http.request.body.raw</code> field inspects a limited portion of the request body. The exact limit <a href="/ruleset-engine/rules-language/fields/reference/http.request.body.raw/">varies by plan</a>.</li>
<li><strong>JSON payloads.</strong> The raw body includes the full JSON structure. Your regex should account for the fact that the prompt text is nested inside a JSON string.</li>
<li><strong>Performance.</strong> Complex regex patterns can impact rule evaluation time. Keep patterns as specific as possible.</li>
</ul>
<h2 id="combine-both-approaches">Combine both approaches</h2>
<p>You can use AI-based and exact detection together for layered protection:</p>
<p><code>(cf.llm.prompt.pii_detected or http.request.body.raw matches &quot;EMP-[0-9]{6}&quot;)</code></p>
<p>This rule blocks requests where either the AI model detects any built-in PII category or the regex matches your custom identifier format.</p>
