---
cp9:
  canonical: https://developers.cloudflare.com/stream/transform-videos/sources/
  description: Specify which origins can serve source videos for Cloudflare Media Transformations.
  full_title: Define source origin · Cloudflare Stream docs
  head_html: <title>Define source origin · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Specify which origins can serve source videos for Cloudflare Media Transformations."><link rel="canonical" href="https://developers.cloudflare.com/stream/transform-videos/sources/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/transform-videos/sources/index.md"><meta property="og:title" content="Define source origin · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Specify which origins can serve source videos for Cloudflare Media Transformations."><meta property="og:url" content="https://developers.cloudflare.com/stream/transform-videos/sources/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/transform-videos/sources/#page","headline":"Define source origin \u00b7 Cloudflare Stream docs","description":"Specify which origins can serve source videos for Cloudflare Media Transformations.","url":"https://developers.cloudflare.com/stream/transform-videos/sources/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/transform-videos/sources/
  schema: 1
---
<p>When optimizing remote videos, you can specify which origins can be used as the source for transformed videos. By default, Cloudflare accepts only source videos from the zone where your transformations are served.</p>
<p>On this page, you will learn how to define and manage the origins for the source videos that you want to optimize.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14392.md")
</aside>
<h2 id="configure-origins">Configure origins</h2>
<p>To get started, you must have <a href="/stream/transform-videos/#getting-started">transformations enabled on your zone</a>.</p>
<p>In the Cloudflare dashboard, go to <strong>Stream</strong> &gt; <strong>Transformations</strong> and select the zone where you want to serve transformations.</p>
<p>In <strong>Sources</strong>, you can configure the origins for transformations on your zone.</p>
<p><img src="/assets/upstream/images/images/allowed-origins.png" alt="Enable allowed origins from the Cloudflare dashboard" /></p>
<h2 id="allow-source-videos-only-from-allowed-origins">Allow source videos only from allowed origins</h2>
<p>You can restrict source videos to <strong>allowed origins</strong>, which applies transformations only to source videos from a defined list.</p>
<p>By default, your accepted sources are set to <strong>allowed origins</strong>. Cloudflare will always allow source videos from the same zone where your transformations are served.</p>
<p>If you request a transformation with a source video from outside your <strong>allowed origins</strong>, then the video will be rejected. For example, if you serve transformations on your zone <code>a.com</code> and do not define any additional origins, then <code>a.com/video.mp4</code> can be used as a source video, but <code>b.com/video.mp4</code> will return an error.</p>
<p>To define a new origin:</p>
<ol>
<li>From <strong>Sources</strong>, select <strong>Add origin</strong>.</li>
<li>Under <strong>Domain</strong>, specify the domain for the source video. Only valid web URLs will be accepted.</li>
</ol>
<p><img src="/assets/upstream/images/images/add-origin.png" alt="Add the origin for source videos in the Cloudflare dashboard" /></p>
<p>When you add a root domain, subdomains are not accepted. In other words, if you add <code>b.com</code>, then source videos from <code>media.b.com</code> will be rejected.</p>
<p>To support individual subdomains, define an additional origin such as <code>media.b.com</code>. If you add only <code>media.b.com</code> and not the root domain, then source videos from the root domain (<code>b.com</code>) and other subdomains (<code>cdn.b.com</code>) will be rejected.</p>
<p>To support all subdomains, use the <code>*</code> wildcard at the beginning of the root domain. For example, <code>*.b.com</code> will accept source videos from the root domain (like <code>b.com/video.mp4</code>) as well as from subdomains (like <code>media.b.com/video.mp4</code> or <code>cdn.b.com/video.mp4</code>).</p>
<ol start="3">
<li>Optionally, you can specify the <strong>Path</strong> for the source video. If no path is specified, then source videos from all paths on this domain are accepted.</li>
</ol>
<p>Cloudflare checks whether the defined path is at the beginning of the source path. If the defined path is not present at the beginning of the path, then the source video will be rejected.</p>
<p>For example, if you define an origin with domain <code>b.com</code> and path <code>/themes</code>, then <code>b.com/themes/video.mp4</code> will be accepted but <code>b.com/media/themes/video.mp4</code> will be rejected.</p>
<ol start="4">
<li>Select <strong>Add</strong>. Your origin will now appear in your list of allowed origins.</li>
<li>Select <strong>Save</strong>. These changes will take effect immediately.</li>
</ol>
<p>When you configure <strong>allowed origins</strong>, only the initial URL of the source video is checked. Any redirects, including URLs that leave your zone, will be followed, and the resulting video will be transformed.</p>
<p>If you change your accepted sources to <strong>any origin</strong>, then your list of sources will be cleared and reset to default.</p>
<h2 id="allow-source-videos-from-any-origin">Allow source videos from any origin</h2>
<p>When your accepted sources are set to <strong>any origin</strong>, any publicly available video can be used as the source video for transformations on this zone.</p>
<p><strong>Any origin</strong> is less secure and may allow third parties to serve transformations on your zone.</p>
