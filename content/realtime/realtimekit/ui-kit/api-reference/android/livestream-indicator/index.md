<p>A visual indicator that shows when a livestream is active.</p>
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
<td>Update the indicator based on the current livestream state</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.RtkLivestreamIndicator&#10;    android:id=&quot;@+id/rtk_livestream_indicator&quot;&#10;    android:layout_width=&quot;wrap_content&quot;&#10;    android:layout_height=&quot;wrap_content&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val indicator = findViewById&lt;RtkLivestreamIndicator&gt;(R.id.rtk_livestream_indicator)&#10;indicator.refresh(meeting)&#10;</code></pre>
