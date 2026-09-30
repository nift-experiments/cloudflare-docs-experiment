---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/analytics/5/
  description: '2025-10-02'
  full_title: Analytics changelog - page 5 | Cloudflare Docs
  head_html: <title>Analytics changelog - page 5 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-10-02"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/analytics/5/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Analytics changelog - page 5"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-10-02"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/analytics/5/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/analytics/5/#page","headline":"Analytics changelog - page 5 | Cloudflare Docs","description":"2025-10-02","url":"https://developers.cloudflare.com/changelog/product-group/analytics/5/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/analytics/5/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="workers-analytics-engine-adds-supports-for-new-sql-functions"><a href="/changelog/post/2025-09-26-analytics-engine-sql-enhancements/">Workers Analytics Engine adds supports for new SQL functions</a></h2>
<p><em>2025-10-02</em></p>
<p>You can now perform more powerful queries directly in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a> with a major expansion of our SQL function library.</p>
<p>Workers Analytics Engine allows you to ingest and store high-cardinality data at scale (such as custom analytics) and query your data through a simple SQL API.</p>
<p>Today, we've expanded Workers Analytics Engine's SQL capabilities with several new functions:</p>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/"><strong>New aggregate functions:</strong></a></p>
<ul>
<li><code>argMin()</code> - Returns the value associated with the minimum in a group</li>
<li><code>argMax()</code> - Returns the value associated with the maximum in a group</li>
<li><code>topK()</code> - Returns an array of the most frequent values in a group</li>
<li><code>topKWeighted()</code> - Returns an array of the most frequent values in a group using weights</li>
<li><code>first_value()</code> - Returns the first value in an ordered set of values within a partition</li>
<li><code>last_value()</code> - Returns the last value in an ordered set of values within a partition</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/"><strong>New bit functions:</strong></a></p>
<ul>
<li><code>bitAnd()</code> - Returns the bitwise AND of two expressions</li>
<li><code>bitCount()</code> - Returns the number of bits set to one in the binary representation of a number</li>
<li><code>bitHammingDistance()</code> - Returns the number of bits that differ between two numbers</li>
<li><code>bitNot()</code> - Returns a number with all bits flipped</li>
<li><code>bitOr()</code> - Returns the inclusive bitwise OR of two expressions</li>
<li><code>bitRotateLeft()</code> - Rotates all bits in a number left by specified positions</li>
<li><code>bitRotateRight()</code> - Rotates all bits in a number right by specified positions</li>
<li><code>bitShiftLeft()</code> - Shifts all bits in a number left by specified positions</li>
<li><code>bitShiftRight()</code> - Shifts all bits in a number right by specified positions</li>
<li><code>bitTest()</code> - Returns the value of a specific bit in a number</li>
<li><code>bitXor()</code> - Returns the bitwise exclusive-or of two expressions</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/"><strong>New mathematical functions:</strong></a></p>
<ul>
<li><code>abs()</code> - Returns the absolute value of a number</li>
<li><code>log()</code> - Computes the natural logarithm of a number</li>
<li><code>round()</code> - Rounds a number to a specified number of decimal places</li>
<li><code>ceil()</code> - Rounds a number up to the nearest integer</li>
<li><code>floor()</code> - Rounds a number down to the nearest integer</li>
<li><code>pow()</code> - Returns a number raised to the power of another number</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/string-functions/"><strong>New string functions:</strong></a></p>
<ul>
<li><code>lowerUTF8()</code> - Converts a string to lowercase using UTF-8 encoding</li>
<li><code>upperUTF8()</code> - Converts a string to uppercase using UTF-8 encoding</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/"><strong>New encoding functions:</strong></a></p>
<ul>
<li><code>hex()</code> - Converts a number to its hexadecimal representation</li>
<li><code>bin()</code> - Converts a string to its binary representation</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/"><strong>New type conversion functions:</strong></a></p>
<ul>
<li><code>toUInt8()</code> - Converts any numeric expression, or expression resulting in a string representation of a decimal, into an unsigned 8 bit integer</li>
</ul>
<h4 id="2025-09-26-analytics-engine-sql-enhancements-ready-to-get-started">Ready to get started?</h4>
Whether you're building usage-based billing systems, customer analytics dashboards, or other custom analytics, these functions let you get the most out of your data. [Get started ](/analytics/analytics-engine/get-started/) with Workers Analytics Engine and explore all available functions in our [SQL reference documentation](/analytics/analytics-engine/sql-reference/).


<h2 id="new-confidence-intervals-in-graphql-analytics-api"><a href="/changelog/post/2025-10-01-confidence-intervals/">New Confidence Intervals in GraphQL Analytics API</a></h2>
<p><em>2025-10-01</em></p>
<p>The GraphQL Analytics API now supports confidence intervals for <code>sum</code> and <code>count</code> fields on adaptive (sampled) datasets. Confidence intervals provide a statistical range around sampled results, helping verify accuracy and quantify uncertainty.</p>
<ul>
<li><strong>Supported datasets</strong>: Adaptive (sampled) datasets only.</li>
<li><strong>Supported fields</strong>: All <code>sum</code> and <code>count</code> fields.</li>
<li><strong>Usage</strong>: The confidence <code>level</code> must be provided as a decimal between 0 and 1 (e.g. <code>0.90</code>, <code>0.95</code>, <code>0.99</code>).</li>
<li><strong>Default</strong>: If no confidence level is specified, no intervals are returned.</li>
</ul>
<p>For examples and more details, see the <a href="/analytics/graphql-api/features/confidence-intervals/">GraphQL Analytics API documentation</a>.</p>


<h2 id="regional-data-in-cloudflare-radar"><a href="/changelog/post/2025-09-29-radar-regional-data/">Regional Data in Cloudflare Radar</a></h2>
<p><em>2025-09-29</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now introduces Regional Data, providing traffic insights that bring a more localized perspective to the traffic trends shown on Radar.</p>
<p>The following API endpoints are now available:</p>
<ul>
<li><a href="/api/resources/radar/subresources/geolocations/methods/get/"><code>Get Geolocation</code></a> - Retrieves geolocation by <code>geoId</code>.</li>
<li><a href="/api/resources/radar/subresources/geolocations/methods/list/"><code>List Geolocations</code></a> - Lists geolocations.</li>
<li><a href="/api/resources/radar/subresources/netflows/methods/summary_v2/"><code>NetFlows Summary By Dimension</code></a> - Retrieves NetFlows summary by dimension.</li>
</ul>
<p>All <code>summary</code> and <code>timeseries_groups</code> endpoints in <a href="/api/resources/radar/subresources/http/"><code>HTTP</code></a> and <a href="/api/resources/radar/subresources/netflows/"><code>NetFlows</code></a> now include an <code>adm1</code> dimension for grouping data by first level administrative division (for example, state, province, etc.)</p>
<p>A new filter <code>geoId</code> was also added to all endpoints in <a href="/api/resources/radar/subresources/http/"><code>HTTP</code></a> and <a href="/api/resources/radar/subresources/netflows/"><code>NetFlows</code></a>, allowing filtering by a specific administrative division.</p>
<p>Check out the new Regional traffic insights on a country specific traffic page <a href="https://radar.cloudflare.com/traffic/pt">new Radar page</a>.</p>


<h2 id="contextual-pivots"><a href="/changelog/post/2025-09-11-contextual-pivots/">Contextual pivots</a></h2>
<p><em>2025-09-11</em></p>
<p>Directly from <a href="/log-explorer/log-search/">Log Search</a> results, customers can pivot to other parts of the Cloudflare dashboard to immediately take action as a result of their investigation.</p>
<p>From the <code>http_requests</code> or <code>fw_events</code> dataset results, right click on an IP Address or JA3 Fingerprint to pivot to the Investigate portal to lookup the reputation of an IP address or JA3 fingerprint.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/investigate-ip-address.png" alt="Investigate IP address" /></p>
<p>Easily learn about error codes by linking directly to our documentation from the <strong>EdgeResponseStatus</strong> or <strong>OriginResponseStatus</strong> fields.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/view-documentation.png" alt="View documentation" /></p>
<p>From the <code>gateway_http</code> dataset, click on a <strong>policyid</strong> to link directly to the Zero Trust dashboard to review or make changes to a specific Gateway policy.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/policyid.png" alt="View policy" /></p>


<h2 id="new-results-table-view"><a href="/changelog/post/2025-09-11-new-results-table-view/">New results table view</a></h2>
<p><em>2025-09-11</em></p>
<p>The results table view of <strong>Log Search</strong> has been updated with additional functionality and a more streamlined user experience. Users can now easily:</p>
<ul>
<li>Remove/add columns.</li>
<li>Resize columns.</li>
<li>Sort columns.</li>
<li>Copy values from any field.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/log-explorer/new-table.png" alt="New results table view" /></p>


<h2 id="logging-headers-and-cookies-using-custom-fields"><a href="/changelog/post/2025-09-03-log-headers-and-cookies/">Logging headers and cookies using custom fields</a></h2>
<p><em>2025-09-03</em></p>
<p><a href="/log-explorer/">Log Explorer</a> now supports logging and filtering on header or cookie fields in the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/"><code>http_requests</code> dataset</a>.</p>
<p>Create a custom field to log desired header or cookie values into the <code>http_requests</code> dataset and Log Explorer will import these as searchable fields. Once configured, use the custom SQL editor in Log Explorer to view or filter on these requests.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/edit-custom-fields.png" alt="Edit Custom fields" /></p>
<p>For more details, refer to <a href="/log-explorer/log-search/#headers-and-cookies">Headers and cookies</a>.</p>


<h2 id="dex-mcp-server"><a href="/changelog/post/2025-08-29-dex-mcp-server/">DEX MCP Server</a></h2>
<p><em>2025-08-29</em></p>
<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device connectivity and performance across your Cloudflare SASE deployment.</p>
<p>We've released an MCP server <a href="https://cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/">(Model Context Protocol)</a> for DEX.</p>
<p>The DEX MCP server is an AI tool that allows customers to ask a question like, &quot;Show me the connectivity and performance metrics for the device used by carly‌@acme.com&quot;, and receive an answer that contains data from the DEX API.</p>
<p>Any Cloudflare One customer using a Free, Pay-as-you-go, or Enterprise account can access the DEX MCP Server. This feature is available to everyone.</p>
<p>Customers can test the new DEX MCP server in less than one minute. To learn more, read the <a href="/cloudflare-one/insights/dex/dex-mcp-server/">DEX MCP server documentation</a>.</p>


<h2 id="dedicated-egress-ip-for-logpush"><a href="/changelog/post/2025-08-22-dedicated-egress-ip-logpush/">Dedicated Egress IP for Logpush</a></h2>
<p><em>2025-08-22</em></p>
<p>Cloudflare Logpush can now deliver logs from using fixed, dedicated egress IPs. By routing Logpush traffic through a Cloudflare zone enabled with <a href="/smart-shield/configuration/dedicated-egress-ips/">Aegis IP</a>, your log destination only needs to allow Aegis IPs making setup more secure.</p>
<p>Highlights:</p>
<ul>
<li>Fixed egress IPs ensure your destination only accepts traffic from known addresses.</li>
<li>Works with any supported Logpush destination.</li>
<li>Recommended to use a dedicated zone as a proxy for easier management.</li>
</ul>
<p>To get started, work with your Cloudflare account team to provision Aegis IPs, then configure your Logpush job to deliver logs through the proxy zone. For full setup instructions, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/egress-ip/">Logpush documentation</a>.</p>


<h2 id="extended-retention"><a href="/changelog/post/2025-08-15-extended-retention/">Extended retention</a></h2>
<p><em>2025-08-15</em></p>
<p>Customers can now rely on Log Explorer to meet their log retention compliance requirements.</p>
<p>Contract customers can choose to store their logs in Log Explorer for up to two years, at an additional cost of $0.10 per GB per month. Customers interested in this feature can contact their account team to have it added to their contract.</p>


<h2 id="save-time-with-bulk-query-creation-in-brand-protection"><a href="/changelog/post/2025-08-15-brand-protection-bulk-endpoint/">Save time with bulk query creation in Brand Protection</a></h2>
<p><em>2025-08-15</em></p>
<p><a href="/security-center/brand-protection/">Brand Protection</a> detects domains that may be impersonating your brand — from common misspellings (<code>cloudfalre.com</code>) to malicious concatenations (<code>cloudflare-okta.com</code>). Saved search queries run continuously and alert you when suspicious domains appear.</p>
<p>You can now create and save multiple queries in a single step, streamlining setup and management. Available now via the <a href="/api/resources/brand_protection/subresources/queries/methods/bulk/">Brand Protection bulk query creation API</a>.</p>


<h2 id="ibm-cloud-logs-as-logpush-destination"><a href="/changelog/post/2025-08-13-ibm-cloud-logs-destination/">IBM Cloud Logs as Logpush destination</a></h2>
<p><em>2025-08-13</em></p>
<p>Cloudflare Logpush now supports IBM Cloud Logs as a native destination.</p>
<p>Logs from Cloudflare can be sent to <a href="https://www.ibm.com/products/cloud-logs">IBM Cloud Logs</a> via <a href="/logs/logpush/">Logpush</a>. The setup can be done through the Logpush UI in the Cloudflare Dashboard or by using the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>. The integration requires IBM Cloud Logs HTTP Source Address and an IBM API Key. The feature also allows for filtering events and selecting specific log fields.</p>
<p>For more information, refer to <a href="/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/">Destination Configuration</a> documentation.</p>


<h2 id="certificate-transparency-insights-in-cloudflare-radar"><a href="/changelog/post/2025-08-04-radar-ct-insights/">Certificate Transparency Insights in Cloudflare Radar</a></h2>
<p><em>2025-08-06</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now introduces Certificate Transparency (CT) insights, providing visibility into certificate issuance trends based on Certificate Transparency logs currently monitored by Cloudflare.</p>
<p>The following API endpoints are now available:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ct/methods/timeseries/"><code>/ct/timeseries</code></a>: Retrieves certificate issuance time series.</li>
<li><a href="/api/resources/radar/subresources/ct/methods/summary/"><code>/ct/summary/{dimension}</code></a>: Retrieves certificate distribution by dimension.</li>
<li><a href="/api/resources/radar/subresources/ct/methods/timeseries_groups/"><code>/ct/timeseries_groups/{dimension}</code></a>: Retrieves time series of certificate distribution by dimension.</li>
<li><a href="/api/resources/radar/subresources/ct/subresources/authorities/methods/list/"><code>/ct/authorities</code></a>: Lists certification authorities.</li>
<li><a href="/api/resources/radar/subresources/ct/subresources/authorities/methods/get/"><code>/ct/authorities/{ca_slug}</code></a>: Retrieves details about a Certification Authority (CA). CA information is derived from the <a href="https://www.ccadb.org/">Common CA Database (CCADB)</a>.</li>
<li><a href="/api/resources/radar/subresources/ct/subresources/logs/methods/list/"><code>/ct/logs</code></a>: Lists CT logs.</li>
<li><a href="/api/resources/radar/subresources/ct/subresources/logs/methods/get/"><code>/ct/logs/{log_slug}</code></a>: Retrieves details about a CT log. CT log information is derived from the <a href="https://googlechrome.github.io/CertificateTransparency/log_lists.html">Google Chrome log list</a>.</li>
</ul>
<p>For the <code>summary</code> and <code>timeseries_groups</code> endpoints, the following dimensions are available (and also usable as filters):</p>
<ul>
<li><code>ca</code>: Certification Authority (certificate issuer)</li>
<li><code>ca_owner</code>: Certification Authority Owner</li>
<li><code>duration</code>: Certificate validity duration (between NotBefore and NotAfter dates)</li>
<li><code>entry_type</code>: Entry type (certificate vs. pre-certificate)</li>
<li><code>expiration_status</code>: Expiration status (valid vs. expired)</li>
<li><code>has_ips</code>: Presence of IP addresses in certificate <a href="https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/#hostname-and-wildcard-coverage">Subject Alternative Names (SANs)</a></li>
<li><code>has_wildcards</code>: Presence of wildcard DNS names in certificate SANs</li>
<li><code>log</code>: CT log name</li>
<li><code>log_api</code>: CT log API (<a href="https://datatracker.ietf.org/doc/html/rfc6962">RFC6962</a> vs. <a href="https://c2sp.org/static-ct-api">Static</a>)</li>
<li><code>log_operator</code>: CT log operator</li>
<li><code>public_key_algorithm</code>: Public key algorithm of certificate's key</li>
<li><code>signature_algorithm</code>: Signature algorithm used by CA to sign certificate</li>
<li><code>tld</code>: Top-level domain for DNS names found in certificates SANs</li>
<li><code>validation_level</code>: <a href="https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/">Validation level</a></li>
</ul>
<p>Check out the new Certificate Transparency insights in the <a href="https://radar.cloudflare.com/certificate-transparency">new Radar page</a>.</p>


<h2 id="new-apis-for-brand-protection-setup"><a href="/changelog/post/2025-07-18-brand-protection-api/">New APIs for Brand Protection setup</a></h2>
<p><em>2025-07-18</em></p>
<hr />
<h4 id="2025-07-18-brand-protection-api-title-new-apis-for-brand-protection-setup-description-you-can-now-use-the-brand-protection-api-endpoints-to-manage-your-brand-protection-queries-date-2025-07-18">title: New APIs for Brand Protection setup
description: You can now use the Brand Protection API endpoints to manage your Brand Protection queries
date: 2025-07-18</h4>
<p>The Brand Protection API is now available, allowing users to create new queries and delete existing ones, fetch matches and more!</p>
<p>What you can do:</p>
<ul>
<li><strong>create new string or logo query</strong></li>
<li><strong>delete string or logo queries</strong></li>
<li><strong>download matches for both logo and string queries</strong></li>
<li><strong>read matches for both logo and string queries</strong></li>
</ul>
<p>Ready to start? Check out the <a href="/api/resources/brand_protection/">Brand Protection API</a> in our documentation.</p>


<h2 id="usage-tracking"><a href="/changelog/post/2025-07-09-usage-tracking/">Usage tracking</a></h2>
<p><em>2025-07-09</em></p>
<p><a href="/log-explorer/">Log Explorer</a> customers can now monitor their data ingestion volume to keep track of their billing. Monthly usage is displayed at the top of the <a href="/log-explorer/log-search/">Log Search</a> and <a href="/log-explorer/manage-datasets/">Manage Datasets</a> screens in Log Explorer.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/ingested-data.png" alt="Ingested data" /></p>


<h2 id="bot-crawler-insights-in-cloudflare-radar"><a href="/changelog/post/2025-07-01-radar-bots-insights/">Bot & Crawler Insights in Cloudflare Radar</a></h2>
<p><em>2025-07-01</em></p>
<h4 id="2025-07-01-radar-bots-insights-web-crawlers-insights">Web crawlers insights</h4>
<p><a href="/radar/"><strong>Radar</strong></a> now offers expanded insights into web crawlers, giving you greater visibility into aggregated trends in crawl and refer activity.</p>
<p>We have introduced the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/summary/"><code>/bots/crawlers/summary/{dimension}</code></a>: Returns an overview of crawler HTTP request distributions across key dimensions.</li>
<li><a href="/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/timeseries_groups/"><code>/bots/crawlers/timeseries_groups/{dimension}</code></a>: Provides time-series data on crawler request distributions across the same dimensions.</li>
</ul>
<p>These endpoints allow analysis across the following dimensions:</p>
<ul>
<li><code>user_agent</code>: Parsed data from the <code>User-Agent</code> header.</li>
<li><code>referer</code>: Parsed data from the <code>Referer</code> header.</li>
<li><code>crawl_refer_ratio</code>: Ratio of HTML page crawl requests to HTML page referrals by platform.</li>
</ul>
<h4 id="2025-07-01-radar-bots-insights-broader-bot-insights">Broader bot insights</h4>
<p>In addition to crawler-specific insights, Radar now provides a broader set of bot endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bots/"><code>/bots/</code></a>: Lists all bots.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/get/"><code>/bots/{bot_slug}</code></a>: Returns detailed metadata for a specific bot.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/timeseries/"><code>/bots/timeseries</code></a>: Time-series data for bot activity.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/summary/"><code>/bots/summary/{dimension}</code></a>: Returns an overview of bot HTTP request distributions across key dimensions.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/timeseries_groups/"><code>/bots/timeseries_groups/{dimension}</code></a>: Provides time-series data on bot request distributions across the same dimensions.</li>
</ul>
<p>These endpoints support filtering and breakdowns by:</p>
<ul>
<li><code>bot</code>: Bot name.</li>
<li><code>bot_operator</code>: The organization or entity operating the bot.</li>
<li><code>bot_category</code>: Classification of bot type.</li>
</ul>
<p>The previously available <code>verified_bots</code> endpoints have now been deprecated in favor of this set of bot insights APIs.
While current data still focuses on verified bots, we plan to expand support for unverified bot traffic in the future.</p>
<p>Learn more about the new Radar bot and crawler insights in our <a href="https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar">blog post</a>.</p>


<h2 id="log-explorer-is-ga"><a href="/changelog/post/2025-06-18-log-explorer-ga/">Log Explorer is GA</a></h2>
<p><em>2025-06-18</em></p>
<p><a href="/log-explorer/">Log Explorer</a> is now GA, providing native observability and forensics for traffic flowing through Cloudflare.</p>
<p>Search and analyze your logs, natively in the Cloudflare dashboard. These logs are also stored in Cloudflare's network, eliminating many of the costs associated with other log providers.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/log-explorer-dash.png" alt="Log Explorer dashboard" /></p>
<p>With Log Explorer, you can now:</p>
<ul>
<li><strong>Monitor security and performance issues with custom dashboards</strong> – use natural language to define charts for measuring response time, error rates, top statistics and more.</li>
<li><strong>Investigate and troubleshoot issues with Log Search</strong> – use data type-aware search filters or custom sql to investigate detailed logs.</li>
<li><strong>Save time and collaborate with saved queries</strong> – save Log Search queries for repeated use or sharing with other users in your account.</li>
<li><strong>Access Log Explorer at the account and zone level</strong> – easily find Log Explorer at the account and zone level for querying any dataset.</li>
</ul>
<p>For help getting started, refer to <a href="/log-explorer/">our documentation</a>.</p>


<h2 id="new-graphql-analytics-api-explorer-and-mcp-server"><a href="/changelog/post/2025-05-23-graphql-api-explorer/">New GraphQL Analytics API Explorer and MCP Server</a></h2>
<p><em>2025-05-23</em></p>
<p>We’ve launched two powerful new tools to make the GraphQL Analytics API more accessible:</p>
<h4 id="2025-05-23-graphql-api-explorer-graphql-api-explorer">GraphQL API Explorer</h4>
<p>The new <a href="https://graphql.cloudflare.com/explorer">GraphQL API Explorer</a> helps you build, test, and run queries directly in your browser. Features include:</p>
<ul>
<li>In-browser schema documentation to browse available datasets and fields</li>
<li>Interactive query editor with autocomplete and inline documentation</li>
<li>A &quot;Run in GraphQL API Explorer&quot; button to execute example queries from our docs</li>
<li>Seamless OAuth authentication — no manual setup required</li>
</ul>
<p><img src="/assets/upstream/images/changelog/analytics/graphql-api-explorer.png" alt="GraphQL API Explorer" /></p>
<h4 id="2025-05-23-graphql-api-explorer-graphql-model-context-protocol-mcp-server">GraphQL Model Context Protocol (MCP) Server</h4>
<p>MCP Servers let you use natural language tools like Claude to generate structured queries against your data. See our <a href="https://blog.cloudflare.com/thirteen-new-mcp-servers-from-cloudflare/">blog post</a> for details on how they work and which servers are available. The new <a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/graphql">GraphQL MCP server</a> helps you discover and generate useful queries for the GraphQL Analytics API. With this server, you can:</p>
<ul>
<li>Explore what data is available to query</li>
<li>Generate and refine queries using natural language, with one-click links to run them in the API Explorer</li>
<li>Build dashboards and visualizations from structured query outputs</li>
</ul>
<p>Example prompts include:</p>
<ul>
<li>“Show me HTTP traffic for the last 7 days for example.com”</li>
<li>“What GraphQL node returns firewall events?”</li>
<li>“Can you generate a link to the Cloudflare GraphQL API Explorer with a pre-populated query and variables?”</li>
</ul>
<p>We’re continuing to expand these tools, and your feedback helps shape what’s next. <a href="/analytics/graphql-api/">Explore the documentation</a> to learn more and get started.</p>


<h2 id="url-scanner-now-supports-geo-specific-scanning"><a href="/changelog/post/2025-05-07-url-scanner-geoegress/">URL Scanner now supports geo-specific scanning</a></h2>
<p><em>2025-05-08</em></p>
<p>Enterprise customers can now choose the geographic location from which a URL scan is performed — either via <a href="/security-center/investigate/">Security Center</a> in the Cloudflare dashboard or via the <a href="/api/resources/url_scanner/subresources/scans/methods/create/">URL Scanner API</a>.</p>
<p>This feature gives security teams greater insight into how a website behaves across different regions, helping uncover targeted, location-specific threats.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li>Location Picker: Select a location for the scan via <strong>Security Center → Investigate</strong> in the dashboard or through the API.</li>
<li>Region-aware scanning: Understand how content changes by location — useful for detecting regionally tailored attacks.</li>
<li>Default behavior: If no location is set, scans default to the user’s current geographic region.</li>
</ul>
<p>Learn more in the <a href="/security-center/">Security Center documentation</a>.</p>


<h2 id="custom-fields-raw-and-transformed-values-support"><a href="/changelog/post/2025-04-18-custom-fields-raw-transformed-values/">Custom fields raw and transformed values support</a></h2>
<p><em>2025-04-18</em></p>
<p>Custom Fields now support logging both <strong>raw and transformed values</strong> for request and response headers in the HTTP requests dataset.</p>
<p>These fields are configured per zone and apply to all Logpush jobs in that zone that include request headers, response headers. Each header can be logged in only one format—either raw or transformed—not both.</p>
<p>By default:</p>
<ul>
<li>Request headers are logged as raw values</li>
<li>Response headers are logged as transformed values</li>
</ul>
<p>These defaults can be overridden to suit your logging needs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17737.md")</aside>
<p>For more information refer to <a href="/logs/logpush/logpush-job/custom-fields/">Custom fields</a> documentation</p>


<h2 id="leaked-credentials-insights-in-cloudflare-radar"><a href="/changelog/post/2025-03-18-radar-leaked-credentials-insights/">Leaked Credentials Insights in Cloudflare Radar</a></h2>
<p><em>2025-03-18</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> has expanded its security insights, providing visibility into aggregate trends in authentication requests,
including the detection of leaked credentials through <a href="/waf/detections/leaked-credentials/">leaked credentials detection</a> scans.</p>
<p>We have now introduced the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/leaked_credentials/subresources/summary/"><code>/leaked_credential_checks/summary/{dimension}</code></a>: Retrieves summaries of HTTP authentication requests distribution across two different dimensions.</li>
<li><a href="/api/resources/radar/subresources/leaked_credentials/subresources/timeseries_groups/"><code>/leaked_credential_checks/timeseries_groups/{dimension}</code></a>: Retrieves timeseries data for HTTP authentication requests distribution across two different dimensions.</li>
</ul>
<p>The following dimensions are available, displaying the distribution of HTTP authentication requests based on:</p>
<ul>
<li><code>compromised</code>: Credential status (clean vs. compromised).</li>
<li><code>bot_class</code>: <a href="/radar/concepts/bot-classes">Bot class</a> (human vs. bot).</li>
</ul>
<p>Dive deeper into leaked credential detection in this <a href="https://blog.cloudflare.com/password-reuse-rampant-half-user-logins-compromised/">blog post</a> and learn more about the expanded Radar security insights in our <a href="https://blog.cloudflare.com/cloudflare-radar-ddos-leaked-credentials-bots">blog post</a>.</p>


<h2 id="cloudflare-one-agent-now-supports-endpoint-monitoring"><a href="/changelog/post/2025-03-07-cloudflare-one-device-health-monitoring/">Cloudflare One Agent now supports Endpoint Monitoring</a></h2>
<p><em>2025-03-07</em></p>
<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device, network, and application performance across your Cloudflare SASE deployment. The latest release of the Cloudflare One agent (v2025.1.861) now includes device endpoint monitoring capabilities
to provide deeper visibility into end-user device performance which can be analyzed directly from the dashboard.</p>
<p>Device health metrics are now automatically collected, allowing administrators to:</p>
<ul>
<li>View the last network a user was connected to</li>
<li>Monitor CPU and RAM utilization on devices</li>
<li>Identify resource-intensive processes running on endpoints</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dex/cloudflare-one-agent-health-monitoring.gif" alt="Device endpoint monitoring dashboard" /></p>
<p>This feature complements existing DEX features like <a href="/cloudflare-one/insights/dex/tests/">synthetic application monitoring</a> and <a href="/cloudflare-one/insights/dex/tests/traceroute/">network path visualization</a>, creating a comprehensive troubleshooting workflow that connects application performance with device state.</p>
<p>For more details refer to our <a href="/cloudflare-one/insights/dex/">DEX</a> documentation.</p>


<h2 id="one-click-logpush-setup-with-r2-object-storage"><a href="/changelog/post/2025-03-06-oneclick-logpush/">One-click Logpush Setup with R2 Object Storage</a></h2>
<p><em>2025-03-06</em></p>
<p>We’ve streamlined the <a href="/logs/logpush/">Logpush</a> setup process by integrating R2 bucket creation directly into the Logpush workflow!</p>
<p>Now, you no longer need to navigate multiple pages to manually create an R2 bucket or copy credentials. With this update, you can seamlessly <strong>configure a Logpush job to R2 in just one click</strong>, reducing friction and making setup faster and easier.</p>
<p>This enhancement makes it easier for customers to adopt Logpush and R2.</p>
<p>For more details refer to our <a href="/logs/logpush/logpush-job/enable-destinations/r2/">Logs</a> documentation.</p>


<h2 id="dns-insights-in-cloudflare-radar"><a href="/changelog/post/2025-02-27-radar-dns-insights/">DNS Insights in Cloudflare Radar</a></h2>
<p><em>2025-02-27</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> has expanded its DNS insights, providing visibility into aggregated traffic and usage trends observed by our <a href="/1.1.1.1/">1.1.1.1</a> DNS resolver.
In addition to global, location, and ASN traffic trends, we are also providing perspectives on protocol usage, query/response characteristics, and DNSSEC usage.</p>
<p>Previously limited to the <a href="/api/resources/radar/subresources/dns/subresources/top/"><code>top</code></a> locations and ASes endpoints, we have now introduced the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/dns/methods/timeseries/"><code>/dns/timeseries</code></a>: Retrieves DNS query volume over time.</li>
<li><a href="/api/resources/radar/subresources/dns/subresources/summary/"><code>/dns/summary/{dimension}</code></a>: Retrieves summaries of DNS query distribution across ten different dimensions.</li>
<li><a href="/api/resources/radar/subresources/dns/subresources/timeseries_groups/"><code>/dns/timeseries_groups/{dimension}</code></a>: Retrieves timeseries data for DNS query distribution across ten different dimensions.</li>
</ul>
<p>For the <code>summary</code> and <code>timeseries_groups</code> endpoints, the following dimensions are available, displaying the distribution of DNS queries based on:</p>
<ul>
<li><code>cache_hit</code>: Cache status (hit vs. miss).</li>
<li><code>dnsssec</code>: DNSSEC support status (secure, insecure, invalid or other).</li>
<li><code>dnsssec_aware</code>: DNSSEC client awareness (aware vs. not-aware).</li>
<li><code>dnsssec_e2e</code>: End-to-end security (secure vs. insecure).</li>
<li><code>ip_version</code>: IP version (IPv4 vs. IPv6).</li>
<li><code>matching_answer</code>: Matching answer status (match vs. no-match).</li>
<li><code>protocol</code>: Transport protocol (UDP, TLS, HTTPS or TCP).</li>
<li><code>query_type</code>: Query type (<code>A</code>, <code>AAAA</code>, <code>PTR</code>, etc.).</li>
<li><code>response_code</code>: Response code (<code>NOERROR</code>, <code>NXDOMAIN</code>, <code>REFUSED</code>, etc.).</li>
<li><code>response_ttl</code>: Response TTL.</li>
</ul>
<p>Learn more about the new Radar DNS insights in our <a href="https://blog.cloudflare.com/new-dns-section-on-cloudflare-radar/">blog post</a>, and check out the <a href="https://radar.cloudflare.com/dns">new Radar page</a>.</p>


<h2 id="zaraz-moves-to-the-tag-management-category-in-the-cloudflare-dashboard"><a href="/changelog/post/2025-02-24-zaraz-dash-placement/">Zaraz moves to the “Tag Management” category in the Cloudflare dashboard</a></h2>
<p><em>2025-02-24</em></p>
<p><img src="/assets/upstream/images/zaraz/zaraz-account-level.jpg" alt="Zaraz at zone level to Tag management at account level" /></p>
<p>Previously, you could only configure Zaraz by going to each individual zone under your Cloudflare account. Now, if you’d like to get started with Zaraz or manage your existing configuration, you can navigate to the <a href="https://dash.cloudflare.com/?to=/:account/tag-management/zaraz">Tag Management</a> section on the Cloudflare dashboard – this will make it easier to compare and configure the same settings across multiple zones.</p>
<p>These changes will not alter any existing configuration or entitlements for zones you already have Zaraz enabled on. If you’d like to edit existing configurations, you can go to the <a href="https://dash.cloudflare.com/?to=/:account/tag-management/zaraz">Tag Setup</a> section of the dashboard, and select the zone you'd like to edit.</p>


<h2 id="expanded-ai-insights-in-cloudflare-radar"><a href="/changelog/post/2025-02-04-radar-ai-insights/">Expanded AI insights in Cloudflare Radar</a></h2>
<p><em>2025-02-04</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> has expanded its AI insights with new API endpoints for Internet services rankings, robots.txt analysis, and AI inference data.</p>
<h4 id="2025-02-04-radar-ai-insights-internet-services-ranking">Internet services ranking</h4>
<p>Radar now provides <a href="/radar/glossary/#internet-services-ranking">rankings for Internet services</a>, including Generative AI platforms, based on anonymized 1.1.1.1 resolver data.
Previously limited to the annual Year in Review, these insights are now available daily via the <a href="/api/resources/radar/subresources/ranking/subresources/internet_services/">API</a>, through the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ranking/subresources/internet_services/methods/top/"><code>/ranking/internet_services/top</code></a> show service popularity at a specific date.</li>
<li><a href="/api/resources/radar/subresources/ranking/subresources/internet_services/methods/timeseries_groups/"><code>/ranking/internet_services/timeseries_groups</code></a> track ranking trends over time.</li>
</ul>
<h4 id="2025-02-04-radar-ai-insights-robots-txt">Robots.txt</h4>
<p>Radar now analyzes <a href="/radar/glossary/#robotstxt">robots.txt</a> files from the top 10,000 domains, identifying AI bot access rules.
AI-focused user agents from <a href="https://github.com/ai-robots-txt/ai.robots.txt">ai.robots.txt</a> are categorized as:</p>
<ul>
<li><strong>Fully allowed/disallowed</strong> if directives apply to all paths (<code>*</code>).</li>
<li><strong>Partially allowed/disallowed</strong> if restrictions apply to specific paths.</li>
</ul>
<p>These insights are now available weekly via the <a href="/api/resources/radar/subresources/robots_txt/">API</a>, through the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/robots_txt/subresources/top/subresources/user_agents/methods/directive/"><code>/robots_txt/top/user_agents/directive</code></a> to get the top AI user agents by directive.</li>
<li><a href="/api/resources/radar/subresources/robots_txt/subresources/top/methods/domain_categories/"><code>/robots_txt/top/domain_categories</code></a> to get the top domain categories by robots.txt files.</li>
</ul>
<h4 id="2025-02-04-radar-ai-insights-workers-ai">Workers AI</h4>
<p>Radar now provides insights into public AI inference models from <a href="/workers-ai/">Workers AI</a>, tracking usage trends across <strong>models</strong> and <strong>tasks</strong>.
These insights are now available via the <a href="/api/resources/radar/subresources/ai/subresources/inference/">API</a>, through the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ai/subresources/inference/subresources/summary/"><code>/ai/inference/summary/{dimension}</code></a> to view aggregated <code>model</code> and <code>task</code> popularity.</li>
<li><a href="/api/resources/radar/subresources/ai/subresources/inference/subresources/timeseries_groups/"><code>/ai/inference/timeseries_groups/{dimension}</code></a> to track changes over time for <code>model</code> or <code>task</code>.</li>
</ul>
<p>Learn more about the new Radar AI insights in our <a href="https://blog.cloudflare.com/expanded-ai-insights-on-cloudflare-radar/">blog post</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/analytics/4/">Previous</a><span>Page 5 of 6</span><a class="pagination-next" rel="next" href="/changelog/product-group/analytics/6/">Next</a></nav>
