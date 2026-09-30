---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/
  description: New updates and improvements at Cloudflare.
  full_title: Additional step context and ReadableStream support now available in Workflows step.do() · Changelog
  head_html: <title>Additional step context and ReadableStream support now available in Workflows step.do() · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Additional step context and ReadableStream support now available in Workflows step.do() · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/#page","headline":"Additional step context and ReadableStream support now available in Workflows step.do() \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-21-step-context-and-readable-streams/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 21, 2026</time><h2 id="post-title">Additional step context and ReadableStream support now available in Workflows step.do()</h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> now provides additional context inside <code>step.do()</code> callbacks and supports returning <code>ReadableStream</code> to handle larger step outputs.</p>
<h4 id="step-context-properties">Step context properties</h4>
<p>The <code>step.do()</code> callback receives a context object with new properties <a href="/changelog/post/2026-03-06-step-context-available/">alongside</a> <code>attempt</code>:</p>
<ul>
<li><strong><code>step.name</code></strong> — The name passed to <code>step.do()</code></li>
<li><strong><code>step.count</code></strong> — How many times a step with that name has been invoked in this instance (1-indexed)
<ul>
<li>Useful when running the same step in a loop.</li>
</ul>
</li>
<li><strong><code>config</code></strong> — The resolved step configuration, including <code>timeout</code> and <code>retries</code> with defaults applied</li>
</ul>
<pre tabindex="0"><code class="language-ts">type ResolvedStepConfig = {&#10;	retries: {&#10;		limit: number;&#10;		delay: WorkflowDelayDuration | number;&#10;		backoff?: &quot;constant&quot; | &quot;linear&quot; | &quot;exponential&quot;;&#10;	};&#10;	timeout: WorkflowTimeoutDuration | number;&#10;};&#10;&#10;type WorkflowStepContext = {&#10;	step: {&#10;		name: string;&#10;		count: number;&#10;	};&#10;	attempt: number;&#10;	config: ResolvedStepConfig;&#10;};&#10;</code></pre>
<h4 id="readablestream-support-in-step-do">ReadableStream support in <code>step.do()</code></h4>
<p>Steps can now return a <code>ReadableStream</code> directly. Although non-stream step outputs are <a href="/workflows/reference/limits/">limited to 1 MiB</a>, streamed outputs support much larger payloads.</p>
<pre tabindex="0"><code class="language-ts">const largePayload = await step.do(&quot;fetch-large-file&quot;, async () =&gt; {&#10;	const object = await env.MY_BUCKET.get(&quot;large-file.bin&quot;);&#10;	return object.body;&#10;});&#10;</code></pre>
<p>Note that streamed outputs are still considered part of the Workflow instance storage limit.</p>
</div></article></div>
