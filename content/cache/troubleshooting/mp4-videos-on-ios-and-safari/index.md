<p>When traffic is proxied through Cloudflare, Safari on macOS and iOS devices may fail to load MP4 video files.</p>
<p>This issue occurs because Safari handles HTTP range requests differently than other browsers, particularly in how it processes ETags during video streaming.</p>
<p>Safari and iOS devices rely on HTTP range requests to support video features such as seeking to specific timestamps and resuming interrupted downloads.</p>
<p>When Cloudflare's caching layer processes these range requests with weak ETags, Safari may reject the cached response entirely, resulting in videos that fail to load or display as black screens.</p>
<p>To resolve this issue, configure two cache rules in the following order.</p>
<h2 id="1-create-the-strong-etags-rule"><ol>
<li>Create the strong ETags rule</li>
</ol></h2>
<p>Create a <a href="/cache/how-to/cache-rules/create-dashboard/">cache rule</a> that applies to all MP4 files, marks them as eligible for cache, and turns on the Respect Strong ETags setting.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Cache Rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong> &gt; <strong>Cache rules</strong>.</li>
<li>Enter a descriptive name for the rule in <strong>Rule name</strong>.</li>
<li>In the <strong>When incoming requests match…</strong> section, create a filter that applies to all MP4 files, for example <code>URI Full</code> <code>Wildcard</code> <code>*.mp4</code>.</li>
<li>Select <strong>Eligible for cache</strong> in the <strong>Cache eligibility</strong> section.</li>
<li>Select <strong>+ Add Setting</strong> for <strong>Respect strong ETags</strong> and turn on the toggle.</li>
<li>Select <strong>Last</strong> as <strong>Place at</strong>.</li>
</ol>
<h2 id="2-create-the-bypass-cache-rule"><ol start="2">
<li>Create the bypass cache rule</li>
</ol></h2>
<p>Create another cache rule that applies to all MP4 files and bypasses cache entirely.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Cache Rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong> &gt; <strong>Cache rules</strong>.</li>
<li>Enter a descriptive name for the rule in <strong>Rule name</strong>.</li>
<li>In the <strong>When incoming requests match…</strong> section, create the same filter for MP4 files, for example <code>URI Full</code> <code>Wildcard</code> <code>*.mp4</code>.</li>
<li>Select <strong>Bypass cache</strong> in the <strong>Cache eligibility</strong> section.</li>
<li>Select <strong>Last</strong> as <strong>Place at</strong>.</li>
</ol>
<h2 id="why-this-order-matters">Why this order matters</h2>
<p>The first rule preserves strong ETags for MP4 files, which satisfies Safari's requirements for range request handling. The second rule bypasses cache so that Cloudflare forwards range requests to the origin server instead of serving cached responses with potentially mismatched ETags.</p>
<p>The first rule must appear above the second rule in the Cache Rules list.</p>
