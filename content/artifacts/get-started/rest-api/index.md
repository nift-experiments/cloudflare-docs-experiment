<p>Create an Artifacts repo with the REST API, then use a regular Git client to push and pull content.</p>
<p>By the end of this guide, you will create a repo inside a namespace, read back the repo remote URL, push a commit, and clone the same repo with a standard Git client.</p>
<p>Start by reading <a href="/artifacts/concepts/namespaces/">Namespaces</a>, then choose the namespace name you will use. This guide uses <code>default</code> in the examples.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need:</p>
<ul>
<li>Access to Artifacts.</li>
<li>A namespace name, for example <code>default</code>.</li>
<li>A <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> with <strong>Artifacts</strong> &gt; <strong>Read</strong> and <strong>Artifacts</strong> &gt; <strong>Edit</strong>.</li>
<li>A local <code>git</code> client.</li>
<li><code>jq</code>, if you want to extract response fields automatically.</li>
</ul>
<p>If you want to create and manage repos directly from a Worker (instead of calling the REST API), use the <a href="/artifacts/get-started/workers/">Workers get started guide</a>.</p>
<h2 id="1-export-your-environment-variables"><ol>
<li>Export your environment variables</li>
</ol></h2>
<p>Set the following variables using your Cloudflare account ID and Artifacts API token:</p>
<pre><code class="language-sh">export ARTIFACTS_NAMESPACE=&quot;default&quot;&#10;export ARTIFACTS_REPO=&quot;starter-repo&quot;&#10;export ACCOUNT_ID=&quot;&lt;YOUR_ACCOUNT_ID&gt;&quot;&#10;export CLOUDFLARE_API_TOKEN=&quot;&lt;YOUR_API_TOKEN&gt;&quot;&#10;export ARTIFACTS_BASE_URL=&quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces/$ARTIFACTS_NAMESPACE&quot;&#10;</code></pre>
<p>Use a unique repo name each time you run this guide.</p>
<p>Artifacts uses Bearer authentication for API requests:</p>
<pre><code class="language-txt">Authorization: Bearer $CLOUDFLARE_API_TOKEN&#10;</code></pre>
<h2 id="2-create-a-repo"><ol start="2">
<li>Create a repo</li>
</ol></h2>
<p>Choose one of the following ways to create a repo inside that namespace:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3312.md")
</div></div>
<h2 id="3-get-the-repo-url-again"><ol start="3">
<li>Get the repo URL again</li>
</ol></h2>
<p>Fetch the repo metadata when you need to recover the remote URL later:</p>
<pre><code class="language-bash">curl &quot;$ARTIFACTS_BASE_URL/repos/$ARTIFACTS_REPO&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;repo_123&quot;,&#10;		&quot;name&quot;: &quot;starter-repo&quot;,&#10;		&quot;description&quot;: null,&#10;		&quot;default_branch&quot;: &quot;main&quot;,&#10;		&quot;created_at&quot;: &quot;&lt;ISO_TIMESTAMP&gt;&quot;,&#10;		&quot;updated_at&quot;: &quot;&lt;ISO_TIMESTAMP&gt;&quot;,&#10;		&quot;last_push_at&quot;: null,&#10;		&quot;source&quot;: null,&#10;		&quot;read_only&quot;: false,&#10;		&quot;remote&quot;: &quot;https://&lt;ACCOUNT_ID&gt;.artifacts.cloudflare.net/git/default/starter-repo.git&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>This endpoint returns repo metadata only. If you need a new repo token, mint one with <code>POST /tokens</code>.</p>
<h2 id="4-push-your-first-commit-with-git"><ol start="4">
<li>Push your first commit with git</li>
</ol></h2>
<p>Create a local repository and push it to the Artifacts remote:</p>
<pre><code class="language-sh">mkdir artifacts-demo&#10;cd artifacts-demo&#10;git init -b main&#10;printf &#x27;# Artifacts demo\n&#x27; &gt; README.md&#10;git add README.md&#10;git commit -m &quot;Initial commit&quot;&#10;git remote add origin &quot;$ARTIFACTS_REMOTE&quot;&#10;git -c http.extraHeader=&quot;Authorization: Bearer $ARTIFACTS_TOKEN&quot; push -u origin main&#10;</code></pre>
<p>This uses the recommended header-based form and keeps the token out of the remote URL.</p>
<p>If you need a self-contained remote URL for a short-lived command, build one from the token secret instead:</p>
<pre><code class="language-sh">export ARTIFACTS_TOKEN_SECRET=&quot;${ARTIFACTS_TOKEN%%\?expires=*}&quot;&#10;export ARTIFACTS_AUTH_REMOTE=&quot;https://x:${ARTIFACTS_TOKEN_SECRET}@${ARTIFACTS_REMOTE#https://}&quot;&#10;git push &quot;$ARTIFACTS_AUTH_REMOTE&quot; HEAD:main&#10;</code></pre>
<h2 id="5-pull-the-repo-with-a-regular-git-client"><ol start="5">
<li>Pull the repo with a regular git client</li>
</ol></h2>
<p>Clone the same repo into a second directory:</p>
<pre><code class="language-sh">cd ..&#10;git -c http.extraHeader=&quot;Authorization: Bearer $ARTIFACTS_TOKEN&quot; clone &quot;$ARTIFACTS_REMOTE&quot; artifacts-clone&#10;git -C artifacts-clone log --oneline -1&#10;</code></pre>
<p>You should see the commit you pushed in the previous step.</p>
<p>You can also clone with a self-contained remote URL for a short-lived command:</p>
<pre><code class="language-sh">git clone &quot;$ARTIFACTS_AUTH_REMOTE&quot; artifacts-clone&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/artifacts/api/rest-api/"><h3 id="card-rest-api-reference-artifacts-api-rest-api">REST API reference</h3><p>Review every repo and token endpoint with request and response examples.</p></a></p>
<p><a class="nb-card nb-link-card" href="/artifacts/examples/git-client/"><h3 id="card-git-client-example-artifacts-examples-git-client">Git client example</h3><p>Use repo discovery and token minting with a standard Git client flow.</p></a></p>
<p><a class="nb-card nb-link-card" href="/artifacts/concepts/best-practices/"><h3 id="card-best-practices-artifacts-concepts-best-practices">Best practices</h3><p>Use repo isolation, least-privilege tokens, and namespace separation effectively.</p></a></p>
