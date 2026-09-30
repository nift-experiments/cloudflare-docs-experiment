<p>Meeting header view that displays the meeting title, participant count, elapsed time clock, recording indicator, and camera switch button.</p>
<h2 id="initializer-parameters">Initializer parameters</h2>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>meeting</code></td>
<td><code>RealtimeKitClient</code></td>
<td>✅</td>
<td>-</td>
<td>The RealtimeKit client instance for the active meeting</td>
</tr>
</tbody>
</table>
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
<td><code>setContentTop(offset: CGFloat)</code></td>
<td><code>Void</code></td>
<td>Sets the top content offset for the header layout</td>
</tr>
<tr>
<td><code>refreshNextPreviousButtonState()</code></td>
<td><code>Void</code></td>
<td>Refreshes the enabled state of next and previous page buttons</td>
</tr>
<tr>
<td><code>setClicks(nextButton:previousButton:)</code></td>
<td><code>Void</code></td>
<td>Assigns tap handlers for the next and previous page buttons</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let headerView = RtkMeetingHeaderView(meeting: rtkClient)&#10;view.addSubview(headerView)&#10;</code></pre>
<h3 id="with-page-navigation">With page navigation</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let headerView = RtkMeetingHeaderView(meeting: rtkClient)&#10;headerView.setClicks(&#10;    nextButton: { print(&quot;Next page&quot;) },&#10;    previousButton: { print(&quot;Previous page&quot;) }&#10;)&#10;headerView.refreshNextPreviousButtonState()&#10;view.addSubview(headerView)&#10;</code></pre>
