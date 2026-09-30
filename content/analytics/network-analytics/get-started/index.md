<aside class="nb-aside note">
<h3 class="nb-aside-title" id="requirements">Requirements</h3>
@markup("md", "content/.markup/bodies/3127.md")
</aside>
<h2 id="view-the-network-analytics-dashboard">View the Network Analytics dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Network Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select an account that has access to Magic Transit or Spectrum.</li>
<li>Configure the displayed data. You can <a href="/analytics/network-analytics/configure/time-range/">adjust the time range</a>, <a href="/analytics/network-analytics/configure/displayed-data/#select-high-level-metric">select the main metric</a> (total packets or total bytes), <a href="/analytics/network-analytics/configure/displayed-data/#apply-filters">apply filters</a>, and more.</li>
</ol>
<h2 id="get-network-analytics-data-via-api">Get Network Analytics data via API</h2>
<p>Use the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> to query data using the available <a href="/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/">Network Analytics nodes</a>.</p>
<h2 id="send-network-analytics-logs-to-a-third-party-service">Send Network Analytics logs to a third-party service</h2>
<p><a href="/logs/logpush/logpush-job/enable-destinations/">Create a Logpush job</a> that sends Network analytics logs to your storage service, <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3128.md")
</div>, or log management provider.
<h2 id="limitations">Limitations</h2>
<p>Users with the <code>Analytics</code> role will have visibility to IDs but will not see the following on the Network Analytics dashboard:</p>
<ul>
<li>Tunnel names</li>
<li>Prefix names</li>
<li><a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> rules</li>
<li><a href="/ddos-protection/managed-rulesets/">DDoS managed rulesets</a></li>
<li>Override names</li>
</ul>
