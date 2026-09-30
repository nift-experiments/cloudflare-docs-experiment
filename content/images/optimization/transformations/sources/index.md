<p>When optimizing remote images, you can specify which origins can be used as the source for transformed images. By default, Cloudflare accepts only source images from the zone where your transformations are served.</p>
<p>On this page, you will learn how to define and manage the origins for the source images that you want to optimize.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9458.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>In the Cloudflare dashboard, go to <strong>Images</strong> &gt; <strong>Transformations</strong> and select the zone where you want to serve transformations.</p>
<p>To get started, you must have <a href="/images/optimization/transformations/overview/#how-it-works">transformations enabled on your zone</a>.</p>
<p>In <strong>Sources</strong>, you can configure the origins for transformations on your zone.</p>
<p><img src="/assets/upstream/images/images/allowed-origins.png" alt="Enable allowed origins from the Cloudflare dashboard" /></p>
<h2 id="allow-source-images-only-from-allowed-origins">Allow source images only from allowed origins</h2>
<p>You can restrict source images to <strong>allowed origins</strong>, which applies transformations only to source images from a defined list.</p>
<p>By default, your accepted sources are set to <strong>allowed origins</strong>. Cloudflare will always allow source images from the same zone where your transformations are served.</p>
<p>If you request a transformation with a source image from outside your <strong>allowed origins</strong>, then the image will be rejected. For example, if you serve transformations on your zone <code>a.com</code> and do not define any additional origins, then <code>a.com/image.png</code> can be used as a source image, but <code>b.com/image.png</code> will return an error.</p>
<p>To define a new origin:</p>
<ol>
<li>From <strong>Sources</strong>, select <strong>Add origin</strong>.</li>
<li>Under <strong>Domain</strong>, specify the domain for the source image. Only valid web URLs will be accepted.</li>
</ol>
<p><img src="/assets/upstream/images/images/add-origin.png" alt="Add the origin for source images in the Cloudflare dashboard" /></p>
<p>When you add a root domain, subdomains are not accepted. In other words, if you add <code>b.com</code>, then source images from <code>media.b.com</code> will be rejected.</p>
<p>To support individual subdomains, define an additional origin such as <code>media.b.com</code>. If you add only <code>media.b.com</code> and not the root domain, then source images from the root domain (<code>b.com</code>) and other subdomains (<code>cdn.b.com</code>) will be rejected.</p>
<p>To support all subdomains, use the <code>*</code> wildcard at the beginning of the root domain. For example, <code>*.b.com</code> will accept source images from the root domain (like <code>b.com/image.png</code>) as well as from subdomains (like <code>media.b.com/image.png</code> or <code>cdn.b.com/image.png</code>).</p>
<ol start="3">
<li>Optionally, you can specify the <strong>Path</strong> for the source image. If no path is specified, then source images from all paths on this domain are accepted.</li>
</ol>
<p>Cloudflare checks whether the defined path is at the beginning of the source path. If the defined path is not present at the beginning of the path, then the source image will be rejected.</p>
<p>For example, if you define an origin with domain <code>b.com</code> and path <code>/themes</code>, then <code>b.com/themes/image.png</code> will be accepted but <code>b.com/media/themes/image.png</code> will be rejected.</p>
<ol start="4">
<li>Select <strong>Add</strong>. Your origin will now appear in your list of allowed origins.</li>
<li>Select <strong>Save</strong>. These changes will take effect immediately.</li>
</ol>
<p>When you configure <strong>allowed origins</strong>, only the initial URL of the source image is checked. Any redirects, including URLs that leave your zone, will be followed, and the resulting image will be transformed.</p>
<p>If you change your accepted sources to <strong>any origin</strong>, then your list of sources will be cleared and reset to default.</p>
<h2 id="allow-source-images-from-any-origin">Allow source images from any origin</h2>
<p>When your accepted sources are set to <strong>any origin</strong>, any publicly available image can be used as the source image for transformations on this zone.</p>
<p><strong>Any origin</strong> is less secure and may allow third parties to serve transformations on your zone.</p>
