<p>After a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/4249.md")
</div> capture is requested and the capture is collected, the output is contained within one or more files in PCAP file format. Before starting a `full` type packet capture, you must first follow instructions for [configuring a bucket](/cloudflare-network-firewall/packet-captures/pcaps-bucket-setup/).
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4248.md")
</aside>
<h2 id="send-a-packet-capture-request">Send a packet capture request</h2>
<p>Currently, when a packet capture is requested, packets flowing at Cloudflare's global network through the Magic Transit system are captured. The default API field for this is <code>&quot;system&quot;: &quot;magic-transit&quot;</code>, both for the request and response.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/4247.md")
</aside>
<h3 id="packet-capture-limits">Packet capture limits</h3>
<p><strong>Sample and full</strong></p>
<ul>
<li><code>packet_limit</code>: The minimum value is <code>1</code> packet and maximum value is <code>10000</code> packets.</li>
</ul>
<p><strong>Sample</strong></p>
<ul>
<li><code>time_limit</code>: The minimum value is <code>1</code> seconds and maximum value is <code>300</code> seconds.</li>
</ul>
<p><strong>Full</strong></p>
<ul>
<li><code>time_limit</code>: The minimum value is <code>1</code> seconds and maximum value is <code>86400</code> seconds.</li>
<li><code>byte_limit</code>: The minimum value is <code>1</code> byte and maximum value is <code>1000000000</code> bytes.</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4254.md")
</div></div>
<h2 id="check-packet-capture-status">Check packet capture status</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4257.md")
</div></div>
<p>The capture status displays one of the following options:</p>
<ul>
<li><strong>Complete:</strong> The capture request is done and ready for download.</li>
<li><strong>In progress:</strong> The capture request was captured but still processing.</li>
<li><strong>Failure:</strong> The capture failed. If this occurs, verify your ownership information.</li>
</ul>
<h2 id="download-packet-captures">Download packet captures</h2>
<p>After your request finishes processing, you can download your packet captures.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4260.md")
</div></div>
<h2 id="list-packet-captures">List packet captures</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4263.md")
</div></div>
<h2 id="best-practices">Best practices</h2>
<p>Due to the nature of Cloudflare network, your traffic may traverse various physical machines within a single Cloudflare location.</p>
<ul>
<li>Multiple PCAP Files: A single full PCAP capture may produce many small PCAP files, as a capture is taken for each physical server your traffic traverses in a Cloudflare location.
<ul>
<li>You can get more granular by applying packet-specific filters like protocol, port (and more) to target the traffic you need.</li>
</ul>
</li>
<li>Merging for Analysis: To view the traffic as a single flow, you can use a tool like mergecap to combine the individual files into one larger file for analysis in Wireshark. Refer to the <a href="https://www.wireshark.org/docs/wsug_html_chunked/AppToolsmergecap.html">Wireshark mergecap documentation</a> for instructions.</li>
</ul>
