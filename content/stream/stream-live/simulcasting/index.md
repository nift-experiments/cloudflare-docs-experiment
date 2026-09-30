<p>Simulcasting lets you forward your live stream to third-party platforms such as Twitch, YouTube, Facebook, Twitter, and more. You can simulcast to up to 50 concurrent destinations from each live input. To begin simulcasting, select an input and add one or more Outputs.</p>
<h2 id="add-an-output-using-the-api">Add an Output using the API</h2>
<p>Add an Output to start retransmitting live video. You can add or remove Outputs at any time during a broadcast to start and stop retransmitting.</p>
<pre><code class="language-bash">curl -X POST \&#10;&#45;-data &#x27;{&quot;url&quot;: &quot;rtmp://a.rtmp.youtube.com/live2&quot;,&quot;streamKey&quot;: &quot;&lt;redacted&gt;&quot;}&#x27; \&#10;&#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream/live_inputs/&lt;INPUT_UID&gt;/outputs&#10;</code></pre>
<pre><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;uid&quot;: &quot;6f8339ed45fe87daa8e7f0fe4e4ef776&quot;,&#10;    &quot;url&quot;: &quot;rtmp://a.rtmp.youtube.com/live2&quot;,&#10;    &quot;streamKey&quot;: &quot;&lt;redacted&gt;&quot;&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="control-when-you-start-and-stop-simulcasting">Control when you start and stop simulcasting</h2>
<p>You can enable and disable individual live outputs with either:</p>
<ul>
<li>The <strong>Live inputs</strong> page of the Cloudflare dashboard.</li>
</ul>
<div class="nb-dash-button"></div>
- [The API](/api/resources/stream/subresources/live_inputs/subresources/outputs/methods/update/)
<p>This allows you to:</p>
<ul>
<li>Start a live stream, but wait to start simulcasting to YouTube and Twitch until right before the content begins.</li>
<li>Stop simulcasting before the live stream ends, to encourage viewers to transition from a third-party service like YouTube or Twitch to a direct live stream.</li>
<li>Give your own users manual control over when they go live to specific simulcasting destinations.</li>
</ul>
<p>When a live output is disabled, video is not simulcast to the live output, even when actively streaming to the corresponding live input.</p>
<p>By default, all live outputs are enabled.</p>
<h3 id="enable-outputs-from-the-dashboard">Enable outputs from the dashboard:</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Live inputs</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select an input from the list.</li>
<li>Under <strong>Outputs</strong> &gt; <strong>Enabled</strong>, set the toggle to enabled or disabled.</li>
</ol>
<h2 id="manage-outputs">Manage outputs</h2>
<table>
<thead>
<tr>
<th>Command</th>
<th>Method</th>
<th>Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/stream/subresources/live_inputs/methods/list/">List outputs</a></td>
<td><code>GET</code></td>
<td><code>accounts/:account_identifier/stream/live_inputs</code></td>
</tr>
<tr>
<td><a href="/api/resources/stream/subresources/live_inputs/methods/delete/">Delete outputs</a></td>
<td><code>DELETE</code></td>
<td><code>accounts/:account_identifier/stream/live_inputs/:live_input_identifier</code></td>
</tr>
<tr>
<td><a href="/api/resources/stream/subresources/live_inputs/subresources/outputs/methods/list/">List All Outputs Associated With A Specified Live Input</a></td>
<td><code>GET</code></td>
<td><code>/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs</code></td>
</tr>
<tr>
<td><a href="/api/resources/stream/subresources/live_inputs/subresources/outputs/methods/delete/">Delete An Output</a></td>
<td><code>DELETE</code></td>
<td><code>/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}</code></td>
</tr>
</tbody>
</table>
<p>If the associated live input is already retransmitting to this output when you make the <code>DELETE</code> request, that output will be disconnected within 30 seconds.</p>
