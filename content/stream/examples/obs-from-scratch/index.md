---
cp9:
  canonical: https://developers.cloudflare.com/stream/examples/obs-from-scratch/
  description: Set up and start your first Live Stream using OBS (Open Broadcaster Software) Studio
  full_title: First Live Stream with OBS · Cloudflare Stream docs
  head_html: <title>First Live Stream with OBS · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up and start your first Live Stream using OBS (Open Broadcaster Software) Studio"><link rel="canonical" href="https://developers.cloudflare.com/stream/examples/obs-from-scratch/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/examples/obs-from-scratch/index.md"><meta property="og:title" content="First Live Stream with OBS · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up and start your first Live Stream using OBS (Open Broadcaster Software) Studio"><meta property="og:url" content="https://developers.cloudflare.com/stream/examples/obs-from-scratch/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/examples/obs-from-scratch/#page","headline":"First Live Stream with OBS \u00b7 Cloudflare Stream docs","description":"Set up and start your first Live Stream using OBS (Open Broadcaster Software) Studio","url":"https://developers.cloudflare.com/stream/examples/obs-from-scratch/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/examples/obs-from-scratch/
  schema: 1
---
<p class="article-summary">Set up and start your first Live Stream using OBS (Open Broadcaster Software) Studio</p>
<h2 id="overview">Overview</h2>
<p>Stream empowers customers and their end-users to broadcast a live stream quickly and at scale. The player can be embedded in sites and applications easily, but not everyone knows how to make a live stream because it happens in a separate application. This walkthrough will demonstrate how to start your first live stream using OBS Studio, a free live streaming application used by thousands of Stream customers. There are five required steps; you should be able to complete this walkthrough in less than 15 minutes.</p>
<h3 id="before-you-start">Before you start</h3>
<p>To go live on Stream, you will need any of the following:</p>
<ul>
<li>A paid Stream subscription</li>
<li>A Pro or Business zone plan — these include 100 minutes of video storage and 10,000 minutes of video delivery</li>
<li>An enterprise contract with Stream enabled</li>
</ul>
<p>Also, you will also need to be able to install the application on your computer.</p>
<p>If your computer and network connection are good enough for video calling, you should at least be able to stream something basic.</p>
<h2 id="1-set-up-a-live-input-stream-stream-live-start-stream-live"><ol>
<li>Set up a <a href="/stream/stream-live/start-stream-live/">Live Input</a></li>
</ol></h2>
<p>You need a Live Input on Stream. Follow the <a href="/stream/stream-live/start-stream-live/">Start a live stream</a> guide. Make note of three things:</p>
<ul>
<li><strong>RTMPS URL</strong>, which will most likely be <code>rtmps://live.cloudflare.com:443/live/</code></li>
<li><strong>RTMPS Key</strong>, which is specific to the new live input</li>
<li>Whether you selected the beta &quot;Low-Latency HLS Support&quot; or not. For your first test, leave this <em>disabled.</em> (<a href="https://blog.cloudflare.com/cloudflare-stream-low-latency-hls-open-beta">What is that?</a>)</li>
</ul>
<h2 id="2-install-obs"><ol start="2">
<li>Install OBS</li>
</ol></h2>
<p>Download <a href="https://obsproject.com/">OBS Studio</a> for Windows, macOS, or Linux. The OBS Knowledge Base includes several <a href="https://obsproject.com/kb/category/1">installation guides</a>, but installer defaults are generally acceptable.</p>
<h2 id="3-first-launch-obs-configuration"><ol start="3">
<li>First Launch OBS Configuration</li>
</ol></h2>
<p>When you first launch OBS, the Auto-Configuration Wizard will ask a few questions and offer recommended settings. See their <a href="https://obsproject.com/kb/quick-start-guide">Quick Start Guide</a> for more details. For a quick start with Stream, use these settings:</p>
<ul>
<li><strong>Step 1: &quot;Usage Information&quot;</strong>
<ul>
<li>Select &quot;Optimize for streaming, recording is secondary.&quot;</li>
</ul>
</li>
<li><strong>Step 2: &quot;Video Settings&quot;</strong>
<ul>
<li><strong>Base (Canvas) Resolution:</strong> 1920x1080</li>
<li><strong>FPS:</strong> &quot;Either 60 or 30, but prefer 60 when possible&quot;</li>
</ul>
</li>
<li><strong>Step 3: &quot;Stream Information&quot;</strong>
<ul>
<li><strong>Service:</strong> &quot;Custom&quot;</li>
<li>For <strong>Server</strong>, enter the RTMPS URL from Stream</li>
<li>For <strong>Stream Key</strong>, enter the RTMPS Key from Stream</li>
<li>If available, select both <strong>&quot;Prefer hardware encoding&quot;</strong> and <strong>&quot;Estimate bitrate with a bandwidth test.&quot;</strong></li>
</ul>
</li>
</ul>
<h2 id="4-set-up-a-stage"><ol start="4">
<li>Set up a Stage</li>
</ol></h2>
<p>Add some test content to the stage in OBS. In this example, I have added a background image, a web browser (to show <a href="https://time.is">time.is</a>), and an overlay of my webcam:</p>
<p><img src="/assets/upstream/images/stream/examples/obs-from-scratch/obs-stage.png" alt="OBS Stage" /></p>
<p>OBS offers many different audio, video, still, and generated sources to set up your broadcast content. Use the &quot;+&quot; button in the &quot;Sources&quot; panel to add content. Check out the <a href="https://obsproject.com/kb/sources-guide">OBS Sources Guide</a> for more information. For an initial test, use a source that will show some motion: try a webcam (&quot;Video Capture Device&quot;), a screen share (&quot;Display Capture&quot;), or a browser with a site that has moving content.</p>
<h2 id="5-go-live"><ol start="5">
<li>Go Live</li>
</ol></h2>
<p>Click the &quot;Start Streaming&quot; button on the bottom right panel under &quot;Controls&quot; to start a stream with default settings.</p>
<p>Return to the Live Input page on Stream Dash. Under &quot;Input Status,&quot; you should see &quot;🟢 Connected&quot; and some connection metrics. Further down the page, you will see a test player and an embed code. For more ways to watch and embed your Live Stream, see <a href="/stream/stream-live/watch-live-stream/">Watch a live stream</a>.</p>
<h2 id="6-optional-optimize-settings"><ol start="6">
<li>(Optional) Optimize Settings</li>
</ol></h2>
<p>Tweaking some settings in OBS can improve quality, glass-to-glass latency, or stability of the stream playback. This is particularly important if you selected the &quot;Low-Latency HLS&quot; beta option.</p>
<p>Return to OBS, click &quot;Stop Streaming.&quot; Then click &quot;Settings&quot; and open the &quot;Output&quot; section:</p>
<p><img src="/assets/upstream/images/stream/examples/obs-from-scratch/obs-output-settings-1.png" alt="OBS Output Settings - Simple Mode" /></p>
<ul>
<li>Change <strong>Output Mode</strong> to &quot;Advanced&quot;</li>
</ul>
<p><img src="/assets/upstream/images/stream/examples/obs-from-scratch/obs-output-settings-2.png" alt="OBS Output Settings - Advanced Mode" /></p>
<p><em>Your available options in the &quot;Video Encoder&quot; menu, as well as the resulting &quot;Encoder Settings,&quot; may look slightly different than these because the options vary by hardware.</em></p>
<ul>
<li><strong>Video Encoder:</strong> may have several options. Start with the default selected, which was &quot;x264&quot; in this example. Other options to try, which will leverage improved hardware acceleration when possible, include &quot;QuickSync H.264&quot; or &quot;NVIDIA NVENC.&quot; See OBS's guide to Hardware Encoding for more information. H.264 is the required output codec.</li>
<li><strong>Rate Control:</strong> confirm &quot;CBR&quot; (constant bitrate) is selected.</li>
<li><strong>Bitrate:</strong> depending on the content of your stream, a bitrate between 3000 Kbps and 8000 Kbps should be sufficient. Lower bitrate is more tolerant to network congestion and is suitable for content with less detail or less motion (speaker, slides, etc.) where a higher bitrate requires a more stable network connection and is best for content with lots of motion or details (events, moving cameras, video games, screen share, higher framerates).</li>
<li><strong>Keyframe Interval</strong>, sometimes referred to as <em>GOP Size</em>:
<ul>
<li>If you did <em>not</em> select Low-Latency HLS Beta, set this to 4 seconds. Raise it to 8 if your stream has stuttering or freezing.</li>
<li>If you <em>did</em> select the Low-Latency HLS Beta, set this to 2 seconds. Raise it to 4 if your stream has stuttering or freezing. Lower it to 1 if your stream has smooth playback.</li>
<li>In general, higher keyframe intervals make more efficient use of bandwidth and CPU for encoding, at the expense of higher glass-to-glass latency. Lower keyframe intervals reduce latency, but are more resource intensive and less tolerant to network disruptions and congestion.</li>
</ul>
</li>
<li><strong>Profile</strong> and <strong>Tuning</strong> can be left at their default settings.</li>
<li><strong>B Frames</strong> (available only for some encoders) should be set to 0 for LL-HLS Beta streams.</li>
</ul>
<p>Learn more about optimizing your live stream with <a href="/stream/stream-live/start-stream-live/#recommendations-requirements-and-limitations">live stream recommendations</a> and <a href="/stream/stream-live/troubleshooting/">live stream troubleshooting</a>.</p>
<h2 id="what-is-next">What is Next</h2>
<p>With these steps, you have created a Live Input on Stream, broadcast a test from OBS, and you saw it played back in via the Stream built-in player in Dash. Up next, consider trying:</p>
<ul>
<li>Embedding your live stream into a website</li>
<li>Find and replay the recording of your live stream</li>
</ul>
