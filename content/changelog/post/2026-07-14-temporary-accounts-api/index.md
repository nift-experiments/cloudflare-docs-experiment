<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 14, 2026</time><h2 id="post-title">Platforms can now create Temporary Accounts via the Cloudflare API</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Platforms can now create temporary preview accounts through the Cloudflare REST API. This lets your platform deploy a live Worker before the user signs in to Cloudflare.</p>
<p>With the Temporary Accounts API, coding agents, AI app builders, and other platforms can build a similar flow for generated Workers and supported resources.</p>
<p>Your platform can keep users in its onboarding flow while they generate, deploy, and test an application. Users do not need an existing Cloudflare account, and your platform does not need write access to one.</p>
<p><img src="/assets/upstream/images/workers/claim-deployments-flow.png" alt="Diagram showing an AI agent deploying, verifying, and redeploying a Worker in a temporary account, then a user authenticating and claiming the account to keep its resources" /></p>
<p>The API returns a claim URL that lets the user make the temporary account and its resources permanent.</p>
<p><a href="https://www.cloudflare.com/drop/">Cloudflare Drop</a> demonstrates this preview-and-claim pattern for static sites. Someone can upload a site, test and share it for one hour, then sign in or create an account only when they want to keep it.</p>
<p>This API expands the flow first introduced with <a href="/changelog/post/2026-06-19-temporary-accounts-for-agents/"><code>wrangler deploy --temporary</code></a>. Your backend now controls the provisioning and deployment experience directly:</p>
<ol>
<li>Show Cloudflare's Terms of Service and Privacy Policy in your product, and require the user to accept them.</li>
<li>Request and solve a proof-of-work challenge.</li>
<li>Create a temporary preview account.</li>
<li>Deploy with the returned temporary account ID and API token.</li>
<li>Show the deployed Worker URL and claim URL to the user.</li>
</ol>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/provisioning/previews/challenge&quot; \&#10;  &#45;X POST \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{}&#x27;&#10;&#10;curl &quot;https://api.cloudflare.com/client/v4/provisioning/previews&quot; \&#10;  &#45;X POST \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;termsOfService&quot;: &quot;https://www.cloudflare.com/terms/&quot;,&#10;    &quot;privacyPolicy&quot;: &quot;https://www.cloudflare.com/privacypolicy/&quot;,&#10;    &quot;acceptTermsOfService&quot;: &quot;yes&quot;,&#10;    &quot;challengeToken&quot;: &quot;&lt;CHALLENGE_TOKEN&gt;&quot;,&#10;    &quot;solution&quot;: {&#10;      &quot;checkpoints&quot;: &quot;&lt;BASE64_CHECKPOINTS&gt;&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>For the complete API flow, proof-of-work requirements, supported products, and limits, refer to <a href="/workers/platform/claim-deployments/#integrate-with-the-rest-api">Claim deployments (temporary accounts)</a>. For the background and design goals behind this flow, refer to <a href="https://blog.cloudflare.com/temporary-accounts/">Temporary Cloudflare Accounts for AI agents</a>.</p>
</div></article></div>
