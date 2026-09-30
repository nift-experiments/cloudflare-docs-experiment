<p>Use the Artifacts Workers binding to create, import, inspect, fork, and delete repos directly from your Worker. The Artifacts binding returns repo handles that allow repo-scoped operations such as token management and forking.</p>
<p>Review <a href="/artifacts/concepts/namespaces/">Namespaces</a> first, then choose the namespace name you will bind here.</p>
<h2 id="configure-the-binding">Configure the binding</h2>
<p>Add the Artifacts binding to your Wrangler config file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3325.md")
</div>
<p>After you run <code>npx wrangler types</code>, your Worker environment looks like this:</p>
<pre><code class="language-ts">export interface Env {&#10;	ARTIFACTS: Artifacts;&#10;}&#10;</code></pre>
<p>Wrangler generates the <code>Artifacts</code> type for consumers and binds it directly in your environment.</p>
<p>In named Wrangler environments, <code>artifacts</code> is non-inheritable. Repeat the binding in each environment where you need it.</p>
<p>At runtime, deployed Workers use the configured binding directly. For local Wrangler commands such as <code>wrangler dev</code>, <code>wrangler deploy</code>, or <code>wrangler types</code>, authenticate Wrangler first. For local OAuth authentication, refer to <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a>. For CI or headless environments, refer to <a href="/workers/ci-cd/">Running Wrangler in CI/CD</a>.</p>
<h2 id="namespace-methods">Namespace methods</h2>
<p>Use namespace methods on <code>env.ARTIFACTS</code> to create, list, inspect, import, or delete repos.</p>
<h3 id="create-name-opts"><code>create(name, opts?)</code></h3>
<ul>
<li><code>name</code> <span class="nb-type">RepoName</span> <span class="nb-metainfo">required</span></li>
<li><code>opts.readOnly</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></li>
<li><code>opts.description</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></li>
<li><code>opts.setDefaultBranch</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></li>
<li>Returns <span class="nb-type">Promise&lt;ArtifactsCreateRepoResult&gt;</span></li>
</ul>
<p><code>create()</code> returns repo metadata including <code>name</code>, <code>remote</code>, <code>defaultBranch</code>, and an initial token. Save these values if you need them later.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3326.md")
</div>
<h3 id="get-name"><code>get(name)</code></h3>
<ul>
<li><code>name</code> <span class="nb-type">RepoName</span> <span class="nb-metainfo">required</span></li>
<li>Returns <span class="nb-type">Promise&lt;ArtifactsRepo&gt;</span></li>
<li>Throws if the repo does not exist or is not ready yet.</li>
</ul>
<p><code>get()</code> returns a handle to an existing repo. Use the handle to call async methods on the repo, such as <code>createToken()</code>, <code>listTokens()</code>, <code>revokeToken()</code>, and <code>fork()</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3327.md")
</div>
<h3 id="list-opts"><code>list(opts?)</code></h3>
<ul>
<li><code>opts.limit</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></li>
<li><code>opts.cursor</code> <span class="nb-type">Cursor</span> <span class="nb-metainfo">optional</span></li>
<li>Returns <span class="nb-type">Promise&lt;ArtifactsRepoListResult&gt;</span></li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3328.md")
</div>
<p>Each listed repo includes a <code>status</code> value of <code>ready</code>, <code>importing</code>, or <code>forking</code>.</p>
<h3 id="import-params"><code>import(params)</code></h3>
<p>Import a repository from an external git remote.</p>
<ul>
<li><code>params.source.url</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span> — HTTPS URL of the source repository.</li>
<li><code>params.source.branch</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span> — Branch to import (defaults to the remote's default branch).</li>
<li><code>params.source.depth</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span> — Shallow clone depth.</li>
<li><code>params.target.name</code> <span class="nb-type">RepoName</span> <span class="nb-metainfo">required</span> — Name for the imported repo.</li>
<li><code>params.target.opts.description</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></li>
<li><code>params.target.opts.readOnly</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></li>
<li>Returns <span class="nb-type">Promise&lt;ArtifactsCreateRepoResult&gt;</span></li>
</ul>
<p><code>import()</code> returns repo metadata including <code>name</code>, <code>remote</code>, <code>defaultBranch</code>, and an initial token. Save the <code>remote</code> and <code>name</code> values if you need them later.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3329.md")
</div>
<h3 id="delete-name"><code>delete(name)</code></h3>
<ul>
<li><code>name</code> <span class="nb-type">RepoName</span> <span class="nb-metainfo">required</span></li>
<li>Returns <span class="nb-type">Promise&lt;boolean&gt;</span></li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3330.md")
</div>
<h2 id="repo-handle-methods">Repo handle methods</h2>
<p>Call <code>await artifacts.get(name)</code> to get a repo handle. Use the handle to call async methods on the repo.</p>
<h3 id="createtoken-scope-ttl"><code>createToken(scope?, ttl?)</code></h3>
<ul>
<li><code>scope</code> <span class="nb-type">read&quot; | &quot;write</span> <span class="nb-metainfo">optional (default: &quot;write&quot;)</span></li>
<li><code>ttl</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional (seconds)</span></li>
<li>Returns <span class="nb-type">Promise&lt;ArtifactsCreateTokenResult&gt;</span></li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3331.md")
</div>
<p>Unlike <code>create()</code> and <code>import()</code>, <code>repo.createToken()</code> returns a structured result with <code>plaintext</code> and <code>expiresAt</code>. The <code>plaintext</code> value is the Git token string.</p>
<h3 id="listtokens"><code>listTokens()</code></h3>
<ul>
<li>Returns <span class="nb-type">Promise&lt;ArtifactsTokenListResult&gt;</span></li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3332.md")
</div>
<h3 id="revoketoken-tokenorid"><code>revokeToken(tokenOrId)</code></h3>
<ul>
<li><code>tokenOrId</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></li>
<li>Returns <span class="nb-type">Promise&lt;boolean&gt;</span></li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3333.md")
</div>
<h3 id="fork-name-opts"><code>fork(name, opts?)</code></h3>
<ul>
<li><code>name</code> <span class="nb-type">RepoName</span> <span class="nb-metainfo">required</span></li>
<li><code>opts.description</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></li>
<li><code>opts.readOnly</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></li>
<li><code>opts.defaultBranchOnly</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></li>
<li>Returns <span class="nb-type">Promise&lt;ArtifactsCreateRepoResult&gt;</span></li>
</ul>
<p><code>fork()</code> returns metadata for the new repo. Save the <code>remote</code> and <code>name</code> values if you need them later.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3334.md")
</div>
<h3 id="log-opts"><code>log(opts?)</code></h3>
<ul>
<li><code>opts.ref</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span> — Branch, tag, or commit hash.</li>
<li><code>opts.limit</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></li>
<li><code>opts.offset</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></li>
<li>Returns <span class="nb-type">Promise&lt;ArtifactsLogResult&gt;</span></li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3335.md")
</div>
<h3 id="readcommit-hash"><code>readCommit(hash)</code></h3>
<ul>
<li><code>hash</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span> — Commit SHA-1 hash.</li>
<li>Returns <span class="nb-type">Promise&lt;ArtifactsCommit&gt;</span></li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3336.md")
</div>
<h3 id="readtree-hash"><code>readTree(hash)</code></h3>
<ul>
<li><code>hash</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span> — Tree SHA-1 hash.</li>
<li>Returns <span class="nb-type">Promise&lt;ArtifactsTree&gt;</span></li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3337.md")
</div>
<h2 id="worker-example">Worker example</h2>
<p>This example combines the binding methods in one Worker route.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3338.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="protect-token-routes">Protect token routes</h3>
@markup("md", "content/.markup/bodies/3324.md")
</aside>
<h2 id="generated-types">Generated types</h2>
<p>Run <code>npx wrangler types</code> in your own project and treat the generated <code>worker-configuration.d.ts</code> file as the source of truth for the Artifacts binding types in that environment.</p>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/artifacts/api/rest-api/"><h3 id="card-rest-api-artifacts-api-rest-api">REST API</h3><p>Compare the binding methods with the underlying HTTP routes.</p></a></p>
<p><a class="nb-card nb-link-card" href="/artifacts/get-started/workers/"><h3 id="card-get-started-with-workers-artifacts-get-started-workers">Get started with Workers</h3><p>Use the binding in a full Worker project from local development through deploy.</p></a></p>
<p><a class="nb-card nb-link-card" href="/artifacts/api/git-protocol/"><h3 id="card-git-protocol-artifacts-api-git-protocol">Git protocol</h3><p>Use repo remotes and tokens with standard git-over-HTTPS clients.</p></a></p>
