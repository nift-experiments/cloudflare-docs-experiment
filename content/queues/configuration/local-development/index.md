---
cp9:
  canonical: https://developers.cloudflare.com/queues/configuration/local-development/
  description: Develop and test Cloudflare Queues locally using Wrangler.
  full_title: Local Development · Cloudflare Queues docs
  head_html: <title>Local Development · Cloudflare Queues docs</title><meta name="generator" content="Nift"><meta name="description" content="Develop and test Cloudflare Queues locally using Wrangler."><link rel="canonical" href="https://developers.cloudflare.com/queues/configuration/local-development/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/queues/configuration/local-development/index.md"><meta property="og:title" content="Local Development · Cloudflare Queues docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Develop and test Cloudflare Queues locally using Wrangler."><meta property="og:url" content="https://developers.cloudflare.com/queues/configuration/local-development/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Queues"><meta name="algolia_product_filter" content="Queues"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Queues"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/queues/configuration/local-development/#page","headline":"Local Development \u00b7 Cloudflare Queues docs","description":"Develop and test Cloudflare Queues locally using Wrangler.","url":"https://developers.cloudflare.com/queues/configuration/local-development/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /queues/configuration/local-development/
  schema: 1
---
<p>Queues support local development workflows using <a href="/workers/wrangler/install-and-update/">Wrangler</a>, the command-line interface for Workers. Wrangler runs the same version of Queues as Cloudflare runs globally.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To develop locally with Queues, you will need:</p>
<ul>
<li>
<p><a href="https://blog.cloudflare.com/wrangler3/">Wrangler v3.1.0</a> or later.</p>
</li>
<li>
<p>Node.js version of <code>18.0.0</code> or later. Consider using a Node version manager like <a href="https://volta.sh/">Volta</a> or <a href="https://github.com/nvm-sh/nvm">nvm</a> to avoid permission issues and change Node versions.</p>
</li>
<li>
<p>If you are new to Queues and/or Cloudflare Workers, refer to the <a href="/queues/get-started/">Queues tutorial</a> to install <code>wrangler</code> and deploy their first Queue.</p>
</li>
</ul>
<h2 id="start-a-local-development-session">Start a local development session</h2>
<p>Open your terminal and run the following commands to start a local development session:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler@latest dev&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#45;-----------------&#10;Your Worker and resources are simulated locally via Miniflare. For more information, see: https://developers.cloudflare.com/workers/testing/local-development.&#10;&#10;Your worker has access to the following bindings:&#10;&#45; Queues: &lt;QUEUE-NAME&gt;&#10;</code></pre>
<p>Local development sessions create a standalone, local-only environment that mirrors the production environment Queues runs in so you can test your Workers <em>before</em> you deploy to production.</p>
<p>Refer to the <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code> documentation</a> to learn more about how to configure a local development session.</p>
<h2 id="separating-producer-consumer-workers">Separating producer &amp; consumer Workers</h2>
Wrangler supports running multiple Workers simultaneously with a single command. If your architecture separates the producer and consumer into distinct Workers, you can use this functionality to test the entire message flow locally.
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11264.md")
</aside>
<p>For example, if your project has the following directory structure:</p>
<pre tabindex="0"><code>producer-worker/&#10;├── wrangler.jsonc&#10;├── index.ts&#10;└── consumer-worker/&#10;    ├── wrangler.jsonc&#10;    └── index.ts&#10;</code></pre>
<p>You can start development servers for both workers with the following command:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler@latest dev -c wrangler.jsonc -c consumer-worker/wrangler.jsonc --persist-to .wrangler/state&#10;</code></pre>
<p>When the producer Worker sends messages to the queue, the consumer Worker will automatically be invoked to handle them.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11263.md")
</aside>
<h2 id="known-issues">Known Issues</h2>
- Queues does not support Wrangler remote mode (`wrangler dev --remote`).
