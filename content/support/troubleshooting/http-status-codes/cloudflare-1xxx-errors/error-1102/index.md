---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1102/
  description: Troubleshoot Cloudflare 1102 error code.
  full_title: Error 1102 · Cloudflare Support docs
  head_html: <title>Error 1102 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Cloudflare 1102 error code."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1102/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1102/index.md"><meta property="og:title" content="Error 1102 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Cloudflare 1102 error code."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1102/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1102/#page","headline":"Error 1102 \u00b7 Cloudflare Support docs","description":"Troubleshoot Cloudflare 1102 error code.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1102/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1102/
  schema: 1
---
<h2 id="error-1102-worker-exceeded-resource-limits">Error 1102: Worker exceeded resource limits</h2>
<p>This error indicates that a Cloudflare Worker has exceeded its CPU time limit or memory limit.</p>
<h3 id="exceeded-cpu-time">Exceeded CPU time</h3>
<p>A Cloudflare Worker exceeds a <a href="/workers/platform/limits/#cpu-time">CPU time limit</a>. CPU time is the time spent executing code (for example, loops, parsing JSON, etc). Time spent on network requests (fetching, responding) does not count towards CPU time.</p>
<h4 id="debugging">Debugging</h4>
<p>To identify CPU-intensive code:</p>
<ol>
<li>Use <a href="/workers/observability/dev-tools/cpu-usage/">CPU profiling with DevTools</a> locally to identify expensive operations.</li>
<li>Review <a href="/workers/observability/logs/workers-logs/">Workers Logs</a> - CPU time is surfaced in the invocation log. This can help find if specific routes or requests are consuming high CPU time.</li>
</ol>
<h4 id="resolution">Resolution</h4>
<p>Contact the developer of your Workers code to optimize code for a reduction in CPU usage. Common optimization strategies include:</p>
<ul>
<li>Reducing the number of iterations in loops</li>
<li>Optimizing JSON parsing operations</li>
<li>Caching computed values</li>
<li>Breaking up large operations into smaller chunks</li>
</ul>
<p>You can also <a href="/workers/platform/limits/#cpu-time">increase the CPU time limit</a> on the Workers Paid plan up to 5 minutes for CPU-bound tasks.</p>
<h3 id="exceeded-memory">Exceeded memory</h3>
<p>A Cloudflare Worker exceeds the <a href="/workers/platform/limits/#memory">128 MB memory limit</a>. This is a per-isolate limit, an isolate may be handling multiple requests concurrently.</p>
<h4 id="debugging-1">Debugging</h4>
<p>To identify memory issues:</p>
<ol>
<li>Use <a href="/workers/observability/dev-tools/memory-usage/">memory profiling with DevTools</a> locally to take memory snapshots and identify leaks.</li>
<li>Look for patterns like buffering a body which could be large (request or response), large objects stored in global scope or accumulating data in arrays.</li>
</ol>
<h4 id="resolution-1">Resolution</h4>
<p>To avoid exceeding memory limits:</p>
<ul>
<li>Avoid buffering large objects or responses in memory</li>
<li>Use streaming APIs such as <a href="/workers/runtime-apis/streams/transformstream/"><code>TransformStream</code></a> or <a href="/workers/runtime-apis/nodejs/streams/"><code>node:stream</code></a> to process data without buffering</li>
<li>Avoid storing large objects in global scope</li>
<li>Be cautious with operations that accumulate data (e.g., appending to strings or arrays repeatedly)</li>
</ul>
<h3 id="related-errors">Related errors</h3>
<ul>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1101/">Error 1101</a> - Workers JavaScript runtime exception</li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-503/">Error 503</a> - Service temporarily unavailable (can be caused by Workers CPU or memory limits)</li>
</ul>
