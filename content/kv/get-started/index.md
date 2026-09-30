---
cp9:
  canonical: https://developers.cloudflare.com/kv/get-started/
  description: Create a KV namespace, write key-value pairs, and read data from Workers KV using Wrangler or the dashboard.
  full_title: Getting started · Cloudflare Workers KV docs
  head_html: <title>Getting started · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a KV namespace, write key-value pairs, and read data from Workers KV using Wrangler or the dashboard."><link rel="canonical" href="https://developers.cloudflare.com/kv/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/get-started/index.md"><meta property="og:title" content="Getting started · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a KV namespace, write key-value pairs, and read data from Workers KV using Wrangler or the dashboard."><meta property="og:url" content="https://developers.cloudflare.com/kv/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/get-started/#page","headline":"Getting started \u00b7 Cloudflare Workers KV docs","description":"Create a KV namespace, write key-value pairs, and read data from Workers KV using Wrangler or the dashboard.","url":"https://developers.cloudflare.com/kv/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/get-started/
  schema: 1
---
<p class="article-summary">Create a basic key-value store which stores the notification configuration of all users in an application, where each user may have `enabled` or `disabled` notifications.
</p>
<p>Workers KV provides low-latency, high-throughput global storage to your <a href="/workers/">Cloudflare Workers</a> applications. Workers KV is ideal for storing user configuration data, routing data, A/B testing configurations and authentication tokens, and is well suited for read-heavy workloads.</p>
<p>This guide instructs you through:</p>
<ul>
<li>Creating a KV namespace.</li>
<li>Writing key-value pairs to your KV namespace from a Cloudflare Worker.</li>
<li>Reading key-value pairs from a KV namespace.</li>
</ul>
<p>You can perform these tasks through the Wrangler CLI or through the Cloudflare dashboard.</p>
<h2 id="quick-start">Quick start</h2>
<p>If you want to skip the setup steps and get started quickly, click on the button below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/update/kv/kv/kv-get-started"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers. Use this option if you are familiar with Cloudflare Workers, and wish to skip the step-by-step guidance.</p>
<p>You may wish to manually follow the steps if you are new to Cloudflare Workers.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/882.md")
</div></details>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="new-to-workers">New to Workers?</h3>
@markup("md", "content/.markup/bodies/881.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvsDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/888.md")
</div></div>
<h2 id="2-create-a-kv-namespace"><ol start="2">
<li>Create a KV namespace</li>
</ol></h2>
<p>A <a href="/kv/concepts/kv-namespaces/">KV namespace</a> is a key-value database replicated to Cloudflare's global network.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvsDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/893.md")
</div></div>
<h2 id="3-bind-your-worker-to-your-kv-namespace"><ol start="3">
<li>Bind your Worker to your KV namespace</li>
</ol></h2>
<p>You must create a binding to connect your Worker with your KV namespace. <a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to access resources, like KV, on the Cloudflare developer platform.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="bindings">Bindings</h3>
@markup("md", "content/.markup/bodies/878.md")
</aside>
<p>To bind your KV namespace to your Worker:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvsDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/899.md")
</div></div>
<h2 id="4-interact-with-your-kv-namespace"><ol start="4">
<li>Interact with your KV namespace</li>
</ol></h2>
<p>You can interact with your KV namespace via <a href="/workers/wrangler/install-and-update/">Wrangler</a> or directly from your <a href="/workers/">Workers</a> application.</p>
<h3 id="4-1-write-a-value">4.1. Write a value</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvsDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/904.md")
</div></div>
<h3 id="4-2-get-a-value">4.2. Get a value</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvsDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/909.md")
</div></div>
<h2 id="5-access-your-kv-namespace-from-your-worker"><ol start="5">
<li>Access your KV namespace from your Worker</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvsDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/916.md")
</div></div>
<h2 id="6-deploy-your-worker"><ol start="6">
<li>Deploy your Worker</li>
</ol></h2>
<p>Deploy your Worker to Cloudflare's global network.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvsDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/921.md")
</div></div>
<h2 id="summary">Summary</h2>
<p>By finishing this tutorial, you have:</p>
<ol>
<li>Created a KV namespace</li>
<li>Created a Worker that writes and reads from that namespace</li>
<li>Deployed your project globally.</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<p>If you have any feature requests or notice any bugs, share your feedback directly with the Cloudflare team by joining the <a href="https://discord.cloudflare.com">Cloudflare Developers community on Discord</a>.</p>
<ul>
<li>Learn more about the <a href="/kv/api/">KV API</a>.</li>
<li>Understand how to use <a href="/kv/reference/environments/">Environments</a> with Workers KV.</li>
<li>Read the Wrangler <a href="/kv/reference/kv-commands/"><code>kv</code> command documentation</a>.</li>
</ul>
