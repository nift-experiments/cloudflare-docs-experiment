<p>Refer to the sections below for an overview of some technical concepts and how they apply to Cloudflare DNSSEC. For broader content on DNSSEC, refer to <a href="https://www.cloudflare.com/dns/dnssec/how-dnssec-works/">How DNSSEC works</a>.</p>
<h2 id="chain-of-trust">Chain of trust</h2>
<p>DNSSEC validation follows a chain of trust from the root DNS servers to your zone:</p>
<ol>
<li>A resolver queries your parent registry (for example, <code>.com</code>) for your DS record.</li>
<li>The DS record contains a hash of your Key Signing Key (KSK).</li>
<li>The resolver expects all Zone Signing Keys (ZSK) to be signed by that specific KSK.</li>
<li>If Cloudflare uses a different KSK, validation fails when resolvers query Cloudflare nameservers.</li>
</ol>
<p>This is why you cannot simply keep your existing DS record when migrating to Cloudflare. The cryptographic chain of trust requires either:</p>
<ul>
<li><a href="/dns/dnssec/">Disabling DNSSEC</a> before migration and re-enabling it on Cloudflare</li>
<li>Using the <a href="/dns/dnssec/multi-signer-dnssec/about/">multi-signer DNSSEC</a> approach to coordinate keys between providers.</li>
</ul>
<hr />
<h2 id="automatic-ds-record-updates">Automatic DS record updates</h2>
<p>When you enable DNSSEC, Cloudflare automatically publishes <strong>CDS</strong> (Child Delegation Signer) and <strong>CDNSKEY</strong> (Child DNSKEY) records in your zone. These records automate the chain of trust management between your domain and the Top-Level Domain registry.</p>
<table>
<thead>
<tr>
<th>Record</th>
<th>Purpose</th>
<th>Contents</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>CDS</strong></td>
<td>High-level instruction</td>
<td>A hashed version of the public key (same data as a DS record)</td>
</tr>
<tr>
<td><strong>CDNSKEY</strong></td>
<td>Public key instruction</td>
<td>The full public Key Signing Key (KSK) for the parent to generate its own DS record</td>
</tr>
</tbody>
</table>
<p>Registrars that support <a href="https://www.rfc-editor.org/rfc/rfc8078.html">RFC 8078</a> periodically scan your domain for these records and automatically update the DS record at the registry level. This eliminates manual DS record management and ensures seamless key rollovers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7676.md")
</aside>
<hr />
<h2 id="dnskey-flags">DNSKEY flags</h2>
<ul>
<li><strong>ZSKs (Zone Signing Keys)</strong>: flag <code>256</code></li>
<li><strong>KSKs (Key Signing Keys)</strong>: flag <code>257</code></li>
</ul>
