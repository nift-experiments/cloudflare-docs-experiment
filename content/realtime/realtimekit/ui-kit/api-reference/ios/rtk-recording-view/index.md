<p>A blinking recording indicator displayed when the meeting is being recorded.
Shows a red dot with configurable text and image.</p>
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
<td><code>title</code></td>
<td><code>String</code></td>
<td>❌</td>
<td><code>&quot;Rec&quot;</code></td>
<td>Text label displayed next to the recording indicator</td>
</tr>
<tr>
<td><code>image</code></td>
<td><code>RtkImage?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Custom image for the recording indicator</td>
</tr>
<tr>
<td><code>appearance</code></td>
<td><code>RtkRecordingViewAppearance</code></td>
<td>❌</td>
<td>-</td>
<td>Appearance configuration for the recording indicator</td>
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
<td><code>blinking(start: Bool)</code></td>
<td><code>Void</code></td>
<td>Starts or stops the blinking animation on the recording indicator</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let recordingView = RtkRecordingView(meeting: rtkClient)&#10;view.addSubview(recordingView)&#10;</code></pre>
<h3 id="with-custom-title">With custom title</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let recordingView = RtkRecordingView(&#10;    meeting: rtkClient,&#10;    title: &quot;Recording&quot;&#10;)&#10;view.addSubview(recordingView)&#10;</code></pre>
