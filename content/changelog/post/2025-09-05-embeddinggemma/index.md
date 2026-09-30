---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-09-05-embeddinggemma/
  description: New updates and improvements at Cloudflare.
  full_title: Introducing EmbeddingGemma from Google on Workers AI · Changelog
  head_html: <title>Introducing EmbeddingGemma from Google on Workers AI · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-09-05-embeddinggemma/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Introducing EmbeddingGemma from Google on Workers AI · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-09-05-embeddinggemma/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-05-embeddinggemma/#page","headline":"Introducing EmbeddingGemma from Google on Workers AI \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-09-05-embeddinggemma/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-09-05-embeddinggemma/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 5, 2025</time><h2 id="post-title">Introducing EmbeddingGemma from Google on Workers AI</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We're excited to be a launch partner alongside <a href="https://developers.googleblog.com/en/introducing-embeddinggemma/">Google</a> to bring their newest embedding model, <strong>EmbeddingGemma</strong>, to Workers AI that delivers best-in-class performance for its size, enabling RAG and semantic search use cases.</p>
<p><a href="/workers-ai/models/embeddinggemma-300m/"><code>@cf/google/embeddinggemma-300m</code></a> is a 300M parameter embedding model from Google, built from Gemma 3 and the same research used to create Gemini models. This multilingual model supports 100+ languages, making it ideal for RAG systems, semantic search, content classification, and clustering tasks.</p>
<p><strong>Using EmbeddingGemma in AI Search:</strong>
Now you can leverage EmbeddingGemma directly through AI Search for your RAG pipelines. EmbeddingGemma's multilingual capabilities make it perfect for global applications that need to understand and retrieve content across different languages with exceptional accuracy.</p>
<p>To use EmbeddingGemma for your AI Search projects:</p>
<ol>
<li>Go to <strong>Create</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/ai/ai-search">AI Search dashboard</a></li>
<li>Follow the setup flow for your new RAG instance</li>
<li>In the <strong>Generate Index</strong> step, open up <strong>More embedding models</strong> and select <code>@cf/google/embeddinggemma-300m</code> as your embedding model</li>
<li>Complete the setup to create an AI Search</li>
</ol>
<p>Try it out and let us know what you think!</p>
</div></article></div>
