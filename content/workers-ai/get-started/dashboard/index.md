---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/get-started/dashboard/
  description: Create and deploy a Workers AI application using the Cloudflare dashboard.
  full_title: Get started - Dashboard · Cloudflare Workers AI docs
  head_html: <title>Get started - Dashboard · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and deploy a Workers AI application using the Cloudflare dashboard."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/get-started/dashboard/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/get-started/dashboard/index.md"><meta property="og:title" content="Get started - Dashboard · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and deploy a Workers AI application using the Cloudflare dashboard."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/get-started/dashboard/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/get-started/dashboard/#page","headline":"Get started - Dashboard \u00b7 Cloudflare Workers AI docs","description":"Create and deploy a Workers AI application using the Cloudflare dashboard.","url":"https://developers.cloudflare.com/workers-ai/get-started/dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-ai/get-started/dashboard/
  schema: 1
---
<p>Follow this guide to create a Workers AI application using the Cloudflare dashboard.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a> if you have not already.</p>
<h2 id="setup">Setup</h2>
<p>To create a Workers AI application:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Create application**.
3. Under **Select a template**, select **LLM Chat App**.
4. Select **Deploy**.
5. Name your Worker, then select **Create and deploy**.
5. Preview your Worker at its provided [`workers.dev`](/workers/configuration/routing/workers-dev/) subdomain.
<h2 id="development">Development</h2>
<h3 id="dashboard">Dashboard</h3>
<p>Editing in the dashboard is helpful for simpler use cases.</p>
<p>Once you have created your Worker script, you can edit and deploy your Worker using the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your application.
3. Select **Edit Code**.
<p><img src="/assets/upstream/images/workers/workers-edit-code.png" alt="Edit code directly within the Cloudflare dashboard" /></p>
<h3 id="wrangler-cli">Wrangler CLI</h3>
<p>To develop more advanced applications or <a href="/workers/testing/">implement tests</a>, start working in the Wrangler CLI.</p>
<ol>
<li>Install <a href="https://docs.npmjs.com/getting-started"><code>npm</code></a>.</li>
<li>Install <a href="https://nodejs.org/en/"><code>Node.js</code></a>.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="node-js-version-manager">Node.js version manager</h3>
@markup("md", "content/.markup/bodies/15814.md")
</aside>
<ol start="3">
<li>Run the following command, replacing the value of <code>[&lt;DIRECTORY&gt;]</code> which the location you want to put your Worker Script.</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- [&lt;DIRECTORY&gt;] --type=pre-existing</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- [&lt;DIRECTORY&gt;] --type=pre-existing" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare [&lt;DIRECTORY&gt;] --type=pre-existing</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare [&lt;DIRECTORY&gt;] --type=pre-existing" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest [&lt;DIRECTORY&gt;] --type=pre-existing</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest [&lt;DIRECTORY&gt;] --type=pre-existing" aria-label="Copy to clipboard">Copy</button></div></div>
<p>After you run this command - and work through the prompts - your local changes will not automatically sync with dashboard. So, once you download your script, continue using the CLI.</p>
