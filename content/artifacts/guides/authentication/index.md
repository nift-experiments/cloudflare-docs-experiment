<p>Artifacts uses a different authentication path for each interface. Choose auth based on how your code reaches the repo.</p>
<p>Review <a href="/artifacts/concepts/namespaces/">Namespaces</a> first, then use one namespace name consistently across each interface.</p>
<h2 id="compare-auth-methods">Compare auth methods</h2>
<table>
<thead>
<tr>
<th>Interface</th>
<th>Authenticate with</th>
<th>Permissions or scopes</th>
<th>Use for</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers binding</td>
<td>Configured <code>artifacts</code> binding</td>
<td>Wrangler auth is only for local Wrangler commands such as <code>dev</code> and <code>deploy</code>.</td>
<td>Worker code that calls <code>env.ARTIFACTS</code></td>
</tr>
<tr>
<td>REST API</td>
<td>Cloudflare API token in <code>Authorization: Bearer ...</code></td>
<td><strong>Artifacts</strong> &gt; <strong>Read</strong> for read routes and <strong>Artifacts</strong> &gt; <strong>Edit</strong> for write routes.</td>
<td>Control-plane HTTP requests</td>
</tr>
<tr>
<td>Git protocol</td>
<td>Repo-scoped Artifacts token</td>
<td><code>read</code> for clone, fetch, and pull. <code>write</code> for push.</td>
<td>Standard Git over HTTPS</td>
</tr>
</tbody>
</table>
<p>Cloudflare API tokens authenticate control-plane access. Repo-scoped Artifacts tokens authenticate Git access.</p>
<h2 id="authenticate-the-workers-binding">Authenticate the Workers binding</h2>
<p>The Workers binding uses the <code>artifacts</code> binding you configure in Wrangler. Your Worker code does not pass a token when it calls <code>env.ARTIFACTS</code>.</p>
<p>Add the binding in your Wrangler config:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3301.md")
</div>
<p>At runtime, deployed Workers use the configured binding directly. For local Wrangler commands such as <code>wrangler dev</code>, <code>wrangler deploy</code>, or <code>wrangler types</code>, authenticate Wrangler first. For local OAuth authentication, refer to <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a>. For CI or headless environments, refer to <a href="/workers/ci-cd/">Running Wrangler in CI/CD</a>.</p>
<h2 id="authenticate-the-rest-api">Authenticate the REST API</h2>
<p>The REST API uses a Cloudflare API token in the <code>Authorization</code> header.</p>
<pre><code class="language-sh">export ACCOUNT_ID=&quot;&lt;YOUR_ACCOUNT_ID&gt;&quot;&#10;export ARTIFACTS_NAMESPACE=&quot;default&quot;&#10;export CLOUDFLARE_API_TOKEN=&quot;&lt;YOUR_API_TOKEN&gt;&quot;&#10;export ARTIFACTS_BASE_URL=&quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces/$ARTIFACTS_NAMESPACE&quot;&#10;</code></pre>
<p>Read repo metadata:</p>
<pre><code class="language-bash">curl &quot;$ARTIFACTS_BASE_URL/repos/starter-repo&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Create a repo:</p>
<pre><code class="language-bash">curl --request POST &quot;$ARTIFACTS_BASE_URL/repos&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;name&quot;: &quot;starter-repo&quot;&#10;  }&#x27;&#10;</code></pre>
<h2 id="authenticate-the-git-protocol">Authenticate the Git protocol</h2>
<p>Git uses repo-scoped Artifacts tokens, not Cloudflare API tokens. Mint these tokens from the Workers binding or the REST API, then use them with the repo <code>remote</code> URL.</p>
<table>
<thead>
<tr>
<th>Token scope</th>
<th>Allowed commands</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>read</code></td>
<td><code>git clone</code>, <code>git fetch</code>, <code>git pull</code></td>
</tr>
<tr>
<td><code>write</code></td>
<td><code>git clone</code>, <code>git fetch</code>, <code>git pull</code>, <code>git push</code></td>
</tr>
</tbody>
</table>
<p>Use the exact repo <code>remote</code> value returned by the Workers binding or REST API:</p>
<pre><code class="language-sh">export ARTIFACTS_REMOTE=&quot;&lt;PASTE_REMOTE_FROM_CREATE_OR_GET_RESPONSE&gt;&quot;&#10;</code></pre>
<p>Use a read token to clone:</p>
<pre><code class="language-sh">git -c http.extraHeader=&quot;Authorization: Bearer &lt;YOUR_READ_TOKEN&gt;&quot; clone &quot;$ARTIFACTS_REMOTE&quot; artifacts-clone&#10;</code></pre>
<p>Use a write token to push:</p>
<pre><code class="language-sh">git -c http.extraHeader=&quot;Authorization: Bearer &lt;YOUR_WRITE_TOKEN&gt;&quot; push &quot;$ARTIFACTS_REMOTE&quot; HEAD:main&#10;</code></pre>
<p>For more information on token handling and authenticated remotes, refer to <a href="/artifacts/api/git-protocol/">Git protocol</a>.</p>
