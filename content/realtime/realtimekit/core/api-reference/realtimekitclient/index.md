<!-- Auto Generated Below -->
<p><a name="module_RealtimeKitClient"></a></p>
<p>The RealtimeKitClient class is the main class of the web core library.
An object of the RealtimeKitClient class can be created using
<code>await RealtimeKitClient.init({ ... })</code>. Typically, an object of <code>RealtimeKitClient</code> is
named <code>meeting</code>.</p>
<ul>
<li><a href="#module_RealtimeKitClient">RealtimeKitClient</a>
<ul>
<li><em>instance</em>
<ul>
<li><a href="#module_RealtimeKitClient+participants">.participants</a></li>
<li><a href="#module_RealtimeKitClient+self">.self</a></li>
<li><a href="#module_RealtimeKitClient+meta">.meta</a></li>
<li><a href="#module_RealtimeKitClient+ai">.ai</a></li>
<li><a href="#module_RealtimeKitClient+plugins">.plugins</a></li>
<li><a href="#module_RealtimeKitClient+chat">.chat</a></li>
<li><a href="#module_RealtimeKitClient+polls">.polls</a></li>
<li><a href="#module_RealtimeKitClient+connectedMeetings">.connectedMeetings</a></li>
<li><a href="#module_RealtimeKitClient+__internals__">.<strong>internals</strong></a></li>
<li><a href="#module_RealtimeKitClient+join">.join()</a></li>
<li><a href="#module_RealtimeKitClient+leave">.leave()</a></li>
</ul>
</li>
<li><em>static</em>
<ul>
<li><a href="#module_RealtimeKitClient.initMedia">.initMedia([options], [skipAwaits], [cachedUserDetails])</a></li>
<li><a href="#module_RealtimeKitClient.init">.init(options)</a></li>
</ul>
</li>
</ul>
</li>
</ul>
<p><a name="module_RealtimeKitClient+participants"></a></p>
<h3 id="meeting-participants">meeting.participants</h3>
The `participants` object consists of 4 maps of participants,
`waitlisted`, `joined`, `active`, `pinned`. The maps are indexed by
`peerId`s, and the values are the corresponding participant objects.
<p><strong>Kind</strong>: instance property of <a href="#module_RealtimeKitClient"><code>RealtimeKitClient</code></a><br />
<a name="module_RealtimeKitClient+self"></a></p>
<h3 id="meeting-self">meeting.self</h3>
The `self` object can be used to manipulate audio and video settings,
and other configurations for the local participant. This exposes methods
to enable and disable media tracks, share the user's screen, etc.
<p><strong>Kind</strong>: instance property of <a href="#module_RealtimeKitClient"><code>RealtimeKitClient</code></a><br />
<a name="module_RealtimeKitClient+meta"></a></p>
<h3 id="meeting-meta">meeting.meta</h3>
The `room` object stores information about the current meeting, such
as chat messages, polls, room name, etc.
<p><strong>Kind</strong>: instance property of <a href="#module_RealtimeKitClient"><code>RealtimeKitClient</code></a><br />
<a name="module_RealtimeKitClient+ai"></a></p>
<h3 id="meeting-ai">meeting.ai</h3>
The `ai` object is used to interface with AI features.
You can obtain the live meeting transcript and use other meeting AI
features such as summary, and agenda using this object.
<p><strong>Kind</strong>: instance property of <a href="#module_RealtimeKitClient"><code>RealtimeKitClient</code></a><br />
<a name="module_RealtimeKitClient+plugins"></a></p>
<h3 id="meeting-plugins">meeting.plugins</h3>
The `plugins` object stores information about the plugins available in
the current meeting. It exposes methods to activate and deactivate them.
<p><strong>Kind</strong>: instance property of <a href="#module_RealtimeKitClient"><code>RealtimeKitClient</code></a><br />
<a name="module_RealtimeKitClient+chat"></a></p>
<h3 id="meeting-chat">meeting.chat</h3>
The chat object stores the chat messages that were sent in the meeting.
This includes text messages, images, and files.
<p><strong>Kind</strong>: instance property of <a href="#module_RealtimeKitClient"><code>RealtimeKitClient</code></a><br />
<a name="module_RealtimeKitClient+polls"></a></p>
<h3 id="meeting-polls">meeting.polls</h3>
The polls object stores the polls that were initiated in the meeting.
It exposes methods to create and vote on polls.
<p><strong>Kind</strong>: instance property of <a href="#module_RealtimeKitClient"><code>RealtimeKitClient</code></a><br />
<a name="module_RealtimeKitClient+connectedMeetings"></a></p>
<h3 id="meeting-connectedmeetings">meeting.connectedMeetings</h3>
The connectedMeetings object stores the connected meetings states.
It exposes methods to create/read/update/delete methods for connected meetings.
<p><strong>Kind</strong>: instance property of <a href="#module_RealtimeKitClient"><code>RealtimeKitClient</code></a><br />
<a name="module_RealtimeKitClient+__internals__"></a></p>
<h3 id="meeting-internals">meeting.__internals__</h3>
The __internals__ object exposes the internal tools & utilities such as features and logger
so that client can utilise the same to build their own feature based UI.
Logger (__internals__.logger) can be used to send logs to servers
	to inform  of issues, if any, proactively.
<p><strong>Kind</strong>: instance property of <a href="#module_RealtimeKitClient"><code>RealtimeKitClient</code></a><br />
<a name="module_RealtimeKitClient+join"></a></p>
<h3 id="meeting-join">meeting.join()</h3>
The `join()` method can be used to join the meeting.
A `roomJoined` event is emitted on `self` when the room
is joined successfully.
<p><strong>Kind</strong>: instance method of <a href="#module_RealtimeKitClient"><code>RealtimeKitClient</code></a><br />
<a name="module_RealtimeKitClient+leave"></a></p>
<h3 id="meeting-leave">meeting.leave()</h3>
The `leave()` method can be used to leave a meeting.
<p><strong>Kind</strong>: instance method of <a href="#module_RealtimeKitClient"><code>RealtimeKitClient</code></a><br />
<a name="module_RealtimeKitClient.initMedia"></a></p>
<h3 id="meeting-initmedia-options-skipawaits-cacheduserdetails">meeting.initMedia([options], [skipAwaits], [cachedUserDetails])</h3>
**Kind**: static method of [<code>RealtimeKitClient</code>](#module_RealtimeKitClient)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td>[options]</td>
<td><code>Object</code></td>
<td></td>
</tr>
<tr>
<td>[options.video]</td>
<td><code>boolean</code></td>
<td></td>
</tr>
<tr>
<td>[options.audio]</td>
<td><code>boolean</code></td>
<td></td>
</tr>
<tr>
<td>[options.constraints]</td>
<td><code>MediaConstraints</code></td>
<td></td>
</tr>
<tr>
<td>[skipAwaits]</td>
<td><code>boolean</code></td>
<td><code>false</code></td>
</tr>
<tr>
<td>[cachedUserDetails]</td>
<td><code>CachedUserDetails</code></td>
<td></td>
</tr>
</tbody>
</table>
<p><a name="module_RealtimeKitClient.init"></a></p>
<h3 id="meeting-init-options">meeting.init(options)</h3>
The `init` method can be used to instantiate the RealtimeKitClient class.
This returns an instance of RealtimeKitClient, which can be used to perform
actions on the meeting.
<p><strong>Kind</strong>: static method of <a href="#module_RealtimeKitClient"><code>RealtimeKitClient</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>options</td>
<td>The options object.</td>
</tr>
<tr>
<td>options.authToken</td>
<td>The authorization token received using the API.</td>
</tr>
<tr>
<td>options.baseURI</td>
<td>The base URL of the API.</td>
</tr>
<tr>
<td>options.defaults</td>
<td>The default audio and video settings.</td>
</tr>
</tbody>
</table>
