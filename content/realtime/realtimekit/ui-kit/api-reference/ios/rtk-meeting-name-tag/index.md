<p>A name tag view that displays the participant name and a microphone status icon.
Automatically updates when the participant's audio state changes.</p>
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
<td><code>participant</code></td>
<td><code>RtkMeetingParticipant</code></td>
<td>✅</td>
<td>-</td>
<td>The participant whose name and mic status to display</td>
</tr>
<tr>
<td><code>appearance</code></td>
<td><code>RtkNameTagAppearance</code></td>
<td>❌</td>
<td>-</td>
<td>Appearance configuration for the name tag</td>
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
<td><code>set(participant:)</code></td>
<td><code>Void</code></td>
<td>Updates the name tag to display a different participant</td>
</tr>
<tr>
<td><code>refresh()</code></td>
<td><code>Void</code></td>
<td>Refreshes the name and microphone status display</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let nameTag = RtkMeetingNameTag(&#10;    meeting: rtkClient,&#10;    participant: participant&#10;)&#10;view.addSubview(nameTag)&#10;</code></pre>
<h3 id="update-participant">Update participant</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let nameTag = RtkMeetingNameTag(&#10;    meeting: rtkClient,&#10;    participant: participant&#10;)&#10;view.addSubview(nameTag)&#10;&#10;// Switch to a different participant&#10;nameTag.set(participant: newParticipant)&#10;nameTag.refresh()&#10;</code></pre>
