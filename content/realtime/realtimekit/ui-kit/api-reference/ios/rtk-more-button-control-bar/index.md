<p>A control bar button that opens a bottom sheet menu with meeting actions such as chat, polls, and participant list.</p>
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
<td>The RealtimeKit client instance</td>
</tr>
<tr>
<td><code>presentingViewController</code></td>
<td><code>UIViewController</code></td>
<td>✅</td>
<td>-</td>
<td>View controller used to present the bottom sheet</td>
</tr>
<tr>
<td><code>settingViewControllerCompletion</code></td>
<td><code>(() -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Closure called when the settings view controller dismisses</td>
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
<td><code>hideBottomSheet()</code></td>
<td><code>Void</code></td>
<td>Programmatically dismisses the bottom sheet menu</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let moreButton = RtkMoreButtonControlBar(&#10;    meeting: rtkClient,&#10;    presentingViewController: self&#10;)&#10;view.addSubview(moreButton)&#10;</code></pre>
<h3 id="with-settings-completion">With settings completion</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let moreButton = RtkMoreButtonControlBar(&#10;    meeting: rtkClient,&#10;    presentingViewController: self,&#10;    settingViewControllerCompletion: {&#10;        print(&quot;Settings dismissed&quot;)&#10;    }&#10;)&#10;view.addSubview(moreButton)&#10;</code></pre>
