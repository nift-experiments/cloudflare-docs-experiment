<p>Packet captures allow you to record raw network traffic data passing through Cloudflare's network so you can inspect it offline in tools like Wireshark. This is useful for diagnosing connectivity issues, verifying firewall rules, or investigating unexpected traffic patterns.</p>
<p>Cloudflare supports two types of packet captures: full and sample. Full packet captures are the default behavior.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5012.md")
</aside>
<h2 id="sample-packet-captures">Sample packet captures</h2>
<p>Sample packet captures collect historical data on network traffic that has already passed through Cloudflare's network. They will not collect any new traffic sent to Cloudflare's network after the packet capture has started. All sample packet captures will complete immediately after they are started because they query historical traffic data.</p>
<p>Sample packet captures can be viewed in the Cloudflare dashboard. They only include the first 160 bytes of each packet, which is useful for capturing packet headers but will not provide detailed packet data. The sample data is collected across all Cloudflare's data centers to build a PCAP file. This allows you to get a global picture of traffic across all data centers.</p>
<p>You should use full packet captures if you need to collect data on packets that pass through your network less frequently.</p>
<h2 id="full-packet-captures">Full packet captures</h2>
<p>Full packet captures actively monitor Cloudflare's network for packets that match the selected filters, and capture the complete packet data, including the payload. The matching packet data is saved to a cloud storage bucket that is owned and configured by you. You must <a href="/cloudflare-one/insights/network-visibility/diagnostics/buckets/">configure a bucket</a> before starting a full packet capture.</p>
<p>Full packet captures will collect new traffic sent to Cloudflare's network after the packet capture has started, and include the full packet data. This type of capture cannot be viewed in the Cloudflare dashboard. You can download them from a cloud storage bucket and analyze them in Wireshark or another packet capture tool.</p>
<p>Refer to the articles in this section to learn how to use packet captures.</p>
<ul class="directory-listing"><li><a href="/cloudflare-one/insights/network-visibility/diagnostics/packet-captures/">Packet captures</a></li><li><a href="/cloudflare-one/insights/network-visibility/diagnostics/buckets/">Buckets</a></li></ul>
