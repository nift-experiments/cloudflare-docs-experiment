---
cp9:
  canonical: https://developers.cloudflare.com/cache/troubleshooting/mp4-videos-on-ios-and-safari/
  description: Learn how to resolve issues with MP4 videos not playing on iOS and Safari.
  full_title: Issues with MP4 videos on iOS and Safari · Cloudflare Cache (CDN) docs
  head_html: <title>Issues with MP4 videos on iOS and Safari · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to resolve issues with MP4 videos not playing on iOS and Safari."><link rel="canonical" href="https://developers.cloudflare.com/cache/troubleshooting/mp4-videos-on-ios-and-safari/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/troubleshooting/mp4-videos-on-ios-and-safari/index.md"><meta property="og:title" content="Issues with MP4 videos on iOS and Safari · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to resolve issues with MP4 videos not playing on iOS and Safari."><meta property="og:url" content="https://developers.cloudflare.com/cache/troubleshooting/mp4-videos-on-ios-and-safari/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/troubleshooting/mp4-videos-on-ios-and-safari/#page","headline":"Issues with MP4 videos on iOS and Safari \u00b7 Cloudflare Cache (CDN) docs","description":"Learn how to resolve issues with MP4 videos not playing on iOS and Safari.","url":"https://developers.cloudflare.com/cache/troubleshooting/mp4-videos-on-ios-and-safari/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/troubleshooting/mp4-videos-on-ios-and-safari/
  schema: 1
---
<p>When traffic is proxied through Cloudflare, Safari on macOS and iOS devices may fail to load MP4 video files.</p>
<p>This issue occurs because Safari handles HTTP range requests differently than other browsers, particularly in how it processes ETags during video streaming.</p>
<p>Safari and iOS devices rely on HTTP range requests to support video features such as seeking to specific timestamps and resuming interrupted downloads.</p>
<p>When Cloudflare's caching layer processes these range requests with weak ETags, Safari may reject the cached response entirely, resulting in videos that fail to load or display as black screens.</p>
<p>To resolve this issue, configure two cache rules in the following order.</p>
<h2 id="1-create-the-strong-etags-rule"><ol>
<li>Create the strong ETags rule</li>
</ol></h2>
<p>Create a <a href="/cache/how-to/cache-rules/create-dashboard/">cache rule</a> that applies to all MP4 files, marks them as eligible for cache, and turns on the Respect Strong ETags setting.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Cache Rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong> &gt; <strong>Cache rules</strong>.</li>
<li>Enter a descriptive name for the rule in <strong>Rule name</strong>.</li>
<li>In the <strong>When incoming requests match…</strong> section, create a filter that applies to all MP4 files, for example <code>URI Full</code> <code>Wildcard</code> <code>*.mp4</code>.</li>
<li>Select <strong>Eligible for cache</strong> in the <strong>Cache eligibility</strong> section.</li>
<li>Select <strong>+ Add Setting</strong> for <strong>Respect strong ETags</strong> and turn on the toggle.</li>
<li>Select <strong>Last</strong> as <strong>Place at</strong>.</li>
</ol>
<h2 id="2-create-the-bypass-cache-rule"><ol start="2">
<li>Create the bypass cache rule</li>
</ol></h2>
<p>Create another cache rule that applies to all MP4 files and bypasses cache entirely.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Cache Rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong> &gt; <strong>Cache rules</strong>.</li>
<li>Enter a descriptive name for the rule in <strong>Rule name</strong>.</li>
<li>In the <strong>When incoming requests match…</strong> section, create the same filter for MP4 files, for example <code>URI Full</code> <code>Wildcard</code> <code>*.mp4</code>.</li>
<li>Select <strong>Bypass cache</strong> in the <strong>Cache eligibility</strong> section.</li>
<li>Select <strong>Last</strong> as <strong>Place at</strong>.</li>
</ol>
<h2 id="why-this-order-matters">Why this order matters</h2>
<p>The first rule preserves strong ETags for MP4 files, which satisfies Safari's requirements for range request handling. The second rule bypasses cache so that Cloudflare forwards range requests to the origin server instead of serving cached responses with potentially mismatched ETags.</p>
<p>The first rule must appear above the second rule in the Cache Rules list.</p>
