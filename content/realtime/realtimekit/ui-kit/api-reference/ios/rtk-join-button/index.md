<p>A pre-configured button that joins the meeting.
Validates the participant name before joining.</p>
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
<td><code>((RtkJoinButton, Bool) -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Closure called when the button is tapped. The <code>Bool</code> parameter indicates whether the join was successful.</td>
</tr>
<tr>
<td><code>appearance</code></td>
<td><code>RtkButtonAppearance</code></td>
<td>❌</td>
<td>-</td>
<td>Appearance configuration for the button</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let joinButton = RtkJoinButton(meeting: rtkClient)&#10;view.addSubview(joinButton)&#10;</code></pre>
<h3 id="with-tap-handler">With tap handler</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let joinButton = RtkJoinButton(&#10;    meeting: rtkClient,&#10;    onClick: { button, success in&#10;        if success {&#10;            print(&quot;Joined meeting&quot;)&#10;        } else {&#10;            print(&quot;Join failed&quot;)&#10;        }&#10;    }&#10;)&#10;view.addSubview(joinButton)&#10;</code></pre>
