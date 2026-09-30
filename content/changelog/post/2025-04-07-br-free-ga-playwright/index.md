<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 7, 2025</time><h2 id="post-title">Browser Rendering REST API is Generally Available, with new endpoints and a free tier</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>We’re excited to announce Browser Rendering is now available on the <a href="https://www.cloudflare.com/plans/developer-platform/">Workers Free plan</a>, making it even easier to prototype and experiment with web search and headless browser use-cases when building applications on Workers.</p>
<p>The Browser Rendering <strong><a href="/browser-run/quick-actions/">REST API</a> is now Generally Available</strong>, allowing you to control browser instances from outside of Workers applications. We've added three new endpoints to help automate more browser tasks:</p>
<ul>
<li><strong>Extract structured data</strong> – Use <code>/json</code> to retrieve structured data from a webpage.</li>
<li><strong>Retrieve links</strong> – Use <code>/links</code> to pull all links from a webpage.</li>
<li><strong>Convert to Markdown</strong> – Use <code>/markdown</code> to convert webpage content into Markdown format.</li>
</ul>
<p>For example, to fetch the Markdown representation of a webpage:</p>
<pre><code class="language-bash">curl -X &#x27;POST&#x27; &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/markdown&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;&#10;  }&#x27;&#10;</code></pre>
<p>For the full list of endpoints, check out our <a href="/browser-run/quick-actions/">REST API documentation</a>. You can also interact with Browser Rendering via the <a href="https://github.com/cloudflare/cloudflare-typescript">Cloudflare TypeScript SDK</a>.</p>
<p>We also recently landed support for <a href="/browser-run/playwright/">Playwright</a> in Browser Rendering for browser automation from Cloudflare <a href="/workers/">Workers</a>, in addition to <a href="/browser-run/puppeteer/">Puppeteer</a>, giving you more flexibility to test across different browser environments.</p>
<p>Visit the <a href="/browser-run/">Browser Rendering docs</a> to learn more about how to use headless browsers in your applications.</p>
</div></article></div>
