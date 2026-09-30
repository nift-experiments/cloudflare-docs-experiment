<p>A bottom sheet shown when tapping the more button. Contains options for participants, chat, polls, plugins, recording, screen share, mute all, and settings.</p>
<h2 id="methods">Methods</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Parameters</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>show</code></td>
<td><code>fragmentManager: FragmentManager, tag: String?</code></td>
<td>Display the meeting options bottom sheet</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-kotlin">val meetingOptions = RtkMeetingOptionBottomSheet()&#10;meetingOptions.show(fragmentManager, &quot;MEETING_OPTIONS_TAG&quot;)&#10;</code></pre>
