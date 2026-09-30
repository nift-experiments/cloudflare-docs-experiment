<p>The suggestions in the <a href="/cloudflare-network-firewall/best-practices/minimal-ruleset/">Minimal ruleset</a> and <a href="/cloudflare-network-firewall/best-practices/extended-ruleset/">Extended ruleset</a> are recommendations for ingress traffic.</p>
<p>For Magic Transit egress traffic, consider the following information:</p>
<ul>
<li>The Cloudflare Network Firewall (formerly Magic Firewall) rules will apply to both Magic Transit ingress and egress traffic passing via Cloudflare.</li>
<li>Network Firewall is not stateful for your Magic Transit egress traffic.</li>
<li>Network Firewall is not stateful in both directions after DDoS mitigations.</li>
<li>If you have a Network Firewall &quot;default drop&quot; catchall rule for ingress traffic, you will need to add an earlier rule to permit traffic sourced from your Magic Transit prefix with the destination as <strong>any</strong> to allow outbound egress traffic.</li>
</ul>
