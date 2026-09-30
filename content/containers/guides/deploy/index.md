---
cp9:
  canonical: https://developers.cloudflare.com/containers/guides/deploy/
  description: Deploy from your machine or Workers Builds, including how images and container instances update.
  full_title: Deploy Containers · Cloudflare Containers docs
  head_html: <title>Deploy Containers · Cloudflare Containers docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy from your machine or Workers Builds, including how images and container instances update."><link rel="canonical" href="https://developers.cloudflare.com/containers/guides/deploy/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/containers/guides/deploy/index.md"><meta property="og:title" content="Deploy Containers · Cloudflare Containers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy from your machine or Workers Builds, including how images and container instances update."><meta property="og:url" content="https://developers.cloudflare.com/containers/guides/deploy/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Containers"><meta name="algolia_product_filter" content="Containers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Containers,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/containers/guides/deploy/#page","headline":"Deploy Containers \u00b7 Cloudflare Containers docs","description":"Deploy from your machine or Workers Builds, including how images and container instances update.","url":"https://developers.cloudflare.com/containers/guides/deploy/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /containers/guides/deploy/
  schema: 1
---
<h2 id="deploy-from-your-machine">Deploy from your machine</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7131.md")
</div>
<p><code>wrangler deploy</code> uploads and activates your Worker before it processes the container configuration. For a Dockerfile image, Wrangler then builds and pushes the image when needed. For a registry image, it uses the configured image reference. These steps are not transactional: an image build, image push, or <a href="/containers/configuration/rollouts/">rollout</a> error can happen after the new Worker is already live.</p>
<p>For an existing container application, Wrangler starts a rollout when the effective container configuration changes. The command does not wait for every container instance to be replaced, so new Worker code may briefly talk to containers that still run the previous image. The first deploy creates the container application directly, and a deploy with no effective container changes starts no rollout.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="first-deploy">First deploy</h3>
@markup("md", "content/.markup/bodies/7130.md")
</aside>
<p>For rollout flags and step configuration, refer to <a href="/containers/configuration/rollouts/">Rollouts</a>.</p>
<h2 id="deploy-with-workers-builds">Deploy with Workers Builds</h2>
<p><a href="/workers/ci-cd/builds/">Workers Builds</a> runs the build and deploy commands you configure for the Worker that is connected to your Git repository.</p>
<table>
<thead>
<tr>
<th>Git branch</th>
<th>Default deploy command</th>
<th>Containers</th>
</tr>
</thead>
<tbody>
<tr>
<td>Production branch</td>
<td><code>npx wrangler deploy</code></td>
<td>Publishes the image when needed and rolls out container instances. Dockerfile builds can run in the Workers Builds environment.</td>
</tr>
<tr>
<td>Other branches (if <a href="/workers/ci-cd/builds/build-branches/">non-production branch builds</a> are enabled)</td>
<td><code>npx wrangler versions upload</code></td>
<td>Uploads Worker code only. Does not publish a new image or roll out container instances.</td>
</tr>
</tbody>
</table>
<h3 id="production">Production</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7132.md")
</div>
<p>To connect a repository, refer to <a href="/workers/ci-cd/builds/">Workers Builds</a>.</p>
<h3 id="before-production">Before production</h3>
<ul>
<li><strong><code>wrangler deploy</code></strong> publishes container images (when needed) and rolls out container instances for the Worker you deploy.</li>
<li><strong><code>wrangler versions upload</code></strong> (the default non-production branch deploy command in Workers Builds) uploads a new Worker version only. It does not publish a new image or roll out container instances.</li>
<li><strong><a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a> are not generated for Workers that implement <a href="/durable-objects/">Durable Objects</a></strong>, which includes Containers Workers. A successful non-production Workers Builds run still creates a Worker version, but not a full-app preview URL.</li>
</ul>
<table>
<thead>
<tr>
<th>Goal</th>
<th>What to do</th>
</tr>
</thead>
<tbody>
<tr>
<td>Change Worker and container together on your machine</td>
<td><a href="/containers/guides/local-dev/">Local development</a> with <code>wrangler dev</code></td>
</tr>
<tr>
<td>Share a deployed environment with its own image and container instances</td>
<td>A <a href="/workers/wrangler/environments/">Wrangler environment</a> or a separate Worker, each connected to Workers Builds with a full deploy command such as <code>npx wrangler deploy --env staging</code>. Refer to <a href="/workers/ci-cd/builds/advanced-setups/#wrangler-environments">Workers Builds and Wrangler environments</a>.</td>
</tr>
<tr>
<td>Update production</td>
<td>Merge to the production branch (or run <code>wrangler deploy</code> locally)</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7129.md")
</aside>
<h2 id="check-your-deploy">Check your deploy</h2>
<p>After <code>wrangler deploy</code> or a production Workers Builds deploy:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7133.md")
</div>
<p>For gradual steps, grace periods, and rollout modes, refer to <a href="/containers/configuration/rollouts/">Rollouts</a>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<table>
<thead>
<tr>
<th>Problem</th>
<th>What to do</th>
</tr>
</thead>
<tbody>
<tr>
<td>Non-production Workers Builds run succeeds but you cannot fully preview the app</td>
<td>Use <a href="/containers/guides/local-dev/">local development</a> or a staging Worker or environment with <code>wrangler deploy</code>. Refer to <a href="#before-production">Before production</a>.</td>
</tr>
<tr>
<td>Deploy or Workers Builds run succeeds but container instances look unchanged</td>
<td>A gradual rollout may still be running, or the command did not update containers (<code>versions upload</code> or <code>--containers-rollout=none</code>). Refer to <a href="/containers/configuration/rollouts/">Rollouts</a>.</td>
</tr>
<tr>
<td>Deploy fails because Docker is missing</td>
<td>Required only when <code>image</code> is a Dockerfile path. Start Docker, use Workers Builds, switch to a <a href="/containers/guides/image-management/#use-pre-built-container-images">registry image</a>, or use <code>--containers-rollout=none</code> for a Worker-only deploy.</td>
</tr>
<tr>
<td>First deploy: Worker works, container routes error</td>
<td>Wait several minutes for provisioning, then check logs.</td>
</tr>
</tbody>
</table>
<h2 id="related">Related</h2>
<ul>
<li><a href="/containers/configuration/rollouts/">Rollouts</a></li>
<li><a href="/containers/guides/image-management/">Image management</a></li>
<li><a href="/containers/guides/local-dev/">Local development</a></li>
<li><a href="/workers/ci-cd/builds/">Workers Builds</a></li>
<li><a href="/workers/wrangler/environments/">Wrangler environments</a></li>
</ul>
