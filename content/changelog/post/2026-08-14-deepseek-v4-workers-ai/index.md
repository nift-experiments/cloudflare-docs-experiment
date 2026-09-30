---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/
  description: New updates and improvements at Cloudflare.
  full_title: DeepSeek V4 Flash and Pro now available on Workers AI · Changelog
  head_html: <title>DeepSeek V4 Flash and Pro now available on Workers AI · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="DeepSeek V4 Flash and Pro now available on Workers AI · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/#page","headline":"DeepSeek V4 Flash and Pro now available on Workers AI \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-14-deepseek-v4-workers-ai/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 14, 2026</time><h2 id="post-title">DeepSeek V4 Flash and Pro now available on Workers AI</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p><a href="/workers-ai/models/deepseek-v4-pro-0813/"><code>@cf/deepseek-ai/deepseek-v4-pro-0813</code></a> and <a href="/workers-ai/models/deepseek-v4-flash-0731/"><code>@cf/deepseek-ai/deepseek-v4-flash-0731</code></a> are now available on Workers AI.</p>
<p>DeepSeek V4 Flash and DeepSeek V4 Pro are the first Workers AI models with a full <strong>one million (1,048,576) token context window</strong>. Use them for long-horizon agentic workflows, large codebases, and multi-step reasoning that exceed the context limits of every other model hosted on the platform.</p>
<p>DeepSeek V4 Flash is the faster, lower-cost sibling. This release supersedes the preview version with substantially enhanced agentic capabilities.</p>
<p><strong>Key capabilities:</strong></p>
<ul>
<li><strong>Reasoning</strong>: Both models support thinking mode for complex, step-by-step problem-solving.</li>
<li><strong>Function calling</strong>: Build agents that invoke tools and APIs across multiple conversation turns.</li>
<li><strong>Long context</strong>: Both models support a full 1,048,576 token context window.</li>
</ul>
<p>Both models require the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a> or prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a>.</p>
<p>Use these models through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API, the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/deepseek-v4-pro-0813/">DeepSeek V4 Pro model page</a>, the <a href="/workers-ai/models/deepseek-v4-flash-0731/">DeepSeek V4 Flash model page</a>, and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>
</div></article></div>
