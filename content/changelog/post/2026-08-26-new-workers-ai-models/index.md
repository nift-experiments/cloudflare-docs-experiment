---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/
  description: New updates and improvements at Cloudflare.
  full_title: New Workers AI text generation models in AI Search · Changelog
  head_html: <title>New Workers AI text generation models in AI Search · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New Workers AI text generation models in AI Search · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/#page","headline":"New Workers AI text generation models in AI Search \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-26-new-workers-ai-models/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 26, 2026</time><h2 id="post-title">New Workers AI text generation models in AI Search</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports six additional <a href="/workers-ai/">Workers AI</a> models for text generation:</p>
<table>
<thead>
<tr>
<th>Model</th>
<th>Context window (tokens)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cf/deepseek-ai/deepseek-v4-flash-0731</code></td>
<td>1,048,576</td>
</tr>
<tr>
<td><code>@cf/deepseek-ai/deepseek-v4-pro-0813</code></td>
<td>1,048,576</td>
</tr>
<tr>
<td><code>@cf/openai/gpt-oss-120b</code></td>
<td>128,000</td>
</tr>
<tr>
<td><code>@cf/openai/gpt-oss-20b</code></td>
<td>128,000</td>
</tr>
<tr>
<td><code>@cf/qwen/qwen3.8-27b</code></td>
<td>262,144</td>
</tr>
<tr>
<td><code>@cf/moonshotai/kimi-k2.7-code</code></td>
<td>262,144</td>
</tr>
</tbody>
</table>
<p>These models run on Workers AI, so they do not require an additional provider key. Select a model when creating or updating an AI Search instance in the dashboard or through the API.</p>
<p>For the full list of supported models, refer to <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>
</div></article></div>
