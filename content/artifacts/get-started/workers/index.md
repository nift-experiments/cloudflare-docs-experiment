---
cp9:
  canonical: https://developers.cloudflare.com/artifacts/get-started/workers/
  description: Create an Artifacts repo from a Worker.
  full_title: Get started - Workers · Cloudflare Artifacts docs
  head_html: <title>Get started - Workers · Cloudflare Artifacts docs</title><meta name="generator" content="Nift"><meta name="description" content="Create an Artifacts repo from a Worker."><link rel="canonical" href="https://developers.cloudflare.com/artifacts/get-started/workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/artifacts/get-started/workers/index.md"><meta property="og:title" content="Get started - Workers · Cloudflare Artifacts docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create an Artifacts repo from a Worker."><meta property="og:url" content="https://developers.cloudflare.com/artifacts/get-started/workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Artifacts"><meta name="algolia_product_filter" content="Artifacts"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Artifacts"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/artifacts/get-started/workers/#page","headline":"Get started - Workers \u00b7 Cloudflare Artifacts docs","description":"Create an Artifacts repo from a Worker.","url":"https://developers.cloudflare.com/artifacts/get-started/workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /artifacts/get-started/workers/
  schema: 1
---
<p>Create an Artifacts repo from a Worker and use a standard Git client to push and pull content.</p>
<p>By the end of this guide, you will create a Worker, bind it to Artifacts, create a repo through the Workers binding, push a commit, and clone the same repo back with a standard Git client.</p>
<p>Start by reading <a href="/artifacts/concepts/namespaces/">Namespaces</a>, then choose the namespace name you will use. This guide uses <code>default</code> in the examples.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3303.md")
</div></details>
<p>You also need:</p>
<ul>
<li>Wrangler installed. If you use local Wrangler commands in this guide, authenticate Wrangler first. For local OAuth authentication or CI setup, refer to <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a> and <a href="/workers/ci-cd/">Running Wrangler in CI/CD</a>.</li>
<li>Access to Artifacts in your Cloudflare account.</li>
<li>A namespace name, for example <code>default</code>.</li>
<li>A local <code>git</code> client.</li>
<li><code>jq</code>, if you want to extract response fields automatically.</li>
</ul>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3304.md")
</div>
<h2 id="2-add-the-artifacts-binding"><ol start="2">
<li>Add the Artifacts binding</li>
</ol></h2>
<p>Open your Wrangler config file and add the Artifacts binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3305.md")
</div>
<p>This exposes Artifacts as <code>env.ARTIFACTS</code> inside your Worker.</p>
<p>If you are using TypeScript, regenerate your local binding types:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler types" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Wrangler adds an <code>Artifacts</code> type to your generated <code>worker-configuration.d.ts</code> file.</p>
<h2 id="3-write-your-worker"><ol start="3">
<li>Write your Worker</li>
</ol></h2>
<p>Replace <code>src/index.ts</code> with the following code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3306.md")
</div>
<p>This Worker creates an Artifacts repo and returns the remote URL and token your Git client needs to push and pull.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="protect-token-issuing-routes">Protect token-issuing routes</h3>
@markup("md", "content/.markup/bodies/3302.md")
</aside>
<p>For the demo, the Worker returns the initial write token. In production, mint short-lived read tokens for clone and pull flows, and mint write tokens only for operations that need push access.</p>
<h2 id="4-invoke-your-worker-to-create-a-repo"><ol start="4">
<li>Invoke your Worker to create a repo</li>
</ol></h2>
<p>Start local development:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler dev" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Then, open a second terminal and send a request to your Worker to create a new Artifacts repo:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3309.md")
</div></div>
<h2 id="5-push-your-first-commit-with-git"><ol start="5">
<li>Push your first commit with git</li>
</ol></h2>
<p>In the previous step, your Worker created an empty Artifacts repo. Now you will create a local Git repo, add a file, and push it to Artifacts — the same way you would push to any Git remote.</p>
<pre tabindex="0"><code class="language-sh">mkdir artifacts-demo&#10;cd artifacts-demo&#10;git init -b main&#10;printf &#x27;# Artifacts demo\n&#x27; &gt; README.md&#10;git add README.md&#10;git commit -m &quot;Initial commit&quot;&#10;git remote add origin &quot;$ARTIFACTS_REMOTE&quot;&#10;git -c http.extraHeader=&quot;Authorization: Bearer $ARTIFACTS_TOKEN&quot; push -u origin main&#10;</code></pre>
<p>The <code>-c http.extraHeader</code> flag passes the token as a request header, which keeps it out of your Git config and shell history.</p>
<p>If you need a self-contained remote URL for a short-lived command, build one from the token secret instead:</p>
<pre tabindex="0"><code class="language-sh">export ARTIFACTS_TOKEN_SECRET=&quot;${ARTIFACTS_TOKEN%%\?expires=*}&quot;&#10;export ARTIFACTS_AUTH_REMOTE=&quot;https://x:${ARTIFACTS_TOKEN_SECRET}@${ARTIFACTS_REMOTE#https://}&quot;&#10;git push &quot;$ARTIFACTS_AUTH_REMOTE&quot; HEAD:main&#10;</code></pre>
<h2 id="6-pull-the-repo-with-a-regular-git-client"><ol start="6">
<li>Pull the repo with a regular Git client</li>
</ol></h2>
<p>Clone the same repo into a second directory:</p>
<pre tabindex="0"><code class="language-sh">cd ..&#10;git -c http.extraHeader=&quot;Authorization: Bearer $ARTIFACTS_TOKEN&quot; clone &quot;$ARTIFACTS_REMOTE&quot; artifacts-clone&#10;git -C artifacts-clone log --oneline -1&#10;</code></pre>
<p>You should see the commit you pushed in the previous step.</p>
<p>You can also clone with a self-contained remote URL for a short-lived command:</p>
<pre tabindex="0"><code class="language-sh">git clone &quot;$ARTIFACTS_AUTH_REMOTE&quot; artifacts-clone&#10;</code></pre>
<h2 id="7-deploy-your-worker"><ol start="7">
<li>Deploy your Worker</li>
</ol></h2>
<p>Switch back to your Worker project directory:</p>
<pre tabindex="0"><code class="language-sh">cd artifacts-worker&#10;</code></pre>
<p>Deploy the Worker so you can create repos without running <code>wrangler dev</code>:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler deploy" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Wrangler prints your <code>workers.dev</code> URL. Use the same <code>curl</code> request against that URL to create additional repos from production.</p>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-workers-binding-reference-artifacts-api-workers-binding"><a href="/artifacts/api/workers-binding/">Workers binding reference</a></h3><p>Review the binding surface, return types, and method-by-method examples.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-best-practices-artifacts-concepts-best-practices"><a href="/artifacts/concepts/best-practices/">Best practices</a></h3><p>Use repo isolation, least-privilege tokens, and namespace separation effectively.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-git-protocol-artifacts-api-git-protocol"><a href="/artifacts/api/git-protocol/">Git protocol</a></h3><p>Use standard git-over-HTTPS remotes with either URL-based auth or `http.extraHeader`.</p></div>
