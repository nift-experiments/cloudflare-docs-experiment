---
cp9:
  canonical: https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/with-durable-objects/
  description: How gradual deployments work with Durable Objects, including version assignment, migrations, and guarantees.
  full_title: With Durable Objects · Cloudflare Workers docs
  head_html: <title>With Durable Objects · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="How gradual deployments work with Durable Objects, including version assignment, migrations, and guarantees."><link rel="canonical" href="https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/with-durable-objects/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/with-durable-objects/index.md"><meta property="og:title" content="With Durable Objects · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How gradual deployments work with Durable Objects, including version assignment, migrations, and guarantees."><meta property="og:url" content="https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/with-durable-objects/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/with-durable-objects/#page","headline":"With Durable Objects \u00b7 Cloudflare Workers docs","description":"How gradual deployments work with Durable Objects, including version assignment, migrations, and guarantees.","url":"https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/with-durable-objects/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/versions-and-deployments/gradual-deployments/with-durable-objects/
  schema: 1
---
<p>To provide <a href="/durable-objects/platform/known-issues/#global-uniqueness">global uniqueness</a>, only one version of each <a href="/durable-objects/">Durable Object</a> can run at a time. This means that gradual deployments work slightly differently for Durable Objects.</p>
<p>When you create a new gradual deployment for a Worker with Durable Objects, each Durable Object is assigned a Worker version based on the percentages you configured in your <a href="/workers/versions-and-deployments/#deployments">deployment</a>. This version will not change until you create a new deployment.</p>
<p><img src="/assets/upstream/images/workers/platform/versions-and-deployments/durable-objects.png" alt="Gradual Deployments Durable Objects" /></p>
<h2 id="example">Example</h2>
<p>This example assumes that you have previously created three Durable Object instances with names &quot;foo&quot;, &quot;bar&quot;, and &quot;baz&quot;.</p>
<p>Your Worker is currently on a version that we will call version &quot;A&quot; and you want to gradually deploy a new version &quot;B&quot; of your Worker.</p>
<p>Here is how the versions of your Durable Objects might change as you progress your gradual deployment:</p>
<table>
<thead>
<tr>
<th align="center">Deployment config</th>
<th align="center">&quot;foo&quot;</th>
<th align="center">&quot;bar&quot;</th>
<th align="center">&quot;baz&quot;</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">Version A: 100% <br/></td>
<td align="center">A</td>
<td align="center">A</td>
<td align="center">A</td>
</tr>
<tr>
<td align="center">Version B: 20% <br/> Version A: 80%</td>
<td align="center">B</td>
<td align="center">A</td>
<td align="center">A</td>
</tr>
<tr>
<td align="center">Version B: 50% <br/> Version A: 50%</td>
<td align="center">B</td>
<td align="center">B</td>
<td align="center">A</td>
</tr>
<tr>
<td align="center">Version B: 100% <br/></td>
<td align="center">B</td>
<td align="center">B</td>
<td align="center">B</td>
</tr>
</tbody>
</table>
<p>This is only an example, so the versions assigned to your Durable Objects may be different. However, the following is guaranteed:</p>
<ul>
<li>For a given deployment, requests to each Durable Object will always use the same Worker version.</li>
<li>When you specify each version in the same order as the previous deployment and increase the percentage of a version, Durable Objects which were previously assigned that version will not be assigned a different version. In this example, Durable Object &quot;foo&quot; would never revert from version &quot;B&quot; to version &quot;A&quot;.</li>
<li>The Durable Object will only be <a href="/durable-objects/observability/troubleshooting/#durable-object-reset-because-its-code-was-updated">reset</a> when it is assigned a different version, so each Durable Object will only be reset once in this example.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17372.md")
</aside>
<h2 id="durable-object-class-lifecycle-changes">Durable Object class lifecycle changes</h2>
<p>Versions of Worker bundles that change Durable Object class lifecycle cannot be uploaded. This applies to both the declarative <a href="/durable-objects/reference/durable-objects-migrations/"><code>exports</code></a> field and the legacy <a href="/durable-objects/reference/durable-object-class-migrations-legacy/"><code>migrations</code></a> array. This is because Durable Object lifecycle changes are atomic operations. Once a lifecycle change is deployed, rollbacks cannot take place to any version prior to the one that included the change.</p>
<p>Durable Object lifecycle changes can be deployed with the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler deploy" aria-label="Copy to clipboard">Copy</button></div></div>
<p>To limit the blast radius of these deployments, Durable Object lifecycle changes should be deployed independently of other code changes.</p>
<p>To understand why Durable Object lifecycle changes are atomic operations, consider the hypothetical example of gradually deploying a class deletion. If a delete were applied to 50% of Durable Object instances, then Workers requesting those Durable Object instances would fail because they would have been deleted.</p>
<p>To do this without producing errors, a version of the Worker which does not depend on any of the Durable Objects to be deleted would have to have already been rolled out. Then, you can deploy the class deletion without affecting any traffic and there is no reason to do so gradually.</p>
