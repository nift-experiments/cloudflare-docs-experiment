<p>Page load time summary gives you an overview of how long your web page takes to load, broken down by area. To access Page load time:</p>
<ol>
<li>Go to <a href="https://dash.cloudflare.com/?to=/:account/web-analytics">Web Analytics</a> from your account home page, and choose a website.</li>
<li>Select <strong>Page load time</strong>.</li>
</ol>
<h2 id="components">Components</h2>
<p>Below is a list of all the components you can inspect:</p>
<h3 id="page-load">Page load</h3>
<p>The total amount of time required to load the page. Note that page load time does not correspond to the sum of the other timings available in Web Analytics. This happens because the page load time also includes timings that are not displayed, such as pre-DNS lookup timings and unattributed gaps between timing metrics.</p>
<h3 id="dns-domainlookupend-domainlookupstart">DNS (<code>domainLookupEnd</code> - <code>domainLookupStart</code>)</h3>
<p>How long a DNS query takes. This could appear as zero for reused connections or content stored in the local cache (memory or disk).</p>
<h3 id="tcp-connectend-connectstart">TCP (<code>connectEnd</code> - <code>connectStart</code>)</h3>
<p>How long it takes to establish a TCP connection with the server. If using HTTPS, this process includes TLS negotiation time.</p>
<h3 id="request-responsestart-requeststart">Request (<code>responseStart</code> - <code>requestStart</code>)</h3>
<p>The time elapsed between making an HTTP request and receiving the first byte of the response.</p>
<h3 id="response-responseend-responsestart">Response (<code>responseEnd</code> - <code>responseStart</code>)</h3>
<p>The time elapsed between the first byte and the last byte of the received response. Think of this as a resource download time.</p>
<h3 id="processing-domcomplete-dominteractive">Processing (<code>domComplete</code> - <code>domInteractive</code>)</h3>
<p>How long it took to render the page. This includes loading any resources that block page rendering, including images, scripts, and style sheets. If this number is big, optimize your document architecture, resource size, or configure settings in the Cloudflare Speed app. This document process can be drilled down more with <code>domInteractive</code>, <code>domContentLoadedEventStart</code>, <code>domContentLoadedEventEnd</code>, and <code>domComplete</code>.</p>
<h3 id="load-event-loadeventend-loadeventstart">Load Event (<code>loadEventEnd</code> - <code>loadEventStart</code>)</h3>
<p>An event triggered by the browser when a document and its resources finish loading. The Load Event duration may be a useful metric if you have additional functions or any logic for the load event.</p>
<p><img src="/assets/upstream/images/web-analytics/dash-web_analytics-page_load_time.png" alt="Web Analytics load time summary page" /></p>
<h2 id="data-collected-for-paint-timings">Data collected for Paint Timings</h2>
<p>To make Web Analytics work, Cloudflare collects several types of data points. These are the additional data points collected for Paint Timings:</p>
<h3 id="first-paint">First Paint</h3>
<p>The time between navigation and when the browser renders the first pixels to the screen.</p>
<h3 id="first-contentful-paint">First Contentful Paint</h3>
<p>Time when the browser renders the first bit of content from the DOM.</p>
