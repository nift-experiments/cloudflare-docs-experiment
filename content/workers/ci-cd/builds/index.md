---
cp9:
  canonical: https://developers.cloudflare.com/workers/ci-cd/builds/
  description: Use Workers Builds to integrate with Git and automatically build and deploy your Worker when pushing a change
  full_title: Builds · Cloudflare Workers docs
  head_html: <title>Builds · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Workers Builds to integrate with Git and automatically build and deploy your Worker when pushing a change"><link rel="canonical" href="https://developers.cloudflare.com/workers/ci-cd/builds/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/ci-cd/builds/index.md"><meta property="og:title" content="Builds · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Workers Builds to integrate with Git and automatically build and deploy your Worker when pushing a change"><meta property="og:url" content="https://developers.cloudflare.com/workers/ci-cd/builds/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/ci-cd/builds/#page","headline":"Builds \u00b7 Cloudflare Workers docs","description":"Use Workers Builds to integrate with Git and automatically build and deploy your Worker when pushing a change","url":"https://developers.cloudflare.com/workers/ci-cd/builds/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/ci-cd/builds/
  schema: 1
---
<p>The Cloudflare <a href="/workers/ci-cd/builds/git-integration/">Git integration</a> lets you connect a new or existing Worker to a GitHub or GitLab repository, enabling automated builds and deployments for your Worker on push.</p>
<h2 id="get-started">Get started</h2>
<h3 id="connect-a-new-worker">Connect a new Worker</h3>
<p>To create a new Worker and connect it to a GitHub or GitLab repository:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create application</strong>.</li>
<li>Select <strong>Get started</strong> next to <strong>Import a repository</strong>.</li>
<li>Under <strong>Import a repository</strong>, select a <strong>Git account</strong>.</li>
<li>Select the repository you want to import from the list. You can also use the search bar to narrow the results.</li>
<li>Configure your project and select <strong>Save and Deploy</strong>.</li>
<li>Preview your Worker at its provided <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code></a> subdomain.</li>
</ol>
<h3 id="connect-an-existing-worker">Connect an existing Worker</h3>
<p>To connect an existing Worker to a GitHub or GitLab repository:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the Worker you want to connect to a repository.</li>
<li>Select <strong>Settings</strong> and then <strong>Builds</strong>.</li>
<li>Select <strong>Connect</strong> and follow the prompts to connect the repository to your Worker and configure your <a href="/workers/ci-cd/builds/configuration/">build settings</a>.</li>
<li>Push a commit to your Git repository to trigger a build and deploy to your Worker.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16767.md")
</aside>
<h2 id="automatic-project-configuration">Automatic project configuration</h2>
<p>When you connect a repository that does not have a Wrangler configuration file, <a href="/workers/framework-guides/automatic-configuration/">autoconfig</a> runs to detect your framework and create a <a href="/workers/ci-cd/builds/automatic-prs/">pull request</a> to configure your project for Cloudflare Workers.</p>
<ol>
<li>Autoconfig detects your framework and generates the necessary configuration</li>
<li>A pull request is created in your repository with the necessary configuration changes</li>
<li>A preview deployment is generated so you can test before merging</li>
<li>Once you merge the PR, your project is ready for deployment</li>
</ol>
<p>For details about supported frameworks and what files are created, refer to <a href="/workers/framework-guides/automatic-configuration/">Deploy an existing project</a>. For details about the PRs created, refer to <a href="/workers/ci-cd/builds/automatic-prs/">Automatic pull requests</a>.</p>
<h2 id="view-build-and-preview-url">View build and preview URL</h2>
<p>You can monitor a build's status and its build logs by navigating to <strong>View build history</strong> at the bottom of the <strong>Deployments</strong> tab of your Worker.</p>
<p>If the build is successful, you can view the build details by selecting <strong>View build</strong> in the associated new <a href="/workers/versions-and-deployments/">version</a> created under Version History. There you will also find the <a href="/workers/versions-and-deployments/preview-urls/">preview URL</a> generated by the version under Version ID.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="builds-versions-deployments">Builds, versions, deployments</h3>
@markup("md", "content/.markup/bodies/16766.md")
</aside>
<h2 id="workers-with-containers">Workers with Containers</h2>
<p>For Workers that use <a href="/containers/">Containers</a>, use <code>wrangler deploy</code> on the production branch so container images and container instances can update. Preview builds still default to <code>wrangler versions upload</code>, which does not update container images. Preview URLs are not generated for these Workers because each container is managed from a Durable Object. Refer to <a href="/containers/guides/deploy/#before-production">Deploy Containers</a>.</p>
<h2 id="disconnecting-builds">Disconnecting builds</h2>
<p>To disconnect a Worker from a GitHub or GitLab repository:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the Worker you want to disconnect from a repository.</li>
<li>Select <strong>Settings</strong> and then <strong>Builds</strong>.</li>
<li>Select <strong>Disconnect</strong>.</li>
</ol>
<p>If you want to switch to a different repository for your Worker, you must first disable builds, then reconnect to select the new repository.</p>
<p>To disable automatic deployments while still allowing builds to run automatically and save as <a href="/workers/versions-and-deployments/">versions</a> (without promoting them to an active deployment), update your deploy command to: <code>npx wrangler versions upload</code>.</p>
