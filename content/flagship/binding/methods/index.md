<p>The Flagship binding provides the following methods for evaluating feature flags. All methods are asynchronous and return a <code>Promise</code>. For known evaluation failures, typed methods return the <code>defaultValue</code> you provide.</p>
<p>Refer to the <a href="/flagship/binding/types/">types reference</a> for the definitions of <code>FlagshipEvaluationContext</code> and <code>FlagshipEvaluationDetails</code>.</p>
<h2 id="get"><code>get()</code></h2>
<p>Returns the raw flag value without type checking. Use this method when the flag type is not known at compile time.</p>
<p>If you provide <code>defaultValue</code>, <code>get()</code> returns that value for known evaluation failures, such as a missing flag. If you omit <code>defaultValue</code>, known evaluation failures are thrown.</p>
<pre><code class="language-ts">get(flagKey: string, defaultValue?: unknown, context?: FlagshipEvaluationContext): Promise&lt;unknown&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>flagKey</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>The key of the flag to evaluate.</td>
</tr>
<tr>
<td><code>defaultValue</code></td>
<td><code>unknown</code></td>
<td>No</td>
<td>The fallback value returned if evaluation fails or the flag is not found.</td>
</tr>
<tr>
<td><code>context</code></td>
<td><code>FlagshipEvaluationContext</code></td>
<td>No</td>
<td>Key-value attributes for targeting rules.</td>
</tr>
</tbody>
</table>
<pre><code class="language-ts">const value = await env.FLAGS.get(&quot;checkout-flow&quot;, &quot;v1&quot;, {&#10;	userId: &quot;user-42&quot;,&#10;});&#10;</code></pre>
<h2 id="getbooleanvalue"><code>getBooleanValue()</code></h2>
<p>Returns the flag value as a <code>boolean</code>.</p>
<pre><code class="language-ts">getBooleanValue(flagKey: string, defaultValue: boolean, context?: FlagshipEvaluationContext): Promise&lt;boolean&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>flagKey</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>The key of the flag to evaluate.</td>
</tr>
<tr>
<td><code>defaultValue</code></td>
<td><code>boolean</code></td>
<td>Yes</td>
<td>The fallback value returned if evaluation fails or the flag is not found.</td>
</tr>
<tr>
<td><code>context</code></td>
<td><code>FlagshipEvaluationContext</code></td>
<td>No</td>
<td>Key-value attributes for targeting rules.</td>
</tr>
</tbody>
</table>
<pre><code class="language-ts">const enabled = await env.FLAGS.getBooleanValue(&quot;dark-mode&quot;, false, {&#10;	userId: &quot;user-42&quot;,&#10;});&#10;</code></pre>
<h2 id="getstringvalue"><code>getStringValue()</code></h2>
<p>Returns the flag value as a <code>string</code>.</p>
<pre><code class="language-ts">getStringValue(flagKey: string, defaultValue: string, context?: FlagshipEvaluationContext): Promise&lt;string&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>flagKey</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>The key of the flag to evaluate.</td>
</tr>
<tr>
<td><code>defaultValue</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>The fallback value returned if evaluation fails or the flag is not found.</td>
</tr>
<tr>
<td><code>context</code></td>
<td><code>FlagshipEvaluationContext</code></td>
<td>No</td>
<td>Key-value attributes for targeting rules.</td>
</tr>
</tbody>
</table>
<pre><code class="language-ts">const variant = await env.FLAGS.getStringValue(&quot;checkout-flow&quot;, &quot;v1&quot;, {&#10;	userId: &quot;user-42&quot;,&#10;	country: &quot;US&quot;,&#10;});&#10;</code></pre>
<h2 id="getnumbervalue"><code>getNumberValue()</code></h2>
<p>Returns the flag value as a <code>number</code>.</p>
<pre><code class="language-ts">getNumberValue(flagKey: string, defaultValue: number, context?: FlagshipEvaluationContext): Promise&lt;number&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>flagKey</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>The key of the flag to evaluate.</td>
</tr>
<tr>
<td><code>defaultValue</code></td>
<td><code>number</code></td>
<td>Yes</td>
<td>The fallback value returned if evaluation fails or the flag is not found.</td>
</tr>
<tr>
<td><code>context</code></td>
<td><code>FlagshipEvaluationContext</code></td>
<td>No</td>
<td>Key-value attributes for targeting rules.</td>
</tr>
</tbody>
</table>
<pre><code class="language-ts">const maxRetries = await env.FLAGS.getNumberValue(&quot;max-retries&quot;, 3, {&#10;	plan: &quot;enterprise&quot;,&#10;});&#10;</code></pre>
<h2 id="getobjectvalue"><code>getObjectValue()</code></h2>
<p>Returns the flag value as a typed object. Use the generic parameter <code>T</code> to specify the expected shape.</p>
<pre><code class="language-ts">getObjectValue&lt;T extends object&gt;(flagKey: string, defaultValue: T, context?: FlagshipEvaluationContext): Promise&lt;T&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>flagKey</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>The key of the flag to evaluate.</td>
</tr>
<tr>
<td><code>defaultValue</code></td>
<td><code>T</code></td>
<td>Yes</td>
<td>The fallback value returned if evaluation fails or the flag is not found.</td>
</tr>
<tr>
<td><code>context</code></td>
<td><code>FlagshipEvaluationContext</code></td>
<td>No</td>
<td>Key-value attributes for targeting rules.</td>
</tr>
</tbody>
</table>
<pre><code class="language-ts">interface ThemeConfig {&#10;	primaryColor: string;&#10;	fontSize: number;&#10;}&#10;&#10;const theme = await env.FLAGS.getObjectValue&lt;ThemeConfig&gt;(&#10;	&quot;theme-config&quot;,&#10;	{ primaryColor: &quot;#000&quot;, fontSize: 14 },&#10;	{ userId: &quot;user-42&quot; },&#10;);&#10;</code></pre>
<h2 id="getbooleandetails"><code>getBooleanDetails()</code></h2>
<p>Returns the flag value as a <code>boolean</code> with evaluation metadata.</p>
<pre><code class="language-ts">getBooleanDetails(flagKey: string, defaultValue: boolean, context?: FlagshipEvaluationContext): Promise&lt;FlagshipEvaluationDetails&lt;boolean&gt;&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>flagKey</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>The key of the flag to evaluate.</td>
</tr>
<tr>
<td><code>defaultValue</code></td>
<td><code>boolean</code></td>
<td>Yes</td>
<td>The fallback value returned if evaluation fails or the flag is not found.</td>
</tr>
<tr>
<td><code>context</code></td>
<td><code>FlagshipEvaluationContext</code></td>
<td>No</td>
<td>Key-value attributes for targeting rules.</td>
</tr>
</tbody>
</table>
<pre><code class="language-ts">const details = await env.FLAGS.getBooleanDetails(&quot;dark-mode&quot;, false, {&#10;	userId: &quot;user-42&quot;,&#10;});&#10;console.log(details.value); // true&#10;console.log(details.reason); // &quot;TARGETING_MATCH&quot;&#10;</code></pre>
<h2 id="getstringdetails"><code>getStringDetails()</code></h2>
<p>Returns the flag value as a <code>string</code> with evaluation metadata.</p>
<pre><code class="language-ts">getStringDetails(flagKey: string, defaultValue: string, context?: FlagshipEvaluationContext): Promise&lt;FlagshipEvaluationDetails&lt;string&gt;&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>flagKey</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>The key of the flag to evaluate.</td>
</tr>
<tr>
<td><code>defaultValue</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>The fallback value returned if evaluation fails or the flag is not found.</td>
</tr>
<tr>
<td><code>context</code></td>
<td><code>FlagshipEvaluationContext</code></td>
<td>No</td>
<td>Key-value attributes for targeting rules.</td>
</tr>
</tbody>
</table>
<pre><code class="language-ts">const details = await env.FLAGS.getStringDetails(&quot;checkout-flow&quot;, &quot;v1&quot;, {&#10;	userId: &quot;user-42&quot;,&#10;});&#10;console.log(details.value); // &quot;v2&quot;&#10;console.log(details.variant); // &quot;new&quot;&#10;console.log(details.reason); // &quot;TARGETING_MATCH&quot;&#10;</code></pre>
<h2 id="getnumberdetails"><code>getNumberDetails()</code></h2>
<p>Returns the flag value as a <code>number</code> with evaluation metadata.</p>
<pre><code class="language-ts">getNumberDetails(flagKey: string, defaultValue: number, context?: FlagshipEvaluationContext): Promise&lt;FlagshipEvaluationDetails&lt;number&gt;&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>flagKey</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>The key of the flag to evaluate.</td>
</tr>
<tr>
<td><code>defaultValue</code></td>
<td><code>number</code></td>
<td>Yes</td>
<td>The fallback value returned if evaluation fails or the flag is not found.</td>
</tr>
<tr>
<td><code>context</code></td>
<td><code>FlagshipEvaluationContext</code></td>
<td>No</td>
<td>Key-value attributes for targeting rules.</td>
</tr>
</tbody>
</table>
<pre><code class="language-ts">const details = await env.FLAGS.getNumberDetails(&quot;max-retries&quot;, 3, {&#10;	plan: &quot;enterprise&quot;,&#10;});&#10;console.log(details.value); // 5&#10;console.log(details.reason); // &quot;TARGETING_MATCH&quot;&#10;</code></pre>
<h2 id="getobjectdetails"><code>getObjectDetails()</code></h2>
<p>Returns the flag value as a typed object with evaluation metadata. Use the generic parameter <code>T</code> to specify the expected shape.</p>
<pre><code class="language-ts">getObjectDetails&lt;T extends object&gt;(flagKey: string, defaultValue: T, context?: FlagshipEvaluationContext): Promise&lt;FlagshipEvaluationDetails&lt;T&gt;&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>flagKey</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>The key of the flag to evaluate.</td>
</tr>
<tr>
<td><code>defaultValue</code></td>
<td><code>T</code></td>
<td>Yes</td>
<td>The fallback value returned if evaluation fails or the flag is not found.</td>
</tr>
<tr>
<td><code>context</code></td>
<td><code>FlagshipEvaluationContext</code></td>
<td>No</td>
<td>Key-value attributes for targeting rules.</td>
</tr>
</tbody>
</table>
<pre><code class="language-ts">interface ThemeConfig {&#10;	primaryColor: string;&#10;	fontSize: number;&#10;}&#10;&#10;const details = await env.FLAGS.getObjectDetails&lt;ThemeConfig&gt;(&#10;	&quot;theme-config&quot;,&#10;	{ primaryColor: &quot;#000&quot;, fontSize: 14 },&#10;	{ userId: &quot;user-42&quot; },&#10;);&#10;console.log(details.value); // { primaryColor: &quot;#0051FF&quot;, fontSize: 16 }&#10;console.log(details.variant); // &quot;brand-refresh&quot;&#10;</code></pre>
<h2 id="error-handling">Error handling</h2>
<p>Typed evaluation methods return the <code>defaultValue</code> you provided for known evaluation failures, such as a missing flag or type mismatch. Unexpected runtime failures can still throw. Use the <code>*Details</code> methods to inspect known evaluation failures.</p>
<h3 id="type-mismatch">Type mismatch</h3>
<p>If you call a typed method on a flag with a different type (for example, <code>getBooleanValue</code> on a string flag), the method returns the default value. The <code>*Details</code> methods set <code>errorCode</code> to <code>&quot;TYPE_MISMATCH&quot;</code>.</p>
<pre><code class="language-ts">// Flag &quot;checkout-flow&quot; is a string flag, but you call getBooleanDetails.&#10;const details = await env.FLAGS.getBooleanDetails(&quot;checkout-flow&quot;, false);&#10;console.log(details.value); // false (the default value)&#10;console.log(details.errorCode); // &quot;TYPE_MISMATCH&quot;&#10;</code></pre>
<h3 id="evaluation-failure">Evaluation failure</h3>
<p>If evaluation fails for another reason, the method returns the default value. The <code>*Details</code> methods include an <code>errorCode</code> such as <code>&quot;FLAG_NOT_FOUND&quot;</code>, <code>&quot;INVALID_CONTEXT&quot;</code>, <code>&quot;PARSE_ERROR&quot;</code>, or <code>&quot;GENERAL&quot;</code>.</p>
<pre><code class="language-ts">const details = await env.FLAGS.getStringDetails(&#10;	&quot;nonexistent-flag&quot;,&#10;	&quot;fallback&quot;,&#10;);&#10;console.log(details.value); // &quot;fallback&quot;&#10;console.log(details.errorCode); // &quot;FLAG_NOT_FOUND&quot;&#10;</code></pre>
<h2 id="parameters-reference">Parameters reference</h2>
<p>The following table summarizes the parameters shared across all evaluation methods.</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>flagKey</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>The key of the flag to evaluate.</td>
</tr>
<tr>
<td><code>defaultValue</code></td>
<td>varies</td>
<td>Yes (except <code>get</code>)</td>
<td>The fallback value returned if evaluation fails or the flag is not found.</td>
</tr>
<tr>
<td><code>context</code></td>
<td><code>FlagshipEvaluationContext</code></td>
<td>No</td>
<td>Key-value attributes for targeting rules (for example, <code>{ userId: &quot;user-42&quot;, country: &quot;US&quot; }</code>).</td>
</tr>
</tbody>
</table>
