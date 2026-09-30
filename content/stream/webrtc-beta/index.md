<aside class="nb-aside note">
<h3 class="nb-aside-title" id="stream-live-webrtc-is-going-ga">Stream Live WebRTC is going GA:</h3>
@markup("md", "content/.markup/bodies/278.md")
</aside>
<p>WebRTC allows ultra-low latency (sub-second) live streaming (using WHIP) and playback (using WHEP) to thousands of concurrent viewers. WebRTC is ideally suited for one-to-many broadcasts with a real-time experience, for example:</p>
<ul>
<li>When the outcome of a live event is time-sensitive: gaming, live sports, financial news</li>
<li>When viewers interact with the content: e-learning, live Q&amp;A, auctions</li>
</ul>
<p>WebRTC is also ideally suited to creator platforms or in-browser experiences because your users can go live <em>without</em> special broadcast applications or dedicated hardware encoders.</p>
<h2 id="step-1-create-a-live-input">Step 1: Create a live input</h2>
<p>Create a live input using one of the two options:</p>
<ul>
<li>Use the <strong>Live inputs</strong> page of the Cloudflare dashboard, then look under the Broadcast and Playback tabs to get the WebRTC URLs.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li>Make a POST request to the <a href="/api/resources/stream/subresources/live_inputs/methods/create/"><code>/live_inputs</code> API endpoint</a></li>
</ul>
<pre><code class="language-json">{&#10;  &quot;uid&quot;: &quot;1a553f11a88915d093d45eda660d2f8c&quot;,&#10; ...&#10;  &quot;webRTC&quot;: {&#10;    &quot;url&quot;: &quot;https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;SECRET&gt;/webRTC/publish&quot;&#10;  },&#10;  &quot;webRTCPlayback&quot;: {&#10;    &quot;url&quot;: &quot;https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;INPUT_UID&gt;/webRTC/play&quot;&#10;  },&#10;...&#10;}&#10;</code></pre>
<h2 id="step-2-go-live-using-whip">Step 2: Go live using WHIP</h2>
<h3 id="broadcasting-from-the-browser">Broadcasting from the browser</h3>
<p>Every live input has a unique URL that one creator can be stream to. <em>This is a credential</em> and should <em>only</em> be shared with the creator — anyone with this URL can stream live video to this input.</p>
<p>Retrieve the WHIP endpoint URL:</p>
<ul>
<li>The <strong>Live inputs</strong> page of the Cloudflare dashboard.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li>The <code>webRTC.url</code> property in the API response when the input is created.</li>
</ul>
<p>For a complete, no-dependency example of going live from a browser, see the <a href="/stream/examples/browser-based-webrtc/">First WebRTC broadcast in the browser</a> tutorial.</p>
<p>You can also use this URL with any client that supports the <a href="https://www.ietf.org/archive/id/draft-ietf-wish-whip-16.html">WebRTC-HTTP Ingestion Protocol (WHIP)</a>. See <a href="#supported-whip-and-whep-clients">supported WHIP clients</a> for a list of clients we have tested and confirmed compatibility with Cloudflare Stream.</p>
<h3 id="broadcasting-from-other-software-obs-ffmpeg">Broadcasting from other software (OBS, FFmpeg)</h3>
<p><strong>Using OBS 31.0 or higher:</strong> Recommended settings to broadcast WebRTC/WHIP. In Settings:</p>
<ul>
<li>In the <strong>Stream</strong> tab
<ul>
<li><strong>Service:</strong> WHIP</li>
<li><strong>Server:</strong> Paste the entire WebRTC (WHIP) URL from Cloudflare Stream
<ul>
<li>The broadcast secret is part of this URL, leave &quot;Bearer Token&quot; blank</li>
</ul>
</li>
</ul>
</li>
<li>In the <strong>Output</strong> tab
<ul>
<li><strong>Audio Encoder:</strong> FFmpeg Opus <em>(or another Opus encoder, if available)</em></li>
<li><strong>Video Encoder:</strong> x264 <em>(or a hardware accelerated H.264 encoder like QuickSync or NVENC)</em></li>
<li><strong>Rate Control:</strong> <code>CBR</code> or <code>VBR</code></li>
<li><strong>Bitrate:</strong> between 3000 Kbps and 7000 Kpbs</li>
<li><strong>Profile:</strong> <code>main</code> or <code>baseline</code></li>
<li><strong>B Frames:</strong> 0</li>
</ul>
</li>
<li>In the <strong>Video</strong> tab
<ul>
<li><strong>Framerate:</strong> field may be called &quot;Common FPS Values&quot; or &quot;Integer FPS Value&quot;, set to 30</li>
</ul>
</li>
</ul>
<p><strong>Using FFmpeg 8.1 or higher:</strong> This sample command outputs a clock and a constant tone. Revise the input criteria with your content.</p>
<pre><code class="language-bash">ffmpeg -hide_banner -y \&#10;  &#45;re -f lavfi -i testsrc=size=1920x1080:rate=30 \&#10;  &#45;re -f lavfi -i &quot;sine=frequency=200&quot; \&#10;  &#45;vf &quot;drawtext=fontsize=120:text=&#x27;%{gmtime}.%{eif\:1M*t-1K*trunc(t\*1K)\:d}&#x27;:x=0:y=0:fontcolor=WhiteSmoke:box=1:boxcolor=black@0.6&quot; \&#10;  &#45;c:v libx264 -flags +global_header -maxrate 4000k -bufsize 1500k \&#10;  &#45;tune zerolatency -g 30 -profile:v baseline -pix_fmt yuv420p \&#10;  &#45;acodec libopus -b:a 128k -ar 48000 -ac 2 \&#10;  &#45;ts_buffer_size 16777216 \&#10;  &#45;f whip https://customer-igynxd2rwhmuoxw8.cloudflarestream.com/71adb6d1676e2aa8d42ddce2271a2aedk5b6efd743b78487c095b2911e08345d8/webRTC/publish&#10;</code></pre>
<p>If using Windows/PowerShell:</p>
<ul>
<li>Add <code>:fontfile='C\:/Windows/Fonts/consola.ttf'</code> to the <code>vf</code> string; a font must be specified in Windows environments</li>
<li>Use backticks <code>\`` instead of backslashes </code>` to segment a multiline command</li>
</ul>
<p>FFmpeg's WHIP support currently requires the use of <code>libx264</code> at <code>baseline</code>. The <code>ts_buffer_size</code> is a memory allocation strategy, not a buffer that increases latency.</p>
<h2 id="step-3-play-live-video-using-whep">Step 3: Play live video using WHEP</h2>
<p><strong>Using the Stream Player:</strong> Stream's built-in player already supports playing WebRTC broadcasts by automatically upgrading to WHEP when available. Refer to &quot;<a href="/stream/viewing-videos/using-the-stream-player/">Use the Stream Player</a>&quot; for more information. The player embed code can be generated on the live input's settings page in the Dashboard.</p>
<p><strong>Using the WHEP endpoint in a custom player:</strong></p>
<p>Copy the URL from either:</p>
<ul>
<li>The <strong>Live inputs</strong> page of the Cloudflare dashboard.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li>The <code>webRTCPlayback.url</code> property in the API response when the input is created.</li>
</ul>
<p>While the creator is actively streaming, viewers can watch the broadcast in their browsers with less than 500 milliseconds of latency. There are no fixed limits on the number of concurrent viewers.</p>
<p>For a complete, no-dependency example of playing WebRTC in a browser, see the <a href="/stream/examples/browser-based-webrtc/">First WebRTC broadcast in the browser</a> tutorial.</p>
<p>This URL can also be used with any client that supports the <a href="https://www.ietf.org/archive/id/draft-murillo-whep-01.html">WebRTC-HTTP Egress Protocol (WHEP)</a>. See <a href="#supported-whip-and-whep-clients">supported WHEP clients</a> for a list of clients we have tested and confirmed compatibility with Cloudflare Stream.</p>
<h2 id="debugging-webrtc">Debugging WebRTC</h2>
<ul>
<li><strong>Chrome</strong>: Navigate to <code>chrome://webrtc-internals</code> to view detailed logs and graphs.</li>
<li><strong>Firefox</strong>: Navigate to <code>about:webrtc</code> to view information about WebRTC sessions, similar to Chrome.</li>
<li><strong>Safari</strong>: To enable WebRTC logs, from the inspector, open the settings tab (cogwheel icon), and set WebRTC logging to &quot;Verbose&quot; in the dropdown menu.</li>
</ul>
<h2 id="supported-whip-and-whep-clients">Supported WHIP and WHEP clients</h2>
<p>You can write your own broadcast and publishing apps using the browser's native WebRTC APIs — see the <a href="/stream/examples/browser-based-webrtc/">First WebRTC broadcast in the browser</a> tutorial. Beyond native code, we have tested and confirmed that the following clients are compatible with Cloudflare Stream:</p>
<h3 id="whip-for-broadcasting">WHIP for Broadcasting</h3>
<p>Dedicated applications:</p>
<ul>
<li><a href="https://obsproject.com">OBS (Open Broadcaster Software)</a> version 31.0 or higher (desktop streaming app)</li>
<li><a href="https://softvelum.com/larix/">Larix Broadcaster</a> (mobile app)</li>
<li><a href="https://www.ffmpeg.org/">FFmpeg</a> version 8.1 or higher (cross-platform command-line application)</li>
</ul>
<p>Development libraries:</p>
<ul>
<li><a href="https://www.npmjs.com/package/whip-whep">whip-whep</a> (JavaScript, the reference implementation from a WHIP specification author)</li>
<li><a href="https://www.npmjs.com/package/@eyevinn/whip-web-client">@eyevinn/whip-web-client</a> (TypeScript)</li>
</ul>
<h3 id="whep-for-playback">WHEP for Playback</h3>
<ul>
<li>Stream's built-in player</li>
<li><a href="https://www.npmjs.com/package/whip-whep">whip-whep</a> (JavaScript, the reference implementation from a WHEP specification author)</li>
<li><a href="https://www.npmjs.com/package/@eyevinn/webrtc-player">@eyevinn/webrtc-player</a> (TypeScript)</li>
<li><a href="https://www.npmjs.com/package/react-native-whip-whep">react-native-whip-whep</a> (React Native)</li>
</ul>
<h2 id="using-webrtc-in-native-apps">Using WebRTC in native apps</h2>
<p>If you are building a native app, the browser example from the <a href="/stream/examples/browser-based-webrtc/">First WebRTC broadcast in the browser</a> tutorial can run within a <a href="https://developer.apple.com/documentation/webkit/wkwebview">WkWebView (iOS)</a>, <a href="https://developer.android.com/reference/android/webkit/WebView">WebView (Android)</a> or using <a href="https://github.com/react-native-webrtc/react-native-webrtc/blob/master/Documentation/BasicUsage.md">react-native-webrtc</a>. If you need to use WebRTC without a webview, you can use Google's Java and Objective-C native <a href="https://webrtc.googlesource.com/src/+/refs/heads/main/sdk">implementations of WebRTC APIs</a>.</p>
<h2 id="supported-broadcast-codecs">Supported broadcast codecs</h2>
<ul>
<li><a href="https://developers.google.com/media/vp9">VP9</a></li>
<li><a href="https://en.wikipedia.org/wiki/VP8">VP8</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advanced_Video_Coding">h264</a> (Constrained Baseline Profile Level 3.1, referred to as <code>42e01f</code> in the SDP offer's <code>profile-level-id</code> parameter.)</li>
</ul>
<h2 id="conformance-with-whip-and-whep-specifications">Conformance with WHIP and WHEP specifications</h2>
<p>Cloudflare Stream supports the <a href="https://www.ietf.org/archive/id/draft-ietf-wish-whip-16.html">WHIP</a> and <a href="https://www.ietf.org/archive/id/draft-murillo-whep-01.html">WHEP</a> specifications, including:</p>
<ul>
<li><a href="https://datatracker.ietf.org/doc/rfc8838/">Trickle ICE</a></li>
<li><a href="https://www.ietf.org/archive/id/draft-murillo-whep-01.html#section-3">Server and client offer modes</a> for WHEP</li>
</ul>
<p>You can find the specific version of WHIP and WHEP being used in the <code>protocol-version</code> header in WHIP and WHEP API responses. The value of this header references the IETF draft slug for each protocol. Currently, Stream uses <code>draft-ietf-wish-whip-06</code> (expected to be the final WHIP draft revision) and <code>draft-murillo-whep-01</code> (the most current WHEP draft).</p>
<h2 id="limitations">Limitations</h2>
<p><strong>WHIP and WHEP must be used together:</strong> we do not yet support inputs using RTMP/SRT to be played using WHEP, or inputs using WHIP to be recorded and played played using HLS/DASH.</p>
<ul>
<li>Broadcast metrics and player experience metrics are not supported</li>
<li>Recording and live HLS playback are not yet supported</li>
<li>Simulcasting (restreaming via RTMP/SRT) is not supported</li>
<li>Live viewer counts are not supported</li>
</ul>
<h2 id="pricing">Pricing</h2>
<p>Stream Live WebRTC follows <a href="/stream/pricing">standard Stream pricing</a>: $1 per 1,000 minutes of video delivered. WebRTC is not currently eligible for recording, thus no storage is consumed.</p>
