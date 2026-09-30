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
<pre><code class="language-ts">const contentRes = await client.browserRendering.content&#10;	.create({&#10;		account_id: &quot;account_id&quot;,&#10;	})&#10;	.asResponse();&#10;&#10;const browserMsUsed = parseInt(&#10;	contentRes.headers.get(&quot;X-Browser-Ms-Used&quot;) || &quot;&quot;,&#10;);&#10;</code></pre>
<p>You can then use the tables above to estimate your costs based on your usage.</p>
<h3 id="do-failed-api-calls-such-as-those-that-time-out-add-to-billable-browser-hours">Do failed API calls, such as those that time out, add to billable browser hours?</h3>
<p>No. If a Quick Actions request fails with a <code>waitForTimeout</code> error, the browser session is not charged.</p>
<h3 id="how-is-the-number-of-concurrent-browsers-calculated">How is the number of concurrent browsers calculated?</h3>
<p>Cloudflare calculates concurrent browsers as the monthly average of your daily peak usage. In other words, we record the peak number of concurrent browsers each day and then average those values over the month. This approach reflects your typical traffic and ensures you are not disproportionately charged for brief spikes in browser concurrency.</p>
<h3 id="how-is-billing-time-calculated">How is billing time calculated?</h3>
<p>At the end of each day, Cloudflare totals all of your browser usage for that day in seconds. At the end of each billing cycle, we add up all of the daily totals to find the monthly total of browser hours, rounded to the nearest whole hour. In other words, 1,800 seconds (30 minutes) or more is rounded up to the nearest hour, and 1,799 seconds or less is rounded down to the nearest whole hour.</p>
<p>For example, if you only use one minute of browser time in a day, that day counts as one minute. If you do that every day for a 30-day month, your total would be 30 minutes. For billing, we round that up to one browser hour.</p>
