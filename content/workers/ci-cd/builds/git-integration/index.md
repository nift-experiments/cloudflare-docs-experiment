<p>Cloudflare supports connecting your <a href="/workers/ci-cd/builds/git-integration/github-integration/">GitHub</a> and <a href="/workers/ci-cd/builds/git-integration/gitlab-integration/">GitLab</a> repository to your Cloudflare Worker, and will automatically deploy your code every time you push a change.</p>
<p>Adding a Git integration also lets you monitor build statuses directly in your Git provider using <a href="/workers/ci-cd/builds/git-integration/github-integration/#pull-request-comment">pull request comments</a>, <a href="/workers/ci-cd/builds/git-integration/github-integration/#check-run">check runs</a>, or <a href="/workers/ci-cd/builds/git-integration/gitlab-integration/#commit-status">commit statuses</a>, so you can manage deployments without leaving your workflow.</p>
<h2 id="supported-git-providers">Supported Git Providers</h2>
<p>Cloudflare supports connecting Cloudflare Workers to your GitHub and GitLab repositories. Workers Builds does not currently support connecting self-hosted instances of GitHub or GitLab.</p>
<p>If you are using a different Git provider (e.g. Bitbucket), you can use an <a href="/workers/ci-cd/external-cicd/">external CI/CD provider (e.g. GitHub Actions)</a> and deploy using <a href="/workers/wrangler/commands/general/#deploy">Wrangler CLI</a>.</p>
<h2 id="add-a-git-integration">Add a Git Integration</h2>
<p>Workers Builds provides direct integration with GitHub and GitLab accounts, including both individual and organization accounts, that are <em>not</em> self-hosted.</p>
<p>If you do not have a Git account linked to your Cloudflare account, you will be prompted to set up an installation to GitHub or GitLab when <a href="/workers/ci-cd/builds/#get-started">connecting a repository</a> for the first time, or when adding a new Git account. Follow the prompts and authorize the Cloudflare Git integration.</p>
<p><img src="/assets/upstream/images/workers/platform/ci-cd/workers-git-provider.png" alt="Git providers" /></p>
<p>You can check the following pages to see if your Git integration has been installed:</p>
<ul>
<li><a href="https://github.com/settings/installations">GitHub Applications page</a> (if you are in an organization, select <strong>Switch settings context</strong> to access your GitHub organization settings)</li>
<li><a href="https://gitlab.com/-/profile/applications">GitLab Authorized Applications page</a></li>
</ul>
<p>For details on providing access to organization accounts, see <a href="/workers/ci-cd/builds/git-integration/github-integration/#organizational-access">GitHub organizational access</a> and <a href="/workers/ci-cd/builds/git-integration/gitlab-integration/#organizational-access">GitLab organizational access</a>.</p>
<h2 id="manage-a-git-integration">Manage a Git Integration</h2>
<p>To manage your Git installation:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16789.md")
</div>
<p>This can be useful for managing repository access or troubleshooting installation issues by reinstalling. For more details, see the <a href="/workers/ci-cd/builds/git-integration/github-integration">GitHub</a> and <a href="/workers/ci-cd/builds/git-integration/gitlab-integration">GitLab</a> guides for how to manage your installation.</p>
