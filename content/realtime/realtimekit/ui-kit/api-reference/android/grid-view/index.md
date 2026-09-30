<p>The main grid component which handles the participant grid layout, pagination, and focus modes.</p>
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
<td>Bind the grid to the meeting state</td>
</tr>
<tr>
<td><code>refresh</code></td>
<td><code>force: Boolean</code></td>
<td>Force a refresh of the grid layout and participants</td>
</tr>
<tr>
<td><code>enableFocusMode</code></td>
<td>-</td>
<td>Enable focus mode, which hides the horizontal peer strip and full-screen toggle to keep attention on the primary speaker or shared content</td>
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
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.grid.RtkGridView&#10;    android:id=&quot;@+id/rtk_grid&quot;&#10;    android:layout_width=&quot;match_parent&quot;&#10;    android:layout_height=&quot;match_parent&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val grid = findViewById&lt;RtkGridView&gt;(R.id.rtk_grid)&#10;grid.activate(meeting)&#10;</code></pre>
