<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 31, 2026</time><h2 id="post-title">Browser Run adds a Playground to the Cloudflare dashboard</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Run</a> now includes a Playground in the Cloudflare dashboard. Use it to try Quick Actions against a live browser without creating a Worker, installing an SDK, or deploying code first.</p>
<p>The Playground helps you test a target URL or raw HTML input, tune viewport and page-load settings, preview the output, and copy working code for the same request.</p>
<p><img src="/images/browser-run/playground.png" alt="Browser Run Playground in the Cloudflare dashboard showing a generated screenshot preview and output settings" /></p>
<p>With the Playground, you can:</p>
<ul>
<li>Capture visuals as <a href="/browser-run/quick-actions/screenshot-endpoint/">screenshots</a> or <a href="/browser-run/quick-actions/pdf-endpoint/">PDFs</a>.</li>
<li>Generate multiple output formats in one request with the <a href="/browser-run/quick-actions/snapshot/">snapshot endpoint</a>.</li>
<li>Extract <a href="/browser-run/quick-actions/content-endpoint/">HTML</a>, <a href="/browser-run/quick-actions/markdown-endpoint/">Markdown</a>, <a href="/browser-run/quick-actions/links-endpoint/">links</a>, or <a href="/browser-run/quick-actions/scrape-endpoint/">scraped data</a>.</li>
<li>Extract <a href="/browser-run/quick-actions/json-endpoint/">structured data with AI</a> using a prompt and optional JSON Schema.</li>
</ul>
<p>You can also configure desktop, laptop, tablet, mobile, or custom viewport sizes, set browser scale, choose page-load conditions, set timeouts, and wait for selectors before running a request.</p>
<p>Select <strong>Show Code</strong> to generate the same request as cURL, TypeScript SDK, Python, or Workers Binding code. For example, a screenshot request can be copied as a Workers Binding call:</p>
<pre><code class="language-ts">interface Env {&#10;	BROWSER: BrowserRun;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env): Promise&lt;Response&gt; {&#10;		return await env.BROWSER.quickAction(&quot;screenshot&quot;, {&#10;			url: &quot;https://developers.cloudflare.com&quot;,&#10;			viewport: {&#10;				width: 1920,&#10;				height: 1080,&#10;			},&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Requests made in the Playground incur <a href="/browser-run/pricing/">Browser Run charges</a>. AI extraction also incurs Workers AI charges.</p>
<p>To try the Playground, go to <strong>Browser Run</strong> in the Cloudflare dashboard and select <strong>Playground</strong>.</p>
<div class="nb-dash-button"></div>
<p>For more information, refer to the <a href="/browser-run/quick-actions/">Quick Actions documentation</a>.</p>
</div></article></div>
