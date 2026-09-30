<p>A themed label that uses design token colors and fonts from the RTK Design System.</p>
<h2 id="initializer-parameters">Initializer parameters</h2>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>appearance</code></td>
<td><code>RtkTextAppearance</code></td>
<td>❌</td>
<td>-</td>
<td>Text appearance configuration for font and color</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let label = RtkLabel()&#10;label.text = &quot;Meeting Room&quot;&#10;view.addSubview(label)&#10;</code></pre>
<h3 id="with-custom-appearance">With custom appearance</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let appearance = RtkTextAppearance(&#10;    font: UIFont.systemFont(ofSize: 16, weight: .semibold),&#10;    textColor: .white&#10;)&#10;let label = RtkLabel(appearance: appearance)&#10;label.text = &quot;Meeting Room&quot;&#10;view.addSubview(label)&#10;</code></pre>
