<p>A versatile button that follows the RTK Design System.
Supports multiple styles, states, and sizes.</p>
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
<td><code>style</code></td>
<td><code>Style</code></td>
<td>❌</td>
<td><code>.solid</code></td>
<td>The button style (solid, line, icon-left, and others)</td>
</tr>
<tr>
<td><code>rtkButtonState</code></td>
<td><code>States</code></td>
<td>❌</td>
<td><code>.active</code></td>
<td>The initial state of the button</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size</code></td>
<td>❌</td>
<td><code>.large</code></td>
<td>The size of the button</td>
</tr>
<tr>
<td><code>appearance</code></td>
<td><code>RtkButtonAppearance</code></td>
<td>❌</td>
<td>-</td>
<td>Appearance configuration for colors and fonts</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let button = RtkButton()&#10;button.setTitle(&quot;Join&quot;, for: .normal)&#10;view.addSubview(button)&#10;</code></pre>
<h3 id="with-custom-style">With custom style</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let button = RtkButton(&#10;    style: .line,&#10;    rtkButtonState: .active,&#10;    size: .large&#10;)&#10;button.setTitle(&quot;Cancel&quot;, for: .normal)&#10;view.addSubview(button)&#10;</code></pre>
