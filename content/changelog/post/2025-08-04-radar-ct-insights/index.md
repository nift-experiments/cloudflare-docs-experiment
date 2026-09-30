<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 6, 2025</time><h2 id="post-title">Certificate Transparency Insights in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now introduces Certificate Transparency (CT) insights, providing visibility into certificate issuance trends based on Certificate Transparency logs currently monitored by Cloudflare.</p>
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
</div></article></div>
