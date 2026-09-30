<p>RealtimeKit's interactive recording feature allows you to add timed metadata to your video stream. Timed metadata serves as cue points for clients to display information and trigger time-aligned actions. The metadata is available to clients in the form of <a href="https://en.wikipedia.org/wiki/ID3">ID3</a> tags on the playback timeline.</p>
<h2 id="what-is-interactive-recording">What is interactive recording?</h2>
<p>Ever wondered how Netflix displays small images on the seek bar or how additional content is shown while watching a cricket match on Hotstar? It's all metadata inserted at a specific time inside the video feed itself, which is called timed metadata.</p>
<p>Timed metadata is metadata with timestamps. It refers to digital markers added to a video file to provide additional context and information at specific points in the content range. These data points can be inserted into a stream programmatically, using the <code>interactive_config</code> in the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start recording a meeting API</a>.</p>
<p>Once RealtimeKit processes the stream, the timed metadata gets synchronized with the audio and video frames. This metadata is available to all viewers during playback at the same time relative to the stream. The timecode acts as a cue point and can trigger specific actions based on the data. For example:</p>
<p>These features are made possible through the use of ID3 tags that are embedded in the video segments, making them available in the recorded video.</p>
<h2 id="add-interactivity-to-your-realtimekit-recordings">Add interactivity to your RealtimeKit recordings</h2>
<p>To add interactivity to your RealtimeKit recording, perform the following steps:</p>
<ol>
<li>In the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start recording a meeting API</a>, pass the <code>interactive_config</code> parameter.</li>
</ol>
<p>This parameter enables you to add timed metadata to your recordings, which is made available to clients in HLS format via ID3 tags. The output files are packaged as a tar file.</p>
<ol start="2">
<li>In <a href="https://docs.realtime.cloudflare.com/web-core/reference/RealtimeKitClient">RealtimeKitClient</a>, call the <code>broadcastMessage</code> method with the parameters, <code>ID3</code> (as a string) and <code>yourData</code> (the data you want to send as timed metadata) on the <a href="https://docs.realtime.cloudflare.com/web-core/reference/RealtimeKitClient#module_RealtimeKitClient+participants">participants</a> object.</li>
</ol>
<pre><code class="language-ts">meeting.participants.broadcastMessage(“ID3Data”, yourData);&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11811.md")
</aside>
<ol start="3">
<li>To stop sending the data, call the following method. Once you make this call, you will no longer be able to send additional ID3 data.</li>
</ol>
<pre><code class="language-ts">meeting.participants.broadcastMessage(“ID3Data”,”CLOSE_TRANSPORT”)&#10;</code></pre>
<p>If you do not pass this parameter, the ID3 metadata stream will automatically be closed when the recording is stopped.</p>
<ol start="4">
<li>Once the recording is completed, you can retrieve the tar file that contains video segments and a playlist file. The <code>download_url</code> provides the link to the tar file. Below is an example screenshot of a tar file:</li>
</ol>
<p><img src="/assets/upstream/images/realtime/realtimekit/interactive-recording-tar-format.png" alt="Recording Tar Format" /></p>
<p>It's also important to note that the length of each segment depends on the frames of the video. Therefore, each segment may not have the same length, although it is typically close to the specified segment length when the recording was started. By default, the segment length is set to 10 seconds.</p>
<ol start="5">
<li>You can play the stream using the <a href="https://github.com/video-dev/hls.js/"><code>hls.js</code></a>.</li>
</ol>
<pre><code class="language-js">const onFragChanged = (_) =&gt; {&#10;  // We first try to find the right metadata track.&#10;  // https://developer.mozilla.org/en-US/docs/Web/API/TextTrack&#10;  const textTrackListCount = videoEl.textTracks.length;&#10;  let metaTextTrack;&#10;  for (let trackIndex = 0; trackIndex &lt; textTrackListCount; trackIndex++) {&#10;    const textTrack = videoEl.textTracks[trackIndex];&#10;    if (textTrack.kind !== &#x27;metadata&#x27;) {&#10;      continue;&#10;    }&#10;    textTrack.mode = &#x27;showing&#x27;;&#10;    metaTextTrack = textTrack;&#10;    break;&#10;  }&#10;  if (!metaTextTrack) {&#10;    return;&#10;  }&#10;  // Add an oncuechange listener on that track.&#10;  metaTextTrack.oncuechange = (event) =&gt; {&#10;    let cue = metaTextTrack.activeCues[metaTextTrack.activeCues.length - 1];&#10;    console.log(cue.value.data);&#10;  };&#10;};&#10;// listen on Hls.Events.FRAG_CHANGED from hls.js&#10;hls.on(Hls.Events.FRAG_CHANGED, onFragChanged);&#10;</code></pre>
<head>
  <title>Interactive Recordings with Timed Metadata Guide</title>
  <meta name="description" content="Learn how to enable interactive recording with RealtimeKit's capabilities. Follow our guide for effective configuration and management." />
</head>
