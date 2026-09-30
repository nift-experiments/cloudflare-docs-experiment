---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/
  description: New updates and improvements at Cloudflare.
  full_title: AI Search UI snippets and MCP support · Changelog
  head_html: <title>AI Search UI snippets and MCP support · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="AI Search UI snippets and MCP support · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/#page","headline":"AI Search UI snippets and MCP support \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 23, 2026</time><h2 id="post-title">AI Search UI snippets and MCP support</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports public endpoints, UI snippets, and MCP, making it easy to add search to your website or connect AI agents.</p>
<p>Public endpoints allow you to expose AI Search capabilities without requiring API authentication. To enable public endpoints:</p>
<ol>
<li>Go to <strong>AI Search</strong> in the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your instance, and turn on **Public Endpoint** in **Settings**.
   For more details, refer to [Public endpoint configuration](/ai-search/configuration/retrieval/public-endpoint/).
<h4 id="ui-snippets">UI snippets</h4>
<p>UI snippets are pre-built search and chat components you can embed in your website. Visit <a href="https://search.ai.cloudflare.com/">search.ai.cloudflare.com</a> to configure and preview components for your AI Search instance.</p>
<p><img src="/assets/upstream/images/ai-search/ui-snippet-search-modal.png" alt="Example of the search-modal-snippet component" /></p>
<p>To add a search modal to your page:</p>
<pre tabindex="0"><code class="language-html">&lt;script&#10;	type=&quot;module&quot;&#10;	src=&quot;https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/assets/v0.0.25/search-snippet.es.js&quot;&#10;&gt;&lt;/script&gt;&#10;&#10;&lt;search-modal-snippet&#10;	api-url=&quot;https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/&quot;&#10;	placeholder=&quot;Search...&quot;&#10;&gt;&#10;&lt;/search-modal-snippet&gt;&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/">UI snippets documentation</a>.</p>
<h4 id="mcp">MCP</h4>
<p>The MCP endpoint allows AI agents to search your content via the Model Context Protocol. Connect your MCP client to:</p>
<pre tabindex="0"><code class="language-txt">https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/mcp&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/api/search/mcp/">MCP documentation</a>.</p>
</div></article></div>
