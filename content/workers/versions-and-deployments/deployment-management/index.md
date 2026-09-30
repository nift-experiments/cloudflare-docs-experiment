---
cp9:
  canonical: https://developers.cloudflare.com/workers/versions-and-deployments/deployment-management/
  description: Upload versions independently and control when and how they are deployed to your Worker's traffic.
  full_title: Deployment management · Cloudflare Workers docs
  head_html: <title>Deployment management · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Upload versions independently and control when and how they are deployed to your Worker&#x27;s traffic."><link rel="canonical" href="https://developers.cloudflare.com/workers/versions-and-deployments/deployment-management/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/versions-and-deployments/deployment-management/index.md"><meta property="og:title" content="Deployment management · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upload versions independently and control when and how they are deployed to your Worker&#x27;s traffic."><meta property="og:url" content="https://developers.cloudflare.com/workers/versions-and-deployments/deployment-management/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/versions-and-deployments/deployment-management/#page","headline":"Deployment management \u00b7 Cloudflare Workers docs","description":"Upload versions independently and control when and how they are deployed to your Worker's traffic.","url":"https://developers.cloudflare.com/workers/versions-and-deployments/deployment-management/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/versions-and-deployments/deployment-management/
  schema: 1
---
<p>By default, a new version is created and immediately deployed to 100% of traffic when you use any of the following:</p>
<ul>
<li><a href="/workers/wrangler/commands/workers/#deploy"><code>wrangler deploy</code></a></li>
<li><a href="/workers/ci-cd/builds/">Workers Builds</a></li>
<li>The <a href="/api/resources/workers/subresources/scripts/methods/update/">Workers Script Upload API</a></li>
</ul>
<p>You can separate these steps so that uploading a version and deploying it are independent actions. This lets you control exactly when a new version goes live.</p>
<h2 id="upload-a-version-without-deploying">Upload a version without deploying</h2>
<h3 id="via-wrangler">Via Wrangler</h3>
<p>Use the <a href="/workers/wrangler/commands/workers/#versions-upload"><code>wrangler versions upload</code></a> command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler versions upload</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler versions upload" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler versions upload</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler versions upload" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler versions upload</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler versions upload" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16047.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16046.md")
</aside>
<h3 id="via-the-cloudflare-dashboard">Via the Cloudflare dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Worker &gt; <strong>Edit code</strong>.</li>
<li>Make your changes, then select the <strong>down arrow</strong> next to <strong>Deploy</strong> &gt; <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16045.md")
</aside>
<h2 id="deploy-an-uploaded-version">Deploy an uploaded version</h2>
<p>Once you have uploaded a version, you can create a deployment that routes traffic to it.</p>
<h3 id="via-wrangler-1">Via Wrangler</h3>
<p>Use the <a href="/workers/wrangler/commands/workers/#versions-deploy"><code>wrangler versions deploy</code></a> command and follow the interactive prompts to select the version and set it to 100%:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler versions deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler versions deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler versions deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler versions deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler versions deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler versions deploy" aria-label="Copy to clipboard">Copy</button></div></div>
<p>You can also set the traffic percentage to less than 100% to start a <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployment</a>.</p>
<h3 id="via-the-cloudflare-dashboard-1">Via the Cloudflare dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Worker &gt; <strong>Deployments</strong>.</li>
<li>Select <strong>Promote deployment</strong> and choose the version you want to deploy.</li>
</ol>
<h3 id="via-infrastructure-as-code">Via Infrastructure as Code</h3>
<p>You can also create versions and deployments directly with the API, library SDKs, and Terraform. Refer to <a href="/workers/platform/infrastructure-as-code/">Infrastructure as Code</a> for examples.</p>
<h2 id="limits">Limits</h2>
<h3 id="deployments-limit">Deployments limit</h3>
<p>You can only create a deployment with the last 100 uploaded versions of your Worker.</p>
<h3 id="first-upload">First upload</h3>
<p>You must use <a href="/workers/get-started/guide/#1-create-a-new-worker-project">C3</a> or <a href="/workers/wrangler/commands/workers/#deploy"><code>wrangler deploy</code></a> the first time you create a new Workers project. Using <a href="/workers/wrangler/commands/workers/#versions-upload"><code>wrangler versions upload</code></a> the first time you upload a Worker will fail.</p>
<h3 id="service-worker-syntax">Service worker syntax</h3>
<p>Service worker syntax is not supported for versions that are uploaded through <a href="/workers/wrangler/commands/workers/#versions-upload"><code>wrangler versions upload</code></a>. You must use ES modules format.</p>
<p>Refer to <a href="/workers/reference/migrate-to-module-workers/#advantages-of-migrating">Migrate from Service Workers to ES modules</a> to learn how to migrate your Workers from the service worker format to the ES modules format.</p>
<h3 id="durable-object-migrations">Durable Object migrations</h3>
<p>Uploading a version that changes Durable Object class lifecycle is not supported. This applies to both the declarative <a href="/durable-objects/reference/durable-objects-migrations/"><code>exports</code></a> field and the legacy <a href="/durable-objects/reference/durable-object-class-migrations-legacy/"><code>migrations</code></a> array - any change that creates, deletes, renames, or transfers a Durable Object class must be applied through <a href="/workers/wrangler/commands/workers/#deploy"><code>wrangler deploy</code></a>.</p>
