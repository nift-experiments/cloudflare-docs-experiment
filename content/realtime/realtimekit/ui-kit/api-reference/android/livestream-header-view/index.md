<p>A pre-built header for livestream meetings. Contains the livestream indicator, viewer count, clock, and meeting title.</p>
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
<td>Bind the header to the meeting state</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.RtkLivestreamHeaderView&#10;    android:id=&quot;@+id/rtk_livestream_header&quot;&#10;    android:layout_width=&quot;match_parent&quot;&#10;    android:layout_height=&quot;wrap_content&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val header = findViewById&lt;RtkLivestreamHeaderView&gt;(R.id.rtk_livestream_header)&#10;header.activate(meeting)&#10;</code></pre>
