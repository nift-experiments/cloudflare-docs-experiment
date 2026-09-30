<h2 id="which-fields-or-columns-are-available-for-querying">Which fields (or columns) are available for querying?</h2>
<p>All fields listed in <a href="/logs/logpush/logpush-job/datasets/">Datasets</a> for the <a href="/log-explorer/manage-datasets/#supported-datasets">supported datasets</a> are viewable in Log Explorer.</p>
<h2 id="why-is-the-matchedrules-field-empty-for-some-requests">Why is the <code>MatchedRules</code> field empty for some requests?</h2>
<p><code>MatchedRules</code> is populated only by security and transformation rules (WAF, Rate Limiting, Transform Rules, Snippets). Cache rules do not populate this field. If you are investigating cache behavior, use the <code>Cache*</code> fields such as <code>CacheCacheStatus</code> instead.</p>
<h2 id="why-does-my-query-not-complete-or-time-out">Why does my query not complete or time out?</h2>
<p>Log Explorer performs best when query parameters focus on narrower ranges of time. You may experience query timeouts when your query would return a large quantity of data. Consider refining your query to improve performance.</p>
<h2 id="why-do-i-not-see-any-logs-in-my-queries-after-enabling-the-dataset">Why do I not see any logs in my queries after enabling the dataset?</h2>
<p>Log Explorer starts ingesting logs from the moment you enable the dataset. It will not display logs for events that occurred before the dataset was enabled. Make sure that new events have been generated since enabling the dataset, and check again.</p>
<h2 id="my-query-returned-an-error-how-do-i-figure-out-what-went-wrong">My query returned an error. How do I figure out what went wrong?</h2>
<p>We are actively working on improving error codes. If you receive a generic error, check your SQL syntax (if you are using the custom SQL feature), and make sure you have included a date and a limit. If the query still fails it is likely timing out. Try refining your filters.</p>
<h2 id="where-is-the-data-stored">Where is the data stored?</h2>
<p>The data is stored in Cloudflare R2. Each Log Explorer dataset is stored on a per-customer level, similar to Cloudflare D1, ensuring that your data is kept separate from that of other customers. In the future, this single-tenant storage model will provide you with the flexibility to create your own retention policies and decide in which regions you want to store your data.</p>
<h2 id="does-log-explorer-support-customer-metadata-boundary">Does Log Explorer support Customer Metadata Boundary?</h2>
<p>Customer Metadata Boundary is currently not supported for Log Explorer.</p>
<h2 id="are-there-any-constraints-on-the-log-volume-that-log-explorer-can-support">Are there any constraints on the log volume that Log Explorer can support?</h2>
<p>We are continually scaling the Log Explorer data platform. At present, Log Explorer supports log ingestion rates of up to 50,000 records per second. If your needs exceed this, contact your account team.</p>
<h2 id="how-is-log-explorer-different-from-logpush-do-i-need-both">How is Log Explorer different from Logpush? Do I need both?</h2>
<p>Log Explorer allows you to search and analyze your Cloudflare logs directly in the dashboard or via API. <a href="/logs/logpush/">Logpush</a>, on the other hand, delivers raw logs to third-party SIEMs or storage systems. You generally do not need both, but some customers choose to use Log Explorer for quick investigation and Logpush for long-term storage or integration with other tools.</p>
<h2 id="is-there-a-free-version-or-trial-of-log-explorer">Is there a free version or trial of Log Explorer?</h2>
<p>Log Explorer is available as a paid add-on for any Application Services or Zero Trust purchase. There is no free version at this time.</p>
<h2 id="how-is-log-explorer-billed">How is Log Explorer billed?</h2>
<p>Log Explorer billing is based on the volume of logs indexed and stored, measured in gigabytes (GB). Your charges scale with the amount of log data you choose to retain in Log Explorer. Unlike query-based billing models (for example, BigQuery), charges are not based on how often you search or scan your data. Once logs are ingested and stored, you can query them without additional cost.</p>
<h2 id="are-logs-from-attack-traffic-included-in-my-log-explorer-usage">Are logs from attack traffic included in my Log Explorer usage?</h2>
<p>Yes. In general, Log Explorer bills based on the total volume of logs ingested and stored, including attack traffic. Since these logs are often critical for investigating security incidents, they are treated the same as all other log data.</p>
<p>However, logs generated from Layer 7 (L7) DDoS attack traffic are not ingested by default and therefore do not count toward your Log Explorer usage.</p>
<h2 id="how-does-log-explorer-store-data-in-r2-and-why-do-i-not-see-it-in-my-own-r2-bucket">How does Log Explorer store data in R2, and why do I not see it in my own R2 bucket?</h2>
<p>Log Explorer uses Cloudflare Logpush and R2 behind the scenes to stream and store logs. For technical and performance reasons, the data is stored in internal, customer-specific R2 buckets managed by Cloudflare. These buckets are single-tenant to keep your data isolated, but they are not visible in your account's R2 interface. You are not billed separately for this storage — it is included in your Log Explorer usage.</p>
<h2 id="are-custom-dashboards-based-on-r2-log-explorer-data-or-on-graphql">Are Custom Dashboards based on R2 Log Explorer data, or on GraphQL?</h2>
<p>Custom Dashboards use <a href="/analytics/graphql-api/sampling/">GraphQL</a> for standard analytics datasets.</p>
<p>Customers with Log Explorer can also select Log Explorer datasets to create charts from raw, unsampled log data. This is supported on all plans and account types, with no additional enablement required.</p>
<p>You cannot turn a saved or active Log Explorer query directly into a Custom Dashboard chart.</p>
<p>For more information, refer to <a href="/analytics/custom-dashboards/">Custom dashboards</a>.</p>
<h2 id="how-can-i-track-my-log-explorer-usage">How can I track my Log Explorer usage?</h2>
<p>Your monthly usage is displayed at the top of the Log Search and Manage Datasets dashboard sections within Log Explorer.</p>
<p><img src="/assets/upstream/images/log-explorer/log-explorer-usage.png" alt="Usage display in the dashboard" /></p>
<h2 id="how-do-i-turn-off-log-explorer">How do I turn off Log Explorer?</h2>
<p>To turn off Log Explorer you must:</p>
<ol>
<li><strong>Stop log ingestion to immediately stop incurring additional charges.</strong> To stop log ingestion, disable any enabled datasets at both the account level and zone level.</li>
<li><strong>Cancel the Log Explorer subscription to stop renewal.</strong> Your subscription may remain active until the end of the current billing cycle.</li>
</ol>
<h3 id="1-stop-log-ingestion"><ol>
<li>Stop log ingestion</li>
</ol></h3>
<p>After performing the following steps, you will immediately stop incurring additional charges for Log Explorer.</p>
<h4 id="review-and-disable-account-level-datasets">Review and disable account-level datasets</h4>
<ol>
<li>In the Cloudflare dashboard, go to the account-level <strong>Manage datasets</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Turn off each dataset you no longer need using the toggle. To confirm each operation, select <strong>Stop ingesting logs</strong>.</li>
</ol>
<h4 id="review-and-disable-zone-level-datasets">Review and disable zone-level datasets</h4>
<ol>
<li>In the Cloudflare dashboard, go to the zone-level <strong>Manage datasets</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Turn off each dataset you no longer need using the toggle. To confirm each operation, select <strong>Stop ingesting logs</strong>.</p>
</li>
<li>
<p>Repeat for all relevant zones.</p>
</li>
</ol>
<h3 id="2-cancel-the-log-explorer-subscription"><ol start="2">
<li>Cancel the Log Explorer subscription</li>
</ol></h3>
<p>This operation will stop Log Explorer's renewal.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Billing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In the <strong>Subscriptions</strong> tab, find the Log Explorer subscription and select <strong>Cancel</strong>.</li>
</ol>
