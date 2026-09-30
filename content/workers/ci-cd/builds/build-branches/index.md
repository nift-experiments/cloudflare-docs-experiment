<p>When you connect a git repository to Workers, commits made on the production git branch will produce a Workers Build. If you want to take advantage of <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a> and <a href="/workers/ci-cd/builds/git-integration/github-integration/#pull-request-comment">pull request comments</a>, you can additionally enable &quot;non-production branch builds&quot; in order to trigger a build on all branches of your repository.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16782.md")
</aside>
<h2 id="change-production-branch">Change production branch</h2>
<p>To change the production branch of your project:</p>
<ol>
<li>In <strong>Overview</strong>, select your Workers project.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Build</strong> &gt; <strong>Branch control</strong>. Workers will default to the default branch of your git repository, but this can be changed in the dropdown.</li>
</ol>
<p>Every push event made to this branch will trigger a build and execute the <a href="/workers/ci-cd/builds/configuration/#deploy-command">build command</a>, followed by the <a href="/workers/ci-cd/builds/configuration/#deploy-command">deploy command</a>.</p>
<h2 id="configure-non-production-branch-builds">Configure non-production branch builds</h2>
<p>To enable or disable non-production branch builds:</p>
<ol>
<li>In <strong>Overview</strong>, select your Workers project.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Build</strong> &gt; <strong>Branch control</strong>. The checkbox <strong>Builds for non-production branches</strong> allows you to enable or disable builds for non-production branches.</li>
</ol>
<p>When enabled, every push event made to a non-production branch will trigger a build and execute the <a href="/workers/ci-cd/builds/configuration/#deploy-command">build command</a>, followed by the <a href="/workers/ci-cd/builds/configuration/#non-production-branch-deploy-command">non-production branch deploy command</a>.</p>
