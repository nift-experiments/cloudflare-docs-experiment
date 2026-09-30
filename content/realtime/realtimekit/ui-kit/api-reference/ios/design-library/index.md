<p>The central design token library providing color, spacing, border width, and border radius tokens.
Access through the <code>DesignLibrary.shared</code> singleton.</p>
<h2 id="access">Access</h2>
<pre><code class="language-swift">let designLibrary = DesignLibrary.shared&#10;</code></pre>
<h2 id="properties">Properties</h2>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>color</code></td>
<td><code>ColorTokens</code></td>
<td>-</td>
<td>-</td>
<td>Color tokens for backgrounds, text, and brand colors</td>
</tr>
<tr>
<td><code>space</code></td>
<td><code>SpaceToken</code></td>
<td>-</td>
<td>-</td>
<td>Spacing tokens for margins and padding</td>
</tr>
<tr>
<td><code>borderSize</code></td>
<td><code>BorderWidthToken</code></td>
<td>-</td>
<td>-</td>
<td>Border width tokens</td>
</tr>
<tr>
<td><code>borderRadius</code></td>
<td><code>BorderRadiusToken</code></td>
<td>-</td>
<td>-</td>
<td>Border radius tokens for corner rounding</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="access-design-tokens">Access design tokens</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let designLibrary = DesignLibrary.shared&#10;&#10;// Access color tokens&#10;let backgroundColor = designLibrary.color.background&#10;let textColor = designLibrary.color.text&#10;&#10;// Access spacing tokens&#10;let padding = designLibrary.space.space4&#10;&#10;// Access border tokens&#10;let borderWidth = designLibrary.borderSize.thin&#10;let cornerRadius = designLibrary.borderRadius.rounded&#10;</code></pre>
