<p>The broadcast APIs allow a user to send custom messages to all other users in a meeting.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<h3 id="broadcasting-a-message">Broadcasting a Message</h3>
<p>The Participants module on the meeting object allows you to broadcast messages to all other users in a meeting (or to other meetings in case of connected meetings) over the signaling channel.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12492.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12493.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12494.md")
</div>
<h3 id="subscribe-to-messages">Subscribe to Messages</h3>
<p>Use the <code>broadcastedMessage</code> event to listen for messages sent via <code>broadcastMessage</code> and handle them in your application.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12495.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12496.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12497.md")
</div>
<h3 id="rate-limiting-constraints">Rate Limiting &amp; Constraints</h3>
<ul>
<li>The method is rate‑limited (server‑side + client‑side) to prevent abuse.</li>
<li>Default client‑side config in the deprecated module: maxInvocations = 5 per period = 1s.</li>
<li>The Participants module exposes a <code>rateLimitConfig</code> and <code>updateRateLimits(maxInvocations, period)</code> for tuning on the client, but server‑side limits may still apply.</li>
<li>The event type cannot be <code>spotlight</code>. This is reserved for internal use by the SDK.</li>
</ul>
<h3 id="examples">Examples</h3>
<h4 id="broadcast-to-everyone-in-the-meeting">Broadcast to everyone in the meeting</h4>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12498.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12499.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12500.md")
</div>
<h4 id="broadcast-to-a-specific-set-of-participants">Broadcast to a specific set of participants.</h4>
<p>Only the participants with those participantIds receive the message.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12501.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12502.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12503.md")
</div>
<h4 id="broadcast-to-a-preset">Broadcast to a preset</h4>
<p>All participants whose preset name is <code>speaker</code> receive the message.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12504.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12505.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12506.md")
</div>
<h4 id="broadcast-across-multiple-meetings">Broadcast across multiple meetings</h4>
<p>All participants in the specified meetings receive the message.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12507.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12508.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12509.md")
</div>
