---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-27-mcp-portal-logpush/
  description: New updates and improvements at Cloudflare.
  full_title: Export MCP server portal logs with Logpush · Changelog
  head_html: <title>Export MCP server portal logs with Logpush · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-27-mcp-portal-logpush/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Export MCP server portal logs with Logpush · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-27-mcp-portal-logpush/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-27-mcp-portal-logpush/#page","headline":"Export MCP server portal logs with Logpush \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-27-mcp-portal-logpush/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-27-mcp-portal-logpush/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 27, 2026</time><h2 id="post-title">Export MCP server portal logs with Logpush</h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><aside class="nb-aside note">
<h4 class="nb-aside-title" id="availability">Availability</h4>
@markup("md", "content/.markup/bodies/17617.md")</aside>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> now supports <a href="/logs/logpush/">Logpush</a> integration. You can automatically export MCP server portal activity logs to third-party storage destinations or security information and event management (SIEM) tools for analysis and auditing.</p>
<h4 id="available-log-fields">Available log fields</h4>
<p>The MCP server portal logs dataset includes fields such as:</p>
<ul>
<li><code>Datetime</code> — Timestamp of the request</li>
<li><code>PortalID</code> / <code>PortalAUD</code> — Portal identifiers</li>
<li><code>ServerID</code> / <code>ServerURL</code> — Upstream MCP server details</li>
<li><code>Method</code> — JSON-RPC method (for example, <code>tools/call</code>, <code>prompts/get</code>, <code>resources/read</code>)</li>
<li><code>ToolCallName</code> / <code>PromptGetName</code> / <code>ResourceReadURI</code> — Method-specific identifiers</li>
<li><code>UserID</code> / <code>UserEmail</code> — Authenticated user information</li>
<li><code>Success</code> / <code>Error</code> — Request outcome</li>
<li><code>ServerResponseDurationMs</code> — Response time from upstream server</li>
</ul>
<p>For the complete field reference, refer to <a href="/logs/logpush/logpush-job/datasets/account/mcp_portal_logs/">MCP portal logs</a>.</p>
<h4 id="set-up-logpush">Set up Logpush</h4>
<p>To configure Logpush for MCP server portal logs, refer to <a href="/cloudflare-one/insights/logs/logpush/">Logpush integration</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17616.md")</aside>
</div></article></div>
