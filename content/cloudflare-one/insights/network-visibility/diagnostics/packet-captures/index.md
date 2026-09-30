<p>Packet captures record network traffic flowing through Cloudflare's network so you can analyze individual <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/4997.md")
</div> for troubleshooting or security investigations. The output is contained within one or more files in PCAP format, which you can open in tools like [Wireshark](https://www.wireshark.org/).
<p>There are two capture types:</p>
<ul>
<li><strong>Sample</strong> captures query historical traffic data that has already passed through Cloudflare's network. They complete immediately and can be downloaded directly from the API, or from the Cloudflare dashboard.</li>
<li><strong>Full</strong> captures actively monitor for new traffic matching your filters and write the complete packet data to a cloud storage bucket you own. Before starting a full capture, you must first <a href="/cloudflare-one/insights/network-visibility/diagnostics/buckets/">configure a bucket</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4996.md")
</aside>
<h2 id="send-a-packet-capture-request">Send a packet capture request</h2>
<p>Currently, when a packet capture is requested, packets flowing through Cloudflare's global network via the Magic Transit system are captured. The default API field for this is <code>&quot;system&quot;: &quot;magic-transit&quot;</code>, both for the request and response.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/4995.md")
</aside>
<h3 id="packet-capture-limits">Packet capture limits</h3>
<p><strong>Sample and full</strong></p>
<ul>
<li><code>time_limit</code>: The minimum value is <code>1</code> second and maximum value is <code>300</code> seconds.</li>
<li><code>packet_limit</code>: The minimum value is <code>1</code> packet and maximum value is <code>10000</code> packets.</li>
</ul>
<p><strong>Full</strong></p>
<ul>
<li><code>byte_limit</code>: The minimum value is <code>1</code> byte and maximum value is <code>1000000000</code> bytes (1 GB).</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5002.md")
</div></div>
<h2 id="check-packet-capture-status">Check packet capture status</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5005.md")
</div></div>
<p>The capture status displays one of the following options:</p>
<ul>
<li><strong>Complete</strong> (API: <code>success</code>): The capture is done and ready for download.</li>
<li><strong>In progress</strong> (API: <code>pending</code>): Packets have been captured but the PCAP file is still being assembled.</li>
<li><strong>Failure</strong>: The capture failed. For full captures, verify that your bucket is correctly configured and that Cloudflare has write access to it. For sample captures, verify your filter configuration.</li>
</ul>
<h2 id="download-packet-captures">Download packet captures</h2>
<p>After your request finishes processing, you can download your packet captures.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5008.md")
</div></div>
<h2 id="list-packet-captures">List packet captures</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5011.md")
</div></div>
