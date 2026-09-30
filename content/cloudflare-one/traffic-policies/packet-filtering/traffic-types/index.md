<p>Cloudflare Network Firewall enables you to allow or block traffic on a variety of packet characteristics, including:</p>
<ul>
<li><strong>Source and destination IP</strong> — the sender's and receiver's IP addresses</li>
<li><strong>Source and destination port</strong> — the numeric port identifying the specific service (for example, port 80 for HTTP)</li>
<li><strong>Protocol</strong> — the communication method, such as TCP or UDP</li>
<li><strong>Packet length</strong> — the size of the packet in bytes</li>
<li>**<div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/6408.md")
</div>** — inspect individual flags within packet headers
<p>Cloudflare Network Firewall operates at OSI layers 3 and 4 — the network layer (IP addressing and routing) and transport layer (port-based connections). It supports protocols such as TCP (reliable, ordered connections), UDP (fast, connectionless messages), and ICMP (network diagnostic messages like ping). You can write rules against any layer 3 or 4 protocol, not only TCP and UDP.</p>
<p>To see the full list of fields you can use when writing filter expressions, refer to <a href="/cloudflare-network-firewall/reference/network-firewall-fields/">Cloudflare Network Firewall fields</a>.</p>
