---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/
  description: New updates and improvements at Cloudflare.
  full_title: Tool and prompt aliases for MCP server portals · Changelog
  head_html: <title>Tool and prompt aliases for MCP server portals · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Tool and prompt aliases for MCP server portals · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/#page","headline":"Tool and prompt aliases for MCP server portals \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 28, 2026</time><h2 id="post-title">Tool and prompt aliases for MCP server portals</h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>When you connect third-party MCP servers through <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a>, you have no control over how the server author named tools or wrote descriptions. Unclear names make it harder for AI agents to select the right tool and harder for users to understand what is available.</p>
<p>You can now <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#rename-tools-and-prompts-with-aliases">rename tools and prompts</a> and rewrite their descriptions directly on the portal, without modifying the upstream server. For example, a tool named <code>super_cool_tool</code> can become <code>search_customer_records</code> with a description tailored to your organization.</p>
<p><img src="/assets/upstream/images/changelog/access/portal-edit-tool-modal.png" alt="Edit tool modal showing name and description fields for an MCP server tool" /></p>
<p>Modified tools display a <strong>Modified</strong> label in the tools list so administrators can see which tools have been customized at a glance.</p>
<p><img src="/assets/upstream/images/changelog/access/portal-tools-authorized-modified.png" alt="Tools authorized list showing a modified label on a renamed tool" /></p>
<p>Aliases override the metadata that MCP clients receive. You can set them at two levels:</p>
<ul>
<li><strong>Per portal</strong>: Applies only within a specific portal. Takes precedence over server-level aliases.</li>
<li><strong>Per server</strong>: Applies across all portals that use the server.</li>
</ul>
<p>You can reset an alias at any time to restore the original upstream name.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#rename-tools-and-prompts-with-aliases">Tool and prompt aliases</a>.</p>
</div></article></div>
