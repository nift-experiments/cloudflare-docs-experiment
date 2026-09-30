<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 8, 2025</time><h2 id="post-title">Deploy a Workers application in seconds with one-click</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now add a <a href="/workers/platform/deploy-buttons/">Deploy to Cloudflare</a> button to the README of your Git repository containing a Workers application — making it simple for other developers to quickly set up and deploy your project!</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/saas-admin-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>The Deploy to Cloudflare button:</p>
<ol>
<li><strong>Creates a new Git repository on your GitHub/ GitLab account</strong>: Cloudflare will automatically clone and create a new repository on your account, so you can continue developing.</li>
<li><strong>Automatically provisions resources the app needs</strong>: If your repository requires Cloudflare primitives like a <a href="/kv/">Workers KV namespace</a>, a <a href="/d1/">D1 database</a>, or an <a href="/r2/">R2 bucket</a>, Cloudflare will automatically provision them on your account and bind them to your Worker upon deployment.</li>
<li><strong>Configures Workers Builds (CI/CD)</strong>: Every new push to your production branch on your newly created repository will automatically build and deploy courtesy of <a href="/workers/ci-cd/builds/">Workers Builds</a>.</li>
<li><strong>Adds preview URLs to each pull request</strong>: If you'd like to test your changes before deploying, you can push changes to a <a href="/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds">non-production branch</a> and <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a> will be generated and <a href="/workers/ci-cd/builds/git-integration/github-integration/#pull-request-comment">posted back to GitHub as a comment</a>.</li>
</ol>
<p><img src="/assets/upstream/images/workers/dtw-user-flow.png" alt="Import repo or choose template" /></p>
<p>To create a Deploy to Cloudflare button in your README, you can add the following snippet, including your Git repository URL:</p>
<pre><code class="language-md">[<img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare">](https://deploy.workers.cloudflare.com/?url=&lt;YOUR_GIT_REPO_URL&gt;)&#10;</code></pre>
<p>Check out our <a href="/workers/platform/deploy-buttons/">documentation</a> for more information on how to set up a deploy button for your application and best practices to ensure a successful deployment for other developers.</p>
</div></article></div>
