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
<pre><code class="language-jsonc">{&#10;  &quot;browser&quot;: {&#10;    &quot;binding&quot;: &quot;BROWSER&quot;&#10;  }&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3636.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3635.md")
</aside>
