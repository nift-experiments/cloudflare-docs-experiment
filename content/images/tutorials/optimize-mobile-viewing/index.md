<p>You can use lazy loading to optimize the images on your webpages for mobile viewing. This helps address common challenges of mobile viewing, like slow network connections or weak processing capabilities.</p>
<p>Lazy loading has two main advantages:</p>
<ul>
<li><strong>Faster page load times</strong> — Images are loaded as the user scrolls down the page, instead of all at once when the page is opened.</li>
<li><strong>Lower costs for image delivery</strong> — When using Cloudflare Images, you only pay to load images that the user actually sees. With lazy loading, images that are not scrolled into view do not count toward your billable Images requests.</li>
</ul>
<p>Lazy loading is natively supported on all major browsers, including Chrome, Safari, Firefox, Opera, and Edge.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9341.md")
</aside>
<h2 id="modify-your-loading-attribute">Modify your loading attribute</h2>
<p>Without modifying your loading attribute, most browsers will fetch all images on a page, prioritizing the images that are closest to the viewport by default. You can override this by modifying your <code>loading</code> attribute.</p>
<p>There are two possible <code>loading</code> attributes for your <code>&lt;img&gt;</code> tags: <code>lazy</code> and <code>eager</code>.</p>
<h3 id="lazy-loading">Lazy loading</h3>
<p>Lazy loading is recommended for most images. With Lazy loading, resources like images are deferred until they reach a certain distance from the viewport. If an image does not reach the threshold, then it does not get loaded.</p>
<p>Example of modifying the <code>loading</code> attribute of your <code>&lt;img&gt;</code> tags to be <code>&quot;lazy&quot;</code>:</p>
<pre><code class="language-html">&lt;img src=&quot;example.com/cdn-cgi/width=300/image.png&quot; loading=&quot;lazy&quot; /&gt;&#10;</code></pre>
<h3 id="eager-loading">Eager loading</h3>
<p>If you have images that are in the viewport, eager loading, instead of lazy loading, is recommended. Eager loading loads the asset at the initial page load, regardless of its location on the page.</p>
<p>Example of modifying the <code>loading</code> attribute of your <code>&lt;img&gt;</code> tags to be <code>&quot;eager&quot;</code>:</p>
<pre><code class="language-html">&lt;img src=&quot;example.com/cdn-cgi/width=300/image.png&quot; loading=&quot;eager&quot; /&gt;&#10;</code></pre>
