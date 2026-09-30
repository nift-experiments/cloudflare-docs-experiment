<p>ArtifactFS mounts a Git repository as a local filesystem without waiting for a full clone. It works well when your environment needs a working tree quickly and can tolerate file contents hydrating on demand.</p>
<p>Use ArtifactFS for large repos in sandboxes, containers, and virtual machines. For smaller repos, a regular <code>git clone</code> is usually simpler.</p>
<p>ArtifactFS works with <a href="/artifacts/api/git-protocol/">Artifacts Git remotes</a> and other Git repositories.</p>
<h2 id="choose-artifactfs-when">Choose ArtifactFS when</h2>
<ul>
<li>startup time matters more than a complete local clone</li>
<li>the repo is large enough that cloning slows down sandbox startup</li>
<li>tools need a mounted working tree instead of direct Git access</li>
</ul>
<p>For smaller repos, start with a regular <code>git clone</code>. It is usually fast enough and simpler to operate.</p>
<h2 id="understand-how-it-behaves">Understand how it behaves</h2>
<p>ArtifactFS starts with a blobless clone. It fetches commits, trees, and refs first, then mounts the working tree through FUSE.</p>
<p>File contents hydrate asynchronously as tools read them. Reads only block when a requested blob is not hydrated yet, and later reads come from the local blob cache.</p>
<p>ArtifactFS prioritizes files that usually unblock developer tools first, such as package manifests, dependency files, and common source files. Large binary assets are deprioritized.</p>
<h2 id="mount-an-artifacts-repo">Mount an Artifacts repo</h2>
<p>This example installs ArtifactFS, builds an authenticated Artifacts remote from a repo token, mounts the repo, and reads files from the mounted working tree.</p>
<p>This example assumes you already have a working FUSE implementation on the host, a repo-scoped Artifacts token, and the repo <code>remote</code> value from a create or get response.</p>
<pre><code class="language-bash">go install github.com/cloudflare/artifact-fs/cmd/artifact-fs@latest&#10;&#10;export ARTIFACTS_REMOTE=&quot;&lt;PASTE_REMOTE_FROM_CREATE_OR_GET_RESPONSE&gt;&quot;&#10;export ARTIFACTS_TOKEN=&quot;&lt;YOUR_READ_TOKEN&gt;&quot;&#10;export ARTIFACTS_TOKEN_SECRET=&quot;${ARTIFACTS_TOKEN%%\?expires=*}&quot;&#10;export ARTIFACTS_AUTH_REMOTE=&quot;https://x:${ARTIFACTS_TOKEN_SECRET}@${ARTIFACTS_REMOTE#https://}&quot;&#10;&#10;artifact-fs add-repo \&#10;  &#45;-name starter-repo \&#10;  &#45;-remote &quot;$ARTIFACTS_AUTH_REMOTE&quot; \&#10;  &#45;-branch main \&#10;  &#45;-mount-root /tmp&#10;&#10;artifact-fs daemon --root /tmp &amp;&#10;&#10;ls /tmp/starter-repo/&#10;cat /tmp/starter-repo/README.md&#10;git -C /tmp/starter-repo log --oneline -5&#10;</code></pre>
<p>Use a short-lived token in the authenticated remote URL. If you need a smaller repo or a simpler local workflow, use a normal <a href="/artifacts/api/git-protocol/">Git protocol</a> clone instead.</p>
