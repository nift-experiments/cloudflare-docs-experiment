<p>Web Assets provides application context to security detections. This helps detections inspect the right traffic and lets you create rules focusing on targeted protections.</p>
<p>Use this guide to connect a Web Assets operation to a security detection and create a rule that logs, challenges, blocks, or rate limits risky traffic.</p>
<h2 id="protection-workflow">Protection workflow</h2>
<p>Most protections that use Web Assets follow the same workflow:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13840.md")
</div>
<h2 id="example-protect-ai-powered-operations">Example: Protect AI-powered operations</h2>
<p><a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a> runs targeted scans on requests to AI-powered operations. Use it to detect prompt injection, personally identifiable information (PII) in prompts, unsafe topics, and other Large Language Model (LLM)-specific signals.</p>
<p>To define protection for an LLM-powered operation:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13841.md")
</div>
<p>For the full setup workflow, refer to <a href="/waf/detections/ai-security-for-apps/get-started/">Get started with AI Security for Apps</a>.</p>
<h2 id="validate-detection-behavior">Validate detection behavior</h2>
<p>Use Security Analytics to confirm that the expected requests carry the right operation and label context before you create a blocking rule.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13842.md")
</div>
<p>You can also export operation and label data with Logpush or query it with the GraphQL Analytics API. For more information, refer to <a href="/security/web-assets/label-operations/#use-labels-in-analytics-and-logs/">Use labels in analytics and logs</a>.</p>
<h2 id="mitigate-matched-traffic">Mitigate matched traffic</h2>
<p>After you validate detection behavior, create rules that act on relevant detection fields.</p>
<p>For example, a rule can match requests addressed to an operation labeled <code>cf-llm</code> that also carry personally identifiable information in an LLM prompt.</p>
<p>You can use <a href="/waf/custom-rules/create-dashboard/">custom rules</a> to log, challenge, block, or skip traffic. You can use <a href="/waf/rate-limiting-rules/">rate limiting rules</a> to limit high-volume activity.</p>
