<p>The suggestions in the <a href="/cloudflare-one/traffic-policies/packet-filtering/best-practices/minimal-ruleset">Minimal ruleset</a> and <a href="/cloudflare-one/traffic-policies/packet-filtering/best-practices/extended-ruleset">Extended ruleset</a> are recommendations for ingress (incoming) traffic. This page covers the additional consideration needed for egress (outgoing) traffic.</p>
<p>Cloudflare Network Firewall does not track connection state (it is not &quot;stateful&quot;). A stateful firewall automatically allows return traffic for active connections — for example, if you send a request outbound, the response is allowed back in. Because Network Firewall is not stateful, each packet — whether ingress or egress — is evaluated independently against your rules. This means ingress block rules can inadvertently block egress traffic.</p>
<p>For Magic Transit egress traffic, consider the following:</p>
<ul>
<li>
<p>Network Firewall rules apply to both Magic Transit ingress and egress traffic passing through Cloudflare.</p>
</li>
<li>
<p>If you have a &quot;default drop&quot; catchall rule (a final rule that blocks all traffic not matched by earlier rules) for ingress traffic, you must add an earlier rule to permit traffic sourced from your Magic Transit prefix with the destination as <strong>any</strong> to allow outbound egress traffic.</p>
<p>For example, place the following allow rule before any default-drop catchall rule:</p>
<p><strong>Match</strong>: <code>ip.src in {&lt;YOUR_MAGIC_TRANSIT_PREFIX&gt;}</code> <br/>
<strong>Action</strong>: Allow</p>
</li>
</ul>
