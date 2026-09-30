<p>A dialog that presents leave and end meeting options.
Displays different options based on host permissions.</p>
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
<td><code>onClick</code></td>
<td><code>((RtkLeaveDialogAlertButtonType) -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Closure called when the user selects a dialog option</td>
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
<td><code>show(on:)</code></td>
<td><code>Void</code></td>
<td>Presents the leave dialog on the specified view controller</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let leaveDialog = RtkLeaveDialog(meeting: rtkClient)&#10;leaveDialog.show(on: self)&#10;</code></pre>
<h3 id="with-selection-handler">With selection handler</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let leaveDialog = RtkLeaveDialog(&#10;    meeting: rtkClient,&#10;    onClick: { buttonType in&#10;        switch buttonType {&#10;        case .leaveMeeting:&#10;            print(&quot;Leaving meeting&quot;)&#10;        case .endMeeting:&#10;            print(&quot;Ending meeting for all&quot;)&#10;        default:&#10;            break&#10;        }&#10;    }&#10;)&#10;leaveDialog.show(on: self)&#10;</code></pre>
