<p>The Flagship binding uses the following TypeScript types. These are available from the <code>@cloudflare/workers-types</code> package after running <code>npx wrangler types</code>.</p>
<h2 id="flagship"><code>Flagship</code></h2>
<p>The binding type. Each Flagship binding in your Wrangler configuration is typed as <code>Flagship</code> on the <code>Env</code> interface.</p>
<pre><code class="language-ts">interface Env {&#10;	FLAGS: Flagship;&#10;}&#10;</code></pre>
<p>Refer to the <a href="/flagship/binding/methods/">methods reference</a> for the full list of evaluation methods available on the binding.</p>
<h2 id="flagshipevaluationcontext"><code>FlagshipEvaluationContext</code></h2>
<p>A record of attribute names to values passed for <a href="/flagship/targeting/">targeting rules</a>. Use this to provide user attributes such as user ID, country, or plan type.</p>
<pre><code class="language-ts">type FlagshipEvaluationContext = Record&lt;string, string | number | boolean&gt;;&#10;</code></pre>
<h2 id="flagshipevaluationdetails"><code>FlagshipEvaluationDetails</code></h2>
<p>Returned by the <code>*Details</code> methods. Contains the evaluated value and metadata about how Flagship resolved the flag.</p>
<pre><code class="language-ts">interface FlagshipEvaluationDetails&lt;T&gt; {&#10;	flagKey: string;&#10;	value: T;&#10;	variant?: string;&#10;	reason?: string;&#10;	errorCode?: string;&#10;}&#10;</code></pre>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>flagKey</code></td>
<td><code>string</code></td>
<td>The key of the evaluated flag.</td>
</tr>
<tr>
<td><code>value</code></td>
<td><code>T</code></td>
<td>The resolved flag value.</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>string</code></td>
<td>The name of the matched variant, if any.</td>
</tr>
<tr>
<td><code>reason</code></td>
<td><code>string</code></td>
<td>Why the flag resolved to this value (for example, <code>&quot;TARGETING_MATCH&quot;</code> or <code>&quot;DEFAULT&quot;</code>).</td>
</tr>
<tr>
<td><code>errorCode</code></td>
<td><code>string</code></td>
<td>An error code if evaluation failed (for example, <code>&quot;TYPE_MISMATCH&quot;</code> or <code>&quot;GENERAL&quot;</code>).</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/flagship/reference/evaluation-reasons/">evaluation reasons and error codes</a> for the full list of possible values.</p>
