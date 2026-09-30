---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/
  description: New updates and improvements at Cloudflare.
  full_title: New GraphQL Analytics API Explorer and MCP Server · Changelog
  head_html: <title>New GraphQL Analytics API Explorer and MCP Server · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New GraphQL Analytics API Explorer and MCP Server · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/#page","headline":"New GraphQL Analytics API Explorer and MCP Server \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-05-23-graphql-api-explorer/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 23, 2025</time><h2 id="post-title">New GraphQL Analytics API Explorer and MCP Server</h2>
<div class="changelog-badges"><span>analytics</span></div><div class="changelog-body"><p>We’ve launched two powerful new tools to make the GraphQL Analytics API more accessible:</p>
<h4 id="graphql-api-explorer">GraphQL API Explorer</h4>
<p>The new <a href="https://graphql.cloudflare.com/explorer">GraphQL API Explorer</a> helps you build, test, and run queries directly in your browser. Features include:</p>
<ul>
<li>In-browser schema documentation to browse available datasets and fields</li>
<li>Interactive query editor with autocomplete and inline documentation</li>
<li>A &quot;Run in GraphQL API Explorer&quot; button to execute example queries from our docs</li>
<li>Seamless OAuth authentication — no manual setup required</li>
</ul>
<p><img src="/assets/upstream/images/changelog/analytics/graphql-api-explorer.png" alt="GraphQL API Explorer" /></p>
<h4 id="graphql-model-context-protocol-mcp-server">GraphQL Model Context Protocol (MCP) Server</h4>
<p>MCP Servers let you use natural language tools like Claude to generate structured queries against your data. See our <a href="https://blog.cloudflare.com/thirteen-new-mcp-servers-from-cloudflare/">blog post</a> for details on how they work and which servers are available. The new <a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/graphql">GraphQL MCP server</a> helps you discover and generate useful queries for the GraphQL Analytics API. With this server, you can:</p>
<ul>
<li>Explore what data is available to query</li>
<li>Generate and refine queries using natural language, with one-click links to run them in the API Explorer</li>
<li>Build dashboards and visualizations from structured query outputs</li>
</ul>
<p>Example prompts include:</p>
<ul>
<li>“Show me HTTP traffic for the last 7 days for example.com”</li>
<li>“What GraphQL node returns firewall events?”</li>
<li>“Can you generate a link to the Cloudflare GraphQL API Explorer with a pre-populated query and variables?”</li>
</ul>
<p>We’re continuing to expand these tools, and your feedback helps shape what’s next. <a href="/analytics/graphql-api/">Explore the documentation</a> to learn more and get started.</p>
</div></article></div>
