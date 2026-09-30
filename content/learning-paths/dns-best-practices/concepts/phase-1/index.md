<p>Detailed planning is the cornerstone of a successful DNS migration.</p>
<h2 id="1-understand-your-current-bind-setup"><ol>
<li>Understand your current BIND setup</li>
</ol></h2>
<ol>
<li>
<p>Identify all DNS zones currently hosted on your BIND servers.</p>
</li>
<li>
<p>Review all DNS records within each zone. Remove stale or unnecessary records and verify the accuracy of existing records.</p>
</li>
<li>
<p>BIND views (split DNS): If you use BIND views to provide different DNS responses to internal versus external resolvers, Cloudflare authoritative DNS does not replicate per-client views directly.</p>
<ul>
<li>Continue to use an internal DNS resolver (for example, BIND, Active Directory, or another internal resolver) for internal-only names, while using Cloudflare authoritative DNS for public zones.</li>
<li>For policy-based internal DNS, consider Cloudflare Zero Trust features such as DNS policies and Internal DNS. For more details, refer to <a href="/dns/">Cloudflare DNS</a> and <a href="/dns/internal-dns/">Internal DNS</a>.</li>
</ul>
</li>
<li>
<p>BIND ACLs (access control lists): If you use ACLs in BIND to restrict which clients can query your authoritative DNS or perform zone transfers, plan how these controls will change:</p>
<ul>
<li>
<p><strong>Authoritative DNS queries:</strong> Cloudflare authoritative DNS nameservers are reachable on the public Internet and do not support per-resolver ACLs for standard DNS queries.</p>
</li>
<li>
<p><strong>HTTP and application access:</strong> To restrict or filter HTTP(S) traffic to your applications, use Cloudflare security features such as the <a href="/waf/">Web Application Firewall (WAF)</a> and other Application Security products. These operate at the HTTP layer, not at the DNS query layer.</p>
</li>
<li>
<p>Zone transfers (AXFR/IXFR): If you use AXFR/IXFR with BIND today, review Cloudflare’s zone transfer setups:</p>
<ul>
<li><a href="/dns/zone-setups/zone-transfers/cloudflare-as-primary/">Cloudflare as primary DNS</a></li>
<li><a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Cloudflare as secondary DNS</a></li>
</ul>
<p>These setups document how to restrict which IP addresses can perform zone transfers.</p>
</li>
</ul>
</li>
<li>
<p>Dependencies: Identify any applications or services critically dependent on specific DNS behaviors of your BIND setup.</p>
</li>
</ol>
<h2 id="2-define-scope-and-objectives"><ol start="2">
<li>Define scope and objectives</li>
</ol></h2>
<p>Clearly list all domain names to be migrated and define success criteria for the migration.</p>
<h2 id="3-cloudflare-account-and-familiarization"><ol start="3">
<li>Cloudflare account and familiarization</li>
</ol></h2>
<ol>
<li><a href="/fundamentals/account/create-account/">Create your Cloudflare account</a> if you have not already.</li>
<li>Familiarize yourself with the Cloudflare DNS dashboard and its features.</li>
<li>Consider the different <a href="/dns/manage-dns-records/reference/dns-record-types/">DNS record types</a> you can manage on Cloudflare and how they map from BIND.</li>
</ol>
<h2 id="4-dnssec-strategy-critical"><ol start="4">
<li>DNSSEC strategy (critical)</li>
</ol></h2>
<p>Determine if DNSSEC is currently enabled for your zones on BIND and at your domain registrar.</p>
<p>Cloudflare supports two main migration approaches when DNSSEC is enabled:</p>
<ul>
<li>Option 1 (recommended for most migrations): <a href="/dns/dnssec/#disable-dnssec">Disable DNSSEC at your registrar</a> before changing nameservers. After the migration to Cloudflare is complete and stable, re-enable DNSSEC through the Cloudflare dashboard.</li>
<li>Option 2 (advanced): Perform an active migration using <a href="/dns/dnssec/multi-signer-dnssec/setup/">multi-signer DNSSEC</a>, where both providers sign the zone during the transition. This requires careful key management but allows you to migrate without disabling DNSSEC. For more information, refer to <a href="/dns/dnssec/dnssec-active-migration/">Migrate an existing zone with DNSSEC enabled</a>.</li>
</ul>
<p><strong>Disable-and-re-enable approach (safer for most teams):</strong></p>
<ol>
<li>Log in to your registrar and remove the DS records associated with your on-prem BIND DNSSEC keys for each domain.</li>
<li>Plan to switch nameservers only after resolvers are no longer expecting the old DNSSEC chain.</li>
</ol>
<p>*DS record TTL: If DNSSEC is active, note the Time To Live (TTL) of your DS records at the parent zone (managed by your registrar). This will determine how long you need to wait after removing DS records. As a rule of thumb, wait at least one full DS TTL and preferably up to 1.5 times the TTL before changing nameservers.</p>
<p>For more information about DNSSEC on Cloudflare, refer to <a href="/dns/dnssec/">DNSSEC</a>.</p>
<h2 id="5-choose-migration-window"><ol start="5">
<li>Choose migration window</li>
</ol></h2>
<p>Select a period of low traffic and activity to minimize potential impact and inform stakeholders of the planned window.</p>
<h2 id="6-develop-communication-and-rollback-plan"><ol start="6">
<li>Develop communication and rollback plan</li>
</ol></h2>
<ul>
<li>Communication: Plan how to communicate with stakeholders before, during, and after the migration.</li>
<li>Rollback Plan: Document steps to revert to your BIND servers if major issues arise. This primarily involves changing nameservers back at the registrar and potentially re-adding old DS records if DNSSEC was involved.</li>
</ul>
