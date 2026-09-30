<!-- Auto Generated Below -->
<h2 id="modules">Modules</h2>
<dl>
<dt><a href="#module_RTKPip">RTKPip</a></dt>
<dd></dd>
</dl>
<h2 id="functions">Functions</h2>
<dl>
<dt><a href="#getInitials">getInitials()</a></dt>
<dd><p>Code from ui-kit. Same method used in the avatar component</p>
</dd>
</dl>
<p><a name="module_RTKPip"></a></p>
<ul>
<li><a href="#module_RTKPip">RTKPip</a>
<ul>
<li><a href="#module_RTKPip+disable">.disable</a></li>
<li><a href="#module_RTKPip+init">.init([options])</a></li>
<li><a href="#module_RTKPip+disableSource">.disableSource(source)</a></li>
<li><a href="#module_RTKPip+addSource">.addSource(id, element, enabled, [displayText])</a></li>
<li><a href="#module_RTKPip+updateSource">.updateSource(id, source)</a></li>
<li><a href="#module_RTKPip+removeSource">.removeSource(id)</a></li>
<li><a href="#module_RTKPip+removePinnedSource">.removePinnedSource(id)</a></li>
<li><a href="#module_RTKPip+removeAllSources">.removeAllSources()</a></li>
<li><a href="#module_RTKPip+enable">.enable()</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKPip+disable"></a></p>
<h3 id="meeting-participants-pip-disable">meeting.participants.pip.disable</h3>
Disable PiP
<p><strong>Kind</strong>: instance property of <a href="#module_RTKPip"><code>RTKPip</code></a><br />
<a name="module_RTKPip+init"></a></p>
<h3 id="meeting-participants-pip-init-options">meeting.participants.pip.init([options])</h3>
Initialize PiP and prepare sources
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPip"><code>RTKPip</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>[options]</td>
<td><code>Object</code></td>
</tr>
<tr>
<td>[options.height]</td>
<td><code>number</code></td>
</tr>
<tr>
<td>[options.width]</td>
<td><code>number</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKPip+disableSource"></a></p>
<h3 id="meeting-participants-pip-disablesource-source">meeting.participants.pip.disableSource(source)</h3>
**Kind**: instance method of [<code>RTKPip</code>](#module_RTKPip)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>source</td>
<td><code>string</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKPip+addSource"></a></p>
<h3 id="meeting-participants-pip-addsource-id-element-enabled-displaytext">meeting.participants.pip.addSource(id, element, enabled, [displayText])</h3>
Add a video source from the participant grid
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPip"><code>RTKPip</code></a></p>
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
<td>id for the source (ex. participant id)</td>
</tr>
<tr>
<td>element</td>
<td><code>HTMLVideoElement</code></td>
<td>HTMLVideoElement for the video source</td>
</tr>
<tr>
<td>enabled</td>
<td><code>boolean</code></td>
<td>if source is enabled</td>
</tr>
<tr>
<td>[displayText]</td>
<td><code>string</code></td>
<td>two character display text</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKPip+updateSource"></a></p>
<h3 id="meeting-participants-pip-updatesource-id-source">meeting.participants.pip.updateSource(id, source)</h3>
Update a video source
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPip"><code>RTKPip</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>id</td>
<td><code>string</code></td>
</tr>
<tr>
<td>source</td>
<td><code>any</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKPip+removeSource"></a></p>
<h3 id="meeting-participants-pip-removesource-id">meeting.participants.pip.removeSource(id)</h3>
Remove the video source for the participant
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPip"><code>RTKPip</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>id</td>
<td>id for the source (ex. participant id)</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKPip+removePinnedSource"></a></p>
<h3 id="meeting-participants-pip-removepinnedsource-id">meeting.participants.pip.removePinnedSource(id)</h3>
Remove the pinned source
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPip"><code>RTKPip</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>id</td>
<td>id for the source (ex. participant id)</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKPip+removeAllSources"></a></p>
<h3 id="meeting-participants-pip-removeallsources">meeting.participants.pip.removeAllSources()</h3>
Remove all sources
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPip"><code>RTKPip</code></a><br />
<a name="module_RTKPip+enable"></a></p>
<h3 id="meeting-participants-pip-enable">meeting.participants.pip.enable()</h3>
Enable PiP
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPip"><code>RTKPip</code></a><br />
<a name="getInitials"></a></p>
<p>Code from ui-kit. Same method used in the avatar component</p>
<p><strong>Kind</strong>: global function</p>
