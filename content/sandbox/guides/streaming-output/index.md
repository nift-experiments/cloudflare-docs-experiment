---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/guides/streaming-output/
  description: Handle real-time output from commands and processes.
  full_title: Stream output · Cloudflare Sandbox SDK docs
  head_html: <title>Stream output · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Handle real-time output from commands and processes."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/guides/streaming-output/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/guides/streaming-output/index.md"><meta property="og:title" content="Stream output · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Handle real-time output from commands and processes."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/guides/streaming-output/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/guides/streaming-output/#page","headline":"Stream output \u00b7 Cloudflare Sandbox SDK docs","description":"Handle real-time output from commands and processes.","url":"https://developers.cloudflare.com/sandbox/guides/streaming-output/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/guides/streaming-output/
  schema: 1
---
<p>This guide shows you how to handle real-time output from commands, processes, and code execution.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13352.md")
</aside>
<h2 id="when-to-use-streaming">When to use streaming</h2>
<p>Use streaming when you need:</p>
<ul>
<li><strong>Real-time feedback</strong> - Show progress as it happens</li>
<li><strong>Long-running operations</strong> - Builds, tests, installations that take time</li>
<li><strong>Interactive applications</strong> - Chat bots, code execution, live demos</li>
<li><strong>Large output</strong> - Process output incrementally instead of all at once</li>
<li><strong>User experience</strong> - Prevent users from waiting with no feedback</li>
</ul>
<p>Use non-streaming (<code>exec()</code>) for:</p>
<ul>
<li><strong>Quick operations</strong> - Commands that complete in seconds</li>
<li><strong>Small output</strong> - When output fits easily in memory</li>
<li><strong>Post-processing</strong> - When you need complete output before processing</li>
</ul>
<h2 id="stream-command-execution">Stream command execution</h2>
<p>Use <code>execStream()</code> to get real-time output:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13353.md")
</div>
<h2 id="stream-to-client">Stream to client</h2>
<p>Return streaming output to users via Server-Sent Events:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13354.md")
</div>
<p>Client-side consumption:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13355.md")
</div>
<h2 id="stream-process-logs">Stream process logs</h2>
<p>Monitor background process output:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13356.md")
</div>
<h2 id="handle-errors">Handle errors</h2>
<p>Check exit codes and handle stream errors:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13357.md")
</div>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Always consume streams</strong> - Don't let streams hang unconsumed</li>
<li><strong>Handle all event types</strong> - Process stdout, stderr, complete, and error events</li>
<li><strong>Check exit codes</strong> - Non-zero exit codes indicate failure</li>
<li><strong>Provide feedback</strong> - Show progress to users for long operations</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/api/commands/">Commands API reference</a> - Complete streaming API</li>
<li><a href="/sandbox/guides/execute-commands/">Execute commands guide</a> - Command execution patterns</li>
<li><a href="/sandbox/guides/background-processes/">Background processes guide</a> - Process log streaming</li>
<li><a href="/sandbox/guides/code-execution/">Code Interpreter guide</a> - Stream code execution output</li>
</ul>
