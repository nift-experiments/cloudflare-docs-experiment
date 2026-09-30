---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/stop-recording/
  description: Stop a RealtimeKit recording automatically or manually using the Stop Recording API.
  full_title: Stop Recording · Cloudflare Realtime docs
  head_html: <title>Stop Recording · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Stop a RealtimeKit recording automatically or manually using the Stop Recording API."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/stop-recording/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/stop-recording/index.md"><meta property="og:title" content="Stop Recording · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Stop a RealtimeKit recording automatically or manually using the Stop Recording API."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/stop-recording/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/stop-recording/#page","headline":"Stop Recording \u00b7 Cloudflare Realtime docs","description":"Stop a RealtimeKit recording automatically or manually using the Stop Recording API.","url":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/stop-recording/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/recording-guide/stop-recording/
  schema: 1
---
<p>RealtimeKit recordings can be stopped in any of the following ways:</p>
<ol>
<li><strong>Automatic Stop (Empty meeting)</strong>: A RealtimeKit recording will automatically stop
if the meeting has no participants for a duration of 1 minute or more. This
wait time can be customized by contacting RealtimeKit's support team to configure a
custom value for your app.</li>
<li><strong>Automatic Stop (maxSeconds elapsed)</strong>: A recording will automatically stop
when it reaches the duration specified by the <code>max_seconds</code> parameter passed
while starting the recording, regardless of whether participants are present
in the meeting. If this parameter is not passed, it defaults to 24 hours
(86400 seconds).</li>
<li><strong>Using Stop Recording API</strong>: A recording can also be stopped by passing the
recording ID and <code>stop</code> action to the <a href="/api/resources/realtime_kit/subresources/recordings/">Stop Recording API</a>.</li>
</ol>
<p>When a recording is stopped, it transitions to the <code>UPLOADING</code> state and then to the <code>UPLOADED</code> state after it has been transferred to RealtimeKit's storage and any external storage that has been set up.</p>
