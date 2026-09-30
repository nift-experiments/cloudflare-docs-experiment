<p>The Observatory overview dashboard provides a single view of your zone's performance over the past seven days. It combines synthetic monitoring, real user data, and Cloudflare's analysis to help you quickly identify performance bottlenecks and receive actionable recommendations.</p>
<h2 id="suggestions">Suggestions</h2>
<p>The <strong>Suggestions</strong> panel highlights tailored optimizations you can make to improve performance. Examples include:</p>
<ul>
<li>Reduce Largest Contentful Paint (LCP) with Polish.</li>
<li>Reduce Time to First Byte (TTFB) with Argo Smart Routing.</li>
</ul>
<p>These recommendations will vary based on your site's observed performance.</p>
<p>Selecting a suggestion expands it to show more detail:</p>
<ul>
<li><strong>Why you're seeing this</strong>: Explains the performance issue detected.</li>
<li><strong>What you can do</strong>: Lists recommended actions you can take.</li>
</ul>
<h2 id="core-web-vitals">Core Web Vitals</h2>
<p>The dashboard integrates <strong>Core Web Vitals</strong>, showing values at the 75th percentile (p75). These metrics reflect real user experiences:</p>
<ul>
<li><strong>Largest Contentful Paint (LCP)</strong>: How quickly the main content of a page becomes visible.</li>
<li><strong>Interaction to Next Paint (INP)</strong>: How responsive the site is to user interactions.</li>
<li><strong>Cumulative Layout Shift (CLS)</strong>: How visually stable the page layout is.</li>
</ul>
<p>If insufficient real user data is available, metrics may show as <strong>No data</strong>.</p>
<h2 id="network-performance">Network Performance</h2>
<p>The <strong>Network Performance</strong> section shows timing data that can help pinpoint where latency occurs.</p>
<ul>
<li>
<p><strong>Time to First Byte (TTFB)</strong>: Measures the time between the initial request and the first byte of the response.</p>
</li>
<li>
<p><strong>Time to Last Byte (TTLB) Breakdown</strong>: Provides a breakdown of response phases:</p>
<ul>
<li>DNS resolution time</li>
<li>TCP connection time</li>
<li>Request processing time at the server</li>
<li>Response transfer time</li>
</ul>
</li>
</ul>
<p>This breakdown helps identify whether delays are caused by DNS, connection setup, server processing, or response delivery.</p>
<h2 id="http-traffic">HTTP Traffic</h2>
<p>The <strong>HTTP Traffic</strong> section shows how traffic is handled between Cloudflare and your origin server:</p>
<ul>
<li><strong>Served by</strong>: Percentage of requests served from Cloudflare versus from your origin.</li>
<li><strong>4xx errors</strong>: Client errors, broken down by Cloudflare edge versus origin.</li>
<li><strong>5xx errors</strong>: Server errors, broken down by Cloudflare edge versus origin.</li>
</ul>
<p>This view helps distinguish between Cloudflare-side issues and origin-side issues.</p>
<h2 id="synthetic-monitoring">Synthetic Monitoring</h2>
<p>The <strong>Synthetic Monitoring</strong> table shows automated test results for your site. Each row includes:</p>
<ul>
<li><strong>URL tested</strong></li>
<li><strong>Last test run</strong></li>
<li><strong>Repeats</strong> (if scheduled multiple times)</li>
<li><strong>Score</strong> (Pass/Fail)</li>
</ul>
<p>Synthetic monitoring allows you to proactively test site availability and performance under consistent conditions, complementing real user monitoring (RUM).</p>
<h2 id="using-the-dashboard">Using the dashboard</h2>
<p>Use the Speed Overview dashboard to:</p>
<ul>
<li>Review <strong>Suggestions</strong> for actionable optimizations.</li>
<li>Track <strong>Core Web Vitals</strong> to ensure a good user experience.</li>
<li>Analyze <strong>Network Performance</strong> to identify latency bottlenecks.</li>
<li>Diagnose errors with <strong>HTTP Traffic</strong> insights.</li>
<li>Confirm site reliability using <strong>Synthetic Monitoring</strong> results.</li>
</ul>
