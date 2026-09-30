<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 31, 2026</time><h2 id="post-title">Rotate Stream broadcast keys for live inputs</h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>You can now rotate the broadcast credentials for a Stream live input without changing the live input identifier.</p>
<p>Use key rotation when live input credentials may have been shared with the wrong audience, exposed in client code or a screenshare, or need to be refreshed as part of your security process. Rotating keys revokes the old credentials, disconnects broadcasts using stale credentials, and returns refreshed credentials in the API response.</p>
<p>To rotate keys for a live input, make a <code>POST</code> request to the <code>rotate_keys</code> endpoint:</p>
<pre><code class="language-bash">curl --request POST \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/rotate_keys \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Live input responses now also include <code>keysRotatedAt</code>, which indicates when the live input keys were last rotated. This field is omitted for live inputs whose keys have never been rotated.</p>
<p>For endpoint details, refer to <a href="/api/resources/stream/subresources/live_inputs/methods/rotate_keys/">Rotate keys for a live input</a>. For usage guidance, refer to <a href="/stream/stream-live/start-stream-live/#manage-live-inputs">Manage live inputs</a>.</p>
</div></article></div>
