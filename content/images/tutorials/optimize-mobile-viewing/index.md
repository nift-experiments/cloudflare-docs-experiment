---
cp9:
  canonical: https://developers.cloudflare.com/images/tutorials/optimize-mobile-viewing/
  description: Lazy loading is an easy way to optimize the images on your webpages for mobile devices, with faster page load times and lower costs.
  full_title: Optimize mobile viewing · Cloudflare Images docs
  head_html: <title>Optimize mobile viewing · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Lazy loading is an easy way to optimize the images on your webpages for mobile devices, with faster page load times and lower costs."><link rel="canonical" href="https://developers.cloudflare.com/images/tutorials/optimize-mobile-viewing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/tutorials/optimize-mobile-viewing/index.md"><meta property="og:title" content="Optimize mobile viewing · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Lazy loading is an easy way to optimize the images on your webpages for mobile devices, with faster page load times and lower costs."><meta property="og:url" content="https://developers.cloudflare.com/images/tutorials/optimize-mobile-viewing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/tutorials/optimize-mobile-viewing/#page","headline":"Optimize mobile viewing \u00b7 Cloudflare Images docs","description":"Lazy loading is an easy way to optimize the images on your webpages for mobile devices, with faster page load times and lower costs.","url":"https://developers.cloudflare.com/images/tutorials/optimize-mobile-viewing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/tutorials/optimize-mobile-viewing/
  schema: 1
---
<p>You can use lazy loading to optimize the images on your webpages for mobile viewing. This helps address common challenges of mobile viewing, like slow network connections or weak processing capabilities.</p>
<p>Lazy loading has two main advantages:</p>
<ul>
<li><strong>Faster page load times</strong> — Images are loaded as the user scrolls down the page, instead of all at once when the page is opened.</li>
<li><strong>Lower costs for image delivery</strong> — When using Cloudflare Images, you only pay to load images that the user actually sees. With lazy loading, images that are not scrolled into view do not count toward your billable Images requests.</li>
</ul>
<p>Lazy loading is natively supported on all major browsers, including Chrome, Safari, Firefox, Opera, and Edge.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9341.md")
</aside>
<h2 id="modify-your-loading-attribute">Modify your loading attribute</h2>
<p>Without modifying your loading attribute, most browsers will fetch all images on a page, prioritizing the images that are closest to the viewport by default. You can override this by modifying your <code>loading</code> attribute.</p>
<p>There are two possible <code>loading</code> attributes for your <code>&lt;img&gt;</code> tags: <code>lazy</code> and <code>eager</code>.</p>
<h3 id="lazy-loading">Lazy loading</h3>
<p>Lazy loading is recommended for most images. With Lazy loading, resources like images are deferred until they reach a certain distance from the viewport. If an image does not reach the threshold, then it does not get loaded.</p>
<p>Example of modifying the <code>loading</code> attribute of your <code>&lt;img&gt;</code> tags to be <code>&quot;lazy&quot;</code>:</p>
<pre tabindex="0"><code class="language-html">&lt;img src=&quot;example.com/cdn-cgi/width=300/image.png&quot; loading=&quot;lazy&quot; /&gt;&#10;</code></pre>
<h3 id="eager-loading">Eager loading</h3>
<p>If you have images that are in the viewport, eager loading, instead of lazy loading, is recommended. Eager loading loads the asset at the initial page load, regardless of its location on the page.</p>
<p>Example of modifying the <code>loading</code> attribute of your <code>&lt;img&gt;</code> tags to be <code>&quot;eager&quot;</code>:</p>
<pre tabindex="0"><code class="language-html">&lt;img src=&quot;example.com/cdn-cgi/width=300/image.png&quot; loading=&quot;eager&quot; /&gt;&#10;</code></pre>
