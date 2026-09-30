<p>When you upload a video to Stream, it can be streamed using HLS/DASH. However, for certain use-cases, you may want to download the MP4 or M4A file.
For cases such as offline viewing, you may want to download the MP4 file. Whereas, for downstream tasks like AI summarization, if you want to extract only the audio, downloading an M4A file may be more useful.</p>
<h2 id="generate-downloadable-mp4-files">Generate downloadable MP4 files</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14331.md")
</aside>
<p>You can enable MP4 support on a per video basis by following the steps below:</p>
<ol>
<li>Enable MP4 support by making a POST request to the <code>/downloads</code> or <code>/downloads/default</code> endpoint.</li>
<li>Save the MP4 URL provided by the response to the endpoint. This MP4 URL will become functional when the MP4 is ready in the next step.</li>
<li>Poll the <code>/downloads</code> endpoint until the <code>status</code> field is set to <code>ready</code> to inform you when the MP4 is available. You can now use the MP4 URL from step 2.</li>
</ol>
<p>You can enable downloads for an uploaded video once it is ready to view by making an HTTP request to either the <code>/downloads</code> or <code>/downloads/default</code> endpoint.</p>
<p>To get notified when a video is ready to view, refer to <a href="/stream/manage-video-library/using-webhooks/#notifications">Using webhooks</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14340.md")
</div></div>
<h2 id="generate-downloadable-m4a-files">Generate downloadable M4A files</h2>
<p>To enable M4A support on a per video basis, follow steps similar to that of generating an MP4 download, but instead send a POST request to the <code>/downloads/audio</code> endpoint.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14349.md")
</div></div>
<h2 id="get-download-links">Get download links</h2>
<p>You can view all available downloads for a video by making a <code>GET</code> HTTP request to the downloads API.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14358.md")
</div></div>
<h2 id="customize-download-file-name">Customize download file name</h2>
<p>You can customize the name of downloadable files by adding the <code>filename</code> query string parameter at the end of the URL.</p>
<p>In the example below, adding <code>?filename=MY_VIDEO.mp4</code> to the URL will change the file name to <code>MY_VIDEO.mp4</code>.</p>
<p><code>https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;VIDEO_UID&gt;/downloads/default.mp4?filename=MY_VIDEO.mp4</code></p>
<p>The <code>filename</code> can be a maximum of 120 characters long and composed of <code>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_</code> characters. The extension (.mp4) is appended automatically.</p>
<h2 id="retrieve-downloads">Retrieve downloads</h2>
<p>The generated MP4 download files can be retrieved via the link in the download API response.</p>
<pre><code class="language-sh">curl -L https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;VIDEO_UID&gt;/downloads/default.mp4 &gt; download.mp4&#10;</code></pre>
<h2 id="delete-downloads">Delete downloads</h2>
<p>You can delete a download for a video. Available types are <code>default</code> and <code>audio</code>. Defaults to <code>default</code> when omitted.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14367.md")
</div></div>
<h2 id="secure-video-downloads">Secure video downloads</h2>
<p>If your video is public, the MP4 will also be publicly accessible. If your video is private and requires a signed URL for viewing, the MP4 will not be publicly accessible. To access the MP4 for a private video, you can generate a signed URL just as you would for regular viewing with an additional flag called <code>downloadable</code> set to <code>true</code>.</p>
<p>You can generate a signed token using the Stream binding:</p>
<pre><code class="language-ts">export default {&#10;	async fetch(request, env) {&#10;		const token = await env.STREAM.video(&quot;VIDEO_ID&quot;).generateToken();&#10;		return Response.json({ token });&#10;	},&#10;};&#10;</code></pre>
<p>Download links will not work for videos which already require signed URLs if the <code>downloadable</code> flag is not present in the token.</p>
<p>For more details about using signed URLs with videos, refer to <a href="/stream/viewing-videos/securing-your-stream/">Securing your Stream</a>.</p>
<p><strong>Example token payload</strong></p>
<pre><code class="language-json">{&#10;    &quot;sub&quot;: &lt;VIDEO_UID&gt;,&#10;    &quot;kid&quot;: &lt;KEY_ID&gt;,&#10;    &quot;exp&quot;: 1537460365,&#10;    &quot;nbf&quot;: 1537453165,&#10;    &quot;downloadable&quot;: true,&#10;    &quot;accessRules&quot;: [&#10;      {&#10;        &quot;type&quot;: &quot;ip.geoip.country&quot;,&#10;        &quot;action&quot;: &quot;allow&quot;,&#10;        &quot;country&quot;: [&#10;          &quot;GB&quot;&#10;        ]&#10;      },&#10;      {&#10;        &quot;type&quot;: &quot;any&quot;,&#10;        &quot;action&quot;: &quot;block&quot;&#10;      }&#10;    ]&#10;  }&#10;</code></pre>
<h2 id="billing-for-mp4-downloads">Billing for MP4 downloads</h2>
<p>MP4 downloads are billed in the same way as streaming of the video. You will be billed for the duration of the video each time the MP4 for the video is downloaded. For example, if you have a 10 minute video that is downloaded 100 times during the month, the downloads will count as 1000 minutes of minutes served.</p>
<p>You will not incur any additional cost for storage when you enable MP4s.</p>
