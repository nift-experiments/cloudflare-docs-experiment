<p>Flagship organizes feature flags into apps. You define flags with variants and targeting rules, then evaluate them within Cloudflare's global network.</p>
<h2 id="overview">Overview</h2>
<p>Flagship feature flags go through three stages from creation to evaluation:</p>
<ol>
<li><strong>Configure</strong> — Create flags and targeting rules in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> or through the <a href="/api/resources/flagship">API</a>.</li>
<li><strong>Propagate</strong> — Flagship automatically distributes your flag configuration across Cloudflare's global network within seconds.</li>
<li><strong>Evaluate</strong> — Your Worker (or SDK) evaluates flags locally using the propagated configuration. There is no round-trip to a central server.</li>
</ol>
<p>Flag changes take effect globally within seconds of saving. You do not need to redeploy your Worker or restart your application. If the dashboard is temporarily unavailable, flag evaluation continues to work using the last propagated configuration.</p>
<h2 id="apps">Apps</h2>
<p>An app is the top-level organizational unit in Flagship. It groups related flags together.</p>
<p>An app typically maps to a single project, service, or product surface. Each Cloudflare account can have multiple apps. For example, you might create one app for your marketing site and another for your API backend.</p>
<h2 id="flags">Flags</h2>
<p>A flag is a named feature toggle. Each flag has a key, a set of <a href="#variants">variants</a>, <a href="#targeting-rules">targeting rules</a>, and an enabled/disabled state.</p>
<p>Flag keys must be unique within an app. Keys can contain letters, numbers, hyphens, and underscores.</p>
<p>When a flag is disabled, it always returns the default variant regardless of any targeting rules. Choose a default variant that is safe for your application if Flagship cannot evaluate the flag.</p>
<h2 id="variants">Variants</h2>
<p>Variants are the possible values a flag can return. Each flag must have at least one variant, and one variant is designated as the default.</p>
<p>Flagship supports four variant types:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Boolean</td>
<td><code>on: true</code>, <code>off: false</code></td>
</tr>
<tr>
<td>String</td>
<td><code>v1: &quot;old-checkout&quot;</code>, <code>v2: &quot;new-checkout&quot;</code></td>
</tr>
<tr>
<td>Number</td>
<td><code>low: 100</code>, <code>high: 1000</code></td>
</tr>
<tr>
<td>JSON</td>
<td><code>premium: { &quot;tier&quot;: &quot;premium&quot;, &quot;features&quot;: [&quot;analytics&quot;, &quot;export&quot;] }</code></td>
</tr>
</tbody>
</table>
<p>Use boolean flags for simple on/off toggles. Use string, number, or JSON flags when you need to deliver configuration values or structured data. JSON variants can contain objects or arrays.</p>
<h2 id="targeting-rules">Targeting rules</h2>
<p>Targeting rules control which variant a flag returns for a given request. Rules are evaluated in sequential order, and the first matching rule wins. If no rule matches, the default variant is returned.</p>
<p>Each rule contains:</p>
<ul>
<li><strong>Conditions</strong> that compare an attribute from the <a href="#evaluation-context">evaluation context</a> against a value using an operator.</li>
<li>An optional <strong>percentage rollout</strong> that splits traffic across variants.</li>
<li>A <strong>variant</strong> to serve when the rule matches.</li>
</ul>
<p>Conditions within a rule can be grouped with <code>AND</code>/<code>OR</code> operators.</p>
<p>Refer to <a href="/flagship/targeting/">Targeting rules</a> and <a href="/flagship/targeting/operators/">Operators</a> for the full list of operators and configuration options.</p>
<h2 id="evaluation-context">Evaluation context</h2>
<p>The evaluation context is a set of key-value attributes that describe the current user or request (for example, <code>userId</code>, <code>country</code>, <code>plan</code>).</p>
<p>You pass the context as the third argument to evaluation methods on the binding:</p>
<pre><code class="language-ts">const value = await env.FLAGS.getBooleanValue(&quot;new-checkout&quot;, false, {&#10;	userId: &quot;user-42&quot;,&#10;	country: &quot;US&quot;,&#10;});&#10;</code></pre>
<p>When using the <a href="/flagship/sdk/">OpenFeature SDK</a>, you pass context through the OpenFeature evaluation context object.</p>
<p>Flagship uses context attributes to match targeting rules and to determine percentage rollout bucketing. A consistent context (for example, the same <code>userId</code>) produces the same rollout result on every evaluation.</p>
<p>Avoid sending sensitive data in evaluation context. Only include attributes needed by targeting rules or rollout bucketing.</p>
<h2 id="flag-propagation">Flag propagation</h2>
<p>After you change a flag, it can take up to 30 seconds for the updated value to reflect globally. During this propagation window, some evaluations may still return the previous flag value.</p>
