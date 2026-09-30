<p>Meeting is a <strong>re-usable virtual room</strong> that you can join and interact in, in real-time.</p>
<p>You can assign a title and feature configuration to it, then add participants who are authorised to join. The Meeting itself doesn't &quot;start&quot; or &quot;end&quot;; it just exists.</p>
<p>Because Meetings do not have a specific date or time, you can create them well in advance or create them just-in-time, right when users need to join.</p>
<p>The following diagram shows the blueprint of a Meeting:</p>
<pre><code class="language-mermaid">&#45;--&#10;title: Meeting&#10;&#45;--&#10;flowchart TB&#10;  accTitle: Meeting blueprint&#10;  accDescr: Diagram showing blueprint of a Meeting&#10;&#10;  subgraph details [ ]&#10;      direction LR&#10;      subgraph feat [&quot;&lt;b&gt;Features&lt;/b&gt;&quot;]&#10;          feat-content[&quot;Chat&lt;br&gt;...&lt;br&gt;Recording&lt;br&gt;...&lt;br&gt;Transcriptions&quot;]&#10;      end&#10;      subgraph config [&quot;&lt;b&gt;Configuration&lt;/b&gt;&quot;]&#10;          config-content[&quot;record_on_start&lt;br&gt;...&lt;br&gt;persist_chat&lt;br&gt;...&lt;br&gt;ai_config&quot;]&#10;      end&#10;  end&#10;&#10;  subgraph participants [&quot;&lt;b&gt;Participants&lt;/b&gt;&quot;]&#10;      direction LR&#10;      subgraph participants-row2 [ ]&#10;          direction TB&#10;          P3[&quot;&lt;br&gt;Participant 3&#10;          &lt;br&gt;&#10;          &quot;]&#10;          P4[&quot;&lt;br&gt;Participant 4&#10;          &lt;br&gt;&#10;          &quot;]&#10;      end&#10;      subgraph participants-row1 [ ]&#10;          direction TB&#10;          P1[&quot;&lt;br&gt;Participant 1&#10;          &lt;br&gt;&#10;          &quot;]&#10;          P2[&quot;&lt;br&gt;Participant 2&#10;          &lt;br&gt;&#10;          &quot;]&#10;      end&#10;  end&#10;&#10;  style participants-row1 fill:none,stroke:none&#10;  style participants-row2 fill:none,stroke:none&#10;  style details fill:none,stroke:none&#10;</code></pre>
<h3 id="session">Session</h3>
<p>A <strong>Session</strong> is a live instance of a Meeting. It starts automatically when the first participant joins the meeting and ends shortly after the last participant leaves.
A Session inherits all settings (like features and title) from its parent Meeting.</p>
<p>Because the Meeting is persistent, it can have many different Sessions over time.</p>
<p>Example - <strong>Think of a Meeting as a recurring weekly standup event.</strong></p>
<p>The Meeting is the permanent “standup event” that exists in your system.</p>
<p>Each week, when participants join for that week’s standup, a <strong>new Session</strong> is created — this Session represents that week’s actual live standup.</p>
<blockquote>
<p><strong>Note</strong>: This distinction is important for billing. You are charged on a per-participant basis only for the duration of an active Session, not for an idle Meeting.</p>
</blockquote>
<p>You can get the details of your sessions from the <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">RealtimeKit Dashboard</a> or using the <a href="/api/resources/realtime_kit/subresources/sessions/">Sessions API</a> endpoints.</p>
<p><img src="/assets/upstream/images/realtime/realtimekit/dashboard-sessions.png" alt="Sessions in RealtimeKit Dashboard" /></p>
<h3 id="session-terminologies">Session Terminologies</h3>
<h4 id="waiting-room">Waiting Room</h4>
<p>A <strong>waiting room</strong> lets participants join a meeting without immediately entering the live session. This gives hosts full control over <strong>who gets in</strong>, <strong>when they enter</strong>, and <strong>how the meeting flow is managed</strong>.</p>
<p>Hosts can also configure specific behaviours for how users move from the waiting room into the meeting.</p>
<ul>
<li>
<p><strong>Join when accepted by someone</strong>
Participants stay in the waiting room until a host or another authorized user explicitly admits them. Ideal for highly controlled or private meetings.</p>
</li>
<li>
<p><strong>Join when a privileged user joins</strong>
Participants remain in the waiting room initially, but are automatically admitted once a host or other privileged user enters the meeting. Useful for scheduled events where attendees should only join after the moderator is present.</p>
</li>
<li>
<p><strong>Accept users into waiting room</strong>
Hosts can see the list of waiting users, admit them individually or in bulk, or remove them. This mode provides maximum visibility and control over incoming participants.</p>
</li>
</ul>
<p>These options allow you to tailor how access is managed—whether you need strict admission control, a smoother flow once a host arrives, or a combination of both.</p>
<h4 id="stage">Stage</h4>
<p>Meetings can be configured with a <strong>virtual stage</strong>, which helps you manage who actively participates with audio and video during high-attendance sessions.</p>
<p>When a participant is <strong>on the stage</strong>, they are visible in the grid and they can publish their audio and video to everyone in the meeting. Participants who are <strong>off the stage</strong> cannot publish media, but they can still fully engage through features like <strong>chat</strong>, <strong>polls</strong>, <strong>Q&amp;A</strong>, and <strong>plugins</strong>—making the experience interactive without overwhelming the live video layout.</p>
<p>Participants can also <strong>request to join the stage</strong>, allowing them to signal when they want to speak or present. Hosts retain full control at all times: they can <strong>approve or deny requests</strong>, or directly <strong>invite or remove participants from the stage</strong> as needed.</p>
<p>This setup is ideal for webinars, town halls, AMAs, and other structured events where only a subset of users should broadcast while everyone else participates from the audience.</p>
<h4 id="connected-meetings">Connected Meetings</h4>
<p>Connected Meetings let you create linked meeting spaces, that participants can switch between during a session. This is useful for workshops, classrooms, parallel discussions, or any scenario where the main meeting splits into smaller groups before coming back together.</p>
<p>You can control how participants move between these connected spaces using the following permissions:</p>
<ul>
<li><strong>Full Access:</strong> Allows participants to create, update, and delete connected meetings.</li>
<li><strong>Switch Connected Meeting:</strong> Lets participants move freely between the available connected (child) meetings.</li>
<li><strong>Switch to Parent Meeting:</strong> Allows participants to return to the main (parent) meeting at any time.</li>
</ul>
<h3 id="create-a-meeting">Create a meeting</h3>
<p>You create and manage RealtimeKit meetings, typically from your backend, using the <a href="/api/resources/realtime_kit/subresources/meetings/">Meetings API</a>. To create
a meeting, send a <code>POST</code> request to the <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">Create Meeting</a> endpoint.</p>
<details class="nb-details"><summary>API Prerequisites</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/12469.md")
</div></details>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/realtime/kit/{APP_ID}/meetings \&#10;  &#45;-request POST \&#10;  &#45;-header &quot;Authorization: Bearer &lt;CLOUDFLARE_API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;title&quot;: &quot;My First Cloudflare RealtimeKit meeting&quot;&#10;    }&#x27;&#10;</code></pre>
<p>A successful response includes a unique <code>id</code> for the created meeting. Save this ID, as it is required for all future operations on this specific meeting,
such as adding participants or disabling it.</p>
<p>For a complete list of all available configuration parameters, refer to the <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">Create Meeting API</a>.</p>
<h3 id="where-to-go-next">Where to Go Next</h3>
<p>After learning about Meetings and Sessions, you can explore the following next steps:</p>
<ul>
<li>Configure <a href="/realtime/realtimekit/concepts/preset/">Presets</a> for your App – Set up default permissions, media settings, and behavior for all Sessions created from a Meeting.</li>
<li>Add <a href="/realtime/realtimekit/concepts/participant/">Participants</a> to a Meeting – Manage who can join, their roles, and the access controls they inherit.</li>
<li>Get started with <a href="/realtime/realtimekit/quickstart/">RealtimeKit SDKs</a> – Integrate RealtimeKit into your web or mobile app with just a few lines of code.</li>
</ul>
