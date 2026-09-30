<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 14, 2025</time><h2 id="post-title">Workers per-branch preview URLs now support long branch names</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We've updated <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a> for Cloudflare Workers to support long branch names.</p>
<p>Previously, branch and Worker names exceeding the 63-character DNS limit would cause alias generation to fail, leaving pull requests without aliased preview URLs. This particularly impacted teams relying on descriptive branch naming.</p>
<p>Now, Cloudflare automatically truncates long branch names and appends a unique hash, ensuring every pull request gets a working preview link.</p>
<h4 id="how-it-works">How it works</h4>
<ul>
<li><strong>63 characters or less</strong>: <code>&lt;branch-name&gt;-&lt;worker-name&gt;</code> → Uses actual branch name as is</li>
<li><strong>64 characters or more</strong>: <code>&lt;truncated-branch-name&gt;--&lt;hash&gt;-&lt;worker-name&gt;</code> → Uses truncated name with 4-character hash</li>
<li><strong>Hash generation</strong>: The hash is derived from the full branch name to ensure uniqueness</li>
<li><strong>Stable URLs</strong>: The same branch always generates the same hash across all commits</li>
</ul>
<h4 id="requirements-and-compatibility">Requirements and compatibility</h4>
<ul>
<li><strong>Wrangler 4.30.0 or later</strong>: This feature requires updating to wrangler@4.30.0+</li>
<li><strong>No configuration needed</strong>: Works automatically with existing preview URL setups</li>
</ul>
</div></article></div>
