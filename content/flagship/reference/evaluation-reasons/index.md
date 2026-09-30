<p>When you evaluate a flag using the binding's <code>*Details</code> methods or the OpenFeature SDK, the response includes a <code>reason</code> field that explains why a particular value was returned. If an error occurs, the response includes an <code>errorCode</code> field.</p>
<h2 id="evaluation-reasons">Evaluation reasons</h2>
<table>
<thead>
<tr>
<th>Reason</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>TARGETING_MATCH</code></td>
<td>A targeting rule's conditions matched the evaluation context, and the rule's variant was returned.</td>
</tr>
<tr>
<td><code>SPLIT</code></td>
<td>A targeting rule with a percentage rollout matched. The user fell within the rollout percentage and received the rule's variant.</td>
</tr>
<tr>
<td><code>DEFAULT</code></td>
<td>No targeting rule matched the evaluation context. The flag's default variant was returned.</td>
</tr>
<tr>
<td><code>DISABLED</code></td>
<td>The flag is disabled. The default variant was returned regardless of targeting rules.</td>
</tr>
<tr>
<td><code>CACHED</code></td>
<td>The SDK returned a cached evaluation result.</td>
</tr>
<tr>
<td><code>ERROR</code></td>
<td>Evaluation failed and the default value was returned.</td>
</tr>
</tbody>
</table>
<h2 id="error-codes">Error codes</h2>
<p>When an evaluation error occurs, the method returns the default value you provided. The <code>*Details</code> methods include additional metadata about the error.</p>
<table>
<thead>
<tr>
<th>Error code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>TYPE_MISMATCH</code></td>
<td>The flag's variant type does not match the requested type. For example, calling <code>getBooleanValue</code> on a flag whose variant is a string. The default value is returned.</td>
</tr>
<tr>
<td><code>FLAG_NOT_FOUND</code></td>
<td>The specified flag key does not exist in the app. The default value is returned.</td>
</tr>
<tr>
<td><code>INVALID_CONTEXT</code></td>
<td>The evaluation context contains unsupported values, such as objects or arrays in HTTP evaluation. The default value is returned.</td>
</tr>
<tr>
<td><code>PARSE_ERROR</code></td>
<td>The SDK received an invalid evaluation response. The default value is returned.</td>
</tr>
<tr>
<td><code>GENERAL</code></td>
<td>An unexpected error occurred during evaluation, such as a timeout or network failure. The default value is returned.</td>
</tr>
</tbody>
</table>
<h2 id="example">Example</h2>
<p>The following example inspects evaluation details returned by <code>getBooleanDetails</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8731.md")
</div>
