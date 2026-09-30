<!-- Auto Generated Below -->
<p><a name="module_PermissionPreset"></a></p>
<p>The PermissionPreset class represents the meeting permissions for the current participant</p>
<ul>
<li><a href="#module_PermissionPreset">PermissionPreset</a>
<ul>
<li><a href="#module_PermissionPreset+stageEnabled">.stageEnabled</a></li>
<li><a href="#module_PermissionPreset+stageAccess">.stageAccess</a></li>
<li><a href="#module_PermissionPreset+acceptWaitingRequests">.acceptWaitingRequests</a></li>
<li><a href="#module_PermissionPreset+requestProduceVideo">.requestProduceVideo</a></li>
<li><a href="#module_PermissionPreset+requestProduceAudio">.requestProduceAudio</a></li>
<li><a href="#module_PermissionPreset+requestProduceScreenshare">.requestProduceScreenshare</a></li>
<li><a href="#module_PermissionPreset+canAllowParticipantAudio">.canAllowParticipantAudio</a></li>
<li><a href="#module_PermissionPreset+canAllowParticipantScreensharing">.canAllowParticipantScreensharing</a></li>
<li><a href="#module_PermissionPreset+canAllowParticipantVideo">.canAllowParticipantVideo</a></li>
<li><a href="#module_PermissionPreset+canDisableParticipantAudio">.canDisableParticipantAudio</a></li>
<li><a href="#module_PermissionPreset+canDisableParticipantVideo">.canDisableParticipantVideo</a></li>
<li><a href="#module_PermissionPreset+kickParticipant">.kickParticipant</a></li>
<li><a href="#module_PermissionPreset+pinParticipant">.pinParticipant</a></li>
<li><a href="#module_PermissionPreset+canRecord">.canRecord</a></li>
<li><a href="#module_PermissionPreset+waitingRoomBehaviour">.waitingRoomBehaviour</a></li>
<li><a href="#module_PermissionPreset+plugins">.plugins</a></li>
<li><a href="#module_PermissionPreset+polls">.polls</a></li>
<li><a href="#module_PermissionPreset+canProduceVideo">.canProduceVideo</a></li>
<li><a href="#module_PermissionPreset+canProduceScreenshare">.canProduceScreenshare</a></li>
<li><a href="#module_PermissionPreset+canProduceAudio">.canProduceAudio</a></li>
<li><a href="#module_PermissionPreset+chatPublic">.chatPublic</a></li>
<li><a href="#module_PermissionPreset+chatPrivate">.chatPrivate</a></li>
<li><a href="#module_PermissionPreset+hiddenParticipant">.hiddenParticipant</a></li>
<li><a href="#module_PermissionPreset+showParticipantList">.showParticipantList</a></li>
<li><a href="#module_PermissionPreset+canChangeParticipantPermissions">.canChangeParticipantPermissions</a></li>
<li><a href="#module_PermissionPreset+canLivestream">.canLivestream</a></li>
</ul>
</li>
</ul>
<p><a name="module_PermissionPreset+stageEnabled"></a></p>
<h3 id="meeting-self-permissions-stageenabled">meeting.self.permissions.stageEnabled</h3>
The `stageEnabled` property returns a boolean value.
If `true`, stage management is available for the participant.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+stageAccess"></a></p>
<h3 id="meeting-self-permissions-stageaccess">meeting.self.permissions.stageAccess</h3>
The `stageAccess` property dictates how a user interacts with the stage.
The possible values are `ALLOWED`, `NOT_ALLOWED`, `CAN_REQUEST`;
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+acceptWaitingRequests"></a></p>
<h3 id="meeting-self-permissions-acceptwaitingrequests">meeting.self.permissions.acceptWaitingRequests</h3>
The `acceptWaitingRequests` returns boolean value.
If `true`, participant can accept the request of waiting participant.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+requestProduceVideo"></a></p>
<h3 id="meeting-self-permissions-requestproducevideo">meeting.self.permissions.requestProduceVideo</h3>
The `requestProduceVideo` returns boolean value.
If `true`, participant can send request to participants
about producing video.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+requestProduceAudio"></a></p>
<h3 id="meeting-self-permissions-requestproduceaudio">meeting.self.permissions.requestProduceAudio</h3>
The `requestProduceAudio` returns boolean value.
If `true`, participant can send request to participants
about producing audio.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+requestProduceScreenshare"></a></p>
<h3 id="meeting-self-permissions-requestproducescreenshare">meeting.self.permissions.requestProduceScreenshare</h3>
The `requestProduceScreenshare` returns boolean value.
If `true`, participant can send request to participants
about sharing screen.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+canAllowParticipantAudio"></a></p>
<h3 id="meeting-self-permissions-canallowparticipantaudio">meeting.self.permissions.canAllowParticipantAudio</h3>
The `canAllowParticipantAudio` returns boolean value.
If `true`, participant can enable other participants` audio.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+canAllowParticipantScreensharing"></a></p>
<h3 id="meeting-self-permissions-canallowparticipantscreensharing">meeting.self.permissions.canAllowParticipantScreensharing</h3>
The `canAllowParticipantScreensharing` returns boolean value.
If `true`, participant can enable other participants` screen share.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+canAllowParticipantVideo"></a></p>
<h3 id="meeting-self-permissions-canallowparticipantvideo">meeting.self.permissions.canAllowParticipantVideo</h3>
The `canAllowParticipantVideo` returns boolean value.
If `true`, participant can enable other participants` video.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+canDisableParticipantAudio"></a></p>
<h3 id="meeting-self-permissions-candisableparticipantaudio">meeting.self.permissions.canDisableParticipantAudio</h3>
If `true`, a participant can disable other participants` audio.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+canDisableParticipantVideo"></a></p>
<h3 id="meeting-self-permissions-candisableparticipantvideo">meeting.self.permissions.canDisableParticipantVideo</h3>
If `true`, a participant can disable other participants` video.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+kickParticipant"></a></p>
<h3 id="meeting-self-permissions-kickparticipant">meeting.self.permissions.kickParticipant</h3>
The `kickParticipant` returns boolean value.
If `true`, participant can remove other participants from the meeting.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+pinParticipant"></a></p>
<h3 id="meeting-self-permissions-pinparticipant">meeting.self.permissions.pinParticipant</h3>
The `pinParticipant` returns boolean value.
If `true`, participant can pin a participant in the meeting.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+canRecord"></a></p>
<h3 id="meeting-self-permissions-canrecord">meeting.self.permissions.canRecord</h3>
The `canRecord` returns boolean value.
If `true`, participant can record the meeting.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+waitingRoomBehaviour"></a></p>
<h3 id="meeting-self-permissions-waitingroombehaviour">meeting.self.permissions.waitingRoomBehaviour</h3>
The `waitingRoomType` returns string value.
type of waiting room behavior
possible values are `SKIP`, `ON_PRIVILEGED_USER_ENTRY`, `SKIP_ON_ACCEPT`
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+plugins"></a></p>
<h3 id="meeting-self-permissions-plugins">meeting.self.permissions.plugins</h3>
The `plugins` tells if the participant can act on plugins
there are 2 permissions with boolean values, `canStart` and `canClose`.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+polls"></a></p>
<h3 id="meeting-self-permissions-polls">meeting.self.permissions.polls</h3>
The `polls` tells if the participant can use polls.
There are 3 permissions with boolean values, `canCreate`, `canVote`, `canViewResults`
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+canProduceVideo"></a></p>
<h3 id="meeting-self-permissions-canproducevideo">meeting.self.permissions.canProduceVideo</h3>
The `canProduceVideo` shows permissions for enabling video.
There possible values are `ALLOWED`, `NOT_ALLOWED`, `CAN_REQUEST`
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+canProduceScreenshare"></a></p>
<h3 id="meeting-self-permissions-canproducescreenshare">meeting.self.permissions.canProduceScreenshare</h3>
The `canProduceScreenshare` shows permissions for sharing screen.
There possible values are `ALLOWED`, `NOT_ALLOWED`, `CAN_REQUEST`
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+canProduceAudio"></a></p>
<h3 id="meeting-self-permissions-canproduceaudio">meeting.self.permissions.canProduceAudio</h3>
The `canProduceAudio` shows permissions for enabling audio.
There possible values are `ALLOWED`, `NOT_ALLOWED`, `CAN_REQUEST`
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+chatPublic"></a></p>
<h3 id="meeting-self-permissions-chatpublic">meeting.self.permissions.chatPublic</h3>
The `chatPublic` shows permissions for public chat
there are 4 permissions
`canSend` - if true, the participant can send chat
`text` - if true, the participant can send text
`files` - if true, the participant can send files
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+chatPrivate"></a></p>
<h3 id="meeting-self-permissions-chatprivate">meeting.self.permissions.chatPrivate</h3>
The `chatPrivate` shows permissions for public chat
there are 4 permissions
`canSend` - if true, the participant can send private chat
`text` - if true, the participant can send text as private chat
`files` - if true, the participant can send files as private chat
`canReceive` - (optional) if true, the participant can receive private chat
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+hiddenParticipant"></a></p>
<h3 id="meeting-self-permissions-hiddenparticipant">meeting.self.permissions.hiddenParticipant</h3>
The `hiddenParticipant` returns boolean value.
If `true`, participant is hidden.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+showParticipantList"></a></p>
<h3 id="meeting-self-permissions-showparticipantlist">meeting.self.permissions.showParticipantList</h3>
The `showParticipantList` returns boolean value.
If `true`, participant list can be shown to the participant.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+canChangeParticipantPermissions"></a></p>
<h3 id="meeting-self-permissions-canchangeparticipantpermissions">meeting.self.permissions.canChangeParticipantPermissions</h3>
The `canChangeParticipantPermissions` returns boolean value.
If `true`, allow changing the participants' permissions.
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a><br />
<a name="module_PermissionPreset+canLivestream"></a></p>
<h3 id="meeting-self-permissions-canlivestream">meeting.self.permissions.canLivestream</h3>
Livestream
<p><strong>Kind</strong>: instance property of <a href="#module_PermissionPreset"><code>PermissionPreset</code></a></p>
