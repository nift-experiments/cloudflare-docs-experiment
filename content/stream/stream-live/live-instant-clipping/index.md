<p>Stream supports generating clips of live streams and recordings so creators and viewers alike can highlight short, engaging pieces of a longer broadcast or recording. Live instant clips can be created by end users and do not result in additional storage fees or new entries in the video library.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note:</h3>
@markup("md", "content/.markup/bodies/14402.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>When configuring a <a href="/stream/stream-live/start-stream-live/">Live input</a>, ensure &quot;Live Playback and Recording&quot; (<code>mode</code>) is enabled.</p>
<p>API keys are not needed to generate a preview or clip, but are needed to create Live Inputs.</p>
<p>Live instant clips are generated dynamically from the recording of a live stream. When generating clips manifests or MP4s, always reference the Video ID, not the Live Input ID. If the recording is deleted, the instant clip will no longer be available.</p>
<h2 id="preview-manifest">Preview manifest</h2>
<p>To help users replay and seek recent content, request a preview manifest by adding a <code>duration</code> parameter to the HLS manifest URL:</p>
<pre><code class="language-txt">https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;VIDEO_ID||INPUT_ID&gt;/manifest/video.m3u8?duration=5m&#10;</code></pre>
<ul>
<li><code>duration</code> string duration of the preview, up to 5 minutes as either a number of seconds (&quot;30s&quot;) or minutes (&quot;3m&quot;)</li>
</ul>
<p>When the preview manifest is delivered, inspect the headers for two properties:</p>
<ul>
<li><code>preview-start-seconds</code> float seconds into the start of the live stream or recording that the preview manifest starts. Useful in applications that allow a user to select a range from the preview because the clip will need to reference its offset from the <em>broadcast</em> start time, not the <em>preview</em> start time.</li>
<li><code>stream-media-id</code> string the video ID of the live stream or recording. Useful in applications that render the player using an <em>input</em> ID because the clip URL should reference the <em>video</em> ID.</li>
</ul>
<p>This manifest can be played and seeked using any HLS-compatible player.</p>
<h3 id="reading-headers">Reading headers</h3>
<p>Reading headers when loading a manifest requires adjusting how players handle
the response. For example, if using <a href="https://github.com/video-dev/hls.js">HLS.js</a>
and the default loader, override the <code>pLoader</code> (playlist loader) class:</p>
<pre><code class="language-js">let currentPreviewStart;&#10;let currentPreviewVideoID;&#10;&#10;// Override the pLoader (playlist loader) to read the manifest headers:&#10;class pLoader extends Hls.DefaultConfig.loader {&#10;  constructor(config) {&#10;    super(config);&#10;    var load = this.load.bind(this);&#10;    this.load = function (context, config, callbacks) {&#10;      if (context.type == &#x27;manifest&#x27;) {&#10;        var onSuccess = callbacks.onSuccess;&#10;        // copy the existing onSuccess handler to fire it later.&#10;&#10;        callbacks.onSuccess = function (response, stats, context, networkDetails) {&#10;          // The fourth argument here is undocumented in HLS.js but contains&#10;          // the response object for the manifest fetch, which gives us headers:&#10;&#10;          currentPreviewStart =&#10;            parseFloat(networkDetails.getResponseHeader(&#x27;preview-start-seconds&#x27;));&#10;          // Save the start time of the preview manifest&#10;&#10;          currentPreviewVideoID =&#10;            networkDetails.getResponseHeader(&#x27;stream-media-id&#x27;);&#10;          // Save the video ID in case the preview was loaded with an input ID&#10;&#10;          onSuccess(response, stats, context);&#10;          // And fire the existing success handler.&#10;        };&#10;      }&#10;      load(context, config, callbacks);&#10;    };&#10;  }&#10;}&#10;&#10;// Specify the new loader class when setting up HLS&#10;const hls = new Hls({&#10;  pLoader: pLoader,&#10;});&#10;</code></pre>
<h2 id="clip-manifest">Clip manifest</h2>
<p>To play a clip of a live stream or recording, request a clip manifest with a duration and a start time, relative to the start of the live stream.</p>
<pre><code class="language-txt">https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;VIDEO_ID&gt;/manifest/clip.m3u8?time=600s&amp;duration=30s&#10;</code></pre>
<ul>
<li><code>time</code> string start time of the clip in seconds, from the start of the live stream or recording</li>
<li><code>duration</code> string duration of the clip in seconds, up to 60 seconds max</li>
</ul>
<p>This manifest can be played and seeked using any HLS-compatible player.</p>
<h2 id="clip-mp4-download">Clip MP4 download</h2>
<p>An MP4 of the clip can also be generated dynamically to be saved and shared on other platforms.</p>
<pre><code class="language-txt">https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;VIDEO_ID&gt;/clip.mp4?time=600s&amp;duration=30s&amp;filename=clip.mp4&#10;</code></pre>
<ul>
<li><code>time</code> string start time of the clip in seconds, from the start of the live stream or recording (example: &quot;500s&quot;)</li>
<li><code>duration</code> string duration of the clip in seconds, up to 60 seconds max (example: &quot;60s&quot;)</li>
<li><code>filename</code> string <em>(optional)</em> a filename for the clip</li>
</ul>
