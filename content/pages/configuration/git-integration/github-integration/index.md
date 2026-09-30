---
cp9:
  canonical: https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/
  description: Connect a GitHub repository to Cloudflare Pages for automatic deployments, preview URLs, and check runs.
  full_title: GitHub integration · Cloudflare Pages docs
  head_html: <title>GitHub integration · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect a GitHub repository to Cloudflare Pages for automatic deployments, preview URLs, and check runs."><link rel="canonical" href="https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/index.md"><meta property="og:title" content="GitHub integration · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect a GitHub repository to Cloudflare Pages for automatic deployments, preview URLs, and check runs."><meta property="og:url" content="https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/#page","headline":"GitHub integration \u00b7 Cloudflare Pages docs","description":"Connect a GitHub repository to Cloudflare Pages for automatic deployments, preview URLs, and check runs.","url":"https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/configuration/git-integration/github-integration/
  schema: 1
---
<p>You can connect each Cloudflare Pages project to a GitHub repository, and Cloudflare will automatically deploy your code every time you push a change to a branch.</p>
<h2 id="features">Features</h2>
<p>Beyond automatic deployments, the Cloudflare GitHub integration lets you monitor, manage, and preview deployments directly in GitHub, keeping you informed without leaving your workflow.</p>
<h3 id="custom-branches">Custom branches</h3>
<p>Pages will default to setting your <a href="/pages/configuration/branch-build-controls/#production-branch-control">production environment</a> to the branch you first push. If a branch other than the default branch (e.g. <code>main</code>) represents your project's production branch, then go to <strong>Settings</strong> &gt; <strong>Builds</strong> &gt; <strong>Branch control</strong>, change the production branch by clicking the <strong>Production branch</strong> dropdown menu and choose any other branch.</p>
<p>You can also use <a href="/pages/configuration/preview-deployments/">preview deployments</a> to preview versions of your project before merging your production branch, and deploying to production. Pages allows you to configure which of your preview branches are automatically deployed using <a href="/pages/configuration/branch-build-controls/">branch build controls</a>. To configure, go to <strong>Settings</strong> &gt; <strong>Builds</strong> &gt; <strong>Branch control</strong> and select an option under <strong>Preview branch</strong>. Use <a href="/pages/configuration/branch-build-controls/"><strong>Custom branches</strong></a> to specify branches you wish to include or exclude from automatic preview deployments.</p>
<h3 id="preview-urls">Preview URLs</h3>
<p>Every time you open a new pull request on your GitHub repository, Cloudflare Pages will create a unique preview URL, which will stay updated as you continue to push new commits to the branch. Note that preview URLs will not be created for pull requests created from forks of your repository. Learn more in <a href="/pages/configuration/preview-deployments/">Preview Deployments</a>.</p>
<p><img src="/assets/upstream/images/pages/configuration/ghpreviewurls.png" alt="GitHub Preview URLs" /></p>
<h3 id="skipping-a-build-via-a-commit-message">Skipping a build via a commit message</h3>
<p>Without any configuration required, you can choose to skip a deployment on an ad hoc basis. By adding the <code>[CI Skip]</code>, <code>[CI-Skip]</code>, <code>[Skip CI]</code>, <code>[Skip-CI]</code>, or <code>[CF-Pages-Skip]</code> flag as a prefix in your commit message, Pages will omit that deployment. The prefixes are not case sensitive.</p>
<h3 id="check-runs">Check runs</h3>
<p>If you have one or multiple projects connected to a repository (i.e. a <a href="/pages/configuration/monorepos/">monorepo</a>), you can check on the status of each build within GitHub via <a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks#checks">GitHub check runs</a>.</p>
<p>You can see the checks by selecting the status icon next to a commit within your GitHub repository. In the example below, you can select the green check mark to see the results of the check run.</p>
<p><img src="/assets/upstream/images/workers/platform/ci-cd/gh-status-check-runs.png" alt="GitHub status" /></p>
<p>Check runs will appear like the following in your repository.</p>
<p><img src="/assets/upstream/images/pages/configuration/ghcheckrun.png" alt="GitHub check runs" /></p>
<p>If a build skips for any reason (i.e. CI Skip, build watch paths, or branch deployment controls), the check run/commit status will not appear.</p>
<h2 id="manage-access">Manage access</h2>
<p>You can deploy projects to Cloudflare Workers from your company or side project on GitHub using the <a href="https://github.com/apps/cloudflare-workers-and-pages">Cloudflare Workers &amp; Pages GitHub App</a>.</p>
<h3 id="organizational-access">Organizational access</h3>
<p>You can deploy projects to Cloudflare Pages from your company or side project on both GitHub and GitLab.</p>
<p>When authorizing Cloudflare Pages to access a GitHub account, you can specify access to your individual account or an organization that you belong to on GitHub. In order to be able to add the Cloudflare Pages installation to that organization, your user account must be an owner or have the appropriate role within the organization (that is, the GitHub Apps Manager role). More information on these roles can be seen on <a href="https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#github-app-managers">GitHub's documentation</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="github-security-consideration">GitHub security consideration</h3>
@markup("md", "content/.markup/bodies/11086.md")
</aside>
<h3 id="remove-access">Remove access</h3>
<p>You can remove Cloudflare Pages' access to your GitHub repository or account by going to the <a href="https://github.com/settings/installations">Applications page</a> on GitHub (if you are in an organization, select Switch settings context to access your GitHub organization settings). The GitHub App is named Cloudflare Workers and Pages, and it is shared between Workers and Pages projects.</p>
<h4 id="remove-cloudflare-access-to-a-github-repository">Remove Cloudflare access to a GitHub repository</h4>
<p>To remove access to an individual GitHub repository, you can navigate to <strong>Repository access</strong>. Select the <strong>Only select repositories</strong> option, and configure which repositories you would like Cloudflare to have access to.</p>
<p><img src="/assets/upstream/images/workers/platform/ci-cd/github-repository-access.png" alt="GitHub Repository Access" /></p>
<h4 id="remove-cloudflare-access-to-the-entire-github-account">Remove Cloudflare access to the entire GitHub account</h4>
<p>To remove Cloudflare Workers and Pages access to your entire Git account, you can navigate to <strong>Uninstall &quot;Cloudflare Workers and Pages&quot;</strong>, then select <strong>Uninstall</strong>. Removing access to the Cloudflare Workers and Pages app will revoke Cloudflare's access to <em>all repositories</em> from that GitHub account. If you want to only disable automatic builds and deployments, follow the <a href="/workers/ci-cd/builds/#disconnecting-builds">Disable Build</a> instructions.</p>
<p>Note that removing access to GitHub will disable new builds for Workers and Pages project that were connected to those repositories, though your previous deployments will continue to be hosted by Cloudflare Workers.</p>
<h3 id="reinstall-the-cloudflare-github-app">Reinstall the Cloudflare GitHub app</h3>
<p>If you see errors where Cloudflare Pages cannot access your git repository, you should attempt to uninstall and reinstall the GitHub application associated with the Cloudflare Pages installation.</p>
<ol>
<li>Go to the installation settings page on GitHub:
<ul>
<li>Navigate to <strong>Settings &gt; Builds</strong> for the Pages project and select <strong>Manage</strong> under Git Repository.</li>
<li>Alternatively, visit these links to find the Cloudflare Workers and Pages installation and select <strong>Configure</strong>:</li>
</ul>
</li>
</ol>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Individual</strong></td>
<td><code>https://github.com/settings/installations</code></td>
</tr>
<tr>
<td><strong>Organization</strong></td>
<td><code>https://github.com/organizations/&lt;YOUR_ORGANIZATION_NAME&gt;/settings/installations</code></td>
</tr>
</tbody>
</table>
<ol start="2">
<li>In the Cloudflare Workers and Pages GitHub App settings page, navigate to <strong>Uninstall &quot;Cloudflare Workers and Pages&quot;</strong> and select <strong>Uninstall</strong>.</li>
<li>Go back to the <a href="https://dash.cloudflare.com"><strong>Workers &amp; Pages</strong> overview</a> page. Select <strong>Create application</strong> &gt; <strong>Pages</strong> &gt; <strong>Connect to Git</strong>.</li>
<li>Select the <strong>+ Add account</strong> button, select the GitHub account you want to add, and then select <strong>Install &amp; Authorize</strong>.</li>
<li>You should be redirected to the create project page with your GitHub account or organization in the account list.</li>
<li>Attempt to make a new deployment with your project which was previously broken.</li>
</ol>
