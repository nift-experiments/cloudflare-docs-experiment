---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-03-25-pause-purge-queues/
  description: New updates and improvements at Cloudflare.
  full_title: New Pause & Purge APIs for Queues · Changelog
  head_html: <title>New Pause &amp; Purge APIs for Queues · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-03-25-pause-purge-queues/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New Pause &amp; Purge APIs for Queues · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-03-25-pause-purge-queues/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-25-pause-purge-queues/#page","headline":"New Pause & Purge APIs for Queues \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-03-25-pause-purge-queues/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-03-25-pause-purge-queues/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 27, 2025</time><h2 id="post-title">New Pause &amp; Purge APIs for Queues</h2>
<div class="changelog-badges"><span>queues</span></div><div class="changelog-body"><p><a href="/queues/">Queues</a> now supports the ability to pause message delivery and/or purge (delete) messages on a queue. These operations can be useful when:</p>
<ul>
<li>Your consumer has a bug or downtime, and you want to temporarily stop messages from being processed while you fix the bug</li>
<li>You have pushed invalid messages to a queue due to a code change during development, and you want to clean up the backlog</li>
<li>Your queue has a backlog that is stale and you want to clean it up to allow new messages to be consumed</li>
</ul>
<p>To pause a queue using <a href="/workers/wrangler/">Wrangler</a>, run the <code>pause-delivery</code> command. Paused queues continue to receive messages. And you can easily unpause a queue using the <code>resume-delivery</code> command.</p>
<pre tabindex="0"><code class="language-bash">$ wrangler queues pause-delivery my-queue&#10;Pausing message delivery for queue my-queue.&#10;Paused message delivery for queue my-queue.&#10;&#10;$ wrangler queues resume-delivery my-queue&#10;Resuming message delivery for queue my-queue.&#10;Resumed message delivery for queue my-queue.&#10;</code></pre>
<p>Purging a queue permanently deletes all messages in the queue. Unlike pausing, purging is an irreversible operation:</p>
<pre tabindex="0"><code class="language-bash">$ wrangler queues purge my-queue&#10;✔ This operation will permanently delete all the messages in queue my-queue. Type my-queue to proceed. … my-queue&#10;Purged queue &#x27;my-queue&#x27;&#10;</code></pre>
<p>You can also do these operations using the <a href="/api/resources/queues/">Queues REST API</a>, or the dashboard page for a queue.</p>
<p><img src="/assets/upstream/images/queues/pause-purge.png" alt="Pause and purge using the dashboard" /></p>
<p>This feature is available on all new and existing queues. Head over to the <a href="/queues/configuration/pause-purge">pause and purge documentation</a> to learn more. And if you haven't used Cloudflare Queues before, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>
</div></article></div>
