<p>Artifacts exposes Git access for every Artifacts repository.</p>
<p>Each repo has a standard Git smart HTTP remote at <code>https://&lt;ACCOUNT_ID&gt;.artifacts.cloudflare.net/git/&lt;namespace&gt;/&lt;repo&gt;.git</code>.</p>
<p>Replace the <code>&lt;ACCOUNT_ID&gt;</code> placeholder with your Cloudflare account ID. Use the exact hostname from the repo <code>remote</code> returned by the Workers binding or REST API.</p>
<p>Use the returned repo <code>remote</code> with a regular Git client for <code>clone</code>, <code>fetch</code>, <code>pull</code>, and <code>push</code>.</p>
<h2 id="authentication">Authentication</h2>
<p>Git routes accept repo access tokens in two forms:</p>
<table>
<thead>
<tr>
<th>Format</th>
<th>Details</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bearer token in <code>http.extraHeader</code></td>
<td>Recommended for local workflows. Use the full token string returned by the control plane and keep credentials out of the remote URL.</td>
<td><code>git -c http.extraHeader=&quot;Authorization: Bearer $ARTIFACTS_TOKEN&quot; clone &quot;$ARTIFACTS_REMOTE&quot; artifacts-clone</code></td>
</tr>
<tr>
<td>HTTP Basic auth in the remote URL</td>
<td>Use for short-lived, one-off commands when you need a self-contained remote. Put the token secret in the password slot.</td>
<td><code>https://x:&lt;token-secret&gt;@&lt;ACCOUNT_ID&gt;.artifacts.cloudflare.net/git/&lt;namespace&gt;/&lt;repo&gt;.git</code></td>
</tr>
</tbody>
</table>
<h3 id="token-format">Token format</h3>
<p>Repo tokens are issued in the format <code>art_v1_&lt;40 hex&gt;?expires=&lt;unix_seconds&gt;</code>. The <code>?expires=</code> suffix is the token's expiry as a unix timestamp in seconds. To check when a token expires, parse the value after <code>?expires=</code>.</p>
<h3 id="git-extraheader-parameter">Git <code>extraHeader</code> parameter</h3>
<p>Git's <a href="https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpextraHeader"><code>http.extraHeader</code></a> setting lets you attach an HTTP header to git requests.</p>
<p>If you want to use the full token string returned by the API, pass it as a Bearer token:</p>
<pre><code class="language-sh">git -c http.extraHeader=&quot;Authorization: Bearer $ARTIFACTS_TOKEN&quot; clone &quot;$ARTIFACTS_REMOTE&quot; artifacts-clone&#10;</code></pre>
<h3 id="https-remote-with-basic-auth">HTTPS remote with Basic auth</h3>
<p>For the URL form, use the token secret in the password slot. Artifacts ignores the Basic auth username.</p>
<p>Use this form only when you need a self-contained remote URL for a short-lived command.</p>
<pre><code class="language-sh">export ARTIFACTS_TOKEN_SECRET=&quot;${ARTIFACTS_TOKEN%%\?expires=*}&quot;&#10;export ARTIFACTS_AUTH_REMOTE=&quot;https://x:${ARTIFACTS_TOKEN_SECRET}@${ARTIFACTS_REMOTE#https://}&quot;&#10;</code></pre>
<pre><code class="language-sh">git clone &quot;$ARTIFACTS_AUTH_REMOTE&quot; artifacts-clone&#10;</code></pre>
<pre><code class="language-sh">git push &quot;$ARTIFACTS_AUTH_REMOTE&quot; HEAD:main&#10;</code></pre>
<p>Use any non-empty username in the URL. Artifacts accepts that username but does not otherwise use or log it, so <code>x</code> is just a placeholder.</p>
<h2 id="protocol-support">Protocol support</h2>
<p>Artifacts supports Git protocol v1 and v2 for clone and fetch. Git clients negotiate the protocol automatically.</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Git service</th>
<th>Protocol support</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Clone and fetch</td>
<td><code>git-upload-pack</code></td>
<td>v1 and v2</td>
<td>Protocol v2 supports <code>ls-refs</code> and <code>fetch</code>. Protocol v1 supports normal fetch flows, including shallow and deepen fetches.</td>
</tr>
<tr>
<td>Push</td>
<td><code>git-receive-pack</code></td>
<td>v1</td>
<td>Push uses the standard v1 receive-pack flow.</td>
</tr>
<tr>
<td>Push over protocol v2</td>
<td><code>git-receive-pack</code></td>
<td>Not supported</td>
<td>Artifacts does not support v2 receive-pack.</td>
</tr>
<tr>
<td>Optional protocol v1 capabilities</td>
<td><code>git-upload-pack</code></td>
<td>Partial</td>
<td>Some optional v1 capabilities, such as <code>filter</code> and <code>include-tag</code>, are not supported.</td>
</tr>
</tbody>
</table>
<h2 id="token-scopes">Token scopes</h2>
<table>
<thead>
<tr>
<th>Scope</th>
<th>Commands</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>read</code></td>
<td><code>git clone</code>, <code>git fetch</code>, <code>git pull</code></td>
<td>Use for read-only access.</td>
</tr>
<tr>
<td><code>write</code></td>
<td><code>git clone</code>, <code>git fetch</code>, <code>git pull</code>, <code>git push</code></td>
<td><code>git push</code> mutates the repo and requires a write token.</td>
</tr>
</tbody>
</table>
