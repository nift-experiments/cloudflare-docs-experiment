---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/
  description: New updates and improvements at Cloudflare.
  full_title: Manage AI Search namespaces with Wrangler CLI · Changelog
  head_html: <title>Manage AI Search namespaces with Wrangler CLI · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Manage AI Search namespaces with Wrangler CLI · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/#page","headline":"Manage AI Search namespaces with Wrangler CLI \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 10, 2026</time><h2 id="post-title">Manage AI Search namespaces with Wrangler CLI</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports namespace-level Wrangler commands, making it easier to manage <a href="/ai-search/concepts/namespaces/">namespaces</a> from your terminal, scripts, and agent workflows.</p>
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
<td><code>wrangler ai-search namespace list</code></td>
<td>List AI Search namespaces</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace create</code></td>
<td>Create a new AI Search namespace</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace get</code></td>
<td>Get details for a namespace</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace update</code></td>
<td>Update a namespace description</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace delete</code></td>
<td>Delete an AI Search namespace</td>
</tr>
</tbody>
</table>
<p>Create a namespace for a new application or tenant directly from the CLI:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search namespace create docs-production --description &quot;Production documentation search&quot;&#10;</code></pre>
<p>List namespaces with pagination or filter by name or description:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search namespace list --search docs --page 1 --per-page 10&#10;</code></pre>
<p>Use <code>--json</code> with <code>list</code>, <code>create</code>, <code>get</code>, and <code>update</code> to return structured output that automation and AI agents can parse directly.</p>
<p>Instance-level commands also now support a <code>--namespace</code> flag, so you can interact with instances inside a specific namespace from the CLI:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search list --namespace docs-production&#10;</code></pre>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">AI Search Wrangler commands documentation</a>.</p>
</div></article></div>
