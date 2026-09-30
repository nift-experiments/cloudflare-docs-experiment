<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisites">Prerequisites</h3>
@markup("md", "content/.markup/bodies/12329.md")
</aside>
<p>To end the current <a href="/realtime/realtimekit/concepts/meeting/#session/">session</a> for all participants, remove all participants using <code>kickAll()</code>. This stops any ongoing recording for that session and sets the session status to <code>ENDED</code>.</p>
<p>Ending a session is different from leaving a meeting. Leaving disconnects only the current participant. The session remains active if other participants are still present.</p>
<h2 id="steps">Steps</h2>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<ol>
<li>Check that the local participant has permission to remove participants.</li>
</ol>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12330.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12331.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12332.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12333.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12334.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12335.md")
</div>
<ol start="2">
<li>End the session by removing all participants.</li>
</ol>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12336.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12337.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12338.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12339.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12340.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12341.md")
</div>
<ol start="3">
<li>Listen for the session end event.</li>
</ol>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12342.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12343.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12344.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12345.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12346.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12347.md")
</div>
<p>You can also end a session from your backend by removing all participants using the <a href="/api/resources/realtime_kit/subresources/active-session/methods/kick_all_participants/">Kick all participants</a> API.</p>
<h2 id="end-a-session-from-your-backend">End a session from your backend</h2>
<h3 id="remove-all-participants-with-the-api">Remove all participants with the API</h3>
<p>Use the <a href="/api/resources/realtime_kit/subresources/active-session/methods/kick_all_participants/">Kick all participants</a> API method to remove all participants from an active session for a meeting.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick-all \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="listen-for-session-end-events-with-webhooks">Listen for session end events with webhooks</h3>
<p>Register a webhook that subscribes to <code>meeting.ended</code>. RealtimeKit sends this event when the session ends.
You can use it to trigger backend workflows, such as sending a notification, generating a report, or updating session records in your database.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/realtime/kit/{app_id}/webhooks \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;Session ended webhook&quot;,&#10;  &quot;url&quot;: &quot;&lt;YOUR_WEBHOOK_URL&gt;&quot;,&#10;  &quot;events&quot;: [&#10;    &quot;meeting.ended&quot;&#10;  ]&#10;}&#x27;</code></pre>
<h2 id="disable-a-meeting">Disable a meeting</h2>
<p>Ending a session does not disable the meeting. Participants can join the meeting again and start a new session.
To prevent participants from joining again and starting a new session, set the meeting status to <code>INACTIVE</code> using the <a href="/api/resources/realtime_kit/subresources/meetings/methods/update_meeting_by_id/">Update a meeting</a> API.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;status&quot;: &quot;INACTIVE&quot;&#10;}&#x27;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Review how presets control permissions in <a href="/realtime/realtimekit/concepts/preset/">Preset</a>.</li>
<li>Review the possible values of the local participant room state in <a href="/realtime/realtimekit/core/local-participant/#state-properties/">Local Participant</a>.</li>
</ul>
