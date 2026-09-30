---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/
  description: New updates and improvements at Cloudflare.
  full_title: Select models now require the Workers Paid plan · Changelog
  head_html: <title>Select models now require the Workers Paid plan · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Select models now require the Workers Paid plan · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/#page","headline":"Select models now require the Workers Paid plan \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-07-28-models-require-workers-paid/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 28, 2026</time><h2 id="post-title">Select models now require the Workers Paid plan</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We are limiting Workers Free plan access to a few resource-intensive models so we can prioritize capacity for the broader Workers AI user base. This helps everyone get a more reliable inference experience, with fewer <code>429</code> and <code>3040</code> (Out of Capacity) errors.</p>
<p>The following models now require the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a>:</p>
<ul>
<li><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a></li>
<li><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a></li>
<li><a href="/workers-ai/models/glm-5.2/"><code>@cf/zai-org/glm-5.2</code></a></li>
</ul>
<p>On the Workers Free plan, requests to these models now return a <code>403</code> HTTP error (<a href="/workers-ai/platform/errors/">internal error <code>5035</code></a>) prompting you to upgrade. The Workers Paid plan starts at $5 per month and still includes the 10,000 free Neurons per day allocation, with usage beyond that billed at each <a href="/workers-ai/platform/pricing/">model's pricing</a>.</p>
<p>Many models remain available on the Workers Free plan, including:</p>
<ul>
<li><a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a></li>
<li><a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a></li>
<li><a href="/workers-ai/models/nemotron-3-120b-a12b/"><code>@cf/nvidia/nemotron-3-120b-a12b</code></a></li>
</ul>
<p>For the full list, refer to the <a href="/workers-ai/models/">Workers AI model catalog</a>.</p>
</div></article></div>
