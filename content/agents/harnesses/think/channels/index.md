<aside class="nb-aside note">
<h3 class="nb-aside-title" id="experimental">Experimental</h3>
@markup("md", "content/.markup/bodies/2175.md")
</aside>
<p>A channel is a surface a Think agent talks over: the browser WebSocket, a messenger webhook (Telegram, Slack, and so on), voice, or your own custom transport. Channels generalize <a href="/agents/harnesses/think/messengers/">messengers</a> into one vocabulary so you can apply per-channel policy (a different system prompt, a narrowed tool set, a step cap) and deliver out-of-band notices, regardless of the surface a turn arrived on.</p>
<p>Every Think agent always has an implicit <code>web</code> channel (the WebSocket chat your browser clients use). You declare additional channels — and override the <code>web</code> policy — with <code>configureChannels()</code>. Messengers returned from <code>getMessengers()</code> are automatically absorbed as <code>messenger</code> channels, so existing messenger apps keep working unchanged.</p>
<h2 id="configure-channels">Configure channels</h2>
<p>Override <code>configureChannels()</code> to return a map of channel id to <code>ChannelDefinition</code>. The id is how you select the channel on a turn:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2176.md")
</div>
<p>A <code>ChannelDefinition</code> has these fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>kind</code></td>
<td><code>&quot;web&quot; | &quot;messenger&quot; | &quot;voice&quot; | &quot;custom&quot;</code></td>
<td>The surface category.</td>
</tr>
<tr>
<td><code>ingress</code></td>
<td><code>{ transport: &quot;websocket&quot; | &quot;voice&quot; }</code> or a webhook messenger spec</td>
<td>How turns arrive. <code>messengerChannel()</code> builds the webhook form for you.</td>
</tr>
<tr>
<td><code>instructions</code></td>
<td><code>string | (ctx: ChannelContext) =&gt; string | Promise&lt;string&gt;</code></td>
<td>Prepended to the system prompt for turns on this channel.</td>
</tr>
<tr>
<td><code>tools</code></td>
<td><code>(all: ToolSet) =&gt; ToolSet</code></td>
<td>Narrow the assembled tool set for this channel (filter only — it cannot add tools).</td>
</tr>
<tr>
<td><code>maxTurns</code></td>
<td><code>number</code></td>
<td>Per-channel cap on model steps for a turn.</td>
</tr>
<tr>
<td><code>capabilities</code></td>
<td><code>ChannelCapabilities</code></td>
<td>Surface capabilities (streaming, message editing). Defaulted for <code>web</code>.</td>
</tr>
<tr>
<td><code>conversation</code></td>
<td>messenger conversation mode or resolver</td>
<td>Messenger thread routing (see <a href="/agents/harnesses/think/messengers/">Messengers</a>).</td>
</tr>
<tr>
<td><code>delivery</code></td>
<td>channel delivery policy</td>
<td>Messenger delivery policy.</td>
</tr>
</tbody>
</table>
<p>Use the <code>defineChannels()</code> helper for type inference, and <code>messengerChannel()</code> to wrap a Chat SDK adapter definition as a <code>kind: &quot;messenger&quot;</code> channel.</p>
<h3 id="channel-kinds">Channel kinds</h3>
<table>
<thead>
<tr>
<th>Kind</th>
<th>Ingress</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>web</code></td>
<td><code>{ transport: &quot;websocket&quot; }</code></td>
<td>Always present. Declare it in <code>configureChannels()</code> only to set policy; you cannot remove it.</td>
</tr>
<tr>
<td><code>messenger</code></td>
<td>webhook (<code>messengerChannel(...)</code>)</td>
<td>Fed into the messenger runtime. Equivalent to a <code>getMessengers()</code> entry.</td>
</tr>
<tr>
<td><code>voice</code></td>
<td><code>{ transport: &quot;voice&quot; }</code></td>
<td>Applies policy and turn context; out-of-band delivery is not yet wired.</td>
</tr>
<tr>
<td><code>custom</code></td>
<td>app-defined</td>
<td>For your own transport. Same delivery limitations as <code>voice</code> today.</td>
</tr>
</tbody>
</table>
<h2 id="per-channel-policy">Per-channel policy</h2>
<p>Channel policy is applied as an <strong>overridable default</strong> before <a href="/agents/harnesses/think/lifecycle-hooks/"><code>beforeTurn</code></a> runs, so a <code>beforeTurn</code> override still wins:</p>
<ul>
<li><code>instructions</code> is prepended to the base system prompt for the turn.</li>
<li><code>tools</code> filters the assembled tool set (it can only remove tools — the <code>getTools()</code> seam adds them).</li>
<li><code>maxTurns</code> caps model steps: <code>beforeTurn</code>'s <code>maxSteps</code> wins, then the channel <code>maxTurns</code>, then the instance <code>maxSteps</code> default.</li>
</ul>
<h2 id="select-a-channel-on-a-turn">Select a channel on a turn</h2>
<p>Pass <code>channel</code> to <a href="/agents/harnesses/think/#runturn"><code>runTurn()</code></a> (or <code>chat()</code>) to run a turn on a specific channel. The channel id is stamped onto the user message, so a continued or recovered turn re-resolves the same channel and re-applies its policy:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2177.md")
</div>
<p>Inside a turn, the active channel is available as <code>this.activeChannel</code> (a <code>ChannelContext</code> with <code>channelId</code>, <code>kind</code>, and messenger details when relevant). A turn with no <code>channel</code> runs without a channel context and applies no channel policy.</p>
<h2 id="deliver-out-of-band">Deliver out of band</h2>
<p><code>deliverNotice()</code> sends a message to a channel <strong>without</strong> starting a model turn. Use it for status updates (&quot;your import finished&quot;) or to surface an action's <a href="/agents/harnesses/think/actions/#reply-attachments">reply attachment</a> — it does not run inference, does not enter the turn queue, and is therefore safe to call from inside a tool's <code>execute</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2178.md")
</div>
<pre><code class="language-ts">type DeliverNoticeOptions = {&#10;	channel?: string; // defaults to the active turn&#x27;s channel, else &quot;web&quot;&#10;	informModel?: boolean; // also write to the model-visible transcript (default false)&#10;	kind?: &quot;final&quot; | &quot;interim&quot; | &quot;notice&quot; | &quot;command&quot;; // wire tag (default &quot;notice&quot;)&#10;	thread?: string; // required for out-of-turn delivery to a multi-thread messenger&#10;};&#10;</code></pre>
<p>Behavior depends on the target channel:</p>
<ul>
<li><strong><code>web</code></strong> — the notice is always appended to the transcript (that is its only render path). <code>informModel</code> then only controls the phrasing.</li>
<li><strong><code>messenger</code></strong> — the notice is posted to the provider. Out of turn, pass <code>thread</code> to target a conversation. With <code>informModel: true</code>, it is also written to the transcript.</li>
<li><strong><code>voice</code> / <code>custom</code></strong> — out-of-turn delivery throws, because these surfaces have no delivery target yet.</li>
</ul>
<p>Override <code>renderAttachment(attachment)</code> to turn an action reply attachment into a notice; Think calls it at the end of a turn and delivers the rendered text as a trailing <code>interim</code> notice. Return <code>undefined</code> to skip an attachment type.</p>
<h2 id="relationship-to-messengers">Relationship to messengers</h2>
<p><code>configureChannels()</code> wraps <code>getMessengers()</code> — it does not replace it. Each <code>getMessengers()</code> entry becomes a <code>kind: &quot;messenger&quot;</code> channel, and everything in the <a href="/agents/harnesses/think/messengers/">Messengers</a> guide (Telegram setup, webhook routing, conversation targets, delivery and recovery) continues to apply. A channel id in <code>configureChannels()</code> that collides with a <code>getMessengers()</code> id is an error. Keep using <code>getMessengers()</code> for messenger-only apps; reach for <code>configureChannels()</code> when you also want <code>web</code>/<code>voice</code>/<code>custom</code> policy or out-of-band notices.</p>
<h2 id="observability">Observability</h2>
<p>Channel activity is reported on the <code>channel</code> observability channel:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2179.md")
</div>
<h2 id="reference">Reference</h2>
<table>
<thead>
<tr>
<th>Member</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>configureChannels()</code></td>
<td>Return the channel map. Defaults to <code>{}</code> (the implicit <code>web</code> channel only).</td>
</tr>
<tr>
<td><code>deliverNotice(text, options?)</code></td>
<td>Send an out-of-band message to a channel with no model turn.</td>
</tr>
<tr>
<td><code>activeChannel</code></td>
<td>The <code>ChannelContext</code> for the in-flight turn, or <code>undefined</code>.</td>
</tr>
<tr>
<td><code>renderAttachment(attachment)</code></td>
<td>Map a reply attachment to channel notice text (or <code>undefined</code> to skip).</td>
</tr>
<tr>
<td><code>defineChannels(channels)</code></td>
<td>Identity helper for channel-map type inference.</td>
</tr>
<tr>
<td><code>messengerChannel(definition)</code></td>
<td>Wrap a Chat SDK adapter as a <code>kind: &quot;messenger&quot;</code> channel.</td>
</tr>
</tbody>
</table>
<h2 id="related">Related</h2>
<ul>
<li><a href="/agents/harnesses/think/messengers/">Messengers</a> — Chat SDK webhook setup and delivery in depth.</li>
<li><a href="/agents/harnesses/think/actions/">Actions</a> — record reply attachments for <code>renderAttachment()</code>.</li>
<li><a href="/agents/communication-channels/voice/">Voice</a> — real-time speech surfaces.</li>
</ul>
