<p>When you connect a git repository to Pages, by default a change to any file in the repository will trigger a Pages build. You can configure Pages to include or exclude specific paths to specify if Pages should skip a build for a given path. This can be especially helpful if you are using a monorepo project structure and want to limit the amount of builds being kicked off.</p>
<h2 id="configure-paths">Configure paths</h2>
<p>To configure which paths are included and excluded:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11073.md")
</div>
<p>The configuration fields can be filled in two ways:</p>
<ul>
<li><strong>Static filepaths</strong>: Enter the precise name of the file you are looking to include or exclude (for example, <code>docs/README.md</code>).</li>
<li><strong>Wildcard syntax:</strong> Use wildcards to match multiple paths. You can specify wildcards at the start or end of your rule.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wildcard-syntax">Wildcard syntax</h3>
@markup("md", "content/.markup/bodies/11072.md")
</aside>
<p>For each path in a push event, build watch paths will be evaluated as follows:</p>
<ul>
<li>Paths satisfying excludes conditions are ignored first</li>
<li>Any remaining paths are checked against includes conditions</li>
<li>If any matching path is found, a build is triggered. Otherwise the build is skipped</li>
</ul>
<p>Pages will bypass the path matching for a push event and default to building the project if:</p>
<ul>
<li>A push event contains 0 file changes, in case a user pushes an empty push event to trigger a build</li>
<li>A push event contains 3000+ file changes or 20+ commits</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="trigger-builds-for-specific-directories-monorepo">Trigger builds for specific directories (monorepo)</h3>
<p>If you want to trigger a build only when files change within specific directories, such as <code>project-a/</code> and <code>packages/</code>. Because <code>*</code> matches across path separators, this includes changes in nested subdirectories like <code>project-a/src/index.js</code> or <code>packages/utils/lib/helpers.ts</code>.</p>
<ul>
<li>Include paths: <code>project-a/*, packages/*</code></li>
<li>Exclude paths: ``</li>
</ul>
<h3 id="exclude-a-directory-from-triggering-builds">Exclude a directory from triggering builds</h3>
<p>If you want to trigger a build for any changes, but want to exclude changes to a certain directory, such as all changes in a <code>docs/</code> directory (including nested paths like <code>docs/guides/setup.md</code>).</p>
<ul>
<li>Include paths: <code>*</code></li>
<li>Exclude paths: <code>docs/*</code></li>
</ul>
<h3 id="trigger-builds-for-a-specific-filetype">Trigger builds for a specific filetype</h3>
<p>If you want to trigger a build for a specific file or specific filetype, for example all <code>.md</code> files anywhere in the repository.</p>
<ul>
<li>Include paths: <code>*.md</code></li>
<li>Exclude paths: ``</li>
</ul>
<h3 id="trigger-builds-for-a-directory-but-exclude-a-subdirectory">Trigger builds for a directory but exclude a subdirectory</h3>
<p>If you want to trigger a build for changes in <code>src/</code> but want to ignore changes in <code>src/tests/</code>.</p>
<ul>
<li>Include paths: <code>src/*</code></li>
<li>Exclude paths: <code>src/tests/*</code></li>
</ul>
