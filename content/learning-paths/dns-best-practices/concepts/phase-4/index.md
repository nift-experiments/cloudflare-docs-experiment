<p>After the cutover, verify and stabilize.</p>
<h2 id="1-thorough-testing-and-validation"><ol>
<li>Thorough testing and validation</li>
</ol></h2>
<ol>
<li>Test all services that rely on DNS: websites, email (sending and receiving), VPNs, APIs, etc.</li>
<li>Test from different networks and geographical locations if possible.</li>
<li>Monitor application logs for any DNS-related errors.</li>
</ol>
<h2 id="2-enable-dnssec-in-cloudflare-if-disabled-earlier"><ol start="2">
<li>Enable DNSSEC in Cloudflare (if disabled earlier)</li>
</ol></h2>
<p>Enable DNSSEC only after you are confident that DNS is resolving correctly through Cloudflare and that nameserver changes have fully propagated. In practice, plan for at least one full DS TTL after you add new DS records at the registrar.</p>
<p><strong>Action in Cloudflare:</strong></p>
<ol>
<li>In the Cloudflare dashboard, go to your zone's <strong>DNS Settings</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Enable DNSSEC</strong>. Cloudflare will sign your zone and generate <code>DNSKEY</code> and <code>DS</code> record details.</li>
</ol>
<p><strong>Action at registrar:</strong></p>
<ol>
<li>Log in to your domain registrar.</li>
<li>Navigate to the DNSSEC management section for your domain.</li>
<li>Add the <code>DS</code> record details provided by Cloudflare.</li>
</ol>
<p>After adding the <code>DS</code> record, allow time for propagation and then validate your configuration with tools such as <a href="https://dnsviz.net">DNSViz</a> or <a href="https://dnssec-debugger.verisignlabs.com/">Verisign's DNSSEC debugger</a>. For more information, refer to <a href="/dns/dnssec/">DNSSEC</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9757.md")
</aside>
<h2 id="3-adjust-ttls-in-cloudflare"><ol start="3">
<li>Adjust TTLs in Cloudflare</li>
</ol></h2>
<p>After the migration is stable and DNSSEC is active (if used), increase the TTLs for your DNS records from the short values used during the migration to more standard values (for example, 3600 seconds for frequently changing records or 86400 seconds for very stable records).</p>
<p>Higher TTLs improve resolver cache efficiency and can reduce latency by allowing recursive resolvers to reuse cached answers for longer, at the cost of slower propagation when you make changes.</p>
<h2 id="4-review-and-enable-cloudflare-proxy-features"><ol start="4">
<li>Review and enable Cloudflare proxy features</li>
</ol></h2>
<p>If you initially set records to <strong>DNS Only</strong> (grey cloud), now is a good time to enable Cloudflare's proxy (orange cloud) for HTTP/S records (<code>A</code>, <code>AAAA</code>, <code>CNAME</code>) to leverage <a href="/cache/">CDN</a>, <a href="/waf/">WAF</a>, and other security and performance features. Test thoroughly after enabling proxying.</p>
<h2 id="5-decommission-on-prem-bind-servers"><ol start="5">
<li>Decommission On-Prem BIND servers</li>
</ol></h2>
<p>Only after a significant stabilization period (for example, several days to a week after full propagation and successful testing) and when you are fully confident in the Cloudflare setup, decommission the on-premise BIND servers.</p>
<p>Ensure no resolvers are still pointing to the old BIND servers. This is especially important for internal resolvers, if they were not addressed separately.</p>
<h2 id="6-update-internal-documentation-and-monitoring"><ol start="6">
<li>Update internal documentation and monitoring</li>
</ol></h2>
<p>Update all internal IT documentation to reflect the new DNS infrastructure and ensure your monitoring systems are checking DNS resolution via Cloudflare.</p>
