<p>When you connect a git repository to Workers, by default a change to any file in the repository will trigger a build. You can configure Workers to include or exclude specific paths to specify if Workers should skip a build for a given path. This can be especially helpful if you are using a monorepo project structure and want to limit the number of builds being kicked off.</p>
<h2 id="configure-paths">Configure Paths</h2>
<p>To configure which paths are included and excluded:</p>
<ol>
<li>In <strong>Overview</strong>, select your Workers project.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Build</strong> &gt; <strong>Build watch paths</strong>. Workers will default to setting your project’s includes paths to everything ([*]) and excludes paths to nothing (<code>[]</code>).</li>
</ol>
<p>The configuration fields can be filled in two ways:</p>
<ul>
<li><strong>Static filepaths</strong>: Enter the precise name of the file you are looking to include or exclude (for example, <code>docs/README.md</code>).</li>
<li><strong>Wildcard syntax:</strong> Use wildcards to match multiple path directories. You can specify wildcards at the start or end of your rule.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wildcard-syntax">Wildcard syntax</h3>
@markup("md", "content/.markup/bodies/16779.md")
</aside>
<p>For each path in a push event, build watch paths will be evaluated as follows:</p>
<ul>
<li>Paths satisfying excludes conditions are ignored first</li>
<li>Any remaining paths are checked against includes conditions</li>
<li>If any matching path is found, a build is triggered. Otherwise the build is skipped</li>
</ul>
<p>Workers will bypass the path matching for a push event and default to building the project if:</p>
<ul>
<li>A push event contains 0 file changes, in case a user pushes an empty push event to trigger a build</li>
<li>A push event contains 3000+ file changes or 20+ commits</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="example-1">Example 1</h3>
<p>If you want to trigger a build from all changes within a set of directories, such as all changes in the folders <code>project-a/</code> and <code>packages/</code></p>
<ul>
<li>Include paths: <code>project-a/*, packages/*</code></li>
<li>Exclude paths: ``</li>
</ul>
<h3 id="example-2">Example 2</h3>
<p>If you want to trigger a build for any changes, but want to exclude changes to a certain directory, such as all changes in a docs/ directory</p>
<ul>
<li>Include paths: <code>*</code></li>
<li>Exclude paths: <code>docs/*</code></li>
</ul>
<h3 id="example-3">Example 3</h3>
<p>If you want to trigger a build for a specific file or specific filetype, for example all files ending in <code>.md</code>.</p>
<ul>
<li>Include paths: <code>*.md</code></li>
<li>Exclude paths: ``</li>
</ul>
