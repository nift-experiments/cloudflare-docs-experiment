---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/
  description: Control headless browsers with Cloudflare's Workers Browser Run API. Automate tasks, take screenshots, convert pages to PDFs, and test web apps.
  full_title: Browser Run · Cloudflare Browser Run docs
  head_html: <title>Browser Run · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Control headless browsers with Cloudflare&#x27;s Workers Browser Run API. Automate tasks, take screenshots, convert pages to PDFs, and test web apps."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/index.md"><meta property="og:title" content="Browser Run · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Control headless browsers with Cloudflare&#x27;s Workers Browser Run API. Automate tasks, take screenshots, convert pages to PDFs, and test web apps."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/browser-run/#page","headline":"Browser Run \u00b7 Cloudflare Browser Run docs","description":"Control headless browsers with Cloudflare's Workers Browser Run API. Automate tasks, take screenshots, convert pages to PDFs, and test web apps.","url":"https://developers.cloudflare.com/browser-run/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/1416.md")
</div>
<div class="nb-plan">
<p>Available on Free and Paid plans</p>
</div>
<p>Browser Run, formerly known as Browser Rendering, enables developers to programmatically control and interact with headless browser instances running on Cloudflare’s global network.</p>
<h2 id="use-cases">Use cases</h2>
<p>Programmatically load and fully render dynamic webpages or raw HTML and capture specific outputs such as:</p>
<ul>
<li><a href="/browser-run/quick-actions/markdown-endpoint/">Markdown</a></li>
<li><a href="/browser-run/quick-actions/screenshot-endpoint/">Screenshots</a></li>
<li><a href="/browser-run/quick-actions/pdf-endpoint/">PDFs</a></li>
<li><a href="/browser-run/quick-actions/snapshot/">Snapshots</a></li>
<li><a href="/browser-run/quick-actions/links-endpoint/">Links</a></li>
<li><a href="/browser-run/quick-actions/scrape-endpoint/">HTML elements</a></li>
<li><a href="/browser-run/quick-actions/json-endpoint/">Structured data</a></li>
<li><a href="/browser-run/quick-actions/crawl-endpoint/">Crawled web content</a></li>
</ul>
<h2 id="integration-methods">Integration methods</h2>
<p>Browser Run offers two categories of integration methods:</p>
<ul>
<li><strong><a href="/browser-run/quick-actions/">Quick Actions</a></strong>: Simple, stateless browser tasks like screenshots, PDFs, and scraping. No code deployment needed.</li>
<li><strong>Browser Sessions</strong>: Direct browser control via <a href="/browser-run/puppeteer/">Puppeteer</a>, <a href="/browser-run/playwright/">Playwright</a>, <a href="/browser-run/cdp/">CDP</a>, or <a href="/browser-run/stagehand/">Stagehand</a>. Deploy within Cloudflare Workers or connect from any environment via CDP.</li>
</ul>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Recommended</th>
<th>Why</th>
</tr>
</thead>
<tbody>
<tr>
<td>Simple screenshot, PDF, or scrape</td>
<td><a href="/browser-run/quick-actions/">Quick Actions</a></td>
<td>No code deployment; single HTTP request</td>
</tr>
<tr>
<td>Browser automation</td>
<td><a href="/browser-run/playwright/">Playwright</a>, <a href="/browser-run/puppeteer/">Puppeteer</a>, or <a href="/browser-run/cdp/">CDP</a></td>
<td>Full browser control with scripting</td>
</tr>
<tr>
<td>Porting existing scripts</td>
<td><a href="/browser-run/puppeteer/">Puppeteer</a>, <a href="/browser-run/playwright/">Playwright</a>, or <a href="/browser-run/cdp/">CDP</a></td>
<td>Minimal code changes from standard libraries</td>
</tr>
<tr>
<td>AI-powered data extraction</td>
<td><a href="/browser-run/quick-actions/json-endpoint/">JSON endpoint</a></td>
<td>Structured data via natural language prompts</td>
</tr>
<tr>
<td>Site-wide crawling</td>
<td><a href="/browser-run/quick-actions/crawl-endpoint/">Crawl endpoint</a></td>
<td>Multi-page content extraction with async results</td>
</tr>
<tr>
<td>AI agent browsing</td>
<td><a href="/browser-run/playwright/playwright-mcp/">Playwright MCP</a> or <a href="/browser-run/cdp/mcp-clients/">CDP with MCP clients</a></td>
<td>LLMs control browsers via MCP</td>
</tr>
<tr>
<td>Resilient scraping</td>
<td><a href="/browser-run/stagehand/">Stagehand</a></td>
<td>AI finds elements by intent, not selectors</td>
</tr>
<tr>
<td>Direct browser control from any environment</td>
<td><a href="/browser-run/cdp/">CDP</a></td>
<td>WebSocket access from local machines, CI/CD, or external servers</td>
</tr>
</tbody>
</table>
<h2 id="key-features">Key features</h2>
<ul>
<li><strong>Scale to thousands of browsers</strong>: Instant access to a global pool of browsers with low cold-start time, ideal for high-volume screenshot generation, data extraction, or automation at scale</li>
<li><strong>Global by default</strong>: Browser sessions run on Cloudflare's edge network, opening close to your users for better speed and availability worldwide</li>
<li><strong>Easy to integrate</strong>: <a href="/browser-run/quick-actions/">Quick Actions</a> for common tasks, <a href="/browser-run/puppeteer/">Puppeteer</a> and <a href="/browser-run/playwright/">Playwright</a> for complex workflows, and <a href="/browser-run/cdp/">CDP</a> for direct browser control from any environment</li>
<li><strong>Session management</strong>: <a href="/browser-run/features/reuse-sessions/">Reuse browser sessions</a> across requests to improve performance and reduce cold-start overhead</li>
<li><strong>Flexible pricing</strong>: Pay only for browser time used with generous free tier (<a href="/browser-run/pricing/">view pricing</a>)</li>
</ul>
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1417.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1418.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1419.md")
</div>
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/1426.md")
</div>
