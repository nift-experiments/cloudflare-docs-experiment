<!-- Auto Generated Below -->
<p><a name="module_RTKParticipant"></a></p>
<p>This module represents a single participant in the meeting.
The participant object can be accessed from one of the participant lists
present in the <code>meeting.participants</code> object. For example,</p>
<pre><code class="language-ts">const participant1 = meeting.participants.active.get(participantId);&#10;const participant2 = meeting.participants.joined.get(participantId);&#10;const participant3 = meeting.participants.active.toArray()[0];&#10;const participantsNamedJohn = meeting.participants.active.toArray()&#10;  .filter((p) =&gt; p.name === &#x27;John&#x27;);&#10;</code></pre>
<ul>
<li><a href="#module_RTKParticipant">RTKParticipant</a>
<ul>
<li><a href="#module_RTKParticipant+id">.id</a></li>
<li><a href="#module_RTKParticipant+userId">.userId</a></li>
<li><a href="#module_RTKParticipant+name">.name</a></li>
<li><a href="#module_RTKParticipant+picture">.picture</a></li>
<li><a href="#module_RTKParticipant+customParticipantId">.customParticipantId</a></li>
<li><a href="#module_RTKParticipant+device">.device</a></li>
<li><a href="#module_RTKParticipant+videoTrack">.videoTrack</a></li>
<li><a href="#module_RTKParticipant+audioTrack">.audioTrack</a></li>
<li><a href="#module_RTKParticipant+screenShareTracks">.screenShareTracks</a></li>
<li><a href="#module_RTKParticipant+videoEnabled">.videoEnabled</a></li>
<li><a href="#module_RTKParticipant+audioEnabled">.audioEnabled</a></li>
<li><a href="#module_RTKParticipant+screenShareEnabled">.screenShareEnabled</a></li>
<li><a href="#module_RTKParticipant+producers">.producers</a></li>
<li><a href="#module_RTKParticipant+manualProducerConfig">.manualProducerConfig</a></li>
<li><a href="#module_RTKParticipant+supportsRemoteControl">.supportsRemoteControl</a></li>
<li><a href="#module_RTKParticipant+presetName">.presetName</a></li>
<li><a href="#module_RTKParticipant+stageStatus">.stageStatus</a></li>
<li><a href="#module_RTKParticipant+isPinned">.isPinned</a></li>
<li><a href="#module_RTKParticipant+pin">.pin()</a></li>
<li><a href="#module_RTKParticipant+unpin">.unpin()</a></li>
<li><a href="#module_RTKParticipant+disableAudio">.disableAudio()</a></li>
<li><a href="#module_RTKParticipant+kick">.kick()</a></li>
<li><a href="#module_RTKParticipant+disableVideo">.disableVideo()</a></li>
<li><a href="#module_RTKParticipant+registerVideoElement">.registerVideoElement(videoElem)</a></li>
<li><a href="#module_RTKParticipant+deregisterVideoElement">.deregisterVideoElement([videoElem])</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKParticipant+id"></a></p>
<h3 id="participant-id">participant.id</h3>
The peer ID of the participant.
The participants are indexed by this ID in the participant map.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+userId"></a></p>
<h3 id="participant-userid">participant.userId</h3>
The user ID of the participant.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+name"></a></p>
<h3 id="participant-name">participant.name</h3>
The name of the participant.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+picture"></a></p>
<h3 id="participant-picture">participant.picture</h3>
The picture of the participant.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+customParticipantId"></a></p>
<h3 id="participant-customparticipantid">participant.customParticipantId</h3>
The custom id of the participant set during https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant REST API
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+device"></a></p>
<h3 id="participant-device">participant.device</h3>
The device configuration of the participant.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+videoTrack"></a></p>
<h3 id="participant-videotrack">participant.videoTrack</h3>
The participant's video track.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+audioTrack"></a></p>
<h3 id="participant-audiotrack">participant.audioTrack</h3>
The participant's audio track.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+screenShareTracks"></a></p>
<h3 id="participant-screensharetracks">participant.screenShareTracks</h3>
The participant's screenshare video and audio track.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+videoEnabled"></a></p>
<h3 id="participant-videoenabled">participant.videoEnabled</h3>
This is true if the participant's video is enabled.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+audioEnabled"></a></p>
<h3 id="participant-audioenabled">participant.audioEnabled</h3>
This is true if the participant's audio is enabled.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+screenShareEnabled"></a></p>
<h3 id="participant-screenshareenabled">participant.screenShareEnabled</h3>
This is true if the participant is screensharing.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+producers"></a></p>
<h3 id="participant-producers">participant.producers</h3>
producers created by participant
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+manualProducerConfig"></a></p>
<h3 id="participant-manualproducerconfig">participant.manualProducerConfig</h3>
producer config passed during manual subscription
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+supportsRemoteControl"></a></p>
<h3 id="participant-supportsremotecontrol">participant.supportsRemoteControl</h3>
This is true if the participant supports remote control.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+presetName"></a></p>
<h3 id="participant-presetname">participant.presetName</h3>
The preset of the participant.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+stageStatus"></a></p>
<h3 id="participant-stagestatus">participant.stageStatus</h3>
Denotes the participants's current stage status.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+isPinned"></a></p>
<h3 id="participant-ispinned">participant.isPinned</h3>
Returns true if the participant is pinned.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+pin"></a></p>
<h3 id="participant-pin">participant.pin()</h3>
Returns `participant.id` if user has permission
to pin participants.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+unpin"></a></p>
<h3 id="participant-unpin">participant.unpin()</h3>
Returns `participant.id` if user has permission
to unpin participants.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+disableAudio"></a></p>
<h3 id="participant-disableaudio">participant.disableAudio()</h3>
Disables audio for this participant.
Requires the permission to disable participant audio.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+kick"></a></p>
<h3 id="participant-kick">participant.kick()</h3>
Kicks this participant from the meeting.
Requires the permission to kick a participant.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+disableVideo"></a></p>
<h3 id="participant-disablevideo">participant.disableVideo()</h3>
Disables video for this participant.
Requires the permission to disable video for a participant.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipant"><code>RTKParticipant</code></a><br />
<a name="module_RTKParticipant+registerVideoElement"></a></p>
<h3 id="participant-registervideoelement-videoelem">participant.registerVideoElement(videoElem)</h3>
**Kind**: instance method of [<code>RTKParticipant</code>](#module_RTKParticipant)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>videoElem</td>
<td><code>HTMLVideoElement</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKParticipant+deregisterVideoElement"></a></p>
<h3 id="participant-deregistervideoelement-videoelem">participant.deregisterVideoElement([videoElem])</h3>
**Kind**: instance method of [<code>RTKParticipant</code>](#module_RTKParticipant)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>[videoElem]</td>
<td><code>HTMLVideoElement</code></td>
</tr>
</tbody>
</table>
