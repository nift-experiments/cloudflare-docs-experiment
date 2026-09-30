---
cp9:
  canonical: https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/gitlab-integration/
  description: Learn how to manage your GitLab integration for Workers Builds
  full_title: GitLab integration · Cloudflare Workers docs
  head_html: <title>GitLab integration · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to manage your GitLab integration for Workers Builds"><link rel="canonical" href="https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/gitlab-integration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/gitlab-integration/index.md"><meta property="og:title" content="GitLab integration · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to manage your GitLab integration for Workers Builds"><meta property="og:url" content="https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/gitlab-integration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/gitlab-integration/#page","headline":"GitLab integration \u00b7 Cloudflare Workers docs","description":"Learn how to manage your GitLab integration for Workers Builds","url":"https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/gitlab-integration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/ci-cd/builds/git-integration/gitlab-integration/
  schema: 1
---
<p>Cloudflare supports connecting your GitLab repository to your Cloudflare Worker, and will automatically deploy your code every time you push a change.</p>
<h2 id="features">Features</h2>
<p>Beyond automatic builds and deployments, the Cloudflare GitLab integration lets you monitor builds directly in GitLab, keeping you informed without leaving your workflow.</p>
<h3 id="merge-request-comment">Merge request comment</h3>
<p>If a commit is on a merge request, Cloudflare will automatically post a comment on the merge request with the status of the build.</p>
<p><img src="/assets/upstream/images/workers/platform/ci-cd/gitlab-pull-request-comment.png" alt="GitLab merge request comment" /></p>
<p>A <a href="/workers/versions-and-deployments/preview-urls/">preview URL</a> will be provided for any builds which perform <code>wrangler versions upload</code>. This is particularly useful when reviewing your pull request, as it allows you to compare the code changes alongside an updated version of your Worker.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16791.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="enabling-gitlab-merge-request-events-for-existing-connections">Enabling GitLab Merge Request events for existing connections</h3>
@markup("md", "content/.markup/bodies/16790.md")
</aside>
<h3 id="commit-status">Commit Status</h3>
<p>If you have one or multiple Workers connected to a repository (i.e. a <a href="/workers/ci-cd/builds/advanced-setups/#monorepos">monorepo</a>), you can check on the status of each build within GitLab via <a href="https://docs.gitlab.com/ee/user/project/merge_requests/status_checks.html">GitLab commit status</a>.</p>
<p>You can see the statuses by selecting the status icon next to a commit or by going to <strong>Build</strong> &gt; <strong>Pipelines</strong> within your GitLab repository. In the example below, you can select on the green check mark to see the results of the check run.</p>
<p><img src="/assets/upstream/images/workers/platform/ci-cd/gl-status-checks.png" alt="GitLab Status" /></p>
<p>Check runs will appear like the following in your repository. You can select one of the statuses to view the build on the Cloudflare Dashboard.</p>
<p><img src="/assets/upstream/images/workers/platform/ci-cd/gl-commit-status.png" alt="GitLab Commit Status" /></p>
<p>Note that when using <a href="/workers/ci-cd/builds/build-watch-paths/">build watch paths</a>, only projects that trigger a build will generate a commit status.</p>
<h2 id="manage-access">Manage access</h2>
<p>You can deploy projects to Cloudflare Workers from your company or side project on GitLab using the Cloudflare Pages app.</p>
<h3 id="organizational-access">Organizational access</h3>
<p>When you authorize Cloudflare Workers to access your GitLab account, you automatically give Cloudflare Workers access to organizations, groups, and namespaces accessed by your GitLab account. Managing access to these organizations and groups is handled by GitLab.</p>
<h3 id="remove-access">Remove access</h3>
<p>You can remove Cloudflare Workers' access to your GitLab account by navigating to <a href="https://gitlab.com/-/profile/applications">Authorized Applications page</a> on GitLab. Find the applications called Cloudflare Pages and select the <strong>Revoke</strong> button to revoke access.</p>
<p>Note that the GitLab application Cloudflare Workers is shared between Workers and Pages projects, and removing access to GitLab will disable new builds for Workers and Pages, though your previous deployments will continue to be hosted by Cloudflare Workers.</p>
<h3 id="reinstall-the-cloudflare-gitlab-app">Reinstall the Cloudflare GitLab App</h3>
<ol>
<li>Go to your application settings page on GitLab: <a href="https://gitlab.com/-/profile/applications">https://gitlab.com/-/profile/applications</a></li>
<li>Click the &quot;Revoke&quot; button on your Cloudflare Workers installation if it exists.</li>
<li>Go back to the <a href="https://dash.cloudflare.com"><strong>Workers &amp; Pages</strong> overview</a> page. Select <strong>Create application</strong> &gt; <strong>Pages</strong> &gt; <strong>Connect to Git</strong>.</li>
<li>Select the <strong>+ Add account</strong> button, select the GitLab account you want to add, and then select <strong>Install &amp; Authorize</strong>.</li>
<li>You should be redirected to the create project page with your GitLab account or organization in the account list.</li>
<li>Attempt to make a new deployment with your project which was previously broken.</li>
</ol>
