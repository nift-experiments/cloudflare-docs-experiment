<p>Displays the current viewer count for a livestream.</p>
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
<td><code>refresh</code></td>
<td><code>meeting: RealtimeKitClient</code></td>
<td>Update the viewer count based on the current meeting state</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.RtkLivestreamViewerCount&#10;    android:id=&quot;@+id/rtk_viewer_count&quot;&#10;    android:layout_width=&quot;wrap_content&quot;&#10;    android:layout_height=&quot;wrap_content&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val viewerCount = findViewById&lt;RtkLivestreamViewerCount&gt;(R.id.rtk_viewer_count)&#10;viewerCount.refresh(meeting)&#10;</code></pre>
