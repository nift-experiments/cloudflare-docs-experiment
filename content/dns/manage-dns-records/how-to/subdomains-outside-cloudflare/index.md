<p>Subdomain delegation allows different individuals, teams, or organizations to manage different subdomains of a site.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7812.md")
</aside>
<p>For instance, consider <code>example.com</code> as a Cloudflare domain with <code>www.example.com</code> managed in Cloudflare's <strong>DNS</strong> app and <code>blog.example.com</code> delegated to nameservers outside of Cloudflare. In this example, <code>blog.example.com</code> can now be managed by individuals who do not have access to Cloudflare credentials for the <code>example.com</code> domain.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7811.md")
</aside>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="delegate-a-subdomain-outgoing">Delegate a subdomain (outgoing)</h2>
<p>To delegate a subdomain such as <code>blog.example.com</code>, tell DNS resolvers where to find the zone file:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account.</li>
<li>Select the domain that contains the subdomain to be delegated.</li>
<li>Go to the <strong>DNS Records</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="4">
<li>Create <code>NS</code> records for the subdomain. For example:
<ul>
<li><code>blog.example.com NS ns1.externalhost.com</code></li>
<li><code>blog.example.com NS ns2.externalhost.com</code></li>
<li><code>blog.example.com NS ns3.externalhost.com</code></li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7810.md")
</aside>
5. (Optional) If the delegated nameserver has DNSSEC enabled, [add the `DS` record](/dns/dnssec/#1-activate-dnssec-in-cloudflare) in Cloudflare.
<h3 id="limits">Limits</h3>
<p>When creating NS records, there are limits on the number of nameservers that can be associated with a single delegation name.</p>
<p>According to DNS standards defined in <a href="https://www.rfc-editor.org/rfc/rfc1912.html">RFC 1912</a>, a delegation should not include more than seven nameserver names for the same delegation name.</p>
<p>To align with these standards and maintain platform stability:</p>
<ul>
<li>Cloudflare supports up to 10 NS records per delegation name, but the best practice is to keep the set at seven or fewer.</li>
<li>Creating more than 10 NS records for the same name is not supported. Requests that exceed this limit may be rejected or fail validation.</li>
</ul>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@input("content/.markup/bodies/7814.md")
</div></details>
<h2 id="delegate-a-subdomain-incoming">Delegate a subdomain (incoming)</h2>
<p>To delegate a subdomain from an external DNS provider to Cloudflare, refer to <a href="/dns/zone-setups/subdomain-setup/setup/">subdomain setups</a>.</p>
