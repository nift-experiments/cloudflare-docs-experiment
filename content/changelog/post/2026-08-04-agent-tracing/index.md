---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/
  description: New updates and improvements at Cloudflare.
  full_title: Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK · Changelog
  head_html: <title>Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/#page","headline":"Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-04-agent-tracing/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 4, 2026</time><h2 id="post-title">Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>Agent tracing is now available for applications built with the Agents SDK. Traces show each agent turn alongside model calls, tool runs, approvals, token usage, and Workers runtime operations.</p>
<p>Turn on Workers tracing in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17683.md")</div>
<p>Think and Flue applications emit agent traces automatically. For direct AI SDK calls, wrap the AI SDK namespace once. <code>wrapAISDK()</code> supports AI SDK v6 and v7. This AI SDK v7 example also supplies the agent identity:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17684.md")</div>
<p>Message and tool payload recording is off by default. Turn it on only when the payloads are safe to store:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17685.md")</div>
<p>Open the <a href="https://dash.cloudflare.com/?to=/:account/agents"><strong>Agents</strong> tab</a> in the Cloudflare dashboard to inspect sessions, replay conversations, and view trace waterfalls. For advanced setup, privacy controls, and trace structure, refer to <a href="/agents/runtime/operations/observability/tracing/">Agent tracing</a>.</p>
</div></article></div>
