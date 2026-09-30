<ol>
<li>On the <a href="https://horizon.area1security.com/">Email security (formerly Area 1) dashboard</a>, select <strong>Domains</strong> under <strong>DOMAINS &amp; ROUTING</strong>, then select <strong>NEW DOMAIN</strong>. Fill in the information to add a new domain:
<ul>
<li>On <strong>FORWARDING TO</strong>: Enter <code>Google.com</code>.</li>
<li>Adjust <strong>Hops</strong> to 2.</li>
<li>On <strong>Outbound TLS</strong>: Ensure you select <strong>Forward all messages over TLS</strong>.</li>
</ul>
</li>
<li>Select <strong>Publish Domain</strong>.</li>
<li>Select <strong>RETRACT SETTINGS</strong> &gt; <strong>Authorize Gmail</strong>.</li>
<li>Upload the JSON file <a href="/email-security/deployment/api/setup/gsuite-bcc-setup/create-service-account/">previously generated</a>.</li>
<li>Under <strong>DOMAINS</strong>, select the domain you added previously, then select <strong>SAVE</strong>.</li>
</ol>
<h2 id="post-delivery-retractions-for-new-threats">Post delivery retractions for new threats</h2>
<p>Email security (formerly Area 1) is continuously gathering new information about phishing campaigns. Users might have email messages in their inboxes that were scanned by Email security but not retracted initially because, at the time of scan, these email messages had not been identified as a threat. To mitigate risk, Email security offers you tools to re-evaluate email messages at a fixed time interval based on knowledge Cloudflare may have acquired since initial delivery. Any email messages that fit this new threat knowledge will be retracted.</p>
<p>You can enable two options:</p>
<ul>
<li><strong>Post Delivery Response</strong>: Email security will continue to re-evaluate emails already delivered to your users' inboxes at a fixed time interval in search for phishing sites or campaigns not previously known to Cloudflare. If any email messages fitting these new criteria are found, Email security retracts them.</li>
<li><strong>Phish Submission Response</strong>: Email security will retract emails already delivered that are reported by your users as phishing, and are found to be malicious by Email security. Retraction will occur according to your configuration.</li>
</ul>
