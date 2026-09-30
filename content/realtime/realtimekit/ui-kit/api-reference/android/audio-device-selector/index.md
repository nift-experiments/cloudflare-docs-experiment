<p>An audio device selector component which can be used to select audio devices.</p>
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
<td><code>rtk_ds_label</code></td>
<td><code>string</code></td>
<td>❌</td>
<td><code>Audio</code></td>
<td>Custom label text</td>
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
<td><code>activate</code></td>
<td><code>meeting: RealtimeKitClient</code></td>
<td>Bind the selector to the meeting state</td>
</tr>
<tr>
<td><code>disableLabel</code></td>
<td>-</td>
<td>Disable the label text above the dropdown</td>
</tr>
<tr>
<td><code>applyDesignTokens</code></td>
<td><code>designTokens: RtkDesignTokens</code></td>
<td>Apply custom design tokens for theming</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.RtkAudioDeviceSelector&#10;    android:id=&quot;@+id/audioSelector&quot;&#10;    app:rtk_ds_label=&quot;Audio&quot;&#10;    android:layout_width=&quot;0dp&quot;&#10;    android:layout_height=&quot;wrap_content&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val audioSelector = findViewById&lt;RtkAudioDeviceSelector&gt;(R.id.audioSelector)&#10;audioSelector.activate(meeting)&#10;</code></pre>
