---
cp9:
  canonical: https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/
  description: Profile memory usage with DevTools snapshots to optimize Workers and avoid OOM errors.
  full_title: Profiling Memory · Cloudflare Workers docs
  head_html: <title>Profiling Memory · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Profile memory usage with DevTools snapshots to optimize Workers and avoid OOM errors."><link rel="canonical" href="https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/index.md"><meta property="og:title" content="Profiling Memory · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Profile memory usage with DevTools snapshots to optimize Workers and avoid OOM errors."><meta property="og:url" content="https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/#page","headline":"Profiling Memory \u00b7 Cloudflare Workers docs","description":"Profile memory usage with DevTools snapshots to optimize Workers and avoid OOM errors.","url":"https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/observability/dev-tools/memory-usage/
  schema: 1
---
<p>Understanding Worker memory usage can help you optimize performance, avoid Out of Memory (OOM) errors
when hitting <a href="/workers/platform/limits/#memory">Worker memory limits</a>, and fix memory leaks.</p>
<p>You can profile memory usage with snapshots in DevTools. Memory snapshots let you view a summary of
memory usage, see how much memory is allocated to different data types, and get details on specific
objects in memory.</p>
<p>When using DevTools to profile memory, it may be difficult to replicate specific behavior you are
seeing in production. To mimic production behavior, make sure the requests you send to the local Worker
are similar to requests in production. This might mean sending a large volume of requests, making requests
to specific routes, or using production-like data with the <a href="/workers/local-development/#remote-bindings">--remote flag</a>.</p>
<h2 id="taking-a-snapshot">Taking a snapshot</h2>
<p>To generate a memory snapshot:</p>
<ul>
<li>Run <code>wrangler dev</code> to start your Worker</li>
<li>Press the <code>D</code> from your terminal to open DevTools</li>
<li>Select on the &quot;Memory&quot; tab</li>
<li>Send requests to your Worker to start allocating memory
<ul>
<li>Optionally include a debugger to make sure you can pause execution at the proper time</li>
</ul>
</li>
<li>Select <code>Take snapshot</code></li>
</ul>
<p>You can now inspect Worker memory.</p>
<h2 id="an-example-snapshot">An Example Snapshot</h2>
<p>Let's look at an example to learn how to read a memory snapshot. Imagine you have the following Worker:</p>
<pre tabindex="0"><code class="language-js">let responseText = &quot;Hello world!&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		let now = new Date().toISOString();&#10;		responseText = responseText + ` (Requested at: ${now})`;&#10;		return new Response(responseText.slice(0, 53));&#10;	},&#10;};&#10;</code></pre>
<p>While this code worked well initially, over time you notice slower responses and
Out of Memory errors. Using DevTools, you can find out if this is a memory leak.</p>
<p>First, as mentioned above, you open DevTools by pressing the <code>D</code> key after running <code>wrangler dev</code>.
Then, you navigate to the &quot;Memory&quot; tab.</p>
<p>Next, generate a large volume of traffic to the Worker by sending requests. You can do this with <code>curl</code> or by
repeatedly reloading the browser. Note that other Workers may require more specific requests to reproduce
a memory leak.</p>
<p>Then, click the &quot;Take Snapshot&quot; button and view the results.</p>
<p>First, navigate to &quot;Statistics&quot; in the dropdown to get a general sense of what takes up memory.</p>
<p><img src="/assets/upstream/images/workers/observability/memory-stats.png" alt="Memory Statistics" /></p>
<p>Looking at these statistics, you can see that a lot of memory is dedicated to strings at 67 kB. This is
likely the source of the memory leak. If you make more requests and take another snapshot, you would see
this number grow.</p>
<p><img src="/assets/upstream/images/workers/observability/memory-summary.png" alt="Memory Summary" /></p>
<p>The memory summary lists data types by the amount of memory they take up. When you click into &quot;(string)&quot;, you can see
a string that is far larger than the rest. The text shows that you are appending &quot;Requested at&quot; and a date repeatedly,
inadvertently overwriting the global variable with an increasingly large string:</p>
<pre tabindex="0"><code class="language-js">responseText = responseText + ` (Requested at: ${now})`;&#10;</code></pre>
<p>Using Memory Snapshotting in DevTools, you've identified the object and line of code causing the memory leak.
You can now fix it with a small code change.</p>
<h2 id="additional-resources">Additional Resources</h2>
<p>To learn more about how to use Memory Snapshotting, see <a href="https://developer.chrome.com/docs/devtools/memory-problems/heap-snapshots">Google's documentation on Memory Heap Snapshots</a>.</p>
<p>To learn how to use DevTools to gain insight into CPU usage, see the <a href="/workers/observability/dev-tools/cpu-usage/">CPU Profiling Documentation</a>.</p>
