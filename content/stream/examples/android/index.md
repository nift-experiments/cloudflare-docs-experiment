<p class="article-summary">Example of video playback on Android using ExoPlayer</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14467.md")
</aside>
<pre><code class="language-kotlin">implementation &#x27;com.google.android.exoplayer:exoplayer-hls:2.X.X&#x27;&#10;&#10;SimpleExoPlayer player = new SimpleExoPlayer.Builder(context).build();&#10;&#10;// Set the media item to the Cloudflare Stream HLS Manifest URL:&#10;player.setMediaItem(MediaItem.fromUri(&quot;https://customer-9cbb9x7nxdw5hb57.cloudflarestream.com/8f92fe7d2c1c0983767649e065e691fc/manifest/video.m3u8&quot;));&#10;&#10;player.prepare();&#10;</code></pre>
<h3 id="download-and-run-an-example-app">Download and run an example app</h3>
<ol>
<li>Download <a href="https://github.com/googlecodelabs/exoplayer-intro.git">this example app</a> from the official Android developer docs, following <a href="https://developer.android.com/codelabs/exoplayer-intro#4">this guide</a>.</li>
<li>Open and run the <a href="https://github.com/googlecodelabs/exoplayer-intro/tree/main/exoplayer-codelab-04">exoplayer-codelab-04 example app</a> using <a href="https://developer.android.com/studio">Android Studio</a>.</li>
<li>Replace the <code>media_url_dash</code> URL on <a href="https://github.com/googlecodelabs/exoplayer-intro/blob/main/exoplayer-codelab-04/src/main/res/values/strings.xml#L21">this line</a> with the DASH manifest URL for your video.</li>
</ol>
<p>For more, see <a href="/stream/viewing-videos/using-own-player/ios/">read the docs</a>.</p>
