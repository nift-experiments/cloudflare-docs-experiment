---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/
  description: New updates and improvements at Cloudflare.
  full_title: Improve Global Upload Performance with R2 Local Uploads - Now in Open Beta · Changelog
  head_html: <title>Improve Global Upload Performance with R2 Local Uploads - Now in Open Beta · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Improve Global Upload Performance with R2 Local Uploads - Now in Open Beta · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/#page","headline":"Improve Global Upload Performance with R2 Local Uploads - Now in Open Beta \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-03-r2-local-uploads/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 3, 2026</time><h2 id="post-title">Improve Global Upload Performance with R2 Local Uploads - Now in Open Beta</h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p><a href="/r2/buckets/local-uploads/">Local Uploads</a> is now available in open beta. Enable it on your <a href="/r2/">R2</a> bucket to improve upload performance when clients upload data from a different region than your bucket. With Local Uploads enabled, object data is written to storage infrastructure near the client, then asynchronously replicated to your bucket. The object is immediately accessible and remains strongly consistent throughout. Refer to <a href="/r2/how-r2-works/">How R2 works</a> for details on how data is written to your bucket.</p>
<p>In our tests, we observed <strong>up to 75% reduction in Time to Last Byte (TTLB)</strong> for upload requests when Local Uploads is enabled.</p>
<p><img src="/assets/upstream/images/r2/local-uploads-latency.png" alt="Local Uploads latency comparison showing p50 TTLB dropping from around 2 seconds to 500ms after enabling Local Uploads" /></p>
<p>This feature is ideal when:</p>
<ul>
<li>Your users are globally distributed</li>
<li>Upload performance and reliability is critical to your application</li>
<li>You want to optimize write performance without changing your bucket's primary location</li>
</ul>
<p>To enable Local Uploads on your bucket, find <strong>Local Uploads</strong> in your bucket settings in the <a href="https://dash.cloudflare.com/?to=/:account/r2/overview">Cloudflare Dashboard</a>, or run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket local-uploads enable &lt;BUCKET_NAME&gt;&#10;</code></pre>
<p>Enabling Local Uploads on a bucket is seamless: existing uploads will complete as expected and there’s no interruption to traffic. There is no additional cost to enable Local Uploads. Upload requests incur the standard <a href="/r2/pricing/">Class A operation costs</a> same as upload requests made without Local Uploads.</p>
<p>For more information, refer to <a href="/r2/buckets/local-uploads/">Local Uploads</a>.</p>
</div></article></div>
