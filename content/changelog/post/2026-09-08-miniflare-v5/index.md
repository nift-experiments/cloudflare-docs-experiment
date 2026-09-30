<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 8, 2026</time><h2 id="post-title">Miniflare v5 prepares local development for the cf CLI</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Miniflare v5 prepares Cloudflare local development tooling for the upcoming <code>cf</code> CLI.</p>
<p>Miniflare powers local Workers development behind <code>wrangler dev</code>, the Cloudflare Vite plugin, and <code>@cloudflare/vitest-plugin</code>.
Most projects should use those tools instead of depending on Miniflare directly, and Miniflare v5 will not require any action.</p>
<p>The most significant change is a new configuration shape which aligns Miniflare with <code>cloudflare.config.ts</code>, the programmatic Cloudflare configuration format now available for testing.</p>
<p>Other breaking changes include:</p>
<ul>
<li>Removed deprecated APIs and options, such as legacy alpha D1 bindings.</li>
<li>Removed now-unused, internal APIs like <code>wrappedBindings</code></li>
<li>Removed Miniflare's built-in module discovery; higher-level tools like Wrangler and the Vite plugin should be providing the module graph.</li>
<li>Moved local-only /cdn-cgi routes under /cdn-cgi/local.</li>
<li>Replaced per-resource persistence options with shared persistence root options.</li>
</ul>
<p>For a more comprehensive list, refer to <a href="https://github.com/cloudflare/workers-sdk/blob/main/packages/miniflare/CHANGELOG.md#5202607300-alpha">Miniflare's changelog</a></p>
<p>This work sets up a cleaner foundation for the next generation of local development tooling, including the new <code>cf</code> CLI.</p>
</div></article></div>
