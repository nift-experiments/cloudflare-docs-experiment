---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/miniflare/migrations/from-v2/
  description: Migrate from Miniflare v2 to v3, which uses the workerd runtime for full Workers compatibility.
  full_title: Migrating from Version 2 · Cloudflare Workers docs
  head_html: <title>Migrating from Version 2 · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Migrate from Miniflare v2 to v3, which uses the workerd runtime for full Workers compatibility."><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/miniflare/migrations/from-v2/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/miniflare/migrations/from-v2/index.md"><meta property="og:title" content="Migrating from Version 2 · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Migrate from Miniflare v2 to v3, which uses the workerd runtime for full Workers compatibility."><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/miniflare/migrations/from-v2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/testing/miniflare/migrations/from-v2/#page","headline":"Migrating from Version 2 \u00b7 Cloudflare Workers docs","description":"Migrate from Miniflare v2 to v3, which uses the workerd runtime for full Workers compatibility.","url":"https://developers.cloudflare.com/workers/testing/miniflare/migrations/from-v2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/miniflare/migrations/from-v2/
  schema: 1
---
<p>Miniflare v3 now uses <a href="https://github.com/cloudflare/workerd"><code>workerd</code></a>, the
open-source Cloudflare Workers runtime. This is the same runtime that's deployed
on Cloudflare's network, giving bug-for-bug compatibility and practically
eliminating behavior mismatches. Refer to the
<a href="https://blog.cloudflare.com/miniflare-and-workerd/">Miniflare v3</a> and
<a href="https://blog.cloudflare.com/wrangler3/">Wrangler v3 announcements</a> for more
information.</p>
<h2 id="cli-changes">CLI Changes</h2>
<p>Miniflare v3 no longer includes a standalone CLI. To get the same functionality,
you will need to switch over to
<a href="/workers/wrangler/">Wrangler</a>. Wrangler v3
uses Miniflare v3 by default. To start a local development server, run:</p>
<pre tabindex="0"><code class="language-sh">$ npx wrangler@3 dev&#10;</code></pre>
<p>If there are features from the Miniflare CLI you would like to see in Wrangler,
please open an issue on
<a href="https://github.com/cloudflare/workers-sdk/issues/new/choose">GitHub</a>.</p>
<h2 id="api-changes">API Changes</h2>
<p>We have tried to keep Miniflare v3's API close to Miniflare v2 where possible,
but many options and methods have been removed or changed with the switch to the
open-source <code>workerd</code> runtime. See the <a href="/workers/testing/miniflare/get-started">Getting Started guide for the new API docs</a></p>
<h3 id="updated-options">Updated Options</h3>
<ul>
<li><code>kvNamespaces/r2Buckets/d1Databases</code>
<ul>
<li>In addition to <code>string[]</code>s, these options now accept
<code>Record&lt;string, string&gt;</code>s, mapping binding names to namespace IDs/bucket
names/database IDs. This means multiple Workers can bind to the same
namespace/bucket/database under different names.</li>
</ul>
</li>
<li><code>queueBindings</code>
<ul>
<li>Renamed to <code>queueProducers</code>. This either accepts a <code>Record&lt;string, string&gt;</code>
mapping binding names to queue names, or a <code>string[]</code> of binding names to
queues of the same name.</li>
</ul>
</li>
<li><code>queueConsumers</code>
<ul>
<li>Either accepts a <code>Record&lt;string, QueueConsumerOptions&gt;</code> mapping queue names
to consumer options, or a <code>string[]</code> of queue names to consume with default
options. <code>QueueConsumerOptions</code> has the following type:</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-ts">interface QueueConsumerOptions {&#10;	// /queues/platform/configuration/#consumer&#10;	maxBatchSize?: number; // default: 5&#10;	maxBatchTimeout?: number /* seconds */; // default: 1&#10;	maxRetries?: number; // default: 2&#10;	deadLetterQueue?: string; // default: none&#10;}&#10;</code></pre>
<ul>
<li><code>cfFetch</code>
<ul>
<li>Renamed to <code>cf</code>. Either accepts a <code>boolean</code>, <code>string</code> (as before), or an
object to use a the <code>cf</code> object for incoming requests.</li>
</ul>
</li>
</ul>
<h3 id="removed-options">Removed Options</h3>
<ul>
<li><code>wranglerConfigPath/wranglerConfigEnv</code>
<ul>
<li>Miniflare no longer handles Wrangler's configuration. To programmatically
start up a Worker based on Wrangler configuration, use the
<a href="/workers/wrangler/api/#unstable_dev"><code>unstable_dev()</code></a>
API.</li>
</ul>
</li>
<li><code>packagePath</code>
<ul>
<li>Miniflare no longer loads script paths from <code>package.json</code> files. Use the
<code>scriptPath</code> option to specify your script instead.</li>
</ul>
</li>
<li><code>watch</code>
<ul>
<li>Miniflare's API is primarily intended for testing use cases, where file
watching isn't usually required. This option was here to enable Miniflare's
CLI which has now been removed. If you need to watch files, consider using a
separate file watcher like
<a href="https://nodejs.org/api/fs.html#fswatchfilename-options-listener"><code>fs.watch()</code></a>
or <a href="https://github.com/paulmillr/chokidar"><code>chokidar</code></a>, and calling
<code>setOptions()</code> with your original configuration on change.</li>
</ul>
</li>
<li><code>logUnhandledRejections</code>
<ul>
<li>Unhandled rejections can be handled in Workers with
<a href="https://community.cloudflare.com/t/2021-10-21-workers-runtime-release-notes/318571"><code>addEventListener(&quot;unhandledrejection&quot;)</code></a>.</li>
</ul>
</li>
<li><code>globals</code>
<ul>
<li>Injecting arbitrary globals is not supported by
<a href="https://github.com/cloudflare/workerd"><code>workerd</code></a>. If you're using a
service worker, <code>bindings</code> will be injected as globals, but these must be
JSON-serialisable.</li>
</ul>
</li>
<li><code>https/httpsKey(Path)/httpsCert(Path)/httpsPfx(Path)/httpsPassphrase</code>
<ul>
<li>Miniflare does not support starting HTTPS servers yet. These options may be
added back in a future release.</li>
</ul>
</li>
<li><code>crons</code>
<ul>
<li><a href="https://github.com/cloudflare/workerd"><code>workerd</code></a> does not support
triggering scheduled events yet. This option may be added back in a future
release.</li>
</ul>
</li>
<li><code>mounts</code>
<ul>
<li>Miniflare no longer has the concept of parent and child Workers. Instead,
all Workers can be defined at the same level, using the new <code>workers</code>
option. Here's an example that uses a service binding to increment a value
in a shared KV namespace:</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-ts">import { Miniflare, Response } from &quot;miniflare&quot;;&#10;&#10;const message = &quot;The count is &quot;;&#10;const mf = new Miniflare({&#10;	// Options shared between Workers such as HTTP and persistence configuration&#10;	// should always be defined at the top level.&#10;	host: &quot;0.0.0.0&quot;,&#10;	port: 8787,&#10;	kvPersist: true,&#10;&#10;	workers: [&#10;		{&#10;			name: &quot;worker&quot;,&#10;			kvNamespaces: { COUNTS: &quot;counts&quot; },&#10;			serviceBindings: {&#10;				INCREMENTER: &quot;incrementer&quot;,&#10;				// Service bindings can also be defined as custom functions, with access&#10;				// to anything defined outside Miniflare.&#10;				async CUSTOM(request) {&#10;					// `request` is the incoming `Request` object.&#10;					return new Response(message);&#10;				},&#10;			},&#10;			modules: true,&#10;			script: `export default {&#10;        async fetch(request, env, ctx) {&#10;          // Get the message defined outside&#10;          const response = await env.CUSTOM.fetch(&quot;http://host/&quot;);&#10;          const message = await response.text();&#10;&#10;          // Increment the count 3 times&#10;          await env.INCREMENTER.fetch(&quot;http://host/&quot;);&#10;          await env.INCREMENTER.fetch(&quot;http://host/&quot;);&#10;          await env.INCREMENTER.fetch(&quot;http://host/&quot;);&#10;          const count = await env.COUNTS.get(&quot;count&quot;);&#10;&#10;          return new Response(message + count);&#10;        }&#10;      }`,&#10;		},&#10;		{&#10;			name: &quot;incrementer&quot;,&#10;			// Note we&#x27;re using the same `COUNTS` namespace as before, but binding it&#10;			// to `NUMBERS` instead.&#10;			kvNamespaces: { NUMBERS: &quot;counts&quot; },&#10;			// Worker formats can be mixed-and-matched&#10;			script: `addEventListener(&quot;fetch&quot;, (event) =&gt; {&#10;        event.respondWith(handleRequest());&#10;      })&#10;      async function handleRequest() {&#10;        const count = parseInt((await NUMBERS.get(&quot;count&quot;)) ?? &quot;0&quot;) + 1;&#10;        await NUMBERS.put(&quot;count&quot;, count.toString());&#10;        return new Response(count.toString());&#10;      }`,&#10;		},&#10;	],&#10;});&#10;const res = await mf.dispatchFetch(&quot;http://localhost&quot;);&#10;console.log(await res.text()); // &quot;The count is 3&quot;&#10;await mf.dispose();&#10;</code></pre>
<ul>
<li><code>metaProvider</code>
<ul>
<li>The <code>cf</code> object and <code>X-Forwarded-Proto</code>/<code>X-Real-IP</code> headers can be specified
when calling <code>dispatchFetch()</code> instead. A default <code>cf</code> object can be
specified using the new <code>cf</code> option too.</li>
</ul>
</li>
<li><code>durableObjectAlarms</code>
<ul>
<li>Miniflare now always enables Durable Object alarms.</li>
</ul>
</li>
<li><code>globalAsyncIO/globalTimers/globalRandom</code>
<ul>
<li><a href="https://github.com/cloudflare/workerd"><code>workerd</code></a> cannot support these
options without fundamental changes.</li>
</ul>
</li>
<li><code>actualTime</code>
<ul>
<li>Miniflare now always returns the current time.</li>
</ul>
</li>
<li><code>inaccurateCpu</code>
<ul>
<li>Set the <code>inspectorPort: 9229</code> option to enable the V8 inspector. Visit
<code>chrome://inspect</code> in Google Chrome to open DevTools and perform CPU
profiling.</li>
</ul>
</li>
</ul>
<h3 id="updated-methods">Updated Methods</h3>
<ul>
<li><code>setOptions()</code>
<ul>
<li>Miniflare v3 now requires a full configuration object to be passed, instead
of a partial patch.</li>
</ul>
</li>
</ul>
<h3 id="removed-methods">Removed Methods</h3>
<ul>
<li><code>reload()</code>
<ul>
<li>Call <code>setOptions()</code> with the original configuration object to reload
Miniflare.</li>
</ul>
</li>
<li><code>createServer()/startServer()</code>
<ul>
<li>Miniflare now always starts a
<a href="https://github.com/cloudflare/workerd"><code>workerd</code></a> server listening on the
configured <code>host</code> and <code>port</code>, so these methods are redundant.</li>
</ul>
</li>
<li><code>dispatchScheduled()/startScheduled()</code>
<ul>
<li>The functionality of <code>dispatchScheduled</code> can now be done via <code>getWorker()</code>. For more information read the <a href="/workers/testing/miniflare/core/scheduled#dispatching-events">scheduled events documentation</a>.</li>
</ul>
</li>
<li><code>dispatchQueue()</code>
<ul>
<li>Use the <code>queue()</code> method on
<a href="/workers/runtime-apis/bindings/service-bindings">service bindings</a>
or
<a href="/queues/configuration/configure-queues/#producer-worker-configuration">queue producer bindings</a>
instead.</li>
</ul>
</li>
<li><code>getGlobalScope()/getBindings()/getModuleExports()</code>
<ul>
<li>These methods returned objects from inside the Workers sandbox. Since
Miniflare now uses <a href="https://github.com/cloudflare/workerd"><code>workerd</code></a>, which
runs in a different process, these methods can no longer be supported.</li>
</ul>
</li>
<li><code>addEventListener()</code>/<code>removeEventListener()</code>
<ul>
<li>Miniflare no longer emits <code>reload</code> events. As Miniflare no longer watches
files, reloads are only triggered by initialisation or <code>setOptions()</code> calls.
In these cases, it's possible to wait for the reload with either
<code>await mf.ready</code> or <code>await mf.setOptions()</code> respectively.</li>
</ul>
</li>
<li><code>Response#waitUntil()</code>
<ul>
<li><a href="https://github.com/cloudflare/workerd"><code>workerd</code></a> does not support waiting
for all <code>waitUntil()</code>ed promises yet.</li>
</ul>
</li>
</ul>
<h3 id="removed-packages">Removed Packages</h3>
<ul>
<li><code>@miniflare/*</code>
<ul>
<li>Miniflare is now contained within a single <code>miniflare</code> package.</li>
</ul>
</li>
</ul>
