<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 25, 2026</time><h2 id="post-title">No config? No problem. Just `wrangler deploy`</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now deploy any existing project to Cloudflare Workers — even without a Wrangler configuration file — and <code>wrangler deploy</code> will <em>just work</em>.</p>
<p>Starting with Wrangler <strong>4.68.0</strong>, running <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> <a href="/workers/framework-guides/automatic-configuration/">automatically configures your project</a> by detecting your framework, installing required adapters, and deploying it to Cloudflare Workers.</p>
<h4 id="using-wrangler-locally">Using Wrangler locally</h4>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>When you run <code>wrangler deploy</code> in a project without a configuration file, Wrangler:</p>
<ol>
<li>Detects your framework from <code>package.json</code></li>
<li>Prompts you to confirm the detected settings</li>
<li>Installs any required adapters</li>
<li>Generates a <code>wrangler.jsonc</code> <a href="/workers/wrangler/configuration/">configuration file</a></li>
<li>Deploys your project to Cloudflare Workers</li>
</ol>
<p>You can also use <a href="/workers/wrangler/commands/general/#setup"><code>wrangler setup</code></a> to configure without deploying, or pass <a href="/workers/wrangler/commands/general/#deploy"><code>--yes</code></a> to skip prompts.</p>
<h4 id="using-the-cloudflare-dashboard">Using the Cloudflare dashboard</h4>
<p><img src="/assets/upstream/images/workers/ci-cd/builds/automatic-pr.png" alt="Automatic configuration pull request created by Workers Builds" /></p>
<p>When you connect a repository through the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create">Workers dashboard</a>, a <a href="/workers/ci-cd/builds/automatic-prs/">pull request is generated</a> for you with all necessary files, and a <a href="/workers/versions-and-deployments/preview-urls/">preview deployment</a> to check before merging.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17800.md")</aside>
<h4 id="background">Background</h4>
<p>In December 2025, we <a href="/changelog/2025-12-16-wrangler-autoconfig/">introduced automatic configuration</a> as an experimental feature. It is now generally available and the default behavior.</p>
<p>If you have questions or run into issues, join the <a href="https://github.com/cloudflare/workers-sdk/discussions/11667">GitHub discussion</a>.</p>
</div></article></div>
