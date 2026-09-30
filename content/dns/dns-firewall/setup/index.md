<h2 id="prerequisites">Prerequisites</h2>
<p>Prior to setting up DNS Firewall, you need:</p>
<ul>
<li>Account access to DNS Firewall (provided by your Enterprise account team).</li>
<li>Access to <strong>DNS Administrator</strong> or <strong>Super Administrator</strong> privileges on your account.</li>
<li>Newly updated IP addresses for your nameservers (protects against previously compromised IP addresses).</li>
</ul>
<h2 id="configure-dns-firewall">Configure DNS Firewall</h2>
<h3 id="create-a-dns-firewall-cluster">Create a DNS Firewall cluster</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7701.md")
</div></div>
<h3 id="update-registrar-settings">Update registrar settings</h3>
<p>Update the <code>A/AAAA</code> glue records for your nameserver hostnames at your registrar with your DNS Firewall cluster IP addresses.</p>
<h3 id="update-dns-servers">Update DNS servers</h3>
<p>At your DNS servers, update the <code>A/AAAA</code> records for your nameserver hostnames in your DNS zone file with your DNS Firewall cluster IP addresses.</p>
<h3 id="test-dns-resolution">Test DNS resolution</h3>
<p>Confirm that your nameservers are functioning correctly by running a <code>dig</code> command.</p>
<h3 id="update-security-policies">Update security policies</h3>
<p>Configure security policy in your DNS servers and Firewall to allow only <a href="https://cloudflare.com/ips">Cloudflare IPs</a> and TCP/UDP port 53.</p>
<h2 id="additional-options">Additional options</h2>
<p>Beyond the required fields, you can configure the following settings on your DNS Firewall cluster — in the Cloudflare dashboard when you create or edit a cluster, or via the API:</p>
<ul>
<li><strong>Rate limit</strong> (queries per second per data center).</li>
<li><strong>Negative cache TTL</strong> for <code>REFUSED</code>, <code>NXDOMAIN</code>, and <code>SERVFAIL</code> responses.</li>
<li><strong>EDNS Client Subnet (ECS) fallback</strong> — forward the resolver's IP subnet when the incoming query does not include ECS data. Refer to the <a href="/dns/dns-firewall/faq/#does-dns-firewall-support-edns-client-subnet-ecs">FAQ</a> for details.</li>
<li><strong>Attack mitigation</strong> for <a href="/dns/dns-firewall/random-prefix-attacks/">random prefix attacks</a>.</li>
</ul>
<p>For the full parameter reference, refer to the <a href="/api/resources/dns_firewall/methods/create/">Create</a> and <a href="/api/resources/dns_firewall/methods/edit/">Update</a> DNS Firewall Cluster API endpoints.</p>
