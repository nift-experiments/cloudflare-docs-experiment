---
cp9:
  canonical: https://developers.cloudflare.com/pages/functions/smart-placement/
  description: Automatically run Pages Functions closer to your back-end infrastructure to reduce latency.
  full_title: Smart Placement · Cloudflare Pages docs
  head_html: <title>Smart Placement · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Automatically run Pages Functions closer to your back-end infrastructure to reduce latency."><link rel="canonical" href="https://developers.cloudflare.com/pages/functions/smart-placement/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/functions/smart-placement/index.md"><meta property="og:title" content="Smart Placement · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Automatically run Pages Functions closer to your back-end infrastructure to reduce latency."><meta property="og:url" content="https://developers.cloudflare.com/pages/functions/smart-placement/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/functions/smart-placement/#page","headline":"Smart Placement \u00b7 Cloudflare Pages docs","description":"Automatically run Pages Functions closer to your back-end infrastructure to reduce latency.","url":"https://developers.cloudflare.com/pages/functions/smart-placement/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/functions/smart-placement/
  schema: 1
---
<p>By default, <a href="/workers/">Workers</a> and <a href="/pages/functions/">Pages Functions</a> are invoked in a data center closest to where the request was received. If you are running back-end logic in a Pages Function, it may be more performant to run that Pages Function closer to your back-end infrastructure rather than the end user. Smart Placement (beta) automatically places your workloads in an optimal location that minimizes latency and speeds up your applications.</p>
<h2 id="background">Background</h2>
<p>Smart Placement applies to Pages Functions and middleware. Normally, assets are always served globally and closest to your users.</p>
<p>Smart Placement on Pages currently has some caveats. While assets are always meant to be served from a location closest to the user, there are two exceptions to this behavior:</p>
<ol>
<li>
<p>If using middleware for every request (<code>functions/_middleware.js</code>) when Smart Placement is enabled, all assets will be served from a location closest to your back-end infrastructure. This may result in an unexpected increase in latency as a result.</p>
</li>
<li>
<p>When using <a href="https://developers.cloudflare.com/pages/functions/advanced-mode/"><code>env.ASSETS.fetch</code></a>, assets served via the <code>ASSETS</code> fetcher from your Pages Function are served from the same location as your Function. This could be the location closest to your back-end infrastructure and not the user.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10941.md")
</aside>
<h2 id="enable-smart-placement-beta">Enable Smart Placement (beta)</h2>
<p>Smart Placement is available on all plans.</p>
<h3 id="enable-smart-placement-via-the-dashboard">Enable Smart Placement via the dashboard</h3>
<p>To enable Smart Placement via the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Pages project.</li>
<li>Select <strong>Settings</strong> &gt; <strong>Runtime</strong>.</li>
<li>Under <strong>Placement</strong>, choose <strong>Smart</strong>.</li>
<li>Send some initial traffic (approximately 20-30 requests) to your Pages Functions. It takes a few minutes after you have sent traffic to your Pages Function for Smart Placement to take effect.</li>
<li>View your Pages Function's <a href="/workers/observability/metrics-and-analytics/">request duration metrics</a> under Functions Metrics.</li>
</ol>
<h2 id="give-feedback-on-smart-placement">Give feedback on Smart Placement</h2>
<p>Smart Placement is in beta. To share your thoughts and experience with Smart Placement, join the <a href="https://discord.cloudflare.com">Cloudflare Developer Discord</a>.</p>
