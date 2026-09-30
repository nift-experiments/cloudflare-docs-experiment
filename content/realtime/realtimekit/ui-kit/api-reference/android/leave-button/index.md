<p>A button which toggles visibility of the leave confirmation dialog.</p>
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
<td>Bind the button to the meeting state</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.controlbarbuttons.RtkLeaveButton&#10;    android:id=&quot;@+id/rtk_leave_button&quot;&#10;    android:layout_width=&quot;48dp&quot;&#10;    android:layout_height=&quot;48dp&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val leaveButton = findViewById&lt;RtkLeaveButton&gt;(R.id.rtk_leave_button)&#10;leaveButton.activate(meeting)&#10;</code></pre>
