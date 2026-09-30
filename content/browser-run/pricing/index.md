---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/pricing/
  description: Understand Browser Run pricing for Quick Actions and Browser Sessions, including browser hours and concurrent browser costs.
  full_title: Pricing · Cloudflare Browser Run docs
  head_html: <title>Pricing · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand Browser Run pricing for Quick Actions and Browser Sessions, including browser hours and concurrent browser costs."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/pricing/index.md"><meta property="og:title" content="Pricing · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand Browser Run pricing for Quick Actions and Browser Sessions, including browser hours and concurrent browser costs."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/pricing/#page","headline":"Pricing \u00b7 Cloudflare Browser Run docs","description":"Understand Browser Run pricing for Quick Actions and Browser Sessions, including browser hours and concurrent browser costs.","url":"https://developers.cloudflare.com/browser-run/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/pricing/
  schema: 1
---
<div class="nb-plan">
<p>Available on Free and Paid plans</p>
</div>
<p>Billing depends on how you use Browser Run:</p>
<ul>
<li><a href="/browser-run/quick-actions/"><strong>Quick Actions</strong></a>: Charged for browser hours only.</li>
<li><strong>Browser Sessions</strong> (<a href="/browser-run/puppeteer/">Puppeteer</a>, <a href="/browser-run/playwright/">Playwright</a>, <a href="/browser-run/cdp/">CDP</a>): Direct browser control, charged for both browser hours and concurrent browsers.</li>
</ul>
<p>Browser hours are shared across all methods.</p>
<table>
<thead>
<tr>
<th></th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Browser hours</td>
<td>10 minutes per day</td>
<td>10 hours per month, then $0.09 per additional hour</td>
</tr>
<tr>
<td>Concurrent browsers (Browser Sessions only)</td>
<td>3 browsers</td>
<td>10 browsers (<a href="#how-is-the-number-of-concurrent-browsers-calculated">averaged monthly</a>), then $2.00 per additional browser</td>
</tr>
</tbody>
</table>
<p>To view or change your plan, go to the <strong>Workers plans</strong> page in the Cloudflare dashboard:</p>
<div class="nb-dash-button"></div>
<h2 id="examples-of-workers-paid-pricing">Examples of Workers Paid pricing</h2>
<h4 id="example-quick-actions-pricing">Example: Quick Actions pricing</h4>
<p>If a Workers Paid user uses Quick Actions for 50 hours during the month, the estimated cost for the month is as follows.</p>
<p>For browser hours:</p>
<br />
50 hours - 10 hours (included in plan) = 40 hours
<br />
40 hours × $0.09 per hour = $3.60
<h4 id="example-browser-sessions-pricing">Example: Browser Sessions pricing</h4>
<p>If a Workers Paid plan user uses Browser Sessions (Puppeteer, Playwright, or CDP) for 50 hours during the month, and uses 10 concurrent browsers for the first 15 days and 20 concurrent browsers the last 15 days, the estimated cost for the month is as follows.</p>
<p>For browser hours:</p>
<br />
50 hours - 10 hours (included in plan) = 40 hours
<br />
40 hours × $0.09 per hour = $3.60
<p>For concurrent browsers:</p>
<br />
((10 browsers × 15 days) + (20 browsers × 15 days)) = 450 total browsers used in
month
<br />
450 browsers used in month ÷ 30 days in month = 15 browsers (averaged monthly)
<br />
15 browsers (averaged monthly) − 10 (included in plan) = 5 browsers
<br />5 browsers × $2.00 per browser = $10.00
<p>For browser hours and concurrent browsers:</p>
<br />
$3.60 + $10.00 = $13.60
<h2 id="pricing-faq">Pricing FAQ</h2>
<h3 id="how-do-i-estimate-my-browser-run-costs">How do I estimate my Browser Run costs?</h3>
<p>You can monitor Browser Run usage in two ways:</p>
<ul>
<li>To monitor your Browser Run usage in the Cloudflare dashboard, go to the <strong>Browser Run</strong> page.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li>The <code>X-Browser-Ms-Used</code> header, which is returned in every Quick Actions response, reports browser time used for the request (in milliseconds). You can also access this header using the Typescript SDK with the .asResponse() method:</li>
</ul>
<pre tabindex="0"><code class="language-ts">const contentRes = await client.browserRendering.content&#10;	.create({&#10;		account_id: &quot;account_id&quot;,&#10;	})&#10;	.asResponse();&#10;&#10;const browserMsUsed = parseInt(&#10;	contentRes.headers.get(&quot;X-Browser-Ms-Used&quot;) || &quot;&quot;,&#10;);&#10;</code></pre>
<p>You can then use the tables above to estimate your costs based on your usage.</p>
<h3 id="do-failed-api-calls-such-as-those-that-time-out-add-to-billable-browser-hours">Do failed API calls, such as those that time out, add to billable browser hours?</h3>
<p>No. If a Quick Actions request fails with a <code>waitForTimeout</code> error, the browser session is not charged.</p>
<h3 id="how-is-the-number-of-concurrent-browsers-calculated">How is the number of concurrent browsers calculated?</h3>
<p>Cloudflare calculates concurrent browsers as the monthly average of your daily peak usage. In other words, we record the peak number of concurrent browsers each day and then average those values over the month. This approach reflects your typical traffic and ensures you are not disproportionately charged for brief spikes in browser concurrency.</p>
<h3 id="how-is-billing-time-calculated">How is billing time calculated?</h3>
<p>At the end of each day, Cloudflare totals all of your browser usage for that day in seconds. At the end of each billing cycle, we add up all of the daily totals to find the monthly total of browser hours, rounded to the nearest whole hour. In other words, 1,800 seconds (30 minutes) or more is rounded up to the nearest hour, and 1,799 seconds or less is rounded down to the nearest whole hour.</p>
<p>For example, if you only use one minute of browser time in a day, that day counts as one minute. If you do that every day for a 30-day month, your total would be 30 minutes. For billing, we round that up to one browser hour.</p>
