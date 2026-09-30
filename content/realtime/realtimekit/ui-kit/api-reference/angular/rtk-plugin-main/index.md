<p>A component which renders a plugin's UI.</p>
<p>The plugin's <code>component</code> (an HTMLElement) is placed into this element's
light DOM and projected into the shadow DOM layout via a <code>&lt;slot&gt;</code>.
This ensures external CSS from the consuming application continues
to apply to the plugin content.</p>
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
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>Meeting</code></td>
<td>✅</td>
<td>-</td>
<td>Meeting</td>
</tr>
<tr>
<td><code>plugin</code></td>
<td><code>RTKPlugin</code></td>
<td>✅</td>
<td>-</td>
<td>Plugin</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-plugin-main&gt;&lt;/rtk-plugin-main&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-plugin-main&#10; [meeting]=&quot;meeting&quot;&#10; [plugin]=&quot;rtkplugin&quot;&gt;&#10;&lt;/rtk-plugin-main&gt;&#10;</code></pre>
