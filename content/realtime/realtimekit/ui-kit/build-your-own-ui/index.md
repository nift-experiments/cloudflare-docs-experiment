---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/build-your-own-ui/
  description: Build a custom meeting interface video UI using RealtimeKit SDK components and Core SDK.
  full_title: Build Your Own UI · Cloudflare Realtime docs
  head_html: <title>Build Your Own UI · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Build a custom meeting interface video UI using RealtimeKit SDK components and Core SDK."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/build-your-own-ui/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/build-your-own-ui/index.md"><meta property="og:title" content="Build Your Own UI · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build a custom meeting interface video UI using RealtimeKit SDK components and Core SDK."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/build-your-own-ui/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/build-your-own-ui/#page","headline":"Build Your Own UI \u00b7 Cloudflare Realtime docs","description":"Build a custom meeting interface video UI using RealtimeKit SDK components and Core SDK.","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/build-your-own-ui/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/build-your-own-ui/
  schema: 1
---
<p>This guide explains how to use RealtimeKit UI Kit components to build a custom meeting interface instead of the default full-screen meeting view.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>This page builds upon the <a href="/realtime/realtimekit/core/">Initialize SDK</a>, <a href="/realtime/realtimekit/ui-kit/">Render Default Meeting UI</a>, and <a href="/realtime/realtimekit/ui-kit/state-management/">UI Kit States</a> guides. First refer to these pages to understand the core concepts.</p>
<p>The code examples on this page assume you have already imported the necessary packages and initialized the SDK.</p>
<h2 id="build-a-custom-ui-with-ui-kit">Build a custom UI with UI Kit</h2>
<p>If the default meeting component does not provide enough control over layout or behavior, use <a href="/realtime/realtimekit/ui-kit/component-library/">UI Kit components</a> to build a custom interface. The UI Kit provides pre-built components on top of the Core SDK. You can mix and match pieces while saving time compared to building from scratch.</p>
<p>A custom UI requires you to manage participant audio, notifications, dialogs, component layout, and screen transitions.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11760.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11761.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11762.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11763.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11764.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11765.md")
</div>
<h2 id="example-code">Example code</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11766.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11767.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11768.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11769.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11770.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11771.md")
</div>
