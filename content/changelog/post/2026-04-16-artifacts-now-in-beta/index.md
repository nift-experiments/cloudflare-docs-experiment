<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 16, 2026</time><h2 id="post-title">Artifacts now in beta: versioned filesystem with Git access</h2>
<div class="changelog-badges"><span>artifacts</span></div><div class="changelog-body"><p><a href="/artifacts/">Artifacts</a> is now in private beta. Artifacts is Git-compatible storage built for scale: create tens of millions of repos, fork from any remote, and hand off a URL to any Git client. It provides a versioned filesystem for storing and exchanging file trees across Workers, the REST API, and any Git client, running locally or within an agent.</p>
<p>You can <a href="https://blog.cloudflare.com/artifacts-git-for-agents-beta/">read the announcement blog</a> to learn more about what Artifacts does, how it works, and how to create repositories for your agents to use.</p>
<p>Artifacts has three API surfaces:</p>
<ul>
<li>Workers bindings (for creating and managing repositories)</li>
<li>REST API (for creating and managing repos from any other compute platform)</li>
<li>Git protocol (for interacting with repos)</li>
</ul>
<p>As an example: you can use the Workers binding to create a repo and read back its remote URL:</p>
<pre><code class="language-ts">&#35; Create a thousand, a million or ten million repos: one for every agent, for every upstream branch, or every user.&#10;const created = await env.PROD_ARTIFACTS.create(&quot;agent-007&quot;);&#10;const remote = (await created.repo.info())?.remote;&#10;</code></pre>
<p>Or, use the REST API to create a repo inside a namespace from your agent(s) running on any platform:</p>
<pre><code class="language-bash">curl --request POST &quot;https://artifacts.cloudflare.net/v1/api/namespaces/some-namespace/repos&quot; --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; --header &quot;Content-Type: application/json&quot; --data &#x27;{&quot;name&quot;:&quot;agent-007&quot;}&#x27;&#10;</code></pre>
<p>Any Git client that speaks smart HTTP can use the returned remote URL:</p>
<pre><code class="language-bash">&#35; Agents know git.&#10;&#35; Every repository can act as a git repo, allowing agents to interact with Artifacts the way they know best: using the git CLI.&#10;git clone https://x:${REPO_TOKEN}@artifacts.cloudflare.net/some-namespace/agent-007.git&#10;</code></pre>
<p>To learn more, refer to <a href="/artifacts/get-started/">Get started</a>, <a href="/artifacts/api/workers-binding/">Workers binding</a>, and <a href="/artifacts/api/git-protocol/">Git protocol</a>.</p>
</div></article></div>
