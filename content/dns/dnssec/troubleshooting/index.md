<p>Learn more about how to troubleshoot issues with DNSSEC.</p>
<h2 id="test-dnssec-with-dig">Test DNSSEC with Dig</h2>
<p><code>Dig</code> is a command-line tool to query a nameserver for DNS records.</p>
<p>For instance, <code>dig</code> can ask a DNS resolver for the IP address of <code>www.cloudflare.com</code>:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/7680.md")
</div>
<p>Use <code>+dnssec</code> to verify that the DNS records are signed:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/7681.md")
</div>
<p><code>Dig</code> can also retrieve the public key used to verify the DNS record, <code>DNSKEY</code>:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-2">Example</h3>
@markup("md", "content/.markup/bodies/7682.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7679.md")
</aside>
<p>When not using the <code>+short</code> option with <code>dig</code>, a DNS response is DNSSEC authenticated if the <code>ad</code> flag appears in the response header:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-3">Example</h3>
@markup("md", "content/.markup/bodies/7683.md")
</div>
<hr />
<h2 id="troubleshoot-dnssec-validation-using-dnsviz">Troubleshoot DNSSEC validation using DNSViz</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7678.md")
</aside>
<p>To visualize and discover potential issues with DNSSEC:</p>
<ol>
<li>Go to <a href="https://dnsviz.net/">https://dnsviz.net/</a>.</li>
<li>Enter a domain name in the text field that appears.</li>
<li>If DNSViz has never analyzed the site before, select <strong>Analyze</strong>.</li>
<li>If the site has been analyzed by DNSViz before, select <strong>Update Now</strong>.</li>
</ol>
<h3 id="example-with-missing-or-incorrect-rrsig-record-on-authoritative-nameserver">Example with missing or incorrect RRSIG record on authoritative nameserver</h3>
<p>Below is an example of how dnsviz.net will display incorrect delegation when no valid DNSKEY records are provided by the authoritative nameserver to match the DS record published by the TLD nameserver:</p>
<p><img src="/assets/upstream/images/support/troubleshoot_dnssec-example_no_rrsig.png" alt="Incorrect delegation when no valid DNSKEY records are provided" /></p>
<hr />
<h2 id="view-the-dnssec-chain-of-trust-with-dig">View the DNSSEC chain of trust with Dig</h2>
<p>Full verification of domain signatures (for example, <code>cloudflare.com</code>) involves verifying the key signing key at the top-level domain (for example, <code>.com</code>).</p>
<p>Similar verification is then performed by checking the key-signing key of <code>.com</code> at the root server level. DNSSEC root keys are distributed to DNS clients to complete the chain of trust.</p>
<p>When DNSSEC is enabled, a <code>DS</code> record is required at the registrar's DNS. The <code>DS</code> record contains a hash of the public key signing key as well as metadata about the key.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-4">Example</h3>
@markup("md", "content/.markup/bodies/7684.md")
</div>
<p>An easier alternative to manually running the steps above is to use the third-party tool <a href="#troubleshoot-dnssec-validation-using-dnsviz">DNSViz</a>.</p>
<hr />
<h2 id="troubleshoot-dnssec-validation-with-dig">Troubleshoot DNSSEC validation with Dig</h2>
<p>Issues occur if authoritative DNS providers are changed without updating or removing old DNSSEC records at the registrar:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-5">Example</h3>
@markup("md", "content/.markup/bodies/7685.md")
</div>
<hr />
<h2 id="delete-remaining-dnskey-records-after-disabling-dnssec">Delete remaining DNSKEY records after disabling DNSSEC</h2>
<p>After disabling DNSSEC, DNSKEY records continue to appear in DNS queries and zone transfers. In the <code>disabled</code> state, Cloudflare still signs the zone and serves RRSIG, NSEC, and DNSKEY records. This is expected behavior and <strong>not a misconfiguration or error</strong>. Refer to <a href="/dns/dnssec/dnssec-states/">DNSSEC states</a> and <a href="https://www.rfc-editor.org/rfc/rfc8078.html#section-4">RFC 8078</a> for details.</p>
<p>However, some security vendors or audit tools may flag these DNSKEY records as problematic, reporting &quot;DNSKEY record found but no DS record found&quot; with a security outcome of &quot;Provably Insecure&quot;. You can remove the DNSKEY records using the API.</p>
<h3 id="how-to-remove-remaining-dnskey-records">How to remove remaining DNSKEY records</h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="make-sure-dnssec-is-fully-turned-off">Make sure DNSSEC is fully turned off</h3>
@markup("md", "content/.markup/bodies/7677.md")
</aside>
<p>Use the <a href="/api/resources/dns/subresources/dnssec/methods/delete/">Delete DNSSEC API</a> to transition the zone to the <code>deleted</code> state. This stops all zone signing and removes all DNSSEC record types (RRSIG, NSEC, DNSKEY, CDS, and CDNSKEY):</p>
<pre class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/dnssec \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<p>For more information on DNSSEC states, refer to <a href="/dns/dnssec/dnssec-states/">DNSSEC states</a>.</p>
<h3 id="verify-dnskey-removal">Verify DNSKEY removal</h3>
<p>After removing the DNSKEY records, verify they no longer appear in DNS responses. An empty response confirms removal.</p>
<pre><code class="language-sh">dig DNSKEY example.com +short&#10;</code></pre>
<p>If DNSKEY records still appear, wait for the <a href="/dns/manage-dns-records/reference/ttl/">time-to-live (TTL)</a> to expire. DNSKEY records typically have longer TTL values (often 3600 seconds or more), so propagation may take one hour or longer.</p>
<hr />
<h2 id="next-steps">Next steps</h2>
<p>If a problem is discovered with DNSSEC implementation, contact the domain's registrar and confirm the DS record matches what the authoritative DNS provider has specified. If Cloudflare is the authoritative DNS provider, follow the instructions for <a href="/dns/dnssec/">configuring DNSSEC with Cloudflare</a>.</p>
