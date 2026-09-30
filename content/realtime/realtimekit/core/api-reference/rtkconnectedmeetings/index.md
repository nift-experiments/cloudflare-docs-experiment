<!-- Auto Generated Below -->
<p><a name="module_RTKConnectedMeetings"></a></p>
<p>This consists of the methods to facilitate connected meetings</p>
<ul>
<li><a href="#module_RTKConnectedMeetings">RTKConnectedMeetings</a>
<ul>
<li><a href="#module_RTKConnectedMeetings+getConnectedMeetings">.getConnectedMeetings()</a></li>
<li><a href="#module_RTKConnectedMeetings+createMeetings">.createMeetings(request)</a></li>
<li><a href="#module_RTKConnectedMeetings+updateMeetings">.updateMeetings(request)</a></li>
<li><a href="#module_RTKConnectedMeetings+deleteMeetings">.deleteMeetings(meetingIds)</a></li>
<li><a href="#module_RTKConnectedMeetings+moveParticipants">.moveParticipants(sourceMeetingId, destinationMeetingId, participantIds)</a></li>
<li><a href="#module_RTKConnectedMeetings+moveParticipantsWithCustomPreset">.moveParticipantsWithCustomPreset(sourceMeetingId, destinationMeetingId, participants)</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKConnectedMeetings+getConnectedMeetings"></a></p>
<h3 id="meeting-connectedmeetings-getconnectedmeetings">meeting.connectedMeetings.getConnectedMeetings()</h3>
get connected meeting state
<p><strong>Kind</strong>: instance method of <a href="#module_RTKConnectedMeetings"><code>RTKConnectedMeetings</code></a><br />
<a name="module_RTKConnectedMeetings+createMeetings"></a></p>
<h3 id="meeting-connectedmeetings-createmeetings-request">meeting.connectedMeetings.createMeetings(request)</h3>
create connected meetings
<p><strong>Kind</strong>: instance method of <a href="#module_RTKConnectedMeetings"><code>RTKConnectedMeetings</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>request</td>
<td><code>Array.&lt;{title: string}&gt;</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKConnectedMeetings+updateMeetings"></a></p>
<h3 id="meeting-connectedmeetings-updatemeetings-request">meeting.connectedMeetings.updateMeetings(request)</h3>
update meeting title
<p><strong>Kind</strong>: instance method of <a href="#module_RTKConnectedMeetings"><code>RTKConnectedMeetings</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>request</td>
<td><code>Array.&lt;{id: string, title: string}&gt;</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKConnectedMeetings+deleteMeetings"></a></p>
<h3 id="meeting-connectedmeetings-deletemeetings-meetingids">meeting.connectedMeetings.deleteMeetings(meetingIds)</h3>
delete connected meetings
<p><strong>Kind</strong>: instance method of <a href="#module_RTKConnectedMeetings"><code>RTKConnectedMeetings</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>meetingIds</td>
<td><code>Array.&lt;string&gt;</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKConnectedMeetings+moveParticipants"></a></p>
<h3 id="meeting-connectedmeetings-moveparticipants-sourcemeetingid-destinationmeetingid-participantids">meeting.connectedMeetings.moveParticipants(sourceMeetingId, destinationMeetingId, participantIds)</h3>
Trigger event to move participants
<p><strong>Kind</strong>: instance method of <a href="#module_RTKConnectedMeetings"><code>RTKConnectedMeetings</code></a></p>
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
<td>sourceMeetingId</td>
<td><code>string</code></td>
<td>id of source meeting</td>
</tr>
<tr>
<td>destinationMeetingId</td>
<td><code>string</code></td>
<td>id of destination meeting</td>
</tr>
<tr>
<td>participantIds</td>
<td><code>Array.&lt;string&gt;</code></td>
<td>list of id of the participants</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKConnectedMeetings+moveParticipantsWithCustomPreset"></a></p>
<h3 id="meeting-connectedmeetings-moveparticipantswithcustompreset-sourcemeetingid-destinationmeetingid-participants">meeting.connectedMeetings.moveParticipantsWithCustomPreset(sourceMeetingId, destinationMeetingId, participants)</h3>
Trigger event to move participants with custom preset
<p><strong>Kind</strong>: instance method of <a href="#module_RTKConnectedMeetings"><code>RTKConnectedMeetings</code></a></p>
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
<td>sourceMeetingId</td>
<td><code>string</code></td>
<td>id of source meeting</td>
</tr>
<tr>
<td>destinationMeetingId</td>
<td><code>string</code></td>
<td>id of destination meeting</td>
</tr>
<tr>
<td>participants</td>
<td><code>Array.&lt;{id: string, presetId: string}&gt;</code></td>
<td></td>
</tr>
</tbody>
</table>
