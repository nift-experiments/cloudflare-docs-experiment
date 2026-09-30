---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/
  description: New updates and improvements at Cloudflare.
  full_title: Moonshot AI Kimi K2.7 Code now available on Workers AI · Changelog
  head_html: <title>Moonshot AI Kimi K2.7 Code now available on Workers AI · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Moonshot AI Kimi K2.7 Code now available on Workers AI · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/#page","headline":"Moonshot AI Kimi K2.7 Code now available on Workers AI \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 12, 2026</time><h2 id="post-title">Moonshot AI Kimi K2.7 Code now available on Workers AI</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a> is now available on Workers AI. Kimi K2.7 Code is a code-optimized variant of the Kimi K2 family, built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token.</p>
<h4 id="improved-coding-and-agent-performance">Improved coding and agent performance</h4>
<p>K2.7 Code delivers meaningful gains over K2.6 on coding and agentic benchmarks:</p>
<ul>
<li><strong>+21.8%</strong> on Kimi Code Bench v2</li>
<li><strong>+11.0%</strong> on Program Bench</li>
<li><strong>+31.5%</strong> on MLS Bench Lite</li>
</ul>
<h4 id="reasoning-efficiency">Reasoning efficiency</h4>
<p>K2.7 Code uses 30% fewer reasoning tokens compared to K2.6, reducing overthinking and lowering inference cost for reasoning-heavy workloads.</p>
<h4 id="key-capabilities">Key capabilities</h4>
<ul>
<li><strong>262.1k token context window</strong> for retaining full conversation history, tool definitions, and codebases across long-running agent sessions</li>
<li><strong>Long-horizon coding</strong> with improved instruction following and higher end-to-end coding task success rates</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Thinking mode</strong> with configurable reasoning depth via <code>chat_template_kwargs.thinking</code></li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
<li><strong>Structured outputs</strong> with JSON schema support</li>
</ul>
<h4 id="differences-from-kimi-k2-6">Differences from Kimi K2.6</h4>
<p>If you are migrating from Kimi K2.6, note the following:</p>
<ul>
<li>K2.7 Code is optimized for coding tasks with improved benchmark performance and reasoning efficiency</li>
<li>Cached input token pricing is $0.19 per M tokens (vs $0.16 for K2.6)</li>
<li>API usage is identical — no parameter changes required</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>Use Kimi K2.7 Code through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/ai/run</code>, or the OpenAI-compatible endpoint at <code>/v1/chat/completions</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with any of these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.7-code/">Kimi K2.7 Code model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>
</div></article></div>
