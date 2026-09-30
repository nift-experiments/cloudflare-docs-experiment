<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8769.md")
</aside>
<p>PCI scanners are tools used to identify security weaknesses. When a business undergoes a compliance audit, PCI scan results are used for compliance verification.</p>
<h2 id="initiate-a-scan">Initiate a scan</h2>
<ol>
<li>
<p>Identify which server your scan should target. Are you scanning against your origin server, where your applications are hosted, or at a proxy server sitting in front of your origin, such as Cloudflare?</p>
</li>
<li>
<p>On your scanner tool, enter a public URL or an IP address. If you enter a public website URL, the scanner will resolve the hostname and scan the resulting the IP address. To scan your origin server, be sure to enter your origin server's IP address or a hostname that resolves to the origin server's IP, not a proxy server.</p>
</li>
<li>
<p>Start the scan and analyze the results.</p>
</li>
<li>
<p>(Optional) Run another scan for a different origin server.</p>
</li>
</ol>
<h3 id="open-ports-versus-blocked-traffic">Open ports versus blocked traffic</h3>
<p>Cloudflare's anycast network operates in a way that keeps ports other than 80 and 443 open, allowing it to serve traffic for other customers on these ports.</p>
<p>However, customers can easily block all unwanted traffic to these ports by using Cloudflare <a href="/fundamentals/reference/network-ports/#how-to-block-traffic-on-additional-ports">WAF Managed Rules</a> or <a href="/waf/custom-rules/">custom rules</a>. The PCI scan will show the ports being open, but the traffic will not reach your origin server. This concern is often misunderstood.</p>
<h2 id="additional-resources">Additional resources</h2>
<p>You can find all our public compliance resources in the following pages:</p>
<ul>
<li><a href="https://www.cloudflare.com/trust-hub/compliance-resources/">Certifications and compliance resources</a></li>
<li><a href="/fundamentals/reference/policies-compliances/compliance-docs/">Compliance documentation</a></li>
</ul>
<p>You can access Compliance documents in the Cloudflare dashboard by selecting your account where you are a Super Administrator and then navigating to <strong>Support</strong> &gt; <strong>Compliance Documents</strong>.</p>
