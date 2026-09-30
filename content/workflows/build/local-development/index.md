---
cp9:
  canonical: https://developers.cloudflare.com/workflows/build/local-development/
  description: Develop and test Cloudflare Workflows locally using Wrangler's emulated runtime.
  full_title: Local Development · Cloudflare Workflows docs
  head_html: <title>Local Development · Cloudflare Workflows docs</title><meta name="generator" content="Nift"><meta name="description" content="Develop and test Cloudflare Workflows locally using Wrangler&#x27;s emulated runtime."><link rel="canonical" href="https://developers.cloudflare.com/workflows/build/local-development/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workflows/build/local-development/index.md"><meta property="og:title" content="Local Development · Cloudflare Workflows docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Develop and test Cloudflare Workflows locally using Wrangler&#x27;s emulated runtime."><meta property="og:url" content="https://developers.cloudflare.com/workflows/build/local-development/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workflows"><meta name="algolia_product_filter" content="Workflows"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workflows"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workflows/build/local-development/#page","headline":"Local Development \u00b7 Cloudflare Workflows docs","description":"Develop and test Cloudflare Workflows locally using Wrangler's emulated runtime.","url":"https://developers.cloudflare.com/workflows/build/local-development/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workflows/build/local-development/
  schema: 1
---
<p>Workflows support local development using <a href="/workers/wrangler/install-and-update/">Wrangler</a>, the command-line interface for Workers. Wrangler runs an emulated version of Workflows compared to the one that Cloudflare runs globally.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To develop locally with Workflows, you will need:</p>
<ul>
<li><a href="https://blog.cloudflare.com/wrangler3/">Wrangler v3.89.0</a> or later.</li>
<li>Node.js version of <code>18.0.0</code> or later. Consider using a Node version manager like <a href="https://volta.sh/">Volta</a> or <a href="https://github.com/nvm-sh/nvm">nvm</a> to avoid permission issues and change Node versions.</li>
<li>If you are new to Workflows and/or Cloudflare Workers, refer to the <a href="/workflows/get-started/guide/">Workflows Guide</a> to install <code>wrangler</code> and deploy their first Workflows.</li>
</ul>
<h2 id="start-a-local-development-session">Start a local development session</h2>
<p>Open your terminal and run the following commands to start a local development session:</p>
<pre tabindex="0"><code class="language-sh">&#35; Confirm we are using wrangler v3.89.0+&#10;npx wrangler --version&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">⛅️ wrangler 3.89.0&#10;</code></pre>
<p>Start a local dev session</p>
<pre tabindex="0"><code class="language-sh">&#35; Start a local dev session:&#10;npx wrangler dev&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#45;-----------------&#10;Your worker has access to the following bindings:&#10;&#45; Workflows:&#10;  &#45; MY_WORKFLOW: MyWorkflow&#10;⎔ Starting local server...&#10;[wrangler:inf] Ready on http://127.0.0.1:8787/&#10;</code></pre>
<p>Local development sessions create a standalone, local-only environment that mirrors the production environment Workflows runs in so you can test your Workflows <em>before</em> you deploy to production.</p>
<p>Refer to the <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code> documentation</a> to learn more about how to configure a local development session.</p>
<h2 id="manage-workflows-locally">Manage Workflows locally</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17577.md")
</aside>
<p>While a <code>wrangler dev</code> session is running, you can use all <a href="/workers/wrangler/commands/workflows/"><code>wrangler workflows</code> commands</a> with the <code>--local</code> flag to interact with your local Workflow instances.</p>
<p>For example, to list your local Workflows:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler workflows list --local&#10;</code></pre>
<p>To trigger a Workflow locally:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler workflows trigger my-workflow --local&#10;</code></pre>
<p>To inspect a specific instance:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler workflows instances describe my-workflow &lt;INSTANCE_ID&gt; --local&#10;</code></pre>
<p>All commands accept <code>--port</code> to target a specific <code>wrangler dev</code> session (defaults to <code>8787</code>).</p>
<h2 id="local-explorer">Local Explorer</h2>
<p><a href="/workers/local-development/local-explorer/">Local Explorer</a> is a browser-based interface for viewing and managing your local Workflow instances during development. Instead of running CLI commands, you can open Local Explorer in your browser and interact with your Workflows directly.</p>
<p>While a <code>wrangler dev</code> session is running, press <code>e</code> in your terminal to open Local Explorer, or go to <code>http://localhost:8787/cdn-cgi/local/explorer</code> in your browser.</p>
<p>With Local Explorer you can:</p>
<ul>
<li>View all Workflows defined in your project and their instances.</li>
<li>Inspect the step history and current status of each instance.</li>
<li>Trigger new Workflow runs and send events to running instances.</li>
<li>Pause, resume, terminate, and restart instances.</li>
<li>Delete specific instances or clear all of them at once.</li>
</ul>
<p>Local Explorer requires Wrangler version <code>4.82.1</code> or later, or <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> version <code>1.32.0</code> or later.</p>
<h2 id="known-issues">Known Issues</h2>
<p>Workflows are not supported as <a href="/workers/local-development/#remote-bindings">remote bindings</a> or when using <code>npx wrangler dev --remote</code>.</p>
