<p>A confirmation dialog screen shown when the user's request to join stage is approved or when the host invites the local user to join stage.</p>
<h2 id="methods">Methods</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Parameters</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>activate</code></td>
<td><code>meeting: RealtimeKitClient</code></td>
<td>Bind the dialog to the meeting state</td>
</tr>
<tr>
<td><code>applyDesignTokens</code></td>
<td><code>designTokens: RtkDesignTokens</code></td>
<td>Apply custom design tokens for theming</td>
</tr>
<tr>
<td><code>show</code></td>
<td>-</td>
<td>Display the dialog</td>
</tr>
<tr>
<td><code>dismiss</code></td>
<td>-</td>
<td>Dismiss the dialog</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-kotlin">val rtkJoinStage = RtkJoinStageDialog(requireContext())&#10;rtkJoinStage.show()&#10;rtkJoinStage.activate(meeting)&#10;</code></pre>
