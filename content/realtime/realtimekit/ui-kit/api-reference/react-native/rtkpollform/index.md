<p>Form for creating a new poll with question, dynamic options, anonymous voting, and hide results toggles.</p>
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
<tr>
<td><code>onRtkCreatePoll</code></td>
<td><code>any</code></td>
<td>❌</td>
<td>-</td>
<td>Callback when poll is created (receives question, options, anonymous, hideVotes)</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkPollForm } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkPollForm onRtkCreatePoll={(data) =&gt; handleCreatePoll(data)} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkPollForm } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkPollForm&#10;			onRtkCreatePoll={(data) =&gt; handleCreatePoll(data)}&#10;			iconPack={customIconPack}&#10;		/&gt;&#10;	);&#10;}&#10;</code></pre>
