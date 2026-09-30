<p class="article-summary">Allow a client to request static assets while waiting for the HTML response.</p>
<p>If you want to get started quickly, click on the button below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/103-early-hints"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.</p>
<p><code>103</code> Early Hints is an HTTP status code designed to speed up content delivery. When enabled, Cloudflare can cache the <code>Link</code> headers marked with preload and/or preconnect from HTML pages and serve them in a <code>103</code> Early Hints response before reaching the origin server. Browsers can use these hints to fetch linked assets while waiting for the origin’s final response, dramatically improving page load speeds.</p>
<p>To ensure Early Hints are enabled on your zone:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16582.md")
</div>
<p>You can return <code>Link</code> headers from a Worker running on your zone to speed up your page load times.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16587.md")
</div></div>
