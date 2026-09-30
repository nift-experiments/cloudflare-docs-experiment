<!-- Auto Generated Below -->
<p><a name="module_RTKMeta"></a></p>
<p>This consists of the metadata of the meeting, such as the room name and the title.</p>
<ul>
<li><a href="#module_RTKMeta">RTKMeta</a>
<ul>
<li><a href="#module_RTKMeta+selfActiveTab">.selfActiveTab</a></li>
<li><a href="#module_RTKMeta+broadcastTabChanges">.broadcastTabChanges</a></li>
<li><a href="#module_RTKMeta+viewType">.viewType</a></li>
<li><a href="#module_RTKMeta+meetingStartedTimestamp">.meetingStartedTimestamp</a></li>
<li><a href="#module_RTKMeta+meetingTitle">.meetingTitle</a></li>
<li><a href="#module_RTKMeta+sessionId">.sessionId</a></li>
<li><a href="#module_RTKMeta+meetingId">.meetingId</a></li>
<li><a href="#module_RTKMeta+setBroadcastTabChanges">.setBroadcastTabChanges(broadcastTabChanges)</a></li>
<li><a href="#module_RTKMeta+setSelfActiveTab">.setSelfActiveTab(spotlightTab, tabChangeSource)</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKMeta+selfActiveTab"></a></p>
<h3 id="meeting-meta-selfactivetab">meeting.meta.selfActiveTab</h3>
Represents the current active tab
<p><strong>Kind</strong>: instance property of <a href="#module_RTKMeta"><code>RTKMeta</code></a><br />
<a name="module_RTKMeta+broadcastTabChanges"></a></p>
<h3 id="meeting-meta-broadcasttabchanges">meeting.meta.broadcastTabChanges</h3>
Represents whether current user is spotlighted
<p><strong>Kind</strong>: instance property of <a href="#module_RTKMeta"><code>RTKMeta</code></a><br />
<a name="module_RTKMeta+viewType"></a></p>
<h3 id="meeting-meta-viewtype">meeting.meta.viewType</h3>
The `viewType` tells the type of the meeting
possible values are: GROUP_CALL| LIVESTREAM | CHAT | AUDIO_ROOM
<p><strong>Kind</strong>: instance property of <a href="#module_RTKMeta"><code>RTKMeta</code></a><br />
<a name="module_RTKMeta+meetingStartedTimestamp"></a></p>
<h3 id="meeting-meta-meetingstartedtimestamp">meeting.meta.meetingStartedTimestamp</h3>
The timestamp of the time when the meeting started.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKMeta"><code>RTKMeta</code></a><br />
<a name="module_RTKMeta+meetingTitle"></a></p>
<h3 id="meeting-meta-meetingtitle">meeting.meta.meetingTitle</h3>
The title of the meeting.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKMeta"><code>RTKMeta</code></a><br />
<a name="module_RTKMeta+sessionId"></a></p>
<h3 id="meeting-meta-sessionid">meeting.meta.sessionId</h3>
(Experimental) The sessionId this meeting object is part of.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKMeta"><code>RTKMeta</code></a><br />
<a name="module_RTKMeta+meetingId"></a></p>
<h3 id="meeting-meta-meetingid">meeting.meta.meetingId</h3>
The room name of the meeting.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKMeta"><code>RTKMeta</code></a><br />
<a name="module_RTKMeta+setBroadcastTabChanges"></a></p>
<h3 id="meeting-meta-setbroadcasttabchanges-broadcasttabchanges">meeting.meta.setBroadcastTabChanges(broadcastTabChanges)</h3>
Sets current user as broadcasting tab changes
<p><strong>Kind</strong>: instance method of <a href="#module_RTKMeta"><code>RTKMeta</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>broadcastTabChanges</td>
<td><code>boolean</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKMeta+setSelfActiveTab"></a></p>
<h3 id="meeting-meta-setselfactivetab-spotlighttab-tabchangesource">meeting.meta.setSelfActiveTab(spotlightTab, tabChangeSource)</h3>
Sets current active tab for user
<p><strong>Kind</strong>: instance method of <a href="#module_RTKMeta"><code>RTKMeta</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>spotlightTab</td>
<td><code>ActiveTab</code></td>
</tr>
<tr>
<td>tabChangeSource</td>
<td><code>TabChangeSource</code></td>
</tr>
</tbody>
</table>
