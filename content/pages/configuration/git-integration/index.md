<p>You can connect each Cloudflare Pages project to a <a href="/pages/configuration/git-integration/github-integration">GitHub</a> or <a href="/pages/configuration/git-integration/gitlab-integration">GitLab</a> repository, and Cloudflare will automatically deploy your code every time you push a change to a branch.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11084.md")
</aside>
<p>When you connect a git repository to your Cloudflare Pages project, Cloudflare will also:</p>
<ul>
<li><strong>Preview deployments for custom branches</strong>, generating preview URLs for a commit to any branch in the repository without affecting your production deployment.</li>
<li><strong>Preview URLs in pull requests</strong> (PRs) to the repository.</li>
<li><strong>Build and deployment status checks</strong> within the Git repository.</li>
<li><strong>Skipping builds using a commit message</strong>.</li>
</ul>
<p>These features allow you to manage your deployments directly within GitHub or GitLab without leaving your team's regular development workflow.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="you-cannot-switch-to-direct-upload-later">You cannot switch to Direct Upload later</h3>
@markup("md", "content/.markup/bodies/11083.md")
</aside>
<h2 id="supported-git-providers">Supported Git providers</h2>
<p>Cloudflare supports connecting Cloudflare Pages to your GitHub and GitLab repositories. Pages does not currently support connecting self-hosted instances of GitHub or GitLab.</p>
<p>If you using a different Git provider (e.g. Bitbucket) or a self-hosted instance, you can start with a Direct Upload project and deploy using a CI/CD provider (e.g. GitHub Actions) with <a href="/pages/how-to/use-direct-upload-with-continuous-integration/">Wrangler CLI</a>.</p>
<h2 id="add-a-git-integration">Add a Git integration</h2>
<p>If you do not have a Git account linked to your Cloudflare account, you will be prompted to set up an installation to GitHub or GitLab when <a href="/pages/get-started/git-integration/">connecting to Git</a> for the first time, or when adding a new Git account. Follow the prompts and authorize the Cloudflare Git integration.</p>
<p>You can check the following pages to see if your Git integration has been installed:</p>
<ul>
<li><a href="https://github.com/settings/installations">GitHub Applications page</a> (if you're in an organization, select <strong>Switch settings context</strong> to access your GitHub organization settings)</li>
<li><a href="https://gitlab.com/-/profile/applications">GitLab Authorized Applications page</a></li>
</ul>
<p>For details on providing access to organization accounts, see the <a href="/pages/configuration/git-integration/github-integration/#organizational-access">GitHub</a> and <a href="/pages/configuration/git-integration/gitlab-integration/#organizational-access">GitLab</a> guides.</p>
<h2 id="manage-a-git-integration">Manage a Git integration</h2>
<p>You can manage the Git installation associated with your repository connection by navigating to the Pages project, then going to <strong>Settings</strong> &gt; <strong>Builds</strong> and selecting <strong>Manage</strong> under <strong>Git Repository</strong>.</p>
<p>This can be useful for managing repository access or troubleshooting installation issues by reinstalling. For more details, see the <a href="/pages/configuration/git-integration/github-integration/#managing-access">GitHub</a> and <a href="/pages/configuration/git-integration/gitlab-integration/#managing-access">GitLab</a> guides.</p>
<h2 id="disable-automatic-deployments">Disable automatic deployments</h2>
<p>If you are using a Git-integrated project and do not want to trigger deployments every time you push a commit, you can use <a href="/pages/configuration/branch-build-controls/">branch control</a> to disable/pause builds:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11085.md")
</div>
<p>Then, you can use Wrangler to deploy directly to your Pages project and make changes to your Git repository without automatically triggering a build.</p>
