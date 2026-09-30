<p>Base button class for control bar items.
Supports normal and selected states, notification badges, and theming through appearance configuration.</p>
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
<td><code>RtkImage</code></td>
<td>✅</td>
<td>-</td>
<td>The icon image for the button</td>
</tr>
<tr>
<td><code>title</code></td>
<td><code>String</code></td>
<td>❌</td>
<td><code>&quot;&quot;</code></td>
<td>The title text displayed below the icon</td>
</tr>
<tr>
<td><code>appearance</code></td>
<td><code>RtkControlBarButtonAppearance</code></td>
<td>❌</td>
<td>-</td>
<td>Appearance configuration for colors and styling</td>
</tr>
</tbody>
</table>
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
<td><code>selectedStateTintColor</code></td>
<td><code>UIColor</code></td>
<td>❌</td>
<td>-</td>
<td>Tint color applied when the button is in the selected state</td>
</tr>
<tr>
<td><code>normalStateTintColor</code></td>
<td><code>UIColor</code></td>
<td>❌</td>
<td>-</td>
<td>Tint color applied when the button is in the normal state</td>
</tr>
<tr>
<td><code>notificationBadge</code></td>
<td><code>RtkNotificationBadgeView</code></td>
<td>-</td>
<td>-</td>
<td>Badge view for displaying notification counts</td>
</tr>
</tbody>
</table>
<h2 id="methods">Methods</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Return Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>setSelected(image:title:)</code></td>
<td><code>Void</code></td>
<td>Sets the button to the selected state with a custom image and title</td>
</tr>
<tr>
<td><code>setDefault(image:title:)</code></td>
<td><code>Void</code></td>
<td>Sets the button to the default state with a custom image and title</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let button = RtkControlBarButton(&#10;    image: RtkImage(image: UIImage(systemName: &quot;mic&quot;)),&#10;    title: &quot;Mute&quot;&#10;)&#10;view.addSubview(button)&#10;</code></pre>
<h3 id="with-state-changes">With state changes</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let button = RtkControlBarButton(&#10;    image: RtkImage(image: UIImage(systemName: &quot;mic&quot;)),&#10;    title: &quot;Mute&quot;&#10;)&#10;&#10;// Switch to selected state&#10;button.setSelected(&#10;    image: RtkImage(image: UIImage(systemName: &quot;mic.slash&quot;)),&#10;    title: &quot;Unmute&quot;&#10;)&#10;&#10;// Switch back to default state&#10;button.setDefault(&#10;    image: RtkImage(image: UIImage(systemName: &quot;mic&quot;)),&#10;    title: &quot;Mute&quot;&#10;)&#10;view.addSubview(button)&#10;</code></pre>
