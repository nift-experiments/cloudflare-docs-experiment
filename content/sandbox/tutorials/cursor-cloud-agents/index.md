---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/tutorials/cursor-cloud-agents/
  description: Deploy Cursor self-hosted machines that run each assigned session in an isolated Cloudflare container.
  full_title: Run Cursor Cloud Agents on Cloudflare via self-hosted machines · Cloudflare Sandbox SDK docs
  head_html: <title>Run Cursor Cloud Agents on Cloudflare via self-hosted machines · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy Cursor self-hosted machines that run each assigned session in an isolated Cloudflare container."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/tutorials/cursor-cloud-agents/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/tutorials/cursor-cloud-agents/index.md"><meta property="og:title" content="Run Cursor Cloud Agents on Cloudflare via self-hosted machines · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy Cursor self-hosted machines that run each assigned session in an isolated Cloudflare container."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/tutorials/cursor-cloud-agents/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Sandbox SDK,Containers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/tutorials/cursor-cloud-agents/#page","headline":"Run Cursor Cloud Agents on Cloudflare via self-hosted machines \u00b7 Cloudflare Sandbox SDK docs","description":"Deploy Cursor self-hosted machines that run each assigned session in an isolated Cloudflare container.","url":"https://developers.cloudflare.com/sandbox/tutorials/cursor-cloud-agents/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/tutorials/cursor-cloud-agents/
  schema: 1
---
<p>Run Cursor Cloud Agents on Cloudflare via <a href="https://cursor.com/docs/cloud-agent/self-hosted">self-hosted machines</a>. Each Cursor session assigned to the deployment runs in an isolated container backed by Cloudflare Containers.</p>
<p>Cursor hosts the agent loop, inference, and planning. Cloudflare runs commands, file edits, repository operations, and other tools inside infrastructure that you control.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need:</p>
<ul>
<li>A Cursor Enterprise plan with self-hosted machines enabled</li>
<li>A Cursor team service-account API key with agent scope</li>
<li>A Cloudflare Workers Paid account with access to Containers and R2</li>
<li><a href="https://nodejs.org/">Node.js 20</a> or later</li>
<li>A running <a href="https://www.docker.com/">Docker</a> daemon for deployment and local development</li>
</ul>
<h3 id="configure-a-cursor-team-pool">Configure a Cursor team pool</h3>
<p>To create a team pool, set <code>CURSOR_API_KEY</code> in your shell. Then, start a local worker with the Cursor Agent CLI:</p>
<pre tabindex="0"><code class="language-sh">CURSOR_API_KEY=&quot;$CURSOR_API_KEY&quot; agent worker --pool cloudflare-test start&#10;</code></pre>
<p>The command registers the pool and temporarily connects your local machine as a worker. After the pool appears in Cursor, stop the worker with <code>Ctrl+C</code> and run <code>unset CURSOR_API_KEY</code>. Record the pool name for <code>CURSOR_POOL</code>. Keep the local worker stopped while testing the Cloudflare deployment so it does not claim the agent request.</p>
<p>For more information, refer to <a href="https://cursor.com/docs/cloud-agent/self-hosted-guides/pool">Cursor team pools</a>.</p>
<h2 id="deploy-the-template">Deploy the template</h2>
<p>The template deploys a Worker, a Durable Object namespace, a container application, an R2 bucket binding, and a cron trigger.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13320.md")
</div>
<h2 id="run-a-repository-bound-agent">Run a repository-bound agent</h2>
<p>Repository-bound agents route work by Git remote. The team pool name provides an additional routing constraint.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13321.md")
</div>
<p>The request provides the repository URL. The container restores or clones that repository into <code>$HOME/workspaces/repo-0</code>. It then starts the Cursor worker:</p>
<pre tabindex="0"><code class="language-sh">agent worker --worker-dir &quot;$HOME/workspaces/repo-0&quot; --pool &quot;$CURSOR_POOL&quot; start --verbose&#10;</code></pre>
<p>The Cursor worker derives its repository label from the Git remote. Do not configure <code>repo=</code> labels manually.</p>
<h2 id="run-an-any-repository-agent">Run an any-repository agent</h2>
<p>Any-repository agents route work by team pool name. They start with an empty working directory and no Git remote.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13322.md")
</div>
<p>The container creates <code>$HOME/workspaces/repo-0</code> without a Git remote. The agent or a project hook can clone a repository during the session.</p>
<h2 id="configure-repository-snapshots">Configure repository snapshots</h2>
<p>Repository snapshots are an optional cache for repository-bound agents. A snapshot stores the post-clone working tree in R2. An any-repository agent does not use this cache.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13323.md")
</div>
<p>A cache miss performs a normal Git clone. It does not prevent the agent from starting.</p>
<h2 id="how-the-template-works">How the template works</h2>
<p>The template manages one container for each assigned Cursor session:</p>
<ul>
<li><strong>List:</strong> A cron trigger runs every five minutes. The Worker lists sessions waiting for <code>CURSOR_POOL</code>.</li>
<li><strong>Stream:</strong> The Worker holds Cursor's server-sent events stream open until the next scheduled run.</li>
<li><strong>Assign:</strong> The Worker accepts a waiting session with a unique worker ID. Cursor assigns that session exclusively to the Worker, which prevents duplicate processing.</li>
<li><strong>Start:</strong> A Durable Object starts one container with the session environment and repository information.</li>
<li><strong>Stop:</strong> The container exits after the configured idle timeout. The Durable Object also enforces a maximum run lifetime.</li>
</ul>
<p>The container opens an outbound connection to Cursor. The container does not require an inbound port or public IP address.</p>
<p>The Worker only exposes its health and optional snapshot routes. Cursor remains responsible for the agent loop and session orchestration.</p>
<h2 id="monitor-the-deployment">Monitor the deployment</h2>
<p>To stream controller and container logs, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler tail&#10;</code></pre>
<p>To list container instances, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler containers list&#10;</code></pre>
<p>To test one scheduled controller run during local development, start <code>wrangler</code> with scheduled-event testing:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev --test-scheduled&#10;</code></pre>
<p>In another terminal, invoke the scheduled route:</p>
<pre tabindex="0"><code class="language-sh">curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?cron=*/5+*+*+*+*&quot;&#10;</code></pre>
<p>If you change the cron interval, update both <code>triggers.crons</code> in <code>wrangler.jsonc</code> and <code>CONTROLLER_RUN_BUDGET_MS</code> in <code>src/config.ts</code>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<table>
<thead>
<tr>
<th>Symptom</th>
<th>Cause</th>
<th>Resolution</th>
</tr>
</thead>
<tbody>
<tr>
<td>No sessions are assigned</td>
<td>The cron does not run, the key is missing, or the team pool name does not match</td>
<td>Run <code>npx wrangler tail</code>. Check controller runs, <code>401</code> responses, and the configured team pool name.</td>
</tr>
<tr>
<td>The controller returns <code>401</code></td>
<td>The key is personal or lacks agent scope</td>
<td>Replace <code>CURSOR_API_KEY</code> with a team service-account key that has agent scope.</td>
</tr>
<tr>
<td>The team pool is absent for a repo</td>
<td>The worker started without repository labels</td>
<td>Select <strong>Any repo</strong>, or start a repository-bound agent with a configured Git remote.</td>
</tr>
<tr>
<td>The session is assigned but does not start</td>
<td>The container cannot start, clone the repository, or authenticate</td>
<td>Run <code>npx wrangler containers list</code> and inspect <code>npx wrangler tail</code>. Check capacity and Git secrets.</td>
</tr>
<tr>
<td>The container exits with <code>Error: Container exited with unexpected exit code: 1</code> and an earlier log reports <code>cursor-agent CLI not found on PATH</code></td>
<td>Cloudflare WARP or another TLS-inspecting proxy may have prevented Docker from downloading the Cursor CLI. An unguarded shell pipeline can hide the installation failure and produce an incomplete image.</td>
<td>Run <code>npx wrangler tail</code> and inspect the preceding container logs. If the Cursor CLI is missing, disconnect WARP, clear the Docker build cache, and run <code>npx wrangler deploy</code> again. Alternatively, configure Docker to trust your organization's root certificate.</td>
</tr>
<tr>
<td>The first repository start is slow</td>
<td>The snapshot cache is empty or not configured</td>
<td>Configure both <code>WORKER_PUBLIC_URL</code> and <code>SNAPSHOT_AUTH_TOKEN</code>, or allow a cold Git clone.</td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://github.com/anysphere/cloudflare-workers">Cursor Cloudflare Workers template</a></li>
<li><a href="https://cursor.com/docs/cloud-agent/self-hosted">Cursor self-hosted machines overview</a></li>
<li><a href="https://cursor.com/docs/cloud-agent/self-hosted-guides/pool">Cursor team pools</a></li>
<li><a href="/containers/">Cloudflare Containers</a></li>
<li><a href="/r2/">R2</a></li>
</ul>
