<p>A component which lists all available plugins from their preset, with the ability to enable or disable plugins.</p>
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
<td><code>show</code></td>
<td><code>fragmentManager: FragmentManager, tag: String?</code></td>
<td>Display the plugins bottom sheet</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-kotlin">val rtkPluginsBottomSheet = RtkPluginsBottomSheet()&#10;rtkPluginsBottomSheet.show(fragmentManager, &quot;PLUGINS_TAG&quot;)&#10;</code></pre>
