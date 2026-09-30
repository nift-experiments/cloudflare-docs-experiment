<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 18, 2025</time><h2 id="post-title">Build image policies for Workers Builds and Cloudflare Pages</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We've published build image policies for <a href="/workers/ci-cd/builds/build-image/#build-image-policy">Workers Builds</a> and <a href="/pages/configuration/build-image/#build-image-policy">Cloudflare Pages</a>, which establish:</p>
<ul>
<li><strong>Minor version updates</strong>: We typically update preinstalled software to the latest available minor version without notice. For tools that don't follow semantic versioning (e.g., Bun or Hugo), we provide 3 months’ notice.</li>
<li><strong>Major version updates</strong>: Before preinstalled software reaches end-of-life, we update to the next stable LTS version with 3 months’ notice.</li>
<li><strong>Build image version deprecation (Pages only)</strong>: We provide 6 months’ notice before deprecation. Projects on v1 or v2 will be automatically moved to v3 on their specified deprecation dates.</li>
</ul>
<p>To prepare for updates, monitor the <a href="https://developers.cloudflare.com/changelog/">Cloudflare Changelog</a>, dashboard notifications, and email. You can also <a href="/workers/ci-cd/builds/build-image/#overriding-default-versions">override default versions</a> to maintain specific versions.</p>
</div></article></div>
