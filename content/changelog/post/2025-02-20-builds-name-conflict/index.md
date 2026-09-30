<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 20, 2025</time><h2 id="post-title">Autofix Worker name configuration errors at build time</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/workers/platform/ci-cd/gh-auto-pr-name.png" alt="Auto-fixing Workers Name in Git Repo" /></p>
<p>Small misconfigurations shouldn’t break your deployments. Cloudflare is introducing automatic error detection and fixes in <a href="/workers/ci-cd/builds/">Workers Builds</a>, identifying common issues in your wrangler.toml or wrangler.jsonc and proactively offering fixes, so you spend less time debugging and more time shipping.</p>
<p>Here's how it works:</p>
<ol>
<li>Before running your build, Cloudflare checks your Worker's Wrangler configuration file (wrangler.toml or wrangler.jsonc) for common errors.</li>
<li>Once you submit a build, if Cloudflare finds an error it can fix, it will submit a pull request to your repository that fixes it.</li>
<li>Once you merge this pull request, Cloudflare will run another build.</li>
</ol>
<p>We're starting with fixing name mismatches between your Wrangler file and the Cloudflare dashboard, a top cause of build failures.</p>
<p>This is just the beginning, we want your feedback on what other errors we should catch and fix next. Let us know in the Cloudflare Developers Discord, <a href="https://discord.com/channels/595317990191398933/1064502845061210152">#workers-and-pages-feature-suggestions</a>.</p>
</div></article></div>
