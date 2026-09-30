<p>Percentage rollouts let you gradually release a feature to a fraction of your users. Any <a href="/flagship/targeting/">targeting rule</a> can include a rollout percentage between 0 and 100.</p>
<p>Use percentage rollouts when you want to limit blast radius, run an experiment, or sample requests without deploying new code.</p>
<h2 id="how-percentage-rollouts-work">How percentage rollouts work</h2>
<p>When a rule has a percentage rollout, the rule only serves its variant when both the rule conditions and the rollout bucket match. Contexts that do not match the rule continue to the next rule or receive the default variant if no later rule matches.</p>
<p>For example, a rule can target users on the <code>enterprise</code> plan, then serve the new experience to only 10% of those users. Users outside the 10% continue through the rest of the rule list.</p>
<pre><code class="language-json">{&#10;	&quot;priority&quot;: 1,&#10;	&quot;conditions&quot;: [&#10;		{ &quot;attribute&quot;: &quot;plan&quot;, &quot;operator&quot;: &quot;equals&quot;, &quot;value&quot;: &quot;enterprise&quot; }&#10;	],&#10;	&quot;serve_variation&quot;: &quot;on&quot;,&#10;	&quot;rollout&quot;: {&#10;		&quot;percentage&quot;: 10,&#10;		&quot;attribute&quot;: &quot;userId&quot;&#10;	}&#10;}&#10;</code></pre>
<p>The <code>reason</code> in evaluation details is <code>SPLIT</code> when a percentage rollout serves the variant.</p>
<h2 id="sticky-bucketing">Sticky bucketing</h2>
<p>Flagship uses consistent hashing on a configurable attribute to assign users to a rollout bucket. The same user always receives the same flag value for a given rollout configuration. This ensures a consistent experience across repeated evaluations.</p>
<p>By default, the bucketing attribute is <code>targetingKey</code>. You can configure which attribute to use for bucketing when you set up the rollout in the dashboard.</p>
<p>Rollout buckets are independent across accounts and flags. The same identifier may fall into different buckets for different flags, which helps avoid correlated rollouts across unrelated features.</p>
<p>Choose a bucketing attribute based on what should remain stable:</p>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Suggested attribute</th>
</tr>
</thead>
<tbody>
<tr>
<td>User-facing release</td>
<td>Stable user ID or <code>targetingKey</code></td>
</tr>
<tr>
<td>Account-level rollout</td>
<td>Account ID</td>
</tr>
<tr>
<td>Organization rollout</td>
<td>Organization or workspace ID</td>
</tr>
<tr>
<td>Request-level sampling</td>
<td>Request ID or another per-request value</td>
</tr>
</tbody>
</table>
<p>For most feature releases and experiments, use a stable user or account identifier. Use request-level values only when changing between requests is acceptable, such as for traffic sampling.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="random-assignment-without-targetingkey">Random assignment without targetingKey</h3>
@markup("md", "content/.markup/bodies/8710.md")
</aside>
<h2 id="common-rollout-patterns">Common rollout patterns</h2>
<h3 id="progressive-rollout">Progressive rollout</h3>
<p>Start with a small rollout, monitor your application, then increase the percentage as confidence grows.</p>
<ol>
<li>Create a flag with a 5% rollout.</li>
<li>Monitor errors, latency, product metrics, and user feedback.</li>
<li>Increase to 25%, then 50%, then 100%.</li>
<li>After the rollout reaches 100%, remove temporary targeting rules and make the winning variant the default.</li>
<li>After the feature is fully shipped, remove the old code path and delete the flag.</li>
</ol>
<h3 id="targeted-rollout-plus-percentage-rollout">Targeted rollout plus percentage rollout</h3>
<p>Consider a flag <code>new-checkout</code> with the following rules:</p>
<ol>
<li><strong>Rule 1</strong>: <code>plan equals &quot;enterprise&quot;</code> — serve variant <code>on</code>.</li>
<li><strong>Rule 2</strong>: 25% rollout on <code>userId</code> — serve variant <code>on</code>.</li>
<li><strong>Default variant</strong>: <code>off</code>.</li>
</ol>
<p>In this configuration:</p>
<ul>
<li>All enterprise users see the new checkout.</li>
<li>25% of all other users, determined by their <code>userId</code>, also see the new checkout.</li>
<li>The remaining 75% of non-enterprise users see the standard checkout.</li>
</ul>
<p>As you gain confidence, increase the rollout percentage until you reach 100%.</p>
<h3 id="a-b-n-testing">A/B/n testing</h3>
<p>For a plain A/B/n test with no audience conditions, configure each variant's traffic share in the Cloudflare dashboard. The dashboard calculates the cumulative thresholds for you.</p>
<p>If you manage a plain A/B/n test directly through the API, create one rule per variant with cumulative rollout percentages. Flagship evaluates rules in priority order. If a context matches a rule but does not fall into that rule's rollout percentage, evaluation continues to the next rule.</p>
<p>For a 30% / 40% / 30% split across variants A, B, and C:</p>
<table>
<thead>
<tr>
<th>Variant</th>
<th>Share</th>
<th>Cumulative threshold</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>30%</td>
<td>30</td>
</tr>
<tr>
<td>B</td>
<td>40%</td>
<td>70</td>
</tr>
<tr>
<td>C</td>
<td>30%</td>
<td>100</td>
</tr>
</tbody>
</table>
<pre><code class="language-json">[&#10;	{&#10;		&quot;priority&quot;: 1,&#10;		&quot;conditions&quot;: [],&#10;		&quot;serve_variation&quot;: &quot;variant-a&quot;,&#10;		&quot;rollout&quot;: { &quot;percentage&quot;: 30, &quot;attribute&quot;: &quot;targetingKey&quot; }&#10;	},&#10;	{&#10;		&quot;priority&quot;: 2,&#10;		&quot;conditions&quot;: [],&#10;		&quot;serve_variation&quot;: &quot;variant-b&quot;,&#10;		&quot;rollout&quot;: { &quot;percentage&quot;: 70, &quot;attribute&quot;: &quot;targetingKey&quot; }&#10;	},&#10;	{&#10;		&quot;priority&quot;: 3,&#10;		&quot;conditions&quot;: [],&#10;		&quot;serve_variation&quot;: &quot;variant-c&quot;,&#10;		&quot;rollout&quot;: { &quot;percentage&quot;: 100, &quot;attribute&quot;: &quot;targetingKey&quot; }&#10;	}&#10;]&#10;</code></pre>
<p>In API-managed configurations, the first rule covers buckets 0-30. The second rule covers buckets 31-70. The final rule catches the remaining buckets through 100. Always set the final rule to 100 when every eligible context should receive a variant.</p>
<p>Use the same bucketing attribute on every rule in the experiment. If each rule uses a different attribute, users may not stay in the intended split.</p>
<h3 id="targeted-a-b-n-testing">Targeted A/B/n testing</h3>
<p>You can combine audience targeting with a multi-variant rollout. For example, you might want only premium users to enter an experiment, then split those premium users across three variants.</p>
<p>For targeted A/B/n tests, repeat the same audience condition on each variant rule and use cumulative rollout thresholds. When you use this targeted multi-rule pattern, configure the cumulative threshold for each rule explicitly, whether you are using the dashboard or the API.</p>
<p>For a premium-only split where 20% receive variant A, 40% receive variant B, and the remaining 40% receive variant C, use thresholds of 20, 60, and 100:</p>
<pre><code class="language-json">[&#10;	{&#10;		&quot;priority&quot;: 1,&#10;		&quot;conditions&quot;: [&#10;			{ &quot;attribute&quot;: &quot;plan&quot;, &quot;operator&quot;: &quot;equals&quot;, &quot;value&quot;: &quot;premium&quot; }&#10;		],&#10;		&quot;serve_variation&quot;: &quot;variant-a&quot;,&#10;		&quot;rollout&quot;: { &quot;percentage&quot;: 20, &quot;attribute&quot;: &quot;targetingKey&quot; }&#10;	},&#10;	{&#10;		&quot;priority&quot;: 2,&#10;		&quot;conditions&quot;: [&#10;			{ &quot;attribute&quot;: &quot;plan&quot;, &quot;operator&quot;: &quot;equals&quot;, &quot;value&quot;: &quot;premium&quot; }&#10;		],&#10;		&quot;serve_variation&quot;: &quot;variant-b&quot;,&#10;		&quot;rollout&quot;: { &quot;percentage&quot;: 60, &quot;attribute&quot;: &quot;targetingKey&quot; }&#10;	},&#10;	{&#10;		&quot;priority&quot;: 3,&#10;		&quot;conditions&quot;: [&#10;			{ &quot;attribute&quot;: &quot;plan&quot;, &quot;operator&quot;: &quot;equals&quot;, &quot;value&quot;: &quot;premium&quot; }&#10;		],&#10;		&quot;serve_variation&quot;: &quot;variant-c&quot;,&#10;		&quot;rollout&quot;: { &quot;percentage&quot;: 100, &quot;attribute&quot;: &quot;targetingKey&quot; }&#10;	}&#10;]&#10;</code></pre>
<p>Users who do not match <code>plan equals &quot;premium&quot;</code> skip all three rules and receive the flag's default variant, unless a later rule matches them.</p>
<h3 id="request-sampling">Request sampling</h3>
<p>You can use percentage rollouts for request-level sampling by choosing a per-request bucketing attribute. For example, a 1% rollout can enable extra logging or diagnostics for a small fraction of requests.</p>
<p>Only use this pattern when it is acceptable for the same user to receive different results on different requests.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="rollout-results-change-between-requests">Rollout results change between requests</h3>
<p>If the same user receives different values across requests, the evaluation context is probably missing <code>targetingKey</code> or the configured bucketing attribute.</p>
<p>Pass the same stable identifier on every evaluation:</p>
<pre><code class="language-ts">const enabled = await env.FLAGS.getBooleanValue(&quot;gradual-rollout&quot;, false, {&#10;	userId: session.user.id,&#10;});&#10;</code></pre>
<p>Then configure the rollout to bucket by <code>userId</code>.</p>
<h3 id="rollout-never-reaches-some-users">Rollout never reaches some users</h3>
<p>Check rule order. A catch-all rule with a lower priority number can return a variant before later rollout rules run. Place broad catch-all rules after more specific rules.</p>
<h3 id="a-b-n-split-does-not-match-expected-percentages">A/B/n split does not match expected percentages</h3>
<p>For plain dashboard-managed A/B/n tests, enter each variant's traffic share and let the dashboard calculate thresholds.</p>
<p>For API-managed A/B/n tests, or for targeted A/B/n tests configured as multiple rules, use cumulative thresholds. A 30% / 40% / 30% split should use thresholds of 30, 70, and 100, not 30, 40, and 30.</p>
<h3 id="default-variant-appears-during-a-rollout">Default variant appears during a rollout</h3>
<p>This can happen when a context matches the rule conditions but falls outside the rollout percentage, and no later rule matches. Add a later rule or use a 100% final rule if every matching context should receive a non-default variant.</p>
