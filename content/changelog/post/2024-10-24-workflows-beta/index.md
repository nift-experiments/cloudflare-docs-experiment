<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 24, 2024</time><h2 id="post-title">Workflows is now in open beta</h2>
<div class="changelog-badges"><span>workers</span><span>workflows</span></div><div class="changelog-body"><p>Workflows is now in open beta, and available to any developer a free or paid Workers plan.</p>
<p>Workflows allow you to build multi-step applications that can automatically retry, persist state and run for minutes, hours, days, or weeks. Workflows introduces a programming model that makes it easier to build reliable, long-running tasks, observe as they progress, and programmatically trigger instances based on events across your services.</p>
<h4 id="get-started">Get started</h4>
<p>You can get started with Workflows by <a href="/workflows/get-started/guide/">following our get started guide</a> and/or using <code>npm create cloudflare</code> to pull down the starter project:</p>
<pre><code class="language-sh">npm create cloudflare@latest workflows-starter -- --template &quot;cloudflare/workflows-starter&quot;&#10;</code></pre>
<p>You can open the <code>src/index.ts</code> file, extend it, and use <code>wrangler deploy</code> to deploy your first Workflow. From there, you can:</p>
<ul>
<li>Learn the <a href="/workflows/build/workers-api/">Workflows API</a></li>
<li><a href="/workflows/build/trigger-workflows/">Trigger Workflows</a> via your Workers apps.</li>
<li>Understand the <a href="/workflows/build/rules-of-workflows/">Rules of Workflows</a> and how to adopt best practices</li>
</ul>
</div></article></div>
