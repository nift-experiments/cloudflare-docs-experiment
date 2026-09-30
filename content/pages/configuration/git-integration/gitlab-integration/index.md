<p>You can connect each Cloudflare Pages project to a GitLab repository, and Cloudflare will automatically deploy your code every time you push a change to a branch.</p>
<h2 id="features">Features</h2>
<p>Beyond automatic deployments, the Cloudflare GitLab integration lets you monitor, manage, and preview deployments directly in GitLab, keeping you informed without leaving your workflow.</p>
<h3 id="custom-branches">Custom branches</h3>
<p>Pages will default to setting your <a href="/pages/configuration/branch-build-controls/#production-branch-control">production environment</a> to the branch you first push. If a branch other than the default branch (e.g. <code>main</code>) represents your project's production branch, then go to <strong>Settings</strong> &gt; <strong>Builds</strong> &gt; <strong>Branch control</strong>, change the production branch by clicking the <strong>Production branch</strong> dropdown menu and choose any other branch.</p>
<p>You can also use <a href="/pages/configuration/preview-deployments/">preview deployments</a> to preview versions of your project before merging your production branch, and deploying to production. Pages allows you to configure which of your preview branches are automatically deployed using <a href="/pages/configuration/branch-build-controls/">branch build controls</a>. To configure, go to <strong>Settings</strong> &gt; <strong>Builds</strong> &gt; <strong>Branch control</strong> and select an option under <strong>Preview branch</strong>. Use <a href="/pages/configuration/branch-build-controls/"><strong>Custom branches</strong></a> to specify branches you wish to include or exclude from automatic preview deployments.</p>
<h3 id="skipping-a-specific-build-via-a-commit-message">Skipping a specific build via a commit message</h3>
<p>Without any configuration required, you can choose to skip a deployment on an ad hoc basis. By adding the <code>[CI Skip]</code>, <code>[CI-Skip]</code>, <code>[Skip CI]</code>, <code>[Skip-CI]</code>, or <code>[CF-Pages-Skip]</code> flag as a prefix in your commit message, Pages will omit that deployment. The prefixes are not case sensitive.</p>
<h3 id="check-runs-and-preview-urls">Check runs and preview URLs</h3>
<p>If you have one or multiple projects connected to a repository (i.e. a <a href="/workers/ci-cd/builds/advanced-setups/#monorepos">monorepo</a>), you can check on the status of each build within GitLab via <a href="https://docs.gitlab.com/ee/user/project/merge_requests/status_checks.html">GitLab commit status</a>.</p>
<p>You can see the statuses by selecting the status icon next to a commit or by going to <strong>Build</strong> &gt; <strong>Pipelines</strong> within your GitLab repository. In the example below, you can select the green check mark to see the results of the check run.</p>
<p><img src="/assets/upstream/images/workers/platform/ci-cd/gl-status-checks.png" alt="GitLab Status" /></p>
<p>Check runs will appear like the following in your repository. You can select one of the statuses to view the <a href="/pages/configuration/preview-deployments/">preview URL</a> for that deployment.</p>
<p><img src="/assets/upstream/images/pages/configuration/glcommitstatus.png" alt="GitLab Commit Status" /></p>
<p>If a build skips for any reason (i.e. CI Skip, build watch paths, or branch deployment controls), the check run/commit status will not appear.</p>
<h2 id="manage-access">Manage access</h2>
<p>You can deploy projects to Cloudflare Workers from your company or side project on GitLab using the Cloudflare Pages app.</p>
<h3 id="organizational-access">Organizational access</h3>
<p>You can deploy projects to Cloudflare Pages from your company or side project on both GitHub and GitLab.</p>
<p>When you authorize Cloudflare Pages to access your GitLab account, you automatically give Cloudflare Pages access to organizations, groups, and namespaces accessed by your GitLab account. Managing access to these organizations and groups is handled by GitLab.</p>
<h3 id="remove-access">Remove access</h3>
<p>You can remove Cloudflare Workers' access to your GitLab account by navigating to <a href="https://gitlab.com/-/profile/applications">Authorized Applications page</a> on GitLab. Find the applications called Cloudflare Workers and select the <strong>Revoke</strong> button to revoke access.</p>
<p>Note that the GitLab application Cloudflare Workers is shared between Workers and Pages projects, and removing access to GitLab will disable new builds for Workers and Pages, though your previous deployments will continue to be hosted by Cloudflare Pages.</p>
<h3 id="reinstall-the-cloudflare-gitlab-app">Reinstall the Cloudflare GitLab app</h3>
<p>When encountering Git integration related issues, one potential troubleshooting step is attempting to uninstall and reinstall the GitHub or GitLab application associated with the Cloudflare Pages installation.</p>
<ol>
<li>Go to your application settings page on GitLab located here: <a href="https://gitlab.com/-/profile/applications">https://gitlab.com/-/profile/applications</a></li>
<li>Select the <strong>Revoke</strong> button on your Cloudflare Pages installation if it exists.</li>
<li>Go back to the <strong>Workers &amp; Pages</strong> overview page at <code>https://dash.cloudflare.com/[YOUR_ACCOUNT_ID]/workers-and-pages</code>. Select <strong>Create application</strong> &gt; <strong>Pages</strong> &gt; <strong>Connect to Git</strong>.</li>
<li>Select the <strong>GitLab</strong> tab at the top, select the <strong>+ Add account</strong> button, select the GitLab account you want to add, and then select <strong>Authorize</strong> on the modal titled &quot;Authorize Cloudflare Pages to use your account?&quot;.</li>
<li>You will be redirected to the create project page with your GitLab account or organization in the account list.</li>
<li>Attempt to make a new deployment with your project which was previously broken.</li>
</ol>
