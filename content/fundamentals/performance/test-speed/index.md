---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/performance/test-speed/
  description: Test your website speed and Internet connection using Cloudflare dashboard tools and third-party services.
  full_title: Test speed · Cloudflare Fundamentals docs
  head_html: <title>Test speed · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Test your website speed and Internet connection using Cloudflare dashboard tools and third-party services."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/performance/test-speed/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/performance/test-speed/index.md"><meta property="og:title" content="Test speed · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Test your website speed and Internet connection using Cloudflare dashboard tools and third-party services."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/performance/test-speed/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/performance/test-speed/#page","headline":"Test speed \u00b7 Cloudflare Fundamentals docs","description":"Test your website speed and Internet connection using Cloudflare dashboard tools and third-party services.","url":"https://developers.cloudflare.com/fundamentals/performance/test-speed/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/performance/test-speed/
  schema: 1
---
<p>Cloudflare offers several tools to test the speed of your website, as well as the speed of your Internet connection.</p>
<hr />
<h2 id="test-website-speed">Test website speed</h2>
<h3 id="using-cloudflare">Using Cloudflare</h3>
<p>Once your domain is <a href="/fundamentals/manage-domains/add-site/">active on Cloudflare</a>, you can run speed tests within the <a href="https://dash.cloudflare.com/?to=/:account/:zone/speed">Cloudflare dashboard</a>.</p>
<p>This speed test will provide information about critical loading times, performance with and without <a href="/fundamentals/concepts/how-cloudflare-works/">Cloudflare's proxy</a>, and recommended optimizations.</p>
<p>If you experience any issues, make sure you are not blocking specific <a href="/fundamentals/reference/cloudflare-site-crawling/#other-situations">user agents</a>.</p>
<h3 id="using-third-party-tools">Using third-party tools</h3>
<p>If your domain is not yet active on Cloudflare or you want to measure the before and after improvements of using Cloudflare, Cloudflare recommends using the following third-party tools:</p>
<ul>
<li><a href="https://pagegym.com/">PageGym</a></li>
<li><a href="https://gtmetrix.com/">GTmetrix</a></li>
<li><a href="https://www.debugbear.com/test/website-speed">DebugBear</a></li>
<li><a href="https://developer.chrome.com/docs/lighthouse/">Lighthouse</a></li>
<li><a href="https://www.webpagetest.org/">WebPageTest</a></li>
</ul>
<p>If you use these third-party tools, you should do the following to test website speed:</p>
<ol>
<li><a href="/fundamentals/manage-domains/pause-cloudflare/">Pause Cloudflare</a> to remove performance and caching benefits.</li>
<li>Run a speed test.</li>
<li>Unpause Cloudflare.</li>
<li>Run a speed test<sup><a href="#footnote-1">1</a></sup>.</li>
<li>Run a second speed test to get your baseline performance with Cloudflare.</li>
</ol>
<h3 id="improve-speed">Improve speed</h3>
<p>Based on the results of these speed tests, you may want to explore other ways to <a href="/speed/">optimize your site speed</a> using Cloudflare.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8809.md")
</aside>
<hr />
<h2 id="test-internet-speed">Test Internet speed</h2>
<p>To test the speed of your home network connection (download, update, packet loss, ping measurements, and more), visit <a href="https://speed.cloudflare.com">speed.cloudflare.com</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">The results of your first speed test with Cloudflare will likely contain uncached results, which will provide inaccurate results.<br/><br/>One of the key ways Cloudflare speeds up your site is through [caching](/cache/), which will appear in the results of the second test.</li></ol></section>
