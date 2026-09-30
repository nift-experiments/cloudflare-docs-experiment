---
cp9:
  canonical: https://developers.cloudflare.com/stream/examples/browser-based-webrtc/
  description: Broadcast your webcam to Cloudflare Stream with WHIP and play it back with WHEP, using native browser WebRTC and no third-party libraries.
  full_title: First WebRTC broadcast in the browser · Cloudflare Stream docs
  head_html: <title>First WebRTC broadcast in the browser · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Broadcast your webcam to Cloudflare Stream with WHIP and play it back with WHEP, using native browser WebRTC and no third-party libraries."><link rel="canonical" href="https://developers.cloudflare.com/stream/examples/browser-based-webrtc/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/examples/browser-based-webrtc/index.md"><meta property="og:title" content="First WebRTC broadcast in the browser · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Broadcast your webcam to Cloudflare Stream with WHIP and play it back with WHEP, using native browser WebRTC and no third-party libraries."><meta property="og:url" content="https://developers.cloudflare.com/stream/examples/browser-based-webrtc/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/examples/browser-based-webrtc/#page","headline":"First WebRTC broadcast in the browser \u00b7 Cloudflare Stream docs","description":"Broadcast your webcam to Cloudflare Stream with WHIP and play it back with WHEP, using native browser WebRTC and no third-party libraries.","url":"https://developers.cloudflare.com/stream/examples/browser-based-webrtc/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/examples/browser-based-webrtc/
  schema: 1
---
<p class="article-summary">Broadcast your webcam to Cloudflare Stream with WHIP and play it back with WHEP, using native browser WebRTC and no third-party libraries.</p>
<p>This tutorial shows how to broadcast ultra-low latency live video from a browser to Cloudflare Stream using <a href="https://www.ietf.org/archive/id/draft-ietf-wish-whip-16.html">WHIP</a> and play it back in a browser using <a href="https://www.ietf.org/archive/id/draft-murillo-whep-01.html">WHEP</a>. Both the broadcaster and the player use the browser's built-in <a href="/stream/webrtc-beta/">WebRTC</a> APIs — there are no libraries to install and no external applications.</p>
<p>By the end, you will have a basic HTML page that captures your camera and microphone, streams it to a live input, and plays the same stream back with sub-second latency. You should be able to complete this walkthrough in less than 15 minutes.</p>
<p>WHIP and WHEP are simple HTTP-based signaling protocols for WebRTC. In both cases, this code creates an <a href="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection"><code>RTCPeerConnection</code></a>, generates a local session description (SDP offer), sends that offer to a Cloudflare URL with a single HTTP <code>POST</code>, and applies the SDP answer that Cloudflare returns. Because the whole exchange is one request and response, you do not need a signaling server of your own.</p>
<h3 id="before-you-start">Before you start</h3>
<p>To follow this tutorial, you will need:</p>
<ul>
<li>Any of the following, so you can create a live input:
<ul>
<li>A paid Stream subscription.</li>
<li>A Pro or Business zone plan — these include 100 minutes of video storage and 10,000 minutes of video delivery.</li>
<li>An enterprise contract with Stream enabled.</li>
</ul>
</li>
<li>A modern browser with a camera and microphone.</li>
<li>To serve your page over <code>https</code> or from <code>localhost</code>.
<ul>
<li><em>Why?</em> Browsers only allow <a href="https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia"><code>getUserMedia()</code></a> in a <a href="https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts">secure context</a>. Opening an HTML file directly with a <code>file://</code> URL will <em>not</em> work.</li>
<li>Deploy to Cloudflare <a href="/workers/">Workers</a> or <a href="/pages/">Pages</a> to get started quickly, for free.</li>
</ul>
</li>
</ul>
<h2 id="1-create-a-live-input"><ol>
<li>Create a live input</li>
</ol></h2>
<p>Every broadcast targets a live input. Create one using either option:</p>
<ul>
<li>Use the <strong>Live inputs</strong> page of the Cloudflare dashboard, then look under the Broadcast and Playback tabs to get the WebRTC URLs.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li>Make a <code>POST</code> request to the <a href="/api/resources/stream/subresources/live_inputs/methods/create/"><code>/live_inputs</code> API endpoint</a>.</li>
</ul>
<p>The response includes two URLs you will use in this tutorial:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;uid&quot;: &quot;1a553f11a88915d093d45eda660d2f8c&quot;,&#10;  ...&#10;  &quot;webRTC&quot;: {&#10;    &quot;url&quot;: &quot;https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;SECRET&gt;/webRTC/publish&quot;&#10;  },&#10;  &quot;webRTCPlayback&quot;: {&#10;    &quot;url&quot;: &quot;https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;INPUT_UID&gt;/webRTC/play&quot;&#10;  },&#10;  ...&#10;}&#10;</code></pre>
<ul>
<li><code>webRTC.url</code> is the <strong>WHIP</strong> endpoint you broadcast to. <em>The broadcast secret is part of this URL,</em> so treat it like a stream key and share it only with the person broadcasting.</li>
<li><code>webRTCPlayback.url</code> is the <strong>WHEP</strong> endpoint viewers play from, unless you have enabled signed URLs on the input (not covered here).</li>
</ul>
<p>Copy both URLs. You will paste them into the code below.</p>
<h2 id="2-broadcast-with-whip"><ol start="2">
<li>Broadcast with WHIP</li>
</ol></h2>
<p>This broadcast script captures local media, adds it to an <code>RTCPeerConnection</code> as send-only tracks, and posts the resulting SDP offer to the WHIP URL.</p>
<p>Starting with a basic HTML page, add a <code>&lt;video&gt;</code> element to preview the local camera:</p>
<pre tabindex="0"><code class="language-html">&lt;video id=&quot;broadcast-preview&quot; autoplay muted playsinline&gt;&lt;/video&gt;&#10;</code></pre>
<p>Then add this script to broadcast:</p>
<pre tabindex="0"><code class="language-javascript">// Paste the webRTC.url value from your live input.&#10;const WHIP_URL = &quot;&lt;WHIP_URL_FROM_YOUR_LIVE_INPUT&gt;&quot;;&#10;&#10;async function startBroadcast() {&#10;	// 1. Capture the camera and microphone.&#10;	const media = await navigator.mediaDevices.getUserMedia({&#10;		video: true,&#10;		audio: true,&#10;	});&#10;	document.getElementById(&quot;broadcast-preview&quot;).srcObject = media;&#10;&#10;	// 2. Create the peer connection and add each track as send-only.&#10;	const pc = new RTCPeerConnection();&#10;	media.getTracks().forEach((track) =&gt; {&#10;		pc.addTransceiver(track, { direction: &quot;sendonly&quot; });&#10;	});&#10;&#10;	// 3. Create the SDP offer and set it as the local description.&#10;	const offer = await pc.createOffer();&#10;	await pc.setLocalDescription(offer);&#10;&#10;	// 4. POST the offer to the WHIP endpoint.&#10;	const response = await fetch(WHIP_URL, {&#10;		method: &quot;POST&quot;,&#10;		headers: { &quot;Content-Type&quot;: &quot;application/sdp&quot; },&#10;		body: offer.sdp,&#10;	});&#10;	if (!response.ok) {&#10;		throw new Error(`WHIP request failed: ${response.status}`);&#10;	}&#10;&#10;	// 5. Apply the SDP answer returned by Cloudflare.&#10;	const answer = await response.text();&#10;	await pc.setRemoteDescription({ type: &quot;answer&quot;, sdp: answer });&#10;&#10;	// The Location header identifies this session, used to stop it later.&#10;	const sessionUrl = new URL(&#10;		response.headers.get(&quot;Location&quot;),&#10;		WHIP_URL,&#10;	).toString();&#10;&#10;	return { pc, sessionUrl };&#10;}&#10;&#10;startBroadcast().catch(console.error);&#10;</code></pre>
<p>Once you call <code>startBroadcast()</code> and grant camera and microphone permission, the browser negotiates a connection and begins sending live video and audio to Cloudflare over WebRTC. You do not need to select a codec — the browser will negotiate a <a href="/stream/webrtc-beta/#supported-codecs">supported codec</a> automatically.</p>
<p>This script does not cover selecting between multiple camera or audio sources and will use the default provided by the browser.</p>
<h2 id="3-play-back-with-whep"><ol start="3">
<li>Play back with WHEP</li>
</ol></h2>
<p>The player script is the reverse of the broadcaster. Instead of adding local tracks, it adds receive-only transceivers, posts an offer to the WHEP URL, and attaches the incoming media to a <code>&lt;video&gt;</code> element.</p>
<p>Starting with a basic HTML page, add a <code>&lt;video&gt;</code> element for playback:</p>
<pre tabindex="0"><code class="language-html">&lt;video id=&quot;playback-video&quot; autoplay playsinline controls&gt;&lt;/video&gt;&#10;</code></pre>
<p>Then add this script to play:</p>
<pre tabindex="0"><code class="language-javascript">// Paste the webRTCPlayback.url value from your live input.&#10;const WHEP_URL = &quot;&lt;WHEP_URL_FROM_YOUR_LIVE_INPUT&gt;&quot;;&#10;&#10;async function startPlayback() {&#10;	const pc = new RTCPeerConnection();&#10;&#10;	// 1. Ask to receive one audio track and one video track.&#10;	pc.addTransceiver(&quot;video&quot;, { direction: &quot;recvonly&quot; });&#10;	pc.addTransceiver(&quot;audio&quot;, { direction: &quot;recvonly&quot; });&#10;&#10;	// 2. Attach incoming media to the video element as it arrives.&#10;	const stream = new MediaStream();&#10;	document.getElementById(&quot;playback-video&quot;).srcObject = stream;&#10;	pc.ontrack = (event) =&gt; stream.addTrack(event.track);&#10;&#10;	// 3. Create the SDP offer and set it as the local description.&#10;	const offer = await pc.createOffer();&#10;	await pc.setLocalDescription(offer);&#10;&#10;	// 4. POST the offer to the WHEP endpoint.&#10;	const response = await fetch(WHEP_URL, {&#10;		method: &quot;POST&quot;,&#10;		headers: { &quot;Content-Type&quot;: &quot;application/sdp&quot; },&#10;		body: offer.sdp,&#10;	});&#10;	if (!response.ok) {&#10;		throw new Error(`WHEP request failed: ${response.status}`);&#10;	}&#10;&#10;	// 5. Apply the SDP answer returned by Cloudflare.&#10;	const answer = await response.text();&#10;	await pc.setRemoteDescription({ type: &quot;answer&quot;, sdp: answer });&#10;&#10;	const sessionUrl = new URL(&#10;		response.headers.get(&quot;Location&quot;),&#10;		WHEP_URL,&#10;	).toString();&#10;&#10;	return { pc, sessionUrl };&#10;}&#10;&#10;startPlayback().catch(console.error);&#10;</code></pre>
<p>While the broadcaster is live, the player connects and shows the stream with less than 500 milliseconds of latency.</p>
<h2 id="4-stop-the-broadcast"><ol start="4">
<li>Stop the broadcast</li>
</ol></h2>
<p>WebRTC sessions end automatically when the page closes or the connection drops, but you should end them explicitly when the user is done. Send an HTTP <code>DELETE</code> to the session URL from the <code>Location</code> header, then close the peer connection:</p>
<pre tabindex="0"><code class="language-javascript">async function stop({ pc, sessionUrl }) {&#10;	if (sessionUrl) {&#10;		await fetch(sessionUrl, { method: &quot;DELETE&quot; });&#10;	}&#10;	pc.close();&#10;}&#10;</code></pre>
<p>This applies to both WHIP and WHEP sessions — pass the object returned by <code>startBroadcast()</code> or <code>startPlayback()</code>.</p>
<h2 id="5-full-working-example"><ol start="5">
<li>Full working example</li>
</ol></h2>
<p>The following single file combines everything above. Replace the two placeholder URLs with the <code>webRTC.url</code> and <code>webRTCPlayback.url</code> values from your live input. Then serve the file over <code>https</code> (with Workers or Pages) or <code>localhost</code> and open it in a browser.</p>
<pre tabindex="0"><code class="language-html">&lt;!doctype html&gt;&#10;&lt;html lang=&quot;en&quot;&gt;&#10;	&lt;head&gt;&#10;		&lt;meta charset=&quot;utf-8&quot; /&gt;&#10;		&lt;title&gt;Cloudflare Stream WHIP/WHEP example&lt;/title&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;		&lt;h2&gt;Broadcast (WHIP)&lt;/h2&gt;&#10;		&lt;video id=&quot;broadcast-preview&quot; autoplay muted playsinline&gt;&lt;/video&gt;&#10;		&lt;button id=&quot;broadcast-btn&quot;&gt;Start broadcasting&lt;/button&gt;&#10;&#10;		&lt;h2&gt;Playback (WHEP)&lt;/h2&gt;&#10;		&lt;video id=&quot;playback-video&quot; autoplay playsinline controls&gt;&lt;/video&gt;&#10;		&lt;button id=&quot;playback-btn&quot;&gt;Start playback&lt;/button&gt;&#10;&#10;		&lt;script type=&quot;module&quot;&gt;&#10;			const WHIP_URL = &quot;&lt;WHIP_URL_FROM_YOUR_LIVE_INPUT&gt;&quot;;&#10;			const WHEP_URL = &quot;&lt;WHEP_URL_FROM_YOUR_LIVE_INPUT&gt;&quot;;&#10;&#10;			async function negotiate(pc, url) {&#10;				const offer = await pc.createOffer();&#10;				await pc.setLocalDescription(offer);&#10;&#10;				const response = await fetch(url, {&#10;					method: &quot;POST&quot;,&#10;					headers: { &quot;Content-Type&quot;: &quot;application/sdp&quot; },&#10;					body: offer.sdp,&#10;				});&#10;				if (!response.ok) {&#10;					throw new Error(`Request failed: ${response.status}`);&#10;				}&#10;&#10;				const answer = await response.text();&#10;				await pc.setRemoteDescription({ type: &quot;answer&quot;, sdp: answer });&#10;				return new URL(response.headers.get(&quot;Location&quot;), url).toString();&#10;			}&#10;&#10;			document&#10;				.getElementById(&quot;broadcast-btn&quot;)&#10;				.addEventListener(&quot;click&quot;, async () =&gt; {&#10;					const media = await navigator.mediaDevices.getUserMedia({&#10;						video: true,&#10;						audio: true,&#10;					});&#10;					document.getElementById(&quot;broadcast-preview&quot;).srcObject = media;&#10;&#10;					const pc = new RTCPeerConnection();&#10;					media&#10;						.getTracks()&#10;						.forEach((track) =&gt;&#10;							pc.addTransceiver(track, { direction: &quot;sendonly&quot; }),&#10;						);&#10;&#10;					await negotiate(pc, WHIP_URL);&#10;				});&#10;&#10;			document&#10;				.getElementById(&quot;playback-btn&quot;)&#10;				.addEventListener(&quot;click&quot;, async () =&gt; {&#10;					const pc = new RTCPeerConnection();&#10;					pc.addTransceiver(&quot;video&quot;, { direction: &quot;recvonly&quot; });&#10;					pc.addTransceiver(&quot;audio&quot;, { direction: &quot;recvonly&quot; });&#10;&#10;					const stream = new MediaStream();&#10;					document.getElementById(&quot;playback-video&quot;).srcObject = stream;&#10;					pc.ontrack = (event) =&gt; stream.addTrack(event.track);&#10;&#10;					await negotiate(pc, WHEP_URL);&#10;				});&#10;		&lt;/script&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<h2 id="debugging">Debugging</h2>
<p>If a broadcast or playback session does not connect, your browser's built-in WebRTC tools show the SDP exchange and ICE connection state:</p>
<ul>
<li><strong>Chrome</strong>: Navigate to <code>chrome://webrtc-internals</code> to view detailed logs and graphs.</li>
<li><strong>Firefox</strong>: Navigate to <code>about:webrtc</code> to view information about WebRTC sessions.</li>
<li><strong>Safari</strong>: From the inspector, open the settings tab (cogwheel icon), and set WebRTC logging to &quot;Verbose&quot; in the dropdown menu.</li>
</ul>
<p>Common issues:</p>
<ul>
<li><strong><code>getUserMedia</code> throws an error or returns nothing</strong> — confirm the page is served securely and that you granted camera and microphone permission.</li>
<li><strong>The <code>POST</code> fails</strong> — confirm you pasted the correct URL. Use <code>webRTC.url</code> for broadcasting and <code>webRTCPlayback.url</code> for playback.</li>
<li><strong>Playback stays black</strong> — confirm a broadcaster is actively live on the same input and that signed URLs are not enabled.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Review the <a href="/stream/webrtc-beta/">WebRTC reference</a> for supported codecs, protocol conformance, and limitations.</li>
<li>Broadcast from other software with the <a href="/stream/webrtc-beta/#step-2-go-live-using-whip">OBS and FFmpeg instructions</a>.</li>
<li>Use a maintained <a href="/stream/webrtc-beta/#supported-whip-and-whep-clients">WHIP or WHEP client library</a> instead of writing signaling yourself.</li>
</ul>
