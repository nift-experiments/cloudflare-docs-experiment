---
cp9:
  canonical: https://developers.cloudflare.com/turnstile/
  description: Verify visitors are human with a CAPTCHA-free, privacy-preserving alternative.
  full_title: Overview · Cloudflare Turnstile docs
  head_html: <title>Overview · Cloudflare Turnstile docs</title><meta name="generator" content="Nift"><meta name="description" content="Verify visitors are human with a CAPTCHA-free, privacy-preserving alternative."><link rel="canonical" href="https://developers.cloudflare.com/turnstile/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/turnstile/index.md"><meta property="og:title" content="Overview · Cloudflare Turnstile docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Verify visitors are human with a CAPTCHA-free, privacy-preserving alternative."><meta property="og:url" content="https://developers.cloudflare.com/turnstile/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Turnstile"><meta name="algolia_product_filter" content="Turnstile"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Turnstile"><meta name="pcx_tags" content="Privacy"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/turnstile/#page","headline":"Overview \u00b7 Cloudflare Turnstile docs","description":"Verify visitors are human with a CAPTCHA-free, privacy-preserving alternative.","url":"https://developers.cloudflare.com/turnstile/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Privacy"]}</script>
  markdown: true
  noindex: false
  route: /turnstile/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/237.md")
</div>
<p>Turnstile can be embedded into any website without sending traffic through Cloudflare and works without showing visitors a CAPTCHA.</p>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/7f1104dc5895d96c1957a4db5fdf496a/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2F5b75f329-b7fe-4122-cae4-9bee54c35100%2Fpublic" title="Get started with Cloudflare Turnstile" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<p>Cloudflare issues challenges through the <a href="/cloudflare-challenges/">Challenge Platform</a>, which is the same underlying technology powering <a href="/turnstile/">Turnstile</a>.</p>
<p>In contrast to our Challenge page offerings, Turnstile allows you to run challenges anywhere on your site in a less-intrusive way without requiring the use of Cloudflare's CDN.</p>
<h2 id="how-turnstile-works">How Turnstile works</h2>
<p><img src="/assets/upstream/images/turnstile/turnstile-overview.png" alt="Turnstile Overview" /></p>
<p>Turnstile adapts the challenge outcome to the individual visitor or browser. First, we run a series of small non-interactive JavaScript challenges to gather signals about the visitor or browser environment.</p>
<p>These challenges include proof-of-work (computational puzzles), proof-of-space, probing for web APIs, and various other challenges for detecting browser-quirks and human behavior. As a result, we can fine-tune the difficulty of the challenge to the specific request and avoid showing a visual or interactive puzzle to a user.</p>
<p>Turnstile performs client-side security challenges on behalf of the website operator to distinguish human visitors from automated traffic. To do so, Turnstile processes only the data strictly necessary to provide this security function. Turnstile does not access, store, or transmit user communications, form entries, or other page inputs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/236.md")
</aside>
<h3 id="widget-types">Widget types</h3>
<p>Turnstile <a href="/turnstile/concepts/widget/">widget types</a> include:</p>
<ul>
<li><strong>Managed</strong> (recommended): Automatically decides whether to show a checkbox based on visitor risk level.</li>
<li><strong>Non-interactive</strong>: Visitors never need to interact with the widget.</li>
<li><strong>Invisible</strong>: The widget is completely hidden from the visitor.</li>
</ul>
<hr />
<h2 id="accessibility">Accessibility</h2>
<p>Turnstile is WCAG 2.2 AA compliant.</p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/238.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/239.md")
</div>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/240.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/241.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/242.md")
</div>
<hr />
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/244.md")
</div>
