---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/radar/2/
  description: '2025-10-27'
  full_title: radar changelog - page 2 | Cloudflare Docs
  head_html: <title>radar changelog - page 2 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-10-27"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/radar/2/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="radar changelog - page 2"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-10-27"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/radar/2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/radar/2/#page","headline":"radar changelog - page 2 | Cloudflare Docs","description":"2025-10-27","url":"https://developers.cloudflare.com/changelog/product/radar/2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/radar/2/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="tld-insights-in-cloudflare-radar"><a href="/changelog/post/2025-10-27-radar-tld-insights/">TLD Insights in Cloudflare Radar</a></h2>
<p><em>2025-10-27</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now introduces Top-Level Domain (TLD) insights, providing visibility into popularity based on the DNS magnitude metric, detailed TLD information including its type, manager, DNSSEC support, RDAP support, and WHOIS data, and trends such as DNS query volume and geographic distribution observed by the <a href="/1.1.1.1/">1.1.1.1</a> DNS resolver.</p>
<p>The following dimensions were added to the Radar DNS API, specifically, to the <a href="/api/resources/radar/subresources/dns/methods/summary_v2/"><code>/dns/summary/{dimension}</code></a> and <a href="/api/resources/radar/subresources/dns/methods/timeseries_groups_v2/"><code>/dns/timeseries_groups/{dimension}</code></a> endpoints:</p>
<ul>
<li><code>tld</code>: Top-level domain extracted from DNS queries; can also be used as a filter.</li>
<li><code>tld_dns_magnitude</code>: Top-level domain ranking by <a href="/radar/glossary#dns-magnitude">DNS magnitude</a>.</li>
</ul>
<p>And the following endpoints were added:</p>
<ul>
<li><a href="/api/resources/radar/subresources/tlds/methods/list/"><code>/tlds</code></a> - Lists all TLDs.</li>
<li><a href="/api/resources/radar/subresources/tlds/methods/get/"><code>/tlds/{tld}</code></a> - Retrieves information about a specific TLD.</li>
</ul>
<p><img src="/assets/upstream/images/radar/tld-ranking-by-dns-magnitude.png" alt="Screenshot of the TLD ranking by DNS magnitude" /></p>
<p>Learn more about the new Radar DNS insights in our <a href="https://blog.cloudflare.com/introducing-tld-insights-on-cloudflare-radar/">blog post</a>, and check out the <a href="https://radar.cloudflare.com/tlds">new Radar page</a>.</p>


<h2 id="expanded-ct-log-activity-insights-on-cloudflare-radar"><a href="/changelog/post/2025-10-09-radar-ct-log-activity-insights/">Expanded CT log activity insights on Cloudflare Radar</a></h2>
<p><em>2025-10-09</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> has expanded its Certificate Transparency (CT) log insights with new stats that provide greater visibility into log activity:</p>
<ul>
<li><strong>Log growth rate</strong>: The average throughput of the CT log over the past 7 days, measured in certificates per hour.</li>
<li><strong>Included certificate count</strong>: The total number of certificates already included in this CT log.</li>
<li><strong>Eligible-for-inclusion certificate count</strong>: The number of certificates eligible for inclusion in this log but not yet included. This metric is based on certificates signed by trusted root CAs within the log’s accepted date range.</li>
<li><strong>Last update</strong>: The timestamp of the most recent update to the CT log.</li>
</ul>
<p>These new statistics have been added to the response of the <a href="/api/resources/radar/subresources/ct/subresources/logs/methods/get/">Get Certificate Log Details</a> API endpoint, and are displayed on the <a href="https://radar.cloudflare.com/certificate-transparency/log/nimbus2025#log-activity">CT log information page</a>.</p>
<p><img src="/assets/upstream/images/radar/ct-log-activity.png" alt="Screenshot of the CT log activity card on the CT log information page" /></p>


<h2 id="browser-support-detection-for-pq-encryption-on-cloudflare-radar"><a href="/changelog/post/2025-10-06-radar-pq-encryption-test/">Browser Support Detection for PQ Encryption on Cloudflare Radar</a></h2>
<p><em>2025-10-06</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now includes browser detection for Post-quantum (PQ) encryption.
The <a href="https://radar.cloudflare.com/adoption-and-usage#post-quantum-encryption">Post-quantum encryption card</a> now checks whether a user’s browser supports post-quantum encryption.
If support is detected, information about the key agreement in use is displayed.</p>
<p><img src="/assets/upstream/images/radar/pq-encryption-test.png" alt="Screenshot of the PQ encryption browser support test on the Adoption &amp; Usage page" /></p>


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


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/radar/">Previous</a><span>Page 2 of 2</span></nav>
