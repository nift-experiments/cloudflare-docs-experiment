<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 4, 2026</time><h2 id="post-title">Node.js compatibility is now enabled by default</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers now enable the <code>nodejs_compat</code> and <code>nodejs_compat_v2</code> compatibility
flags by default for <a href="/workers/configuration/compatibility-dates/">compatibility dates</a>
of <code>2026-08-04</code> or later. These flags are not used for these compatibility
dates because the compatibility date enables the same behavior.</p>
<p>This means all <a href="/workers/runtime-apis/nodejs/">Node.js built-in APIs</a> supported
by the Workers runtime are available by default, including <code>node:crypto</code>,
<code>node:buffer</code>, <code>node:stream</code>, <code>node:net</code>, <code>node:dns</code>, <code>node:fs</code>, <code>node:http</code>,
and more. npm packages that depend on these APIs will work without additional
configuration.</p>
<p>Workers using an earlier compatibility date are not affected. They can still
opt in by adding <code>nodejs_compat</code> to <code>compatibility_flags</code>.</p>
<p>New projects do not need to add either flag. Existing projects can update their
compatibility date without removing them. Wrangler, Miniflare, the Cloudflare
Vite plugin, and Vitest Pool Workers ignore these redundant flags when starting
the runtime.</p>
<p>To turn off Node.js compatibility completely, remove any <code>nodejs_compat</code> and
<code>nodejs_compat_v2</code> flags. Then add both of the following flags:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17813.md")</div>
<p>For more information, refer to the <a href="/workers/runtime-apis/nodejs/">Node.js compatibility documentation</a>.</p>
</div></article></div>
