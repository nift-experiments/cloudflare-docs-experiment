<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 1, 2026</time><h2 id="post-title">Deploy Hooks are now available for Workers Builds</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/ci-cd/builds/">Workers Builds</a> now supports Deploy Hooks — trigger builds from your headless CMS, a Cron Trigger, a Slack bot, or any system that can send an HTTP request.</p>
<p>Each Deploy Hook is a unique URL tied to a specific branch. Send it a <code>POST</code> and your Worker builds and deploys.</p>
<pre><code class="language-sh">curl -X POST &quot;https://api.cloudflare.com/client/v4/workers/builds/deploy_hooks/&lt;DEPLOY_HOOK_ID&gt;&quot;&#10;</code></pre>
<p>To create one, go to <strong>Workers &amp; Pages</strong> &gt; your Worker &gt; <strong>Settings</strong> &gt; <strong>Builds</strong> &gt; <strong>Deploy Hooks</strong>.</p>
<p>Since a Deploy Hook is a URL, you can also call it from another Worker. For example, a Worker with a <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> can rebuild your project on a schedule:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17803.md")</div>
<p>You can also use Deploy Hooks to <a href="/workers/ci-cd/builds/deploy-hooks/#cms-integration">rebuild when your CMS publishes new content</a> or <a href="/workers/ci-cd/builds/deploy-hooks/#deploy-from-a-slack-slash-command">deploy from a Slack slash command</a>.</p>
<h4 id="built-in-optimizations">Built-in optimizations</h4>
<ul>
<li><strong>Automatic deduplication</strong>: If a Deploy Hook fires multiple times before the first build starts running, redundant builds are automatically skipped. This keeps your build queue clean when webhooks retry or CMS events arrive in bursts.</li>
<li><strong>Last triggered</strong>: The dashboard shows when each hook was last triggered.</li>
<li><strong>Build source</strong>: Your Worker's build history shows which Deploy Hook started each build by name.</li>
</ul>
<p>Deploy Hooks are rate limited to 10 builds per minute per Worker and 100 builds per minute per account. For all limits, see <a href="/workers/ci-cd/builds/limits-and-pricing/">Limits &amp; pricing</a>.</p>
<p>To get started, read the <a href="/workers/ci-cd/builds/deploy-hooks/">Deploy Hooks documentation</a>.</p>
</div></article></div>
