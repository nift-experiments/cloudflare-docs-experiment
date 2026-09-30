---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/
  description: Run Workers on a recurring schedule using the scheduled() handler and Cron Triggers.
  full_title: Scheduled Handler · Cloudflare Workers docs
  head_html: <title>Scheduled Handler · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Run Workers on a recurring schedule using the scheduled() handler and Cron Triggers."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/index.md"><meta property="og:title" content="Scheduled Handler · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run Workers on a recurring schedule using the scheduled() handler and Cron Triggers."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/#page","headline":"Scheduled Handler \u00b7 Cloudflare Workers docs","description":"Run Workers on a recurring schedule using the scheduled() handler and Cron Triggers.","url":"https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/handlers/scheduled/
  schema: 1
---
<h2 id="background">Background</h2>
<p>When a Worker is invoked via a <a href="/workers/configuration/cron-triggers/">Cron Trigger</a>, the <code>scheduled()</code> handler handles the invocation.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="testing-scheduled-handlers-in-local-development">Testing scheduled() handlers in local development</h3>
@markup("md", "content/.markup/bodies/17168.md")
</aside>
<hr />
<h2 id="syntax">Syntax</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17172.md")
</div></div>
<h3 id="properties">Properties</h3>
<ul>
<li><code>controller.cron</code> string
<ul>
<li>The value of the <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> that started the <code>ScheduledEvent</code>.</li>
</ul>
</li>
<li><code>controller.type</code> string
<ul>
<li>The type of controller. This will always return <code>&quot;scheduled&quot;</code>.</li>
</ul>
</li>
<li><code>controller.scheduledTime</code> number
<ul>
<li>The time the <code>ScheduledEvent</code> was scheduled to be executed in milliseconds since January 1, 1970, UTC. It can be parsed as <code>new Date(controller.scheduledTime)</code>.</li>
</ul>
</li>
<li><code>env</code> object
<ul>
<li>An object containing the bindings associated with your Worker using ES modules format, such as KV namespaces and Durable Objects.</li>
</ul>
</li>
<li><code>ctx</code> object
<ul>
<li>An object containing the context associated with your Worker using ES modules format. Currently, this object just contains the <code>waitUntil</code> function.</li>
</ul>
</li>
</ul>
<h3 id="handle-multiple-cron-triggers">Handle multiple cron triggers</h3>
<p>When you configure multiple <a href="/workers/configuration/cron-triggers/">Cron Triggers</a> for a single Worker, each trigger invokes the same <code>scheduled()</code> handler. Use <code>controller.cron</code> to distinguish which schedule fired and run different logic for each.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17173.md")
</div>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17177.md")
</div></div>
<p>The value of <code>controller.cron</code> is the exact cron expression string from your configuration. It must match character-for-character, including spacing.</p>
<h3 id="methods">Methods</h3>
<p>When a Workers script is invoked by a <a href="/workers/configuration/cron-triggers/">Cron Trigger</a>, the Workers runtime starts a <code>ScheduledEvent</code> which will be handled by the <code>scheduled</code> function in your Workers Module class. The <code>ctx</code> argument represents the context your function runs in, and contains the following methods to control what happens next:</p>
<ul>
<li><code>ctx.waitUntil(promise)</code> : void - Use this method to
register asynchronous tasks (for example, logging, analytics to third-party
services, streaming and caching) that should settle before the invocation
completes. The first <code>ctx.waitUntil</code> to fail will be observed and recorded as
the status in the <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> Past
Events table. Otherwise, it will be reported as a success.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17167.md")
</aside>
