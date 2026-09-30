---
cp9:
  canonical: https://developers.cloudflare.com/workers/platform/deploy-buttons/
  description: Set up a Deploy to Cloudflare button
  full_title: Deploy to Cloudflare buttons · Cloudflare Workers docs
  head_html: <title>Deploy to Cloudflare buttons · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up a Deploy to Cloudflare button"><link rel="canonical" href="https://developers.cloudflare.com/workers/platform/deploy-buttons/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/platform/deploy-buttons/index.md"><meta property="og:title" content="Deploy to Cloudflare buttons · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up a Deploy to Cloudflare button"><meta property="og:url" content="https://developers.cloudflare.com/workers/platform/deploy-buttons/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/platform/deploy-buttons/#page","headline":"Deploy to Cloudflare buttons \u00b7 Cloudflare Workers docs","description":"Set up a Deploy to Cloudflare button","url":"https://developers.cloudflare.com/workers/platform/deploy-buttons/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/platform/deploy-buttons/
  schema: 1
---
<p>If you're building a Workers application and would like to share it with other developers, you can embed a Deploy to Cloudflare button in your README, blog post, or documentation to enable others to quickly deploy your application on their own Cloudflare account. Deploy to Cloudflare buttons eliminate the need for complex setup, allowing developers to get started with your public GitHub or GitLab repository in just a few clicks.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/saas-admin-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<h2 id="what-are-deploy-to-cloudflare-buttons">What are Deploy to Cloudflare buttons?</h2>
<p>Deploy to Cloudflare buttons simplify the deployment of a Workers application by enabling Cloudflare to:</p>
<ul>
<li><strong>Clone a Git repository</strong>: Cloudflare clones your source repository into the user's GitHub/GitLab account where they can continue development after deploying.</li>
<li><strong>Configure a project</strong>: Your users can customize key details such as repository name, Worker name, and required resource names in a single setup page with customizations reflected in the newly created Git repository.</li>
<li><strong>Build &amp; deploy</strong>: Cloudflare builds the application using <a href="/workers/ci-cd/builds">Workers Builds</a> and deploys it to the Cloudflare network. Any required resources are automatically provisioned and bound to the Worker without additional setup.</li>
</ul>
<p><img src="/assets/upstream/images/workers/dtw-user-flow.png" alt="Deploy to Cloudflare Flow" /></p>
<h2 id="how-to-set-up-deploy-to-cloudflare-buttons">How to Set Up Deploy to Cloudflare buttons</h2>
<p>Deploy to Cloudflare buttons can be embedded anywhere developers might want to launch your project. To add a Deploy to Cloudflare button, copy the following snippet and replace the Git repository URL with your project's URL. You can also optionally specify a subdirectory.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="DeployButtonSnippet"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16228.md")
</div></div>
<p>If you have already deployed your application using Workers Builds, you can generate a Deploy to Cloudflare button directly from the Cloudflare dashboard by selecting the share button (located within your Worker details) and copying the provided snippet.</p>
<p><img src="/assets/upstream/images/workers/dtw-share-project.png" alt="Share an application" /></p>
<p>Once you have your snippet, you can paste this wherever you would like your button to be displayed.</p>
<h2 id="automatic-resource-provisioning">Automatic resource provisioning</h2>
<p>If your Worker application requires Cloudflare resources, they will be automatically provisioned as part of the deployment. Currently, supported resources include:</p>
<ul>
<li><strong>Storage</strong>: <a href="/kv/">KV namespaces</a>, <a href="/d1/">D1 databases</a>, <a href="/r2/">R2 buckets</a>, <a href="/hyperdrive/">Hyperdrive</a>, <a href="/vectorize/">Vectorize databases</a>, and <a href="/secrets-store/">Secrets Store Secrets</a></li>
<li><strong>Compute</strong>: <a href="/durable-objects/">Durable Objects</a>, <a href="/workers-ai/">Workers AI</a>, and <a href="/queues/">Queues</a></li>
</ul>
<p>Cloudflare will read the Wrangler configuration file of your source repo to determine resource requirements for your application. During deployment, Cloudflare will provision any necessary resources and update the Wrangler configuration where applicable for newly created resources (e.g. database IDs and namespace IDs). To ensure successful deployment, please make sure your source repository includes default values for resource names, resource IDs and any other properties for each binding.</p>
<h3 id="worker-environment-variables-and-secrets">Worker environment variables and secrets</h3>
<p><a href="/workers/configuration/environment-variables/">Worker environment variables</a> can be defined in your Wrangler configuration file as normal:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16229.md")
</div>
<p><a href="/workers/configuration/secrets/">Worker secrets</a> can be defined in a <code>.dev.vars.example</code> or <code>.env.example</code> file with a <a href="https://www.npmjs.com/package/dotenv">dotenv</a> format:</p>
<pre tabindex="0"><code class="language-ini">COOKIE_SIGNING_KEY=my-secret # comment&#10;</code></pre>
<p><a href="/secrets-store/">Secrets Store</a> secrets can be configured in the Wrangler configuration file as normal:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16230.md")
</div>
<h2 id="best-practices">Best practices</h2>
<p><strong>Configuring Build/Deploy commands</strong>: If you are using custom <code>build</code> and <code>deploy</code> scripts in your <code>package.json</code> (for example, if using a full stack framework or running D1 migrations), Cloudflare will automatically detect and pre-populate the build and deploy fields. Users can choose to modify or accept the custom commands during deployment configuration.</p>
<p>If no <code>deploy</code> script is specified, Cloudflare will preconfigure <code>npx wrangler deploy</code> by default. If no <code>build</code> script is specified, Cloudflare will leave this field blank.</p>
<p><strong>Running D1 Migrations</strong>: If you would like to run migrations as part of your setup, you can specify this in your <code>package.json</code> by running your migrations as part of your <code>deploy</code> script. The migration command should reference the binding name rather than the database name to ensure migrations are successful when users specify a database name that is different from that of your source repository. The following is an example of how you can set up the scripts section of your <code>package.json</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;scripts&quot;: {&#10;		&quot;build&quot;: &quot;astro build&quot;,&#10;		&quot;deploy&quot;: &quot;npm run db:migrations:apply &amp;&amp; wrangler deploy&quot;,&#10;		&quot;db:migrations:apply&quot;: &quot;wrangler d1 migrations apply DB_BINDING --remote&quot;&#10;	}&#10;}&#10;</code></pre>
<p><strong>Provide a description for bindings</strong>: If you wish to provide additional information about bindings, such as why they are required in this template, or suggestions for how to configure a value, you can provide a description in your <code>package.json</code>. This can be particularly useful for environment variables and secrets where users might need to find a value outside of Cloudflare.</p>
<p>Inline markdown <code>`code`</code>, <code>**bold**</code>, <code>__italics__</code> and <code>[links](https://example.com)</code> are supported.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;name&quot;: &quot;my-worker&quot;,&#10;	&quot;private&quot;: true,&#10;	&quot;cloudflare&quot;: {&#10;		&quot;bindings&quot;: {&#10;			&quot;API_KEY&quot;: {&#10;				&quot;description&quot;: &quot;Select your company&#x27;s [API key](https://example.com/) for connecting to the example service.&quot;&#10;			},&#10;			&quot;COOKIE_SIGNING_KEY&quot;: {&#10;				&quot;description&quot;: &quot;Generate a random string using `openssl rand -hex 32`.&quot;&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h2 id="limitations">Limitations</h2>
<ul>
<li><strong>Monorepos</strong>: Cloudflare does not fully support monorepos
<ul>
<li>If your repository URL contains a subdirectory, your application must be fully isolated within that subdirectory, including any dependencies. Otherwise, the build will fail. Cloudflare treats this subdirectory as the root of the new repository created as part of the deploy process.</li>
<li>Additionally, if you have a monorepo that contains multiple Workers applications, they will not be deployed together. You must configure a separate Deploy to Cloudflare button for each application. The user will manually create a distinct Workers application for each subdirectory.</li>
</ul>
</li>
<li><strong>Pages applications</strong>: Deploy to Cloudflare buttons only support Workers applications.</li>
<li><strong>Non-GitHub/GitLab repositories</strong>: Source repositories from anything other than github.com and gitlab.com are not supported. Self-hosted versions of GitHub and GitLab are also not supported.</li>
<li><strong>Private repositories</strong>: Repositories must be public in order for others to successfully use your Deploy to Cloudflare button.</li>
</ul>
