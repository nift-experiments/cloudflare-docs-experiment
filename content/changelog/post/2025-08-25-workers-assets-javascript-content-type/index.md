---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/
  description: New updates and improvements at Cloudflare.
  full_title: Content type returned in Workers Assets for Javascript files is now `text/javascript` · Changelog
  head_html: <title>Content type returned in Workers Assets for Javascript files is now `text/javascript` · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Content type returned in Workers Assets for Javascript files is now `text/javascript` · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/#page","headline":"Content type returned in Workers Assets for Javascript files is now `text/javascript` \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-08-25-workers-assets-javascript-content-type/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 25, 2025</time><h2 id="post-title">Content type returned in Workers Assets for Javascript files is now `text/javascript`</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>JavaScript asset responses have been updated to use the <code>text/javascript</code> Content-Type header instead of <code>application/javascript</code>. While both MIME types are widely supported by browsers, the HTML Living Standard explicitly recommends <code>text/javascript</code> as the preferred type going forward.</p>
<p>This change improves:</p>
<ul>
<li>Standards alignment: Ensures consistency with the HTML spec and modern web platform guidance.</li>
<li>Interoperability: Some developer tools, validators, and proxies expect text/javascript and may warn or behave inconsistently with application/javascript.</li>
<li>Future-proofing: By following the spec-preferred MIME type, we reduce the risk of deprecation warnings or unexpected behavior in evolving browser environments.</li>
<li>Consistency: Most frameworks, CDNs, and hosting providers now default to text/javascript, so this change matches common ecosystem practice.</li>
</ul>
<p>Because all major browsers accept both MIME types, this update is backwards compatible and should not cause breakage.</p>
<p>Users will see this change on the next deployment of their assets.</p>
</div></article></div>
