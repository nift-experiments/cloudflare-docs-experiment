<p>A control bar button that ends or leaves the meeting.
Optionally displays a confirmation dialog before ending the meeting.</p>
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
<td><code>alertViewController</code></td>
<td><code>UIViewController</code></td>
<td>✅</td>
<td>-</td>
<td>View controller used to present the confirmation alert</td>
</tr>
<tr>
<td><code>onClick</code></td>
<td><code>((RtkEndMeetingControlBarButton, RtkLeaveDialog.RtkLeaveDialogAlertButtonType) -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Closure called after the user confirms leaving or ending the meeting, receiving the button and the selected action type</td>
</tr>
<tr>
<td><code>appearance</code></td>
<td><code>RtkControlBarButtonAppearance</code></td>
<td>❌</td>
<td>-</td>
<td>Appearance configuration for the button</td>
</tr>
</tbody>
</table>
<h2 id="properties">Properties</h2>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>shouldShowAlertOnClick</code></td>
<td><code>Bool</code></td>
<td>❌</td>
<td><code>true</code></td>
<td>Whether to show a confirmation alert before ending the meeting</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let endButton = RtkEndMeetingControlBarButton(&#10;    meeting: rtkClient,&#10;    alertViewController: self&#10;)&#10;view.addSubview(endButton)&#10;</code></pre>
<h3 id="without-confirmation-dialog">Without confirmation dialog</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let endButton = RtkEndMeetingControlBarButton(&#10;    meeting: rtkClient,&#10;    alertViewController: self,&#10;    onClick: { button, actionType in&#10;        print(&quot;Action: \(actionType)&quot;)&#10;    }&#10;)&#10;endButton.shouldShowAlertOnClick = false&#10;view.addSubview(endButton)&#10;</code></pre>
