<p>Cloudflare enables IPv6 on all domains without requiring additional configuration or hardware (as long as your host provides IPv6 support).</p>
<p>When IPv6 compatibility is turned on, Cloudflare auto generates <a href="/dns/manage-dns-records/reference/dns-record-types/#a-and-aaaa"><code>AAAA</code> DNS records</a> to allow IPv6 clients to connect. On the other hand, when IPv6 compatibility is turned off, Cloudflare does not automatically generate and advertise <code>AAAA</code> DNS for the zone. Client software will determine whether to use IPv4 or IPv6 to connect to a hostname that supports both methods.</p>
<p>For <a href="/dns/proxy-status/">proxied DNS records</a> that have both an IPv6 and IPv4 origin address, Cloudflare will prefer the IPv4 address when connecting to your origin server.</p>
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
<tr>
<td>Can customize</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="enable-ipv6-compatibility">Enable IPv6 compatibility</h2>
<p>By default, IPv6 compatibility is turned on for your domain and will apply to all domains and subdomains covered by <a href="/dns/proxy-status/">proxied DNS records</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/677.md")
</aside>
<h2 id="disable-ipv6-compatibility">Disable IPv6 compatibility</h2>
<p>If your origin web server only understands IPv4 formatted IP addresses, non-Enterprise customers should <a href="/network/pseudo-ipv4/">configure Pseudo IPv4</a>.</p>
<p>Alternatively, customers with an Enterprise account can turn off Cloudflare's IPv6 compatibility.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/676.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/680.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/675.md")
</aside>
<hr />
<h2 id="troubleshoot-an-ipv6-network-issue">Troubleshoot an IPv6 network issue</h2>
<p>Provide the following information to <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> if you experience issues with IPv6 connectivity:</p>
<ul>
<li>A <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#perform-a-traceroute">traceroute</a> that demonstrates the IPv6 connection issues.</li>
<li>The <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#identify-the-cloudflare-data-center-serving-your-request">Cloudflare data center serving your request</a> when the IPv6 issues occur.</li>
<li>Confirmation of whether <a href="#disable-ipv6-compatibility">disabling IPv6 Compatibility</a> resolves the issue.</li>
</ul>
