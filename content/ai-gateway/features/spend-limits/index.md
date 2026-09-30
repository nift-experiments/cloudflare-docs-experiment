<p>Spend limits let you set cost-based budgets on your AI Gateway. When cumulative spend reaches the limit within a time window, AI Gateway blocks further requests with a <code>429</code> response until the window resets.</p>
<p>Unlike <a href="/ai-gateway/features/rate-limiting/">rate limiting</a>, which caps the number of requests, spend limits track actual dollar cost per request based on model pricing. You can scope limits to any combination of model, provider, or <a href="/ai-gateway/observability/custom-metadata/">custom metadata</a> dimensions like user ID, team, or application.</p>
<p>Spend limits apply to both <a href="/ai-gateway/features/unified-billing/">Unified Billing</a> requests and <a href="/ai-gateway/configuration/bring-your-own-keys/">BYOK</a> requests for models with known pricing.</p>
<p><img src="/assets/upstream/images/ai-gateway/spend-limits-rules.png" alt="Spend limits rules configured on a gateway" /></p>
<h2 id="how-it-works">How it works</h2>
<p>Each spend limit rule defines a budget (in dollars) over a rolling or fixed time window. AI Gateway calculates the cost of each request based on token usage and model pricing, then tracks cumulative spend against the limit in real time.</p>
<p>Before sending a request to the provider, AI Gateway evaluates all applicable spend limit rules at once. If any individual rule is over budget, the request is blocked with a <code>429</code> response.</p>
<p>Spend limits are eventually consistent. The current request's cost is recorded after completion, so a burst of concurrent requests can briefly exceed the limit before enforcement catches up.</p>
<h2 id="scoping-with-dimensions">Scoping with dimensions</h2>
<p>Each rule can be scoped by one or more dimensions:</p>
<ul>
<li><strong>Limit by provider</strong> — the provider used for the request.</li>
<li><strong>Limit by model</strong> — the model used for the request.</li>
<li><strong>Limit by metadata</strong> — a <a href="/ai-gateway/observability/custom-metadata/">custom metadata</a> key you attach to requests. Enter the metadata key name (for example, <code>agent_id</code> or <code>environment</code>).</li>
</ul>
<p>Each dimension can be configured in one of two modes:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Behavior</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Split by value</strong></td>
<td>Each distinct value gets its own independent budget bucket.</td>
<td>For example, if you pass in <code>agent_id</code>, splitting by <code>agent_id</code> gives every agent its own budget.</td>
</tr>
<tr>
<td><strong>Filter by value</strong></td>
<td>The rule applies only when the dimension equals a specific value.</td>
<td>For example, if you pass in <code>agent_id</code>, filtering <code>agent_id</code> to <code>agent_42</code> limits only that agent's requests.</td>
</tr>
</tbody>
</table>
<p>If a dimension is not configured on a rule, all values share one budget bucket. For example, a rule without a <code>provider</code> dimension tracks spend across all providers together.</p>
<h3 id="dimension-examples">Dimension examples</h3>
<p>Given a request with model <code>openai/gpt-5.5</code> and an <code>agent_id</code> metadata value of <code>agent_42</code>:</p>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Dimensions</th>
<th>Budget bucket</th>
</tr>
</thead>
<tbody>
<tr>
<td>Global budget for everyone</td>
<td>None</td>
<td>One shared bucket</td>
</tr>
<tr>
<td>Per-agent budget</td>
<td><code>agent_id</code> metadata: split by value</td>
<td>Separate bucket per agent</td>
</tr>
<tr>
<td>Per-provider, per-agent</td>
<td><code>agent_id</code> metadata: split by value, <code>provider</code>: split by value</td>
<td>Separate bucket per agent+provider combination</td>
</tr>
<tr>
<td>Specific model only</td>
<td><code>model</code>: filter by value <code>openai/gpt-5.5</code></td>
<td>Only applies to <code>openai/gpt-5.5</code> requests</td>
</tr>
<tr>
<td>Per-agent, per-model</td>
<td><code>agent_id</code> metadata: split by value, <code>model</code>: split by value</td>
<td>Separate bucket per agent+model combination</td>
</tr>
</tbody>
</table>
<h2 id="configure-spend-limits">Configure spend limits</h2>
<p>Spend limits are configured for each gateway through the dashboard or the API. In the dashboard, select your gateway, then go to <strong>Settings</strong> &gt; <strong>Spend limits</strong>. You can define up to 20 rules per gateway.</p>
<p><img src="/assets/upstream/images/ai-gateway/spend-limits-add-rule.png" alt="Add spend limit rule form" /></p>
<p>To scope spend limits by custom dimensions like user ID or team, attach <a href="/ai-gateway/observability/custom-metadata/">custom metadata</a> to your requests.</p>
<h3 id="set-spend-limits-by-user">Set spend limits by user</h3>
<p>You can give every user their own budget by scoping a rule to a user identifier. How you get that identifier depends on how your gateway is authenticated.</p>
<h4 id="with-cloudflare-access">With Cloudflare Access</h4>
<p>If your gateway is protected by <a href="/ai-gateway/configuration/cloudflare-access/">Cloudflare Access</a>, AI Gateway automatically adds the authenticated Access user ID to each request as the reserved <a href="/ai-gateway/observability/custom-metadata/#reserved-metadata"><code>cf.user_id</code></a> metadata key. You do not need to pass user IDs from your client application.</p>
<p>To set a per-user budget:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2823.md")
</div>
<p>Each authenticated Access user now gets an independent budget. To instead limit a single user, set the dimension to <strong>Filter by value</strong> and enter that user's Access JWT <code>sub</code> claim.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2822.md")
</aside>
<h4 id="without-cloudflare-access">Without Cloudflare Access</h4>
<p>If your gateway is not behind Access, pass your own user identifier as <a href="/ai-gateway/observability/custom-metadata/">custom metadata</a> (for example, a <code>user_id</code> key). Then, under <strong>Limit by metadata</strong>, add a dimension with the key <code>user_id</code> and set it to <strong>Split by value</strong>.</p>
<h2 id="behavior-when-a-limit-is-reached">Behavior when a limit is reached</h2>
<p>When a spend limit is exceeded, AI Gateway returns a <code>429 Too Many Requests</code> response. You have two options:</p>
<ul>
<li><strong>Block requests</strong> (default) - The request is rejected until the budget window resets.</li>
<li><strong>Fall back to a cheaper model</strong> - Create a <a href="/ai-gateway/features/dynamic-routing/">Dynamic Route</a> with a primary model and a fallback (for example, <code>anthropic/claude-opus-4.7</code> with a fallback to <code>@cf/moonshotai/kimi-k2.6</code>). Then set a spend limit on the primary model using this feature. When the primary model's budget is exceeded, AI Gateway automatically routes requests to the fallback model instead of blocking them.</li>
</ul>
<h2 id="monitoring-spend">Monitoring spend</h2>
<p>You can track your spend per model, provider, or any custom metadata attribute on the <a href="/ai-gateway/observability/analytics/">Analytics dashboard</a>. Use this to understand usage patterns and set informed budgets.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Cost tracking is a best-effort estimation based on token counts and model pricing. Refer to your provider's dashboard for exact billing amounts.</li>
<li>A maximum of 20 spend limit rules can be configured per gateway.</li>
</ul>
