---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/miniflare/core/scheduled/
  description: 'scheduled events are automatically dispatched according to the specified cron triggers:'
  full_title: Scheduled Events · Cloudflare Workers docs
  head_html: <title>Scheduled Events · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="scheduled events are automatically dispatched according to the specified cron triggers:"><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/miniflare/core/scheduled/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/miniflare/core/scheduled/index.md"><meta property="og:title" content="Scheduled Events · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="scheduled events are automatically dispatched according to the specified cron triggers:"><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/miniflare/core/scheduled/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/testing/miniflare/core/scheduled/#page","headline":"Scheduled Events \u00b7 Cloudflare Workers docs","description":"scheduled events are automatically dispatched according to the specified cron triggers:","url":"https://developers.cloudflare.com/workers/testing/miniflare/core/scheduled/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/miniflare/core/scheduled/
  schema: 1
---
<ul>
<li><a href="/workers/runtime-apis/handlers/scheduled/"><code>ScheduledEvent</code> Reference</a></li>
</ul>
<h2 id="cron-triggers">Cron Triggers</h2>
<p><code>scheduled</code> events are automatically dispatched according to the specified cron
triggers:</p>
<pre tabindex="0"><code class="language-js">const mf = new Miniflare({&#10;	crons: [&quot;15 * * * *&quot;, &quot;45 * * * *&quot;],&#10;});&#10;</code></pre>
<h2 id="http-triggers">HTTP Triggers</h2>
<p>Because waiting for cron triggers is annoying, you can also make HTTP requests
to <code>/cdn-cgi/local/scheduled</code> to trigger <code>scheduled</code> events:</p>
<pre tabindex="0"><code class="language-sh">$ curl &quot;http://localhost:8787/cdn-cgi/local/scheduled&quot;&#10;</code></pre>
<p>To simulate different values of <code>scheduledTime</code> and <code>cron</code> in the dispatched
event, use the <code>time</code> and <code>cron</code> query parameters:</p>
<pre tabindex="0"><code class="language-sh">$ curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?time=1000&quot;&#10;$ curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*&quot;&#10;</code></pre>
<h2 id="dispatching-events">Dispatching Events</h2>
<p>When using the API, the <code>getWorker</code> function can be used to dispatch
<code>scheduled</code> events to your Worker. This can be used for testing responses. It
takes optional <code>scheduledTime</code> and <code>cron</code> parameters, which default to the
current time and the empty string respectively. It will return a promise which
resolves to an array containing data returned by all waited promises:</p>
<pre tabindex="0"><code class="language-js">import { Miniflare } from &quot;miniflare&quot;;&#10;&#10;const mf = new Miniflare({&#10;	modules: true,&#10;	script: `&#10;  export default {&#10;    async scheduled(controller, env, ctx) {&#10;      const lastScheduledController = controller;&#10;      if (controller.cron === &quot;* * * * *&quot;) controller.noRetry();&#10;    }&#10;  }&#10;  `,&#10;});&#10;&#10;const worker = await mf.getWorker();&#10;&#10;let scheduledResult = await worker.scheduled({&#10;	cron: &quot;* * * * *&quot;,&#10;});&#10;console.log(scheduledResult); // { outcome: &#x27;ok&#x27;, noRetry: true }&#10;&#10;scheduledResult = await worker.scheduled({&#10;	scheduledTime: new Date(1000),&#10;	cron: &quot;30 * * * *&quot;,&#10;});&#10;&#10;console.log(scheduledResult); // { outcome: &#x27;ok&#x27;, noRetry: false }&#10;</code></pre>
