<p>You can stream both on-demand and live video to native iOS, tvOS and macOS apps using <a href="https://developer.apple.com/documentation/avfoundation/avplayer">AVPlayer</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14599.md")
</aside>
<h2 id="example-apps">Example Apps</h2>
<ul>
<li><a href="/stream/examples/ios/">iOS</a></li>
</ul>
<h2 id="using-avplayer">Using AVPlayer</h2>
<p>Play a video from Cloudflare Stream using AVPlayer:</p>
<pre><code class="language-swift">import SwiftUI&#10;import AVKit&#10;&#10;struct MyView: View {&#10;    // Change the url to the Cloudflare Stream HLS manifest URL&#10;    private let player = AVPlayer(url: URL(string: &quot;https://customer-9cbb9x7nxdw5hb57.cloudflarestream.com/8f92fe7d2c1c0983767649e065e691fc/manifest/video.m3u8&quot;)!)&#10;&#10;    var body: some View {&#10;        VideoPlayer(player: player)&#10;            .onAppear() {&#10;                player.play()&#10;            }&#10;    }&#10;}&#10;&#10;struct MyView_Previews: PreviewProvider {&#10;    static var previews: some View {&#10;        MyView()&#10;    }&#10;}&#10;</code></pre>
