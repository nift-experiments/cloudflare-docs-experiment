<p><em>Last updated March 27, 2024</em></p>
<h2 id="cloudflare-s-commitment-to-privacy-1-1-1-1-public-dns-resolver">Cloudflare's commitment to privacy: 1.1.1.1 Public DNS Resolver</h2>
<p>The 1.1.1.1 public DNS resolver is governed by our <a href="https://www.cloudflare.com/privacypolicy/">Privacy Policy</a>. This document provides additional details on our collection, use, and disclosure of the information collected from the 1.1.1.1 public DNS resolver.</p>
<hr />
<p>Nearly everything on the Internet starts with a DNS request. DNS is the Internet's directory. Select a link, open an app, send an email, and the first thing your device does is ask a DNS resolver: where can I find this?</p>
<p>By default, most devices use a DNS resolver provided by the Internet service provider (ISP). Some ISPs and third-party DNS providers log your queries, sell data about your Internet activity, or use it to target you with ads. DNS queries are also typically sent in plaintext, which means anyone on the network path between your device and the resolver can see every site you visit and every app you use — even if the content itself is encrypted.</p>
<p>Cloudflare built the 1.1.1.1 public DNS resolver to address these problems. In partnership with APNIC, Cloudflare operates 1.1.1.1 as a recursive DNS service designed for privacy and security. DNS requests to 1.1.1.1 can be sent over an <a href="/1.1.1.1/encryption/">encrypted channel</a>, significantly decreasing the odds of unwanted spying or man-in-the-middle attacks.</p>
<p>The 1.1.1.1 public DNS resolver was designed for privacy first. Cloudflare commits to the following:</p>
<ol>
<li>Cloudflare will not sell or share Public Resolver users' personal data with third parties or use personal data from the Public Resolver to target any user with advertisements.</li>
<li>Cloudflare will only retain or use what is being asked, not information that will identify who is asking it. Except for randomly sampled network packets captured from at most 0.05% of all traffic sent to Cloudflare's network infrastructure, Cloudflare will not retain the source IP from DNS queries to the Public Resolver in non-volatile storage. These randomly sampled packets are solely used for network troubleshooting and DoS mitigation purposes.</li>
<li>A Public Resolver user's IP address (referred to as the client or source IP address) will not be stored in non-volatile storage. Cloudflare will anonymize source IP addresses via IP truncation methods (last octet for IPv4 and last 80 bits for IPv6). Cloudflare will delete the truncated IP address within 25 hours.</li>
<li>Cloudflare will retain only the limited transaction and debug log data (&quot;Public Resolver Logs&quot;) set forth below, for the legitimate operation of our Public Resolver and research purposes, and Cloudflare will delete the Public Resolver Logs within 25 hours.</li>
<li>Cloudflare will not share the Public Resolver Logs with any third parties except for APNIC pursuant to a Research Cooperative Agreement. APNIC will only have limited access to query the anonymized data in the Public Resolver Logs and conduct research related to the operation of the DNS system.</li>
</ol>
<p>Cloudflare has taken technical steps to ensure that we cannot retain our user's information.</p>
<p>We have also retained one of the top four accounting firms to audit our practices and publish a public report confirming we are doing what we said we would. The report is available on the <a href="https://www.cloudflare.com/trust-hub/compliance-resources/">Certifications and compliance resources</a> page.</p>
<h2 id="limited-data-sharing-with-apnic">Limited data sharing with APNIC</h2>
<p>Cloudflare has partnered with <a href="https://labs.apnic.net/?p=1127">APNIC Labs</a>, the regional Internet registry for the Asia-Pacific region, which provided the 1.1.1.1 IP address for use as a public DNS resolver. As part of its mission to ensure a global, open, and secure Internet, APNIC conducts research about the functioning and governance of the Internet, which it publishes at <a href="http://www.apnic.net">www.apnic.net</a>.</p>
<p>Cloudflare has agreed to provide APNIC with access to some of the anonymized data that Cloudflare collects through the Cloudflare Public DNS Resolver. APNIC can access query names, query types, resolver location, and other metadata via a Cloudflare API. This allows APNIC to study topics like the volume of DDoS attacks on the Internet and adoption of IPv6.</p>
<p>APNIC Labs uses this data for non-profit operational research. As part of Cloudflare's commitment to privacy, Cloudflare will not provide APNIC with any access to the IP address associated with a client.</p>
<p>Aside from APNIC, Cloudflare will not share the Public Resolver Logs with any third party.</p>
<h2 id="data-in-public-resolver-logs">Data in public resolver logs</h2>
<p>The Public Resolver Logs consist of the following fields:</p>
<ul>
<li>answerData type</li>
<li>answerData</li>
<li>coloID (unique Cloudflare data center ID)</li>
<li>date</li>
<li>dateTime</li>
<li>dstIPVersion</li>
<li>dstIPv6</li>
<li>dstIPv4</li>
<li>dstPort</li>
<li>ede</li>
<li>ednsVersion</li>
<li>ednsPayload</li>
<li>ednsNsid</li>
<li>feature.uid</li>
<li>feature.value</li>
<li>metalId (unique Cloudflare data center ID)</li>
<li>ns ip</li>
<li>ns name</li>
<li>protocol</li>
<li>queryName</li>
<li>queryType</li>
<li>queryClass</li>
<li>queryRd</li>
<li>queryDo</li>
<li>querySize</li>
<li>queryEdns</li>
<li>queryCd</li>
<li>responseType</li>
<li>responseCode</li>
<li>responseSize</li>
<li>responseCount</li>
<li>responseTimeMs</li>
<li>responseCached</li>
<li>responseMinTTL</li>
<li>reused</li>
<li>srcAsNum</li>
<li>srcCountry</li>
<li>srcIPVersion</li>
<li>validationState</li>
</ul>
<p>Additionally, the resolver performs outgoing queries to authoritative nameservers in the DNS hierarchy. These queries are logged in subrequest fields and are used for the operation and debugging of the Public DNS Resolver service.</p>
<p>The following subrequest data is included in the Public Resolver Logs:</p>
<ul>
<li>subrequest.ipv6 (authoritative nameserver)</li>
<li>subrequest.ipv4 (authoritative nameserver)</li>
<li>subrequest.protocol</li>
<li>subrequest.durationMs</li>
<li>subrequest.queryName</li>
<li>subrequest.queryType</li>
<li>subrequest.responseCode</li>
<li>subrequest.responseCount</li>
<li>subrequest.recordType</li>
<li>subrequest.recordData</li>
<li>subrequest.error</li>
</ul>
<p>Except for limited sampled data from the Public Resolver Logs (which do not include truncated IP addresses) used to generate the aggregations described below, all Public Resolver Logs are deleted within 25 hours.</p>
<p>Cloudflare may produce the following aggregations:</p>
<ul>
<li>Total number of queries with different protocol settings (for example, TCP/UDP/DNSSEC) by Cloudflare data center.</li>
<li>Response code and response time quantiles with different protocol settings by Cloudflare data center.</li>
<li>Total number of requests processed by Cloudflare data center.</li>
<li>Aggregate list of all domain names requested, with aggregate request count and timestamp of first request by region.</li>
<li>Number of unique clients, queries over IPv4, queries over IPv6, queries with the RD bit set, queries asking for DNSSEC, number of bogus, valid, and invalid DNSSEC answers, queries by type, number of answers with each response code, response time quantiles (for example, 50th percentile), response TTL, and number of cached answers per minute, per day, per protocol (HTTPS/UDP/TCP/TLS), per region, per Cloudflare data center, and per Autonomous System Number.</li>
<li>Number of queries, number of queries with EDNS, number of bytes and time in answers quantiles (for example, 50th percentile) by day, month, Cloudflare data center, and by IPv4 versus IPv6.</li>
<li>Number of queries, response codes and response code quantiles (for example, 50th percentile) by day, region, name, and type.</li>
</ul>
<p>Cloudflare may store this aggregated data indefinitely to power Cloudflare Radar and to improve Cloudflare services, such as enhancing the overall performance of the Cloudflare Resolver and identifying security threats.</p>
<h2 id="what-about-requests-for-content-blocking">What about requests for content blocking?</h2>
<p>Cloudflare does not block or filter any content through the 1.1.1.1 Public DNS Resolver, which is designed for direct, fast DNS resolution, not for blocking or filtering content. Cloudflare does block and filter malware and adult content through 1.1.1.1 for Families, which is designed to help individuals protect their home networks.</p>
<p>In general, Cloudflare views government or civil requests to block content at the DNS level as ineffective, inefficient, and overboard. Because such a block would apply globally to all users of the resolver, regardless of where they are located, it would affect end users outside of the blocking government's jurisdiction. A government request to block content through a globally available public recursive resolver like the 1.1.1.1 Public DNS Resolver and 1.1.1.1 for Families should therefore be evaluated as a request to block content globally.</p>
<p>Given the broad extraterritorial effect, if Cloudflare were to receive written requests from law enforcement and government agencies to block access to domains or content through the 1.1.1.1 Public DNS Resolver or to block access to domains or content through 1.1.1.1 for Families that is outside the scope of the filtering in that product, Cloudflare would pursue its legal remedies before complying with such a request. We also commit to documenting any government request to block access in our semi-annual transparency report, unless legally prohibited from doing so.</p>
