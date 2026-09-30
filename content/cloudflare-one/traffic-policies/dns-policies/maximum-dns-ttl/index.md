<p>Set a maximum time-to-live (TTL) for DNS responses returned by Gateway. When an upstream DNS record has a TTL that exceeds the configured maximum, Gateway caps the TTL to the value you specify. Lower values ensure that DNS policy changes - such as blocking a newly identified malicious domain - take effect faster across all clients, at the cost of increased query volume from reduced caching.</p>
<p>The maximum TTL cap only applies to upstream-derived DNS answers for allowed queries. Gateway-generated responses (blocks, overrides, safe-search answers) are not affected because they already use a short default TTL.</p>
<h2 id="how-it-works">How it works</h2>
<p>Gateway applies a tiered TTL hierarchy. The most specific setting takes precedence:</p>
<ol>
<li>If the DNS location has a per-location override, that value is used.</li>
<li>If the location inherits its setting, the account-level maximum TTL is used.</li>
<li>If no maximum TTL is configured at any level, upstream TTL values pass through unchanged.</li>
</ol>
<p>The valid range for any maximum TTL value is <strong>60 to 36,000 seconds</strong> (1 minute to 10 hours).</p>
<h2 id="configure-the-account-level-maximum-ttl">Configure the account-level maximum TTL</h2>
<p>The account-level setting applies to all DNS locations that do not have a per-location override.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6647.md")
</div></div>
<h2 id="configure-a-per-location-maximum-ttl">Configure a per-location maximum TTL</h2>
<p>Each <a href="/cloudflare-one/networks/resolvers-proxies/">DNS location</a> can override the account-level setting. The per-location setting supports three modes:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Respect account-level setting</strong> (<code>inherit</code>)</td>
<td>Uses whatever value is configured at the account level. This is the default for new locations.</td>
</tr>
<tr>
<td><strong>Do not set max value</strong> (<code>disabled</code>)</td>
<td>Disables the maximum TTL cap for this location, even if one is configured at the account level. Upstream TTL values pass through unchanged.</td>
</tr>
<tr>
<td><strong>Custom</strong> (<code>override</code>)</td>
<td>Sets a location-specific maximum TTL that overrides the account-level value. Requires a <code>ttl_secs</code> value between 60 and 36,000.</td>
</tr>
</tbody>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6650.md")
</div></div>
<h2 id="dns-log-fields">DNS log fields</h2>
<p>When a maximum TTL is active, two additional fields appear in Gateway DNS logs:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>upstream_record_ttls</code></td>
<td>The original TTL values from the upstream DNS response, before any cap was applied.</td>
</tr>
<tr>
<td><code>applied_max_ttl</code></td>
<td>The maximum TTL value that Gateway applied to the response. If no cap was applied, this field is absent.</td>
</tr>
</tbody>
</table>
<p>These fields are visible in the DNS logs column picker under the <strong>DNS Response Details</strong> group in the dashboard, and in Logpush datasets.</p>
