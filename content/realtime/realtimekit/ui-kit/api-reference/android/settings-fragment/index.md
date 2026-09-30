<p>A settings dialog that contains audio and video device selectors and a self-preview tile. Used in landscape orientation.</p>
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
<td>Display the settings dialog</td>
</tr>
<tr>
<td><code>setBottomSheetEnabled</code></td>
<td><code>onClick: () -&gt; Unit</code></td>
<td>Enable a button to switch to the bottom sheet view</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-kotlin">val settingsFragment = RtkSettingsFragment()&#10;settingsFragment.show(fragmentManager, &quot;SETTINGS_TAG&quot;)&#10;</code></pre>
