<p>A small circular badge view that displays a notification count.
Hides automatically when the count is zero and shows &quot;99+&quot; for counts over 99.</p>
<h2 id="methods">Methods</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Return Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>setBadgeCount(_:)</code></td>
<td><code>Void</code></td>
<td>Sets the badge count. Hides the badge at zero and displays &quot;99+&quot; for values over 99.</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let badge = RtkNotificationBadgeView()&#10;badge.setBadgeCount(5)&#10;view.addSubview(badge)&#10;</code></pre>
<h3 id="reset-badge">Reset badge</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let badge = RtkNotificationBadgeView()&#10;badge.setBadgeCount(3)&#10;view.addSubview(badge)&#10;&#10;// Hide the badge by setting count to zero&#10;badge.setBadgeCount(0)&#10;</code></pre>
