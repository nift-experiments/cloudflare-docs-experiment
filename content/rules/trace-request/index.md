---
cp9:
  canonical: https://developers.cloudflare.com/rules/trace-request/
  description: Trace a request through Cloudflare to see which rules match and apply.
  full_title: Trace a request with Cloudflare Trace · Cloudflare Rules docs
  head_html: <title>Trace a request with Cloudflare Trace · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Trace a request through Cloudflare to see which rules match and apply."><link rel="canonical" href="https://developers.cloudflare.com/rules/trace-request/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/trace-request/index.md"><meta property="og:title" content="Trace a request with Cloudflare Trace · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Trace a request through Cloudflare to see which rules match and apply."><meta property="og:url" content="https://developers.cloudflare.com/rules/trace-request/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/trace-request/#page","headline":"Trace a request with Cloudflare Trace \u00b7 Cloudflare Rules docs","description":"Trace a request through Cloudflare to see which rules match and apply.","url":"https://developers.cloudflare.com/rules/trace-request/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/trace-request/
  schema: 1
---
<div class="nb-plan">
<p>Available on all plans</p>
</div>
<p>Cloudflare Trace <div class="nb-data-component" data-cf-component="ProductAvailabilityText"></div> simulates an HTTP/S request through Cloudflare's network to your origin server. Use this tool to understand how your Cloudflare configurations (such as rules, caching, and security settings) would affect a specific request. If the hostname you are testing is not <a href="/dns/proxy-status/">proxied by Cloudflare</a>, Cloudflare Trace will still return all the configurations that Cloudflare would have applied to the request.</p>
<p>You can define specific request properties to simulate different conditions for an HTTP/S request. Rules that are turned off in Cloudflare products will not be evaluated.</p>
<p>Cloudflare Trace is available to users with an Administrator or Super Administrator role.</p>
<h2 id="when-to-use-trace">When to use Trace</h2>
<p>Use Trace when you need to test what would happen with a simulated request:</p>
<ul>
<li>Understanding why a rule did not trigger as expected</li>
<li>Testing how your rules handle different request scenarios</li>
<li>Seeing the evaluation order of your rules</li>
<li>Simulating requests from different geolocations or conditions</li>
</ul>
<p>Use <a href="/log-explorer/">Log Explorer</a> when you need to investigate what actually happened with real production traffic:</p>
<ul>
<li>Analyzing historical data and trends</li>
<li>Investigating security incidents after they occur</li>
<li>Searching for patterns across thousands of requests</li>
<li>Monitoring application performance over time</li>
<li>Providing forensic evidence to support teams</li>
</ul>
<p>The key difference is that Trace simulates &quot;what-if&quot; scenarios, while Log Explorer shows actual historical traffic.</p>
<h2 id="resources">Resources</h2>
<ul class="directory-listing"><li><a href="/rules/trace-request/how-to/">Use Cloudflare Trace</a></li><li><a href="/rules/trace-request/limitations/">Cloudflare Trace limitations</a></li><li><a href="/rules/trace-request/changelog/">Cloudflare Trace changelog</a></li></ul>
