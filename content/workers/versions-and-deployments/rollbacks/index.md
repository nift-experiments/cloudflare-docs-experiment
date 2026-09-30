---
cp9:
  canonical: https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/
  description: Revert to an older version of your Worker.
  full_title: Rollbacks · Cloudflare Workers docs
  head_html: <title>Rollbacks · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Revert to an older version of your Worker."><link rel="canonical" href="https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/index.md"><meta property="og:title" content="Rollbacks · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Revert to an older version of your Worker."><meta property="og:url" content="https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/#page","headline":"Rollbacks \u00b7 Cloudflare Workers docs","description":"Revert to an older version of your Worker.","url":"https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/versions-and-deployments/rollbacks/
  schema: 1
---
<p>You can roll back to a previously deployed <a href="/workers/versions-and-deployments/#versions">version</a> of your Worker using <a href="/workers/wrangler/commands/general/#rollback">Wrangler</a> or the Cloudflare dashboard. Rolling back to a previous version of your Worker will immediately create a new <a href="/workers/versions-and-deployments/#deployments">deployment</a> with the version specified and become the active deployment across all your deployed routes and domains.</p>
<p>You can roll back from any deployment, including:</p>
<ul>
<li>A single-version deployment (rolling back replaces the current version with the selected version).</li>
<li>A <a href="/workers/versions-and-deployments/gradual-deployments/">split deployment</a> with two versions (rolling back replaces both versions with the selected version at 100% traffic).</li>
</ul>
<h2 id="via-wrangler">Via Wrangler</h2>
<p>To roll back to a specified version of your Worker via Wrangler, use the <a href="/workers/wrangler/commands/general/#rollback"><code>wrangler rollback</code></a> command.</p>
<h2 id="via-the-cloudflare-dashboard">Via the Cloudflare Dashboard</h2>
<p>To roll back to a specified version of your Worker via the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Worker &gt; <strong>Deployments</strong>.</li>
<li>Select the three dot icon on the right of the version you would like to roll back to and select <strong>Rollback</strong>.</li>
</ol>
<h2 id="rolling-back-from-a-split-deployment">Rolling back from a split deployment</h2>
<p>If you are using a <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployment</a> with two versions splitting traffic, rolling back will:</p>
<ol>
<li>Replace the split deployment with a single-version deployment.</li>
<li>Route 100% of traffic to the version you selected for rollback.</li>
</ol>
<p>This effectively promotes one version to handle all traffic, which is useful if you notice issues with one of the versions in your split deployment and want to revert to a stable version immediately.</p>
<p>To roll back from a split deployment:</p>
<ol>
<li>Identify which version in your split deployment is stable and performing correctly.</li>
<li>Use the <a href="#via-wrangler">rollback procedure</a> or <a href="#via-the-cloudflare-dashboard">dashboard rollback</a> to roll back to that version.</li>
<li>The split deployment will be replaced with the selected version at 100% traffic.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16035.md")
</aside>
<h2 id="limits">Limits</h2>
<h3 id="rollbacks-limit">Rollbacks limit</h3>
<p>You can only roll back to the 100 most recently published versions.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16034.md")
</aside>
<h3 id="bindings">Bindings</h3>
<p>You cannot roll back to a previous version of your Worker if the <a href="/workers/runtime-apis/bindings/">Cloudflare Developer Platform resources</a> (such as <a href="/kv/">KV</a> and <a href="/d1/">D1</a>) have been deleted or modified between the version selected to roll back to and the version in the active deployment. Specifically, rollbacks will not be allowed if:</p>
<ul>
<li>A Durable Object class lifecycle change (via <a href="/durable-objects/reference/durable-objects-migrations/"><code>exports</code></a> or the legacy <a href="/durable-objects/reference/durable-object-class-migrations-legacy/"><code>migrations</code></a> array) has occurred between the version in the active deployment and the version selected to roll back to.</li>
<li>If the target deployment has a <a href="/workers/runtime-apis/bindings/">binding</a> to an R2 bucket, KV namespace, or queue that no longer exists.</li>
</ul>
