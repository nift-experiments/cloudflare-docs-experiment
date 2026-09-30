---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-20-contextual-403s/
  description: New updates and improvements at Cloudflare.
  full_title: Enriched 403 responses for the Cloudflare API · Changelog
  head_html: <title>Enriched 403 responses for the Cloudflare API · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-20-contextual-403s/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Enriched 403 responses for the Cloudflare API · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-20-contextual-403s/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-20-contextual-403s/#page","headline":"Enriched 403 responses for the Cloudflare API \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-20-contextual-403s/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-20-contextual-403s/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 21, 2026</time><h2 id="post-title">Enriched 403 responses for the Cloudflare API</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare API <code>403 Forbidden</code> responses now include a <code>documentation_url</code> field that links directly to the API documentation for the endpoint that was denied. This gives developers, administrators, and agents an immediate path to the relevant docs with role information instead of guessing at which role or permission they are missing for that endpoint.</p>
<p><strong>What's New</strong></p>
<p><strong>Enriched 403 error responses</strong>: When a Cloudflare API request is denied, the error response now includes a <code>documentation_url</code> field that points to the documentation for that specific endpoint. Contextual 403 responses are now available across nearly all Cloudflare product APIs.</p>
<p><strong>Faster troubleshooting</strong>: The linked API docs surface the roles required for each endpoint, making it easier to self-serve access issues.</p>
<p><strong>Better support for tools and agents</strong>: Agents can use the \documentation_url` field to immediately fetch the endpoint's documentation from the 403 error response, identify the accepted permissions for the denied action, and use that context to drive third-party approval workflows.`</p>
<p>Example 403 response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: false,&#10;  &quot;errors&quot;: [&#10;    {&#10;      &quot;code&quot;: 10000,&#10;      &quot;message&quot;: &quot;Forbidden&quot;,&#10;      &quot;documentation_url&quot;: &quot;https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/list&quot;&#10;    }&#10;  ],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: null&#10;}&#10;</code></pre>
<p>For more info:</p>
<ul>
<li><a href="/api/">Browse the Cloudflare API documentation</a></li>
<li><a href="/fundamentals/manage-members/roles/">Review Cloudflare roles</a></li>
<li><a href="/fundamentals/api/reference/permissions/">Review API token permissions</a></li>
</ul>
</div></article></div>
