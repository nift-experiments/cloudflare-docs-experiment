<p>A full-screen error view that displays an error message and a retry button.</p>
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
<td><code>errorMessage: String, onRetryClicked: () -&gt; Unit</code></td>
<td>Set the error message and retry button callback</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.RtkErrorView&#10;    android:id=&quot;@+id/rtk_error_view&quot;&#10;    android:layout_width=&quot;match_parent&quot;&#10;    android:layout_height=&quot;match_parent&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val errorView = findViewById&lt;RtkErrorView&gt;(R.id.rtk_error_view)&#10;errorView.refresh(&quot;Failed to connect&quot;) {&#10;    // Retry connection&#10;}&#10;</code></pre>
