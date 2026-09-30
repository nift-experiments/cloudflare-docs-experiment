<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 19, 2026</time><h2 id="post-title">Temporary accounts for AI agent deployments</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>AI agents can now deploy Workers to Cloudflare without first requiring a user to sign up, open a browser-based OAuth flow, click through the dashboard, or create an API token. When an agent tries to deploy without Cloudflare credentials, Wrangler can tell it to rerun with <code>--temporary</code>, then deploy the Worker to a temporary preview account.</p>
<p>To try this with your agent, update to Wrangler 4.102.0 or later, make sure you are logged out (<code>wrangler logout</code>), and then ask your agent to build something and deploy it to Cloudflare. The agent should follow Wrangler's output and deploy using the <code>--temporary</code> flag.</p>
<p><img src="/assets/upstream/images/workers/claim-deployments-flow.png" alt="Diagram showing an AI agent deploying, verifying, and redeploying a Worker to a temporary account, then claiming it after authentication and moving it to a permanent account" /></p>
<pre><code class="language-sh">wrangler deploy --temporary&#10;</code></pre>
<p>The temporary deployment stays live for 60 minutes. During that window, the agent can verify the Worker, redeploy changes, and return both the live Worker URL and claim URL. Opening the claim URL lets you sign in to or create a Cloudflare account and make the temporary account permanent.</p>
<p>Temporary preview accounts currently support a limited set of products, including Workers, Workers Static Assets, Workers KV, D1, Durable Objects, Hyperdrive, Queues, and SSL/TLS certificates. For supported products, limits, and claim behavior, refer to <a href="/workers/platform/claim-deployments/">Claim deployments (temporary accounts)</a>.</p>
<p>For more context, refer to <a href="https://blog.cloudflare.com/temporary-accounts/">Temporary Cloudflare Accounts for Agents</a>.</p>
</div></article></div>
