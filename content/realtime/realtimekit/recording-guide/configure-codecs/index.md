<p>Video codecs are software programs that compress and decompress digital video data for transmission, storage, or playback. Configuring the appropriate video codec can help reduce file size, enhance video quality, and ensure compatibility with different playback devices.</p>
<h2 id="configure-codecs">Configure Codecs</h2>
<p>You can modify the codec which is used for recording the videos. We currently
support the following codecs:</p>
<ul>
<li><strong>H264 (default)</strong>: Records video using the H.264 codec with 1280px × 720px
resolution, and 384 kbps AAC audio in MP4 container.</li>
<li><strong>VP8</strong>: Records video using the VP8 codec with 1280px × 720px
resolution, and Vorbis codec audio in WebM container.</li>
</ul>
<p>You can change the codec by specifying the codec in the <code>video_config</code> field in
the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a>, for
example:</p>
<pre><code class="language-json">{&#10;  &quot;video_config&quot;: {&#10;    &quot;codec&quot;: &quot;H264&quot;&#10;  }&#10;}&#10;</code></pre>
<h2 id="download-video-files">Download Video Files</h2>
<p>The video file for your recording is generated only if you passed the <code>video_config</code> parameters in the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a>.</p>
<p>When the recording is completed, you can use the <code>downloadUrl</code> provided in the response body of the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a> to download and export the video file.</p>
