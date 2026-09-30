---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/limits/
  description: Learn about the limits associated with Browser Run.
  full_title: Limits · Cloudflare Browser Run docs
  head_html: <title>Limits · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about the limits associated with Browser Run."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/limits/index.md"><meta property="og:title" content="Limits · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about the limits associated with Browser Run."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/limits/#page","headline":"Limits \u00b7 Cloudflare Browser Run docs","description":"Learn about the limits associated with Browser Run.","url":"https://developers.cloudflare.com/browser-run/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/limits/
  schema: 1
---
<p>Browser Run limits are based on your <a href="/workers/platform/pricing/">Cloudflare Workers plan</a>.</p>
<p>For pricing information, refer to <a href="/browser-run/pricing/">Browser Run pricing</a>.</p>
<h2 id="workers-free">Workers Free</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-higher-limits">Need higher limits?</h3>
@markup("md", "content/.markup/bodies/1410.md")
</aside>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Browser hours</td>
<td>10 minutes per day</td>
</tr>
<tr>
<td>Concurrent browsers per account (Browser Sessions only) <sup><a href="#footnote-1">1</a></sup></td>
<td>3 per account</td>
</tr>
<tr>
<td>New browser instances (Browser Sessions only)</td>
<td>1 every 20 seconds</td>
</tr>
<tr>
<td>Browser timeout</td>
<td>60 seconds <sup><a href="#footnote-2">2</a></sup></td>
</tr>
<tr>
<td>Total requests (Quick Actions only) <sup><a href="#footnote-3">3</a></sup></td>
<td>1 every 10 seconds</td>
</tr>
</tbody>
</table>
<h3 id="crawl-endpoint-limits"><code>/crawl</code> endpoint limits</h3>
<p>The <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code> endpoint</a> has additional limits for Workers Free plan users:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Crawl jobs per day</td>
<td>5 per day</td>
</tr>
<tr>
<td>Maximum pages per crawl</td>
<td>100 pages</td>
</tr>
</tbody>
</table>
<h2 id="workers-paid">Workers Paid</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-higher-limits-1">Need higher limits?</h3>
@markup("md", "content/.markup/bodies/1409.md")
</aside>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Browser hours</td>
<td>No limit (<a href="/browser-run/pricing/">See pricing</a>)</td>
</tr>
<tr>
<td>Concurrent browsers per account (Browser Sessions only) <sup><a href="#footnote-1">1</a></sup></td>
<td>200 per account (<a href="/browser-run/pricing/">See pricing</a>)</td>
</tr>
<tr>
<td>New browser instances per second (Browser Sessions only)</td>
<td>3 per second</td>
</tr>
<tr>
<td>Browser timeout</td>
<td>60 seconds <sup><a href="#footnote-2">2</a></sup></td>
</tr>
<tr>
<td>Total requests per second (Quick Actions only) <sup><a href="#footnote-3">3</a></sup></td>
<td>30 per second</td>
</tr>
</tbody>
</table>
<h2 id="faq">FAQ</h2>
<h3 id="how-can-i-manage-concurrency-and-session-isolation-with-browser-run">How can I manage concurrency and session isolation with Browser Run?</h3>
<p>If you are hitting concurrency <a href="/browser-run/limits/#workers-paid">limits</a>, or want to optimize concurrent browser usage, here are a few tips:</p>
<ul>
<li>Optimize with tabs or shared browsers: Instead of launching a new browser for each task, consider opening multiple tabs or running multiple actions within the same browser instance.</li>
<li><a href="/browser-run/features/reuse-sessions/">Reuse sessions</a>: You can optimize your setup and decrease startup time by reusing sessions instead of launching a new browser every time. If you are concerned about maintaining test isolation (for example, for tests that depend on a clean environment), we recommend using <a href="https://pptr.dev/api/puppeteer.browser.createbrowsercontext">incognito browser contexts</a>, which isolate cookies and cache with other sessions.</li>
</ul>
<p>If you are still running into concurrency limits you can <a href="https://forms.gle/CdueDKvb26mTaepa9">request a higher limit</a>.</p>
<h3 id="can-i-increase-the-browser-timeout">Can I increase the browser timeout?</h3>
<p>By default, a browser instance will time out after 60 seconds of inactivity. If you want to keep the browser open longer, you can use the <a href="/browser-run/puppeteer/#keep-alive"><code>keep_alive</code> option</a>, which allows you to extend the timeout to up to 10 minutes.</p>
<h3 id="is-there-a-maximum-session-duration">Is there a maximum session duration?</h3>
<p>There is no fixed maximum lifetime for a browser session as long as it remains active. By default, Browser Run closes sessions after one minute of inactivity to prevent unintended usage. You can <a href="/browser-run/puppeteer/#keep-alive">increase this inactivity timeout</a> to up to 10 minutes.</p>
<p>If you need sessions to remain open longer, keep them active by sending a command at least once within your configured inactivity window (for example, every 10 minutes). Sessions also close when Browser Run rolls out a new release.</p>
<h3 id="i-upgraded-from-the-workers-free-plan-but-i-m-still-hitting-the-10-minute-per-day-limit-what-should-i-do">I upgraded from the Workers Free plan, but I'm still hitting the 10-minute per day limit. What should I do?</h3>
<p>If you recently upgraded to the <a href="/workers/platform/pricing/">Workers Paid plan</a> but still encounter the 10-minute per day limit, redeploy your Worker to ensure your usage is correctly associated with the new plan.</p>
<h3 id="why-is-my-browser-usage-higher-than-expected">Why is my browser usage higher than expected?</h3>
<p>If you are hitting the daily limit or seeing higher usage than expected, the most common cause is browser sessions that are not being closed properly. When a browser session is not explicitly closed with <code>browser.close()</code>, it remains open and continues to consume browser time until it times out (60 seconds by default, or up to 10 minutes if you use the <code>keep_alive</code> option).</p>
<p>To minimize usage:</p>
<ul>
<li>Always call <code>browser.close()</code> when you are finished with a browser session.</li>
<li>Wrap your browser code in a <code>try/finally</code> block to ensure <code>browser.close()</code> is called even if an error occurs.</li>
<li>Use <a href="/browser-run/puppeteer/#list-recent-sessions"><code>puppeteer.history()</code></a> or <a href="/browser-run/playwright/#list-recent-sessions"><code>playwright.history()</code></a> to review recent sessions and identify any that closed due to <code>BrowserIdle</code> instead of <code>NormalClosure</code>. Sessions that close due to idle timeout indicate the browser was not closed explicitly.</li>
</ul>
<p>You can monitor your usage and view session close reasons in the Cloudflare dashboard on the <strong>Browser Run</strong> page:</p>
<div class="nb-dash-button"></div>
<p>Refer to <a href="/browser-run/reference/browser-close-reasons/">Browser close reasons</a> for more information.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="error-429-too-many-requests">Error: <code>429 Too many requests</code></h3>
<p>When you make too many requests in a short period of time, Browser Run will respond with HTTP status code <code>429 Too many requests</code>. You can view your account's rate limits in the <a href="#workers-free">Workers Free</a> and <a href="#workers-paid">Workers Paid</a> sections above.</p>
<p>The example below demonstrates how to handle rate limiting gracefully by reading the <code>Retry-After</code> value and retrying the request after that delay.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1413.md")
</div></div>
<h3 id="error-429-browser-time-limit-exceeded-for-today">Error: <code>429 Browser time limit exceeded for today</code></h3>
<p>This <code>Error processing the request: Unable to create new browser: code: 429: message: Browser time limit exceeded for today</code> error indicates you have hit the daily browser limit on the Workers Free plan. <a href="#workers-free">Workers Free plan accounts are limited</a> to 10 minutes of Browser Run usage per day. If you exceed that limit, you will receive a <code>429</code> error until the next UTC day.</p>
<p>You can <a href="#workers-paid">increase your limits</a> by upgrading to a Workers Paid plan on the <strong>Workers plans</strong> page of the Cloudflare dashboard:</p>
<div class="nb-dash-button"></div>
<p>If you recently upgraded but still encounter the 10-minute per day limit, redeploy your Worker to ensure your usage is correctly associated with the new plan.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Browsers close upon task completion or sixty seconds of inactivity (if you do not [extend your browser timeout](#can-i-increase-the-browser-timeout)). Therefore, in practice, many workflows do not require a high number of concurrent browsers.</li>
<li id="footnote-2">By default, a browser will time out after 60 seconds of inactivity. You can extend this to up to 10 minutes using the [`keep_alive` option](/browser-run/puppeteer/#keep-alive). Call `browser.close()` to release the browser instance immediately.</li>
<li id="footnote-3">If you exceed the per-second rate limit, you will receive a `429` response. Refer to [troubleshooting the `429 Too many requests` error](#error-429-too-many-requests).</li></ol></section>
