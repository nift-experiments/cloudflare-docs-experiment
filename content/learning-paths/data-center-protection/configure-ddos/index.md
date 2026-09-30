<p>Cloudflare DDoS protection automatically detects and mitigates Distributed Denial of Service (DDoS) attacks using its Autonomous Edge. Magic Transit customers have access to additional features, such as:</p>
<ul>
<li><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP protection</a> (disabled by default)</li>
<li><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS protection (beta)</a></li>
</ul>
<h2 id="create-a-ddos-override">Create a DDoS override</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/9622.md")
</div>
<h2 id="ddos-advanced-protection">DDoS advanced protection</h2>
<h3 id="advanced-tcp-protection">Advanced TCP Protection</h3>
<p>Cloudflare's Advanced TCP Protection, powered by <a href="https://blog.cloudflare.com/announcing-flowtrackd/"><code>flowtrackd</code></a>, is a stateful TCP inspection engine used to detect and mitigate sophisticated out-of-state TCP attacks such as randomized and spoofed ACK floods or SYN and SYN-ACK floods.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9618.md")
</aside>
<h4 id="setup">Setup</h4>
<p><a href="/ddos-protection/advanced-ddos-systems/overview/#rules">Create a global configuration</a> to set up SYN Flood and Out-of-state TCP rules and filters for Advanced TCP Protection.</p>
<h3 id="advanced-dns-protection">Advanced DNS Protection</h3>
<p>Cloudflare's Advanced DNS Protection, powered by <a href="https://blog.cloudflare.com/announcing-flowtrackd/"><code>flowtrackd</code></a>, provides stateful protection against DNS-based DDoS attacks, specifically sophisticated and fully randomized DNS attacks such as <a href="/dns/dns-firewall/random-prefix-attacks/about/">random prefix attacks</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9617.md")
</aside>
<h4 id="setup-1">Setup</h4>
<p><a href="/ddos-protection/advanced-ddos-systems/how-to/create-rule/#create-an-advanced-dns-protection-rule">Create a rule</a> to enable Advanced DNS Protection.</p>
