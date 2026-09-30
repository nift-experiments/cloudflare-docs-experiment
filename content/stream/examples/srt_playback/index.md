<p class="article-summary">Example of sub 1s latency video playback using SRT and ffplay</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14464.md")
</aside>
<p>Copy the SRT Playback URL for your live input from either:</p>
<ul>
<li>The <strong>Live inputs</strong> page of the Cloudflare dashboard.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li>The <a href="/stream/stream-live/start-stream-live/#use-the-api">Stream API</a></li>
</ul>
<p>Paste it into the URL below, replacing <code>&lt;SRT_PLAYBACK_URL&gt;</code>:</p>
<pre><code class="language-sh">ffplay -analyzeduration 1 -fflags -nobuffer -probesize 32 -sync ext &#x27;&lt;SRT_PLAYBACK_URL&gt;&#x27;&#10;</code></pre>
<p>For more, refer to <a href="/stream/viewing-videos/using-own-player/#play-live-video-in-native-apps-with-less-than-1-second-latency">Play live video in native apps with less than one second latency</a>.</p>
