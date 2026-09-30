<p>This guide helps you determine whether a tunnel health alert is actually affecting your traffic. A degraded or down tunnel only matters if your traffic is currently routing through the Cloudflare data center where that tunnel is unhealthy.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6733.md")
</aside>
<h2 id="before-you-begin">Before you begin</h2>
<p>Understand how Cloudflare WAN health checks and traffic routing work:</p>
<ul>
<li>Health checks run independently from every Cloudflare data center.</li>
<li>Each data center evaluates tunnel health based on its own probes.</li>
<li>Traffic enters Cloudflare at the data center closest to the source (anycast routing).</li>
<li>A degraded tunnel in a data center that is not handling your traffic has no impact on your connectivity.</li>
</ul>
<p>If you are experiencing actual tunnel health issues (tunnels flapping, all tunnels down, or IPsec errors), refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/tunnel-health/">Troubleshoot tunnel health</a> instead.</p>
<h2 id="diagnostic-flowchart">Diagnostic flowchart</h2>
<p>Use this flowchart to determine whether a tunnel health alert requires action.</p>
<pre><code class="language-mermaid">flowchart TD&#10;accTitle: Connectivity troubleshooting flowchart&#10;accDescr: A decision tree to determine whether a degraded tunnel alert is affecting your traffic.&#10;&#10;A[&quot;You received a tunnel&lt;br&gt;health alert&quot;] --&gt; B{&quot;Is your traffic&lt;br&gt;affected?&quot;}&#10;B -- &quot;Yes, I have&lt;br&gt;connectivity issues&quot; --&gt; C[&quot;Identify your ingress&lt;br&gt;data center and check&lt;br&gt;tunnel health there&quot;]&#10;B -- &quot;No, traffic&lt;br&gt;flows normally&quot; --&gt; D{&quot;Does the alert match&lt;br&gt;a data center carrying&lt;br&gt;your traffic?&quot;}&#10;D -- &quot;No&quot; --&gt; E[&quot;No action required.&lt;br&gt;The degraded tunnel is in&lt;br&gt;a data center not serving&lt;br&gt;your traffic.&quot;]&#10;D -- &quot;Yes&quot; --&gt; C&#10;C --&gt; G{&quot;Are tunnels healthy&lt;br&gt;at your ingress&lt;br&gt;data center?&quot;}&#10;G -- &quot;Yes&quot; --&gt; H[&quot;The issue is not&lt;br&gt;tunnel-related. Check&lt;br&gt;Cloudflare Status and&lt;br&gt;your origin network.&quot;]&#10;G -- &quot;No&quot; --&gt; I[&quot;Tunnels at your ingress&lt;br&gt;data center are unhealthy.&lt;br&gt;Refer to Troubleshoot&lt;br&gt;tunnel health.&quot;]&#10;</code></pre>
<h2 id="1-identify-your-ingress-data-center"><ol>
<li>Identify your ingress data center</li>
</ol></h2>
<p>Determine which Cloudflare data center your traffic is entering. This is the only data center whose tunnel health status matters for your current connectivity.</p>
<h3 id="use-traceroute">Use traceroute</h3>
<p>Run a <code>traceroute</code> from the source network to your Cloudflare WAN prefix. Look for the Cloudflare data center hostname in the trace output, which contains a three-letter <a href="https://en.wikipedia.org/wiki/IATA_airport_code">IATA airport code</a> that identifies the data center.</p>
<pre><code class="language-sh">traceroute 203.0.113.1&#10;</code></pre>
<pre><code class="language-txt"> 1  192.168.1.1 (192.168.1.1)  1.234 ms&#10; 2  10.0.0.1 (10.0.0.1)  5.678 ms&#10; 3  198.51.100.1 (198.51.100.1)  10.123 ms&#10; 4  198.51.100.10 (198.51.100.10)  12.345 ms&#10; 5  lhr01.cf (198.51.100.11)  15.678 ms&#10;</code></pre>
<p>In this example, <code>lhr</code> indicates that traffic enters Cloudflare at the London (Heathrow) data center.</p>
<h3 id="use-the-cloudflare-dashboard">Use the Cloudflare dashboard</h3>
<p>You can identify which data centers handle your traffic by using <strong>Network Analytics</strong>.</p>
<ol>
<li>Go to the <strong>Network Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add filter</strong> and filter traffic by your source IP addresses to isolate your traffic.</li>
<li>Under <strong>Packets summary</strong>, select the <strong>Source data center</strong> tab. If the tab is not visible, select the three-dot menu (<code>...</code>) to reveal additional view options and select <strong>Source data center</strong>.</li>
<li>Review the per-data-center traffic breakdown to identify which Cloudflare data centers are handling your traffic.</li>
<li>Cross-reference these data centers with the tunnel health status on the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/"><strong>Connector health</strong> page</a>. If tunnels are healthy at the data centers carrying your traffic, a degraded tunnel alert for a different data center is not the cause of your connectivity issue.</li>
</ol>
<h2 id="2-correlate-with-cloudflare-status"><ol start="2">
<li>Correlate with Cloudflare status</li>
</ol></h2>
<p>If your tunnels are healthy at the relevant data center but you still experience connectivity issues, check for broader platform issues.</p>
<ol>
<li>Go to <a href="https://www.cloudflarestatus.com/">Cloudflare Status</a>.</li>
<li>Look for any active incidents or maintenance at the data center you identified.</li>
<li>Check for any incidents that might affect your traffic, such as outages related to networking, BYOIP, or the services your configuration depends on.</li>
</ol>
<h2 id="3-gather-information-for-support"><ol start="3">
<li>Gather information for support</li>
</ol></h2>
<p>If you have worked through this guide and cannot resolve the issue, gather the following information before contacting Cloudflare support.</p>
<h3 id="required-information">Required information</h3>
<ol>
<li><strong>Account ID</strong> and <strong>tunnel name(s)</strong> affected</li>
<li><strong>Timestamps</strong> (in UTC) when the issue started</li>
<li><strong>Ingress data center</strong> you identified (airport code, for example <code>LHR</code>, <code>IAD</code>)</li>
<li><strong>Symptoms observed:</strong>
<ul>
<li>Whether user traffic is affected or only health check alerts fired</li>
<li>Which tunnels and data centers show degraded or down status</li>
<li>Whether the issue is intermittent or persistent</li>
</ul>
</li>
</ol>
<h3 id="helpful-diagnostic-data">Helpful diagnostic data</h3>
<ul>
<li><strong>Traceroute output</strong> from your source network to your Cloudflare WAN prefix</li>
<li><strong>Dashboard screenshots</strong> showing tunnel health at the relevant data center</li>
<li><strong>Distributed traceroutes</strong> using tools like <a href="https://ping.pe">ping.pe</a> to test reachability from multiple global locations</li>
<li><strong>Packet captures</strong> from your router if traffic loss is confirmed</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/tunnel-health/">Troubleshoot tunnel health</a>: Resolve common tunnel health issues (flapping, IPsec errors, stateful firewall drops).</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/routing-and-bgp/">Troubleshoot routing and BGP</a>: Diagnose routing and BGP issues that affect traffic delivery.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/">Check tunnel health in the dashboard</a>: Monitor tunnel status per data center.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/tunnel-health-checks/">Tunnel health checks</a>: Technical details on how health checks work.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/analytics/network-analytics/">Network Analytics</a>: Analyze traffic patterns over time.</li>
</ul>
<hr />
<h2 id="more-wan-resources">More WAN resources</h2>
<p>For more information, refer to the full Cloudflare WAN documentation.</p>
<p><a class="nb-link-button" href="/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/connectivity/">Full connectivity troubleshooting guide ❯</a></p>
