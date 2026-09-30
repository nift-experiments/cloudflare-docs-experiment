<!-- Auto Generated Below -->
<p><a name="module_RTKSelf"></a></p>
<p>The RTKSelf module represents the current user, and allows to modify the state
of the user in the meeting. The audio and video streams of the user can be retrieved from
this module.</p>
<ul>
<li><a href="#module_RTKSelf">RTKSelf</a>
<ul>
<li><a href="#module_RTKSelf+peerId">.peerId</a></li>
<li><a href="#module_RTKSelf+roomState">.roomState</a></li>
<li><a href="#module_RTKSelf+permissions">.permissions</a></li>
<li><a href="#module_RTKSelf+config">.config</a></li>
<li><a href="#module_RTKSelf+roomJoined">.roomJoined</a></li>
<li><a href="#module_RTKSelf+isPinned">.isPinned</a></li>
<li><a href="#module_RTKSelf+cleanupEvents">.cleanupEvents()</a></li>
<li><a href="#module_RTKSelf+setName">.setName(name)</a></li>
<li><a href="#module_RTKSelf+setupTracks">.setupTracks(options)</a></li>
<li><a href="#module_RTKSelf+enableAudio">.enableAudio()</a></li>
<li><a href="#module_RTKSelf+enableVideo">.enableVideo()</a></li>
<li><a href="#module_RTKSelf+updateVideoConstraints">.updateVideoConstraints()</a></li>
<li><a href="#module_RTKSelf+enableScreenShare">.enableScreenShare()</a></li>
<li><a href="#module_RTKSelf+updateScreenshareConstraints">.updateScreenshareConstraints()</a></li>
<li><a href="#module_RTKSelf+disableAudio">.disableAudio()</a></li>
<li><a href="#module_RTKSelf+disableVideo">.disableVideo()</a></li>
<li><a href="#module_RTKSelf+disableScreenShare">.disableScreenShare()</a></li>
<li><a href="#module_RTKSelf+getAllDevices">.getAllDevices()</a></li>
<li><a href="#module_RTKSelf+pin">.pin()</a></li>
<li><a href="#module_RTKSelf+unpin">.unpin()</a></li>
<li><a href="#module_RTKSelf+hide">.hide()</a></li>
<li><a href="#module_RTKSelf+show">.show()</a></li>
<li><a href="#module_RTKSelf+setDevice">.setDevice(device)</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKSelf+peerId"></a></p>
<h3 id="meeting-self-peerid">meeting.self.peerId</h3>
NOTE(ishita1805): Discussed with Ravindra, added a duplicate for consistency
when using identifiers in Locker.
We might want to look at deprecating the `id` sometime later.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+roomState"></a></p>
<h3 id="meeting-self-roomstate">meeting.self.roomState</h3>
Returns the current state of room
init - Initial State
joined - User is in the meeting
waitlisted - User is in the waitlist state
rejected - User's was in the waiting room, but the entry was rejected
kicked - A privileged user removed the user from the meeting
left - User left the meeting
ended - The meeting was ended
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+permissions"></a></p>
<h3 id="meeting-self-permissions">meeting.self.permissions</h3>
Returns the current permission given to the user for the meeting.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+config"></a></p>
<h3 id="meeting-self-config">meeting.self.config</h3>
Returns configuration for the meeting.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+roomJoined"></a></p>
<h3 id="meeting-self-roomjoined">meeting.self.roomJoined</h3>
Returns true if the local participant has joined the meeting.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+isPinned"></a></p>
<h3 id="meeting-self-ispinned">meeting.self.isPinned</h3>
Returns true if the current user is pinned.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+cleanupEvents"></a></p>
<h3 id="meeting-self-cleanupevents">meeting.self.cleanupEvents()</h3>
**Kind**: instance method of [<code>RTKSelf</code>](#module_RTKSelf)  
<a name="module_RTKSelf+setName"></a>
<h3 id="meeting-self-setname-name">meeting.self.setName(name)</h3>
The name of the user can be set by calling this method.
This will get reflected to other participants ONLY if
this method is called before the room is joined.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>name</td>
<td><code>string</code></td>
<td>Name of the user.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKSelf+setupTracks"></a></p>
<h3 id="meeting-self-setuptracks-options">meeting.self.setupTracks(options)</h3>
Sets up the local media tracks.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>options</td>
<td><code>Object</code></td>
<td>The audio and video options.</td>
</tr>
<tr>
<td>[options.video]</td>
<td><code>boolean</code></td>
<td>If true, the video stream is fetched.</td>
</tr>
<tr>
<td>[options.audio]</td>
<td><code>boolean</code></td>
<td>If true, the audio stream is fetched.</td>
</tr>
<tr>
<td>[options.forceReset]</td>
<td><code>boolean</code></td>
<td>If true, force resets tracks before re-acquiring.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKSelf+enableAudio"></a></p>
<h3 id="meeting-self-enableaudio">meeting.self.enableAudio()</h3>
This method is used to unmute the local participant's audio.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+enableVideo"></a></p>
<h3 id="meeting-self-enablevideo">meeting.self.enableVideo()</h3>
This method is used to start streaming the local participant's video
to the meeting.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+updateVideoConstraints"></a></p>
<h3 id="meeting-self-updatevideoconstraints">meeting.self.updateVideoConstraints()</h3>
This method is used to apply constraints to the current video
stream.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+enableScreenShare"></a></p>
<h3 id="meeting-self-enablescreenshare">meeting.self.enableScreenShare()</h3>
This method is used to start sharing the local participant's screen
to the meeting.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+updateScreenshareConstraints"></a></p>
<h3 id="meeting-self-updatescreenshareconstraints">meeting.self.updateScreenshareConstraints()</h3>
This method is used to apply constraints to the current screenshare
stream.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+disableAudio"></a></p>
<h3 id="meeting-self-disableaudio">meeting.self.disableAudio()</h3>
This method is used to mute the local participant's audio.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+disableVideo"></a></p>
<h3 id="meeting-self-disablevideo">meeting.self.disableVideo()</h3>
This participant is used to disable the local participant's video.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+disableScreenShare"></a></p>
<h3 id="meeting-self-disablescreenshare">meeting.self.disableScreenShare()</h3>
This method is used to stop sharing the local participant's screen.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+getAllDevices"></a></p>
<h3 id="meeting-self-getalldevices">meeting.self.getAllDevices()</h3>
Returns all media devices accessible by the local participant.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+pin"></a></p>
<h3 id="meeting-self-pin">meeting.self.pin()</h3>
Returns `self.id` if user has permission
to pin participants.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+unpin"></a></p>
<h3 id="meeting-self-unpin">meeting.self.unpin()</h3>
Returns `self.id` if user has permission
to unpin participants.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+hide"></a></p>
<h3 id="meeting-self-hide">meeting.self.hide()</h3>
Hide's user's tile in the UI (locally)
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+show"></a></p>
<h3 id="meeting-self-show">meeting.self.show()</h3>
Show's user's tile in the UI if hidden (locally)
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a><br />
<a name="module_RTKSelf+setDevice"></a></p>
<h3 id="meeting-self-setdevice-device">meeting.self.setDevice(device)</h3>
Change the current media device that is being used by the local participant.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelf"><code>RTKSelf</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>device</td>
<td><code>MediaDeviceInfo</code></td>
<td>The device that is to be used. A device of the same <code>kind</code> will be replaced. the primary stream.</td>
</tr>
</tbody>
</table>
