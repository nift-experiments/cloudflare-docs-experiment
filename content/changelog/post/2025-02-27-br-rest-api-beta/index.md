---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-02-27-br-rest-api-beta/
  description: New updates and improvements at Cloudflare.
  full_title: New REST API is in open beta! · Changelog
  head_html: <title>New REST API is in open beta! · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-02-27-br-rest-api-beta/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New REST API is in open beta! · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-02-27-br-rest-api-beta/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-27-br-rest-api-beta/#page","headline":"New REST API is in open beta! \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-02-27-br-rest-api-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-02-27-br-rest-api-beta/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 27, 2025</time><h2 id="post-title">New REST API is in open beta!</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>We've released a new REST API for <a href="/browser-run/">Browser Rendering</a> in open beta, making interacting with browsers easier than ever. This new API provides endpoints for common browser actions, with more to be added in the future.</p>
<p>With the <strong>REST API</strong> you can:</p>
<ul>
<li><strong>Capture screenshots</strong> – Use <code>/screenshot</code> to take a screenshot of a webpage from provided URL or HTML.</li>
<li><strong>Generate PDFs</strong> – Use <code>/pdf</code> to convert web pages into PDFs.</li>
<li><strong>Extract HTML content</strong> – Use <code>/content</code> to retrieve the full HTML from a page.
<strong>Snapshot (HTML + Screenshot)</strong> – Use <code>/snapshot</code> to capture both the page's HTML and a screenshot in one request</li>
<li><strong>Scrape Web Elements</strong> – Use <code>/scrape</code> to extract specific elements from a page.</li>
</ul>
<p>For example, to capture a screenshot:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/screenshot&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;html&quot;: &quot;Hello World!&quot;,&#10;    &quot;screenshotOptions&quot;: {&#10;      &quot;type&quot;: &quot;webp&quot;,&#10;      &quot;omitBackground&quot;: true&#10;    }&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.webp&quot;&#10;</code></pre>
<p>Learn more in our <a href="/browser-run/quick-actions/">documentation</a>.</p>
</div></article></div>
