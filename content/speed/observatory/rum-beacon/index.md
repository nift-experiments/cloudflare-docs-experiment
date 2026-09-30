<p>The RUM beacon is a JavaScript snippet that runs when a Cloudflare customer enables RUM through <a href="/web-analytics/">Web Analytics</a> or <a href="/speed/observatory/">Observatory</a>. This script runs in users' browsers when they visit the customer's site, and its purpose is to collect performance-related data, for example, page load time, and send it to Cloudflare's systems for processing. This <a href="/web-analytics/data-metrics/">data</a> is then presented to the customer, providing valuable insights into the website's performance and usage.</p>
<p>The RUM beacon script can be enabled into a webpage in two ways:</p>
<ul>
<li>
<p><strong>One-click setup</strong>: For <a href="/web-analytics/get-started/#sites-proxied-through-cloudflare">sites proxied through Cloudflare</a> that have Web Analytics enabled, the snippet can be <em>automatically</em> injected into pages as the HTML response passes through Cloudflare's edge network to the browser by simply enabling the automatic injection option.</p>
</li>
<li>
<p><strong>Manual setup</strong>: Websites can <em>manually</em> add the script by embedding a code snippet into their pages. Refer to the <a href="/web-analytics/get-started/#sites-not-proxied-through-cloudflare">Sites not proxied through Cloudflare section</a>, for more information about how to manually insert the snippet into your HTML.</p>
</li>
</ul>
<h2 id="data-collection">Data collection</h2>
<p>Once downloaded to the browser, the RUM beacon script runs as JavaScript in the browser. It collects performance data from browser <a href="https://developer.mozilla.org/en-US/docs/Web/API/Performance_API">APIs</a> and sends this data to Cloudflare for processing.</p>
<p>The data collected from the browser is summarized in the table below:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Example</th>
<th>Description</th>
<th>How it is collected</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pageloadId</code></td>
<td>0c698922-8d60-40bf-85ac-7982b5f8034d</td>
<td>The unique ID for the page.</td>
<td>Generated in the browser code.</td>
</tr>
<tr>
<td><code>referrer</code></td>
<td><a href="https://cfrumtest.com/">https://cfrumtest.com/</a></td>
<td>The referring page URL.</td>
<td>If it is a multi-page application (MPA), then it is generated from <a href="https://developer.mozilla.org/en-US/docs/Web/API/Document/referrer">document.referrer</a>. If it is a single-page application (SPA), then it is generated from a local in-memory variable in the beacon code which stores previous URLs.</td>
</tr>
<tr>
<td><code>startTime</code></td>
<td>1693488419352</td>
<td>Baseline for performance-related timestamps.</td>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/Performance/timeOrigin">performance.timeOrigin</a></td>
</tr>
<tr>
<td><code>memory</code></td>
<td><code>{ totalJSHeapSize: 39973671, usedJSHeapSize: 39127515, jsHeapSizeLimit: 4294705152 }</code></td>
<td>Measures memory heap size.</td>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/Performance/memory">performance.memory</a> (deprecated)</td>
</tr>
<tr>
<td><code>timings</code></td>
<td>Object of <a href="https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming">PerformanceTiming</a></td>
<td>Timing data.</td>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/Performance/timing">performance.timing</a> (deprecated, fallback when <code>timingV2</code> is unavailable)</td>
</tr>
<tr>
<td><code>timingV2</code></td>
<td>Array of <a href="https://developer.mozilla.org/en-US/docs/Web/API/PerformanceNavigationTiming">PerformanceNavigationTiming</a></td>
<td>Navigation timing data.</td>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/Performance/getEntriesByType">performance.getEntriesByType(&quot;navigation&quot;)</a></td>
</tr>
<tr>
<td><code>resources</code></td>
<td>Array of <a href="https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming">PerformanceResourceTiming</a></td>
<td>Resource timing data.</td>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming">performance.getEntriesByType(&quot;resource&quot;)</a></td>
</tr>
<tr>
<td><code>firstPaint</code></td>
<td>Array of <a href="https://developer.mozilla.org/en-US/docs/Web/API/PerformancePaintTiming">PerformancePaintTiming</a></td>
<td>Paint timing data.</td>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/PerformancePaintTiming">performance.getEntriesByType(&quot;paint&quot;)</a></td>
</tr>
<tr>
<td><code>firstContentfulPaint</code></td>
<td>209</td>
<td>First Contentful Paint metric.</td>
<td><a href="https://www.npmjs.com/package/web-vitals">web-vitals module</a> <sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td><code>FCP</code></td>
<td>209</td>
<td>First Contentful Paint metric.</td>
<td><a href="https://www.npmjs.com/package/web-vitals">web-vitals module</a> <sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td><code>LCP</code></td>
<td>209</td>
<td>Largest Contentful Paint metric.</td>
<td><a href="https://www.npmjs.com/package/web-vitals">web-vitals module</a> <sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td><code>CLS</code></td>
<td>0.001</td>
<td>Cumulative Layout Shift metric.</td>
<td><a href="https://www.npmjs.com/package/web-vitals">web-vitals module</a> <sup><a href="#footnote-1">1</a></sup></td>
</tr>
</tbody>
</table>
<pre><code>                                                       |&#10;</code></pre>
<p>| <code>TTFB</code>       | 0.03 | Time to First Byte metric. | <a href="https://www.npmjs.com/package/web-vitals">web-vitals module</a> <sup><a href="#footnote-1">1</a></sup>                                                           |
| <code>INP</code>        | 1.23 | Interaction to Next Paint metric. | <a href="https://www.npmjs.com/package/web-vitals">web-vitals module</a> <sup><a href="#footnote-1">1</a></sup>                                                           |
| <code>landingPath</code>| <a href="https://cfrumtest.com/">https://cfrumtest.com/</a>  | The landing page URL. | <a href="https://developer.mozilla.org/en-US/docs/Web/API/Performance/getEntriesByType">performance.getEntriesByType(&quot;navigation&quot;)</a> |</p>
<h2 id="data-processing">Data processing</h2>
<p>RUM data is generally processed at the nearest Cloudflare data center based on how the incoming request is routed. This is determined by a number of factors including <a href="https://www.cloudflare.com/en-gb/learning/cdn/glossary/anycast-network/">Anycast</a> and <a href="https://blog.cloudflare.com/unimog-cloudflares-edge-load-balancer/">Unimog</a>. Since RUM data does not use location services, it may be processed in a different country or region from where it originated. Although the RUM service receives the client/source IP address from the beacon as part of normal HTTP request handling process, it discards the IP address at the nearest Cloudflare data center and does not store it in core databases or logs.</p>
<h2 id="privacy-information">Privacy information</h2>
<p>The RUM beacon script does not store any data in the browser or access any storage data, such as <a href="https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie">cookies</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage">localStorage</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage">sessionStorage</a>, IP address, or <a href="https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB">IndexedDB</a>. The data we collect is performance data from the browser performance <a href="https://developer.mozilla.org/en-US/docs/Web/API/Performance_API">APIs</a>. This performance data is ephemeral and only relates to the current webpage that is being viewed. If the user refreshes their browser, all the previous performance data is gone and new performance data starts being available. This data is not stored or accessed from anywhere on the device, it is only available as in-memory data.</p>
<h2 id="rum-excluding-eea-eu">RUM excluding EEA/EU</h2>
<p>Customers have the option to enable RUM globally or to limit its application to exclude users connecting to Cloudflare data centers in the EEA/EU. If the latter option is selected, the RUM beacon does not process performance data for users connecting to a Cloudflare data center located in the following countries (ISO codes): AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IS, IE, IT, LV, LI, LT, LU, MT, NL, NO, PL, PT, RO, SK, SI, ES, SE, CH, GB.</p>
<p>Free customers have RUM enabled automatically, with EU traffic excluded, and can switch it off if they prefer. Customers on other plans may enable RUM as needed.</p>
<div class="medium-img">
<p><img src="/assets/upstream/images/speed/enable-rum.png" alt="Enable RUM in the dashboard." /></p>
</div>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">The web-vitals module is an open-source module written by Google. It does not access any type of storage on the browser.</li></ol></section>
