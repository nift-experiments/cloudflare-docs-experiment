<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 29, 2024</time><h2 id="post-title">Faster Workers Builds with Build Caching and Watch Paths</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/workers/platform/ci-cd/workers-build-caching.png" alt="Build caching settings" />
<img src="/assets/upstream/images/workers/platform/ci-cd/workers-build-watch-paths.png" alt="Build watch path settings" /></p>
<p><a href="/workers/ci-cd/builds/"><strong>Workers Builds</strong></a>, the integrated CI/CD system for Workers (currently in beta), now lets you cache artifacts across builds, speeding up build jobs by eliminating repeated work, such as downloading dependencies at the start of each build.</p>
<ul>
<li>
<p><strong><a href="/workers/ci-cd/builds/build-caching/">Build Caching</a></strong>: Cache dependencies and build outputs between builds with a shared project-wide cache, ensuring faster builds for the entire team.</p>
</li>
<li>
<p><strong><a href="/workers/ci-cd/builds/build-watch-paths/">Build Watch Paths</a></strong>: Define paths to include or exclude from the build process, ideal for <a href="/workers/ci-cd/builds/advanced-setups/#monorepos">monorepos</a> to target only the files that need to be rebuilt per Workers project.</p>
</li>
</ul>
<p>To get started, select your Worker on the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> then go to <strong>Settings</strong> &gt; <strong>Builds</strong>, and connect a GitHub or GitLab repository. Once connected, you'll see options to configure Build Caching and Build Watch Paths.</p>
</div></article></div>
