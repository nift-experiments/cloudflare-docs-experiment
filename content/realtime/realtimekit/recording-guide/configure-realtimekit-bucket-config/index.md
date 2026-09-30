<p>Once the recording is complete, by default, RealtimeKit uploads all recordings to RealtimeKit's Cloudflare R2 bucket. Additionally, a presigned URL is generated with a 7-day expiry. The recording can be accessed using the <code>downloadUrl</code> associated with each recording.</p>
<p>However, RealtimeKit provides users with the flexibility to choose whether or not to upload their recordings to RealtimeKit's R2 bucket. If you wish to disable uploads to RealtimeKit's bucket, you can set the <code>realtimekit_bucket_config</code> parameter to false in the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a>.</p>
<p>For example:</p>
<pre><code class="language-json">{&#10;	&quot;realtimekit_bucket_config&quot;: {&#10;		&quot;enabled&quot;: false&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11814.md")
</aside>
