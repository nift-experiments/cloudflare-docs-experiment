<p>When your DNS records are <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7765.md")
</div>, Cloudflare speeds up and protects your site.
<p>A <code>dig</code> query against your proxied apex domain returns a Cloudflare IP address. This way, your origin server's IP address remains concealed from the public. Proxy benefits only apply to HTTP traffic.</p>
<p>When your server's IP address is exposed, your server is more vulnerable to direct attacks. It is still possible (but more difficult) for attackers to determine your origin server IP address when proxying traffic to Cloudflare.</p>
<hr />
<h2 id="dashboard-warnings">Dashboard warnings</h2>
<p>The Cloudflare dashboard displays warnings when DNS records may expose your origin server's IP address. These warnings do not block or affect traffic to your site.</p>
<p>When your zone has DNS records that are not proxied, the <strong>DNS Records</strong> page displays the following banner:</p>
<p><code>Proxying is required for most security and performance features. Set your DNS records to proxied by clicking &quot;Edit&quot; in the table below, to benefit from DDoS protection, security rules, caching, and more.</code></p>
<p>Individual DNS records may also display warnings. The specific message depends on whether the record can be proxied.</p>
<hr />
<h2 id="dns-records-that-should-be-proxied">DNS records that should be proxied</h2>
<p>Cloudflare recommends <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7766.md")
</div> any record that handles HTTP traffic so that a `dig` query returns a Cloudflare IP address instead of your origin server IP address.
<p>To take advantage of Cloudflare's performance and security benefits, proxy <code>A</code>, <code>AAAA</code>, and <code>CNAME</code> records.</p>
<hr />
<h2 id="dns-records-that-should-be-dns-only">DNS records that should be DNS-only</h2>
<p>Some DNS records need to remain DNS-only. For example, you may have to host multiple services (for example, a website and email) on the same physical server.</p>
<p>When a DNS-only record points to the same origin server as a proxied record, a <code>dig</code> query against that record reveals your origin server's IP address. This makes it easier for potential attackers to target your origin server directly.</p>
<p>To mitigate this risk:</p>
<ul>
<li>Analyze the impact of hosting multiple services on the same origin server in cases when you cannot avoid having DNS-only records.</li>
<li>Proxy all records that share the same origin IP address as your apex domain and can be safely proxied through Cloudflare.</li>
</ul>
