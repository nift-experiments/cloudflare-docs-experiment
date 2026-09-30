---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-30-rum-navigation-types/
  description: New updates and improvements at Cloudflare.
  full_title: Web Analytics adds Navigation Type filtering and reporting · Changelog
  head_html: <title>Web Analytics adds Navigation Type filtering and reporting · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-30-rum-navigation-types/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Web Analytics adds Navigation Type filtering and reporting · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-30-rum-navigation-types/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-30-rum-navigation-types/#page","headline":"Web Analytics adds Navigation Type filtering and reporting \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-30-rum-navigation-types/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-30-rum-navigation-types/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 30, 2026</time><h2 id="post-title">Web Analytics adds Navigation Type filtering and reporting</h2>
<div class="changelog-badges"><span>web-analytics</span></div><div class="changelog-body"><p>Cloudflare Web Analytics now supports <strong>Navigation Type</strong> reporting and filtering.</p>
<p>This update allows developers and performance analysts to see how users are navigating between pages — whether through a link click or form submission, a page reload, or using the browser's back/forward buttons — and whether a browser cache hit occurred for these behaviors.</p>
<p>Understanding navigation types is critical for optimizing user experience. For example, if a high volume of your traffic consists of &quot;Back-forward&quot; navigations versus &quot;Back-forward Cache&quot;, those visitors are not benefiting from the Back/Forward Cache (bfcache) and therefore are experiencing higher load times due to potentially unnecessary network requests.</p>
<p>The same applies for regular &quot;Navigate&quot; entries — where &quot;Navigate Cache&quot;, &quot;Navigate Prefetch Cache&quot; and &quot;Prerender&quot; would provide instant document retrieval — and &quot;Reload&quot;, where &quot;Reload cache&quot; would be more optimal.</p>
<p>A high volume of &quot;Reload&quot; entries can also indicate a potential stability problem with your website.</p>
<p>By identifying these patterns, you can tune your browser caching strategies to ensure HTML documents are served instantaneously from local caches rather than requiring a roundtrip to the network.</p>
<p>For more information, refer to <a href="/web-analytics/data-metrics/dimensions/#navigation-types">Navigation Types</a>.</p>
<h4 id="key-benefits">Key benefits</h4>
<ul>
<li><strong>Monitor Cache Effectiveness:</strong> See how often your site is served from the HTTP cache or bfcache.</li>
<li><strong>Identify Performance Bottlenecks:</strong> Filter by the different types to understand performance opportunity of improving browser cache hit ratio.</li>
</ul>
<h4 id="analyze-navigation-types-in-the-cloudflare-dashboard">Analyze navigation types in the Cloudflare dashboard</h4>
<p>You can now find the <strong>Navigation Type</strong> dimension in the Web Analytics dashboard. You can filter to include/exclude one or more specific types using &quot;equals&quot;, &quot;does not equal&quot;, &quot;in&quot;, or &quot;not in&quot; matchers.</p>
<p><img src="/assets/upstream/images/web-analytics/dash-web_analytics-navigation-type-filter.png" alt="Navigation Type filter" /></p>
<p>To check the list of popular navigation types, select <strong>Page views</strong> on the Web Analytics sidebar and scroll down to the bottom:</p>
<p><img src="/assets/upstream/images/web-analytics/dash-web_analytics-navigation-types-list.png" alt="Navigation Types list in Page Views tab" /></p>
</div></article></div>
