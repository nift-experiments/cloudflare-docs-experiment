---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/artifacts/
  description: '2026-08-13'
  full_title: artifacts changelog | Cloudflare Docs
  head_html: <title>artifacts changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-08-13"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/artifacts/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="artifacts changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-08-13"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/artifacts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/artifacts/#page","headline":"artifacts changelog | Cloudflare Docs","description":"2026-08-13","url":"https://developers.cloudflare.com/changelog/product/artifacts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/artifacts/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="data-localization-support-for-artifacts"><a href="/changelog/post/2026-08-13-artifacts-jurisdictions/">Data localization support for Artifacts</a></h2>
<p><em>2026-08-13</em></p>
<p>Artifacts now supports jurisdictions, allowing you to select the European Union or the United States as the only location where repo data is stored and processed.</p>
<p>Select a jurisdiction when you create a namespace. Every repo in that namespace automatically uses the selected jurisdiction.</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;namespace&quot;: &quot;my-eu-namespace&quot;,&#10;    &quot;jurisdiction&quot;: &quot;eu&quot;&#10;  }&#x27;&#10;</code></pre>
<p>Jurisdictions cannot be changed after namespace creation. If you omit the jurisdiction, Artifacts creates an unrestricted namespace.</p>
<p>For supported jurisdictions and usage details, refer to <a href="/artifacts/guides/data-localization/">Data localization</a>.</p>


<h2 id="build-and-deploy-artifacts-repos-on-every-push"><a href="/changelog/post/2026-08-04-build-and-deploy-on-push/">Build and deploy Artifacts repos on every push</a></h2>
<p><em>2026-08-04</em></p>
<p>You can now run your CI/CD pipeline on your <a href="/artifacts/">Artifacts</a> repo by defining a CI <a href="/workflows/">Workflow</a> with the <a href="https://github.com/cloudflare/ci">CI SDK</a>, automatically triggered on Artifacts push events.</p>
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


<h2 id="manage-artifacts-from-the-cloudflare-dashboard"><a href="/changelog/post/2026-06-17-dashboard-management/">Manage Artifacts from the Cloudflare dashboard</a></h2>
<p><em>2026-06-17T12:00:00+00:00</em></p>
<p>You can now configure <a href="/artifacts/concepts/how-artifacts-works/">Artifacts</a> namespaces, repos, and tokens directly from the Cloudflare dashboard.</p>
<p>Artifacts is Git-compatible storage that lets you store repos on Cloudflare and interact with them using standard Git workflows.</p>
<p>You can view and create <a href="/artifacts/concepts/namespaces/#use-namespaces-as-containers">namespaces</a>, which are top-level containers for repos:</p>
<p><img src="/assets/upstream/images/changelog/artifacts/dashboard-namespaces.png" alt="Artifacts namespaces dashboard showing namespace search and create namespace controls" /></p>
<p>You can view, create, fork, and search repos within a namespace:</p>
<p><img src="/assets/upstream/images/changelog/artifacts/dashboard-repositories.png" alt="Artifacts repositories dashboard showing repo source, access, and created columns" /></p>
<p>You can open a repo to view its files and copy its Git remote URL.</p>
<p><img src="/assets/upstream/images/changelog/artifacts/dashboard-repo-overview.png" alt="Artifacts repository overview showing files, commits, token management, and quick actions" /></p>
<p>You can also provision tokens directly from the dashboard to scope Git access to a single repo, with read tokens for clone, fetch, and pull workflows, or write tokens when a client needs to push changes.</p>
<p>To get started, go to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select <strong>Storage &amp; databases</strong> &gt; <strong>Artifacts</strong>.</p>
<p>If you are enrolled in the Artifacts beta, you can use the dashboard to set up Artifacts. If you would like to join the beta, complete the <a href="https://forms.gle/DwBoPRa3CWQ8ajFp7">request form</a>.</p>


<h2 id="event-subscriptions-for-artifacts-lifecycle-events"><a href="/changelog/post/2026-05-19-event-subscriptions/">Event subscriptions for Artifacts lifecycle events</a></h2>
<p><em>2026-05-19</em></p>
<p>You can now receive <a href="/queues/event-subscriptions/">event notifications</a> for <a href="/artifacts/">Artifacts</a> repository changes and consume them from a Worker to build commit-driven automation.</p>
<p>This allows you to:</p>
<ul>
<li>Run custom workflows when a repository is created or imported</li>
<li>Kick off a build and deploy a change when an agent pushes to a repo</li>
<li>Trigger a review agent on every push</li>
</ul>
<p>Available events include:</p>
<ul>
<li><strong>Account-level events</strong> (<code>artifacts</code> source) — <code>repo.created</code>, <code>repo.deleted</code>, <code>repo.forked</code>, <code>repo.imported</code></li>
<li><strong>Repository-level events</strong> (<code>artifacts.repo</code> source) — <code>pushed</code>, <code>cloned</code>, <code>fetched</code></li>
</ul>
<p>To learn more, refer to <a href="/artifacts/guides/event-subscriptions/">Artifacts documentation</a>.</p>


<h2 id="manage-artifacts-namespaces-and-repos-with-wrangler-cli"><a href="/changelog/post/2026-05-18-wrangler-support/">Manage Artifacts namespaces and repos with Wrangler CLI</a></h2>
<p><em>2026-05-18</em></p>
<p>You can now manage <a href="/artifacts/">Artifacts</a> namespaces, repos, and repo-scoped tokens directly from Wrangler CLI.</p>
<p>Available commands:</p>
<ul>
<li><code>wrangler artifacts namespaces list</code> — List Artifacts namespaces in your account.</li>
<li><code>wrangler artifacts namespaces get</code> — Get metadata for a namespace.</li>
<li><code>wrangler artifacts repos create</code> — Create a repo in a namespace.</li>
<li><code>wrangler artifacts repos list</code> — List repos in a namespace.</li>
<li><code>wrangler artifacts repos get</code> — Get metadata for a repo.</li>
<li><code>wrangler artifacts repos delete</code> — Delete a repo.</li>
<li><code>wrangler artifacts repos issue-token</code> — Issue a repo-scoped token for Git access.</li>
</ul>
<p>To get started, refer to the <a href="/workers/wrangler/commands/artifacts/">Wrangler Artifacts commands documentation</a>.</p>


<h2 id="artifacts-now-in-beta-versioned-filesystem-with-git-access"><a href="/changelog/post/2026-04-16-artifacts-now-in-beta/">Artifacts now in beta: versioned filesystem with Git access</a></h2>
<p><em>2026-04-16</em></p>
<p><a href="/artifacts/">Artifacts</a> is now in private beta. Artifacts is Git-compatible storage built for scale: create tens of millions of repos, fork from any remote, and hand off a URL to any Git client. It provides a versioned filesystem for storing and exchanging file trees across Workers, the REST API, and any Git client, running locally or within an agent.</p>
<p>You can <a href="https://blog.cloudflare.com/artifacts-git-for-agents-beta/">read the announcement blog</a> to learn more about what Artifacts does, how it works, and how to create repositories for your agents to use.</p>
<p>Artifacts has three API surfaces:</p>
<ul>
<li>Workers bindings (for creating and managing repositories)</li>
<li>REST API (for creating and managing repos from any other compute platform)</li>
<li>Git protocol (for interacting with repos)</li>
</ul>
<p>As an example: you can use the Workers binding to create a repo and read back its remote URL:</p>
<pre tabindex="0"><code class="language-ts">&#35; Create a thousand, a million or ten million repos: one for every agent, for every upstream branch, or every user.&#10;const created = await env.PROD_ARTIFACTS.create(&quot;agent-007&quot;);&#10;const remote = (await created.repo.info())?.remote;&#10;</code></pre>
<p>Or, use the REST API to create a repo inside a namespace from your agent(s) running on any platform:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST &quot;https://artifacts.cloudflare.net/v1/api/namespaces/some-namespace/repos&quot; --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; --header &quot;Content-Type: application/json&quot; --data &#x27;{&quot;name&quot;:&quot;agent-007&quot;}&#x27;&#10;</code></pre>
<p>Any Git client that speaks smart HTTP can use the returned remote URL:</p>
<pre tabindex="0"><code class="language-bash">&#35; Agents know git.&#10;&#35; Every repository can act as a git repo, allowing agents to interact with Artifacts the way they know best: using the git CLI.&#10;git clone https://x:${REPO_TOKEN}@artifacts.cloudflare.net/some-namespace/agent-007.git&#10;</code></pre>
<p>To learn more, refer to <a href="/artifacts/get-started/">Get started</a>, <a href="/artifacts/api/workers-binding/">Workers binding</a>, and <a href="/artifacts/api/git-protocol/">Git protocol</a>.</p>



