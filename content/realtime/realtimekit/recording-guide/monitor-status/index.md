<h2 id="recording-states">Recording states</h2>
<p>The recording of a meeting can have the following states:</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>INVOKED</td>
<td>RealtimeKit backend servers have received the recording request, and the master is looking for a ready worker to assign the recording job.</td>
</tr>
<tr>
<td>RECORDING</td>
<td>The meeting is currently being recorded by a worker; note that this will also hold true if the meeting is being live streamed.</td>
</tr>
<tr>
<td>UPLOADING</td>
<td>The recording has been stopped and the file is being uploaded to the cloud storage. If you have not specified storage details, then the files will be uploaded only to RealtimeKit's server. Any RTMP and livestreaming link will also stop at this stage.</td>
</tr>
<tr>
<td>UPLOADED</td>
<td>The recording file upload is complete and the status webhook is also triggered.</td>
</tr>
<tr>
<td>ERRORED</td>
<td>There was an irrecoverable error while recording the meeting and the file will not be available.</td>
</tr>
</tbody>
</table>
<h2 id="fetching-the-state">Fetching the state</h2>
<p>There are two ways you can track what state a recording is in or view more
details about a recording:</p>
<h3 id="using-the-recording-statusupdate-webhook">Using the <code>recording.statusUpdate</code> webhook</h3>
<p>RealtimeKit sends a <code>recording.statusUpdate</code> webhook when the recording transitions between states during its lifecycle. Add <code>recording.statusUpdate</code> to your webhook's <code>events</code> array to receive these notifications.</p>
<pre><code class="language-bash">curl --request POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/webhooks&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;name&quot;: &quot;Recording status webhook&quot;,&#10;    &quot;url&quot;: &quot;https://example.com/webhook&quot;,&#10;    &quot;events&quot;: [&quot;recording.statusUpdate&quot;],&#10;    &quot;enabled&quot;: true&#10;  }&#x27;&#10;</code></pre>
<p>The webhook payload includes the current recording status, recording metadata, and associated meeting details. When the status is <code>UPLOADED</code>, the payload can include <code>downloadUrl</code>, <code>audioDownloadUrl</code>, and <code>downloadUrlExpiry</code> fields for accessing the uploaded files.</p>
<p>For setup, signature verification, retry behavior, and a full payload example, refer to <a href="/realtime/realtimekit/webhooks/#recordingstatusupdate">RealtimeKit webhooks</a>.</p>
<h3 id="by-polling-http-apis">By polling HTTP APIs</h3>
<p>Alternatively, you can also use the following APIs:</p>
<ul>
<li><a href="/api/resources/realtime_kit/subresources/recordings/methods/get_recordings/">List recordings</a>:
This endpoint gets all past and ongoing recordings linked to a meeting.</li>
<li><a href="/api/resources/realtime_kit/subresources/recordings/methods/get_active_recordings/">Fetch active recording</a>: This
endpoint gets all ongoing recordings of a meeting.</li>
<li><a href="/api/resources/realtime_kit/subresources/recordings/methods/get_one_recording/">Fetch details of a recording</a>: This
endpoint gets a specific recording using a recording ID.</li>
</ul>
