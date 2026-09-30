<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 28, 2026</time><h2 id="post-title">Record specific participant audio tracks in RealtimeKit</h2>
<div class="changelog-badges"><span>realtime</span></div><div class="changelog-body"><p>You can now record specific participant audio tracks in RealtimeKit with <a href="/realtime/realtimekit/recording-guide/track-recording/">track recording</a>. Track recording creates separate WebM files for each participant instead of a single composite recording, which is useful for post-processing, transcription, and regulated or content-sensitive workflows.</p>
<p>To record specific participants, pass <code>user_ids</code> when starting a track recording:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/recordings/track \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;meeting_id&quot;: &quot;97440c6a-140b-40a9-9499-b23fd7a3868a&quot;,&#10;  &quot;user_ids&quot;: [&quot;user-123&quot;, &quot;user-456&quot;]&#10;}&#x27;&#10;</code></pre>
<p>To pass <code>user_ids</code> for selective track recording, use the following minimum SDK versions:</p>
<ul>
<li>Web Core: <code>@cloudflare/realtimekit</code> version <code>1.4.0</code> or later</li>
<li>Web UI Kit: <code>@cloudflare/realtimekit-ui</code>, <code>@cloudflare/realtimekit-react-ui</code>, or <code>@cloudflare/realtimekit-angular-ui</code> version <code>1.1.2</code> or later</li>
<li>Android Core or iOS Core: version <code>2.0.0</code> or later</li>
<li>Android UI Kit or iOS UI Kit: version <code>1.1.0</code> or later</li>
</ul>
<p><a href="/realtime/realtimekit/">RealtimeKit</a> provides SDKs and UI components so that you can build your own meeting experience on Cloudflare's <a href="/realtime/#realtime-sfu">global WebRTC infrastructure</a>. Teams today build products ranging from telehealth to education on RealtimeKit for global audiences. You can get started today with our <a href="/realtime/realtimekit/quickstart/">Quickstart</a> or take a look at our <a href="https://github.com/cloudflare/meet">Cloudflare Meet repo</a> as a reference.</p>
</div></article></div>
