<p>Before a user can join a meeting through the RealtimeKit SDK, your backend must add that user as a participant to that meeting using the <a href="/api/resources/realtime_kit/subresources/meetings/methods/add_participant/">Add Participant API</a>.
In RealtimeKit, a <strong>participant</strong> represents a user who is allowed to join a specific meeting.</p>
<p>You can think of this as enrolling a student into a classroom. The meeting is the classroom, and adding a participant is how you register a user so that they are allowed to attend.</p>
<p>When you add a participant, you also choose which <a href="/realtime/realtimekit/concepts/preset/">preset</a> to apply. The preset defines the role, permissions, and
meeting experience of that participant.</p>
<h3 id="participant-tokens">Participant tokens</h3>
<p>When you add a participant to a meeting using the <a href="/api/resources/realtime_kit/subresources/meetings/methods/add_participant/">Add Participant</a> API endpoint, it returns:</p>
<ul>
<li>A participant <code>id</code> that identifies this participant within the meeting.</li>
<li>An authentication <code>token</code> for that participant.</li>
</ul>
<p>Your backend should make it available to your frontend application. When the user chooses to join the meeting, the frontend passes the token to the RealtimeKit SDK.</p>
<p>RealtimeKit uses the token to authenticate the participant and determine which meeting and which participant is joining. Without a valid authentication token,
the SDK cannot join the meeting on behalf of that participant. As long as a participant has a valid authentication token, that participant can join multiple live sessions of the same meeting over time.</p>
<h3 id="token-validity-and-refresh">Token validity and refresh</h3>
<p>Participant authentication tokens are JSON Web Tokens (JWTs). The <code>meetingId</code> and <code>participantId</code> fields scope each token to one participant in one meeting.</p>
<p>A token becomes valid when issued and expires 100 days later. You cannot configure custom start or expiration dates. If you need scheduled access, enforce the schedule in your own system because RealtimeKit SDKs do not manage scheduling or duration logic.</p>
<p>Your backend can call the <a href="/api/resources/realtime_kit/subresources/meetings/methods/refresh_participant_token/">Refresh Participant Token</a> endpoint before or after a token expires. The new token uses the existing participant record, including its participant <code>id</code> and preset. Refreshing does not invalidate previously issued tokens. Each token remains valid until its own expiration time.</p>
<p>To revoke all tokens for a participant in a meeting, call the <a href="/api/resources/realtime_kit/subresources/meetings/methods/delete_meeting_participant/">Delete Participant</a> endpoint. First, use the <a href="/api/resources/realtime_kit/subresources/active-session/methods/kick_participants/">Kick Participants</a> endpoint to safely remove the participant from any active session.</p>
<p>A participant cannot join a meeting with an expired or revoked token. The RealtimeKit UI and Core SDK report the token as invalid. RealtimeKit rejects the participant before they enter the <a href="/realtime/realtimekit/core/stage-management/">meeting stage</a>, so they are not billed.</p>
<h3 id="custom-participant-identifier">Custom participant identifier</h3>
<p>When adding the participant, you can optionally provide a custom participant identifier, referred to as <code>custom_participant_id</code>. This value is purely for your use.
RealtimeKit stores it and returns it in APIs, but does not use it to control access. It allows you to map your application's user to RealtimeKit participant and
to correlate RealtimeKit session data, events or analytics with user information in your system.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12468.md")
</aside>
<h3 id="where-to-go-next">Where to Go Next</h3>
<p>After understanding participants, you can explore the following topics:</p>
<ul>
<li>Learn how <a href="/realtime/realtimekit/concepts/preset">Presets</a> define roles and permissions for participants</li>
<li><a href="/realtime/realtimekit/ui-kit/">Get started with RealtimeKit SDKs</a></li>
</ul>
