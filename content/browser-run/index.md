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
