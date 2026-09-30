<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 17, 2025</time><h2 id="post-title">Preview URLs now default to opt-in</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>To prevent the accidental exposure of applications, we've updated how <a href="/workers/versions-and-deployments/preview-urls/">Worker preview URLs</a> (<code>&lt;PREVIEW&gt;-&lt;WORKER_NAME&gt;.&lt;SUBDOMAIN&gt;.workers.dev</code>) are handled. We made this change to ensure preview URLs are only active when intentionally configured, improving the default security posture of your Workers.</p>
<h4 id="one-time-update-for-workers-with-workers-dev-disabled">One-Time Update for Workers with workers.dev Disabled</h4>
We performed a one-time update to disable preview URLs for existing Workers where the [workers.dev subdomain](/workers/configuration/routing/workers-dev/) was also disabled.
<p>Because preview URLs were historically enabled by default, users who had intentionally disabled their workers.dev route may not have realized their Worker was still accessible at a separate preview URL. This update was performed to ensure that using a preview URL is always an intentional, opt-in choice.</p>
<p>If your Worker was affected, its preview URL (<code>&lt;PREVIEW&gt;-&lt;WORKER_NAME&gt;.&lt;SUBDOMAIN&gt;.workers.dev</code>) will now direct to an informational page explaining this change.</p>
<p><strong>How to Re-enable Your Preview URL</strong></p>
<p>If your preview URL was disabled, you can re-enable it <a href="/workers/versions-and-deployments/preview-urls/#toggle-preview-urls-enable-or-disable">via the Cloudflare dashboard</a> by navigating to your Worker's Settings page and toggling on the Preview URL.</p>
<p>Alternatively, you can use Wrangler by adding the <code>preview_urls = true</code> setting to your Wrangler file and redeploying the Worker.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17788.md")</div>
<p><strong>Note:</strong> You can set <code>preview_urls = true</code> with any Wrangler version that supports the preview URL flag (v3.91.0+). However, we recommend updating to v4.34.0 or newer, as this version defaults <code>preview_urls</code> to false, ensuring preview URLs are always enabled by explicit choice.</p>
</div></article></div>
