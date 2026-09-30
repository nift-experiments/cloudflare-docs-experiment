---
cp9:
  canonical: https://developers.cloudflare.com/speed/troubleshooting/slow-website/
  description: Identify and resolve performance issues affecting your website.
  full_title: Troubleshooting a slow website · Cloudflare Speed docs
  head_html: <title>Troubleshooting a slow website · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Identify and resolve performance issues affecting your website."><link rel="canonical" href="https://developers.cloudflare.com/speed/troubleshooting/slow-website/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/troubleshooting/slow-website/index.md"><meta property="og:title" content="Troubleshooting a slow website · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Identify and resolve performance issues affecting your website."><meta property="og:url" content="https://developers.cloudflare.com/speed/troubleshooting/slow-website/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Speed"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/speed/troubleshooting/slow-website/#page","headline":"Troubleshooting a slow website \u00b7 Cloudflare Speed docs","description":"Identify and resolve performance issues affecting your website.","url":"https://developers.cloudflare.com/speed/troubleshooting/slow-website/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /speed/troubleshooting/slow-website/
  schema: 1
---
<p>This guide helps you identify and resolve performance issues affecting your website. It starts with basic diagnostics and progresses to advanced troubleshooting techniques.</p>
<h2 id="before-you-start-verify-traffic-goes-through-cloudflare">Before you start: Verify traffic goes through Cloudflare</h2>
<p>Before troubleshooting performance, confirm that your traffic is actually going through Cloudflare. If requests bypass Cloudflare, the issue is not related to Cloudflare and this guide will not help.</p>
<h3 id="check-for-the-cf-ray-header">Check for the cf-ray header</h3>
<p>Every response served through Cloudflare includes a <code>cf-ray</code> header. Check for this header:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13885.md")
</div></div>
<p>If you see a <code>cf-ray</code> header (for example, <code>cf-ray: 8a1b2c3d4e5f6g7h-SJC</code>), your traffic is going through Cloudflare. If not, check your DNS configuration.</p>
<h3 id="verify-dns-is-pointing-to-cloudflare">Verify DNS is pointing to Cloudflare</h3>
<p>Your domain must resolve to Cloudflare IP addresses for traffic to be proxied:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13888.md")
</div></div>
<p>The returned IP addresses should be <a href="https://www.cloudflare.com/ips/">Cloudflare IPs</a>. If they point directly to your origin server, your DNS records are not proxied.</p>
<p>To fix this:</p>
<ol>
<li>Go to the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns">Cloudflare dashboard</a>.</li>
<li>Find the DNS record for the slow hostname.</li>
<li>Ensure the <strong>Proxy status</strong> is set to <strong>Proxied</strong> (orange cloud icon).</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13882.md")
</aside>
<hr />
<h2 id="gather-information-about-the-slow-requests">Gather information about the slow requests</h2>
<p>Performance issues are easier to solve when you can pinpoint exactly what is slow. Start by gathering the following information:</p>
<ol>
<li><strong>Identify specific slow requests</strong> - Determine which URLs, assets, or API endpoints are slow.</li>
<li><strong>Measure the slowness</strong> - Quantify the delay (for example, &quot;this image takes 5 seconds to load&quot;).</li>
<li><strong>Reproduce the issue</strong> - Confirm the slowness is consistent and not a one-time occurrence.</li>
</ol>
<hr />
<h2 id="step-1-use-observatory-to-analyze-performance">Step 1: Use Observatory to analyze performance</h2>
<p><a href="/speed/observatory/">Observatory</a> provides synthetic tests and real user monitoring (RUM) data to assess your website's performance.</p>
<p>RUM is particularly important as these metrics are captured from your actual visitors' browsers so it's an objective view of how they are experiencing your website, rather than lab data, which is typically more detailed (useful for debugging) but doesn't always correlate with the devices or connectivity real people have access to.</p>
<h3 id="run-a-speed-test">Run a speed test</h3>
<ol>
<li>Go to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Observatory**.
3. Enter the URL you want to test and select **Run test**.
<h3 id="understand-the-results">Understand the results</h3>
<p>Observatory reports key metrics:</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>What it measures</th>
<th>Target</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Largest Contentful Paint (LCP)</strong></td>
<td>Time until the largest visible element loads</td>
<td>Under 2.5 seconds</td>
</tr>
<tr>
<td><strong>First Contentful Paint (FCP)</strong></td>
<td>Time until the first content appears</td>
<td>Under 1.8 seconds</td>
</tr>
<tr>
<td><strong>Cumulative Layout Shift (CLS)</strong></td>
<td>Visual stability during page load</td>
<td>Under 0.1</td>
</tr>
<tr>
<td><strong>Time to First Byte (TTFB)</strong></td>
<td>Time until the first byte of response is received</td>
<td>Under 800 ms</td>
</tr>
<tr>
<td><strong>Total Blocking Time (TBT)</strong></td>
<td>Time the main thread is blocked</td>
<td>Under 200 ms</td>
</tr>
</tbody>
</table>
<p>Real User Monitoring reports similar metrics but you'll see Interaction to Next Paint (INP) in place of Total Blocking Time (TBT).</p>
<p>TBT only measures during page load but INP measures every interaction real visitors make with your website.</p>
<h3 id="enable-recommended-optimizations">Enable recommended optimizations</h3>
<p>Based on Observatory results, enable relevant <a href="/speed/optimization/">Speed optimizations</a>:</p>
<ul>
<li><a href="/speed/optimization/content/compression/">Brotli compression</a> - Compress responses for faster transfer</li>
<li><a href="/cache/advanced-configuration/early-hints/">Early Hints</a> - Preload critical resources</li>
<li><a href="/speed/optimization/protocol/">HTTP/2 and HTTP/3</a> - Use modern protocols with multiplexing, allowing multiple requests over a single connection instead of opening separate connections for each asset</li>
<li><a href="/images/">Image optimization</a> - Automatically optimize and resize images</li>
<li><a href="/speed/optimization/content/rocket-loader/">Rocket Loader</a> - Defer loading of JavaScript to improve paint times</li>
</ul>
<hr />
<h2 id="step-2-identify-slow-resources">Step 2: Identify slow resources</h2>
<p>If Observatory and RUM data point to specific issues, use browser developer tools to investigate individual resources.</p>
<h3 id="use-browser-developer-tools">Use browser developer tools</h3>
<ol>
<li>Open your browser's developer tools.</li>
<li>Go to the <strong>Network</strong> tab.</li>
<li>Reload the page and observe which requests take the longest.</li>
<li>Sort by <strong>Time</strong> or <strong>Duration</strong> to identify the slowest assets.</li>
<li>Note the specific URLs of slow resources.</li>
</ol>
<p>Look for:</p>
<ul>
<li>Large images or videos</li>
<li>Slow API calls</li>
<li>Third-party scripts</li>
<li>Render-blocking resources</li>
</ul>
<hr />
<h2 id="step-3-analyze-origin-performance">Step 3: Analyze origin performance</h2>
<p>If your website is slow, the issue may be at your origin server. Use Origin Analytics to understand how your origin is performing.</p>
<h3 id="check-origin-response-times">Check origin response times</h3>
<p>In the Cloudflare dashboard:</p>
<ol>
<li>Go to <strong>Speed</strong> &gt; <strong>Origin Analytics</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
2. Review the **Origin Response Time** metrics.
3. Look for patterns in slow responses (specific paths, times of day, or geographic regions).
<p>High origin response times indicate your origin server is struggling. Consider:</p>
<ul>
<li>Upgrading your hosting plan</li>
<li>Optimizing database queries</li>
<li>Implementing server-side caching</li>
</ul>
<p>For a full guide on available metrics, diagnostic flows, and how to interpret origin status codes, refer to <a href="/speed/origin-analytics/">Origin Analytics</a>.</p>
<h3 id="check-for-slow-workers">Check for slow Workers</h3>
<p>If your zone has <a href="/workers/">Cloudflare Workers</a> deployed, they execute on every matching request and add to the total response time. A slow Worker is a common cause of high TTFB.</p>
<p>To check if Workers are affecting performance:</p>
<ol>
<li>Go to <strong>Workers &amp; Pages</strong> in the Cloudflare dashboard.</li>
<li>Review which Workers are deployed on your zone.</li>
<li>Check the <strong>Analytics</strong> for each Worker to see execution times.</li>
<li>Temporarily disable Workers to isolate whether they are causing the slowness.</li>
</ol>
<p>If a Worker is slow, review its code for:</p>
<ul>
<li>Slow external API calls or <code>fetch()</code> requests</li>
<li>Inefficient loops or data processing</li>
<li>Missing <code>await</code> statements causing sequential instead of parallel execution</li>
</ul>
<hr />
<h2 id="step-4-measure-performance-from-the-command-line">Step 4: Measure performance from the command line</h2>
<p>For detailed timing metrics on specific requests, use command-line tools to measure performance.</p>
<h3 id="basic-performance-test">Basic performance test</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13891.md")
</div></div>
<p>Example output (bash):</p>
<pre tabindex="0"><code class="language-txt">DNS Lookup: 0.025s&#10;TCP Connect: 0.045s&#10;TLS Handshake: 0.120s&#10;Time to First Byte: 0.350s&#10;Total Time: 1.250s&#10;</code></pre>
<h3 id="understand-the-metrics">Understand the metrics</h3>
<p>The curl timing breakdown shows the following:</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Description</th>
<th>High value indicates</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>DNS Lookup</strong></td>
<td>Time to resolve the domain name</td>
<td>DNS issues or slow resolver</td>
</tr>
<tr>
<td><strong>TCP Connect</strong></td>
<td>Time to establish TCP connection</td>
<td>Network latency or server distance</td>
</tr>
<tr>
<td><strong>TLS Handshake</strong></td>
<td>Time to complete SSL/TLS negotiation</td>
<td>Certificate chain issues or slow server</td>
</tr>
<tr>
<td><strong>Time to First Byte (TTFB)</strong></td>
<td>Time until first response byte</td>
<td>Slow origin processing</td>
</tr>
<tr>
<td><strong>Total Time</strong></td>
<td>Complete request duration</td>
<td>Large file size or slow transfer</td>
</tr>
</tbody>
</table>
<h3 id="test-from-different-locations">Test from different locations</h3>
<p>To test from different geographic locations, use online tools like:</p>
<ul>
<li><a href="https://tools.keycdn.com/performance">KeyCDN Tools</a></li>
<li><a href="https://www.uptrends.com/tools/website-speed-test">Uptrends</a></li>
<li><a href="https://www.dotcom-tools.com/website-speed-test">Dotcom-Tools</a></li>
</ul>
<hr />
<h2 id="step-5-investigate-caching">Step 5: Investigate caching</h2>
<p>Caching is one of the most effective ways to improve website performance. When content is cached, Cloudflare serves it directly from a data center close to your visitors, eliminating the round trip to your origin server. This can reduce response times from hundreds of milliseconds to just a few milliseconds.</p>
<p>Uncached content must travel from the visitor to Cloudflare, then to your origin server, and back again. Use <a href="/cache/performance-review/cache-analytics/">Cache Analytics</a> to understand your cache performance and identify opportunities to cache more content.</p>
<h3 id="check-if-assets-are-cached">Check if assets are cached</h3>
<p>Check the cache status of a specific asset:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13894.md")
</div></div>
<p>Possible values:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Meaning</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>HIT</strong></td>
<td>Served from Cloudflare cache</td>
<td>No action needed</td>
</tr>
<tr>
<td><strong>MISS</strong></td>
<td>Not in cache, fetched from origin</td>
<td>May need cache rules</td>
</tr>
<tr>
<td><strong>DYNAMIC</strong></td>
<td>Not eligible for caching</td>
<td>Create a cache rule if static</td>
</tr>
<tr>
<td><strong>BYPASS</strong></td>
<td>Cache intentionally bypassed</td>
<td>Review cache rules</td>
</tr>
<tr>
<td><strong>EXPIRED</strong></td>
<td>Cached copy was stale</td>
<td>Increase Edge TTL</td>
</tr>
<tr>
<td><strong>REVALIDATED</strong></td>
<td>Cloudflare confirmed content is current</td>
<td>Increase Edge TTL</td>
</tr>
</tbody>
</table>
<p>For a complete list, refer to <a href="/cache/concepts/cache-responses/">Cloudflare cache responses</a>.</p>
<h3 id="use-cache-analytics">Use Cache Analytics</h3>
<ol>
<li>Go to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
2. Review the **Cache Performance** section.
3. Filter by **Cache status equals MISS** or **DYNAMIC** to identify uncached content.
<h3 id="investigate-why-static-content-is-not-cached">Investigate why static content is not cached</h3>
<p>If static assets (images, CSS, JavaScript) show a cache status of <code>DYNAMIC</code>, <code>BYPASS</code>, or <code>MISS</code>, investigate the cause:</p>
<table>
<thead>
<tr>
<th>Symptom</th>
<th>Likely cause</th>
<th>Solution</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>DYNAMIC</code> status</td>
<td>Content type not in <a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">default file extensions</a></td>
<td>Create a Cache Rule to cache the content</td>
</tr>
<tr>
<td><code>DYNAMIC</code> status</td>
<td>Origin sends <code>Cache-Control: private</code> or <code>no-store</code></td>
<td>Create a Cache Rule to <a href="/cache/how-to/cache-rules/settings/#origin-cache-control">override origin cache control</a></td>
</tr>
<tr>
<td><code>BYPASS</code> status</td>
<td>A Cache Rule is bypassing cache</td>
<td>Review your <a href="/cache/how-to/cache-rules/">Cache Rules</a> configuration</td>
</tr>
<tr>
<td><code>MISS</code> on every request</td>
<td>Response includes <code>Set-Cookie</code> header</td>
<td>Configure your origin to not set cookies on static assets, or use a Cache Rule to <a href="/cache/concepts/cache-behavior/#interaction-of-set-cookie-response-header-with-cache">ignore cookies</a></td>
</tr>
<tr>
<td><code>MISS</code> with query strings</td>
<td>Different query strings create different cache entries</td>
<td>Use a <a href="/cache/how-to/cache-rules/examples/custom-cache-key/">custom cache key</a> to ignore or normalize query strings</td>
</tr>
</tbody>
</table>
<h3 id="cache-additional-static-content">Cache additional static content</h3>
<p>By default, Cloudflare only caches certain <a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">file extensions</a>. To cache additional static content:</p>
<ol>
<li>Go to <strong>Caching</strong> &gt; <strong>Cache Rules</strong>.</li>
<li>Create a rule to <a href="/cache/how-to/cache-rules/examples/cache-everything/">cache specific content</a>.</li>
<li>Set appropriate <a href="/cache/how-to/cache-rules/settings/#edge-ttl">Edge TTLs</a>.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13881.md")
</aside>
<h3 id="use-cloudflare-trace-to-debug-cache-rules">Use Cloudflare Trace to debug cache rules</h3>
<p>If your cache rules are not applying as expected, use <a href="/rules/trace-request/">Cloudflare Trace</a> to simulate a request and see exactly which rules match. Trace shows you how your Cloudflare configurations (including cache rules, page rules, and other settings) would affect a specific URL.</p>
<p>This is particularly useful when:</p>
<ul>
<li>A cache rule should be caching content but the response shows <code>DYNAMIC</code> or <code>BYPASS</code></li>
<li>You are unsure which rule is taking precedence</li>
<li>You want to test a &quot;what-if&quot; scenario before making changes</li>
</ul>
<hr />
<h2 id="step-6-diagnose-network-issues">Step 6: Diagnose network issues</h2>
<p>If curl shows high TCP Connect or TLS Handshake times, the issue may be network-related rather than application-related.</p>
<h3 id="test-your-internet-connection">Test your Internet connection</h3>
<p>Visit <a href="https://speed.cloudflare.com">speed.cloudflare.com</a> to test:</p>
<ul>
<li>Download and upload speeds</li>
<li>Latency (ping)</li>
<li>Jitter</li>
<li>Packet loss</li>
</ul>
<p>Poor results indicate issues with your local network or ISP.</p>
<h3 id="run-mtr-from-your-location-to-cloudflare">Run MTR from your location to Cloudflare</h3>
<p>MTR combines traceroute and ping to show latency and packet loss at each network hop.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13897.md")
</div></div>
<p>Look for:</p>
<ul>
<li><strong>High latency</strong> at specific hops (indicates slow network segments)</li>
<li><strong>Packet loss</strong> (indicates network congestion or issues)</li>
<li><strong>Timeouts</strong> (may indicate firewalls or routing issues)</li>
</ul>
<p>For more details, refer to <a href="https://www.cloudflare.com/learning/network-layer/what-is-mtr/">How to read MTR</a>.</p>
<h3 id="run-mtr-from-your-origin-to-cloudflare">Run MTR from your origin to Cloudflare</h3>
<p>If you have access to your origin server, run MTR from the origin to a <a href="https://www.cloudflare.com/ips/">Cloudflare IP address</a> to test the network path between your origin and Cloudflare.</p>
<pre tabindex="0"><code class="language-bash">mtr -rw 104.16.132.229&#10;</code></pre>
<p>High latency or packet loss on this path affects all requests that miss the cache.</p>
<hr />
<h2 id="step-7-understand-network-routing">Step 7: Understand network routing</h2>
<p>How requests are routed to Cloudflare data centers can significantly impact performance.</p>
<h3 id="identify-which-data-center-serves-your-requests">Identify which data center serves your requests</h3>
<p>Add <code>/cdn-cgi/trace</code> to your domain to see which Cloudflare data center is serving your requests:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13900.md")
</div></div>
<p>The <code>colo</code> field shows the three-letter airport code of the serving data center (for example, <code>colo=SJC</code> for San Jose). You can find the full list of Cloudflare data centers and their codes on the <a href="https://www.cloudflarestatus.com/">Cloudflare status page</a>.</p>
<h3 id="why-routing-matters">Why routing matters</h3>
<p>When a request reaches Cloudflare:</p>
<ol>
<li>The request is routed to a nearby Cloudflare data center based on <span class="nb-glossary-tooltip" title="anycast">anycast</span> <a href="https://www.cloudflare.com/learning/cdn/glossary/anycast-network/">routing</a>.</li>
<li>If the content is cached, it is served immediately.</li>
<li>If not cached, Cloudflare fetches from your origin server.</li>
</ol>
<p>If your origin server is geographically distant from the Cloudflare data center serving your users, uncached requests will be slow.</p>
<h3 id="troubleshoot-unexpected-routing">Troubleshoot unexpected routing</h3>
<p>If requests are being routed to a data center that seems far from the user, this may be due to Cloudflare's automated traffic engineering or a user’s ISP routing traffic.</p>
<p>While Cloudflare always strives to provide the best possible performance by serving traffic from the closest location, reliability is the top priority. In instances where performance and reliability are in conflict, Cloudflare's systems are designed to prioritize a stable connection over a local one.</p>
<p>For more details, refer to <a href="/support/troubleshooting/general-troubleshooting/geographic-traffic-routing/">Cloudflare traffic not being sent to the geographically closest data center</a>.</p>
<p>Common causes of unexpected routing:</p>
<table>
<thead>
<tr>
<th>Symptom</th>
<th>Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td>Requests route to a distant data center</td>
<td>Cloudflare traffic engineering for reliability, or ISP routing decisions</td>
</tr>
<tr>
<td>Routing changes between requests</td>
<td>Normal behavior - routing adapts to network conditions or ISP load balancing</td>
</tr>
<tr>
<td>Consistent routing to a distant region</td>
<td>ISP peering location or Cloudflare capacity management</td>
</tr>
<tr>
<td>High latency despite nearby data center</td>
<td>Network congestion on the path</td>
</tr>
</tbody>
</table>
<h3 id="solutions-for-origin-distance">Solutions for origin distance</h3>
<p>Consider these solutions based on your needs:</p>
<table>
<thead>
<tr>
<th>Solution</th>
<th>Description</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Improve cache hit ratio</strong></td>
<td>Cache more content to reduce origin fetches</td>
<td>All sites</td>
</tr>
<tr>
<td><strong><a href="/cache/how-to/tiered-cache/">Tiered Cache</a></strong></td>
<td>Use upper-tier data centers to reduce origin requests</td>
<td>Sites with global traffic</td>
</tr>
<tr>
<td><strong><a href="/argo-smart-routing/">Argo Smart Routing</a></strong></td>
<td>Route traffic over faster network paths</td>
<td>Sites with slow origin connections</td>
</tr>
<tr>
<td><strong>Move origin closer</strong></td>
<td>Deploy origin servers in multiple regions</td>
<td>Large-scale applications</td>
</tr>
</tbody>
</table>
<h3 id="enable-argo-smart-routing">Enable Argo Smart Routing</h3>
<p><a href="/argo-smart-routing/">Argo Smart Routing</a> analyzes network conditions in real-time and routes traffic over the fastest paths, reducing latency by an average of 30%.</p>
<p>Argo Smart Routing is part of <a href="/smart-shield/">Smart Shield</a>, which bundles multiple Cloudflare performance and reliability features.</p>
<p>To enable Argo Smart Routing:</p>
<ol>
<li>Go to the <a href="https://dash.cloudflare.com/?to=/:account/:zone/smart-shield">Cloudflare dashboard</a>.</li>
<li>Follow the <a href="/smart-shield/get-started/">Smart Shield setup guide</a> to enable the feature.</li>
</ol>
<p>Argo is particularly effective when:</p>
<ul>
<li>Your origin is far from your users</li>
<li>Network congestion affects certain paths</li>
<li>You need consistent performance globally</li>
</ul>
<p>For detailed information about how Argo Smart Routing works, refer to the <a href="/argo-smart-routing/">Argo Smart Routing documentation</a>.</p>
<hr />
<h2 id="contact-support-if-the-problem-persists">Contact Support if the problem persists</h2>
<p>If you have followed the steps above and the performance issue persists, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> for assistance.</p>
<p>When contacting Support, provide as much evidence as possible to help diagnose the issue:</p>
<ul>
<li><strong>HAR file</strong> - <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#generate-a-har-file">Generate a HAR file</a> that captures the slow requests. This provides detailed timing information for every request.</li>
<li><strong>Observatory results</strong> - Share screenshots or links to your Observatory test results.</li>
<li><strong>RUM data</strong> - If you have Web Analytics enabled, share relevant metrics showing the performance issue.</li>
<li><strong>curl output</strong> - Include the timing breakdown from <code>curl --write-out</code> for the slow assets.</li>
<li><strong>MTR results</strong> - If you suspect network issues, include MTR output from your location to the affected domain.</li>
<li><strong>Specific URLs</strong> - List the exact URLs that are slow, along with the expected and actual response times.</li>
</ul>
<p>The more evidence you provide showing the slowness, the faster Support can identify and resolve the issue.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/speed/observatory/">Observatory</a> - Test and monitor website performance</li>
<li><a href="/cache/performance-review/cache-analytics/">Cache Analytics</a> - Analyze cache hit rates</li>
<li><a href="/cache/how-to/cache-rules/">Cache Rules</a> - Control what gets cached</li>
<li><a href="/argo-smart-routing/">Argo Smart Routing</a> - Optimize network routing</li>
<li><a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/">Gathering information for troubleshooting</a> - Collect diagnostic data</li>
</ul>
