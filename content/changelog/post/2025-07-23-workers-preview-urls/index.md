<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 22, 2025</time><h2 id="post-title">Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Now, when you connect your Cloudflare Worker to a git repository on GitHub or GitLab, each branch of your repository has its own stable preview URL, that you can use to preview code changes before merging the pull request and deploying to production.</p>
<p>This works the same way that Cloudflare Pages does — every time you create a pull request, you'll automatically get a shareable preview link where you can see your changes running, without affecting production. The link stays the same, even as you add commits to the same branch.
These preview URLs are named after your branch and are posted as a comment to each pull request. The URL stays the same with every commit and always points to the latest version of that branch.</p>
<p><img src="/assets/upstream/images/changelog/workers/preview-urls-comment.png" alt="PR comment preview" /></p>
<h4 id="preview-url-types">Preview URL types</h4>
<p>Each comment includes <strong>two preview URLs</strong> as shown above:</p>
<ul>
<li><strong>Commit Preview URL</strong>: Unique to the specific version/commit (e.g., <code>&lt;version-prefix&gt;-&lt;worker-name&gt;.&lt;subdomain&gt;.workers.dev</code>)</li>
<li><strong>Branch Preview URL</strong>: A stable alias based on the branch name (e.g., <code>&lt;branch-name&gt;-&lt;worker-name&gt;.&lt;subdomain&gt;.workers.dev</code>)</li>
</ul>
<h4 id="how-it-works">How it works</h4>
<p>When you create a pull request:</p>
<ul>
<li><strong>A preview alias is automatically created</strong> based on the Git branch name (e.g., <code>&lt;branch-name&gt;</code> becomes <code>&lt;branch-name&gt;-&lt;worker-name&gt;.&lt;subdomain&gt;.workers.dev</code>)</li>
<li><strong>No configuration is needed</strong>, the alias is generated for you</li>
<li><strong>The link stays the same</strong> even as you add commits to the same branch</li>
<li><strong>Preview URLs are posted directly to your pull request as comments</strong> (just like they are in Cloudflare Pages)</li>
</ul>
<h4 id="custom-alias-name">Custom alias name</h4>
<p>You can also assign a custom preview alias using the <a href="/workers/wrangler/">Wrangler CLI</a>, by passing the <code>--preview-alias</code> flag when <a href="/workers/wrangler/commands/general/#versions-upload">uploading a version</a> of your Worker:</p>
<pre><code class="language-bash">wrangler versions upload --preview-alias staging&#10;</code></pre>
<h4 id="limitations-while-in-beta">Limitations while in beta</h4>
<ul>
<li>Only available on the <strong>workers.dev</strong> subdomain (custom domains not yet supported)</li>
<li>Requires <strong>Wrangler v4.21.0+</strong></li>
<li>Preview URLs are not generated for Workers that use <a href="/durable-objects/">Durable Objects</a></li>
<li>Not yet supported for <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a></li>
</ul>
</div></article></div>
