---
cp9:
  canonical: https://developers.cloudflare.com/workers/get-started/guide/
  description: Set up and deploy your first Cloudflare Worker using Wrangler, the command-line interface.
  full_title: Get started - CLI · Cloudflare Workers docs
  head_html: <title>Get started - CLI · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up and deploy your first Cloudflare Worker using Wrangler, the command-line interface."><link rel="canonical" href="https://developers.cloudflare.com/workers/get-started/guide/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/get-started/guide/index.md"><meta property="og:title" content="Get started - CLI · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up and deploy your first Cloudflare Worker using Wrangler, the command-line interface."><meta property="og:url" content="https://developers.cloudflare.com/workers/get-started/guide/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/get-started/guide/#page","headline":"Get started - CLI \u00b7 Cloudflare Workers docs","description":"Set up and deploy your first Cloudflare Worker using Wrangler, the command-line interface.","url":"https://developers.cloudflare.com/workers/get-started/guide/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/get-started/guide/
  schema: 1
---
<p>Set up and deploy your first Worker with Wrangler, the Cloudflare Developer Platform CLI.</p>
<p>This guide will instruct you through setting up and deploying your first Worker.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/16296.md")
</div></details>
<h2 id="1-create-a-new-worker-project"><ol>
<li>Create a new Worker project</li>
</ol></h2>
<p>Open a terminal window and run C3 to create your Worker project. <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3 (<code>create-cloudflare-cli</code>)</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- my-first-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-first-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare my-first-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-first-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest my-first-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-first-worker" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>JavaScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Now, you have a new project set up. Move into that project folder.</p>
<pre tabindex="0"><code class="language-sh">cd my-first-worker&#10;</code></pre>
<details class="nb-details"><summary>What files did C3 create?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/16297.md")
</div></details>
<details class="nb-details"><summary>What if I already have a project in a git repository?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/16298.md")
</div></details>
<h2 id="2-develop-with-wrangler-cli"><ol start="2">
<li>Develop with Wrangler CLI</li>
</ol></h2>
<p>C3 installs <a href="/workers/wrangler/install-and-update/">Wrangler</a>, the Workers command-line interface, in Workers projects by default. Wrangler lets you to <a href="/workers/wrangler/commands/general/#init">create</a>, <a href="/workers/wrangler/commands/general/#dev">test</a>, and <a href="/workers/wrangler/commands/general/#deploy">deploy</a> your Workers projects.</p>
<p>After you have created your first Worker, run the <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> command in the project directory to start a local server for developing your Worker. This will allow you to preview your Worker locally during development.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>If you have never used Wrangler before, it will open your web browser so you can login to your Cloudflare account.</p>
<p>Go to <a href="http://localhost:8787">http://localhost:8787</a> to view your Worker.</p>
<details class="nb-details"><summary>Browser issues?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/16299.md")
</div></details>
<h2 id="3-write-code"><ol start="3">
<li>Write code</li>
</ol></h2>
<p>With your new project generated and running, you can begin to write and edit your code.</p>
<p>Find the <code>src/index.js</code> file. <code>index.js</code> will be populated with the code below:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		return new Response(&quot;Hello World!&quot;);&#10;	},&#10;};&#10;</code></pre>
<details class="nb-details"><summary>Code explanation</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/16300.md")
</div></details>
<p>Replace the content in your current <code>index.js</code> file with the content below, which changes the text output.</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		return new Response(&quot;Hello Worker!&quot;);&#10;	},&#10;};&#10;</code></pre>
<p>Then, save the file and reload the page. Your Worker's output will have changed to the new text.</p>
<details class="nb-details"><summary>No visible changes?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/16301.md")
</div></details>
<h2 id="4-deploy-your-project"><ol start="4">
<li>Deploy your project</li>
</ol></h2>
<p>Deploy your Worker via Wrangler to a <code>*.workers.dev</code> subdomain or a <a href="/workers/configuration/routing/custom-domains/">Custom Domain</a>.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>If you have not configured any subdomain or domain, Wrangler will prompt you during the publish process to set one up.</p>
<p>Preview your Worker at <code>&lt;YOUR_WORKER&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>.</p>
<details class="nb-details"><summary>Seeing 523 errors?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/16302.md")
</div></details>
<h2 id="next-steps">Next steps</h2>
<p>To do more:</p>
<ul>
<li>Push your project to a GitHub or GitLab repository then <a href="/workers/ci-cd/builds/#get-started">connect to builds</a> to enable automatic builds and deployments.</li>
<li>Visit the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> for simpler editing.</li>
<li>Review our <a href="/workers/examples/">Examples</a> and <a href="/workers/tutorials/">Tutorials</a> for inspiration.</li>
<li>Set up <a href="/workers/runtime-apis/bindings/">bindings</a> to allow your Worker to interact with other resources and unlock new functionality.</li>
<li>Learn how to <a href="/workers/testing/">test and debug</a> your Workers.</li>
<li>Read about <a href="/workers/platform/">Workers limits and pricing</a>.</li>
</ul>
