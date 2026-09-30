---
cp9:
  canonical: https://developers.cloudflare.com/stream/manage-video-library/creator-id/
  description: Set and use creator IDs to associate Cloudflare Stream videos with internal user accounts.
  full_title: Manage creators · Cloudflare Stream docs
  head_html: <title>Manage creators · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Set and use creator IDs to associate Cloudflare Stream videos with internal user accounts."><link rel="canonical" href="https://developers.cloudflare.com/stream/manage-video-library/creator-id/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/manage-video-library/creator-id/index.md"><meta property="og:title" content="Manage creators · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set and use creator IDs to associate Cloudflare Stream videos with internal user accounts."><meta property="og:url" content="https://developers.cloudflare.com/stream/manage-video-library/creator-id/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/manage-video-library/creator-id/#page","headline":"Manage creators \u00b7 Cloudflare Stream docs","description":"Set and use creator IDs to associate Cloudflare Stream videos with internal user accounts.","url":"https://developers.cloudflare.com/stream/manage-video-library/creator-id/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/manage-video-library/creator-id/
  schema: 1
---
<p>You can set the creator field with an internal user ID at the time a tokenized upload URL is requested. When the video is uploaded, the creator property is automatically set to the internal user ID which can be used for analytics data or when searching for videos by a specific creator.</p>
<p>For basic uploads, you will need to add the Creator ID after you upload the video.</p>
<h2 id="upload-from-url">Upload from URL</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14417.md")
</div></div>
<h2 id="set-default-creators-for-videos">Set default creators for videos</h2>
<p>You can associate videos with a single creator by setting a default creator ID value, which you can later use for searching for videos by creator ID or for analytics data.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14422.md")
</div></div>
<p>If you have multiple creators who start live streams, <a href="/stream/get-started/#step-1-create-a-live-input">create a live input</a> for each creator who will live stream and then set a <code>DefaultCreator</code> value per input. Setting the default creator ID for each input ensures that any recorded videos streamed from the creator's input will inherit the <code>DefaultCreator</code> value.</p>
<p>At this time, you can only manage the default creator ID values via the API.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14408.md")
</aside>
<h2 id="update-creator-in-existing-videos">Update creator in existing videos</h2>
<p>To update the creator property in existing videos, make a <code>POST</code> request to the video object endpoint with a JSON payload specifying the creator property as show in the example below.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14431.md")
</div></div>
<h2 id="direct-creator-upload">Direct creator upload</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14440.md")
</div></div>
<h2 id="get-videos-by-creator-id">Get videos by Creator ID</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14445.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14407.md")
</aside>
<h2 id="tus">tus</h2>
<p>Add the Creator ID via the <code>Upload-Creator</code> header. For more information, refer to <a href="/stream/uploading-videos/resumable-uploads/#set-creator-property">Resumable and large files (tus)</a>.</p>
<h2 id="query-by-creator-id-with-graphql">Query by Creator ID with GraphQL</h2>
<p>After you set the creator property, you can use the <a href="/analytics/graphql-api/">GraphQL API</a> to filter by a specific creator. Refer to <a href="/stream/getting-analytics/fetching-bulk-analytics">Fetching bulk analytics</a> for more information about available metrics and filters.</p>
