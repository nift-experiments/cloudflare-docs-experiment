---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/workers/get-started/first-worker/
  description: Build and deploy your first Worker.
  full_title: First Worker · Cloudflare Learning Paths
  head_html: <title>First Worker · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Build and deploy your first Worker."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/workers/get-started/first-worker/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/workers/get-started/first-worker/index.md"><meta property="og:title" content="First Worker · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build and deploy your first Worker."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/workers/get-started/first-worker/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/workers/get-started/first-worker/#page","headline":"First Worker \u00b7 Cloudflare Learning Paths","description":"Build and deploy your first Worker.","url":"https://developers.cloudflare.com/learning-paths/workers/get-started/first-worker/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/workers/get-started/first-worker/
  schema: 1
---
<h2 id="build-and-deploy-your-first-worker">Build and deploy your first Worker</h2>
<p>You can deploy your first Worker via the Cloudflare dashboard or programmatically using your terminal.</p>
<p>You must have a Cloudflare account to create a Worker. To get started with Cloudflare, refer to <a href="/fundamentals/account/create-account/">Create account</a>.</p>
<h3 id="via-the-cloudflare-dashboard">Via the Cloudflare dashboard</h3>
<p>To create your first Worker using the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create application</strong>.</li>
<li>Select <strong>Create Worker</strong> &gt; <strong>Deploy</strong>.</li>
</ol>
<h3 id="via-c3-and-wrangler">Via C3 and Wrangler</h3>
<h4 id="prerequisites">Prerequisites</h4>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10289.md")
</div></details>
<h4 id="create-and-deploy-your-first-worker">Create and deploy your first Worker</h4>
<p><a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3 (create-cloudflare-cli)</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare. In addition to speed, it leverages officially developed templates for Workers and framework-specific setup guides to ensure each new application that you set up follows Cloudflare and any third-party best practices for deployment on the Cloudflare network.</p>
<p>To create your Worker project, run:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- first-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- first-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare first-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare first-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest first-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest first-worker" aria-label="Copy to clipboard">Copy</button></div></div>
<p>This will prompt you to install the <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code></a> package, and lead you through setup.</p>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>JavaScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>You will be asked if you would like to deploy the project to Cloudflare.</p>
<ul>
<li>
<p>If you choose to deploy, you will be asked to authenticate (if not logged in already), and your project will be deployed to the Cloudflare global network and available on your custom <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code> subdomain</a>.</p>
</li>
<li>
<p>If you choose not to deploy, go to the newly created project directory to begin writing code. Deploy your project by running the <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> command.</p>
</li>
</ul>
<p>Refer to <a href="/workers/wrangler/commands/#how-to-run-wrangler-commands">How to run Wrangler commands</a> to learn how to run Wrangler commands according to your package manager.</p>
<p>In your Worker project directory, C3 has generated the following:</p>
<ol>
<li><code>wrangler.jsonc</code>: Your <a href="/workers/wrangler/configuration/#sample-wrangler-configuration">Wrangler</a> configuration file.</li>
<li><code>index.js</code> (in <code>/src</code>): A minimal <code>'Hello World!'</code> Worker written in <a href="/workers/reference/migrate-to-module-workers/">ES module</a> syntax.</li>
<li><code>package.json</code>: A minimal Node dependencies configuration file.</li>
<li><code>package-lock.json</code>: Refer to <a href="https://docs.npmjs.com/cli/v9/configuring-npm/package-lock-json"><code>npm</code> documentation on <code>package-lock.json</code></a>.</li>
<li><code>node_modules</code>: Refer to <a href="https://docs.npmjs.com/cli/v7/configuring-npm/folders#node-modules"><code>npm</code> documentation <code>node_modules</code></a>.</li>
</ol>
<p>To continue building your Worker, open the <code>index.js</code> file to write your code. Refer to <a href="/workers/examples/">Examples</a> to use ready-made code you can experiment with.</p>
<h2 id="summary">Summary</h2>
<p>You have learned how to:</p>
<ul>
<li>Create and deploy a Worker project using the Cloudflare dashboard and programmatically, using your terminal.</li>
</ul>
<p>In the next section, you can follow a video tutorial to create your first Cloudflare Workers application.</p>
<h3 id="related-resources">Related resources</h3>
<ul>
<li><a href="/workers/get-started/guide/">Get started guide</a> - Create a new Worker with Cloudflare Workers' Get started guide.</li>
</ul>
