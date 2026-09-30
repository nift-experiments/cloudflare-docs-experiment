<p>The main meeting screen view controller.
Displays the participant grid, plugins, screen share, header, and control bar.</p>
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
<tr>
<td><code>completion</code></td>
<td><code>@escaping () -&gt; Void</code></td>
<td>✅</td>
<td>-</td>
<td>Closure called when the meeting ends</td>
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
<td><code>MeetingViewControllerDataSource?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Data source for providing custom topbar, middle view, and bottom bar</td>
</tr>
</tbody>
</table>
<h2 id="meetingviewcontrollerdatasource-protocol">MeetingViewControllerDataSource protocol</h2>
<p>Implement this protocol to provide custom UI sections within the meeting screen.</p>
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
<td><code>getTopbar(viewController:)</code></td>
<td><code>RtkMeetingHeaderView?</code></td>
<td>Returns a custom header view for the meeting screen</td>
</tr>
<tr>
<td><code>getMiddleView(viewController:)</code></td>
<td><code>UIView?</code></td>
<td>Returns a custom middle view between the header and control bar</td>
</tr>
<tr>
<td><code>getBottomTabbar(viewController:)</code></td>
<td><code>RtkMeetingControlBar?</code></td>
<td>Returns a custom control bar for the meeting screen</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let meetingVC = MeetingViewController(&#10;    meeting: rtkClient,&#10;    completion: {&#10;        self.dismiss(animated: true)&#10;    }&#10;)&#10;meetingVC.modalPresentationStyle = .fullScreen&#10;self.present(meetingVC, animated: true)&#10;</code></pre>
<h3 id="with-custom-data-source">With custom data source</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;class CustomDataSource: MeetingViewControllerDataSource {&#10;    func getTopbar(viewController: MeetingViewController) -&gt; RtkMeetingHeaderView? {&#10;        return RtkMeetingHeaderView(meeting: rtkClient)&#10;    }&#10;&#10;    func getMiddleView(viewController: MeetingViewController) -&gt; UIView? {&#10;        return nil&#10;    }&#10;&#10;    func getBottomTabbar(viewController: MeetingViewController) -&gt; RtkMeetingControlBar? {&#10;        return nil&#10;    }&#10;}&#10;&#10;let meetingVC = MeetingViewController(&#10;    meeting: rtkClient,&#10;    completion: {&#10;        self.dismiss(animated: true)&#10;    }&#10;)&#10;meetingVC.dataSource = CustomDataSource()&#10;self.present(meetingVC, animated: true)&#10;</code></pre>
