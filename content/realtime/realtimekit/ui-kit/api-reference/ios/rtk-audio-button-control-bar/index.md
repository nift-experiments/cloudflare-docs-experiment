<p>A control bar button that toggles the local microphone on and off.
Checks microphone permissions before toggling.</p>
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
<td><code>((RtkAudioButtonControlBar) -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Closure called when the button is tapped</td>
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
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let audioButton = RtkAudioButtonControlBar(meeting: rtkClient)&#10;view.addSubview(audioButton)&#10;</code></pre>
<h3 id="with-tap-handler">With tap handler</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let audioButton = RtkAudioButtonControlBar(&#10;    meeting: rtkClient,&#10;    onClick: { button in&#10;        print(&quot;Audio toggled&quot;)&#10;    }&#10;)&#10;view.addSubview(audioButton)&#10;</code></pre>
