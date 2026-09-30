<p>The top-level design token container for customizing the look and feel of all UI Kit components.</p>
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
<td><code>colors</code></td>
<td><code>RtkColorTokens</code></td>
<td>❌</td>
<td>-</td>
<td>Color theme tokens</td>
</tr>
<tr>
<td><code>borderWidth</code></td>
<td><code>RtkBorderWidthToken</code></td>
<td>❌</td>
<td>-</td>
<td>Border width token</td>
</tr>
<tr>
<td><code>borderRadius</code></td>
<td><code>RtkBorderRadiusToken</code></td>
<td>❌</td>
<td>-</td>
<td>Border radius token</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-kotlin">val designTokens = RtkDesignTokens(&#10;    colors = RtkColorTokens(&#10;        brand = BrandColor(&#10;            shade300 = Color.parseColor(&quot;#497CFD&quot;),&#10;            shade400 = Color.parseColor(&quot;#356EFD&quot;),&#10;            shade500 = Color.parseColor(&quot;#2160FD&quot;),&#10;            shade600 = Color.parseColor(&quot;#0D52FD&quot;),&#10;            shade700 = Color.parseColor(&quot;#0046E5&quot;)&#10;        ),&#10;        background = BackgroundColor(&#10;            shade600 = Color.parseColor(&quot;#2C2C2C&quot;),&#10;            shade700 = Color.parseColor(&quot;#242424&quot;),&#10;            shade800 = Color.parseColor(&quot;#1C1C1C&quot;),&#10;            shade900 = Color.parseColor(&quot;#141414&quot;),&#10;            shade1000 = Color.parseColor(&quot;#0C0C0C&quot;)&#10;        )&#10;    ),&#10;    borderRadius = RtkBorderRadiusToken.Rounded,&#10;    borderWidth = RtkBorderWidthToken.Thin&#10;)&#10;</code></pre>
