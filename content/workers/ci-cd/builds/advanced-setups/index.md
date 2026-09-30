---
cp9:
  canonical: https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/
  description: Learn how to use Workers Builds with more advanced setups
  full_title: Advanced setups · Cloudflare Workers docs
  head_html: <title>Advanced setups · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to use Workers Builds with more advanced setups"><link rel="canonical" href="https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/index.md"><meta property="og:title" content="Advanced setups · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to use Workers Builds with more advanced setups"><meta property="og:url" content="https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/#page","headline":"Advanced setups \u00b7 Cloudflare Workers docs","description":"Learn how to use Workers Builds with more advanced setups","url":"https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/ci-cd/builds/advanced-setups/
  schema: 1
---
<h2 id="monorepos">Monorepos</h2>
<p>A monorepo is a single repository that contains multiple applications. This setup can be useful for a few reasons:</p>
<ul>
<li><strong>Simplified dependency management</strong>: Manage dependencies across all your workers and shared packages from a single place using tools like <a href="https://pnpm.io/workspaces">pnpm workspaces</a> and <a href="https://syncpack.dev/">syncpack</a>.</li>
<li><strong>Code sharing and reuse</strong>: Easily create and share common logic, types, and utilities between workers by creating shared packages.</li>
<li><strong>Atomic commits</strong>: Changes affecting multiple workers or shared libraries can be committed together, making the history easier to understand and reducing the risk of inconsistencies.</li>
<li><strong>Consistent tooling</strong>: Apply the same build, test, linting, and formatting configurations (e.g., via <a href="https://turborepo.com">Turborepo</a> for task orchestration and shared configs in <code>packages/</code>) across all projects, ensuring consistent tooling and code quality across Workers.</li>
<li><strong>Easier refactoring</strong>: Refactoring code that spans multiple Workers or shared packages is significantly easier within a single repository.</li>
</ul>
<h4 id="example-workers-monorepos">Example Workers monorepos:</h4>
<ul>
<li><a href="https://github.com/cloudflare/mcp-server-cloudflare">cloudflare/mcp-server-cloudflare</a></li>
<li><a href="https://github.com/jahands/workers-monorepo-template">jahands/workers-monorepo-template</a></li>
<li><a href="https://github.com/cloudflare/templates">cloudflare/templates</a></li>
<li><a href="https://github.com/cloudflare/workers-sdk">cloudflare/workers-sdk</a></li>
</ul>
<h3 id="getting-started">Getting Started</h3>
<p>To set up a monorepo workflow:</p>
<ol>
<li>Find the Workers associated with your project in the <a href="https://dash.cloudflare.com">Workers &amp; Pages Dashboard</a>.</li>
<li>Connect your monorepo to each Worker in the repository.</li>
<li>Set the root directory for each Worker to specify the location of its <code>wrangler.jsonc</code> and where build and deploy commands should run.</li>
<li>Optionally, configure unique build and deploy commands for each Worker.</li>
<li>Optionally, configure <a href="/workers/ci-cd/builds/build-watch-paths/">build watch paths</a> for each Worker to monitor specific paths for changes.</li>
</ol>
<p>When a new commit is made to the monorepo, a new build and deploy will trigger for each Worker if the change is within each of its included watch paths. You can also check on the status of each build associated with your repository within GitHub with <a href="/workers/ci-cd/builds/git-integration/github-integration/#check-run">check runs</a> or within GitLab with <a href="/workers/ci-cd/builds/git-integration/gitlab-integration/#commit-status">commit statuses</a>.</p>
<h3 id="example">Example</h3>
<p>In the example <code>ecommerce-monorepo</code>, a Workers project should be created for <code>product-service</code>, <code>order-service</code>, and <code>notification-service</code>.</p>
<p>A Git connection to <code>ecommerce-monorepo</code> should be added in all of the Workers projects. If you are using a monorepo tool, such as <a href="https://turbo.build/">Turborepo</a>, you can configure a different deploy command for each Worker, for example, <code>turbo deploy -F product-service</code>.</p>
<p>Set the root directory of each Worker to where its Wrangler configuration file is located. For example, for <code>product-service</code>, the root directory should be <code>/workers/product-service/</code>. Optionally, you can add <a href="/workers/ci-cd/builds/build-watch-paths/">build watch paths</a> to optimize your builds.</p>
<p>When a new commit is made to <code>ecommerce-monorepo</code>, a build and deploy will be triggered for each of the Workers if the change is within its included watch paths using the configured commands for that Worker.</p>
<pre tabindex="0" class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/16788.md")&#10;&#10;&#10;</pre>
<h2 id="wrangler-environments">Wrangler Environments</h2>
<p>You can use <a href="/workers/wrangler/environments/">Wrangler Environments</a> with Workers Builds by completing the following steps:</p>
<ol>
<li><a href="/workers/wrangler/commands/general/#deploy">Deploy via Wrangler</a> to create the Workers for your environments on the Dashboard, if you do not already have them.</li>
<li>Find the Workers for your environments. They are typically named <code>[name of Worker] - [environment name]</code>.</li>
<li>Connect your repository to each of the Workers for your environment.</li>
<li>In each of the Workers, edit your Wrangler commands to include the flag <code>--env: &lt;environment name&gt;</code> in the build configurations for both the deploy command, and the non-production branch deploy command (<a href="/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds">if applicable</a>).</li>
</ol>
<p>When a new commit is detected in the repository, a new build/deploy will trigger for each associated Worker.</p>
<h3 id="example-1">Example</h3>
<p>Imagine you have a Worker named <code>my-worker</code>, and you want to set up two environments <code>staging</code> and <code>production</code> set in the <code>wrangler.jsonc</code>. If you have not already, you can deploy <code>my-worker</code> for each environment using the commands <code>wrangler deploy --env staging</code> and <code>wrangler deploy --env production</code>.</p>
<p>In your Cloudflare Dashboard, you should find the two Workers <code>my-worker-staging</code> and <code>my-worker-production</code>. Then, connect the Git repository for the Worker, <code>my-worker</code>, to both of the environment Workers. In the build configurations of each environment Worker, edit the deploy commands to be <code>npx wrangler deploy --env staging</code> and <code>npx wrangler deploy --env production</code> and the non-production branch deploy commands to be <code>npx wrangler versions upload --env staging</code> and <code>npx wrangler versions upload --env production</code> respectively.</p>
