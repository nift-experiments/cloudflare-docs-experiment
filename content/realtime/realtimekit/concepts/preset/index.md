<p>A Preset is a <strong>re-usable configuration</strong> that defines a participant’s experience in a Meeting.
It determines:</p>
<ul>
<li>The meeting type they join (Video, Audio, Webinar, or Livestream <div class="nb-r-t-k-pill"></li>
</ul>
@markup("md", "content/.markup/bodies/12467.md")
</div>)
- Actions they can perform (permissions and controls)
- The UI’s look and feel, including colors and themes, so the experience matches your application's branding.
<p>Presets belong to an App, and they are applied to participants — not to meetings.</p>
<p>You can assign the same Preset to multiple participants when creating them through the Add Participant API. Participants in the same Meeting can have different Presets, allowing each user to have a distinct role and experience.</p>
<p>Example: Large Ed-Tech Classroom</p>
<ul>
<li><strong>Teacher</strong> uses the <code>webinar-host</code> preset — they can share media and access host controls.</li>
<li><strong>Students</strong> use the <code>webinar-participant</code> preset — they cannot share media but can use features like chat.</li>
<li><strong>Teaching</strong> assistant uses the <code>group-call-host</code> preset — they can share media but don’t have full host privileges.</li>
</ul>
<h3 id="create-a-preset">Create a Preset</h3>
<p>A set of default presets are created for you, when you create an app via the <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">Cloudflare dashboard</a>.</p>
<p>You can also create a preset using the <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">dashboard</a> or the <a href="/api/resources/realtime_kit/subresources/presets/methods/create/">Create Preset API</a>.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/presets \&#10;    &#45;H &#x27;Content-Type: application/json&#x27; \&#10;    &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;    &#45;d &#x27;{&#10;          &quot;config&quot;: {&#10;            ...&lt;preset-configuration-json&gt;&#10;        }&#x27;&#10;</code></pre>
<h3 id="preset-editor">Preset Editor</h3>
<p>We provide a UI-based editor to create and manage the presets in the <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">Cloudflare dashboard</a>.</p>
<p><img src="/assets/upstream/images/realtime/realtimekit/preset-editor.png" alt="Preset Editor" /></p>
<p>The permissions are divided into the following categories:</p>
<ul>
<li>
<p><strong>Host Controls:</strong> These permissions allow the user to control the meeting, manage participants, and perform administrative actions like kicking users, muting video/audio for others and more.</p>
</li>
<li>
<p><strong>Stage Management:</strong> Large meetings can be configured with a virtual stage. Participants on the stage can share their audio and video, while participants off the stage can view this media and still use features like chat, polls, and plugins.</p>
<pre><code>  Users can request to join the stage, host can add/remove users from the stage at any point.&#10;  Read more about stage management in [Meetings](/realtime/realtimekit/concepts/meeting#stage).&#10;</code></pre>
</li>
<li>
<p><strong>Chat:</strong> RealtimeKit allows users to send and receive messages in real time. You can also send private messages (visible only to a specific user). You can configure who has access to send &amp; messages and receive various kinds of messages.</p>
</li>
<li>
<p><strong>Polls:</strong> Allows user to configure who can create, view and interact with polls in the meeting.</p>
</li>
<li>
<p><strong>Plugins:</strong> Plugins are interactive real-time applications that run inside the meeting to make collaboration easier. RealtimeKit lets you build your own plugins and also offers built-in options like Whiteboard and Document Sharing.</p>
<pre><code>  You can control which plugins a participant is allowed to view, open, or close.&#10;</code></pre>
</li>
<li>
<p><strong>Waiting Room:</strong> A waiting room allows participants to join a meeting before they’re admitted, giving hosts control over who enters and when. It helps manage access, reduce interruptions, and ensure the meeting starts smoothly.</p>
<pre><code>  Hosts can admit or remove participants at any time, and you can configure who should bypass the waiting room automatically.&#10;  Read more about waiting rooms in [Meetings](/realtime/realtimekit/concepts/meeting#waiting-room).&#10;</code></pre>
</li>
<li>
<p><strong>Connected Meetings:</strong> Connected Meetings let you split a main meeting into linked spaces for smaller group discussions or parallel sessions. Permissions determine whether participants can move between connected meetings, return to the parent meeting, or create, update, and delete those meetings.</p>
<pre><code>  Read more about connected meetings in [Meetings](/realtime/realtimekit/concepts/meeting#connected-meetings).&#10;</code></pre>
</li>
<li>
<p><strong>Miscellaneous:</strong> Miscellaneous permissions let you fine-tune additional aspects of the participant experience that don’t fall under specific categories.</p>
<pre><code>  These options control capabilities like - editing names, viewing the participant list, syncing tab views, enabling transcriptions, and other supplementary features that enhance how users interact within the meeting.&#10;</code></pre>
</li>
</ul>
<h3 id="where-to-go-next">Where to Go Next</h3>
<p>After learning about Meetings and Sessions, you can explore the following next steps:</p>
<ul>
<li>Add <a href="/realtime/realtimekit/concepts/participant">Participants</a> to a Meeting – Manage who can join, their roles, and the access controls they inherit.</li>
<li>Get started with <a href="/realtime/realtimekit/quickstart/">RealtimeKit SDKs</a> – Integrate RealtimeKit into your web or mobile app with just a few lines of code.</li>
</ul>
