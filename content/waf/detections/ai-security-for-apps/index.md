<p>Applications that use <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15574.md")
</div> (LLMs) are exposed to threats specific to how LLMs process input — prompt injection attacks, PII exposure in prompts, and prompts about unsafe topics.
<p>AI Security for Apps (formerly Firewall for AI) complements your existing WAF rules with detections designed for these LLM-specific threats. It is model-agnostic — the detections work regardless of which LLM you use.</p>
<ul>
<li><a href="/waf/detections/ai-security-for-apps/pii-detection/">PII detection</a> — Detect personally identifiable information (PII) in incoming prompts, such as phone numbers, email addresses, social security numbers, and credit card numbers.</li>
<li><a href="/waf/detections/ai-security-for-apps/unsafe-topics/">Unsafe and custom topic detection</a> — Detect prompts related to unsafe subjects such as violent crimes or hate speech, or custom topics specific to your organization.</li>
<li><a href="/waf/detections/ai-security-for-apps/prompt-injection/"><div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/15575.md")
</div> detection</a> — Detect prompts designed to subvert your LLM's intended behavior, such as attempts to make the model ignore its instructions or reveal its system prompt.
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
