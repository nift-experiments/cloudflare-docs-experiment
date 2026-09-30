---
cp9:
  canonical: https://developers.cloudflare.com/radar/investigate/url-scanner/
  description: Scan and investigate domains, IPs, and URLs using the Cloudflare Radar URL Scanner API and Security Center dashboard.
  full_title: URL Scanner · Cloudflare Radar docs
  head_html: <title>URL Scanner · Cloudflare Radar docs</title><meta name="generator" content="Nift"><meta name="description" content="Scan and investigate domains, IPs, and URLs using the Cloudflare Radar URL Scanner API and Security Center dashboard."><link rel="canonical" href="https://developers.cloudflare.com/radar/investigate/url-scanner/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/radar/investigate/url-scanner/index.md"><meta property="og:title" content="URL Scanner · Cloudflare Radar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Scan and investigate domains, IPs, and URLs using the Cloudflare Radar URL Scanner API and Security Center dashboard."><meta property="og:url" content="https://developers.cloudflare.com/radar/investigate/url-scanner/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Radar"><meta name="algolia_product_filter" content="Radar"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Radar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/radar/investigate/url-scanner/#page","headline":"URL Scanner \u00b7 Cloudflare Radar docs","description":"Scan and investigate domains, IPs, and URLs using the Cloudflare Radar URL Scanner API and Security Center dashboard.","url":"https://developers.cloudflare.com/radar/investigate/url-scanner/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /radar/investigate/url-scanner/
  schema: 1
---
<p>To better understand Internet usage around the world, use Cloudflare's URL Scanner. With Cloudflare's URL Scanner, you have the ability to investigate the details of a domain, IP, URL, or ASN. Cloudflare's URL Scanner is available in the Security Center of the Cloudflare dashboard, <a href="https://radar.cloudflare.com/scan">Cloudflare Radar</a>, and the Cloudflare <a href="/api/resources/url_scanner/">API</a>.</p>
<h2 id="use-the-api">Use the API</h2>
<p>To make your first URL scan using the API, you must obtain a URL Scanner specific <a href="/fundamentals/api/get-started/create-token/">API token</a>. Create a Custom Token with <em>Account</em> &gt; <em>URL Scanner</em> in the <strong>Permissions</strong> group, and select <em>Edit</em> as the access level.</p>
<p>Once you have the token, and you know your <code>account_id</code>, you are ready to make your first request to the API at <code>https://api.cloudflare.com/client/v4/accounts/{account_id}/urlscanner/</code>.</p>
<h3 id="submit-url-to-scan">Submit URL to scan</h3>
<p>To submit a URL to scan, the only required information is the URL to be scanned in the <code>POST</code> request body:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/urlscanner/v2/scan&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;url&quot;: &quot;https://www.example.com&quot;&#10;}&#x27;&#10;</code></pre>
<p>By default, the report will have a <code>Public</code> visibility level, which means it will appear in the <a href="https://radar.cloudflare.com/scan#recent-scans">recent scans</a> list and in search results. It will also include a single screenshot with desktop resolution.</p>
<p>A successful response will have a status code of <code>200</code> and be similar to the following:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;uuid&quot;: &quot;095be615-a8ad-4c33-8e9c-c7612fbf6c9f&quot;,&#10;  &quot;api&quot;: &quot;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/urlscanner/v2/result/095be615-a8ad-4c33-8e9c-c7612fbf6c9f&quot;,&#10;  &quot;visibility&quot;: &quot;public&quot;,&#10;  &quot;url&quot;: &quot;https://www.example.com&quot;,&#10;  &quot;message&quot;: &quot;Submission successful&quot;&#10;}&#10;</code></pre>
<p>You can submit up to 100 URLs at the same time via the <a href="https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/bulk_create/">API</a>.</p>
<p>The <code>uuid</code> property in the response above identifies the scan and will be required when fetching the scan report.</p>
<h4 id="submit-a-custom-url-scan">Submit a custom URL Scan</h4>
<p>Here's an example request body with some custom configuration options:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;url&quot;: &quot;https://example.com&quot;,&#10;	&quot;screenshotsResolutions&quot;: [&#10;		&quot;desktop&quot;, &quot;mobile&quot;, &quot;tablet&quot;&#10;	],&#10;  &quot;customagent&quot;: &quot;XXX-my-user-agent&quot;,&#10;  &quot;referer&quot;: &quot;example&quot;,&#10;	&quot;customHeaders&quot;: {&#10;		&quot;Authorization&quot;: &quot;xxx-token&quot;&#10;	},&#10;	&quot;visibility&quot;: &quot;Unlisted&quot;&#10;}&#10;</code></pre>
<p>Above, the visibility level is set as <code>Unlisted</code>, which means that the scan report won't be included in the <a href="https://radar.cloudflare.com/scan#recent-scans">recent scans</a> list nor in search results. In  effect, only users with knowledge of the scan ID will be able to access it.</p>
<p>There will also be three screenshots taken of the webpage, one per target device type. The <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent"><code>User-Agent</code></a> will be set as &quot;XXX-my-user-agent&quot;. Note that you can set any custom HTTP header, including <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Authorization">Authorization</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="header">Header</h3>
@markup("md", "content/.markup/bodies/11551.md")
</aside>
<h3 id="get-scan-report">Get scan report</h3>
<p>Once the URL Scan submission is made, the current progress can be checked by calling <code>https://api.cloudflare.com/client/v4/accounts/{account_id}/urlscanner/v2/result/{scan_id}</code>. The <code>scan_id</code> will be the <code>uuid</code> value returned in the previous response.</p>
<p>While the scan is in progress, the HTTP status code will be <code>404</code>; once it is finished, it will be <code>200</code>. Cloudflare recommends that you poll every 10-30 seconds.</p>
<p>The response will include, among others, the following top properties:</p>
<ul>
<li><code>task</code> - Information on the scan submission.</li>
<li><code>page</code> - Information pertaining to the primary response, for example IP address, ASN, server, and page redirect history.</li>
<li><code>data.requests</code> - Request chains involved in the page load.</li>
<li><code>data.cookies</code> - Cookies set by the page.</li>
<li><code>data.globals</code> - Non-standard JavaScript global variables.</li>
<li><code>data.console</code> - Console logs.</li>
<li><code>data.performance</code> - Timings as given by the <a href="https://developer.mozilla.org/en-US/docs/Web/API/PerformanceNavigationTiming"><code>PerformanceNavigationTiming</code></a> interface.</li>
<li><code>meta</code> - Meta processors output including detected technologies, domain and URL categories, rank, geolocation information, and others.</li>
<li><code>lists.ips</code> - IPs contacted.</li>
<li><code>lists.asns</code> - AS Numbers contacted.</li>
<li><code>lists.domains</code> - Hostnames contacted, including <code>dns</code> record information.</li>
<li><code>lists.hashes</code> - Hashes of response bodies, of the main page HTML structure, screenshots, and favicons.</li>
<li><code>lists.certificates</code> - TLS certificates of HTTP responses.</li>
<li><code>verdicts</code> - Verdicts on malicious content.</li>
</ul>
<p>Some examples of more specific properties include:</p>
<ul>
<li><code>task.uuid</code> - ID of the scan.</li>
<li><code>task.url</code> - Submitted URL of the scan. May differ from final URL (<code>page.url</code>) if there are HTTP redirects.</li>
<li><code>task.success</code> - Whether scan was successful or not. Scans can fail for various reasons, including DNS errors.</li>
<li><code>task.status</code> - Current scan status, for example, <code>Queued</code>, <code>InProgress</code>, or <code>Finished</code>.</li>
<li><code>meta.processors.domainCategories</code> - Cloudflare categories of the main hostname contacted.</li>
<li><code>meta.processors.phishing</code> - What kind of phishing, if any, was detected.</li>
<li><code>meta.processors.radarRank</code> - <a href="http://blog.cloudflare.com/radar-domain-rankings/">Cloudflare Radar Rank</a> of the main hostname contacted.</li>
<li><code>meta.processors.wappa</code> - The kind of technologies detected as being in use by the website, with the help of <a href="https://github.com/Lissy93/wapalyzer">Wappalyzer</a>.</li>
<li><code>page.url</code> - URL of the primary request, after all HTTP redirects.</li>
<li><code>page.country</code> - Country name from geolocation data associated with the main IP address contacted.</li>
<li><code>page.history</code> - Main page history, including any HTTP redirects.</li>
<li><code>page.screenshot</code> - Various hashes of the main screenshot. Can be used to search for sites with similar screenshots.</li>
<li><code>page.domStructHash</code> - HTML structure hash. Use it to search for sites with similar structure.</li>
<li><code>page.favicon.hash</code> - MD5 hash of the favicon.</li>
<li><code>verdicts.overall.malicious</code> - Whether the website was considered malicious <em>at the time of the scan</em>. Please check the remaining properties for each subsystem(s) for specific threats detected.</li>
</ul>
<p>The <a href="/api/resources/url_scanner/subresources/scans/methods/get/">Get URL Scan</a> API endpoint documentation contains the full response schema.</p>
<p>To fetch the scan's <a href="/api/resources/url_scanner/subresources/scans/methods/screenshot/">screenshots</a> or full <a href="/api/resources/url_scanner/subresources/scans/methods/har/">network log</a> refer to the corresponding endpoints' documentation.</p>
<h3 id="search-scans">Search scans</h3>
<p>Use a subset of ElasticSearch Query syntax to filter scans. Search results will include <code>Public</code> scans and your own <code>Unlisted</code> scans.</p>
<p>To search for scans to the hostname <code>google.com</code>, use the query parameter <code>q=page.domain:&quot;google.com&quot;</code>:</p>
<pre tabindex="0"><code class="language-bash">curl &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/urlscanner/v2/search?q=page.domain:google.com&#x27; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>If, instead, you wanted to search for scans that made at least one request to the hostname <code>cdnjs.cloudflare.com</code>, for example sites that use a JavaScript library hosted at <code>cdnjs.cloudflare.com</code>, use the query parameter <code>hostname=cdnjs.cloudflare.com</code>:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/urlscanner/v2/search?q=domain:cdnjs.cloudflare.com&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Some other example queries:</p>
<ul>
<li><code>task.url:&quot;https://google.com&quot; OR task.url:&quot;https://www.google.com&quot;</code>: Search for scans whose submitted URL was either <code>google.com</code> or <code>www.google.com</code>. URLs must be enclosed in quotes.</li>
<li><code>page.url:&quot;https://google.com&quot; AND NOT task.url:&quot;https://google.com&quot;</code>: Search for scans to <code>google.com</code> whose submitted URL was not <code>google.com</code> (that is, sites that redirected to google.com).</li>
<li><code>page.domain:microsoft AND verdicts.malicious:true AND NOT page.domain:microsoft.com</code>: Malicious scans whose hostname starts with <code>microsoft</code>. Would match domains like <code>microsoft.phish.com</code>.</li>
<li><code>apikey:me AND date:[2024-01 TO 2024-10]</code>: Your scans from January 2024 to October 2024.</li>
<li><code>page.domain:(blogspot OR www.blogspot)</code>: Searches for scans whose main domain starts with <code>blogspot</code> or with <code>www.blogspot</code>.</li>
<li><code>date:&gt;now-7d AND path:okta-sign-in.min.js</code>: Scans from the last seven days with any request path that ends with <code>okta-sign-in.min.js</code>.</li>
<li><code>page.asn:AS24940 AND hash:-557369673</code>: Websites hosted in AS24940 where a resource with the given hash was retrieved.</li>
<li><code>hash:8f662c2ce9472ba8d03bfeb8cdae112dbc0426f99da01c5d70c7eb4afd5893ca</code>: Using the hash at <code>page.domStructHash</code> search for other scans with the same HTML structure hash.</li>
</ul>
<p>Go to <a href="/api/resources/url_scanner/subresources/scans/methods/list/">Search URL scans</a> in the API documentation for the full list of available options.</p>
<h3 id="security-center">Security Center</h3>
<p>Alternatively, you can search in the Security Center:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Investigate</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Enter your query and select <strong>Search</strong>.</li>
</ol>
<p>You can scan a URL by location. Scanning a URL by location allows you to analyze how a website may present different content depending on your location. This helps to expose and examine region-specific malicious activities.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11550.md")
</aside>
<p>To scan a URL based on your geographic location:</p>
<ol>
<li>Enter your URL.</li>
<li>Go to <strong>Location</strong> &gt; Select which country to scan the URL from.</li>
<li>Select <strong>Scan now</strong>.</li>
</ol>
<p>You can also use the <a href="https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/create/#(params)%20default%20%3E%20(param)%20account_id%20%3E%20">API</a> to scan a URL from a specific location.</p>
<p>In Security Center, you can retrieve pre-filtered information by:</p>
<ul>
<li>Similar screenshot</li>
<li>Identical favicon</li>
<li>Similar favicon</li>
<li>Similar HTML structure</li>
<li>Identical ASN</li>
<li>Identical IP</li>
<li>Identical domain</li>
<li>Identical final URL (after all redirections)</li>
</ul>
