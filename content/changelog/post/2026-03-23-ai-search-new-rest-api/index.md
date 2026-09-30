---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-new-rest-api/
  description: New updates and improvements at Cloudflare.
  full_title: New AI Search REST API endpoints for /search and /chat/completions · Changelog
  head_html: <title>New AI Search REST API endpoints for /search and /chat/completions · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-new-rest-api/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New AI Search REST API endpoints for /search and /chat/completions · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-new-rest-api/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-new-rest-api/#page","headline":"New AI Search REST API endpoints for /search and /chat/completions \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-new-rest-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-23-ai-search-new-rest-api/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 23, 2026</time><h2 id="post-title">New AI Search REST API endpoints for /search and /chat/completions</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now offers new <a href="/ai-search/api/search/rest-api/">REST API</a> endpoints for search and chat that use an OpenAI compatible format. This means you can use the familiar <code>messages</code> array structure that works with existing OpenAI SDKs and tools. The messages array also lets you pass previous messages within a session, so the model can maintain context across multiple turns.</p>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Path</th>
</tr>
</thead>
<tbody>
<tr>
<td>Chat Completions</td>
<td><code>POST /accounts/{account_id}/ai-search/instances/{name}/chat/completions</code></td>
</tr>
<tr>
<td>Search</td>
<td><code>POST /accounts/{account_id}/ai-search/instances/{name}/search</code></td>
</tr>
</tbody>
</table>
<p>Here is an example request to the Chat Completions endpoint using the new <code>messages</code> array format:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances/{NAME}/chat/completions \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer {API_TOKEN}&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;system&quot;,&#10;        &quot;content&quot;: &quot;You are a helpful documentation assistant.&quot;&#10;      },&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;How do I get started?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/api/search/rest-api/">AI Search REST API guide</a>.</p>
<h4 id="migration-from-existing-autorag-api-recommended">Migration from existing AutoRAG API (recommended)</h4>
<p>If you are using the previous AutoRAG API endpoints (<code>/autorag/rags/</code>), we recommend migrating to the new endpoints. The previous AutoRAG API endpoints will continue to be fully supported.</p>
<p>Refer to the <a href="/ai-search/api/migration/rest-api/">migration guide</a> for step-by-step instructions.</p>
</div></article></div>
