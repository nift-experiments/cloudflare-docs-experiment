---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-21-improved-soft-navigation-measurement-for-single-page-applications/
  description: New updates and improvements at Cloudflare.
  full_title: Web Analytics improves soft navigation measurement for Single Page Applications (SPAs) · Changelog
  head_html: <title>Web Analytics improves soft navigation measurement for Single Page Applications (SPAs) · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-21-improved-soft-navigation-measurement-for-single-page-applications/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Web Analytics improves soft navigation measurement for Single Page Applications (SPAs) · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-21-improved-soft-navigation-measurement-for-single-page-applications/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-21-improved-soft-navigation-measurement-for-single-page-applications/#page","headline":"Web Analytics improves soft navigation measurement for Single Page Applications (SPAs) \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-21-improved-soft-navigation-measurement-for-single-page-applications/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-21-improved-soft-navigation-measurement-for-single-page-applications/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 21, 2026</time><h2 id="post-title">Web Analytics improves soft navigation measurement for Single Page Applications (SPAs)</h2>
<div class="changelog-badges"><span>web-analytics</span></div><div class="changelog-body"><p>Cloudflare Web Analytics (Real User Monitoring) is rolling out accuracy improvements to client-side soft navigations. <strong>Update: this update is complete as of 2026-09-04.</strong></p>
<p><strong>This change may alter the volume of reported pageviews and visits in the dashboard and GraphQL API. The reported Largest Contentful Paint (LCP) metric may also fluctuate.</strong> The extent of these variances depend on your front-end architecture and visitor traffic patterns.</p>
<p>Single Page Applications (SPAs)—such as websites built with React, Angular, Vue, or Svelte—predominantly use soft navigations. Soft navigations avoid fully unloading the current page and rendering the next one from scratch as visitors navigate.</p>
<p>Any client-side navigation counts as a soft navigation, including navigations intercepted by <a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API">the Navigation API</a> or triggered by <a href="https://developer.mozilla.org/en-US/docs/Web/API/History_API">the History API</a>. This means a non-SPA website can have soft navigation activity if its implementation uses these APIs.</p>
<p>The main improvement comes from <a href="https://developer.chrome.com/docs/web-platform/soft-navigations">Google Chrome's new Soft Navigation API</a>. It natively measures <a href="/web-analytics/data-metrics/core-web-vitals/#core-web-vitals-metrics">Largest Contentful Paint (LCP)</a> on soft navigations, removing a blind spot in perceived loading speed across pageviews.</p>
<p>We've extended our <code>navigationType</code> values to segment these different types of navigations:</p>
<table>
<thead>
<tr>
<th><code>navigationType</code></th>
<th>New?</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>navigate</code></td>
<td>❌</td>
<td>Hard navigations that traditional websites (or &quot;Multi Page Applications&quot;) perform when clicking links or submitting forms</td>
</tr>
<tr>
<td><code>soft-navigation</code></td>
<td>✅</td>
<td>Where <a href="https://developer.chrome.com/docs/web-platform/soft-navigations">the new Soft Navigation API</a> is available and a visitor makes a client-side navigation, we record these events</td>
</tr>
<tr>
<td><code>routing-apis</code></td>
<td>✅</td>
<td>Where the native Soft Navigation API is unavailable (e.g. Safari, Firefox, older Chromium-based browsers), we fallback to measuring soft navigations using <a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API">the Navigation API</a> or <a href="https://developer.mozilla.org/en-US/docs/Web/API/History_API">History API</a>. We cannot collect LCP for these, but the other Core Web Vitals are present.</td>
</tr>
</tbody>
</table>
<p>Prior to this change, we only used History API and all navigations were bucketed into <code>navigate</code>.</p>
<p>For more information, refer to the <a href="/web-analytics/data-metrics/dimensions/#navigation-types">Navigation Types</a> and <a href="/web-analytics/get-started/web-analytics-spa/">Web Analytics SPA</a> documentation pages.</p>
</div></article></div>
