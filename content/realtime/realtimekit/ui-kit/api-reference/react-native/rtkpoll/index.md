<p>Renders a single poll with question, votable options, vote counts, and voter avatars.</p>
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
<td><code>poll</code></td>
<td><code>Poll</code></td>
<td>✅</td>
<td>-</td>
<td>The poll object to display</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>RealtimeKitClient</code></td>
<td>✅</td>
<td>-</td>
<td>The RealtimeKit meeting instance</td>
</tr>
<tr>
<td><code>onRtkVotePoll</code></td>
<td><code>any</code></td>
<td>❌</td>
<td>-</td>
<td>Callback when a vote is cast (receives option index)</td>
</tr>
<tr>
<td><code>self</code></td>
<td><code>string</code></td>
<td>❌</td>
<td>-</td>
<td>Self user ID</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Custom icon pack</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td>-</td>
<td>i18n translation function</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkPoll } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkPoll poll={poll} meeting={meeting} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkPoll } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkPoll&#10;			poll={poll}&#10;			meeting={meeting}&#10;			onRtkVotePoll={(index) =&gt; handleVote(index)}&#10;			self={selfUserId}&#10;		/&gt;&#10;	);&#10;}&#10;</code></pre>
