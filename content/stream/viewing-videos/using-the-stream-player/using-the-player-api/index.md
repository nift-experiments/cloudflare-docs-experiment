<p>For further control and customization, we provide an additional JavaScript SDK that you can use to control video playback and listen for media events.</p>
<p>To use this SDK, add an additional <code>&lt;script&gt;</code> tag to your website:</p>
<pre><code class="language-html">&lt;!-- You can use styles and CSS on this iframe element where the video player will appear --&gt;&#10;&lt;iframe&#10;  src=&quot;https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;VIDEO_UID&gt;/iframe&quot;&#10;  style=&quot;border: none&quot;&#10;  height=&quot;720&quot;&#10;  width=&quot;1280&quot;&#10;  allow=&quot;accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;&quot;&#10;  allowfullscreen=&quot;true&quot;&#10;  id=&quot;stream-player&quot;&#10;&gt;&lt;/iframe&gt;&#10;&#10;&lt;script src=&quot;https://embed.cloudflarestream.com/embed/sdk.latest.js&quot;&gt;&lt;/script&gt;&#10;&#10;&lt;!-- Your JavaScript code below--&gt;&#10;&lt;script&gt;&#10;  const player = Stream(document.getElementById(&#x27;stream-player&#x27;));&#10;  player.addEventListener(&#x27;play&#x27;, () =&gt; {&#10;    console.log(&#x27;playing!&#x27;);&#10;  });&#10;  player.play().catch(() =&gt; {&#10;    console.log(&#x27;playback failed, muting to try again&#x27;);&#10;    player.muted = true;&#10;    player.play();&#10;  });&#10;&lt;/script&gt;&#10;</code></pre>
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
<p><code>autoplay</code> boolean</p>
<ul>
<li>Sets or returns whether the autoplay attribute was set, allowing video playback to start upon load.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14590.md")
</aside>
<ul>
<li>
<p><code>buffered</code> TimeRanges readonly</p>
<ul>
<li>An object conforming to the TimeRanges interface. This object is normalized, which means that ranges are ordered, don't overlap, aren't empty, and don't touch (adjacent ranges are folded into one bigger range).</li>
</ul>
</li>
<li>
<p><code>controls</code> boolean</p>
<ul>
<li>Sets or returns whether the video should display controls (like play/pause etc.)</li>
</ul>
</li>
<li>
<p><code>currentTime</code> integer</p>
<ul>
<li>Returns the current playback time in seconds. Setting this value seeks the video to a new time.</li>
</ul>
</li>
<li>
<p><code>defaultTextTrack</code></p>
<ul>
<li>Will initialize the player with the specified language code's text track enabled. The value should be the BCP-47 language code that was used to <a href="/stream/edit-videos/adding-captions/">upload the text track</a>. If the specified language code has no captions available, the player will behave as though no language code had been provided.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14589.md")
</aside>
<ul>
<li>
<p><code>duration</code> integer readonly</p>
<ul>
<li>Returns the duration of the video in seconds.</li>
</ul>
</li>
<li>
<p><code>ended</code> boolean readonly</p>
<ul>
<li>Returns whether the video has ended.</li>
</ul>
</li>
<li>
<p><code>letterboxColor</code> string</p>
<ul>
<li>Any valid <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value">CSS color value</a> provided will be applied to the letterboxing/pillarboxing of the player's UI. This can be set to <code>transparent</code> to avoid letterboxing/pillarboxing when not in fullscreen mode.</li>
</ul>
</li>
<li>
<p><code>loop</code> boolean</p>
<ul>
<li>Sets or returns whether the video should start over when it reaches the end</li>
</ul>
</li>
<li>
<p><code>muted</code> boolean</p>
<ul>
<li>Sets or returns whether the audio should be played with the video</li>
</ul>
</li>
<li>
<p><code>paused</code> boolean readonly</p>
<ul>
<li>Returns whether the video is paused</li>
</ul>
</li>
<li>
<p><code>played</code> TimeRanges readonly</p>
<ul>
<li>An object conforming to the TimeRanges interface. This object is normalized, which means that ranges are ordered, don't overlap, aren't empty, and don't touch (adjacent ranges are folded into one bigger range).</li>
</ul>
</li>
<li>
<p><code>preload</code> boolean</p>
<ul>
<li>Sets or returns whether the video should be preloaded upon element load.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14588.md")
</aside>
<ul>
<li>
<p><code>primaryColor</code> string</p>
<ul>
<li>Any valid <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value">CSS color value</a> provided will be applied to certain elements of the player's UI.</li>
</ul>
</li>
<li>
<p><code>volume</code> float</p>
<ul>
<li>Sets or returns volume from 0.0 (silent) to 1.0 (maximum value)</li>
</ul>
</li>
</ul>
<h2 id="events">Events</h2>
<h3 id="standard-video-element-events">Standard Video Element Events</h3>
<p>We support most of the <a href="https://developer.mozilla.org/en-US/docs/Web/Guide/Events/Media_events">standardized media element events</a>.</p>
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
<li>Sent when an error occurs. (e.g. the video has not finished encoding yet, or the video fails to load due to an incorrect signed URL)</li>
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
<li>The media's metadata has finished loading; all attributes now contain as much useful information as they're going to.</li>
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
<h3 id="non-standard-events">Non-standard Events</h3>
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
