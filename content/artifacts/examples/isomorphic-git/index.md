<p>Use <a href="https://isomorphic-git.org/">isomorphic-git</a> to run Git operations on Artifacts repos directly from a Cloudflare Worker.</p>
<p>The Artifacts binding creates and manages repos, but it cannot read or write files inside them — for that, you need Git. Since Workers do not have a git binary or a local filesystem, <code>isomorphic-git</code> fills that gap. It provides Git operations like init, commit, and push as JavaScript function calls, using an in-memory filesystem in place of a real disk.</p>
<p>Use this when your Worker needs to programmatically build and push file trees to an Artifacts repo — for example, an AI agent that generates code and commits it, or an automation that clones a repo, modifies files, and pushes changes back.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Follow the <a href="/artifacts/get-started/workers/">Artifacts Workers setup guide</a> to set up a Worker with an Artifacts binding.</p>
<h3 id="install-the-dependency">Install the dependency</h3>
<p>Install <code>isomorphic-git</code> in your Worker project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i isomorphic-git</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i isomorphic-git" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add isomorphic-git</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add isomorphic-git" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add isomorphic-git</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add isomorphic-git" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add isomorphic-git</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add isomorphic-git" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="example">Example</h2>
<p>This demo creates a new repo on each request, writes two files, commits them, and pushes <code>main</code> to the new remote.</p>
<p>Use this as a reference for the end-to-end flow. In a production Worker, look up or reuse an existing repo instead of creating a new one for every request.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="protect-write-capable-routes">Protect write-capable routes</h3>
@markup("md", "content/.markup/bodies/3316.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3317.md")
</div>
<details class="nb-details"><summary>In-memory filesystem helper</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3319.md")
</div></details>
