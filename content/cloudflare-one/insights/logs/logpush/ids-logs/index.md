<p>You can use Logpush with <a href="/cloudflare-network-firewall/about/ids/">Cloudflare Network Firewall IDS</a> (Intrusion Detection System) to export logs of detected threats. IDS monitors your network traffic for a wide range of known threat signatures, including attacks such as ransomware, data exfiltration, and network scanning.</p>
<h2 id="set-up-logpush-for-ids">Set up Logpush for IDS</h2>
<ol>
<li>
<p>Consult the <a href="/logs/logpush/logpush-job/api-configuration/#destination">Logpush Destination docs</a> to learn about what destinations Logpush supports. The documentation will also instruct you on how to correctly format the destination URL for Logpush.</p>
</li>
<li>
<p>Follow the <a href="/logs/logpush/examples/example-logpush-curl/">Manage Logpush with cURL</a> tutorial to validate your Logpush destination and define a Logpush job.</p>
</li>
</ol>
<h2 id="notes-on-using-logpush-with-ids">Notes on using Logpush with IDS</h2>
<ul>
<li>
<p>Magic IDS is an account-scoped dataset. Unlike zone-specific datasets that apply to a single domain, account-scoped datasets use a different API endpoint. Replace the string <code>/zone/&lt;ZONE_ID&gt;</code> in the Cloudflare API URLs in the tutorial with <code>/account/&lt;ACCOUNT_ID&gt;</code>.</p>
</li>
<li>
<p>Consult the <a href="/logs/logpush/logpush-job/datasets/account/magic_ids_detections/">Magic IDS Detection fields doc</a> to know what fields you want configured for the job.</p>
</li>
<li>
<p>When creating the Logpush job, the dataset field should equal <code>magic_ids_detections</code>.</p>
</li>
<li>
<p>Timestamps default to <code>unixnano</code> format (nanoseconds since the Unix epoch, January 1, 1970). If your destination expects a different format (such as RFC 3339), refer to <a href="/logs/logpush/logpush-job/api-configuration/#options">Logpush Options</a> for available timestamp formats. In the Logpush API configuration string, options are appended after the field list.</p>
</li>
</ul>
