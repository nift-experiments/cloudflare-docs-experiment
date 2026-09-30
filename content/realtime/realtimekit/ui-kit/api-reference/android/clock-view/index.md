<p>A clock component which shows the elapsed time of a meeting.</p>
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
<td>Bind the clock to the meeting state</td>
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
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.RtkClockView&#10;    android:id=&quot;@+id/rtk_clock_view&quot;&#10;    android:layout_width=&quot;wrap_content&quot;&#10;    android:layout_height=&quot;wrap_content&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val clockView = findViewById&lt;RtkClockView&gt;(R.id.rtk_clock_view)&#10;clockView.activate(meeting)&#10;</code></pre>
