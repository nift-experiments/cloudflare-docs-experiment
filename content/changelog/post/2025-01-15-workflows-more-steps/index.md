---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-01-15-workflows-more-steps/
  description: New updates and improvements at Cloudflare.
  full_title: Increased Workflows limits and improved instance queueing. · Changelog
  head_html: <title>Increased Workflows limits and improved instance queueing. · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-01-15-workflows-more-steps/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Increased Workflows limits and improved instance queueing. · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-01-15-workflows-more-steps/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-01-15-workflows-more-steps/#page","headline":"Increased Workflows limits and improved instance queueing. \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-01-15-workflows-more-steps/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-01-15-workflows-more-steps/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 15, 2025</time><h2 id="post-title">Increased Workflows limits and improved instance queueing.</h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> (beta) now allows you to define up to 1024 <a href="/workflows/build/workers-api/#workflowstep">steps</a>. <code>sleep</code> steps do not count against this limit.</p>
<p>We've also added:</p>
<ul>
<li><code>instanceId</code> as property to the <a href="/workflows/build/workers-api/#workflowevent"><code>WorkflowEvent</code></a> type, allowing you to retrieve the current instance ID from within a running Workflow instance</li>
<li>Improved queueing logic for Workflow instances beyond the current maximum concurrent instances, reducing the cases where instances are stuck in the queued state.</li>
<li>Support for <a href="/workflows/build/workers-api/#pause"><code>pause</code> and <code>resume</code></a> for Workflow instances in a queued state.</li>
</ul>
<p>We're continuing to work on increases to the number of concurrent Workflow instances, steps, and support for a new <code>waitForEvent</code> API over the coming weeks.</p>
</div></article></div>
