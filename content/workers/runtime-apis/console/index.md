---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/console/
  description: Supported methods of the `console` API in Cloudflare Workers
  full_title: Console · Cloudflare Workers docs
  head_html: <title>Console · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Supported methods of the `console` API in Cloudflare Workers"><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/console/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/console/index.md"><meta property="og:title" content="Console · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Supported methods of the `console` API in Cloudflare Workers"><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/console/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/console/#page","headline":"Console \u00b7 Cloudflare Workers docs","description":"Supported methods of the console API in Cloudflare Workers","url":"https://developers.cloudflare.com/workers/runtime-apis/console/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/console/
  schema: 1
---
<p>The <code>console</code> object provides a set of methods to help you emit logs, warnings, and debug code.</p>
<p>All standard <a href="https://developer.mozilla.org/en-US/docs/Web/API/console">methods of the <code>console</code> API</a> are present on the <code>console</code> object in Workers.</p>
<p>However, some methods are no ops — they can be called, and do not emit an error, but do not do anything. This ensures compatibility with libraries which may use these APIs.</p>
<p>The table below enumerates each method, and the extent to which it is supported in Workers.</p>
<p>All methods noted as &quot;✅ supported&quot; have the following behavior:</p>
<ul>
<li>They will be written to the console in local dev (<code>npx wrangler@latest dev</code>)</li>
<li>They will appear in real-time logs when tailing logs in the dashboard or running <a href="/workers/observability/logs/real-time-logs/#view-logs-using-wrangler-tail"><code>wrangler tail</code></a></li>
<li>They will create entries in the <code>logs</code> field of <a href="/workers/observability/logs/tail-workers/">Tail Worker</a> events and <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events/">Workers Trace Events</a>. You can use <a href="/workers/observability/logs/logpush/">Logpush</a> to send Workers Trace Event Logs to a supported destination.</li>
</ul>
<p>All methods noted as &quot;🟡 partial support&quot; have the following behavior:</p>
<ul>
<li>In both production and local development the method can be safely called, but will do nothing (no op)</li>
<li>In the <a href="https://workers.cloudflare.com/playground">Workers Playground</a>, Quick Editor in the Workers dashboard, and remote preview mode (<code>wrangler dev --remote</code>) calling the method will behave as expected, print to the console, etc.</li>
</ul>
<p>Refer to <a href="/workers/observability/logs/">Logs</a> for more information about debugging and adding logs to Workers.</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/debug_static"><code>console.debug()</code></a></td>
<td>✅ supported</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/error_static"><code>console.error()</code></a></td>
<td>✅ supported</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/info_static"><code>console.info()</code></a></td>
<td>✅ supported</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/log_static"><code>console.log()</code></a></td>
<td>✅ supported</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/warn_static"><code>console.warn()</code></a></td>
<td>✅ supported</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/clear_static"><code>console.clear()</code></a></td>
<td>🟡 partial support</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/count_static"><code>console.count()</code></a></td>
<td>🟡 partial support</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/group_static"><code>console.group()</code></a></td>
<td>🟡 partial support</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/table_static"><code>console.table()</code></a></td>
<td>🟡 partial support</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/trace_static"><code>console.trace()</code></a></td>
<td>🟡 partial support</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/assert_static"><code>console.assert()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/countreset_static"><code>console.countReset()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/dir_static"><code>console.dir()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/dirxml_static"><code>console.dirxml()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/groupcollapsed_static"><code>console.groupCollapsed()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/groupend_static"><code>console.groupEnd</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/profile_static"><code>console.profile()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/profileend_static"><code>console.profileEnd()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/time_static"><code>console.time()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/timeend_static"><code>console.timeEnd()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/timelog_static"><code>console.timeLog()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/timestamp_static"><code>console.timeStamp()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.chrome.com/blog/devtools-modern-web-debugging/#linked-stack-traces"><code>console.createTask()</code></a></td>
<td>🔴 Will throw an exception in production, but works in local dev, Quick Editor, and remote preview</td>
</tr>
</tbody>
</table>
