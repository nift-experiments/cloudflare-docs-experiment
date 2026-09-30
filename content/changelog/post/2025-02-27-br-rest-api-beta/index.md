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
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/screenshot&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;html&quot;: &quot;Hello World!&quot;,&#10;    &quot;screenshotOptions&quot;: {&#10;      &quot;type&quot;: &quot;webp&quot;,&#10;      &quot;omitBackground&quot;: true&#10;    }&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.webp&quot;&#10;</code></pre>
<p>Learn more in our <a href="/browser-run/quick-actions/">documentation</a>.</p>
</div></article></div>
