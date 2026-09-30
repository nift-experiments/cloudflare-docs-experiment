<p>In a RealtimeKit webinar, presenters publish audio and video from the <a href="/realtime/realtimekit/concepts/meeting/#stage">stage</a>. Viewers watch and can request to join the stage.</p>
<p>This guide sets up a webinar using the default webinar <a href="/realtime/realtimekit/concepts/preset/">presets</a> and renders it with <a href="/realtime/realtimekit/ui-kit/">RealtimeKit UI Kit</a>. To build a custom interface instead, use <a href="/realtime/realtimekit/core/">RealtimeKit Core SDK</a> with <a href="/realtime/realtimekit/core/stage-management/">stage management</a>.</p>
<h2 id="webinar-roles">Webinar roles</h2>
<p>Every RealtimeKit app includes two default presets for webinars. Assign one of these presets to each participant, modify them, or create your own preset to fit your application.</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Default preset</th>
<th>Stage behavior</th>
<th>Can accept stage requests</th>
</tr>
</thead>
<tbody>
<tr>
<td>Presenter</td>
<td><code>webinar_presenter</code></td>
<td>Can join the stage and publish audio and video</td>
<td>Yes</td>
</tr>
<tr>
<td>Viewer</td>
<td><code>webinar_viewer</code></td>
<td>Can request to join the stage</td>
<td>No</td>
</tr>
</tbody>
</table>
<h2 id="before-you-begin">Before you begin</h2>
<p>Before you set up a webinar, make sure that you have:</p>
<ul>
<li>A <a href="https://dash.cloudflare.com">Cloudflare account</a> with a RealtimeKit app.</li>
<li>An API token with Realtime Admin permissions. Keep it server-side. Do not expose it in frontend code.</li>
<li>A backend that can call the RealtimeKit REST API to create meetings and add participants.</li>
<li>A frontend application ready to integrate <a href="/realtime/realtimekit/ui-kit/">RealtimeKit UI Kit</a>.</li>
</ul>
<p>If you have not completed these requirements, refer to <a href="/realtime/realtimekit/quickstart/">Quickstart</a>.</p>
<h2 id="set-up-a-webinar">Set up a webinar</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11589.md")
</div>
<details class="nb-details"><summary>Configure presets with the API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11590.md")
</div></details>
<h2 id="manage-stage-requests">Manage stage requests</h2>
<p>A viewer whose preset has <strong>Behaviour</strong> set to <strong>Can request to join</strong> can request access to the stage from the UI Kit interface. A presenter whose preset has <strong>Accept Requests</strong> turned on receives the request and can accept or reject it.</p>
<p>Once accepted, the viewer joins the stage and can publish audio and video like a presenter. RealtimeKit UI Kit handles this by default. To build a custom interface, implement the same behavior with the stage management APIs in <a href="/realtime/realtimekit/core/stage-management/">Stage Management</a>.</p>
<h2 id="verify-the-webinar">Verify the webinar</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11591.md")
</div>
<h2 id="pricing">Pricing</h2>
<p>Both presenters and viewers are billed as Audio/Video Participants. For detailed pricing information, refer to <a href="/realtime/realtimekit/pricing/">Pricing</a>.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Customize the webinar interface with a <a href="/realtime/realtimekit/ui-kit/custom-controlbar/">custom control bar</a> or <a href="/realtime/realtimekit/ui-kit/addons/">UI Kit addons</a>.</li>
<li>Review <a href="/realtime/realtimekit/best-practices/video-and-simulcast/#webinar-audience-is-view-only">video and simulcast recommendations</a> for presenter and viewer media quality.</li>
<li><a href="/realtime/realtimekit/recording-guide/">Record the webinar</a> and store the recording in your own storage.</li>
<li>Use <a href="/realtime/realtimekit/webhooks/">webhooks</a> to track webinar lifecycle events in your backend.</li>
</ul>
