<p>A circular avatar view that displays a participant's profile image or name initials as a fallback.</p>
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
<td><code>participant</code></td>
<td><code>RtkMeetingParticipant</code></td>
<td>✅</td>
<td>-</td>
<td>The participant whose avatar to display</td>
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
<td>Updates the avatar to display a different participant</td>
</tr>
<tr>
<td><code>refresh()</code></td>
<td><code>Void</code></td>
<td>Refreshes the avatar image or initials</td>
</tr>
<tr>
<td><code>setInitialName(font:)</code></td>
<td><code>Void</code></td>
<td>Sets the font used for rendering name initials</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let avatarView = RtkAvatarView(participant: participant)&#10;view.addSubview(avatarView)&#10;</code></pre>
<h3 id="update-participant">Update participant</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let avatarView = RtkAvatarView(participant: participant)&#10;view.addSubview(avatarView)&#10;&#10;// Update to a different participant&#10;avatarView.set(participant: newParticipant)&#10;avatarView.refresh()&#10;</code></pre>
