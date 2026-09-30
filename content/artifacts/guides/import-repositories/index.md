<p>Import an existing repository when you already have a baseline outside Artifacts and want to start using it as an Artifacts repo.</p>
<p>This works well for:</p>
<ul>
<li>a baseline repo that agents fork from</li>
<li>a template repo for new sessions or users</li>
<li>a shared prompts or configuration repo used across workflows</li>
</ul>
<p>Artifacts imports public HTTPS remotes through the <a href="/artifacts/api/rest-api/#import-a-public-https-remote">REST API</a> or the <a href="/artifacts/api/workers-binding/#importparams">Workers binding</a>. After import, the repo has a normal Artifacts remote URL and can be cloned, forked, or issued repo-scoped tokens like any other repo.</p>
<p>Review <a href="/artifacts/concepts/namespaces/">Namespaces</a> first, then use one namespace name consistently across your import workflow.</p>
<h2 id="import-a-public-https-repo">Import a public HTTPS repo</h2>
<p>This example imports a public GitHub repo into the <code>default</code> namespace. You can use the same flow with other public HTTPS Git remotes.</p>
<p>Use a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> with <strong>Artifacts</strong> &gt; <strong>Edit</strong>.</p>
<p>This example uses <code>jq</code> to extract the returned fields.</p>
<pre><code class="language-sh">export ACCOUNT_ID=&quot;&lt;YOUR_ACCOUNT_ID&gt;&quot;&#10;export ARTIFACTS_NAMESPACE=&quot;default&quot;&#10;export ARTIFACTS_REPO=&quot;workers-sdk-baseline&quot;&#10;export CLOUDFLARE_API_TOKEN=&quot;&lt;YOUR_API_TOKEN&gt;&quot;&#10;export ARTIFACTS_BASE_URL=&quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces/$ARTIFACTS_NAMESPACE&quot;&#10;</code></pre>
<pre><code class="language-bash">IMPORT_RESPONSE=$(curl --silent --request POST &quot;$ARTIFACTS_BASE_URL/repos/$ARTIFACTS_REPO/import&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;     &quot;url&quot;: &quot;https://github.com/cloudflare/workers-sdk&quot;,&#10;     &quot;branch&quot;: &quot;main&quot;,&#10;     &quot;depth&quot;: 100&#10;   }&#x27;)&#10;&#10;if ! printf &#x27;%s&#x27; &quot;$IMPORT_RESPONSE&quot; | jq -e &#x27;.success == true&#x27; &gt; /dev/null; then&#10;  printf &#x27;%s\n&#x27; &quot;$IMPORT_RESPONSE&quot; | jq .&#10;  exit 1&#10;fi&#10;&#10;export ARTIFACTS_REMOTE=$(printf &#x27;%s&#x27; &quot;$IMPORT_RESPONSE&quot; | jq -r &#x27;.result.remote&#x27;)&#10;export ARTIFACTS_TOKEN=$(printf &#x27;%s&#x27; &quot;$IMPORT_RESPONSE&quot; | jq -r &#x27;.result.token&#x27;)&#10;</code></pre>
<p>The response includes the new Artifacts repo metadata, including <code>result.remote</code> and <code>result.token</code>.</p>
<p>If the request fails, this check prints the API response and exits before it exports empty values.</p>
<p>The token encodes its expiry directly in the <code>?expires=</code> suffix.</p>
<p>Treat <code>result.token</code> as a secret. Do not log it or store it in a long-lived remote URL unless your workflow requires it.</p>
<p>An import can still be in progress after this request returns. If follow-up REST calls return <code>409 Conflict</code>, retry after a short delay.</p>
<h2 id="use-the-imported-repo">Use the imported repo</h2>
<p>After the import finishes, use the repo like any other Artifacts repo.</p>
<ul>
<li>Keep it as a stable baseline and fork from it for agent work</li>
<li>clone it with a repo-scoped token for direct Git access</li>
<li>mark it read-only if you want a fixed template repo</li>
</ul>
<p>For the endpoint details, refer to <a href="/artifacts/api/rest-api/#import-a-public-https-remote">REST API</a>. For auth details, refer to <a href="/artifacts/guides/authentication/">Authentication</a>.</p>
