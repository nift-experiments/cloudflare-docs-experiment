<p>A tab button used in the plugin and screen share tab selector.
Represents a single tab in the <code>RtkActiveTabSelectorView</code>.</p>
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
<td><code>image</code></td>
<td><code>RtkImage?</code></td>
<td>✅</td>
<td>-</td>
<td>The icon image for the tab button</td>
</tr>
<tr>
<td><code>title</code></td>
<td><code>String</code></td>
<td>❌</td>
<td><code>&quot;&quot;</code></td>
<td>The title text for the tab button</td>
</tr>
<tr>
<td><code>id</code></td>
<td><code>String</code></td>
<td>❌</td>
<td><code>&quot;&quot;</code></td>
<td>A unique identifier for the tab button</td>
</tr>
<tr>
<td><code>appearance</code></td>
<td><code>RtkPluginScreenShareTabButtonAppearance</code></td>
<td>❌</td>
<td>-</td>
<td>Appearance configuration for the tab button</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let tabButton = RtkPluginScreenShareTabButton(&#10;    image: RtkImage(image: UIImage(systemName: &quot;square.and.arrow.up&quot;)),&#10;    title: &quot;Screen Share&quot;&#10;)&#10;</code></pre>
<h3 id="with-identifier">With identifier</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let tabButton = RtkPluginScreenShareTabButton(&#10;    image: RtkImage(image: UIImage(systemName: &quot;pencil.tip&quot;)),&#10;    title: &quot;Whiteboard&quot;,&#10;    id: &quot;whiteboard-plugin&quot;&#10;)&#10;</code></pre>
