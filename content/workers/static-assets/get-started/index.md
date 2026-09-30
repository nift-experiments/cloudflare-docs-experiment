---
cp9:
  canonical: https://developers.cloudflare.com/workers/static-assets/get-started/
  description: Run front-end websites — static or dynamic — directly on Cloudflare's global network.
  full_title: Get Started · Cloudflare Workers docs
  head_html: <title>Get Started · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Run front-end websites — static or dynamic — directly on Cloudflare&#x27;s global network."><link rel="canonical" href="https://developers.cloudflare.com/workers/static-assets/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/static-assets/get-started/index.md"><meta property="og:title" content="Get Started · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run front-end websites — static or dynamic — directly on Cloudflare&#x27;s global network."><meta property="og:url" content="https://developers.cloudflare.com/workers/static-assets/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/static-assets/get-started/#page","headline":"Get Started \u00b7 Cloudflare Workers docs","description":"Run front-end websites \u2014 static or dynamic \u2014 directly on Cloudflare's global network.","url":"https://developers.cloudflare.com/workers/static-assets/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/static-assets/get-started/
  schema: 1
---
<p>For most front-end applications, you'll want to use a framework. Workers supports number of popular <a href="/workers/framework-guides/">frameworks</a> that come with ready-to-use components, a pre-defined and structured architecture, and community support. View <a href="/workers/framework-guides/">framework specific guides</a> to get started using a framework.</p>
<p>Alternatively, you may prefer to build your website from scratch if:</p>
<ul>
<li>You're interested in learning by implementing core functionalities on your own.</li>
<li>You're working on a simple project where you might not need a framework.</li>
<li>You want to optimize for performance by minimizing external dependencies.</li>
<li>You require complete control over every aspect of the application.</li>
<li>You want to build your own framework.</li>
</ul>
<p>This guide will instruct you through setting up and deploying a static site or a full-stack application without a framework on Workers.</p>
<h2 id="deploy-a-static-site">Deploy a static site</h2>
<p>This guide will instruct you through setting up and deploying a static site on Workers.</p>
<h3 id="1-create-a-new-worker-project-using-the-cli"><ol>
<li>Create a new Worker project using the CLI</li>
</ol></h3>
<p><a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3 (<code>create-cloudflare-cli</code>)</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare. Open a terminal window and run C3 to create your Worker project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- my-static-site</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-static-site" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare my-static-site</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-static-site" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest my-static-site</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-static-site" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Static site</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>After setting up your project, change your directory by running the following command:</p>
<pre tabindex="0"><code class="language-sh">cd my-static-site&#10;</code></pre>
<h3 id="2-develop-locally"><ol start="2">
<li>Develop locally</li>
</ol></h3>
<p>After you have created your Worker, run the <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> in the project directory to start a local server. This will allow you to preview your project locally during development.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<h3 id="3-deploy-your-project"><ol start="3">
<li>Deploy your project</li>
</ol></h3>
<p>Your project can be deployed to a <code>*.workers.dev</code> subdomain or a <a href="/workers/configuration/routing/custom-domains/">Custom Domain</a>, from your own machine or from any CI/CD system, including <a href="/workers/ci-cd/builds/">Cloudflare's own</a>.</p>
<p>The <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> will build and deploy your project. If you're using CI, ensure you update your <a href="/workers/ci-cd/builds/configuration/#build-settings">&quot;deploy command&quot;</a> configuration appropriately.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16098.md")
</aside>
<h2 id="deploy-a-full-stack-application">Deploy a full-stack application</h2>
<p>This guide will instruct you through setting up and deploying dynamic and interactive server-side rendered (SSR) applications on Cloudflare Workers.</p>
<p>When building a full-stack application, you can use any <a href="/workers/runtime-apis/bindings/">Workers bindings</a>, <a href="/workers/static-assets/binding/">including assets' own</a>, to interact with resources on the Cloudflare Developer Platform.</p>
<h3 id="1-create-a-new-worker-project"><ol>
<li>Create a new Worker project</li>
</ol></h3>
<p><a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3 (<code>create-cloudflare-cli</code>)</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<p>Open a terminal window and run C3 to create your Worker project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- my-dynamic-site</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-dynamic-site" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare my-dynamic-site</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-dynamic-site" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest my-dynamic-site</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-dynamic-site" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>SSR / full-stack app</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>After setting up your project, change your directory by running the following command:</p>
<pre tabindex="0"><code class="language-sh">cd my-dynamic-site&#10;</code></pre>
<h3 id="2-develop-locally-1"><ol start="2">
<li>Develop locally</li>
</ol></h3>
<p>After you have created your Worker, run the <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> in the project directory to start a local server. This will allow you to preview your project locally during development.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<h3 id="3-modify-your-project"><ol start="3">
<li>Modify your Project</li>
</ol></h3>
<p>With your new project generated and running, you can begin to write and edit your project:</p>
<ul>
<li>The <code>src/index.ts</code> file is populated with sample code. Modify its content to change the server-side behavior of your Worker.</li>
<li>The <code>public/index.html</code> file is populated with sample code. Modify its content, or anything else in <code>public/</code>, to change the static assets of your Worker.</li>
</ul>
<p>Then, save the files and reload the page. Your project's output will have changed based on your modifications.</p>
<h3 id="4-deploy-your-project"><ol start="4">
<li>Deploy your Project</li>
</ol></h3>
<p>Your project can be deployed to a <code>*.workers.dev</code> subdomain or a <a href="/workers/configuration/routing/custom-domains/">Custom Domain</a>, from your own machine or from any CI/CD system, including <a href="/workers/ci-cd/builds/">Cloudflare's own</a>.</p>
<p>The <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> will build and deploy your project. If you're using CI, ensure you update your <a href="/workers/ci-cd/builds/configuration/#build-settings">&quot;deploy command&quot;</a> configuration appropriately.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16097.md")
</aside>
