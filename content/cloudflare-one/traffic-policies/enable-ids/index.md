<p>Cloudflare's Intrusion Detection System (IDS) is a Cloudflare Advanced Network Firewall feature you can use to actively monitor for a wide range of known threat signatures in your traffic. An IDS expands the security coverage of a firewall to analyze traffic against a broader threat database, detecting a variety of sophisticated attacks such as ransomware, data exfiltration, and network scanning based on signatures or “fingerprints” in network traffic.</p>
<p>With Cloudflare's global anycast network, you get:</p>
<ul>
<li>Cloudflare's entire global network capacity is now the capacity of your IDS.</li>
<li>Built-in redundancy and failover. Every server runs Cloudflare's IDS software, and traffic is automatically attracted to the closest network location to its source.</li>
<li>Continuous deployment for improvements to Cloudflare's IDS capabilities.</li>
</ul>
<p>Refer to <a href="/cloudflare-one/traffic-policies/enable-ids/#enable-ids">Enable IDS</a> for more information on enabling IDS and creating new rulesets. After IDS is enabled, your traffic will be scanned to find malicious traffic. The detections are logged to destinations that can be configured from the dashboard. Refer to <a href="/cloudflare-one/insights/logs/logpush/ids-logs/">IDS logs</a> for instructions on configuring a destination to receive the detections. Additionally, all traffic that is analyzed can be accessed via <a href="/analytics/network-analytics/">network analytics</a>. Refer to <a href="/cloudflare-network-firewall/tutorials/graphql-analytics/">GraphQL Analytics</a> to query the analytics data.</p>
<p>Cloudflare's IDS takes advantage of the threat intelligence powered by our global network and extends the capabilities of the Cloudflare Firewall to monitor and protect your network from malicious actors.</p>
<h2 id="enable-ids">Enable IDS</h2>
<p>You can enable IDS through the dashboard or via the API.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4418.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4421.md")
</div></div>
<h2 id="ids-rules">IDS rules</h2>
<p>IDS rules are run on a subset of packets. IDS also supports the current flows:</p>
<ul>
<li>Cloudflare WAN to Cloudflare WAN.</li>
<li>Magic Transit ingress traffic (when egress traffic is handled through direct server return).</li>
<li>Magic Transit ingress and egress traffic when Magic Transit has the <a href="/reference-architecture/architectures/magic-transit/#magic-transit-with-egress-option-enabled">Egress option enabled</a>.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<p>You must configure Logpush to log detected risks. Refer to <a href="/cloudflare-network-firewall/how-to/use-logpush-with-ids/">Configure a Logpush destination</a> for more information. Additionally, all traffic that is analyzed can be accessed via <a href="/analytics/network-analytics/">network analytics</a>. Refer to <a href="/cloudflare-network-firewall/tutorials/graphql-analytics/">GraphQL Analytics</a> to query the analytics data.</p>
