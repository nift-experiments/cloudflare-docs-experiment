<p>Attributes are added in the <code>&lt;stream&gt;</code> tag without quotes, as you can see below:</p>
<pre><code>&lt;stream attribute-added-here src=&quot;5d5bc37ffcf54c9b82e996823bffbb81&quot;&gt;&lt;/stream&gt;&#10;</code></pre>
<p>Multiple attributes can be used together, added one after each other like this:</p>
<pre><code>&lt;stream attribute-1 attribute-2 attribute-3 src=&quot;5d5bc37ffcf54c9b82e996823bffbb81&quot;&gt;&lt;/stream&gt;&#10;</code></pre>
<h2 id="supported-attributes">Supported attributes</h2>
<ul>
<li>
<p><code>autoplay</code> boolean</p>
<ul>
<li>Tells the browser to immediately start downloading the video and play it as soon as it can. Note that mobile browsers generally do not support this attribute, the user must tap the screen to begin video playback. Please consider mobile users or users with Internet usage limits as some users do not have unlimited Internet access before using this attribute.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14381.md")
</aside>
<ul>
<li>
<p><code>controls</code> boolean</p>
<ul>
<li>Shows the default video controls such as buttons for play/pause, volume controls. You may choose to build buttons and controls that work with the player. <a href="/stream/viewing-videos/using-own-player/">See an example.</a></li>
</ul>
</li>
<li>
<p><code>height</code> integer</p>
<ul>
<li>The height of the video's display area, in CSS pixels.</li>
</ul>
</li>
<li>
<p><code>loop</code> boolean</p>
<ul>
<li>A Boolean attribute; if included in the HTML tag, player will, automatically seek back to the start upon reaching the end of the video.</li>
</ul>
</li>
<li>
<p><code>muted</code> boolean</p>
<ul>
<li>A Boolean attribute which indicates the default setting of the audio contained in the video. If set, the audio will be initially silenced.</li>
</ul>
</li>
<li>
<p><code>preload</code> string | null</p>
<ul>
<li>This enumerated attribute is intended to provide a hint to the browser about what the author thinks will lead to the best user experience. You may choose to include this attribute as a boolean attribute without a value, or you may specify the value <code>preload=&quot;auto&quot;</code> to preload the beginning of the video. Not including the attribute or using <code>preload=&quot;metadata&quot;</code> will just load the metadata needed to start video playback when requested.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14380.md")
</aside>
<ul>
<li>
<p><code>poster</code> string</p>
<ul>
<li>A URL for an image to be shown before the video is started or while the video is downloading. If this attribute is not specified, a thumbnail image of the video is shown.</li>
</ul>
</li>
<li>
<p><code>src</code> string</p>
<ul>
<li>The video id from the video you've uploaded to Cloudflare Stream should be included here.</li>
</ul>
</li>
<li>
<p><code>width</code> integer</p>
<ul>
<li>The width of the video's display area, in CSS pixels.</li>
</ul>
</li>
</ul>
<h2 id="methods">Methods</h2>
<ul>
<li>
<p><code>play()</code> Promise</p>
<ul>
<li>Start video playback.</li>
</ul>
</li>
<li>
<p><code>pause()</code> null</p>
<ul>
<li>Pause video playback.</li>
</ul>
</li>
</ul>
<h2 id="properties">Properties</h2>
<ul>
<li>
<p><code>autoplay</code></p>
<ul>
<li>Sets or returns whether the autoplay attribute was set, allowing video playback to start upon load.</li>
</ul>
</li>
<li>
<p><code>controls</code></p>
<ul>
<li>Sets or returns whether the video should display controls (like play/pause etc.)</li>
</ul>
</li>
<li>
<p><code>currentTime</code></p>
<ul>
<li>Returns the current playback time in seconds. Setting this value seeks the video to a new time.</li>
</ul>
</li>
<li>
<p><code>duration</code> readonly</p>
<ul>
<li>Returns the duration of the video in seconds.</li>
</ul>
</li>
<li>
<p><code>ended</code> readonly</p>
<ul>
<li>Returns whether the video has ended.</li>
</ul>
</li>
<li>
<p><code>loop</code></p>
<ul>
<li>Sets or returns whether the video should start over when it reaches the end</li>
</ul>
</li>
<li>
<p><code>muted</code></p>
<ul>
<li>Sets or returns whether the audio should be played with the video</li>
</ul>
</li>
<li>
<p><code>paused</code> readonly</p>
<ul>
<li>Returns whether the video is paused</li>
</ul>
</li>
<li>
<p><code>preload</code></p>
<ul>
<li>Sets or returns whether the video should be preloaded upon element load.</li>
</ul>
</li>
<li>
<p><code>volume</code></p>
<ul>
<li>Sets or returns volume from 0.0 (silent) to 1.0 (maximum value)</li>
</ul>
</li>
</ul>
<h2 id="events">Events</h2>
<h3 id="standard-video-element-events">Standard video element events</h3>
<p>Stream supports most of the <a href="https://developer.mozilla.org/en-US/docs/Web/Guide/Events/Media_events">standardized media element events</a>.</p>
<ul>
<li>
<p><code>abort</code></p>
<ul>
<li>Sent when playback is aborted; for example, if the media is playing and is restarted from the beginning, this event is sent.</li>
</ul>
</li>
<li>
<p><code>canplay</code></p>
<ul>
<li>Sent when enough data is available that the media can be played, at least for a couple of frames.</li>
</ul>
</li>
<li>
<p><code>canplaythrough</code></p>
<ul>
<li>Sent when the entire media can be played without interruption, assuming the download rate remains at least at the current level. It will also be fired when playback is toggled between paused and playing. Note: Manually setting the currentTime will eventually fire a canplaythrough event in firefox. Other browsers might not fire this event.</li>
</ul>
</li>
<li>
<p><code>durationchange</code></p>
<ul>
<li>The metadata has loaded or changed, indicating a change in duration of the media. This is sent, for example, when the media has loaded enough that the duration is known.</li>
</ul>
</li>
<li>
<p><code>ended</code></p>
<ul>
<li>Sent when playback completes.</li>
</ul>
</li>
<li>
<p><code>error</code></p>
<ul>
<li>Sent when an error occurs. (for example, the video has not finished encoding yet, or the video fails to load due to an incorrect signed URL)</li>
</ul>
</li>
<li>
<p><code>loadeddata</code></p>
<ul>
<li>The first frame of the media has finished loading.</li>
</ul>
</li>
<li>
<p><code>loadedmetadata</code></p>
<ul>
<li>The media's metadata has finished loading; all attributes now contain as much useful information as they are going to.</li>
</ul>
</li>
<li>
<p><code>loadstart</code></p>
<ul>
<li>Sent when loading of the media begins.</li>
</ul>
</li>
<li>
<p><code>pause</code></p>
<ul>
<li>Sent when the playback state is changed to paused (paused property is true).</li>
</ul>
</li>
<li>
<p><code>play</code></p>
<ul>
<li>Sent when the playback state is no longer paused, as a result of the play method, or the autoplay attribute.</li>
</ul>
</li>
<li>
<p><code>playing</code></p>
<ul>
<li>Sent when the media has enough data to start playing, after the play event, but also when recovering from being stalled, when looping media restarts, and after seeked, if it was playing before seeking.</li>
</ul>
</li>
<li>
<p><code>progress</code></p>
<ul>
<li>Sent periodically to inform interested parties of progress downloading the media. Information about the current amount of the media that has been downloaded is available in the media element's buffered attribute.</li>
</ul>
</li>
<li>
<p><code>ratechange</code></p>
<ul>
<li>Sent when the playback speed changes.</li>
</ul>
</li>
<li>
<p><code>seeked</code></p>
<ul>
<li>Sent when a seek operation completes.</li>
</ul>
</li>
<li>
<p><code>seeking</code></p>
<ul>
<li>Sent when a seek operation begins.</li>
</ul>
</li>
<li>
<p><code>stalled</code></p>
<ul>
<li>Sent when the user agent is trying to fetch media data, but data is unexpectedly not forthcoming.</li>
</ul>
</li>
<li>
<p><code>suspend</code></p>
<ul>
<li>Sent when loading of the media is suspended; this may happen either because the download has completed or because it has been paused for any other reason.</li>
</ul>
</li>
<li>
<p><code>timeupdate</code></p>
<ul>
<li>The time indicated by the element's currentTime attribute has changed.</li>
</ul>
</li>
<li>
<p><code>volumechange</code></p>
<ul>
<li>Sent when the audio volume changes (both when the volume is set and when the muted attribute is changed).</li>
</ul>
</li>
<li>
<p><code>waiting</code></p>
<ul>
<li>Sent when the requested operation (such as playback) is delayed pending the completion of another operation (such as a seek).</li>
</ul>
</li>
</ul>
<h3 id="non-standard-events">Non-standard events</h3>
<p>Non-standard events are prefixed with <code>stream-</code> to distinguish them from standard events.</p>
<ul>
<li>
<p><code>stream-adstart</code></p>
<ul>
<li>Fires when <code>ad-url</code> attribute is present and the ad begins playback</li>
</ul>
</li>
<li>
<p><code>stream-adend</code></p>
<ul>
<li>Fires when <code>ad-url</code> attribute is present and the ad finishes playback</li>
</ul>
</li>
<li>
<p><code>stream-adtimeout</code></p>
<ul>
<li>Fires when <code>ad-url</code> attribute is present and the ad took too long to load.</li>
</ul>
</li>
</ul>
