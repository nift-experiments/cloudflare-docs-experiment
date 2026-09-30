<h2 id="error-1034-edge-ip-restricted">Error 1034: Edge IP Restricted</h2>
<p>This error indicates that the IP address used for the domain is restricted by Cloudflare's edge validation.</p>
<p>Edge IP Validation (EIV) is a safeguard for restricted IP space that is meant to be used by specific Cloudflare accounts, such as <a href="/byoip/">BYOIP</a> prefixes, dedicated/<a href="/byoip/concepts/static-ips/">static</a> IP allocations, or other customer-associated IP ranges. When EIV is enabled, Cloudflare checks whether incoming traffic to those IPs is associated with an authorized account before allowing the request to proceed. This helps prevent accidental misrouting or unauthorized use of dedicated IP space while keeping properly configured traffic flowing normally.</p>
<h3 id="common-causes">Common causes</h3>
<h4 id="pointing-to-reserved-ip-addresses">Pointing to reserved IP addresses</h4>
<p>Customers who previously pointed their domains to <code>1.1.1.1</code> will now encounter a <code>1034</code> error. This is due to edge validation checks in Cloudflare's systems to prevent misconfiguration and potential abuse.</p>
<p><strong>Resolution</strong>: Ensure DNS records are pointed to IP addresses you control. If a placeholder IP address is needed for &quot;originless&quot; setups, use the IPv6 reserved address <code>100::</code> or the IPv4 reserved address <code>192.0.2.0</code>.</p>
<h4 id="saas-provider-ip-restrictions">SaaS provider IP restrictions</h4>
<p>If you are using a SaaS provider that uses <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a>, the provider may restrict access to their infrastructure to validated IP addresses only. In this case, requests to their IP addresses from domains that are not properly configured with the provider will be blocked with a <code>1034</code> error.</p>
<p><strong>Resolution</strong>: Verify that your domain is correctly configured with your SaaS provider. This typically involves:</p>
<ol>
<li>Ensuring your DNS records point to the correct IP addresses or hostnames provided by your SaaS provider.</li>
<li>Confirming that your domain has been properly registered and validated with the SaaS provider's platform.</li>
<li>Contacting your SaaS provider's support team if you continue to experience this error after verifying your configuration.</li>
</ol>
