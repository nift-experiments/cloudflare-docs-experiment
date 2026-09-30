<!-- Auto Generated Below -->
<p><a name="module_RTKParticipants"></a></p>
<p>This module represents all the participants in the meeting (except the local user).
It consists of 4 maps:</p>
<ul>
<li><code>joined</code>: A map of all participants that have joined the meeting.</li>
<li><code>waitlisted</code>: A map of all participants that have been added to the waitlist.</li>
<li><code>active</code>: A map of active participants who should be displayed in the meeting grid.</li>
<li><code>pinned</code>: A map of pinned participants.</li>
</ul>
<ul>
<li><a href="#module_RTKParticipants">RTKParticipants</a>
<ul>
<li><a href="#module_RTKParticipants+waitlisted">.waitlisted</a></li>
<li><a href="#module_RTKParticipants+joined">.joined</a></li>
<li><a href="#module_RTKParticipants+active">.active</a></li>
<li><a href="#module_RTKParticipants+videoSubscribed">.videoSubscribed</a></li>
<li><a href="#module_RTKParticipants+audioSubscribed">.audioSubscribed</a></li>
<li><a href="#module_RTKParticipants+pinned">.pinned</a></li>
<li><a href="#module_RTKParticipants+all">.all</a></li>
<li><a href="#module_RTKParticipants+pip">.pip</a></li>
<li><a href="#module_RTKParticipants+viewMode">.viewMode</a></li>
<li><a href="#module_RTKParticipants+currentPage">.currentPage</a></li>
<li><a href="#module_RTKParticipants+lastActiveSpeaker">.lastActiveSpeaker</a></li>
<li><a href="#module_RTKParticipants+selectedPeers">.selectedPeers</a></li>
<li><a href="#module_RTKParticipants+count">.count</a></li>
<li><a href="#module_RTKParticipants+maxActiveParticipantsCount">.maxActiveParticipantsCount</a></li>
<li><a href="#module_RTKParticipants+pageCount">.pageCount</a></li>
<li><a href="#module_RTKParticipants+setMaxActiveParticipantsCount">.setMaxActiveParticipantsCount(limit)</a></li>
<li><a href="#module_RTKParticipants+acceptWaitingRoomRequest">.acceptWaitingRoomRequest(id)</a></li>
<li><a href="#module_RTKParticipants+acceptAllWaitingRoomRequest">.acceptAllWaitingRoomRequest(userIds)</a></li>
<li><a href="#module_RTKParticipants+rejectWaitingRoomRequest">.rejectWaitingRoomRequest(id)</a></li>
<li><a href="#module_RTKParticipants+setViewMode">.setViewMode(viewMode)</a></li>
<li><a href="#module_RTKParticipants+subscribe">.subscribe(peerIds, [kinds])</a></li>
<li><a href="#module_RTKParticipants+unsubscribe">.unsubscribe(peerIds, [kinds])</a></li>
<li><a href="#module_RTKParticipants+setPage">.setPage(page)</a></li>
<li><a href="#module_RTKParticipants+disableAllAudio">.disableAllAudio(allowUnmute)</a></li>
<li><a href="#module_RTKParticipants+disableAllVideo">.disableAllVideo()</a></li>
<li><a href="#module_RTKParticipants+kickAll">.kickAll()</a></li>
<li><a href="#module_RTKParticipants+broadcastMessage">.broadcastMessage(type, payload, target)</a></li>
<li><a href="#module_RTKParticipants+getAllJoinedPeers">.getAllJoinedPeers(searchQuery, limit, offset)</a></li>
<li><a href="#module_RTKParticipants+getParticipantsInMeetingPreJoin">.getParticipantsInMeetingPreJoin()</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKParticipants+waitlisted"></a></p>
<h3 id="meeting-participants-waitlisted">meeting.participants.waitlisted</h3>
Returns a list of participants waiting to join the meeting.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+joined"></a></p>
<h3 id="meeting-participants-joined">meeting.participants.joined</h3>
Returns a list of all participants in the meeting.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+active"></a></p>
<h3 id="meeting-participants-active">meeting.participants.active</h3>
Returns a list of participants whose streams are currently consumed.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+videoSubscribed"></a></p>
<h3 id="meeting-participants-videosubscribed">meeting.participants.videoSubscribed</h3>
Returns a list of participants whose video streams are currently consumed.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+audioSubscribed"></a></p>
<h3 id="meeting-participants-audiosubscribed">meeting.participants.audioSubscribed</h3>
Returns a list of participants whose audio streams are currently consumed.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+pinned"></a></p>
<h3 id="meeting-participants-pinned">meeting.participants.pinned</h3>
Returns a list of participants who have been pinned.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+all"></a></p>
<h3 id="meeting-participants-all">meeting.participants.all</h3>
Returns all added participants irrespective of whether they are currently
in the meeting or not
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+pip"></a></p>
<h3 id="meeting-participants-pip">meeting.participants.pip</h3>
Return the controls for Picture-in-Picture
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+viewMode"></a></p>
<h3 id="meeting-participants-viewmode">meeting.participants.viewMode</h3>
Indicates whether the meeting is in 'ACTIVE_GRID' mode or 'PAGINATED' mode.
<p>In 'ACTIVE_GRID' mode, participants are populated in the participants.active map
dynamically. The participants present in the map will keep changing when other
participants unmute their audio or turn on their videos.</p>
<p>In 'PAGINATED' mode, participants are populated in the participants.active map
just once, and the participants in the map will only change if the page number is
changed by the user using setPage(page).</p>
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+currentPage"></a></p>
<h3 id="meeting-participants-currentpage">meeting.participants.currentPage</h3>
This indicates the current page that has been set by the user in PAGINATED mode.
If the meeting is in ACTIVE_GRID mode, this value will be 0.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+lastActiveSpeaker"></a></p>
<h3 id="meeting-participants-lastactivespeaker">meeting.participants.lastActiveSpeaker</h3>
This stores the `participantId` of the last participant who spoke in the meeting.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+selectedPeers"></a></p>
<h3 id="meeting-participants-selectedpeers">meeting.participants.selectedPeers</h3>
Keeps a list of all participants who have been present in the selected peers list.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+count"></a></p>
<h3 id="meeting-participants-count">meeting.participants.count</h3>
Returns the number of participants who are joined in the meeting.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+maxActiveParticipantsCount"></a></p>
<h3 id="meeting-participants-maxactiveparticipantscount">meeting.participants.maxActiveParticipantsCount</h3>
Returns the maximum number of participants that can be present in
the active map.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+pageCount"></a></p>
<h3 id="meeting-participants-pagecount">meeting.participants.pageCount</h3>
Returns the number of pages that are available in the meeting in PAGINATED mode.
If the meeting is in ACTIVE_GRID mode, this value will be 0.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+setMaxActiveParticipantsCount"></a></p>
<h3 id="meeting-participants-setmaxactiveparticipantscount-limit">meeting.participants.setMaxActiveParticipantsCount(limit)</h3>
Updates the maximum number of participants that are populated in
the active map.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a></p>
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
<td>limit</td>
<td><code>number</code></td>
<td>Updated max limit</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKParticipants+acceptWaitingRoomRequest"></a></p>
<h3 id="meeting-participants-acceptwaitingroomrequest-id">meeting.participants.acceptWaitingRoomRequest(id)</h3>
Accepts requests from waitlisted participants if user
has appropriate permissions.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a></p>
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
<td>id</td>
<td><code>string</code></td>
<td>peerId or userId of the waitlisted participant.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKParticipants+acceptAllWaitingRoomRequest"></a></p>
<h3 id="meeting-participants-acceptallwaitingroomrequest-userids">meeting.participants.acceptAllWaitingRoomRequest(userIds)</h3>
We need a new event for socket service events
since if we send them all together, sequence of events
can be unreliable
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>userIds</td>
<td><code>Array.&lt;string&gt;</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKParticipants+rejectWaitingRoomRequest"></a></p>
<h3 id="meeting-participants-rejectwaitingroomrequest-id">meeting.participants.rejectWaitingRoomRequest(id)</h3>
Rejects requests from waitlisted participants if user
has appropriate permissions.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a></p>
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
<td>id</td>
<td><code>string</code></td>
<td>participantId of the waitlisted participant.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKParticipants+setViewMode"></a></p>
<h3 id="meeting-participants-setviewmode-viewmode">meeting.participants.setViewMode(viewMode)</h3>
Sets the view mode of the meeting to either ACTIVE_GRID or PAGINATED.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a></p>
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
<td>viewMode</td>
<td><code>ViewMode</code></td>
<td>The mode in which the active map should be populated</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKParticipants+subscribe"></a></p>
<h3 id="meeting-participants-subscribe-peerids-kinds">meeting.participants.subscribe(peerIds, [kinds])</h3>
**Kind**: instance method of [<code>RTKParticipants</code>](#module_RTKParticipants)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>peerIds</td>
<td><code>Array.&lt;string&gt;</code></td>
</tr>
<tr>
<td>[kinds]</td>
<td><code>Array.&lt;('audio'|'video'|'screenshareAudio'|'screenshareVideo')&gt;</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKParticipants+unsubscribe"></a></p>
<h3 id="meeting-participants-unsubscribe-peerids-kinds">meeting.participants.unsubscribe(peerIds, [kinds])</h3>
**Kind**: instance method of [<code>RTKParticipants</code>](#module_RTKParticipants)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>peerIds</td>
<td><code>Array.&lt;string&gt;</code></td>
</tr>
<tr>
<td>[kinds]</td>
<td><code>Array.&lt;('audio'|'video'|'screenshareAudio'|'screenshareVideo')&gt;</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKParticipants+setPage"></a></p>
<h3 id="meeting-participants-setpage-page">meeting.participants.setPage(page)</h3>
Populates the active map with participants present in the page number
indicated by the parameter `page` in PAGINATED mode.
Does not do anything in ACTIVE_GRID mode.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a></p>
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
<td>page</td>
<td><code>number</code></td>
<td>The page number to be set.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKParticipants+disableAllAudio"></a></p>
<h3 id="meeting-participants-disableallaudio-allowunmute">meeting.participants.disableAllAudio(allowUnmute)</h3>
Disables audio for all participants in the meeting.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a></p>
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
<td>allowUnmute</td>
<td><code>boolean</code></td>
<td>Allow participants to unmute after they are muted.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKParticipants+disableAllVideo"></a></p>
<h3 id="meeting-participants-disableallvideo">meeting.participants.disableAllVideo()</h3>
Disables video for all participants in the meeting.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+kickAll"></a></p>
<h3 id="meeting-participants-kickall">meeting.participants.kickAll()</h3>
Kicks all participants from the meeting.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a><br />
<a name="module_RTKParticipants+broadcastMessage"></a></p>
<h3 id="meeting-participants-broadcastmessage-type-payload-target">meeting.participants.broadcastMessage(type, payload, target)</h3>
Broadcasts the message to participants
<p>If no <code>target</code> is specified it is sent to all participants including <code>self</code>.</p>
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a></p>
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
<td>type</td>
<td><code>string</code></td>
<td></td>
</tr>
<tr>
<td>payload</td>
<td><code>BroadcastMessagePayload</code></td>
<td></td>
</tr>
<tr>
<td>target</td>
<td><code>BroadcastMessageTarget</code></td>
<td>object containing a list of <code>participantIds</code> or object containing <code>presetName</code> - every user with that preset will be sent the message</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKParticipants+getAllJoinedPeers"></a></p>
<h3 id="meeting-participants-getalljoinedpeers-searchquery-limit-offset">meeting.participants.getAllJoinedPeers(searchQuery, limit, offset)</h3>
Returns all peers currently present in the room
If you are in a group call, use `meeting.participants.joined`
instead
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>searchQuery</td>
<td><code>string</code></td>
</tr>
<tr>
<td>limit</td>
<td><code>number</code></td>
</tr>
<tr>
<td>offset</td>
<td><code>number</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKParticipants+getParticipantsInMeetingPreJoin"></a></p>
<h3 id="meeting-participants-getparticipantsinmeetingprejoin">meeting.participants.getParticipantsInMeetingPreJoin()</h3>
Returns all peers currently in the room, is a non paginated call
and should only be used if you are in a non room joined state,
if in a joined group call, use `meeting.participants.joined`
<p><strong>Kind</strong>: instance method of <a href="#module_RTKParticipants"><code>RTKParticipants</code></a></p>
