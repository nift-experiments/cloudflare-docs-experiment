<p>You can configure alerts to receive notifications for changes in your secondary DNS.</p>
<details><summary>Secondary DNS all Primaries Failing</summary><strong>Who is it for?</strong><p>Enterprise customers who have at least one secondary zone in their account and want to receive a notification if all of their primary nameservers are failing.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Secondary DNS</p>
<strong>What should you do if you receive one?</strong><ol>
<li>Confirm that your primary nameservers are up and running.</li>
<li>Confirm that the <a href="/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/">Access Control Lists (ACLs)</a> on your primary nameservers are configured correctly.</li>
<li>Confirm that your primary nameservers are configured correctly in your Cloudflare account (correct IP, port, TSIG).</li>
</ol>
</details><details><summary>Secondary DNS Primaries Failing</summary><strong>Who is it for?</strong><p>Enterprise customers who have at least one secondary zone and want to receive a notification if at least one of their primary nameservers is failing while transfers from at least one other primary are still successful.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Secondary DNS.</p>
<strong>What should you do if you receive one?</strong><ol>
<li>Confirm that your primary nameservers are up and running.</li>
<li>Confirm that the <a href="/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/">Access Control Lists (ACLs)</a> on your primary nameservers are configured correctly.</li>
<li>Confirm that your primary nameservers are configured correctly in your Cloudflare account (correct IP, port, TSIG).</li>
</ol>
</details><details><summary>Secondary DNS Successfully Updated</summary><strong>Who is it for?</strong><p>Enterprise customers who have at least one secondary zone in their account and want to receive a notification on successful zone transfers.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Secondary DNS.</p>
<strong>What should you do if you receive one?</strong><p>No action needed. Everything is working correctly.</p>
</details><details><summary>Secondary DNS Warning</summary><strong>Who is it for?</strong><p>Customers who are using Cloudflare for Secondary DNS and want to receive notifications about warnings issued by the transferred zone.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><p>Actions for failure notifications will depend on the type of failure.</p>
</details>
<p>Refer to <a href="/notifications/get-started/">Cloudflare Notifications</a> for more information on how to set up an alert.</p>
