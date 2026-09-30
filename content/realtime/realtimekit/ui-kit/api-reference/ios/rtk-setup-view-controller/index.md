<p>Pre-meeting setup screen view controller.
Provides video preview, audio and video toggles, and name entry before joining a meeting.</p>
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
<td><code>meetingInfo</code></td>
<td><code>RtkMeetingInfo</code></td>
<td>✅</td>
<td>-</td>
<td>Meeting configuration with auth token and media settings</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>RealtimeKitClient</code></td>
<td>✅</td>
<td>-</td>
<td>The RealtimeKit client instance</td>
</tr>
<tr>
<td><code>completion</code></td>
<td><code>@escaping () -&gt; Void</code></td>
<td>✅</td>
<td>-</td>
<td>Closure called when setup completes</td>
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
<td><code>delegate</code></td>
<td><code>SetupViewControllerDelegate?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Delegate notified when the participant joins the meeting</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let setupVC = RtkSetupViewController(&#10;    meetingInfo: meetingInfo,&#10;    meeting: rtkClient,&#10;    completion: {&#10;        print(&quot;Setup complete&quot;)&#10;    }&#10;)&#10;self.present(setupVC, animated: true)&#10;</code></pre>
<h3 id="with-delegate">With delegate</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;class ViewController: UIViewController, SetupViewControllerDelegate {&#10;    func showSetupScreen() {&#10;        let setupVC = RtkSetupViewController(&#10;            meetingInfo: meetingInfo,&#10;            meeting: rtkClient,&#10;            completion: {&#10;                self.dismiss(animated: true)&#10;            }&#10;        )&#10;        setupVC.delegate = self&#10;        self.present(setupVC, animated: true)&#10;    }&#10;}&#10;</code></pre>
