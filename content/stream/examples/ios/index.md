<p class="article-summary">Example of video playback on iOS using AVPlayer</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14466.md")
</aside>
<pre><code class="language-swift">import SwiftUI&#10;import AVKit&#10;&#10;struct MyView: View {&#10;    // Change the url to the Cloudflare Stream HLS manifest URL&#10;    private let player = AVPlayer(url: URL(string: &quot;https://customer-9cbb9x7nxdw5hb57.cloudflarestream.com/8f92fe7d2c1c0983767649e065e691fc/manifest/video.m3u8&quot;)!)&#10;&#10;    var body: some View {&#10;        VideoPlayer(player: player)&#10;            .onAppear() {&#10;                player.play()&#10;            }&#10;    }&#10;}&#10;&#10;struct MyView_Previews: PreviewProvider {&#10;    static var previews: some View {&#10;        MyView()&#10;    }&#10;}&#10;</code></pre>
<h3 id="download-and-run-an-example-app">Download and run an example app</h3>
<ol>
<li>Download <a href="https://developer.apple.com/documentation/avfoundation/offline_playback_and_storage/using_avfoundation_to_play_and_persist_http_live_streams">this example app</a> from Apple's developer docs</li>
<li>Open and run the app using <a href="https://developer.apple.com/xcode/">Xcode</a>.</li>
<li>Search in Xcode for <code>m3u8</code>, and open the <code>Streams</code> file</li>
<li>Replace the value of <code>playlist_url</code> with the HLS manifest URL for your video.</li>
</ol>
<p><img src="/assets/upstream/images/stream/ios-example-screenshot-edit-hls-url.png" alt="Screenshot of a video with Cloudflare watermark at top right" /></p>
<ol start="5">
<li>Click the Play button in Xcode to run the app, and play your video.</li>
</ol>
<p>For more, see <a href="/stream/viewing-videos/using-own-player/ios/">read the docs</a>.</p>
