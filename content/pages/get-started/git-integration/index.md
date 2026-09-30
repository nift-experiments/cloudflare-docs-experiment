---
cp9:
  canonical: https://developers.cloudflare.com/pages/get-started/git-integration/
  description: Connect your Git provider to Pages.
  full_title: Git integration guide · Cloudflare Pages docs
  head_html: <title>Git integration guide · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect your Git provider to Pages."><link rel="canonical" href="https://developers.cloudflare.com/pages/get-started/git-integration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/get-started/git-integration/index.md"><meta property="og:title" content="Git integration guide · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect your Git provider to Pages."><meta property="og:url" content="https://developers.cloudflare.com/pages/get-started/git-integration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/get-started/git-integration/#page","headline":"Git integration guide \u00b7 Cloudflare Pages docs","description":"Connect your Git provider to Pages.","url":"https://developers.cloudflare.com/pages/get-started/git-integration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/get-started/git-integration/
  schema: 1
---
<p>In this guide, you will get started with Cloudflare Pages and deploy your first website to the Pages platform through Git integration. The Git integration enables automatic builds and deployments every time you push a change to your connected <a href="/pages/configuration/git-integration/github-integration/">GitHub</a> or <a href="/pages/configuration/git-integration/gitlab-integration/">GitLab</a> repository.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="you-cannot-switch-to-direct-upload-later">You cannot switch to Direct Upload later</h3>
@markup("md", "content/.markup/bodies/10905.md")
</aside>
<h2 id="connect-your-git-provider-to-pages">Connect your Git provider to Pages</h2>
<p>Pages offers support for <a href="https://github.com/">GitHub</a> and <a href="https://gitlab.com/">GitLab</a>. To create your first Pages project:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Create application** > **Pages** > **Connect to Git**.
<p>You will be prompted to sign in with your preferred Git provider. This allows Cloudflare Pages to deploy your projects, and update your PRs with <a href="/pages/configuration/preview-deployments/">preview deployments</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10904.md")
</aside>
<h3 id="select-your-github-repository">Select your GitHub repository</h3>
<p>You can select a GitHub project from your personal account or an organization you have given Pages access to. This allows you to choose a GitHub repository to deploy using Pages. Both private and public repositories are supported.</p>
<h3 id="select-your-gitlab-repository">Select your GitLab repository</h3>
<p>If using GitLab, you can select a project from your personal account or from a GitLab group you belong to. This allows you to choose a GitLab repository to deploy using Pages. Both private and public repositories are supported.</p>
<h2 id="configure-your-deployment">Configure your deployment</h2>
<p>Once you have selected a Git repository, select <strong>Install &amp; Authorize</strong> and <strong>Begin setup</strong>. You can then customize your deployment in <strong>Set up builds and deployments</strong>.</p>
<p>Your <strong>project name</strong> will be used to generate your project's hostname. By default, this matches your Git project name.</p>
<p><strong>Production branch</strong> indicates the branch that Cloudflare Pages should use to deploy the production version of your site. For most projects, this is the <code>main</code> or <code>master</code> branch. All other branches that are not your production branch will be used for <a href="/pages/configuration/preview-deployments/">preview deployments</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10903.md")
</aside>
<p><img src="/assets/upstream/images/pages/get-started/configuration.png" alt="Set up builds and deployments page with Project name and Production branch filled in" /></p>
<h3 id="configure-your-build-settings">Configure your build settings</h3>
<p>Depending on the framework, tool, or project you are deploying to Cloudflare Pages, you will need to specify the site's <strong>build command</strong> and <strong>build output directory</strong> to tell Cloudflare Pages how to deploy your site. The content of this directory is uploaded to Cloudflare Pages as your website's content.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="no-framework-required">No framework required</h3>
@markup("md", "content/.markup/bodies/10902.md")
</aside>
<p>The dashboard provides a number of framework-specific presets. These presets provide the default build command and build output directory values for the selected framework. If you are unsure what the correct values are for this section, refer to <a href="/pages/configuration/build-configuration/">Build configuration</a>. If you do not need a build step, leave the <strong>Build command</strong> field blank.</p>
<p><img src="/assets/upstream/images/pages/get-started/build-settings.png" alt="Build setting fields that need to be filled in" /></p>
<p>Cloudflare Pages begins by working from your repository's root directory. The entire build pipeline, including the installation steps, will begin from this location. If you would like to change this, specify a new root directory location through the <strong>Root directory (advanced)</strong> &gt; <strong>Path</strong> field.</p>
<p><img src="/assets/upstream/images/pages/get-started/root-directory.png" alt="Root directory field to be filled in" /></p>
<details class="nb-details"><summary>Understanding your build configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10906.md")
</div></details>
<h3 id="environment-variables">Environment variables</h3>
<p>Environment variables are a common way of providing configuration to your build workflow. While setting up your project, you can specify a number of key-value pairs as environment variables. These can be further customized once your project has finished building for the first time.</p>
<p>Refer to the <a href="/pages/framework-guides/deploy-a-hexo-site/#using-a-specific-nodejs-version">Hexo framework guide</a> for more information on how to set up a Node.js version environment variable.</p>
<p>After you have chosen your <em>Framework preset</em> or left this field blank if you are working without a framework, configured <strong>Root directory (advanced)</strong>, and customized your <strong>Environment variables (optional)</strong>, you are ready to deploy.</p>
<h2 id="your-first-deploy">Your first deploy</h2>
<p>After you have finished setting your build configuration, select <strong>Save and Deploy</strong>. Your project build logs will output as Cloudflare Pages installs your project dependencies, builds the project, and deploys it to Cloudflare's global network.</p>
<p><img src="/assets/upstream/images/pages/get-started/deploy-log.png" alt="Deployment details in the Cloudflare dashboard" /></p>
<p>When your project has finished deploying, you will receive a unique URL to view your deployed site.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="dns-errors">DNS errors</h3>
@markup("md", "content/.markup/bodies/10901.md")
</aside>
<h2 id="manage-site">Manage site</h2>
<p>After your first deploy, select <strong>Continue to project</strong> to see your project's configuration in the Cloudflare Pages dashboard. On this page, you can see your project's current deployment status, the production URL and associated commit, and all past deployments.</p>
<p><img src="/assets/upstream/images/pages/get-started/site-dashboard.png" alt="Site dashboard displaying your environments and deployments" /></p>
<h3 id="delete-a-project">Delete a project</h3>
<p>To delete your Pages project:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project > **Settings** > **Delete project**.
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10900.md")
</aside>
<h2 id="advanced-project-settings">Advanced project settings</h2>
<p>In the <strong>Settings</strong> section, you can configure advanced settings, such as changing your project name, updating your Git configuration, or updating your build command, build directory or environment variables.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Set up a <a href="/pages/configuration/custom-domains/">custom domain for your Pages project</a>.</li>
<li>Enable <a href="/pages/how-to/web-analytics/">Cloudflare Web Analytics</a>.</li>
<li>Set up Access policies to <a href="/pages/configuration/preview-deployments/#customize-preview-deployments-access">manage who can view your deployment previews</a>.</li>
</ul>
