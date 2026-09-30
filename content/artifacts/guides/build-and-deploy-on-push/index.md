---
cp9:
  canonical: https://developers.cloudflare.com/artifacts/guides/build-and-deploy-on-push/
  description: Build projects stored in Artifacts repos and deploy them as Workers or Workers for Platforms User Workers.
  full_title: Build and deploy Artifacts repos · Cloudflare Artifacts docs
  head_html: <title>Build and deploy Artifacts repos · Cloudflare Artifacts docs</title><meta name="generator" content="Nift"><meta name="description" content="Build projects stored in Artifacts repos and deploy them as Workers or Workers for Platforms User Workers."><link rel="canonical" href="https://developers.cloudflare.com/artifacts/guides/build-and-deploy-on-push/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/artifacts/guides/build-and-deploy-on-push/index.md"><meta property="og:title" content="Build and deploy Artifacts repos · Cloudflare Artifacts docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build projects stored in Artifacts repos and deploy them as Workers or Workers for Platforms User Workers."><meta property="og:url" content="https://developers.cloudflare.com/artifacts/guides/build-and-deploy-on-push/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Artifacts"><meta name="algolia_product_filter" content="Artifacts"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Artifacts"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/artifacts/guides/build-and-deploy-on-push/#page","headline":"Build and deploy Artifacts repos \u00b7 Cloudflare Artifacts docs","description":"Build projects stored in Artifacts repos and deploy them as Workers or Workers for Platforms User Workers.","url":"https://developers.cloudflare.com/artifacts/guides/build-and-deploy-on-push/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /artifacts/guides/build-and-deploy-on-push/
  schema: 1
---
<p>Artifacts events can build and deploy projects stored in Artifacts repos. When a user or agent pushes a commit, the event triggers a <a href="/workflows/build/trigger-workflows/">Workflow instance</a>.</p>
<p>Within the Workflow, you define a continuous integration (CI) pipeline with the <code>@cloudflare/ci</code> SDK to cache dependencies, run checks, and build the project. The final step in your CI pipeline can deploy the output to a <a href="/workers/">Worker</a> or a <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> User Worker.</p>
<p>This is useful when you need to:</p>
<ul>
<li>Automatically build and deploy application code stored in Artifacts.</li>
<li>Run linting, type checking, tests, and other checks on every push.</li>
<li>Reuse dependencies when the lockfile (i.e. <code>pnpm-lock.yaml</code>) has not changed.</li>
<li>Stop deployment when a check or build fails.</li>
<li>Restrict API token access to the deployment step.</li>
<li>Deploy the output to a <a href="/workers/">Worker</a> or a <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> User Worker.</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<div class="nb-interactive-component" data-cf-component="ArtifactsCIWorkflowDiagram"></div>
<ol>
<li><strong>Push repo changes</strong> — A <code>git push</code> to the Artifacts repo emits an <code>artifacts.repo.pushed</code> event that identifies the pushed repo, branch, and commit.</li>
<li><strong>Run the CI Workflow</strong> — The event starts a Workflow that checks out the commit, installs and caches dependencies, and runs CI steps — build, lint, typecheck, and format — in parallel. A failed step stops the Workflow before deployment.</li>
<li><strong>Deploy the Worker</strong> — The Workflow deploys the built Worker either directly to your account or as a User Worker, if using Workers for Platforms</li>
</ol>
<h3 id="run-the-ci-workflow">Run the CI Workflow</h3>
<p>Use the <code>@cloudflare/ci</code> SDK to define the CI steps. The SDK provides two tools to help you build the pipeline:</p>
<ul>
<li><strong>Runners</strong> — each <code>runner()</code> call spins up an isolated sandbox and executes a shell command. You use the same commands you already run locally or in another CI system. Each runner captures its own logs, status, and output files.</li>
<li><strong>Cache</strong> — the <code>cache</code> option on a runner caches installed dependencies so that later runs do not reinstall them. Pass the files that determine the dependencies, such as <code>pnpm-lock.yaml</code>, to <code>cache.inputs</code>. When those files have not changed, the SDK restores the cached result instead of running the command again.</li>
</ul>
<p><img src="/assets/upstream/images/artifacts/snapshot-cache-flow.svg" alt="Diagram showing three sequential commits: commit 1 has a cache miss so the install step runs and its sandbox snapshot is cached; commit 2 has an unchanged pnpm-lock.yaml so the cache key matches and the cached snapshot is served, skipping install; commit 3 has a changed pnpm-lock.yaml so the cache key misses and install runs again." /></p>
<p>A cached runner takes a <a href="/sandbox/api/backups/">snapshot</a> of its sandbox, which later runners reuse. Multiple runners can branch from the same cached result — for example, lint, type-check, and test runners can all reuse one cached install.</p>
<div class="nb-interactive-component" data-cf-component="ArtifactsCIPipelineDiagram"></div>
<p>A failed runner retries according to its <a href="/workflows/build/sleeping-and-retrying/#retry-steps">step configuration</a>, where you can define the number of retry attempts, backoff schedule, and timeouts. Runners that depend on a previous step do not start until its retry succeeds. If the configured retry limit is reached, the Workflow terminates in an <code>Errored</code> state.</p>
<p>Here is an example of how to set up your Workflow to use runners and cache to install dependencies, run checks, build the project, and deploy the Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3298.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3297.md")
</aside>
<h2 id="start-a-build-when-code-changes">Start a build when code changes</h2>
<p>When a user or agent pushes a commit to an Artifacts repo, Artifacts emits an event that identifies the repo, branch, and commit that changed. You will use this event to trigger a Workflow instance which runs a CI pipeline by automatically checking out the commit and cloning the repo before installing dependencies, running checks, building the project, and/or deploying the Worker, according to your code.</p>
<p>This guide defines those CI steps in a Workflow class named <code>CIWorkflow</code>. To start this Workflow automatically after each push, add an <code>cf.artifacts.repo.pushed</code> trigger to your Wrangler configuration. You should also include:</p>
<ul>
<li>R2 binding: the bucket where your the snapshot of your cached dependencies will be stored</li>
<li>Container (and Durable Object) binding: create a binding to your container to access sandboxes during each <code>runner()</code> step</li>
<li>Workflows binding</li>
<li>Artifacts binding</li>
<li>Observability (optional): inspect your CI jobs as a Workflow instance with <a href="/workers/observability/">Workers observability</a></li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3299.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3296.md")
</aside>
<h3 id="view-build-status">View build status</h3>
<p>The <code>[observability]</code> setting in your Wrangler configuration records the status and logs for each pipeline run. To identify which stage failed, inspect the instance in the Workflows dashboard:</p>
<div class="nb-dash-button"></div>
<p>Each runner displays its own input, output, and status, so you can identify the command that failed. When a runner fails, the Workflow records its output and does not start stages that need its files.</p>
<h2 id="deploy-the-application">Deploy the application</h2>
<p>To deploy a Worker, pass <code>wrangler deploy</code> to your final <code>runner()</code> step, i.e. <code>workspace.runner({ name: &quot;deploy&quot;, command: &quot;wrangler deploy&quot; })</code>.</p>
<p>To deploy a User Worker, pass <code>wrangler deploy --dispatch_namespace &lt;DISPATCH_NAMESPACE&gt;</code> to your final <code>runner()</code> step.</p>
<h2 id="run-one-workflow-for-every-repo-in-a-namespace">Run one workflow for every repo in a namespace</h2>
<p>The <code>filter</code> in your trigger is optional. When you set <code>repoName</code>, only pushes to that specific repo start the Workflow. When you omit <code>repoName</code>, Cloudflare runs the same Workflow for every push to any repo in your Artifacts namespace.</p>
<p>This is useful for platforms that author and own a single CI Workflow and want to apply it uniformly across every customer repo in a namespace. Instead of maintaining a separate trigger per repo, one shared Workflow builds, checks, and deploys each repo on push.</p>
<div class="nb-interactive-component" data-cf-component="ArtifactsPlatformSharedCIDiagram"></div>
<p>To run the same Workflow for every repo in a namespace, drop <code>repoName</code> from the trigger <code>filter</code> and keep only the <code>namespace</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3300.md")
</div>
<p>Each push still starts its own Workflow instance for the repo, branch, and commit that changed, so you can deploy a separate Worker per repo from the same shared Workflow definition.</p>
