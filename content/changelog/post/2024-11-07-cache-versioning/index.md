<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 7, 2024</time><h2 id="post-title">Stage and test cache configurations safely</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now stage and test cache configurations before deploying them to production. Versioned environments let you safely validate cache rules, purge operations, and configuration changes without affecting live traffic.</p>
<h4 id="how-it-works">How it works</h4>
<p>With versioned environments, you can:</p>
<ol>
<li><strong>Create staging versions</strong> of your cache configuration.</li>
<li><strong>Test cache rules</strong> in a non-production environment.</li>
<li><strong>Purge staged content</strong> independently from production.</li>
<li><strong>Validate changes</strong> before promoting to production.</li>
</ol>
<p>This capability integrates with Cloudflare's broader <a href="/version-management/">versioning system</a>, allowing you to manage cache configurations alongside other zone settings.</p>
<h4 id="benefits">Benefits</h4>
<ul>
<li><strong>Risk-free testing</strong>: Validate configuration changes without impacting production.</li>
<li><strong>Independent purging</strong>: Clear staging cache without affecting live content.</li>
<li><strong>Deployment confidence</strong>: Catch issues before they reach end users.</li>
<li><strong>Team collaboration</strong>: Multiple team members can work on different versions.</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>To get started, refer to the <a href="/version-management/">version management documentation</a>.</p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="important-limitation">Important limitation</h4>
@markup("md", "content/.markup/bodies/17701.md")</aside>
</div></article></div>
