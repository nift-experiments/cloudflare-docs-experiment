<p>A skeleton component used for composing custom controlbar buttons.</p>
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
<td><code>rtk_cbb_icon</code></td>
<td><code>reference</code></td>
<td>❌</td>
<td>-</td>
<td>Drawable resource for the button icon</td>
</tr>
<tr>
<td><code>rtk_cbb_variant</code></td>
<td><code>button | horizontal</code></td>
<td>❌</td>
<td><code>button</code></td>
<td>Layout variant</td>
</tr>
<tr>
<td><code>rtk_cbb_showText</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>true</code></td>
<td>Whether to show the label text</td>
</tr>
<tr>
<td><code>rtk_cbb_iconSize</code></td>
<td><code>dimension</code></td>
<td>❌</td>
<td>-</td>
<td>Size of the icon</td>
</tr>
<tr>
<td><code>rtk_cbb_iconPadding</code></td>
<td><code>dimension</code></td>
<td>❌</td>
<td>-</td>
<td>Padding between icon and label</td>
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
<td><code>setIconDrawable</code></td>
<td><code>drawable: Drawable?</code></td>
<td>Set the button icon</td>
</tr>
<tr>
<td><code>setIconTint</code></td>
<td><code>color: Int</code></td>
<td>Set the icon tint color</td>
</tr>
<tr>
<td><code>setText</code></td>
<td><code>text: String?</code></td>
<td>Set the button label text</td>
</tr>
<tr>
<td><code>setProcessingState</code></td>
<td><code>processing: Boolean</code></td>
<td>Show or hide a loading spinner</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.controlbarbuttons.RtkControlBarButton&#10;    android:id=&quot;@+id/rtk_control_bar_button&quot;&#10;    android:layout_width=&quot;wrap_content&quot;&#10;    android:layout_height=&quot;wrap_content&quot;&#10;    app:rtk_cbb_showText=&quot;true&quot;&#10;    app:rtk_cbb_variant=&quot;button&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val buttonView = findViewById&lt;RtkControlBarButton&gt;(R.id.rtk_control_bar_button)&#10;buttonView.setOnClickListener { }&#10;</code></pre>
