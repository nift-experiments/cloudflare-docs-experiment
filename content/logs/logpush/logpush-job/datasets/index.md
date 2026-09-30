<h2 id="datasets">Datasets</h2>
<p>The datasets below describe the fields available by log category:</p>
<ul>
<li><a href="/logs/logpush/logpush-job/datasets/zone/">Zone-scoped datasets</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/account/">Account-scoped datasets</a></li>
</ul>
<h2 id="api">API</h2>
<p>The list of fields can also be accessed directly from the API using the following endpoints:</p>
<ul>
<li>
<p>For zone-scoped datasets: <code>https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/datasets/&lt;DATASET&gt;/fields</code></p>
</li>
<li>
<p>For account-scoped datasets: <code>https://api.cloudflare.com/client/v4/accounts/{account_id}/logpush/datasets/&lt;DATASET&gt;/fields</code></p>
</li>
</ul>
<p>The <code>&lt;DATASET&gt;</code> argument indicates the log category. For example, <code>http_requests</code>, <code>spectrum_events</code>, <code>firewall_events</code>, <code>nel_reports</code>, or <code>dns_logs</code>.</p>
<h2 id="availability">Availability</h2>
<ul>
<li>The availability of Logpush dataset fields depends on your subscription plan.</li>
<li>Zone-scoped HTTP requests are available in both Logpush and Logpull.</li>
<li><a href="/logs/logpush/logpush-job/custom-fields/">Custom fields</a> for HTTP requests are only available in Logpush.</li>
<li>All other datasets are only available through Logpush.</li>
</ul>
<h2 id="deprecation">Deprecation</h2>
<p>Deprecated fields remain available to prevent breaking existing jobs. They may eventually become empty values if completely removed. Customers are encouraged to migrate away from deprecated fields if they are using them.</p>
<h2 id="recommendation">Recommendation</h2>
<p>For log field <strong>ClientIPClass</strong>, Cloudflare recommends using <a href="/bots/concepts/bot-tags/">bot tags</a> to classify IPs.</p>
<h2 id="additional-resources">Additional resources</h2>
<p>For more information on logs available in Cloudflare Zero Trust, refer to <a href="/cloudflare-one/insights/logs/">Zero Trust logs</a>.</p>
