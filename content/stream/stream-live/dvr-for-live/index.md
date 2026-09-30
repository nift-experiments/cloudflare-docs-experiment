<p>Stream Live supports &quot;DVR mode&quot; on an opt-in basis to allow viewers to rewind,
resume, and fast-forward a live broadcast. To enable DVR mode, add the
<code>dvrEnabled=true</code> query parameter to the Stream Player embed source or the HLS
manifest URL.</p>
<h2 id="stream-player">Stream Player</h2>
<pre><code class="language-html">&lt;div style=&quot;position: relative; padding-top: 56.25%;&quot;&gt;&#10;  &lt;iframe&#10;    src=&quot;https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;INPUT_ID|VIDEO_ID&gt;/iframe?dvrEnabled=true&quot;&#10;    style=&quot;border: none; position: absolute; top: 0; left: 0; height: 100%; width: 100%;&quot;&#10;    allow=&quot;accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;&quot;&#10;    allowfullscreen=&quot;true&quot;&#10;  &gt;&lt;/iframe&gt;&#10;&lt;/div&gt;&#10;</code></pre>
<p>When DVR mode is enabled the Stream Player will:</p>
<ul>
<li>Show a timeline the viewer can scrub/seek, similar to watching an on-demand
video. The timeline will automatically scale to show the growing duration of
the broadcast while it is live.</li>
<li>The &quot;LIVE&quot; indicator will show grey if the viewer is behind the live edge or
red if they are watching the latest content. Clicking that indicator will jump
forward to the live edge.</li>
<li>If the viewer pauses the player, it will resume playback from that time instead
of jumping forward to the live edge.</li>
</ul>
<h2 id="hls-manifest-for-custom-players">HLS manifest for custom players</h2>
<pre><code class="language-text">https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;INPUT_ID|VIDEO_ID&gt;/manifest/video.m3u8?dvrEnabled=true&#10;</code></pre>
<p>Custom players using a DVR-capable HLS manifest may need additional
configuration to surface helpful controls or information. Refer to your player
library for additional information.</p>
<h2 id="video-id-or-input-id">Video ID or Input ID</h2>
<p>Stream Live allows loading the Player or HLS manifest by Video ID or Live Input
ID. Refer to <a href="/stream/stream-live/watch-live-stream/">Watch a live stream</a> for how to
retrieve these URLs and compare these options. There are additional
considerations when using DVR mode:</p>
<p><strong>Recommended:</strong> Use DVR Mode on a Video ID URL:</p>
<ul>
<li>When the player loads, it will start playing the active broadcast if it is
still live or play the recording if the broadcast has concluded.</li>
</ul>
<p>DVR Mode on a Live Input ID URL:</p>
<ul>
<li>When the player loads, it will start playing the currently live broadcast if
there is one (refer to <a href="/stream/stream-live/watch-live-stream/#live-input-status">Live Input Status</a>).</li>
<li>If the viewer is still watching <em>after the broadcast ends,</em> they can continue
to watch. However, if the player or manifest is then reloaded, it will show the
latest broadcast or &quot;Stream has not yet started&quot; (<code>HTTP 204</code>). Past broadcasts
are not available by Live Input ID.</li>
</ul>
<h2 id="known-limitations">Known Limitations</h2>
<ul>
<li>When using DVR Mode and a player/manifest created using a Live Input ID, the
player may stall when trying to switch quality levels if a viewer is still
watching after a broadcast has concluded.</li>
<li>Performance may be degraded for DVR-enabled broadcasts longer than three hours.
Manifests are limited to a maximum of 7,200 segments. Segment length is
determined by the keyframe interval, also called GOP size.</li>
<li>DVR Mode relies on Version 8 of the HLS manifest specification. Stream uses
HLS Version 6 in all other contexts. HLS v8 offers extremely broad compatibility
but may not work with certain old player libraries or older devices.</li>
<li>DVR Mode is not available for DASH manifests.</li>
</ul>
