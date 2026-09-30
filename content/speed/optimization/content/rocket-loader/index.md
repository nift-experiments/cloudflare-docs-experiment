---
cp9:
  canonical: https://developers.cloudflare.com/speed/optimization/content/rocket-loader/
  description: Defer JavaScript loading to improve page rendering speed.
  full_title: Rocket Loader · Cloudflare Speed docs
  head_html: <title>Rocket Loader · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Defer JavaScript loading to improve page rendering speed."><link rel="canonical" href="https://developers.cloudflare.com/speed/optimization/content/rocket-loader/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/optimization/content/rocket-loader/index.md"><meta property="og:title" content="Rocket Loader · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Defer JavaScript loading to improve page rendering speed."><meta property="og:url" content="https://developers.cloudflare.com/speed/optimization/content/rocket-loader/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Speed"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/speed/optimization/content/rocket-loader/#page","headline":"Rocket Loader \u00b7 Cloudflare Speed docs","description":"Defer JavaScript loading to improve page rendering speed.","url":"https://developers.cloudflare.com/speed/optimization/content/rocket-loader/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /speed/optimization/content/rocket-loader/
  schema: 1
---
<p>Rocket Loader prioritizes your website's content (text, images, fonts, and more) by deferring the loading of all of your JavaScript until after rendering.</p>
<p>This type of loading (known as asynchronous loading) leads to earlier rendering of your page content. Rocket Loader handles both inline and external scripts, while maintaining order of execution. Cloudflare will detect incompatible browsers and disable Rocket Loader.</p>
<p>On pages with JavaScript, this results in a <a href="https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/">much faster loading experience</a> for your users and improves the following performance metrics:</p>
<ul>
<li>Time to First Paint (TTFP)</li>
<li>Time to First Contentful Paint (TTFCP)</li>
<li>Time to First Meaningful Paint (TTFMP)</li>
<li>Document Load</li>
</ul>
<h2 id="how-to">How to</h2>
<ul class="directory-listing"><li><a href="/speed/optimization/content/rocket-loader/enable/">Enable</a></li><li><a href="/speed/optimization/content/rocket-loader/ignore-javascripts/">Ignore JavaScripts</a></li></ul>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="limitations">Limitations</h2>
<p>Some of Cloudflare's optional features, including Rocket Loader and Email Obfuscation, use non standard tags that fail strict HTML validation via tools like <a href="https://validator.w3.org/">w3.org</a>. These failures do not correlate to issues for your site visitors.</p>
<p>If you observe JavaScript or jQuery issues for your website, <a href="/speed/optimization/content/rocket-loader/enable/">disable Rocket Loader</a> and retest your website.</p>
<p>If you have a <span class="nb-glossary-tooltip" title="content security policy (CSP)">Content Security Policy (CSP)</span> in place for your domain, you will need to <a href="/fundamentals/reference/policies-compliances/content-security-policies/#product-requirements">update your headers</a> to support Rocket Loader.
<br /></p>
