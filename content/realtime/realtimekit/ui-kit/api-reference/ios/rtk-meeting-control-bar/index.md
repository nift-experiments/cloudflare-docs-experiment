<p>Control bar for group calls that extends <code>RtkControlBar</code> with microphone and video toggle buttons.</p>
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
<td><code>delegate</code></td>
<td><code>RtkTabBarDelegate?</code></td>
<td>✅</td>
<td>-</td>
<td>Delegate for handling tab bar interactions</td>
</tr>
<tr>
<td><code>presentingViewController</code></td>
<td><code>UIViewController</code></td>
<td>✅</td>
<td>-</td>
<td>View controller used for presenting modal screens</td>
</tr>
<tr>
<td><code>appearance</code></td>
<td><code>RtkControlBarAppearance</code></td>
<td>❌</td>
<td><code>RtkControlBarAppearanceModel()</code></td>
<td>Appearance configuration for the control bar</td>
</tr>
<tr>
<td><code>settingViewControllerCompletion</code></td>
<td><code>(() -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Closure called when the settings view controller dismisses</td>
</tr>
<tr>
<td><code>onLeaveMeetingCompletion</code></td>
<td><code>(() -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Closure called when the participant leaves the meeting</td>
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
<td><code>dataSource</code></td>
<td><code>RtkMeetingControlBarDataSource?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Data source for customizing control bar buttons</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let controlBar = RtkMeetingControlBar(&#10;    meeting: rtkClient,&#10;    delegate: self,&#10;    presentingViewController: self&#10;)&#10;view.addSubview(controlBar)&#10;</code></pre>
<h3 id="with-leave-meeting-handler">With leave meeting handler</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let controlBar = RtkMeetingControlBar(&#10;    meeting: rtkClient,&#10;    delegate: self,&#10;    presentingViewController: self,&#10;    onLeaveMeetingCompletion: {&#10;        self.navigationController?.popViewController(animated: true)&#10;    }&#10;)&#10;view.addSubview(controlBar)&#10;</code></pre>
