<h2 id="stream">Stream</h2>
<h3 id="can-i-download-original-video-files-from-stream">Can I download original video files from Stream?</h3>
<p>You cannot download the <em>exact</em> input file that you uploaded. However, depending on your use case, you can use the <a href="/stream/viewing-videos/download-videos/">Downloadable Videos</a> feature to get encoded MP4s for use cases like offline viewing.</p>
<h3 id="is-there-a-limit-to-the-amount-of-videos-i-can-upload">Is there a limit to the amount of videos I can upload?</h3>
<ul>
<li>
<p>By default, a video upload can be at most 30 GB.</p>
</li>
<li>
<p>By default, you can have up to 120 videos queued or being encoded simultaneously. Videos in the <code>ready</code> status are playable but may still be encoding certain quality levels until the <code>pctComplete</code> reaches 100. Videos in the <code>error</code>, <code>ready</code>, or <code>pendingupload</code> state do not count toward this limit. If you need the concurrency limit raised, <a href="/support/contacting-cloudflare-support/">contact Cloudflare support</a> explaining your use case and why you would like the limit raised.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/305.md")
</aside>
<ul>
<li>An account cannot upload videos if the total video duration exceeds the video storage capacity purchased.</li>
</ul>
<p>Limits apply to Direct Creator Uploads at the time of upload URL creation.</p>
<p>Uploads over these limits will receive a <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-429/">429 (Too Many Requests)</a> or <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-413/">413 (Payload too large)</a> HTTP status codes with more information in the response body. For higher limits, <a href="/support/contacting-cloudflare-support/">contact Cloudflare support</a> or your account team.</p>
<h3 id="can-i-embed-videos-on-stream-even-if-my-domain-is-not-on-cloudflare">Can I embed videos on Stream even if my domain is not on Cloudflare?</h3>
<p>Yes. Stream videos can be embedded on any domain, even domains not on Cloudflare.</p>
<h3 id="does-stream-support-high-dynamic-range-hdr-video-content">Does Stream support High Dynamic Range (HDR) video content?</h3>
<p>When HDR videos are uploaded to Stream, they are re-encoded and delivered in SDR format, to ensure compatibility with the widest range of viewing devices.</p>
<h3 id="what-are-the-recommended-upload-settings-for-video-uploads">What are the recommended upload settings for video uploads?</h3>
<p>If you are producing a brand new file for Cloudflare Stream, we recommend you use the following settings:</p>
<ul>
<li>MP4 containers, AAC audio codec, H264 video codec, 30 or below frames per second</li>
<li>moov atom should be at the front of the file (Fast Start)</li>
<li>H264 progressive scan (no interlacing)</li>
<li>H264 high profile</li>
<li>Closed GOP</li>
<li>Content should be encoded and uploaded in the same frame rate it was recorded</li>
<li>Mono or Stereo audio (Stream will mix audio tracks with more than 2 channels down to stereo)</li>
</ul>
<p>Below are bitrate recommendations for encoding new videos for Stream:</p>
<table-wrap>
<table>
<thead>
<tr>
<th>Resolution</th>
<th>Recommended bitrate</th>
</tr>
</thead>
<tbody>
<tr>
<td>1080p</td>
<td>8 Mbps</td>
</tr>
<tr>
<td>720p</td>
<td>4.8 Mbps</td>
</tr>
<tr>
<td>480p</td>
<td>2.4 Mbps</td>
</tr>
<tr>
<td>360p</td>
<td>1 Mbps</td>
</tr>
</tbody>
</table>
</table-wrap>
<h3 id="if-i-cancel-my-stream-subscription-are-the-videos-deleted">If I cancel my stream subscription, are the videos deleted?</h3>
<p>Videos are removed if the subscription is not renewed within 30 days.</p>
<h3 id="i-use-content-security-policy-csp-on-my-website-what-domains-do-i-need-to-add-to-which-directives">I use Content Security Policy (CSP) on my website. What domains do I need to add to which directives?</h3>
<p>If your website uses <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/306.md")
</div> directives, depending on your configuration, you may need to add Cloudflare Stream's domains to particular directives, in order to allow videos to be viewed or uploaded by your users.
<p>If you use the provided <a href="/stream/viewing-videos/using-the-stream-player/">Stream Player</a>, <code>videodelivery.net</code> and <code>*.cloudflarestream.com</code> must be included in the <code>frame-src</code> or <code>default-src</code> directive to allow the player's <code>&lt;iframe&gt;</code> element to load.</p>
<pre><code class="language-http">Content-Security-Policy: frame-src &#x27;self&#x27; videodelivery.net *.cloudflarestream.com&#10;</code></pre>
<p>If you use your <strong>own</strong> Player, add <code>*.videodelivery.net</code> and <code>*.cloudflarestream.com</code> to the <code>media-src</code>, <code>img-src</code> and <code>connect-src</code> CSP directives to allow video files and thumbnail images to load.</p>
<pre><code class="language-http">Content-Security-Policy: media-src &#x27;self&#x27; videodelivery.net *.cloudflarestream.com; img-src &#x27;self&#x27; *.videodelivery.net *.cloudflarestream.com; connect-src &#x27;self&#x27; *.videodelivery.net *.cloudflarestream.com&#10;</code></pre>
<p>If you allow users to upload their own videos directly to Cloudflare Stream, add <code>*.videodelivery.net</code> and <code>*.cloudflarestream.com</code> to the <code>connect-src</code> CSP directive.</p>
<pre><code class="language-http">Content-Security-Policy: connect-src &#x27;self&#x27; *.videodelivery.net *.cloudflarestream.com&#10;</code></pre>
<p>To ensure <strong>only</strong> videos from <strong>your</strong> Cloudflare Stream account can be played on your website, replace <code>*</code> in <code>*.cloudflarestream.com</code> and <code>*.videodelivery.net</code> in the examples above with <code>customer-&lt;CODE&gt;</code>, replacing <code>&lt;CODE&gt;</code> with your unique customer code. To find your unique customer code in the Cloudflare dashboard, go to the <strong>Stream</strong> page.</p>
<div class="nb-dash-button"></div>
<p>This code is unique to your Cloudflare Account.</p>
<h3 id="why-is-pagespeed-insights-giving-a-bad-score-when-using-the-stream-player">Why is PageSpeed Insights giving a bad score when using the Stream Player?</h3>
<p>If your website loads in a lot of player instances, PageSpeed Insights will penalize the JavaScript load for each player instance. Our testing shows that when actually loading the page, the script itself is only downloaded once with the local browser cache retrieving the script for the other player objects on the same page. Therefore, we believe that the PageSpeed Insights score is not matching real-world behavior in this situation.</p>
<p>If you are using thumbnails, you can use <a href="/stream/viewing-videos/displaying-thumbnails/#animated-gif-thumbnails">animated thumbnails</a> that link to the video pages.</p>
<p>If multiple players are on the same page, you can lazy load any players that are not visible in the initial viewport. For more information about lazy loading, refer to <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#lazy">Mozilla's lazy loading documentation</a>.</p>
