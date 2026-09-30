<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17308.md")
</aside>
<p>Like with any other Worker, <a href="/workers/configuration/routing/routes/">you can configure a Worker with assets to run on a path of your domain</a>.
Assets defined for a Worker must be nested in a directory structure that mirrors the desired path.</p>
<p>For example, to serve assets from <code>example.com/blog/*</code>, create a <code>blog</code> directory in your asset directory.</p>
<pre class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/17309.md")&#10;&#10;&#10;</pre>
<p>With a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> like so:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17310.md")
</div>
<p>In this example, requests to <code>example.com/blog/</code> will serve the <code>index.html</code> file, and requests to <code>example.com/blog/posts/post1</code> will serve the <code>post1.html</code> file.</p>
<p>If you have a file outside the configured path, it will not be served, unless it is part of the <code>assets.not_found_handling</code> for <a href="/workers/static-assets/routing/single-page-application/">Single Page Applications</a> or <a href="/workers/static-assets/routing/static-site-generation/">custom 404 pages</a>. For example, if you have a <code>home.html</code> file in the root of your asset directory, it will not be served when requesting <code>example.com/blog/home</code>. However, if needed, these files can still be manually fetched over <a href="/workers/static-assets/binding/#binding">the binding</a>.</p>
