---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/quick-actions/
  description: Use Browser Run Quick Actions HTTP endpoints to capture screenshots, extract HTML, generate PDFs, and perform other common browser tasks.
  full_title: Quick Actions · Cloudflare Browser Run docs
  head_html: <title>Quick Actions · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Browser Run Quick Actions HTTP endpoints to capture screenshots, extract HTML, generate PDFs, and perform other common browser tasks."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/quick-actions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/quick-actions/index.md"><meta property="og:title" content="Quick Actions · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Browser Run Quick Actions HTTP endpoints to capture screenshots, extract HTML, generate PDFs, and perform other common browser tasks."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/quick-actions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/browser-run/quick-actions/#page","headline":"Quick Actions \u00b7 Cloudflare Browser Run docs","description":"Use Browser Run Quick Actions HTTP endpoints to capture screenshots, extract HTML, generate PDFs, and perform other common browser tasks.","url":"https://developers.cloudflare.com/browser-run/quick-actions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/quick-actions/
  schema: 1
---
<p>Quick Actions provide simple interfaces for common browser tasks like capturing screenshots, extracting HTML content, generating PDFs, and more. You can use Quick Actions in two ways:</p>
<ul>
<li><strong>REST API</strong>: HTTP endpoints for one-off requests or external integration.</li>
<li><strong>Workers Bindings</strong>: Call Quick Actions directly from a <a href="/workers/">Cloudflare Worker</a> using <code>env.BROWSER.quickAction()</code>.</li>
</ul>
<p>The following are the available options:</p>
<ul class="directory-listing"><li><a href="/browser-run/quick-actions/content-endpoint/">/content - Fetch HTML</a></li><li><a href="/browser-run/quick-actions/screenshot-endpoint/">/screenshot - Capture screenshot</a></li><li><a href="/browser-run/quick-actions/pdf-endpoint/">/pdf - Render PDF</a></li><li><a href="/browser-run/quick-actions/markdown-endpoint/">/markdown - Extract Markdown from a webpage</a></li><li><a href="/browser-run/quick-actions/snapshot/">/snapshot - Capture multiple page formats</a></li><li><a href="/browser-run/quick-actions/accessibility-tree-endpoint/">/accessibilityTree - Capture accessibility tree</a></li><li><a href="/browser-run/quick-actions/scrape-endpoint/">/scrape - Scrape HTML elements</a></li><li><a href="/browser-run/quick-actions/json-endpoint/">/json - Capture structured data using AI</a></li><li><a href="/browser-run/quick-actions/links-endpoint/">/links - Retrieve links from a webpage</a></li><li><a href="/browser-run/quick-actions/crawl-endpoint/">/crawl - Crawl web content</a></li><li><a href="/api/resources/browser_rendering/">Reference</a></li></ul>
<p><a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code></a> is available via the REST API only.</p>
<p>Use Quick Actions when you need a fast, simple way to perform common browser tasks such as capturing screenshots, extracting HTML, or generating PDFs without writing complex scripts. For more advanced automation, custom workflows, or persistent browser sessions, use <a href="/browser-run/puppeteer/">Puppeteer</a>, <a href="/browser-run/playwright/">Playwright</a>, or <a href="/browser-run/cdp/">CDP</a>.</p>
<h2 id="before-you-begin">Before you begin</h2>
<h3 id="rest-api">REST API</h3>
<p>To use Quick Actions via the REST API, <a href="/fundamentals/api/get-started/create-token/">create a custom API Token</a> with the following permissions:</p>
<ul>
<li><code>Browser Rendering - Edit</code></li>
</ul>
<h3 id="workers-binding">Workers binding</h3>
<p>To use Quick Actions from a <a href="/workers/">Worker</a>, configure a <a href="/browser-run/reference/wrangler/#bindings">browser binding</a> in your <code>wrangler.json</code>. No API token is needed when using the Workers binding.</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;  &quot;browser&quot;: {&#10;    &quot;binding&quot;: &quot;BROWSER&quot;&#10;  }&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3636.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3635.md")
</aside>
