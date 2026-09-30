<p>A pre-built control bar for webinar meetings. Contains mic toggle, camera toggle, webinar stage toggle, more toggle, and leave button.</p>
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
<td>Bind the control bar to the meeting state</td>
</tr>
<tr>
<td><code>deactivate</code></td>
<td>-</td>
<td>Unbind the control bar and remove event listeners</td>
</tr>
<tr>
<td><code>refreshStageToggleButton</code></td>
<td>-</td>
<td>Force a refresh of the stage toggle button state</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.controlbars.RtkWebinarControlBarView&#10;    android:id=&quot;@+id/rtk_webinar_control_bar&quot;&#10;    android:layout_width=&quot;match_parent&quot;&#10;    android:layout_height=&quot;wrap_content&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val controlBar = findViewById&lt;RtkWebinarControlBarView&gt;(R.id.rtk_webinar_control_bar)&#10;controlBar.activate(meeting)&#10;</code></pre>
