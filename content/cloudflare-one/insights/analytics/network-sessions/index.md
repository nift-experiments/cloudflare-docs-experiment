<p>The Network session analytics dashboard provides visibility into your Cloudflare One traffic patterns. This dashboard helps you understand how traffic flows through your network, including on-ramps (how traffic enters Cloudflare, such as the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>, <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints (PAC files)</a>, <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a>, or Cloudflare Tunnel) and off-ramps (how traffic exits Cloudflare, such as the public Internet or a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>).</p>
<p>The dashboard is based on the <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust network sessions Logpush dataset</a>. For definitions on any field, refer to the dataset schema documentation.</p>
<p>To review Network session analytics:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Dashboards</strong>.</li>
<li>Select <strong>Network session analytics</strong>.</li>
</ol>
<p>Refer to <a href="/cloudflare-one/insights/">Insights overview</a> to learn how to use Analytics dashboards together with <a href="/cloudflare-one/insights/analytics-overview/">Analytics Overview</a> and <a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> for complete visibility and troubleshooting.</p>
<h2 id="use-cases">Use cases</h2>
<p>The Network session analytics dashboard helps you:</p>
<ul>
<li><strong>Understand traffic patterns</strong>: Visualize how traffic flows through your network infrastructure.</li>
<li><strong>Monitor bandwidth usage</strong>: Track upload, download, and total bytes transferred across your network.</li>
<li><strong>Identify connection issues</strong>: Analyze connection close reasons to troubleshoot network problems.</li>
<li><strong>Track user and device activity</strong>: Monitor unique users and devices accessing your network.</li>
</ul>
<h2 id="provided-analytics">Provided analytics</h2>
<h3 id="summary-metrics">Summary metrics</h3>
<ul>
<li><strong>Session count</strong>: Total number of network sessions. Each session represents an individual TCP, UDP, ICMP, or ICMPv6 flow that passes through Gateway.</li>
<li><strong>Bytes total</strong>: Total bytes transferred (upload + download)</li>
<li><strong>Unique users</strong>: Number of distinct users</li>
</ul>
<h3 id="traffic-by-location">Traffic by location</h3>
<ul>
<li><strong>World map</strong>: Geographic visualization of network traffic by the Cloudflare data center where traffic entered the network (ingress) and where it exited (egress)</li>
<li><strong>Location list</strong>: Top Cloudflare data center locations by ingress and egress session count with accompanying graph</li>
<li><strong>Change</strong>: Shows the total change across ingress and egress for each location</li>
</ul>
<h3 id="top-analytics">Top analytics</h3>
<ul>
<li><strong>Top protocols</strong>: Most used network protocols (TCP, UDP, ICMP, ICMPv6)</li>
<li><strong>Top connection close reasons</strong>: Common reasons for session termination:
<ul>
<li>Client closed</li>
<li>Origin closed</li>
<li>Client idle timeout</li>
<li>Client error</li>
<li>Unknown</li>
<li>Client TLS error</li>
<li>Origin unreachable</li>
<li>Too many new sessions for user</li>
<li>Origin TLS error</li>
<li>Origin unroutable</li>
</ul>
</li>
</ul>
<p>For the full list of reasons for session termination, refer to <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/#connectionclosereason">ConnectionCloseReason</a>.</p>
<h3 id="troubleshoot-session-limit-errors">Troubleshoot session limit errors</h3>
<p>Session limit close reasons identify the type and scope of a limit. Reasons containing <code>ACTIVE_SESSIONS</code> indicate too many concurrent sessions. Reasons containing <code>NEW_SESSIONS</code> indicate that sessions are being created too quickly. <code>FOR_ACCOUNT</code> reasons aggregate sessions for the account on the Cloudflare server enforcing the limit and can affect multiple users connected to that server. <code>FOR_USER</code> reasons apply to one user.</p>
<p>Use <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a>, not Gateway activity logs, to investigate these errors. Filter by <code>ConnectionCloseReason</code>, then correlate <code>SessionStartTime</code> and <code>SessionID</code> with fields such as <code>Email</code>, <code>UserID</code>, <code>DeviceID</code>, <code>SourceIP</code>, <code>OriginIP</code>, <code>OriginPort</code>, <code>Protocol</code>, and <code>ConnectionReuse</code>.</p>
<p>Reduce automatic retries and connection churn in the affected application. Reuse connections when the application and protocol support it. If expected sustained traffic continues to produce these errors, contact your account team or <a href="/cloudflare-one/troubleshooting/contact-support/">Cloudflare Support</a> for review.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust network sessions Logpush dataset</a>: View detailed logs for individual network sessions.</li>
<li><a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a>: Configure policies that apply to network traffic.</li>
</ul>
