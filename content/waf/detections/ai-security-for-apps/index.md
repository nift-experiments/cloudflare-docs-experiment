---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/
  description: Detect prompt injection, PII, and unsafe topics in AI application traffic.
  full_title: AI Security for Apps · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>AI Security for Apps · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Detect prompt injection, PII, and unsafe topics in AI application traffic."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/index.md"><meta property="og:title" content="AI Security for Apps · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Detect prompt injection, PII, and unsafe topics in AI application traffic."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/ai-security-for-apps/#page","headline":"AI Security for Apps \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Detect prompt injection, PII, and unsafe topics in AI application traffic.","url":"https://developers.cloudflare.com/waf/detections/ai-security-for-apps/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /waf/detections/ai-security-for-apps/
  schema: 1
---
<p>Applications that use <span class="nb-glossary-tooltip" title="LLM">large language models</span> (LLMs) are exposed to threats specific to how LLMs process input — prompt injection attacks, PII exposure in prompts, and prompts about unsafe topics.</p>
<p>AI Security for Apps (formerly Firewall for AI) complements your existing WAF rules with detections designed for these LLM-specific threats. It is model-agnostic — the detections work regardless of which LLM you use.</p>
<ul>
<li><a href="/waf/detections/ai-security-for-apps/pii-detection/">PII detection</a> — Detect personally identifiable information (PII) in incoming prompts, such as phone numbers, email addresses, social security numbers, and credit card numbers.</li>
<li><a href="/waf/detections/ai-security-for-apps/unsafe-topics/">Unsafe and custom topic detection</a> — Detect prompts related to unsafe subjects such as violent crimes or hate speech, or custom topics specific to your organization.</li>
<li><a href="/waf/detections/ai-security-for-apps/prompt-injection/"><span class="nb-glossary-tooltip" title="prompt injection">Prompt injection</span> detection</a> — Detect prompts designed to subvert your LLM's intended behavior, such as attempts to make the model ignore its instructions or reveal its system prompt.</li>
</ul>
<p>When enabled, AI Security for Apps scans incoming requests to <a href="/api-shield/management-and-monitoring/endpoint-labels/">endpoints labeled <code>cf-llm</code></a> for LLM prompts that may contain threats. Currently, the detection only handles requests with a JSON content type (<code>application/json</code>).</p>
<p>Based on scan results, Cloudflare populates <a href="/waf/detections/ai-security-for-apps/fields/">AI detection fields</a> — fields you can use in WAF rule expressions. You can use these fields in two ways:</p>
<ul>
<li><strong>Monitor:</strong> Filter by the <code>cf-llm</code> label in <a href="/waf/analytics/security-analytics/">Security Analytics</a> to review detection results across your traffic.</li>
<li><strong>Mitigate:</strong> Use the fields in <a href="/waf/custom-rules/">custom rules</a> or <a href="/waf/rate-limiting-rules/">rate limiting rules</a> to block or challenge requests based on detection results.</li>
</ul>
<h2 id="availability">Availability</h2>
<p>AI Security for Apps capabilities vary by Cloudflare plan:</p>
<table>
<thead>
<tr>
<th>Capability</th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>LLM endpoint discovery</strong> — Automatically identify AI-powered endpoints across your web properties</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td><strong>AI Security Log Mode Ruleset</strong> — Pre-built ruleset that logs the full request body alongside detection results</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Paid add-on</td>
</tr>
<tr>
<td><strong>AI detection fields</strong> — PII detection, prompt injection scoring, unsafe topic detection, custom topics</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Paid add-on</td>
</tr>
</tbody>
</table>
<p>To get access to the <a href="/waf/detections/ai-security-for-apps/log-mode-vs-production-mode/#log-mode">AI Security Log Mode Ruleset</a> and enable <a href="/waf/detections/ai-security-for-apps/fields/">AI detection fields</a>, contact your account team.</p>
<p>AI Security for Apps is built into the Cloudflare <a href="/waf/">Web Application Firewall (WAF)</a> — the WAF must be enabled on your zone before detection fields can be populated and used in rule expressions.</p>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="/ai-gateway/">AI Gateway</a> — Monitor, control, and cache requests to LLM providers.</li>
<li><a href="https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/">What are the OWASP Top 10 risks for LLMs?</a> — Background on the most common security risks for LLM-powered applications.</li>
</ul>
