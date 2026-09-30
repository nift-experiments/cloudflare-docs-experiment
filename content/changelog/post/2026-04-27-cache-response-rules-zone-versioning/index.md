<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 27, 2026</time><h2 id="post-title">Cache Response Rules now support zone versioning</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>Cache Response Rules now work with <a href="/version-management/">Version Management</a>. You can version response-phase cache settings and promote them through environments, just like Cache Rules and other supported configurations.</p>
<h4 id="what-changed">What changed</h4>
<p>Previously, Cache Response Rules were excluded from zone versioning. Any response-phase rule you created applied globally across all environments with no way to test changes in staging first. Cache Rules already supported versioning, but the response phase, where you modify <code>Cache-Control</code> directives, manage cache tags, and strip headers, did not.</p>
<p>Cache Response Rules are now fully integrated with Version Management. You can create or modify response-phase rules within a version, and those changes stay scoped to that version until promoted.</p>
<h4 id="benefits">Benefits</h4>
<ul>
<li><strong>Safe rollout of cache behavior changes</strong>: Test response-phase rules in a staging environment before promoting to production. Catch unintended caching side effects early.</li>
<li><strong>Parity with Cache Rules</strong>: Cache Response Rules now follow the same versioning workflow as Cache Rules, so you can manage all cache configuration through a single promotion pipeline.</li>
<li><strong>Independent environment control</strong>: Run different response-phase cache settings per environment. For example, strip <code>Set-Cookie</code> headers in staging to validate cacheability without affecting production traffic.</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>Configure Cache Response Rules in the <a href="https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules">Cloudflare dashboard</a> under <strong>Caching</strong> &gt; <strong>Cache Rules</strong>, or via the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a>. For more details, refer to the <a href="/cache/how-to/cache-response-rules/">Cache Response Rules documentation</a> and the <a href="/version-management/">Version Management documentation</a>.</p>
</div></article></div>
