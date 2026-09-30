<p>AI Gateway is available to use on all plans.</p>
<p>AI Gateway's core features available today are offered for free, and all it takes is a Cloudflare account and one line of code to <a href="/ai-gateway/get-started/">get started</a>. Core features include: dashboard analytics, caching, and rate limiting.</p>
<p>We will continue to build and expand AI Gateway. Some new features may be additional core features that will be free while others may be part of a premium plan. We will announce these as they become available.</p>
<p>You can monitor your usage in the AI Gateway dashboard.</p>
<h2 id="persistent-logs">Persistent logs</h2>
<p>Persistent logs are available on all plans. Log storage limits vary by plan.</p>
<h3 id="log-storage-limits">Log storage limits</h3>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Log storage limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers Free</td>
<td>100,000 logs total across all gateways</td>
</tr>
<tr>
<td>Workers Paid</td>
<td>10,000,000 logs per gateway</td>
</tr>
</tbody>
</table>
<p>For more details on log storage behavior and automatic log deletion, refer to <a href="/ai-gateway/reference/limits/">Limits</a> and <a href="/ai-gateway/observability/logging/#automatic-log-deletion">Logging</a>.</p>
<h2 id="data-loss-prevention-dlp">Data Loss Prevention (DLP)</h2>
<p>DLP scanning in AI Gateway is free on all plans. Accounts without a Zero Trust subscription have access to two predefined <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a>: Financial Information and Social / Insurance / National Identifier Numbers.</p>
<p>DLP profiles are shared at the account level with <a href="/cloudflare-one/data-loss-prevention/">Cloudflare One</a>. If your account has a Zero Trust subscription that includes DLP, the full set of profiles — including all predefined profiles, custom profiles, integration profiles, DLP datasets, and OCR — is automatically available in AI Gateway.</p>
<h2 id="guardrails">Guardrails</h2>
<p><a href="/ai-gateway/features/guardrails/">Guardrails</a> evaluates prompts and responses using <a href="/workers-ai/models/llama-guard-3-8b/"><code>@cf/meta/llama-guard-3-8b</code></a> on Workers AI. Usage is billed as <a href="/workers-ai/platform/pricing/">Workers AI</a> token-based inference — cost scales with the length of the prompts and responses being evaluated.</p>
<h2 id="unified-billing">Unified Billing</h2>
<p>A 5% fee is applied to all credits purchased through <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>. For example, a $100 credit purchase will result in a $105 charge. Inference pricing from providers is passed through with no markup — you pay the same per-token rates as you would directly with the provider.</p>
<h2 id="logpush">Logpush</h2>
<p>Logpush is only available on the Workers Paid plan.</p>
<table>
<thead>
<tr>
<th></th>
<th>Paid plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>Requests</td>
<td>10 million / month, +$0.05/million</td>
</tr>
</tbody>
</table>
<h2 id="pricing-notes">Pricing notes</h2>
<p>Prices subject to change. If you are an Enterprise customer, reach out to your account team to confirm pricing details.</p>
