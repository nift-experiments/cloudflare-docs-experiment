<p>Learn which network ports Cloudflare proxies by default and how to enable Cloudflare's proxy for additional ports.</p>
<h2 id="network-ports-compatible-with-cloudflare-s-proxy">Network ports compatible with Cloudflare's proxy</h2>
<p>By default, Cloudflare proxies traffic destined for the HTTP/HTTPS ports listed below.</p>
<details class="nb-details"><summary>HTTP ports supported by Cloudflare</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8779.md")
</div></details>
<details class="nb-details"><summary>HTTPS ports supported by Cloudflare</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8780.md")
</div></details>
<details class="nb-details"><summary>Ports supported by Cloudflare, but with caching disabled</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8781.md")
</div></details>
<h2 id="how-to-enable-cloudflare-s-proxy-for-additional-ports">How to enable Cloudflare's proxy for additional ports</h2>
<p>If traffic for your domain is destined for a different port than the ones listed above, for example you have an SSH server that listens for incoming connections on port 22, either:</p>
<ul>
<li>Change your subdomain to be <a href="/dns/proxy-status/">gray-clouded</a>, via your Cloudflare DNS app, to bypass the Cloudflare network and connect directly to your origin.</li>
<li>Configure a <a href="/spectrum/get-started/">Spectrum application</a> for the hostname running the server. Spectrum supports all ports. Spectrum for all TCP and UDP ports is only available on the Enterprise plan. If you would like to know more about Cloudflare plans, please reach out to your Cloudflare account team.</li>
</ul>
<h2 id="how-to-block-traffic-on-additional-ports">How to block traffic on additional ports</h2>
<p>Block traffic on ports other than 80 and 443 in Cloudflare paid plans by doing one of the following:</p>
<ul>
<li>If you are using <a href="/waf/reference/legacy/old-waf-managed-rules/">WAF managed rules (previous version)</a>, enable rule ID <code>100015</code> (<code>Anomaly:Port - Non Standard Port (not 80 or 443)</code>).</li>
<li>If you are using the new <a href="/waf/">Cloudflare Web Application Firewall (WAF)</a>, enable rule ID <code class="nb-rule-id" title="8e361ee4328f4a3caf6caf3e664ed6fe">664ed6fe</code> (<code>Anomaly:Port - Non Standard Port (not 80 or 443)</code>), which is disabled by default. This rule is part of the Cloudflare Managed Ruleset.</li>
</ul>
<p>Ports 80 and 443 are the only ports compatible with:</p>
<ul>
<li>HTTP/HTTPS traffic within China data centers for domains that have the <strong>China Network</strong> enabled</li>
</ul>
<p>Due to the nature of Cloudflare's anycast network, ports other than <code>80</code> and <code>443</code> will be open so that Cloudflare can serve traffic for other customers on these ports. In general, Cloudflare makes available several different products on <a href="https://www.cloudflare.com/ips">Cloudflare IPs</a>, so you can expect tools like Netcat and security scanners to report these non-standard ports as open in specific conditions. If you have questions on security compliance, review <a href="https://www.cloudflare.com/en-gb/trust-hub/compliance-resources/">Cloudflare's certifications and compliance resources</a> and contact your Cloudflare enterprise account manager for more information.
<br /></p>
<p>The WAF's <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare Managed Ruleset</a> includes a rule that will block traffic at the application layer (layer 7 in the <a href="https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/">OSI model</a>), preventing HTTP/HTTPS requests over non-standard ports from reaching the origin server.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8777.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/dns/manage-dns-records/how-to/create-dns-records/">Managing DNS records at Cloudflare</a></li>
</ul>
