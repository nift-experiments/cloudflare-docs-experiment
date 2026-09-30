---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-03-bulk-secrets-api/
  description: New updates and improvements at Cloudflare.
  full_title: New Workers bulk secrets API endpoint · Changelog
  head_html: <title>New Workers bulk secrets API endpoint · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-03-bulk-secrets-api/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New Workers bulk secrets API endpoint · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-03-bulk-secrets-api/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-03-bulk-secrets-api/#page","headline":"New Workers bulk secrets API endpoint \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-03-bulk-secrets-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-03-bulk-secrets-api/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 3, 2026</time><h2 id="post-title">New Workers bulk secrets API endpoint</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now create, update, or delete multiple secrets for your Worker in a single request using the <a href="/api/resources/workers/subresources/scripts/subresources/secrets/methods/bulk_update/">bulk secrets endpoint</a>.</p>
<ul>
<li>Include a secret with a value to create or update.</li>
<li>Set a secret to <code>null</code> to delete.</li>
<li>Secrets not included in the request are left unchanged.</li>
</ul>
<p>The following example creates <code>API_KEY</code>, updates the already existing <code>DB_PASSWORD</code>, and deletes <code>OLD_SECRET</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;secrets&quot;: {&#10;    &quot;API_KEY&quot;: { &quot;type&quot;: &quot;secret_text&quot;, &quot;name&quot;: &quot;API_KEY&quot;, &quot;text&quot;: &quot;my-api-key&quot; },&#10;    &quot;DB_PASSWORD&quot;: { &quot;type&quot;: &quot;secret_text&quot;, &quot;name&quot;: &quot;DB_PASSWORD&quot;, &quot;text&quot;: &quot;my-db-password&quot; },&#10;    &quot;OLD_SECRET&quot;: null&#10;  }&#10;}&#10;</code></pre>
<p>You can do the same from the command line using <a href="/workers/wrangler/commands/workers/#secret-bulk"><code>wrangler secret bulk</code></a>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler secret bulk &lt; secrets.json&#10;</code></pre>
<p>To delete a key, set its value to <code>null</code> in the JSON file. Deletion is not supported with <code>.env</code> files.</p>
<p>Each request supports up to <strong>100 total operations</strong> (creates, updates, and deletes combined).</p>
</div></article></div>
