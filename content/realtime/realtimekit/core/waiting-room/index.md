<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisites">Prerequisites</h3>
@markup("md", "content/.markup/bodies/11826.md")
</aside>
<p>The waiting room feature allows hosts to control who can join a meeting. When enabled, participants must wait for approval before entering the meeting.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<h2 id="how-the-waiting-room-works">How the Waiting Room Works</h2>
<p>After you call <code>meeting.join()</code>, one of two events will occur:</p>
<ul>
<li><strong><code>roomJoined</code></strong> - You are allowed to join the meeting immediately</li>
<li><strong><code>waitlisted</code></strong> - You are placed in the waiting room and must wait for host approval</li>
</ul>
<p>Use <code>meeting.self.roomState</code> to track the user's state in the meeting.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11825.md")
</aside>
<h2 id="waiting-room-states">Waiting Room States</h2>
<h3 id="state-flow">State Flow</h3>
<pre><code>        join()&#10;          ↓&#10;    [waitlisted]  ←------ (host rejects)&#10;          ↓                     ↓&#10;   (host accepts)           [rejected]&#10;          ↓&#10;      [joined]&#10;</code></pre>
<h2 id="listening-to-state-changes">Listening to State Changes</h2>
<h3 id="joined-event">Joined Event</h3>
<p>Triggered when the local user successfully joins the meeting.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11827.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11828.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11829.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11830.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11831.md")
</div>
<h3 id="waitlisted-event">Waitlisted Event</h3>
<p>Triggered when the local user is placed in the waiting room.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11832.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11833.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11834.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11835.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11836.md")
</div>
<h3 id="rejected-event">Rejected Event</h3>
<p>Triggered when the host rejects the entry request.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11837.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11838.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11839.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11840.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11841.md")
</div>
<h3 id="monitor-state-with-roomstate">Monitor State with roomState</h3>
<p>You can also directly check the current room state.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11842.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11843.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11844.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11845.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11846.md")
</div>
<h2 id="host-actions">Host Actions</h2>
<p>Hosts can manage waiting room requests using participant management methods. See <a href="/realtime/realtimekit/core/remote-participants/">Remote Participants</a> for details on:</p>
<ul>
<li><strong><code>acceptWaitingRoomRequest(participantId)</code></strong> - Accept a participant from the waiting room</li>
<li><strong><code>rejectWaitingRoomRequest(participantId)</code></strong> - Reject a participant's entry request</li>
</ul>
<h3 id="example-host-accepting-participants">Example: Host Accepting Participants</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11847.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11848.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11849.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11850.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11851.md")
</div>
<h2 id="best-practices">Best Practices</h2>
<ul>
<li><strong>Provide Clear Feedback</strong> - Show users when they're in the waiting room and that they're waiting for approval</li>
<li><strong>Set Expectations</strong> - Let users know their request is being reviewed</li>
<li><strong>Handle Rejection Gracefully</strong> - Provide a friendly message if entry is rejected</li>
<li><strong>Monitor State Changes</strong> - Subscribe to room state changes to update your UI accordingly</li>
<li><strong>Check Permissions</strong> - Ensure your app has appropriate permissions configured in the preset to use waiting room features</li>
</ul>
