<p>As opposed to the <a href="/dns/dnssec/">normal process</a> for enabling DNSSEC, DNSSEC with a subdomain setup requires a few additional steps.</p>
<h2 id="requirements">Requirements</h2>
<p>To use DNSSEC for a subdomain setup, DNSSEC must be enabled on the parent zone. After enabling DNSSEC on the parent zone, you should wait the minimum <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7907.md")
</div> value (specified in the [SOA record](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/) of the parent zone) to ensure DNS resolvers provide the same DNS query responses.
<h2 id="setup">Setup</h2>
<ol>
<li>
<p><a href="/dns/zone-setups/subdomain-setup/setup/#how-to">Create</a> the child zone.</p>
</li>
<li>
<p>Make sure the child zone is <a href="/dns/zone-setups/reference/domain-status/">active</a> on Cloudflare and that DNS resolution is working properly for your subdomain.</p>
</li>
<li>
<p><a href="/dns/dnssec/">Enable DNSSEC</a> for the child zone and save the information provided within the DS record output.</p>
</li>
<li>
<p>On the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page of the parent zone, <a href="/dns/manage-dns-records/how-to/create-dns-records/">add the DS record</a> from the previous step.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/dns/ds-record-example.png" alt="Screenshot showing how to add a DS record within Cloudflare" /></p>
<ol start="5">
<li>
<p>Add an A record to the child zone to validate DNS resolution.</p>
</li>
<li>
<p>Wait two to six hours. Then, <a href="/dns/dnssec/troubleshooting/#test-dnssec-with-dig">test the A record</a> added in the previous step using multiple DNS resolvers with DNSSEC validation (<code>1.1.1.1</code>, <code>8.8.8.8</code>, and <code>9.9.9.9</code>). For example, if the A record is for <code>test.child.example.com</code>: <code>dig test.child.example.com +dnssec @1.1.1.1</code>.</p>
</li>
</ol>
