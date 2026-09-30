<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 23, 2025</time><h2 id="post-title">Workers Preview URL default behavior now matches your workers.dev setting</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We have updated the default behavior for Cloudflare Workers <a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a>. <strong>Going forward, if a preview URL setting is not <a href="/workers/versions-and-deployments/preview-urls/#toggle-preview-urls-enable-or-disable">explicitly configured</a> during deployment, its default behavior will automatically match the setting of your <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code> subdomain</a>.</strong></p>
<p>This change is intended to provide a more intuitive and secure experience by aligning your preview URL's default state with your <code>workers.dev</code> configuration to prevent cases where a preview URL might remain public even after you disabled your <code>workers.dev</code> route.</p>
<p><strong>What this means for you:</strong></p>
<ul>
<li><strong>If neither setting is configured:</strong> both the workers.dev route and the preview URL will default to enabled</li>
<li><strong>If your workers.dev route is enabled and you do not explicitly set Preview URLs to enabled or disabled:</strong> Preview URLs will default to enabled</li>
<li><strong>If your workers.dev route is disabled and you do not explicitly set Preview URLs to enabled or disabled:</strong> Preview URLs will default to disabled</li>
</ul>
<p>You can override the default setting by explicitly enabling or disabling the preview URL in your Worker's configuration through the <a href="/api/resources/workers/subresources/scripts/subresources/subdomain/">API</a>, <a href="/workers/versions-and-deployments/preview-urls/#from-the-dashboard">Dashboard</a>, or <a href="/workers/versions-and-deployments/preview-urls/#from-the-wrangler-configuration-file">Wrangler</a>.</p>
<p><strong>Wrangler Version Behavior</strong></p>
<p>The default behavior depends on the version of Wrangler you are using. This new logic applies to the latest version. Here is a summary of the behavior across different versions:</p>
<ul>
<li><strong>Before v4.34.0:</strong> Preview URLs defaulted to enabled, regardless of the workers.dev setting.</li>
<li><strong>v4.34.0 up to (but not including) v4.44.0:</strong> Preview URLs defaulted to disabled, regardless of the workers.dev setting.</li>
<li><strong>v4.44.0 or later:</strong> Preview URLs now default to matching your workers.dev setting.</li>
</ul>
<p><strong>Why we’re making this change</strong></p>
<p>In July, <a href="/changelog/2025-07-23-workers-preview-urls/">we introduced preview URLs to Workers</a>, which let you preview code changes before deploying to production. This made disabling your Worker’s workers.dev URL an ambiguous action — the preview URL, served as a subdomain of <code>workers.dev</code> (ex: <code>preview-id-worker-name.account-name.workers.dev</code>) would still be live even if you had disabled your Worker’s <code>workers.dev</code> route. If you misinterpreted what it meant to disable your <code>workers.dev</code> route, you might unintentionally leave preview URLs enabled when you didn’t mean to, and expose them to the public Internet.</p>
<p>To address this, we made a <a href="/changelog/2025-09-17-update-preview-url-setting/">one-time update</a> to disable preview URLs on existing Workers that had their workers.dev route disabled and changed the default behavior to be disabled for all new deployments where a preview URL setting was not explicitly configured.</p>
<p>While this change helped secure many customers, it was disruptive for customers who keep their <code>workers.dev</code> route enabled and actively use the preview functionality, as it now required them to explicitly enable preview URLs on every redeployment.This new, more intuitive behavior ensures that your preview URL settings align with your <code>workers.dev</code> configuration by default, providing a more secure and predictable experience.</p>
<p><strong>Securing access to <code>workers.dev</code> and preview URL endpoints</strong></p>
<p>To further secure your <code>workers.dev</code> subdomain and preview URL, you can <a href="/changelog/2025-10-03-one-click-access-for-workers/">enable Cloudflare Access with a single click</a> in your Worker's settings to limit access to specific users or groups.</p>
</div></article></div>
