---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/
  description: Add a custom image watermark to RealtimeKit recordings with configurable position and size.
  full_title: Add Watermark · Cloudflare Realtime docs
  head_html: <title>Add Watermark · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Add a custom image watermark to RealtimeKit recordings with configurable position and size."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/index.md"><meta property="og:title" content="Add Watermark · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add a custom image watermark to RealtimeKit recordings with configurable position and size."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/#page","headline":"Add Watermark \u00b7 Cloudflare Realtime docs","description":"Add a custom image watermark to RealtimeKit recordings with configurable position and size.","url":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/recording-guide/add-watermark/
  schema: 1
---
<p>RealtimeKit's watermark feature enables you to include an image as a watermark in your recording. To add watermark, configure the following parameters to video_config in the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a>.</p>
<table>
<thead>
<tr>
<th><strong>Parameter</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>URL</td>
<td>Specify the URL of the watermark image</td>
</tr>
<tr>
<td>Position</td>
<td>Specify the placement of the watermark, you have the flexibility to choose between left top, right top, left bottom, or right bottom. The default position is set to left top.</td>
</tr>
<tr>
<td>Size</td>
<td>Specify the height and width of the watermark in pixels.</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;video_config&quot;: {&#10;    &quot;watermark&quot;: {&#10;      &quot;url&quot;: &quot;https://test.io/images/client-logos-6.webp&quot;,&#10;      &quot;position&quot;: &quot;left top&quot;,&#10;      &quot;size&quot;: {&#10;        &quot;height&quot;: 20,&#10;        &quot;width&quot;: 100&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
