---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-04-07-workflows-ga/
  description: New updates and improvements at Cloudflare.
  full_title: Workflows is now Generally Available · Changelog
  head_html: <title>Workflows is now Generally Available · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-04-07-workflows-ga/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Workflows is now Generally Available · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-04-07-workflows-ga/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-07-workflows-ga/#page","headline":"Workflows is now Generally Available \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-04-07-workflows-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-04-07-workflows-ga/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 7, 2025</time><h2 id="post-title">Workflows is now Generally Available</h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> is now <em>Generally Available</em> (or &quot;GA&quot;): in short, it's ready for production workloads. Alongside marking Workflows as GA, we've introduced a number of changes during the beta period, including:</p>
<ul>
<li>A new <code>waitForEvent</code> API that allows a Workflow to wait for an event to occur before continuing execution.</li>
<li>Increased concurrency: you can <a href="/changelog/2025-02-25-workflows-concurrency-increased/">run up to 4,500 Workflow instances</a> concurrently — and this will continue to grow.</li>
<li>Improved observability, including new CPU time metrics that allow you to better understand which Workflow instances are consuming the most resources and/or contributing to your bill.</li>
<li>Support for <code>vitest</code> for testing Workflows locally and in CI/CD pipelines.</li>
</ul>
<p>Workflows also supports the new <a href="/changelog/2025-03-25-higher-cpu-limits/">increased CPU limits</a> that apply to Workers, allowing you to run more CPU-intensive tasks (up to 5 minutes of CPU time per instance), not including the time spent waiting on network calls, AI models, or other I/O bound tasks.</p>
<h4 id="human-in-the-loop">Human-in-the-loop</h4>
<p>The new <code>step.waitForEvent</code> API allows a Workflow instance to wait on events and data, enabling human-in-the-the-loop interactions, such as approving or rejecting a request, directly handling webhooks from other systems, or pushing event data to a Workflow while it's running.</p>
<p>Because Workflows are just code, you can conditionally execute code based on the result of a <code>waitForEvent</code> call, and/or call <code>waitForEvent</code> multiple times in a single Workflow based on what the Workflow needs.</p>
<p>For example, if you wanted to implement a human-in-the-loop approval process, you could use <code>waitForEvent</code> to wait for a user to approve or reject a request, and then conditionally execute code based on the result.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17829.md")</div>
<p>You can then send a Workflow an event from an external service via HTTP or from within a Worker using the <a href="/workflows/build/workers-api/">Workers API</a> for Workflows:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17830.md")</div>
<p>Read the <a href="https://blog.cloudflare.com/workflows-is-now-generally-available/">GA announcement blog</a> to learn more about what landed as part of the Workflows GA.</p>
</div></article></div>
