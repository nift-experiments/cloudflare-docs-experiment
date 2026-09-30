<p>The <code>FlagshipServerProvider</code> implements the OpenFeature server provider interface. The provider works in <a href="/workers/">Cloudflare Workers</a>, Node.js, and any server-side JavaScript runtime that supports the Fetch API.</p>
<p>Inside a Cloudflare Worker, you can pass the Flagship <a href="/flagship/binding/">binding</a> directly to the provider. This avoids HTTP overhead and is the recommended approach. Outside of Workers, initialize the provider with an app ID and account ID.</p>
<h2 id="setup">Setup</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8715.md")
</div></div>
<h2 id="configuration-options">Configuration options</h2>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>binding</code></td>
<td><code>Flagship</code></td>
<td>No</td>
<td>The Flagship binding from <code>env.FLAGS</code>. Use this inside a Worker for best performance. The binding handles authentication automatically.</td>
</tr>
<tr>
<td><code>appId</code></td>
<td><code>string</code></td>
<td>No</td>
<td>The Flagship app ID from the Cloudflare dashboard. Required when not using a binding.</td>
</tr>
<tr>
<td><code>accountId</code></td>
<td><code>string</code></td>
<td>No</td>
<td>Your Cloudflare account ID. Required when using <code>appId</code>.</td>
</tr>
<tr>
<td><code>authToken</code></td>
<td><code>string</code></td>
<td>No</td>
<td>A Cloudflare <a href="/flagship/api-tokens/">API token</a> with Flagship Evaluate or Flagship App Evaluate permission. Required when not using a binding.</td>
</tr>
<tr>
<td><code>fetchOptions</code></td>
<td><code>RequestInit</code></td>
<td>No</td>
<td>Custom fetch options applied to HTTP requests.</td>
</tr>
<tr>
<td><code>timeout</code></td>
<td><code>number</code></td>
<td>No</td>
<td>Request timeout in milliseconds. Defaults to <code>5000</code>.</td>
</tr>
<tr>
<td><code>retries</code></td>
<td><code>number</code></td>
<td>No</td>
<td>Retry attempts on transient errors. Defaults to <code>1</code> and is capped at <code>10</code>.</td>
</tr>
<tr>
<td><code>retryDelay</code></td>
<td><code>number</code></td>
<td>No</td>
<td>Delay between retries in milliseconds. Defaults to <code>1000</code> and is capped at <code>30000</code>.</td>
</tr>
<tr>
<td><code>cacheTtl</code></td>
<td><code>number</code></td>
<td>No</td>
<td>Cache TTL in milliseconds. Enables response caching when greater than <code>0</code>.</td>
</tr>
<tr>
<td><code>cacheMaxSize</code></td>
<td><code>number</code></td>
<td>No</td>
<td>Maximum cached entries. Defaults to <code>1000</code> when <code>cacheTtl</code> is set.</td>
</tr>
</tbody>
</table>
<p>Provide either <code>binding</code> or <code>appId</code>, <code>accountId</code>, and <code>authToken</code>.</p>
<h2 id="response-caching">Response caching</h2>
<p>Server-side response caching is off by default. Enable it with <code>cacheTtl</code> when you want repeated evaluations for the same flag, type, and evaluation context to reuse a recent result.</p>
<pre><code class="language-ts">new FlagshipServerProvider({&#10;	appId: &quot;&lt;APP_ID&gt;&quot;,&#10;	accountId: &quot;&lt;ACCOUNT_ID&gt;&quot;,&#10;	authToken: &quot;&lt;API_TOKEN&gt;&quot;,&#10;	cacheTtl: 30_000,&#10;	cacheMaxSize: 1000,&#10;});&#10;</code></pre>
<p>Use caching for high-traffic server applications that repeatedly evaluate the same flags for the same contexts. Cached values may be stale until the TTL expires, so keep the TTL short for flags that you expect to change during active rollouts. The provider does not cache disabled flags or errors.</p>
<h2 id="evaluation-context">Evaluation context</h2>
<p>OpenFeature uses an evaluation context to pass user attributes to the flag provider. The <code>targetingKey</code> field is the primary user identifier.</p>
<p>Pass additional attributes alongside <code>targetingKey</code> to match <a href="/flagship/targeting/">targeting rules</a>. For example, you can include <code>plan</code>, <code>country</code>, or any custom attribute your rules reference.</p>
<p>Use primitive context values such as strings, numbers, booleans, and <code>Date</code> objects. The provider rejects objects and arrays as invalid context.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8716.md")
</div>
<h2 id="available-hooks">Available hooks</h2>
<p>The SDK ships with two hooks that you can attach to the OpenFeature client.</p>
<ul>
<li><strong>LoggingHook</strong> — Logs structured information for every evaluation.</li>
<li><strong>TelemetryHook</strong> — Captures timing and event data for observability.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8717.md")
</div>
<h2 id="migrate-from-another-provider">Migrate from another provider</h2>
<p>If you use another OpenFeature-compatible provider (for example, LaunchDarkly or Flagsmith), switch to Flagship by replacing the provider initialization. No changes are needed at evaluation call sites.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8718.md")
</div>
