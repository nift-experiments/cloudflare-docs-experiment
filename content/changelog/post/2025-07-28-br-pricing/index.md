<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 28, 2025</time><h2 id="post-title">Introducing pricing for the Browser Rendering API — $0.09 per browser hour</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>We’ve launched pricing for <a href="/browser-run/">Browser Rendering</a>, including a free tier and a pay-as-you-go model that scales with your needs. Starting <strong>August 20, 2025</strong>, Cloudflare will begin billing for Browser Rendering.</p>
<p>There are two ways to use Browser Rendering. Depending on the method you use, here’s how billing will work:</p>
<ul>
<li><a href="/browser-run/quick-actions/"><strong>REST API</strong></a>: Charged for <strong>Duration</strong> only ($/browser hour)</li>
<li><a href="/browser-run/#integration-methods"><strong>Browser Sessions</strong></a>: Charged for both <strong>Duration</strong> and <strong>Concurrency</strong> ($/browser hour and # of concurrent browsers)</li>
</ul>
<p>Included usage and pricing by plan</p>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Included duration</th>
<th>Included concurrency</th>
<th>Price (beyond included)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Workers Free</strong></td>
<td>10 minutes per day</td>
<td>3 concurrent browsers</td>
<td>N/A</td>
</tr>
<tr>
<td><strong>Workers Paid</strong></td>
<td>10 hours per month</td>
<td>10 concurrent browsers (averaged monthly)</td>
<td><strong>1. REST API</strong>: $0.09 per additional browser hour <br /><strong>2. Workers Bindings</strong>: $0.09 per additional browser hour <br /> $2.00 per additional concurrent browser</td>
</tr>
</tbody>
</table>
<p>What you need to know:</p>
<ul>
<li><strong>Workers Free Plan:</strong> 10 minutes of browser usage per day with 3 concurrent browsers at no charge.</li>
<li><strong>Workers Paid Plan:</strong> 10 hours of browser usage per month with 10 concurrent browsers (averaged monthly) at no charge. Additional usage is charged as shown above.</li>
</ul>
<p>You can monitor usage via the <a href="https://dash.cloudflare.com/?to=/:account/workers/browser-run">Cloudflare dashboard</a>. Go to <strong>Compute</strong> &gt; <strong>Browser Run</strong>.</p>
<p><img src="/assets/upstream/images/browser-run/dashboard.png" alt="Browser Rendering dashboard" /></p>
<p>If you've been using Browser Rendering and do not wish to incur charges, ensure your usage stays within your plan's <a href="/browser-run/pricing/">included usage</a>. To estimate costs, take a look at these <a href="/browser-run/pricing/#examples-of-workers-paid-pricing">example pricing scenarios</a>.</p>
</div></article></div>
