<p>This page describes different DNSSEC states and how they relate to the responses you get from the <a href="/api/resources/dns/subresources/dnssec/methods/get/">DNSSEC details API endpoint</a>.</p>
<table>
<thead>
<tr>
<th>State</th>
<th>API response</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pending</td>
<td><code>&quot;status&quot;:&quot;pending&quot;</code><br /> <code>&quot;modified_on&quot;:&lt;TIME_STAMP&gt;</code></td>
<td>DNSSEC has been enabled but the Cloudflare DS record has not been added at the registrar.</td>
</tr>
<tr>
<td>Active</td>
<td><code>&quot;status&quot;:&quot;active&quot;</code><br /> <code>&quot;modified_on&quot;:&lt;TIME_STAMP&gt;</code></td>
<td>DNSSEC has been enabled and the Cloudflare DS record is present at the registrar.</td>
</tr>
<tr>
<td>Pending-disabled</td>
<td><code>&quot;status&quot;:&quot;pending-disabled&quot;</code><br /> <code>&quot;modified_on&quot;:&lt;TIME_STAMP&gt;</code></td>
<td>DNSSEC has been disabled but the Cloudflare DS record is still added at the registrar.</td>
</tr>
<tr>
<td>Disabled</td>
<td><code>&quot;status&quot;:&quot;disabled&quot;</code><br /> <code>&quot;modified_on&quot;:&lt;TIME_STAMP&gt;</code></td>
<td>DNSSEC has been disabled and the Cloudflare DS record has been removed from the registrar.</td>
</tr>
<tr>
<td>Deleted</td>
<td><code>&quot;status&quot;:&quot;disabled&quot;</code><br /> <code>&quot;modified_on&quot;: null</code></td>
<td>DNSSEC has never been enabled for the zone or DNSSEC has been disabled and then deleted using the <a href="/api/resources/dns/subresources/dnssec/methods/delete/">Delete DNSSEC records endpoint</a>.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7693.md")
</aside>
<p>In both <code>pending</code> and <code>active</code> states, Cloudflare signs the zone and responds with RRSIG, NSEC, DNSKEY, CDS, and CDNSKEY record types.</p>
<p>In <code>pending-disabled</code> and <code>disabled</code> states, Cloudflare still signs the zone and serves RRSIG, NSEC, and DNSKEY record types, but the CDS and CDNSKEY records are set to zero (<a href="https://www.rfc-editor.org/rfc/rfc8078.html#section-4">RFC 8078</a>), signaling to the registrar that DNSSEC should be disabled.</p>
<p>In <code>deleted</code> state, Cloudflare does <strong>not</strong> sign the zone and does <strong>not</strong> respond with RRSIG, NSEC, DNSKEY, CDS, and CDNSKEY record types.</p>
<p>Refer to <a href="https://www.cloudflare.com/dns/dnssec/how-dnssec-works/">How DNSSEC works</a> to learn more about the authentication process and records involved.</p>
