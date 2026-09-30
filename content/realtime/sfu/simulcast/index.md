<p>Simulcast is a feature of WebRTC that allows a publisher to send multiple video streams of the same media at different qualities. For example, this is useful for scenarios where you want to send a high quality stream for desktop users and a lower quality stream for mobile users.</p>
<pre><code class="language-mermaid">graph LR&#10;    A[Publisher] --&gt;|Low quality| B[Cloudflare Realtime SFU]&#10;    A --&gt;|Medium quality| B&#10;    A --&gt;|High quality| B&#10;B --&gt;|Low quality| C@{ shape: procs, label: &quot;Subscribers&quot;}&#10;B --&gt;|Medium quality| D@{ shape: procs, label: &quot;Subscribers&quot;}&#10;B --&gt;|High quality| E@{ shape: procs, label: &quot;Subscribers&quot;}&#10;</code></pre>
<h3 id="how-it-works">How it works</h3>
<p>Simulcast in WebRTC allows a single video source, like a camera or screen share, to be encoded at multiple quality levels and sent simultaneously, which is beneficial for subscribers with varying network conditions and device capabilities. The video source is encoded into multiple streams, each identified by RIDs (RTP Stream Identifiers) for different quality levels, such as low, medium, and high. These simulcast streams are described in the SDP you send to Cloudflare Realtime SFU. It's the responsibility of the Cloudflare Realtime SFU to ensure that the appropriate quality stream is delivered to each subscriber based on their network conditions and device capabilities.</p>
<p>Cloudflare Realtime SFU will automatically handle the simulcast configuration based on the SDP you send to it from the publisher. The SFU will then automatically switch between the different quality levels based on the subscriber's network conditions, or the quality level can be controlled manually via the API. You can control the quality switching behavior using the <code>simulcast</code> configuration object when you send an API call to start pulling a remote track.</p>
<h3 id="quality-control">Quality Control</h3>
<p>The <code>simulcast</code> configuration object in the API call when you start pulling a remote track allows you to specify:</p>
<ul>
<li>
<p><code>preferredRid</code>: The preferred quality level for the video stream (RID for the simulcast stream. <a href="https://developer.mozilla.org/en-US/docs/Web/API/RTCRtpSender/setParameters#encodings">RIDs can be specified by the publisher.</a>)</p>
</li>
<li>
<p><code>priorityOrdering</code>: Controls how the SFU handles bandwidth constraints.</p>
<ul>
<li><code>none</code>: Keep sending the preferred layer, set via the preferredRid, even if there's not enough bandwidth.</li>
<li><code>asciibetical</code>: Use alphabetical ordering (a-z) to determine priority, where 'a' is most desirable and 'z' is least desirable.</li>
</ul>
</li>
<li>
<p><code>ridNotAvailable</code>: Controls what happens when the preferred RID is no longer available, for example when the publisher stops sending it.</p>
<ul>
<li><code>none</code>: Do nothing.</li>
<li><code>asciibetical</code>: Switch to the next available RID based on the priority ordering, where 'a' is most desirable and 'z' is least desirable.</li>
</ul>
<p>You will likely want to order the asciibetical RIDs based on your desired metric, such as highest resolution to lowest or highest bandwidth to lowest.</p>
</li>
</ul>
<h3 id="bandwidth-management-across-media-tracks">Bandwidth Management across media tracks</h3>
<p>Cloudflare Realtime treats all media tracks equally at the transport level. For example, if you have multiple video tracks (cameras, screen shares, etc.), they all have equal priority for bandwidth allocation. This means:</p>
<ol>
<li>Each track's simulcast configuration is handled independently</li>
<li>The SFU performs automatic bandwidth estimation and layer switching based on network conditions independently for each track</li>
</ol>
<h3 id="layer-switching-behavior">Layer Switching Behavior</h3>
<p>When a layer switch is requested (through updating <code>preferredRid</code>) with the <code>/tracks/update</code> API:</p>
<ol>
<li>The SFU will automatically generate a Full Intraframe Request (FIR)</li>
<li>PLI generation is debounced to prevent excessive requests</li>
</ol>
<h3 id="publisher-configuration">Publisher Configuration</h3>
<p>For publishers (local tracks), you only need to include the simulcast attributes in your SDP. The SFU will automatically handle the simulcast configuration based on the SDP. For example, the SDP should contain a section like this:</p>
<pre><code class="language-txt">a=simulcast:send f;h;q&#10;a=rid:f send&#10;a=rid:h send&#10;a=rid:q send&#10;</code></pre>
<p>If the publisher endpoint is a browser you can include these by specifying <code>sendEncodings</code> when creating the transceiver like this:</p>
<pre><code class="language-js">const transceiver = peerConnection.addTransceiver(track, {&#10;	direction: &quot;sendonly&quot;,&#10;	sendEncodings: [&#10;		{ scaleResolutionDownBy: 1, rid: &quot;f&quot; },&#10;		{ scaleResolutionDownBy: 2, rid: &quot;h&quot; },&#10;		{ scaleResolutionDownBy: 4, rid: &quot;q&quot; },&#10;	],&#10;});&#10;</code></pre>
<h2 id="example">Example</h2>
<p>Here's an example of how to use simulcast with Cloudflare Realtime:</p>
<ol>
<li>Create a new local track with simulcast configuration. There should be a section in the SDP with <code>a=simulcast:send</code>.</li>
<li>Use the <a href="/realtime/sfu/https-api">Cloudflare Realtime API</a> to push this local track, by calling the /tracks/new endpoint.</li>
<li>Use the <a href="/realtime/sfu/https-api">Cloudflare Realtime API</a> to start pulling a remote track (from another browser or device), by calling the /tracks/new endpoint and specifying the <code>simulcast</code> configuration object along with the remote track ID you get from step 2.</li>
</ol>
<p>For more examples, check out the <a href="https://github.com/cloudflare/calls-examples/tree/main/echo-simulcast">Realtime Examples GitHub repository</a>.</p>
