---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-04-new-markdown-conversion-options/
  description: New updates and improvements at Cloudflare.
  full_title: New conversion options for Markdown Conversion · Changelog
  head_html: <title>New conversion options for Markdown Conversion · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-04-new-markdown-conversion-options/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New conversion options for Markdown Conversion · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-04-new-markdown-conversion-options/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-04-new-markdown-conversion-options/#page","headline":"New conversion options for Markdown Conversion \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-04-new-markdown-conversion-options/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-04-new-markdown-conversion-options/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 4, 2026</time><h2 id="post-title">New conversion options for Markdown Conversion</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>You can now customize how the <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> service processes different file types by passing a <code>conversionOptions</code> object.</p>
<p>Available options:</p>
<ul>
<li><strong>Images</strong>: Set the language for AI-generated image descriptions</li>
<li><strong>HTML</strong>: Use CSS selectors to extract specific content, or provide a hostname to resolve relative links</li>
<li><strong>PDF</strong>: Exclude metadata from the output</li>
</ul>
<p>Use the <a href="/workers-ai/features/markdown-conversion/usage/binding/"><code>env.AI</code></a> binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17817.md")</div>
<p>Or call the REST API:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  &#45;F &#x27;files=@index.html&#x27; \&#10;  &#45;F &#x27;conversionOptions={&quot;html&quot;: {&quot;cssSelector&quot;: &quot;article.content&quot;}}&#x27;&#10;</code></pre>
<p>For more details, refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/">Conversion Options</a>.</p>
</div></article></div>
