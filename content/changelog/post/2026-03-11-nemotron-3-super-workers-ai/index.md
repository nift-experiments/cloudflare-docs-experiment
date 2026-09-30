---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-11-nemotron-3-super-workers-ai/
  description: New updates and improvements at Cloudflare.
  full_title: NVIDIA Nemotron 3 Super now available on Workers AI · Changelog
  head_html: <title>NVIDIA Nemotron 3 Super now available on Workers AI · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-11-nemotron-3-super-workers-ai/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="NVIDIA Nemotron 3 Super now available on Workers AI · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-11-nemotron-3-super-workers-ai/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-11-nemotron-3-super-workers-ai/#page","headline":"NVIDIA Nemotron 3 Super now available on Workers AI \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-11-nemotron-3-super-workers-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-11-nemotron-3-super-workers-ai/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 11, 2026</time><h2 id="post-title">NVIDIA Nemotron 3 Super now available on Workers AI</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We're excited to partner with NVIDIA to bring <a href="/workers-ai/models/nemotron-3-120b-a12b/"><code>@cf/nvidia/nemotron-3-120b-a12b</code></a> to Workers AI. NVIDIA Nemotron 3 Super is a Mixture-of-Experts (MoE) model with a hybrid Mamba-transformer architecture, 120B total parameters, and 12B active parameters per forward pass.</p>
<p>The model is optimized for running many collaborating agents per application. It delivers high accuracy for reasoning, tool calling, and instruction following across complex multi-step tasks.</p>
<p><strong>Key capabilities:</strong></p>
<ul>
<li><strong>Hybrid Mamba-transformer architecture</strong> delivers over 50% higher token generation throughput compared to leading open models, reducing latency for real-world applications</li>
<li><strong>Tool calling</strong> support for building AI agents that invoke tools across multiple conversation turns</li>
<li><strong>Multi-Token Prediction (MTP)</strong> accelerates long-form text generation by predicting several future tokens simultaneously in a single forward pass</li>
<li><strong>32,000 token context window</strong> for retaining conversation history and plan states across multi-step agent workflows</li>
</ul>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="prompt-caching">Prompt caching</h4>
@markup("md", "content/.markup/bodies/17818.md")</aside>
<p>Use Nemotron 3 Super through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, or the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/nemotron-3-120b-a12b/">Nemotron 3 Super model page</a>.</p>
</div></article></div>
