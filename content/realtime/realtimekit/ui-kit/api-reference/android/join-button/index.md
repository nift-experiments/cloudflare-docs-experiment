<p>A button that performs the room join operation. Displays &quot;Join&quot; by default and changes to &quot;Joining...&quot; during the join process. Automatically disables after a successful join.</p>
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
<td><code>meeting: RealtimeKitClient, localUserNameField: EditText?</code></td>
<td>Bind the button to the meeting state. Pass an optional <code>EditText</code> reference to validate the display name before joining — if the user has <code>canEditDisplayName</code> permission and the field is blank, the button shows a &quot;Please enter name&quot; toast and blocks the join.</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.RtkJoinButton&#10;    android:id=&quot;@+id/rtk_join_button&quot;&#10;    android:layout_width=&quot;wrap_content&quot;&#10;    android:layout_height=&quot;48dp&quot;&#10;    app:rtk_btn_variant=&quot;primary&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val joinButton = findViewById&lt;RtkJoinButton&gt;(R.id.rtk_join_button)&#10;val nameField = findViewById&lt;EditText&gt;(R.id.name_field)&#10;joinButton.activate(meeting, nameField)&#10;</code></pre>
