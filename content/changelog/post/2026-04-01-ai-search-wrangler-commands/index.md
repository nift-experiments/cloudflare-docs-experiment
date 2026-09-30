---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-01-ai-search-wrangler-commands/
  description: New updates and improvements at Cloudflare.
  full_title: Create, manage, search AI Search instances with Wrangler CLI · Changelog
  head_html: <title>Create, manage, search AI Search instances with Wrangler CLI · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-01-ai-search-wrangler-commands/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Create, manage, search AI Search instances with Wrangler CLI · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-01-ai-search-wrangler-commands/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-01-ai-search-wrangler-commands/#page","headline":"Create, manage, search AI Search instances with Wrangler CLI \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-01-ai-search-wrangler-commands/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-01-ai-search-wrangler-commands/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 1, 2026</time><h2 id="post-title">Create, manage, search AI Search instances with Wrangler CLI</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> supports a <code>wrangler ai-search</code> command namespace. Use it to manage instances from the command line.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler ai-search create</code></td>
<td>Create a new instance with an interactive wizard</td>
</tr>
<tr>
<td><code>wrangler ai-search list</code></td>
<td>List all instances in your account</td>
</tr>
<tr>
<td><code>wrangler ai-search get</code></td>
<td>Get details of a specific instance</td>
</tr>
<tr>
<td><code>wrangler ai-search update</code></td>
<td>Update the configuration of an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search delete</code></td>
<td>Delete an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search search</code></td>
<td>Run a search query against an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search stats</code></td>
<td>Get usage statistics for an instance</td>
</tr>
</tbody>
</table>
<p>The <code>create</code> command guides you through setup, choosing a name, source type (<code>r2</code> or <code>web</code>), and data source. You can also pass all options as flags for non-interactive use:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search create my-instance --type r2 --source my-bucket&#10;</code></pre>
<p>Use <code>wrangler ai-search search</code> to query an instance directly from the CLI:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search search my-instance --query &quot;how do I configure caching?&quot;&#10;</code></pre>
<p>All commands support <code>--json</code> for structured output that scripts and AI agents can parse directly.</p>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">Wrangler commands documentation</a>.</p>
</div></article></div>
