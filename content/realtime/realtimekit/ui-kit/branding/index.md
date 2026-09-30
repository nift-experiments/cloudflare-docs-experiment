---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/branding/
  description: Customize meeting icons and branding in the RealtimeKit UI Kit.
  full_title: Customise Branding · Cloudflare Realtime docs
  head_html: <title>Customise Branding · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Customize meeting icons and branding in the RealtimeKit UI Kit."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/branding/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/branding/index.md"><meta property="og:title" content="Customise Branding · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Customize meeting icons and branding in the RealtimeKit UI Kit."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/branding/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/branding/#page","headline":"Customise Branding \u00b7 Cloudflare Realtime docs","description":"Customize meeting icons and branding in the RealtimeKit UI Kit.","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/branding/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/branding/
  schema: 1
---
<p>RealtimeKit's UI Kit provides all the necessary UI components to allow complete customization of all its UI Kit components. You can customize your meeting icons such as chat, clock, leave meeting, mic on and off, and more.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To get started with customizing the icons for your meetings, you need to first integrate RealtimeKit's Web SDK into your web application.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<h2 id="customize-the-default-icon-pack">Customize the default icon pack</h2>
<p>RealtimeKit's default icon set is available at <a href="https://icons.realtime.cloudflare.com/">icons.realtime.cloudflare.com</a>. You can modify and generate your custom icon set from there.</p>
<p>To replace RealtimeKit's default icon set with your own, pass the link to your icon set in the UI component.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12651.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12652.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12653.md")
</div>
<h2 id="iconpack-reference">IconPack reference</h2>
<p>The IconPack is an object where:</p>
<ul>
<li><strong>Object key</strong> - Denotes the name of the icon</li>
<li><strong>Object value</strong> - Stores the SVG string</li>
</ul>
<h3 id="available-icons">Available icons</h3>
<p>The default icon pack includes the following icons:</p>
<ul>
<li><code>attach</code></li>
<li><code>call_end</code></li>
<li><code>chat</code></li>
<li><code>checkmark</code></li>
<li><code>chevron_down</code></li>
<li><code>chevron_left</code></li>
<li><code>chevron_right</code></li>
<li><code>chevron_up</code></li>
<li><code>clock</code></li>
<li><code>copy</code></li>
<li><code>disconnected</code></li>
<li><code>dismiss</code></li>
<li><code>download</code></li>
<li><code>emoji_multiple</code></li>
<li><code>full_screen_maximize</code></li>
<li><code>full_screen_minimize</code></li>
<li><code>image</code></li>
<li><code>image_off</code></li>
<li><code>join_stage</code></li>
<li><code>leave_stage</code></li>
<li><code>mic_off</code></li>
<li><code>mic_on</code></li>
<li><code>more_vertical</code></li>
<li><code>participants</code></li>
<li><code>people</code></li>
<li><code>pin</code></li>
<li><code>pin_off</code></li>
<li><code>poll</code></li>
<li><code>recording</code></li>
<li><code>rocket</code></li>
<li><code>search</code></li>
<li><code>send</code></li>
<li><code>settings</code></li>
<li><code>share</code></li>
<li><code>share_screen_person</code></li>
<li><code>share_screen_start</code></li>
<li><code>share_screen_stop</code></li>
<li><code>speaker</code></li>
<li><code>spinner</code></li>
<li><code>spotlight</code></li>
<li><code>stop_recording</code></li>
<li><code>subtract</code></li>
<li><code>vertical_scroll</code></li>
<li><code>vertical_scroll_disabled</code></li>
<li><code>video_off</code></li>
<li><code>video_on</code></li>
<li><code>wand</code></li>
<li><code>warning</code></li>
<li><code>wifi</code></li>
</ul>
<p>Each icon in your custom icon pack JSON file should be defined as a key-value pair where the key matches one of the icon names above, and the value is the SVG string for that icon.</p>
<h2 id="next-steps">Next steps</h2>
<p>Explore additional customization options:</p>
<ul>
<li><a href="/realtime/realtimekit/ui-kit/">Render Default Meeting UI</a> - Complete meeting experience out of the box</li>
<li><a href="/realtime/realtimekit/ui-kit/build-your-own-ui/">Build Your Own UI</a> - Create custom meeting interfaces</li>
</ul>
