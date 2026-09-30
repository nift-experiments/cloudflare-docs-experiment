---
cp9:
  canonical: https://developers.cloudflare.com/images/optimization/transformations/overview/
  description: Cloudflare Images transformations optimize and cache remote images from any origin at the edge.
  full_title: Overview · Cloudflare Images docs
  head_html: <title>Overview · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare Images transformations optimize and cache remote images from any origin at the edge."><link rel="canonical" href="https://developers.cloudflare.com/images/optimization/transformations/overview/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/optimization/transformations/overview/index.md"><meta property="og:title" content="Overview · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare Images transformations optimize and cache remote images from any origin at the edge."><meta property="og:url" content="https://developers.cloudflare.com/images/optimization/transformations/overview/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/optimization/transformations/overview/#page","headline":"Overview \u00b7 Cloudflare Images docs","description":"Cloudflare Images transformations optimize and cache remote images from any origin at the edge.","url":"https://developers.cloudflare.com/images/optimization/transformations/overview/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/optimization/transformations/overview/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/9462.md")
</div>
<p>When you ship applications on Cloudflare, you can use Images to automatically optimize and cache your images from any origin.</p>
<p>Our image optimization pipeline provides a rich set of <a href="/images/optimization/features">features</a> that can be applied across entire media libraries to compress images at scale, transcode files into efficient formats for delivery, and resize and crop images for different use cases and devices.</p>
<h2 id="how-it-works">How it works</h2>
<p>You can request transformations by using a specially-formatted URL to serve images on your Cloudflare zone or through Workers.</p>
<p>To serve transformations on your zone, you must first enable the feature:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/?to=/:account/images/transformations">Cloudflare dashboard</a>, go to <strong>Images</strong> &gt; <strong>Transformations</strong>.</li>
<li>Select the zone where you want to serve transformations.</li>
<li>Enable <strong>transformations</strong> on your zone.</li>
</ol>
<p>When the browser requests a transformed image, Cloudflare checks the edge cache for a previously optimized version with the same parameters:</p>
<p><strong>On a cache hit</strong> — Cloudflare serves the optimized image directly from the edge without contacting the origin or re-applying the optimization parameters.</p>
<p><strong>On a cache miss</strong> — Cloudflare fetches the original image from the source origin, applies the requested parameters (e.g. <code>format</code>, <code>width</code>, <code>quality</code>), caches the transformed result, and serves it to the browser. The original image is also cached to speed up future transformations of the same source.</p>
<p>Each unique combination of source image and parameters is cached and billed separately. The first request for each unique version within a calendar month is billed as one <a href="/images/optimization/features">unique transformation</a>, regardless of cache status. Subsequent requests for this transformation do not incur billable usage within the same calendar month.</p>
<h2 id="configure-your-zone">Configure your zone</h2>
<p>After enabling transformations on your zone, you can configure how Cloudflare handles transformation requests:</p>
<ul>
<li><strong><a href="/images/optimization/transformations/sources">Define source origins</a></strong> — Specify which origins Cloudflare can pull source images from. By default, Cloudflare only accepts source images from the same zone where transformations are served.</li>
<li><strong><a href="/images/optimization/transformations/flows">Create transformation flows</a></strong> — Set up automated rules that apply image optimization to matching requests without requiring URL changes or custom code.</li>
<li><strong><a href="/images/optimization/transformations/control-origin-access">Control origin access</a></strong> — Use Workers to add custom logic for validating and controlling access to source images.</li>
<li><strong><a href="/images/optimization/transformations/rewrite-rules">Set up rewrite rules</a></strong> — Use Transform Rules to rewrite image URLs and serve transformations from custom paths.</li>
</ul>
