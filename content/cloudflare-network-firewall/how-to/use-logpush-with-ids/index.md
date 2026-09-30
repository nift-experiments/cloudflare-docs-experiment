<p>You can use Logpush with Cloudflare Network Firewall (formerly Magic Firewall) IDS to log detected risks:</p>
<ol>
<li>
<p>Consult the <a href="/logs/logpush/logpush-job/api-configuration/#destination">Logpush Destination docs</a> to learn about what destinations Logpush supports. The documentation will also instruct you on how to correctly format the destination URL for Logpush.</p>
</li>
<li>
<p>Follow the <a href="/logs/logpush/examples/example-logpush-curl/">Manage Lopush with cURL</a> tutorial to validate your Logpush destination and define a Logpush job.</p>
</li>
</ol>
<h2 id="notes-on-using-logpush-with-ids">Notes on using Logpush with IDS</h2>
<ul>
<li>
<p>Magic IDS is an account-scoped dataset. This means the string <code>/zone/&lt;ZONE_ID&gt;</code> in the Cloudflare API URLs in the tutorial should be replaced with <code>/account/&lt;ACCOUNT_ID&gt;</code>.</p>
</li>
<li>
<p>Consult the <a href="/logs/logpush/logpush-job/datasets/account/magic_ids_detections/">Magic IDS Detection fields doc</a> to know what fields you want configured for the job.</p>
</li>
<li>
<p>When creating the Logpush job, the dataset field should equal <code>magic_ids_detections</code>.</p>
</li>
<li>
<p>Timestamps by default are unixnano. Consult the <a href="/logs/logpush/logpush-job/api-configuration/#options">Logpush Options docs</a> to learn what format you can choose that will be compatible with your destination and/or expectations. Note that all options must be added <em>after</em> all fields you want from the Logpush job, akin to URL parameters.</p>
</li>
</ul>
