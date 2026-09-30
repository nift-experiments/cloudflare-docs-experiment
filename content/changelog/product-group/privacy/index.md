<h1 id="changelog">Changelog</h1>

<h2 id="improved-doh-json-formatting-for-additional-record-types"><a href="/changelog/post/2026-07-28-improved-record-display-format/">Improved DoH JSON formatting for additional record types</a></h2>
<p><em>2026-07-28</em></p>
<p>Cloudflare is rolling out updated formatting for the <code>data</code> field in the 1.1.1.1 <a href="/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-json/">DoH JSON API</a> (<code>application/dns-json</code>). During the roll out responses may use either the old or new format.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17613.md")</aside>
<h4 id="2026-07-28-improved-record-display-format-human-readable-display-for-additional-record-types">Human-readable display for additional record types</h4>
<p>Several record types previously returned their <code>data</code> field in <a href="https://datatracker.ietf.org/doc/html/rfc3597">RFC 3597</a> generic hex encoding (<code>\# &lt;length&gt; &lt;hex&gt;</code>). These now use standard presentation format:</p>
<pre><code class="language-txt">CAA:        0 issue &quot;letsencrypt.org&quot;&#10;NAPTR:      100 10 &quot;s&quot; &quot;SIP+D2U&quot; &quot;&quot; _sip._udp.example.com.&#10;RP:         admin.example.com. txt.example.com.&#10;IPSECKEY:   10 1 2 192.0.2.1 AwEA...&#10;SVCB:       1 target.example.com. alpn=h2&#10;HTTPS:      1 . alpn=h3,h2 ipv4hint=192.0.2.1&#10;TLSA:       3 1 1 aabbccdd...&#10;SSHFP:      1 2 aabbccdd...&#10;OPENPGPKEY: AwEA...&#10;</code></pre>
<h4 id="2026-07-28-improved-record-display-format-numeric-dnssec-algorithm-identifiers">Numeric DNSSEC algorithm identifiers</h4>
<p>DNSSEC-related records now use numeric algorithm identifiers as defined in <a href="https://datatracker.ietf.org/doc/html/rfc4034">RFC 4034</a> instead of mnemonic names. This affects <code>RRSIG</code>, <code>DS</code>, <code>CDS</code>, <code>DNSKEY</code>, and <code>CDNSKEY</code> records. For example, <code>RSASHA256</code> becomes <code>8</code>, <code>ECDSAP256SHA256</code> becomes <code>13</code>, and <code>ED25519</code> becomes <code>15</code>. DS digest types also change from mnemonic to numeric: <code>SHA-256</code> becomes <code>2</code>.</p>
<pre><code class="language-txt">RRSIG:  A RSASHA256 2 300 ...&#10;DS:     12345 RSASHA256 SHA-256 aabb...&#10;DNSKEY: 257 3 RSASHA256 AwEA...&#10;</code></pre>
<pre><code class="language-txt">RRSIG:  A 8 2 300 ...&#10;DS:     12345 8 2 aabb...&#10;DNSKEY: 257 3 8 AwEA...&#10;</code></pre>
<h4 id="2026-07-28-improved-record-display-format-other-formatting-changes">Other formatting changes</h4>
<p><code>HINFO</code> character-strings are now individually quoted to remove ambiguity when values contain spaces:</p>
<pre><code class="language-txt">&quot;data&quot;: &quot;Intel Xeon Linux&quot;&#10;</code></pre>
<pre><code class="language-txt">&quot;data&quot;: &quot;\&quot;Intel Xeon\&quot; \&quot;Linux\&quot;&quot;&#10;</code></pre>


<h2 id="privacy-proxy-metrics-now-available-via-graphql-analytics-api"><a href="/changelog/post/2026-04-15-graphql-analytics-api/">Privacy Proxy metrics now available via GraphQL Analytics API</a></h2>
<p><em>2026-04-15</em></p>
<p>Privacy Proxy metrics are now queryable through Cloudflare's <a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API</a>, the new default method for accessing Privacy Proxy observability data. All metrics are available through a single endpoint:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/graphql \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;query&quot;: &quot;{ viewer { accounts(filter: { accountTag: $accountTag }) { privacyProxyRequestMetricsAdaptiveGroups(filter: { date_geq: $startDate, date_leq: $endDate }, limit: 10000, orderBy: [date_ASC]) { count dimensions { date } } } } }&quot;,&#10;    &quot;variables&quot;: {&#10;      &quot;accountTag&quot;: &quot;&lt;YOUR_ACCOUNT_TAG&gt;&quot;,&#10;      &quot;startDate&quot;: &quot;2026-04-04&quot;,&#10;      &quot;endDate&quot;: &quot;2026-04-06&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-04-15-graphql-analytics-api-available-nodes">Available nodes</h4>
<p>Four GraphQL nodes are now live, providing aggregate metrics across all key dimensions of your Privacy Proxy deployment:</p>
<ul>
<li><strong><code>privacyProxyRequestMetricsAdaptiveGroups</code></strong> — Request volume, error rates, status codes, and proxy status breakdowns.</li>
<li><strong><code>privacyProxyIngressConnMetricsAdaptiveGroups</code></strong> — Client-to-proxy connection counts, bytes transferred, and latency percentiles.</li>
<li><strong><code>privacyProxyEgressConnMetricsAdaptiveGroups</code></strong> — Proxy-to-origin connection counts, bytes transferred, and latency percentiles.</li>
<li><strong><code>privacyProxyAuthMetricsAdaptiveGroups</code></strong> — Authentication attempt counts by method and result.</li>
</ul>
<p>All nodes support filtering by time, data center (<code>coloCode</code>), and endpoint, with additional node-specific dimensions such as transport protocol and authentication method.</p>
<h4 id="2026-04-15-graphql-analytics-api-what-this-means-for-existing-opentelemetry-users">What this means for existing OpenTelemetry users</h4>
<p>OpenTelemetry-based metrics export remains available. The GraphQL Analytics API is now the recommended default method — a plug-and-play method that requires no collector infrastructure, saving engineering overhead.</p>
<h4 id="2026-04-15-graphql-analytics-api-learn-more">Learn more</h4>
<ul>
<li><a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API for Privacy Proxy</a></li>
<li><a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API — getting started</a></li>
</ul>


<h2 id="zaraz-moves-to-the-tag-management-category-in-the-cloudflare-dashboard"><a href="/changelog/post/2025-02-24-zaraz-dash-placement/">Zaraz moves to the “Tag Management” category in the Cloudflare dashboard</a></h2>
<p><em>2025-02-24</em></p>
<p><img src="/assets/upstream/images/zaraz/zaraz-account-level.jpg" alt="Zaraz at zone level to Tag management at account level" /></p>
<p>Previously, you could only configure Zaraz by going to each individual zone under your Cloudflare account. Now, if you’d like to get started with Zaraz or manage your existing configuration, you can navigate to the <a href="https://dash.cloudflare.com/?to=/:account/tag-management/zaraz">Tag Management</a> section on the Cloudflare dashboard – this will make it easier to compare and configure the same settings across multiple zones.</p>
<p>These changes will not alter any existing configuration or entitlements for zones you already have Zaraz enabled on. If you’d like to edit existing configurations, you can go to the <a href="https://dash.cloudflare.com/?to=/:account/tag-management/zaraz">Tag Setup</a> section of the dashboard, and select the zone you'd like to edit.</p>



