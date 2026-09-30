<p>A button that follows the RealtimeKit design system.</p>
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
<td><code>rtk_btn_variant</code></td>
<td><code>primary | secondary | danger</code></td>
<td>❌</td>
<td>-</td>
<td>Button variant</td>
</tr>
</tbody>
</table>
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
<td><code>applyDesignTokens</code></td>
<td><code>designTokens: RtkDesignTokens</code></td>
<td>Apply custom design tokens for theming</td>
</tr>
<tr>
<td><code>refresh</code></td>
<td><code>uiTokens: RtkDesignTokens</code></td>
<td>Refresh the button with the provided tokens</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.button.RtkButton&#10;    android:id=&quot;@+id/btn_id&quot;&#10;    android:layout_width=&quot;200dp&quot;&#10;    android:layout_height=&quot;48dp&quot;&#10;    android:text=&quot;Text on Button&quot;&#10;    app:rtk_btn_variant=&quot;primary&quot; /&gt;&#10;</code></pre>
