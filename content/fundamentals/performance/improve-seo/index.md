---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/performance/improve-seo/
  description: Use Cloudflare features like caching, HTTPS, and Crawler Hints to improve your website's search engine rankings.
  full_title: Improve SEO · Cloudflare Fundamentals docs
  head_html: <title>Improve SEO · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Cloudflare features like caching, HTTPS, and Crawler Hints to improve your website&#x27;s search engine rankings."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/performance/improve-seo/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/performance/improve-seo/index.md"><meta property="og:title" content="Improve SEO · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Cloudflare features like caching, HTTPS, and Crawler Hints to improve your website&#x27;s search engine rankings."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/performance/improve-seo/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/performance/improve-seo/#page","headline":"Improve SEO \u00b7 Cloudflare Fundamentals docs","description":"Use Cloudflare features like caching, HTTPS, and Crawler Hints to improve your website's search engine rankings.","url":"https://developers.cloudflare.com/fundamentals/performance/improve-seo/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/performance/improve-seo/
  schema: 1
---
<p>The goal of Search Engine Optimization (SEO) is to get your website to rank higher on various search engine providers (Google, Bing, etc.).</p>
<p>In practice, SEO is primarily about quality content, user experience, and not making things more difficult for search engine crawlers. While Cloudflare cannot write quality content for you, our service can help with user experience — especially related to <a href="https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/">site speed</a> — and search crawlers.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="tip">Tip:</h3>
@markup("md", "content/.markup/bodies/8810.md")
</aside>
<h2 id="seo-improvements-with-cloudflare">SEO improvements with Cloudflare</h2>
<p>Several Cloudflare features improve Search Engine site rankings. However, meaningful and regularly updated site content is still crucial to improving SEO.</p>
<h3 id="increase-site-speed">Increase site speed</h3>
<p>Since at least 2010, Google has publicly stated that <a href="https://webmasters.googleblog.com/2010/04/using-site-speed-in-web-search-ranking.html">site speed affects your Google ranking</a>.</p>
<p>Cloudflare offers multiple features to <a href="/speed/">optimize site performance</a>.</p>
<h3 id="enable-https">Enable HTTPS</h3>
<p>Since search engines use HTTPS as <a href="https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html">a ranking signal</a>, HTTPS is vital for SEO.</p>
<p>To make sure your domain is accessible over HTTPS:</p>
<ol>
<li>Get an <a href="/ssl/get-started/">SSL/TLS certificate</a> for your domain.</li>
<li><a href="/ssl/edge-certificates/encrypt-visitor-traffic/">Redirect visitors</a> to the HTTPS version of your domain.</li>
</ol>
<h3 id="enable-crawler-hints">Enable Crawler Hints</h3>
<p>With <a href="/cache/advanced-configuration/crawler-hints/">Crawler Hints</a>, search engines and other bot-powered experiences have the freshest version of your content, translating into happier users and ultimately influencing search rankings.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>Depending on your domain's security settings, you might accidentally block search engine crawlers.</p>
<p>If you notice SEO issues, make sure your:</p>
<ul>
<li><a href="/waf/troubleshooting/faq/#caution-about-potentially-blocking-bots">WAF custom rules</a> are allowing <strong>Verified Bots</strong>.</li>
<li><a href="/waf/rate-limiting-rules/">Rate limiting rules</a> are allowing <strong>Verified Bots</strong>.</li>
<li><a href="/bots/concepts/bot/verified-bots/">Bot protection</a> settings are not blocking <strong>Verified Bots</strong>.</li>
</ul>
<p>If you still notice issues with search engine crawlers, refer to our <a href="/support/troubleshooting/general-troubleshooting/troubleshooting-crawl-errors/">Troubleshooting guide</a>.</p>
<h2 id="common-misconceptions">Common misconceptions</h2>
<p>The following characteristics do not affect your domain's SEO:</p>
<ul>
<li><strong>Changing your nameservers</strong>: Using Cloudflare's nameservers does not affect your domain's SEO.</li>
<li><strong>Server location</strong>: According to Google, <a href="http://www.seroundtable.com/seo-geo-location-server-google-17468.html">server location</a> is not important for SEO.</li>
<li><strong>Sites sharing IP addresses</strong>: Search engines do not generally penalize domains using shared IP addresses unless several of these sites are malicious or spammy.</li>
<li><strong>Cloudflare caching</strong>: When Cloudflare caches your content, it actually speeds up content delivery and only improves SEO. Our caching does not create duplicate content, rewrite URLs, or create additional subdomains.</li>
</ul>
