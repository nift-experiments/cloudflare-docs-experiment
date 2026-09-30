<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 4, 2026</time><h2 id="post-title">Build and deploy Artifacts repos on every push</h2>
<div class="changelog-badges"><span>artifacts</span><span>workflows</span></div><div class="changelog-body"><p>You can now run your CI/CD pipeline on your <a href="/artifacts/">Artifacts</a> repo by defining a CI <a href="/workflows/">Workflow</a> with the <a href="https://github.com/cloudflare/ci">CI SDK</a>, automatically triggered on Artifacts push events.</p>
<p>This allows you to:</p>
<ul>
<li>Automatically build and deploy application code stored in Artifacts.</li>
<li>Run linting, type checking, tests, and other checks on every push.</li>
<li>Reuse dependencies when the lockfile (i.e. <code>pnpm-lock.yaml</code>) has not changed.</li>
<li>Stop deployment when a check or build fails.</li>
<li>Restrict API token access to the deployment step.</li>
<li>Deploy the output to a <a href="/workers/">Worker</a> or a <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> User Worker.</li>
</ul>
<p>Define your CI steps with <code>@cloudflare/ci</code>. Each <code>ci.runner()</code> spins up an isolated sandbox, and the <code>cache</code> option reuses installed dependencies across each sandboxed step in your CI job.</p>
<p>Point <code>cache.inputs</code> at your lockfile (i.e. <code>pnpm-lock.yaml</code>, <code>bun.lock</code>), and the install step only runs again when that lockfile changes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17690.md")</div>
<p>To start the Workflow automatically after each push, add a <code>cf.artifacts.repo.pushed</code> trigger to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17691.md")</div>
<p>To learn more, refer to <a href="/artifacts/guides/build-and-deploy-on-push/">Build and deploy Artifacts repos</a>.</p>
</div></article></div>
