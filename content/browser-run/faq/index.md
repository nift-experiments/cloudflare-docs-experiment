---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/faq/
  description: Find answers to frequently asked questions about Browser Run, including errors, troubleshooting, and session management.
  full_title: Frequently asked questions about Cloudflare Browser Run · Cloudflare Browser Run docs
  head_html: <title>Frequently asked questions about Cloudflare Browser Run · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Find answers to frequently asked questions about Browser Run, including errors, troubleshooting, and session management."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/faq/index.md"><meta property="og:title" content="Frequently asked questions about Cloudflare Browser Run · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Find answers to frequently asked questions about Browser Run, including errors, troubleshooting, and session management."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/faq/#page","headline":"Frequently asked questions about Cloudflare Browser Run \u00b7 Cloudflare Browser Run docs","description":"Find answers to frequently asked questions about Browser Run, including errors, troubleshooting, and session management.","url":"https://developers.cloudflare.com/browser-run/faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/faq/
  schema: 1
---
<p>Below you will find answers to our most commonly asked questions about Browser Run (formerly Browser Rendering).</p>
<p>For pricing questions, visit the <a href="/browser-run/pricing/#pricing-faq">pricing FAQ</a>.
For usage limits questions, visit the <a href="/browser-run/limits/#faq">limits FAQ</a>.
If you cannot find the answer you are looking for, join us on <a href="https://discord.cloudflare.com">Discord</a>.</p>
<hr />
<h2 id="errors-troubleshooting">Errors &amp; Troubleshooting</h2>
<h3 id="error-cannot-read-properties-of-undefined-reading-fetch">Error: Cannot read properties of undefined (reading 'fetch')</h3>
<p>This error typically occurs because your Puppeteer launch is not receiving the browser binding. To resolve this error, pass your browser binding into <code>puppeteer.launch</code>.</p>
<h3 id="error-429-browser-time-limit-exceeded">Error: 429 browser time limit exceeded</h3>
<p>This error (<code>Unable to create new browser: code: 429: message: Browser time limit exceeded for today</code>) indicates you have hit the daily browser-instance limit on the Workers Free plan. <a href="/browser-run/limits/#workers-free">Workers Free plan accounts are capped at 10 minutes of browser use a day</a>. Once you exceed that limit, further creation attempts return a 429 error until the next UTC day.</p>
<p>To resolve this error, <a href="/workers/platform/pricing/">upgrade to a Workers Paid plan</a> which allows for more than 10 minutes of usage a day and has higher <a href="/browser-run/limits/#workers-paid">limits</a>. If you recently upgraded but still see this error, try redeploying your Worker to ensure your usage is correctly associated with your new plan.</p>
<h3 id="error-422-unprocessable-entity">Error: 422 unprocessable entity</h3>
<p>A <code>422 Unprocessable Entity</code> error usually means that Browser Run was not able to complete an action because of an issue with the site.</p>
<p>This can happen if:</p>
<ul>
<li>The website consumes too much memory during rendering.</li>
<li>The page itself crashed or returned an error before the action completed.</li>
<li>The request exceeded one of the <a href="/browser-run/reference/timeouts/">timeout limits</a> for page load, element load, or an action.</li>
</ul>
<p>Most often, this error is caused by a timeout. You can review the different timers and their limits in the <a href="/browser-run/reference/timeouts/">Quick Actions timeouts reference</a>.</p>
<h3 id="why-is-my-page-content-missing-or-incomplete">Why is my page content missing or incomplete?</h3>
<p>If your screenshots, PDFs, or scraped content are missing elements that appear when viewing the page in a browser, the page likely has not finished loading before Browser Run captures the output.</p>
<p>JavaScript-heavy pages and Single Page Applications (SPAs) often load content dynamically after the initial HTML is parsed. By default, Browser Run waits for <code>domcontentloaded</code>, which fires before JavaScript has finished rendering the page.</p>
<p>To fix this, use the <code>goToOptions.waitUntil</code> parameter with one of these values:</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Use when</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>networkidle0</code></td>
<td>The page must be completely idle (no network requests for 500 ms). Best for pages that load all content upfront.</td>
</tr>
<tr>
<td><code>networkidle2</code></td>
<td>The page can have up to 2 ongoing connections (like analytics or websockets). Best for most dynamic pages.</td>
</tr>
</tbody>
</table>
<p>Quick Actions example:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;url&quot;: &quot;https://example.com&quot;,&#10;	&quot;goToOptions&quot;: {&#10;		&quot;waitUntil&quot;: &quot;networkidle2&quot;&#10;	}&#10;}&#10;</code></pre>
<p>If content is still missing:</p>
<ul>
<li>Use <code>waitForSelector</code> to wait for a specific element to appear before capturing.</li>
<li>Increase <code>goToOptions.timeout</code> (up to 60 seconds) for slow-loading pages.</li>
<li>Check if the page requires authentication or returns different content to bots.</li>
</ul>
<p>For a complete reference, see <a href="/browser-run/reference/timeouts/">Quick Actions timeouts</a>.</p>
<hr />
<h2 id="getting-started-development">Getting started &amp; Development</h2>
<h3 id="why-run-browsers-in-the-cloud-instead-of-locally">Why run browsers in the cloud instead of locally?</h3>
<p>Running a browser locally works for development and small-scale tasks, but has practical limits for production workloads.</p>
<p>With Browser Run, browser sessions run on Cloudflare's infrastructure, so your automation runs without a local machine. There is no Chrome installation to maintain, no VM to keep running, and sessions launch on demand and shut down when done.</p>
<p>You can also use <a href="/queues/tutorials/web-crawler-with-browser-run/">Cloudflare Queues</a> to process batches of URLs asynchronously, allowing you to crawl at scale without managing queue infrastructure yourself.</p>
<p>Browser sessions open on Cloudflare's global network, close to the incoming request. Browser Run is a <a href="/browser-run/reference/wrangler/#bindings">Workers binding</a>, so it integrates directly with <a href="/browser-run/how-to/browser-run-with-do/">Durable Objects</a>, Queues, and the rest of the Cloudflare developer platform.</p>
<h3 id="does-local-development-support-all-browser-run-features">Does local development support all Browser Run features?</h3>
<p>Not yet. Local development currently has the following limitation(s):</p>
<ul>
<li>Requests larger than 1 MB are not supported.</li>
</ul>
<p>You can also run Chrome in visible (headful) mode during local development to visually debug your automation scripts (experimental). Set the <code>X_BROWSER_HEADFUL</code> environment variable before starting your dev server:</p>
<pre tabindex="0"><code class="language-sh">X_BROWSER_HEADFUL=true npx wrangler dev&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="use-real-headless-browser-during-local-development">Use real headless browser during local development</h3>
@markup("md", "content/.markup/bodies/1440.md")
</aside>
<h3 id="how-do-i-render-authenticated-pages-using-quick-actions">How do I render authenticated pages using Quick Actions?</h3>
<p>If the page you are rendering requires authentication, you can pass credentials using one of the following methods. These parameters work with all <a href="/browser-run/quick-actions/">Quick Actions</a> endpoints.</p>
<p>HTTP Basic Auth:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;authenticate&quot;: {&#10;		&quot;username&quot;: &quot;user&quot;,&#10;		&quot;password&quot;: &quot;pass&quot;&#10;	}&#10;}&#10;</code></pre>
<p>Cookie-based authentication:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;cookies&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;session_id&quot;,&#10;			&quot;value&quot;: &quot;abc123&quot;,&#10;			&quot;domain&quot;: &quot;example.com&quot;,&#10;			&quot;path&quot;: &quot;/&quot;,&#10;			&quot;secure&quot;: true,&#10;			&quot;httpOnly&quot;: true&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Token-based authentication:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;setExtraHTTPHeaders&quot;: {&#10;		&quot;Authorization&quot;: &quot;Bearer your-token&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For complete working examples of all three methods, refer to <a href="/browser-run/quick-actions/screenshot-endpoint/#capture-a-screenshot-of-an-authenticated-page">Capture a screenshot of an authenticated page</a>.</p>
<h3 id="will-browser-run-be-detected-by-bot-management">Will Browser Run be detected by Bot Management?</h3>
<p>Yes, Browser Run requests are always identified as bot traffic by Cloudflare. Cloudflare does not enforce bot protection by default — that is the customer's choice.</p>
<p>If you are attempting to scan your own zone and want Browser Run to access your website freely without your bot protection configuration interfering, you can create a WAF skip rule to <a href="/browser-run/faq/#can-i-allowlist-browser-run-on-my-own-website">allowlist Browser Run</a>.</p>
<h3 id="can-i-allowlist-browser-run-on-my-own-website">Can I allowlist Browser Run on my own website?</h3>
<p>You must be on an Enterprise plan to allowlist Browser Run on your own website because WAF custom rules require access to <a href="/bots/get-started/bot-management/">Bot Management</a> fields.</p>
<p>Browser Run uses different <a href="/browser-run/reference/automatic-request-headers/#bot-detection">bot detection IDs</a> depending on the method. Use the ID that matches the method you want to allowlist.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1441.md")
</div>
<h3 id="does-browser-run-rotate-ip-addresses-for-outbound-requests">Does Browser Run rotate IP addresses for outbound requests?</h3>
<p>No. Browser Run requests originate from Cloudflare's global network and you cannot configure per-request IP rotation. All rendering traffic comes from Cloudflare IP ranges and requests include <a href="/browser-run/reference/automatic-request-headers/">automatic headers</a>, such as <code>cf-biso-request-id</code> and <code>cf-biso-devtools</code> so origin servers can identify them.</p>
<h3 id="is-there-a-limit-to-how-many-requests-a-single-browser-session-can-handle">Is there a limit to how many requests a single browser session can handle?</h3>
<p>There is no fixed limit on the number of requests per browser session. A single browser can handle multiple requests as long as it stays within available compute and memory limits.</p>
<h3 id="can-i-use-custom-fonts-in-browser-run">Can I use custom fonts in Browser Run?</h3>
<p>Yes. If your webpage or PDF requires a font that is not pre-installed, you can load custom fonts at render time using <code>addStyleTag</code>. This works with <a href="/browser-run/quick-actions/">Quick Actions</a>, <a href="/browser-run/puppeteer/">Puppeteer</a>, and <a href="/browser-run/playwright/">Playwright</a>. For instructions and examples, refer to <a href="/browser-run/features/custom-fonts/">Custom fonts</a>.</p>
<h3 id="how-can-i-manage-concurrency-and-session-isolation-with-browser-run">How can I manage concurrency and session isolation with Browser Run?</h3>
<p>If you are hitting concurrency <a href="/browser-run/limits/#workers-paid">limits</a>, or want to optimize concurrent browser usage, here are a few tips:</p>
<ul>
<li>Optimize with tabs or shared browsers: Instead of launching a new browser for each task, consider opening multiple tabs or running multiple actions within the same browser instance.</li>
<li><a href="/browser-run/features/reuse-sessions/">Reuse sessions</a>: You can optimize your setup and decrease startup time by reusing sessions instead of launching a new browser every time. If you are concerned about maintaining test isolation (for example, for tests that depend on a clean environment), we recommend using <a href="https://pptr.dev/api/puppeteer.browser.createbrowsercontext">incognito browser contexts</a>, which isolate cookies and cache with other sessions.</li>
</ul>
<p>If you are still running into concurrency limits you can <a href="https://forms.gle/CdueDKvb26mTaepa9">request a higher limit</a>.</p>
<hr />
<h2 id="session-management">Session management</h2>
<h3 id="should-i-open-a-new-browser-for-every-task-or-reuse-a-session-and-open-tabs">Should I open a new browser for every task, or reuse a session and open tabs</h3>
<p>For most workloads, reuse an existing browser session and open a new tab instead of launching a fresh browser for each task. Browser Run counts browser instances against your <a href="/browser-run/limits/#workers-paid">concurrent browsers</a> and <a href="/browser-run/limits/#workers-paid">new browser instance rate</a> limits, but tabs inside an existing session do not count against either limit. Reusing a session also avoids the cold-start cost of launching a new browser.</p>
<p>A single browser can run many tabs, but all tabs share the same browser process and memory. Heavy pages (for example, pages with large JavaScript bundles, media, or complex DOMs) consume more memory per tab, so opening too many tabs in the same browser can cause it to crash. Test your workload to find a safe number of tabs per browser. For lightweight pages, tens of tabs may be fine. For heavy pages, only a few.</p>
<p>If you reuse a session but still need isolation between tasks, use an incognito browser context. Incognito contexts isolate cookies, local storage, and cache from each other and from the default context, so you can run separate tasks in tabs within the same browser without data leaking between them.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1444.md")
</div></div>
<p>Open a fresh browser only when you need full process-level isolation, a different browser configuration, or after a browser has become unstable. For automated screenshot, scrape, and crawl workloads, reusing sessions and tabs is usually the right choice. <a href="/browser-run/quick-actions/">Quick Actions</a> manage sessions and tabs automatically, so you do not need to handle reuse yourself.</p>
<hr />
<h2 id="security-data-handling">Security &amp; Data Handling</h2>
<h3 id="does-cloudflare-store-or-retain-the-html-content-i-submit-for-rendering">Does Cloudflare store or retain the HTML content I submit for rendering?</h3>
<p>For <a href="/browser-run/quick-actions/">Quick Actions</a> (except the <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code> endpoint</a>), <a href="/browser-run/puppeteer/">Puppeteer</a>, <a href="/browser-run/playwright/">Playwright</a>, and <a href="/browser-run/cdp/">CDP</a>, Cloudflare processes content ephemerally and does not retain customer-submitted HTML or generated output (such as PDFs or screenshots) beyond what is required to perform the rendering operation. Once the response is returned, the content is immediately discarded from the rendering environment.</p>
<p>There are two exceptions where data is retained beyond the session:</p>
<ul>
<li><strong>Crawl endpoint</strong>: The <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code> Quick Actions endpoint</a> runs jobs asynchronously, so job results (including crawled page content in HTML, Markdown, or JSON format) are stored for 14 days after the job completes, after which the data is deleted. Crawl jobs have a maximum run time of seven days.</li>
<li><strong>Session recording</strong>: Puppeteer, Playwright, and CDP sessions support an opt-in <a href="/browser-run/features/session-recording/">session recording</a> feature. When enabled, DOM changes, mouse and keyboard events, and page navigation are captured as structured JSON events and retained for 30 days. Input field content is masked by default. Recordings are accessible through the <a href="/browser-run/features/session-recording/#view-recordings">dashboard</a> and <a href="/browser-run/features/session-recording/#retrieve-a-recording-via-api">API</a>, and are automatically deleted after the retention period.</li>
</ul>
<h3 id="is-there-any-temporary-caching-of-submitted-content">Is there any temporary caching of submitted content?</h3>
<p>For <a href="/browser-run/quick-actions/">Quick Actions</a> (except the <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code> endpoint</a>), generated content is cached by default for five seconds (configurable up to one day via the <code>cacheTTL</code> parameter, or set to <code>0</code> to disable caching). This cache protects against repeated requests for the same URL by the same account. Customer-submitted HTML content itself is not cached.</p>
<p>For <a href="/browser-run/puppeteer/">Puppeteer</a>, <a href="/browser-run/playwright/">Playwright</a>, and <a href="/browser-run/cdp/">CDP</a>, no caching is used. Content exists only in memory for the duration of the rendering operation and is discarded immediately after the response is returned.</p>
<p>For the <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code> endpoint</a>, all crawl job results are stored in R2 for 14 days after completion.</p>
