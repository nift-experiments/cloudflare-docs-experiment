<p>A label that displays the current participant count.
Automatically updates when participants join or leave the meeting.</p>
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
<td><code>appearance</code></td>
<td><code>RtkTextAppearance</code></td>
<td>❌</td>
<td><code>AppTheme.shared.participantCountAppearance</code></td>
<td>Text appearance configuration for font and color</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let countView = RtkParticipantCountView(meeting: rtkClient)&#10;view.addSubview(countView)&#10;</code></pre>
<h3 id="with-custom-appearance">With custom appearance</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let appearance = RtkTextAppearance(&#10;    font: UIFont.systemFont(ofSize: 14, weight: .medium),&#10;    textColor: .lightGray&#10;)&#10;let countView = RtkParticipantCountView(&#10;    meeting: rtkClient,&#10;    appearance: appearance&#10;)&#10;view.addSubview(countView)&#10;</code></pre>
