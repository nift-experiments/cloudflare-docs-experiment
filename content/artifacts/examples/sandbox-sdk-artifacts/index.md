<p>This example uses the <code>git-repo-per-sandbox</code> Sandbox SDK template and highlights the Artifacts-specific pieces.</p>
<p>Start from the template with <code>create cloudflare</code>, as shown in <a href="/sandbox/tutorials/claude-code/#1-create-your-project">Run Claude Code on a Sandbox</a>. Then adapt the Artifacts flow with the focused snippets below.</p>
<ul>
<li>Creates or reuses a sandbox by ID.</li>
<li>Creates or reuses an Artifacts repo with the same ID.</li>
<li>Passes an authenticated Git remote into the sandbox as <code>ARTIFACTS_GIT_REMOTE</code>.</li>
</ul>
<h2 id="create-your-project">Create your project</h2>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox" aria-label="Copy to clipboard">Copy</button></div></div>
<pre><code class="language-sh">cd repo-per-sandbox&#10;</code></pre>
<h2 id="1-create-or-reuse-the-repo"><ol>
<li>Create or reuse the repo</li>
</ol></h2>
<p>The template keeps one Artifacts repo per sandbox ID. Use your own source of truth to decide whether this request should create a new repo or load an existing one.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3313.md")
</div>
<p>The template already knows the repo name, so start with direct lookup instead of scanning <code>list()</code> pages. Avoid broad <code>catch</code> blocks here. They can hide missing-repo, auth, and validation failures behind the same retry message.</p>
<p>If your flow can race with repo creation, handle that retry at the application level after you inspect the thrown error.</p>
<h2 id="2-create-or-reuse-the-sandbox"><ol start="2">
<li>Create or reuse the sandbox</li>
</ol></h2>
<p>Use the same ID for the sandbox:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3314.md")
</div>
<h2 id="3-pass-the-repo-into-the-sandbox"><ol start="3">
<li>Pass the repo into the sandbox</li>
</ol></h2>
<p>Convert the write token into an authenticated Git remote, then store it as an environment variable inside the sandbox.</p>
<p>Use a short-lived token and pass it into the sandbox only after the sandbox session is authorized to push changes.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3315.md")
</div>
<p>Code running inside the sandbox can then use <code>ARTIFACTS_GIT_REMOTE</code> with <code>git clone</code>, <code>git fetch</code>, <code>git pull</code>, or <code>git push</code>.</p>
