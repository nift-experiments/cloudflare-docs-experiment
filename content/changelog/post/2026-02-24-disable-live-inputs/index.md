---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-24-disable-live-inputs/
  description: New updates and improvements at Cloudflare.
  full_title: Stream live inputs can now be disabled and enabled · Changelog
  head_html: <title>Stream live inputs can now be disabled and enabled · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-24-disable-live-inputs/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Stream live inputs can now be disabled and enabled · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-24-disable-live-inputs/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-24-disable-live-inputs/#page","headline":"Stream live inputs can now be disabled and enabled \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-24-disable-live-inputs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-24-disable-live-inputs/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 24, 2026</time><h2 id="post-title">Stream live inputs can now be disabled and enabled</h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>You can now disable a live input to reject incoming RTMPS and SRT
connections. When a live input is disabled, any broadcast attempts will fail to
connect.</p>
<p>This gives you more control over your live inputs:</p>
<ul>
<li>Temporarily pause an input without deleting it</li>
<li>Programmatically end creator broadcasts</li>
<li>Prevent new broadcasts from starting on a specific input</li>
</ul>
<p>To disable a live input via the API, set the <code>enabled</code> property to <code>false</code>:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{input_id} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-data &#x27;{&quot;enabled&quot;: false}&#x27;&#10;</code></pre>
<p>You can also disable or enable a live input from the <strong>Live inputs</strong> list page
or the live input detail page in the Dashboard.</p>
<p>All existing live inputs remain enabled by default. For more information, refer
to <a href="/stream/stream-live/start-stream-live/">Start a live stream</a>.</p>
</div></article></div>
