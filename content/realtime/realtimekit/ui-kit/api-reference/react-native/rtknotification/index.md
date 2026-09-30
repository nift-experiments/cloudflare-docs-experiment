<p>A single notification toast with slide-in/slide-out animation, avatar, message text, and dismiss button.</p>
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
<td><code>notification</code></td>
<td><code>Notification</code></td>
<td>✅</td>
<td>-</td>
<td>Notification object with id, message, image, duration, and button</td>
</tr>
<tr>
<td><code>onRtkNotificationDismiss</code></td>
<td><code>any</code></td>
<td>❌</td>
<td>-</td>
<td>Callback when notification is dismissed</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Custom icon pack</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>'lg' | 'md' | 'sm' | 'xl'</code></td>
<td>❌</td>
<td><code>'sm'</code></td>
<td>Size variant</td>
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
<pre><code class="language-tsx">import { RtkNotification } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkNotification notification={notification} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkNotification } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkNotification&#10;			notification={notification}&#10;			onRtkNotificationDismiss={(id) =&gt; handleDismiss(id)}&#10;			size=&quot;md&quot;&#10;		/&gt;&#10;	);&#10;}&#10;</code></pre>
