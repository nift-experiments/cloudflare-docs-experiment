<p>If your git integration is experiencing issues, you may find the following banners in the Deployment page of your Pages project.</p>
<h2 id="project-creation">Project creation</h2>
<h4 id="this-repository-is-being-used-for-a-cloudflare-pages-project-on-a-different-cloudflare-account"><code>This repository is being used for a Cloudflare Pages project on a different Cloudflare account.</code></h4>
<p>Using the same GitHub/GitLab repository across separate Cloudflare accounts is disallowed. To use the repository for a Pages project in that Cloudflare account, you should delete any Pages projects using the repository in other Cloudflare accounts.</p>
<h2 id="deployments">Deployments</h2>
<p>If you run into any issues related to deployments or failing, check your project dashboard to see if there are any SCM installation warnings listed as shown in the screenshot below.</p>
<p><img src="/assets/upstream/images/pages/platform/git.dashboard-error.png" alt="Pausing a deployment in the Settings of your Pages project" /></p>
<p>To resolve any errors displayed in the Cloudflare Pages dashboard, follow the steps listed below.</p>
<h4 id="this-project-is-disconnected-from-your-git-account-this-may-cause-deployments-to-fail"><code>This project is disconnected from your Git account, this may cause deployments to fail.</code></h4>
<p>To resolve this issue, follow the steps provided above in the <a href="/pages/configuration/git-integration/#reinstall-a-git-installation">Reinstalling a Git installation section</a> for the applicable SCM provider. If the issue persists even after uninstalling and reinstalling, contact support.</p>
<h4 id="cloudflare-pages-is-not-properly-installed-on-your-git-account-this-may-cause-deployments-to-fail"><code>Cloudflare Pages is not properly installed on your Git account, this may cause deployments to fail.</code></h4>
<p>To resolve this issue, follow the steps provided above in the <a href="/pages/configuration/git-integration/#reinstall-a-git-installation">Reinstalling a Git installation section</a> for the applicable SCM provider. If the issue persists even after uninstalling and reinstalling, contact support.</p>
<h4 id="the-cloudflare-pages-installation-has-been-suspended-this-may-cause-deployments-to-fail"><code>The Cloudflare Pages installation has been suspended, this may cause deployments to fail.</code></h4>
<p>Go to your GitHub installation settings:</p>
<ul>
<li><code>https://github.com/settings/installations</code> for individual accounts</li>
<li><code>https://github.com/organizations/&lt;YOUR_ORGANIZATION_NAME&gt;/settings/installations</code> for organizational accounts</li>
</ul>
<p>Click <strong>Configure</strong> on the Cloudflare Pages application. Scroll down to the bottom of the page and click <strong>Unsuspend</strong> to allow Cloudflare Pages to make future deployments.</p>
<h4 id="the-project-is-linked-to-a-repository-that-no-longer-exists-this-may-cause-deployments-to-fail"><code>The project is linked to a repository that no longer exists, this may cause deployments to fail.</code></h4>
<p>You may have deleted or transferred the repository associated with this Cloudflare Pages project. For a deleted repository, you will need to create a new Cloudflare Pages project with a repository that has not been deleted. For a transferred repository, you can either transfer the repository back to the original Git account or you will need to create a new Cloudflare Pages project with the transferred repository.</p>
<h4 id="the-repository-cannot-be-accessed-this-may-cause-deployments-to-fail"><code>The repository cannot be accessed, this may cause deployments to fail.</code></h4>
<p>You may have excluded this repository from your installation's repository access settings. Go to your GitHub installation settings:</p>
<ul>
<li><code>https://github.com/settings/installations</code> for individual accounts</li>
<li><code>https://github.com/organizations/&lt;YOUR_ORGANIZATION_NAME&gt;/settings/installations</code> for organizational accounts</li>
</ul>
<p>Click <strong>Configure</strong> on the Cloudflare Pages application. Under <strong>Repository access</strong>, ensure that the repository associated with your Cloudflare Pages project is included in the list.</p>
<h4 id="there-is-an-internal-issue-with-your-cloudflare-pages-git-installation"><code>There is an internal issue with your Cloudflare Pages Git installation.</code></h4>
<p>This is an internal error in the Cloudflare Pages SCM system. You can attempt to <a href="/pages/configuration/git-integration/#reinstall-a-git-installation">reinstall your Git installation</a>, but if the issue persists, <a href="/support/contacting-cloudflare-support/">contact support</a>.</p>
<h4 id="github-gitlab-is-having-an-incident-and-push-events-to-cloudflare-are-operating-in-a-degraded-state-check-their-status-page-for-more-details"><code>GitHub/GitLab is having an incident and push events to Cloudflare are operating in a degraded state. Check their status page for more details.</code></h4>
<p>This indicates that GitHub or GitLab may be experiencing an incident affecting push events to Cloudflare. It is recommended to monitor their status page (<a href="https://www.githubstatus.com/">GitHub</a>, <a href="https://status.gitlab.com/">GitLab</a>) for updates and try deploying again later.</p>
