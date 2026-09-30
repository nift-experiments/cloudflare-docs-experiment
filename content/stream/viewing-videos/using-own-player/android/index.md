<p>You can stream both on-demand and live video to native Android apps using <a href="https://exoplayer.dev/">ExoPlayer</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14602.md")
</aside>
<h2 id="example-apps">Example Apps</h2>
<ul>
<li><a href="/stream/examples/android/">Android</a></li>
</ul>
<h2 id="using-exoplayer">Using ExoPlayer</h2>
<p>Play a video from Cloudflare Stream using ExoPlayer:</p>
<pre><code class="language-kotlin">implementation &#x27;com.google.android.exoplayer:exoplayer-hls:2.X.X&#x27;&#10;&#10;SimpleExoPlayer player = new SimpleExoPlayer.Builder(context).build();&#10;&#10;// Set the media item to the Cloudflare Stream HLS Manifest URL:&#10;player.setMediaItem(MediaItem.fromUri(&quot;https://customer-9cbb9x7nxdw5hb57.cloudflarestream.com/8f92fe7d2c1c0983767649e065e691fc/manifest/video.m3u8&quot;));&#10;&#10;player.prepare();&#10;</code></pre>
