---
cp9:
  canonical: https://developers.cloudflare.com/workers/observability/logs/real-time-logs/
  description: Debug your Worker application by accessing logs and exceptions through the Cloudflare dashboard or `wrangler tail`.
  full_title: Real-time logs · Cloudflare Workers docs
  head_html: <title>Real-time logs · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Debug your Worker application by accessing logs and exceptions through the Cloudflare dashboard or `wrangler tail`."><link rel="canonical" href="https://developers.cloudflare.com/workers/observability/logs/real-time-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/observability/logs/real-time-logs/index.md"><meta property="og:title" content="Real-time logs · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Debug your Worker application by accessing logs and exceptions through the Cloudflare dashboard or `wrangler tail`."><meta property="og:url" content="https://developers.cloudflare.com/workers/observability/logs/real-time-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/observability/logs/real-time-logs/#page","headline":"Real-time logs \u00b7 Cloudflare Workers docs","description":"Debug your Worker application by accessing logs and exceptions through the Cloudflare dashboard or wrangler tail.","url":"https://developers.cloudflare.com/workers/observability/logs/real-time-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/observability/logs/real-time-logs/
  schema: 1
---
<p>With Real-time logs, access all your log events in near real-time for log events happening globally. Real-time logs is helpful for immediate feedback, such as the status of a new deployment.</p>
<p>Real-time logs captures <a href="/workers/observability/logs/workers-logs/#invocation-logs">invocation logs</a>, <a href="/workers/observability/logs/workers-logs/#custom-logs">custom logs</a>, errors, and uncaught exceptions. For high-traffic applications, real-time logs may enter sampling mode, which means some messages will be dropped and a warning will appear in your logs.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17040.md")
</aside>
<h2 id="view-logs-from-the-dashboard">View logs from the dashboard</h2>
<p>To view real-time logs associated with any deployed Worker using the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your <strong>Worker</strong>.</li>
<li>Select <strong>Logs</strong>.</li>
<li>In the right-hand navigation bar, select <strong>Live</strong>.</li>
</ol>
<h2 id="view-logs-using-wrangler-tail">View logs using <code>wrangler tail</code></h2>
<p>To view real-time logs associated with any deployed Worker using Wrangler:</p>
<ol>
<li>Go to your Worker project directory.</li>
<li>Run <a href="/workers/wrangler/commands/general/#tail"><code>npx wrangler tail</code></a>.</li>
</ol>
<p>This will log any incoming requests to your application available in your local terminal.</p>
<p>The output of each <code>wrangler tail</code> log is a structured JSON object:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;outcome&quot;: &quot;ok&quot;,&#10;	&quot;scriptName&quot;: null,&#10;	&quot;exceptions&quot;: [],&#10;	&quot;logs&quot;: [],&#10;	&quot;eventTimestamp&quot;: 1590680082349,&#10;	&quot;event&quot;: {&#10;		&quot;request&quot;: {&#10;			&quot;url&quot;: &quot;https://www.bytesized.xyz/&quot;,&#10;			&quot;method&quot;: &quot;GET&quot;,&#10;			&quot;headers&quot;: {},&#10;			&quot;cf&quot;: {}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>By piping the output to tools like <a href="https://stedolan.github.io/jq/"><code>jq</code></a>, you can query and manipulate the requests to look for specific information:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler tail | jq .event.request.url&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&quot;https://www.bytesized.xyz/&quot;&#10;&quot;https://www.bytesized.xyz/component---src-pages-index-js-a77e385e3bde5b78dbf6.js&quot;&#10;&quot;https://www.bytesized.xyz/page-data/app-data.json&quot;&#10;</code></pre>
<p>You can customize how <code>wrangler tail</code> works to fit your needs. Refer to <a href="/workers/wrangler/commands/general/#tail">the <code>wrangler tail</code> documentation</a> for available configuration options.</p>
<h2 id="limits">Limits</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17039.md")
</aside>
<ul>
<li>Real-time logs does not store Workers Logs. To store logs, use <a href="/workers/observability/logs/workers-logs">Workers Logs</a>.</li>
<li>If your Worker has a high volume of traffic, the real-time logs might enter sampling mode. This will cause some of your messages to be dropped and a warning to appear in your logs.</li>
<li>Logs from any <a href="/durable-objects/">Durable Objects</a> your Worker is using will show up in the dashboard.</li>
<li>A maximum of 10 clients can view a Worker's logs at one time. This can be a combination of either dashboard sessions or <code>wrangler tail</code> calls.</li>
<li>When using <code>wrangler tail</code> with <a href="/workers/runtime-apis/websockets/">WebSocket event handlers</a>, any <code>console.log</code> statements within those handlers are hidden until the WebSocket client closes the connection. Once the <code>close</code> is received, all messages are flushed, printing everything to the terminal at once.</li>
</ul>
<h2 id="persist-logs">Persist logs</h2>
<p>Logs can be persisted, filtered, and analyzed with <a href="/workers/observability/logs/workers-logs">Workers Logs</a>. To send logs to a third party, use <a href="/workers/observability/logs/logpush/">Workers Logpush</a> or <a href="/workers/observability/logs/tail-workers/">Tail Workers</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/observability/errors/">Errors and exceptions</a> - Review common Workers errors.</li>
<li><a href="/workers/local-development/">Local development</a> - Develop and test your Workers locally.</li>
<li><a href="/workers/observability/logs/workers-logs">Workers Logs</a> - Collect, store, filter and analyze logging data emitted from Cloudflare Workers.</li>
<li><a href="/workers/observability/logs/logpush/">Logpush</a> - Learn how to push Workers Trace Event Logs to supported destinations.</li>
<li><a href="/workers/observability/logs/tail-workers/">Tail Workers</a> - Learn how to attach Tail Workers to transform your logs and send them to HTTP endpoints.</li>
<li><a href="/workers/observability/source-maps">Source maps and stack traces</a> - Learn how to enable source maps and generate stack traces for Workers.</li>
</ul>
