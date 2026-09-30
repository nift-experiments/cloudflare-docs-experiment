<p>For maintenance expectations and notifications, refer to <a href="/network-interconnect/maintenance/">Maintenance</a>.</p>
<h2 id="customer-responsibility">Customer responsibility</h2>
<p>Your CNI deployment must tolerate an unplanned outage on any single circuit at any time. This means:</p>
<ul>
<li>Traffic failover between redundant circuits must be automatic.</li>
<li>If your operations require manual intervention to reroute traffic during maintenance, your configuration needs review.</li>
<li>Contact your account team to validate your failover design.</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>When facing connectivity problems, your first action should be to check for broader service disruptions. Visit <a href="https://www.cloudflarestatus.com/">Cloudflare Status</a> to see if any scheduled maintenance or active incidents are impacting services. This helps determine if the issue originates outside your network. Refer to <a href="/network-interconnect/monitoring-and-alerts/">Monitoring and alerts</a>.</p>
<p>If no system-wide problems are reported, gather the following information before submitting a support case. Providing comprehensive details facilitates a faster resolution:</p>
<ul>
<li><strong>Timeline</strong>: When the issue began and ended (if applicable), including the timezone.</li>
<li><strong>Identification</strong>: The CNI IP address or point-to-point prefix for the impacted CNI. If your CNI is part of a Magic setup, please also provide the name of the Magic Transit/WAN interconnect as listed in your dashboard.</li>
<li><strong>Physical Layer</strong>: Light levels of the CNI link (if applicable).</li>
<li><strong>Service Impact</strong>: Confirmation whether Magic Transit / WAN traffic was affected.</li>
<li><strong>Problem Description</strong>: A clear summary of the issue (for example, CNI down, Border Gateway Protocol (BGP) session down, prefixes withdrawn).</li>
</ul>
