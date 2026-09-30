<!-- Auto Generated Below -->
<p><a name="module_RTKSelfMedia"></a></p>
<p>The RTKSelfMedia class provides methods to manage the local participant's media.</p>
<ul>
<li><a href="#module_RTKSelfMedia">RTKSelfMedia</a>
<ul>
<li><a href="#module_RTKSelfMedia+audioTrack">.audioTrack</a></li>
<li><a href="#module_RTKSelfMedia+rawAudioTrack">.rawAudioTrack</a></li>
<li><a href="#module_RTKSelfMedia+mediaPermissions">.mediaPermissions</a></li>
<li><a href="#module_RTKSelfMedia+videoTrack">.videoTrack</a></li>
<li><a href="#module_RTKSelfMedia+rawVideoTrack">.rawVideoTrack</a></li>
<li><a href="#module_RTKSelfMedia+screenShareTracks">.screenShareTracks</a></li>
<li><a href="#module_RTKSelfMedia+audioEnabled">.audioEnabled</a></li>
<li><a href="#module_RTKSelfMedia+videoEnabled">.videoEnabled</a></li>
<li><a href="#module_RTKSelfMedia+screenShareEnabled">.screenShareEnabled</a></li>
<li><a href="#module_RTKSelfMedia+addAudioMiddleware">.addAudioMiddleware(audioMiddleware)</a></li>
<li><a href="#module_RTKSelfMedia+removeAudioMiddleware">.removeAudioMiddleware(audioMiddleware)</a></li>
<li><a href="#module_RTKSelfMedia+removeAllAudioMiddlewares">.removeAllAudioMiddlewares()</a></li>
<li><a href="#module_RTKSelfMedia+addVideoMiddleware">.addVideoMiddleware(videoMiddleware)</a></li>
<li><a href="#module_RTKSelfMedia+setVideoMiddlewareGlobalConfig">.setVideoMiddlewareGlobalConfig(config)</a></li>
<li><a href="#module_RTKSelfMedia+removeVideoMiddleware">.removeVideoMiddleware(videoMiddleware)</a></li>
<li><a href="#module_RTKSelfMedia+removeAllVideoMiddlewares">.removeAllVideoMiddlewares()</a></li>
<li><a href="#module_RTKSelfMedia+getCurrentDevices">.getCurrentDevices()</a></li>
<li><a href="#module_RTKSelfMedia+getAudioDevices">.getAudioDevices()</a></li>
<li><a href="#module_RTKSelfMedia+getVideoDevices">.getVideoDevices()</a></li>
<li><a href="#module_RTKSelfMedia+getSpeakerDevices">.getSpeakerDevices()</a></li>
<li><a href="#module_RTKSelfMedia+getDeviceById">.getDeviceById(deviceId, kind)</a></li>
<li><a href="#module_RTKSelfMedia+setDevice">.setDevice(device)</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKSelfMedia+audioTrack"></a></p>
<h3 id="meeting-self-audiotrack">meeting.self.audioTrack</h3>
Returns the `audioTrack`.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+rawAudioTrack"></a></p>
<h3 id="meeting-self-rawaudiotrack">meeting.self.rawAudioTrack</h3>
Returns the `rawAudioTrack` having no middleware executed on it.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+mediaPermissions"></a></p>
<h3 id="meeting-self-mediapermissions">meeting.self.mediaPermissions</h3>
Returns the current audio and video permissions given by the user.
'ACCEPTED' if the user has given permission to use the media.
'CANCELED' if the user has canceled the screenshare.
'DENIED' if the user has denied permission to use the media.
'SYS_DENIED' if the user's system has denied permission to use the media.
'UNAVAILABLE' if the media is not available (or being used by a different application).
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+videoTrack"></a></p>
<h3 id="meeting-self-videotrack">meeting.self.videoTrack</h3>
Returns the `videoTrack`.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+rawVideoTrack"></a></p>
<h3 id="meeting-self-rawvideotrack">meeting.self.rawVideoTrack</h3>
Returns the `videoTrack` having no middleware executed on it.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+screenShareTracks"></a></p>
<h3 id="meeting-self-screensharetracks">meeting.self.screenShareTracks</h3>
Returns the screen share tracks.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+audioEnabled"></a></p>
<h3 id="meeting-self-audioenabled">meeting.self.audioEnabled</h3>
Returns true if audio is enabled.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+videoEnabled"></a></p>
<h3 id="meeting-self-videoenabled">meeting.self.videoEnabled</h3>
Returns true if video is enabled.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+screenShareEnabled"></a></p>
<h3 id="meeting-self-screenshareenabled">meeting.self.screenShareEnabled</h3>
Returns true if screen share is enabled.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+addAudioMiddleware"></a></p>
<h3 id="meeting-self-addaudiomiddleware-audiomiddleware">meeting.self.addAudioMiddleware(audioMiddleware)</h3>
Adds the audio middleware to be executed on the raw audio stream.
If there are more than 1 audio middlewares,
they will be executed in the sequence they were added in.
If you want the sequence to be altered, please remove all previous middlewares and re-add.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>audioMiddleware</td>
<td><code>AudioMiddleware</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKSelfMedia+removeAudioMiddleware"></a></p>
<h3 id="meeting-self-removeaudiomiddleware-audiomiddleware">meeting.self.removeAudioMiddleware(audioMiddleware)</h3>
Removes the audio middleware, if it is there.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>audioMiddleware</td>
<td><code>AudioMiddleware</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKSelfMedia+removeAllAudioMiddlewares"></a></p>
<h3 id="meeting-self-removeallaudiomiddlewares">meeting.self.removeAllAudioMiddlewares()</h3>
Removes all audio middlewares, if they are there.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+addVideoMiddleware"></a></p>
<h3 id="meeting-self-addvideomiddleware-videomiddleware">meeting.self.addVideoMiddleware(videoMiddleware)</h3>
Adds the video middleware to be executed on the raw video stream.
If there are more than 1 video middlewares,
they will be executed in the sequence they were added in.
If you want the sequence to be altered, please remove all previous middlewares and re-add.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>videoMiddleware</td>
<td><code>VideoMiddleware</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKSelfMedia+setVideoMiddlewareGlobalConfig"></a></p>
<h3 id="meeting-self-setvideomiddlewareglobalconfig-config">meeting.self.setVideoMiddlewareGlobalConfig(config)</h3>
Sets global config to be used by video middlewares.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a></p>
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
<td>config</td>
<td><code>VideoMiddlewareGlobalConfig</code></td>
<td>config</td>
</tr>
<tr>
<td>config.disablePerFrameCanvasRendering</td>
<td><code>boolean</code></td>
<td>If set to true, Instead of calling Middleware for every frame, Middleware will only be called once that too with empty canvas,  it is the responsibility of the middleware author to keep updating this canvas. <code>meeting.self.rawVideoTrack</code> can be used to retrieve video track for the periodic updates.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKSelfMedia+removeVideoMiddleware"></a></p>
<h3 id="meeting-self-removevideomiddleware-videomiddleware">meeting.self.removeVideoMiddleware(videoMiddleware)</h3>
Removes the video middleware, if it is there.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>videoMiddleware</td>
<td><code>VideoMiddleware</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKSelfMedia+removeAllVideoMiddlewares"></a></p>
<h3 id="meeting-self-removeallvideomiddlewares">meeting.self.removeAllVideoMiddlewares()</h3>
Removes all video middlewares, if they are there.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+getCurrentDevices"></a></p>
<h3 id="meeting-self-getcurrentdevices">meeting.self.getCurrentDevices()</h3>
Returns the media devices currently being used.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+getAudioDevices"></a></p>
<h3 id="meeting-self-getaudiodevices">meeting.self.getAudioDevices()</h3>
Returns the local participant's audio devices.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+getVideoDevices"></a></p>
<h3 id="meeting-self-getvideodevices">meeting.self.getVideoDevices()</h3>
Returns the local participant's video devices.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+getSpeakerDevices"></a></p>
<h3 id="meeting-self-getspeakerdevices">meeting.self.getSpeakerDevices()</h3>
Returns the local participant's speaker devices.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a><br />
<a name="module_RTKSelfMedia+getDeviceById"></a></p>
<h3 id="meeting-self-getdevicebyid-deviceid-kind">meeting.self.getDeviceById(deviceId, kind)</h3>
Returns the local participant's device, indexed by ID and kind.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a></p>
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
<td>deviceId</td>
<td><code>string</code></td>
<td>The ID of the device.</td>
</tr>
<tr>
<td>kind</td>
<td><code>'audio'</code> | <code>'video'</code> | <code>'speaker'</code></td>
<td>The kind of the device: audio, video, or speaker.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKSelfMedia+setDevice"></a></p>
<h3 id="meeting-self-setdevice-device">meeting.self.setDevice(device)</h3>
Change the current media device that is being used by the local participant.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKSelfMedia"><code>RTKSelfMedia</code></a></p>
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
