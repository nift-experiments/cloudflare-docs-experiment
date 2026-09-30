---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/kitesurf/
  description: Use Kitesurf, Cloudflare's stateless, agent-first browser that runs entirely on Workers, with Browser Run for screenshots, HTML extraction, and automation.
  full_title: Kitesurf · Cloudflare Browser Run docs
  head_html: <title>Kitesurf · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Kitesurf, Cloudflare&#x27;s stateless, agent-first browser that runs entirely on Workers, with Browser Run for screenshots, HTML extraction, and automation."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/kitesurf/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/kitesurf/index.md"><meta property="og:title" content="Kitesurf · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Kitesurf, Cloudflare&#x27;s stateless, agent-first browser that runs entirely on Workers, with Browser Run for screenshots, HTML extraction, and automation."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/kitesurf/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/kitesurf/#page","headline":"Kitesurf \u00b7 Cloudflare Browser Run docs","description":"Use Kitesurf, Cloudflare's stateless, agent-first browser that runs entirely on Workers, with Browser Run for screenshots, HTML extraction, and automation.","url":"https://developers.cloudflare.com/browser-run/kitesurf/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/kitesurf/
  schema: 1
---
<p><a href="https://blog.cloudflare.com/kitesurf">Kitesurf</a> is Cloudflare's stateless, highly scalable browser that runs entirely on top of <a href="/workers/">Workers</a> and is designed for AI agents. Instead of shipping a full desktop browser engine like Chromium, Kitesurf focuses on what matters to an agent — token count, context windows, scalability, performance, and cost — while trading away features that only humans need, such as tabs, themes, extensions, and pixel-perfect rendering.</p>
<p>For common agentic tasks like screenshots and HTML extraction, Kitesurf uses significantly less CPU and memory than Chromium, which means you can run more sessions and scale better for bursty, AI-driven workloads.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="pricing">Pricing</h3>
@markup("md", "content/.markup/bodies/1415.md")
</aside>
<h2 id="when-to-use-kitesurf">When to use Kitesurf</h2>
<p>Kitesurf is a good fit for:</p>
<ul>
<li>AI agents that need to render pages but can accept the trade-offs of not using a full-featured, pixel-perfect Chromium browser.</li>
<li>Automations and applications that rely on one-shot <a href="/browser-run/quick-actions/">Quick Actions</a>, such as extracting content from a page or generating PDFs and screenshots for compatible sites.</li>
<li>Bursty, AI-driven workloads that benefit from an ephemeral, fully-isolated, stateless engine designed to exist only for the duration of a task.</li>
</ul>
<p>Kitesurf correctly renders pages such as <a href="https://todomvc.com/">TodoMVC</a> (vanilla, React, Vue, Angular, Preact), Wikipedia, Hacker News, the Cloudflare Blog, and much of the Cloudflare dashboard.</p>
<h3 id="what-kitesurf-cannot-do-yet">What Kitesurf cannot do yet</h3>
<p>Kitesurf is not yet the right option if you need to:</p>
<ul>
<li>Play video or render WebGL.</li>
<li>Negotiate a bot-challenge handshake with real TLS fingerprints.</li>
<li>Start a long-running, authenticated session that requires persistent state.</li>
</ul>
<p>For these cases, use Browser Run's default browser, which is powered by Chromium.</p>
<p>The best way to know whether a specific site is compatible with Kitesurf is to try it — either through the <a href="/browser-run/cdp/">CDP endpoint</a> and <a href="/browser-run/quick-actions/">Quick Actions</a> or in the <a href="https://kitesurf.cloudflare.app/">public playground</a>.</p>
<h2 id="how-to-use-kitesurf">How to use Kitesurf</h2>
<h3 id="use-kitesurf-with-quick-actions">Use Kitesurf with Quick Actions</h3>
<p>You can also use Kitesurf with Browser Run's <a href="/browser-run/quick-actions/">Quick Actions</a>. Add <code>browser=kitesurf</code> to any Quick Action endpoint.</p>
<p>For example, to take a screenshot with Kitesurf:</p>
<pre tabindex="0"><code class="language-sh">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-run/screenshot?browser=kitesurf&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.png&quot;&#10;</code></pre>
<h3 id="use-kitesurf-with-the-cdp-endpoint">Use Kitesurf with the CDP endpoint</h3>
<p>The <a href="/browser-run/cdp/">Browser Run CDP endpoint</a> supports Kitesurf as an option, so your existing <a href="/browser-run/puppeteer/">Puppeteer</a>, <a href="/browser-run/playwright/">Playwright</a>, or <a href="https://www.npmjs.com/package/chrome-remote-interface">chrome-remote-interface</a> setup already works. To opt in, add <code>browser=kitesurf</code> to the endpoint URL:</p>
<pre tabindex="0"><code class="language-txt">wss://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-run/devtools/browser?browser=kitesurf&#10;</code></pre>
<h3 id="use-kitesurf-from-an-mcp-client">Use Kitesurf from an MCP client</h3>
<p>Any AI agent that speaks MCP and CDP can use Kitesurf. Add the following to your <a href="/browser-run/cdp/mcp-clients/">MCP client</a> configuration:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;mcp&quot;: {&#10;		&quot;kitesurf&quot;: {&#10;			&quot;type&quot;: &quot;local&quot;,&#10;			&quot;command&quot;: [&#10;				&quot;npx&quot;,&#10;				&quot;-y&quot;,&#10;				&quot;chrome-devtools-mcp@latest&quot;,&#10;				&quot;--wsEndpoint=wss://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-run/devtools/browser?browser=kitesurf&quot;,&#10;				&quot;--wsHeaders={\&quot;Authorization\&quot;:\&quot;Bearer &lt;API_TOKEN&gt;\&quot;}&quot;&#10;			],&#10;			&quot;enabled&quot;: true&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Replace <code>&lt;ACCOUNT_ID&gt;</code> with your Cloudflare account ID and <code>&lt;API_TOKEN&gt;</code> with a Browser Run API token.</p>
<h3 id="try-the-kitesurf-playground">Try the Kitesurf playground</h3>
<p>To start exploring Kitesurf without writing any code, use the <a href="https://kitesurf.cloudflare.app/">public playground</a>. Type in any URL to see how Kitesurf renders the page and interact with it.</p>
<p>The playground injects Chrome DevTools into the UI, so you can inspect expanded DOM elements, read console messages, and watch network activity while Kitesurf renders a page. The <a href="https://developer.chrome.com/docs/devtools/memory">Memory panel</a> reports the WebAssembly footprint of each isolate, including frames, so you can see the resources each page consumes.</p>
<h2 id="standards-compliance">Standards compliance</h2>
<p>Kitesurf is tested against the <a href="https://github.com/web-platform-tests/wpt">Web Platform Tests (WPT)</a>, the shared suite used to measure conformance to <a href="https://www.w3.org/">W3C</a> standards. As of the latest run, Kitesurf passes over <strong>235,000 subtests</strong>, and coverage is expanding quickly.</p>
<p>The parts of a browser that matter most to agents have strong coverage:</p>
<table>
<thead>
<tr>
<th>Area</th>
<th>Subtest coverage</th>
</tr>
</thead>
<tbody>
<tr>
<td>DOM</td>
<td>97%</td>
</tr>
<tr>
<td>HTML</td>
<td>96%</td>
</tr>
<tr>
<td>Selection</td>
<td>99%</td>
</tr>
<tr>
<td>SVG</td>
<td>97%</td>
</tr>
<tr>
<td>Encoding</td>
<td>99%</td>
</tr>
<tr>
<td>CORS</td>
<td>95%</td>
</tr>
<tr>
<td>XHR</td>
<td>95%</td>
</tr>
<tr>
<td>URL</td>
<td>83%</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1414.md")
</aside>
<h2 id="how-kitesurf-compares-to-chromium">How Kitesurf compares to Chromium</h2>
<p>Kitesurf is designed to be lightweight and efficient. It uses less CPU and memory than Chromium for common agentic tasks, at the cost of slightly slower wall time and rendering that is not pixel-perfect.</p>
<p>The table below shows the medians of five Browser Run <a href="/browser-run/quick-actions/">Quick Action</a> runs across a <a href="https://kitesurf.cloudflare.app/corpus.txt">14-URL corpus</a>, comparing Chromium (warm pool) with Kitesurf:</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Kitesurf</th>
<th>Chromium (warm pool)</th>
<th>Kitesurf, relative</th>
</tr>
</thead>
<tbody>
<tr>
<td>CPU: screenshot</td>
<td>380 ms</td>
<td>1,173 ms</td>
<td>3.1× less CPU than Chromium</td>
</tr>
<tr>
<td>CPU: HTML extraction</td>
<td>229 ms</td>
<td>877 ms</td>
<td>3.8× less than Chromium</td>
</tr>
<tr>
<td>Memory: screenshot</td>
<td>57.8 MiB</td>
<td>271.0 MiB</td>
<td>4.7× less than Chromium</td>
</tr>
<tr>
<td>Memory: HTML extraction</td>
<td>39.4 MiB</td>
<td>273.7 MiB</td>
<td>7.0× less than Chromium</td>
</tr>
<tr>
<td>Wall time: screenshot</td>
<td>1,148 ms</td>
<td>637 ms</td>
<td>1.8× slower than Chromium</td>
</tr>
<tr>
<td>Wall time: HTML extraction</td>
<td>820 ms</td>
<td>472 ms</td>
<td>1.7× slower than Chromium</td>
</tr>
</tbody>
</table>
<p>Kitesurf wins on the memory and CPU that drive your bill (by 3–7×), while Chromium wins wall time because a warm just-in-time compiler beats a cold software renderer.</p>
