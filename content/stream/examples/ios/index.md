---
cp9:
  canonical: https://developers.cloudflare.com/stream/examples/ios/
  description: Example of video playback on iOS using AVPlayer
  full_title: iOS (AVPlayer) · Cloudflare Stream docs
  head_html: <title>iOS (AVPlayer) · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Example of video playback on iOS using AVPlayer"><link rel="canonical" href="https://developers.cloudflare.com/stream/examples/ios/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/examples/ios/index.md"><meta property="og:title" content="iOS (AVPlayer) · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Example of video playback on iOS using AVPlayer"><meta property="og:url" content="https://developers.cloudflare.com/stream/examples/ios/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Stream"><meta name="pcx_tags" content="Playback"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/examples/ios/#page","headline":"iOS (AVPlayer) \u00b7 Cloudflare Stream docs","description":"Example of video playback on iOS using AVPlayer","url":"https://developers.cloudflare.com/stream/examples/ios/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Playback"]}</script>
  markdown: true
  noindex: false
  route: /stream/examples/ios/
  schema: 1
---
<p class="article-summary">Example of video playback on iOS using AVPlayer</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14466.md")
</aside>
<pre tabindex="0"><code class="language-swift">import SwiftUI&#10;import AVKit&#10;&#10;struct MyView: View {&#10;    // Change the url to the Cloudflare Stream HLS manifest URL&#10;    private let player = AVPlayer(url: URL(string: &quot;https://customer-9cbb9x7nxdw5hb57.cloudflarestream.com/8f92fe7d2c1c0983767649e065e691fc/manifest/video.m3u8&quot;)!)&#10;&#10;    var body: some View {&#10;        VideoPlayer(player: player)&#10;            .onAppear() {&#10;                player.play()&#10;            }&#10;    }&#10;}&#10;&#10;struct MyView_Previews: PreviewProvider {&#10;    static var previews: some View {&#10;        MyView()&#10;    }&#10;}&#10;</code></pre>
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
