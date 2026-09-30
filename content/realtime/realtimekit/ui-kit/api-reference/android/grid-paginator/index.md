<p>A component which allows you to change the current page of the active participants grid.</p>
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
<td><code>rtkAndroidClient: RealtimeKitClient, uiTokens: RtkDesignTokens</code></td>
<td>Bind the paginator to the meeting state</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.RtkGridPaginatorView&#10;    android:id=&quot;@+id/rtk_grid_paginator&quot;&#10;    android:layout_width=&quot;wrap_content&quot;&#10;    android:layout_height=&quot;wrap_content&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val paginatorView = findViewById&lt;RtkGridPaginatorView&gt;(R.id.rtk_grid_paginator)&#10;paginatorView.activate(meeting)&#10;</code></pre>
