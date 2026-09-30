<p>A component which handles the sidebar and
you can customize which sections you want, and which section you want as the default.</p>
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
<td><code>config</code></td>
<td><code>UIConfig</code></td>
<td>❌</td>
<td><code>createDefaultConfig()</code></td>
<td>Config</td>
</tr>
<tr>
<td><code>defaultSection</code></td>
<td><code>RtkSidebarSection</code></td>
<td>✅</td>
<td>-</td>
<td>Default section</td>
</tr>
<tr>
<td><code>enabledSections</code></td>
<td><code>RtkSidebarTab[]</code></td>
<td>✅</td>
<td>-</td>
<td>Enabled sections in sidebar</td>
</tr>
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
<td>Meeting object</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size</code></td>
<td>✅</td>
<td>-</td>
<td>Size</td>
</tr>
<tr>
<td><code>states</code></td>
<td><code>States</code></td>
<td>✅</td>
<td>-</td>
<td>States object</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
<tr>
<td><code>view</code></td>
<td><code>RtkSidebarView</code></td>
<td>✅</td>
<td>-</td>
<td>View type</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-sidebar&gt;&lt;/rtk-sidebar&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-sidebar&#10; [defaultSection]=&quot;rtksidebarsection&quot;&#10; [enabledSections]=&quot;[]&quot;&#10; [meeting]=&quot;meeting&quot;&gt;&#10;&lt;/rtk-sidebar&gt;&#10;</code></pre>
