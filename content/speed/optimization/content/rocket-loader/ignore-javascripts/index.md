---
cp9:
  canonical: https://developers.cloudflare.com/speed/optimization/content/rocket-loader/ignore-javascripts/
  description: Exclude specific scripts from Rocket Loader optimization.
  full_title: Ignore JavaScripts in Rocket Loader · Cloudflare Speed docs
  head_html: <title>Ignore JavaScripts in Rocket Loader · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Exclude specific scripts from Rocket Loader optimization."><link rel="canonical" href="https://developers.cloudflare.com/speed/optimization/content/rocket-loader/ignore-javascripts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/optimization/content/rocket-loader/ignore-javascripts/index.md"><meta property="og:title" content="Ignore JavaScripts in Rocket Loader · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Exclude specific scripts from Rocket Loader optimization."><meta property="og:url" content="https://developers.cloudflare.com/speed/optimization/content/rocket-loader/ignore-javascripts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Speed"><meta name="pcx_tags" content="JavaScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/speed/optimization/content/rocket-loader/ignore-javascripts/#page","headline":"Ignore JavaScripts in Rocket Loader \u00b7 Cloudflare Speed docs","description":"Exclude specific scripts from Rocket Loader optimization.","url":"https://developers.cloudflare.com/speed/optimization/content/rocket-loader/ignore-javascripts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript"]}</script>
  markdown: true
  noindex: false
  route: /speed/optimization/content/rocket-loader/ignore-javascripts/
  schema: 1
---
<p>You can have Rocket Loader ignore individual scripts by adding the <code>data-cfasync=&quot;false&quot;</code> attribute to the relevant script tag:</p>
<pre tabindex="0"><code class="language-html">&lt;script data-cfasync=&quot;false&quot; src=&quot;/javascript.js&quot;&gt;&lt;/script&gt;&#10;</code></pre>
<p>Rocket Loader will still optimize the loading of all other scripts on the page.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13945.md")
</aside>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Adding this attribute within JavaScript will not work if you wish to exclude the script from Rocket Loader.</li>
<li>If the script you want Rocket Loader to ignore has dependency on other JavaScript(s) on the page, those dependencies must also have the <code>data-cfasync=&quot;false&quot;</code> attribute.</li>
<li>The <code>data-cfasync</code> attribute must be added before the <code>src</code> attribute.</li>
<li>Rocket Loader will recognize the tag when either single or double quotes are placed around the attribute value.</li>
</ul>
