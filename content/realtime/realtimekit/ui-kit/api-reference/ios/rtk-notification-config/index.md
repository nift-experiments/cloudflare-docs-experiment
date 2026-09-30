<p>Configuration class for controlling notification behavior in meetings.
Manages sound and toast notifications for participant join/leave events, chat messages, and polls.</p>
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
<td><code>participantJoined</code></td>
<td><code>RtkNotification</code></td>
<td>❌</td>
<td><code>RtkNotification()</code></td>
<td>Notification settings for participant join events</td>
</tr>
<tr>
<td><code>participantLeft</code></td>
<td><code>RtkNotification</code></td>
<td>❌</td>
<td><code>RtkNotification()</code></td>
<td>Notification settings for participant leave events</td>
</tr>
<tr>
<td><code>newChatArrived</code></td>
<td><code>RtkNotification</code></td>
<td>❌</td>
<td><code>RtkNotification()</code></td>
<td>Notification settings for new chat messages</td>
</tr>
<tr>
<td><code>newPollArrived</code></td>
<td><code>RtkNotification</code></td>
<td>❌</td>
<td><code>RtkNotification()</code></td>
<td>Notification settings for new poll events</td>
</tr>
</tbody>
</table>
<h2 id="rtknotification-properties">RtkNotification properties</h2>
<p>Each <code>RtkNotification</code> instance contains the following properties:</p>
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
<td><code>playSound</code></td>
<td><code>Bool</code></td>
<td>❌</td>
<td><code>true</code></td>
<td>Whether to play a notification sound</td>
</tr>
<tr>
<td><code>showToast</code></td>
<td><code>Bool</code></td>
<td>❌</td>
<td><code>true</code></td>
<td>Whether to show a toast notification</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let rtkUI = RealtimeKitUI(meetingInfo: meetingInfo)&#10;// Access the default notification config&#10;let notificationConfig = rtkUI.notification&#10;</code></pre>
<h3 id="customize-notifications">Customize notifications</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let rtkUI = RealtimeKitUI(meetingInfo: meetingInfo)&#10;&#10;// Disable sound for participant join events&#10;rtkUI.notification.participantJoined.playSound = false&#10;&#10;// Disable toast for chat messages&#10;rtkUI.notification.newChatArrived.showToast = false&#10;</code></pre>
