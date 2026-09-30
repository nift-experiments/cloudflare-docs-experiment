---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-20-kimi-k2-6-workers-ai/
  description: New updates and improvements at Cloudflare.
  full_title: Moonshot AI Kimi K2.6 now available on Workers AI · Changelog
  head_html: <title>Moonshot AI Kimi K2.6 now available on Workers AI · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-20-kimi-k2-6-workers-ai/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Moonshot AI Kimi K2.6 now available on Workers AI · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-20-kimi-k2-6-workers-ai/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-20-kimi-k2-6-workers-ai/#page","headline":"Moonshot AI Kimi K2.6 now available on Workers AI \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-20-kimi-k2-6-workers-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-20-kimi-k2-6-workers-ai/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 20, 2026</time><h2 id="post-title">Moonshot AI Kimi K2.6 now available on Workers AI</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> is now available on Workers AI, in partnership with Moonshot AI for Day 0 support. Kimi K2.6 is a native multimodal agentic model from Moonshot AI that advances practical capabilities in long-horizon coding, coding-driven design, proactive autonomous execution, and swarm-based task orchestration.</p>
<p>Built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token, Kimi K2.6 delivers frontier-scale intelligence with efficient inference. It scores competitively against GPT-5.4 and Claude Opus 4.6 on agentic and coding benchmarks, including BrowseComp (83.2), SWE-Bench Verified (80.2), and Terminal-Bench 2.0 (66.7).</p>
<h4 id="key-capabilities">Key capabilities</h4>
<ul>
<li><strong>262.1k token context window</strong> for retaining full conversation history, tool definitions, and codebases across long-running agent sessions</li>
<li><strong>Long-horizon coding</strong> with significant improvements on complex, end-to-end coding tasks across languages including Rust, Go, and Python</li>
<li><strong>Coding-driven design</strong> that transforms simple prompts and visual inputs into production-ready interfaces and full-stack workflows</li>
<li><strong>Agent swarm orchestration</strong> scaling horizontally to 300 sub-agents executing 4,000 coordinated steps for complex autonomous tasks</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Thinking mode</strong> with configurable reasoning depth</li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
</ul>
<h4 id="differences-from-kimi-k2-5">Differences from Kimi K2.5</h4>
<p>If you are migrating from Kimi K2.5, note the following API changes:</p>
<ul>
<li>K2.6 uses <code>chat_template_kwargs.thinking</code> to control reasoning, replacing <code>chat_template_kwargs.enable_thinking</code></li>
<li>K2.6 returns reasoning content in the <code>reasoning</code> field, replacing <code>reasoning_content</code></li>
</ul>
<h4 id="get-started">Get started</h4>
<p>Use Kimi K2.6 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/ai/run</code>, or the OpenAI-compatible endpoint at <code>/v1/chat/completions</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with any of these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.6/">Kimi K2.6 model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>
</div></article></div>
