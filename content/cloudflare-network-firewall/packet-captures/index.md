<p>Cloudflare supports two types of packet captures (PCAPs): <strong>full</strong> and <strong>sample</strong>.
A packet capture records raw network traffic data so you can inspect it offline in tools like Wireshark. Full packet captures are the default.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4246.md")
</aside>
<h2 id="sample-packet-captures">Sample packet captures</h2>
<p>Use sample packet captures when you want to inspect recent traffic quickly.
Packet captures query historical traffic that has already passed through Cloudflare's network — not new traffic — so they complete immediately after you start them.</p>
<p>You can view sample captures in the Cloudflare dashboard. They only include the first 160 bytes of each packet, which is useful for capturing packet headers but will not provide detailed packet data. Cloudflare collects this data across all of its data centers and assembles it into a PCAP file, giving you a global view of traffic across the network.</p>
<p>Use full packet captures instead if you need complete packet payloads, or if the traffic you want to capture occurs infrequently.</p>
<h2 id="full-packet-captures">Full packet captures</h2>
<p>Full packet captures actively monitor Cloudflare's network for new traffic that matches filters you configure. Unlike sample captures, they capture packets that arrive after the capture starts, not historical data.</p>
<p>Full captures include the complete packet data, not just headers. The matching packet data is saved directly to a cloud storage bucket that you own and configure. You cannot view it in the Cloudflare dashboard. You can download the resulting PCAP file and analyze it in Wireshark or another packet capture tool.</p>
<p>Before starting a full packet capture, make sure you have a cloud storage bucket set up and configured. Refer to the articles in this section for setup instructions.</p>
<ul class="directory-listing"><li><a href="/cloudflare-network-firewall/packet-captures/pcaps-bucket-setup/">PCAPs bucket setup</a></li><li><a href="/cloudflare-network-firewall/packet-captures/collect-pcaps/">Collect PCAPs</a></li></ul>
