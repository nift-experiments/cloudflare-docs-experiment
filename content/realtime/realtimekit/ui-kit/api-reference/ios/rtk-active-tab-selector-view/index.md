<p>A horizontally scrollable tab selector for switching between plugins and screen shares.</p>
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
<td><code>buttons</code></td>
<td><code>[RtkPluginScreenShareTabButton]</code></td>
<td>-</td>
<td>-</td>
<td>The array of tab buttons in the selector</td>
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
<td><code>scrollToVisible(button:)</code></td>
<td><code>Void</code></td>
<td>Scrolls the tab selector to make the specified button visible</td>
</tr>
<tr>
<td><code>setAndDisplayButtons(_:)</code></td>
<td><code>Void</code></td>
<td>Sets and displays the provided array of tab buttons</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let tabSelector = RtkActiveTabSelectorView()&#10;let buttons = [&#10;    RtkPluginScreenShareTabButton(image: nil, title: &quot;Screen Share&quot;),&#10;    RtkPluginScreenShareTabButton(image: nil, title: &quot;Whiteboard&quot;)&#10;]&#10;tabSelector.setAndDisplayButtons(buttons)&#10;view.addSubview(tabSelector)&#10;</code></pre>
