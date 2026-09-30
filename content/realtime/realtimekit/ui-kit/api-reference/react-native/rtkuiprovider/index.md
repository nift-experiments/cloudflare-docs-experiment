<p>Context provider component that wraps the meeting UI. Provides SafeAreaView, state management, and back button handling. Must wrap all Rtk UI components.</p>
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
<td><code>children</code></td>
<td><code>ReactNode</code></td>
<td>✅</td>
<td>-</td>
<td>Child components to wrap</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import {&#10;	RtkUIProvider,&#10;	RtkMeeting,&#10;} from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function App() {&#10;	return (&#10;		&lt;RtkUIProvider&gt;&#10;			&lt;RtkMeeting meeting={meeting} /&gt;&#10;		&lt;/RtkUIProvider&gt;&#10;	);&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import {&#10;	RtkUIProvider,&#10;	RtkGrid,&#10;	RtkControlbar,&#10;	RtkHeader,&#10;} from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function App() {&#10;	return (&#10;		&lt;RtkUIProvider&gt;&#10;			&lt;RtkHeader meeting={meeting} /&gt;&#10;			&lt;RtkGrid meeting={meeting} /&gt;&#10;			&lt;RtkControlbar meeting={meeting} /&gt;&#10;		&lt;/RtkUIProvider&gt;&#10;	);&#10;}&#10;</code></pre>
