<p>When optimizing remote videos, you can specify which origins can be used as the source for transformed videos. By default, Cloudflare accepts only source videos from the zone where your transformations are served.</p>
<p>On this page, you will learn how to define and manage the origins for the source videos that you want to optimize.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14392.md")
</aside>
<h2 id="configure-origins">Configure origins</h2>
<p>To get started, you must have <a href="/stream/transform-videos/#getting-started">transformations enabled on your zone</a>.</p>
<p>In the Cloudflare dashboard, go to <strong>Stream</strong> &gt; <strong>Transformations</strong> and select the zone where you want to serve transformations.</p>
<p>In <strong>Sources</strong>, you can configure the origins for transformations on your zone.</p>
<p><img src="/assets/upstream/images/images/allowed-origins.png" alt="Enable allowed origins from the Cloudflare dashboard" /></p>
<h2 id="allow-source-videos-only-from-allowed-origins">Allow source videos only from allowed origins</h2>
<p>You can restrict source videos to <strong>allowed origins</strong>, which applies transformations only to source videos from a defined list.</p>
<p>By default, your accepted sources are set to <strong>allowed origins</strong>. Cloudflare will always allow source videos from the same zone where your transformations are served.</p>
<p>If you request a transformation with a source video from outside your <strong>allowed origins</strong>, then the video will be rejected. For example, if you serve transformations on your zone <code>a.com</code> and do not define any additional origins, then <code>a.com/video.mp4</code> can be used as a source video, but <code>b.com/video.mp4</code> will return an error.</p>
<p>To define a new origin:</p>
<ol>
<li>From <strong>Sources</strong>, select <strong>Add origin</strong>.</li>
<li>Under <strong>Domain</strong>, specify the domain for the source video. Only valid web URLs will be accepted.</li>
</ol>
<p><img src="/assets/upstream/images/images/add-origin.png" alt="Add the origin for source videos in the Cloudflare dashboard" /></p>
<p>When you add a root domain, subdomains are not accepted. In other words, if you add <code>b.com</code>, then source videos from <code>media.b.com</code> will be rejected.</p>
<p>To support individual subdomains, define an additional origin such as <code>media.b.com</code>. If you add only <code>media.b.com</code> and not the root domain, then source videos from the root domain (<code>b.com</code>) and other subdomains (<code>cdn.b.com</code>) will be rejected.</p>
<p>To support all subdomains, use the <code>*</code> wildcard at the beginning of the root domain. For example, <code>*.b.com</code> will accept source videos from the root domain (like <code>b.com/video.mp4</code>) as well as from subdomains (like <code>media.b.com/video.mp4</code> or <code>cdn.b.com/video.mp4</code>).</p>
<ol start="3">
<li>Optionally, you can specify the <strong>Path</strong> for the source video. If no path is specified, then source videos from all paths on this domain are accepted.</li>
</ol>
<p>Cloudflare checks whether the defined path is at the beginning of the source path. If the defined path is not present at the beginning of the path, then the source video will be rejected.</p>
<p>For example, if you define an origin with domain <code>b.com</code> and path <code>/themes</code>, then <code>b.com/themes/video.mp4</code> will be accepted but <code>b.com/media/themes/video.mp4</code> will be rejected.</p>
<ol start="4">
<li>Select <strong>Add</strong>. Your origin will now appear in your list of allowed origins.</li>
<li>Select <strong>Save</strong>. These changes will take effect immediately.</li>
</ol>
<p>When you configure <strong>allowed origins</strong>, only the initial URL of the source video is checked. Any redirects, including URLs that leave your zone, will be followed, and the resulting video will be transformed.</p>
<p>If you change your accepted sources to <strong>any origin</strong>, then your list of sources will be cleared and reset to default.</p>
<h2 id="allow-source-videos-from-any-origin">Allow source videos from any origin</h2>
<p>When your accepted sources are set to <strong>any origin</strong>, any publicly available video can be used as the source video for transformations on this zone.</p>
<p><strong>Any origin</strong> is less secure and may allow third parties to serve transformations on your zone.</p>
