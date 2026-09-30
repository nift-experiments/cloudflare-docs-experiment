<p>You can use a standard Git client to interact with Artifacts repos. This example walks through clone, but the same approach works for fetch, pull, push, and any other Git operation.</p>
<p>To do this, you need to:</p>
<ul>
<li>Fetch the repo's remote URL from the REST API</li>
<li>Mint a short-lived token scoped to that repo</li>
</ul>
<p>Once you have the remote URL and token, you can use them to run Git commands against the repo.</p>
<p>This example assumes the repo already exists and that you have a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> with <strong>Artifacts</strong> &gt; <strong>Edit</strong>.</p>
<h2 id="fetch-the-remote-and-clone-the-repo">Fetch the remote and clone the repo</h2>
<p>Replace the placeholder values with your account ID, API token, and repo name. The script fetches the repo's remote URL from the API, mints a read-only token that expires in one hour, and clones the repo to a local directory.</p>
<p>The example below uses <code>jq</code> to extract fields from the JSON responses.</p>
<pre><code class="language-bash">&#35; Set your account details&#10;export ACCOUNT_ID=&quot;&lt;YOUR_ACCOUNT_ID&gt;&quot;&#10;export ARTIFACTS_NAMESPACE=&quot;default&quot;&#10;export ARTIFACTS_REPO=&quot;starter-repo&quot;&#10;export CLOUDFLARE_API_TOKEN=&quot;&lt;YOUR_API_TOKEN&gt;&quot;&#10;export ARTIFACTS_BASE_URL=&quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces/$ARTIFACTS_NAMESPACE&quot;&#10;&#10;&#35; Fetch the repo&#x27;s remote URL&#10;REPO_JSON=$(curl --silent &quot;$ARTIFACTS_BASE_URL/repos/$ARTIFACTS_REPO&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;)&#10;&#10;ARTIFACTS_REMOTE=$(printf &#x27;%s&#x27; &quot;$REPO_JSON&quot; | jq -r &#x27;.result.remote&#x27;)&#10;&#10;&#35; Mint a short-lived read token&#10;TOKEN_JSON=$(curl --silent &quot;$ARTIFACTS_BASE_URL/tokens&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &quot;{\&quot;repo\&quot;:\&quot;$ARTIFACTS_REPO\&quot;,\&quot;scope\&quot;:\&quot;read\&quot;,\&quot;ttl\&quot;:3600}&quot;)&#10;&#10;ARTIFACTS_TOKEN=$(printf &#x27;%s&#x27; &quot;$TOKEN_JSON&quot; | jq -r &#x27;.result.plaintext&#x27;)&#10;&#10;&#35; Clone the repo&#10;git -c http.extraHeader=&quot;Authorization: Bearer $ARTIFACTS_TOKEN&quot; clone &quot;$ARTIFACTS_REMOTE&quot; artifacts-clone&#10;</code></pre>
<p>You now have a standard Git checkout in <code>./artifacts-clone</code>.</p>
<p>This flow is useful when another system owns repo discovery or access control, but your local tooling still expects a normal git remote.</p>
<h3 id="authentication">Authentication</h3>
Treat `ARTIFACTS_TOKEN` as a secret. Keep it out of logs, and prefer `http.extraHeader` over saving credentials in a remote URL.
<p>If you need a self-contained remote URL for a short-lived workflow, extract the token secret and build the authenticated remote only for that command:</p>
<pre><code class="language-sh">ARTIFACTS_TOKEN_SECRET=&quot;${ARTIFACTS_TOKEN%%\?expires=*}&quot;&#10;ARTIFACTS_AUTH_REMOTE=&quot;https://x:${ARTIFACTS_TOKEN_SECRET}@${ARTIFACTS_REMOTE#https://}&quot;&#10;&#10;git clone &quot;$ARTIFACTS_AUTH_REMOTE&quot; artifacts-clone&#10;</code></pre>
