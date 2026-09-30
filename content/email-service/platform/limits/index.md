<p class="article-summary">Email sending quotas, rate limits, and how to request higher limits for production use</p>
<p>Cloudflare Email Service has the following limits to ensure optimal performance and prevent abuse. These limits apply to emails sent via the <a href="/email-service/api/send-emails/rest-api/">REST API</a>, the <a href="/email-service/api/send-emails/workers-api/">Workers binding</a>, and <a href="/email-service/api/send-emails/smtp/">SMTP</a> unless noted otherwise.</p>
<h2 id="daily-sending-limits">Daily sending limits</h2>
<p>New accounts start with a conservative daily quota and scale up over time based on your sending behavior, deliverability rates, and account standing. Limits are applied per account and may be adjusted automatically as your reputation improves.</p>
<p>If you need higher sending limits sooner than automatic adjustment provides, refer to &quot;Need a higher limit?&quot; at the bottom of this page to request an increase.</p>
<h2 id="verified-destination-addresses">Verified destination addresses</h2>
<p>Before you onboard a sending domain, you can send emails only to <a href="/email-service/configuration/email-routing-addresses/#destination-addresses">verified destination addresses</a> in your account. After you onboard a sending domain, you can send to any recipient immediately.</p>
<p>Sends to verified destination addresses are always free: they do not count toward your monthly <a href="/email-service/platform/pricing/">quota</a> or your daily sending limits, on any plan, including when only Email Routing is configured. You can only send from your routing domains.</p>
<h2 id="email-content-limits">Email content limits</h2>
<table>
<thead>
<tr>
<th>Component</th>
<th>Limit</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Recipients (to, cc, bcc)</strong></td>
<td>50 per email</td>
<td>Combined across all recipient fields</td>
</tr>
<tr>
<td><strong>Subject line</strong></td>
<td>998 characters</td>
<td>RFC 5322 compliant</td>
</tr>
<tr>
<td><strong>Total message size</strong></td>
<td>5 MiB</td>
<td>Including attachments</td>
</tr>
<tr>
<td><strong>Total message size</strong></td>
<td>25 MiB</td>
<td>For <a href="/email-service/configuration/email-routing-addresses/#destination-addresses">verified destination addresses</a> only</td>
</tr>
<tr>
<td><strong>Header size</strong></td>
<td>16 KB</td>
<td>All custom headers combined</td>
</tr>
</tbody>
</table>
<h2 id="suppression-list-limits">Suppression list limits</h2>
<p>The following limits apply to the Email Sending <a href="/email-service/concepts/suppressions/">suppression list</a> API:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Value</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Active entries</strong></td>
<td>1 per address</td>
<td>Enforced independently for each account</td>
</tr>
<tr>
<td><strong>Results per page</strong></td>
<td>1,000</td>
<td>Maximum <code>per_page</code> value with a default of 100</td>
</tr>
<tr>
<td><strong>Items per bulk import</strong></td>
<td>1,000</td>
<td>Split larger imports across several requests</td>
</tr>
<tr>
<td><strong>Bulk import requests</strong></td>
<td>10 per minute</td>
<td>Applies per account and returns <code>429</code> when exceeded</td>
</tr>
<tr>
<td><strong>Note length</strong></td>
<td>1,000 characters</td>
<td>The optional <code>note</code> field on an entry</td>
</tr>
</tbody>
</table>
<p>The suppression list has no total-count field. Refer to the <a href="/api/resources/email_sending/subresources/suppressions/methods/list/">list suppressions API reference</a> for pagination details.</p>
<h2 id="zone-limits">Zone limits</h2>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Value</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Domains per zone</strong></td>
<td>30</td>
<td>Combined total of domains configured for Email Routing or Email Sending in a zone, including the apex domain</td>
</tr>
</tbody>
</table>
<h2 id="email-routing-limits">Email Routing limits</h2>
<p>The following limits apply to inbound email handled by Email Routing.</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Value</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Routing rules per domain</strong></td>
<td>200</td>
<td>Each rule maps an email pattern to a destination</td>
</tr>
<tr>
<td><strong>Destination addresses per account</strong></td>
<td>200</td>
<td>Verified destination addresses are shared across all domains in the account</td>
</tr>
<tr>
<td><strong>Inbound message size</strong></td>
<td>25 MiB</td>
<td>Messages larger than this are rejected</td>
</tr>
<tr>
<td><strong>Reply <code>References</code> entries</strong></td>
<td>100</td>
<td>If the incoming email has more than 100 <code>References</code> entries, <code>message.reply()</code> throws. Reduces reply loops.</td>
</tr>
</tbody>
</table>
<p>Each routing rule maps one email pattern to one destination address or one Worker. To forward a single email pattern to multiple destinations, use a Worker that calls <code>forward()</code> once per destination. All destinations must be verified beforehand.</p>
<h3 id="routing-to-workers-on-the-workers-free-plan">Routing to Workers on the Workers Free plan</h3>
<p>Workers that handle incoming emails count toward the standard Workers CPU and memory limits. On the Workers Free plan, complex handlers may exceed these limits and fail to process a message. Failed invocations appear in <a href="/workers/observability/logs/">Workers logs</a> with the <code>EXCEEDED_CPU</code> error. Upgrade to the <a href="/workers/platform/pricing/">Workers Paid plan</a> for higher CPU and memory limits.</p>
<h3 id="emails-sent-from-workers">Emails sent from Workers</h3>
<p>Emails sent from a Worker using the <code>send_email</code> binding appear in the Email Routing summary as <strong>dropped</strong>, even when they were delivered successfully. To track outbound send success, use <a href="/email-service/observability/">Email sending metrics and logs</a> instead.</p>
<h2 id="compliance">Compliance</h2>
<p>All email sending must follow applicable anti-spam laws and regulations to maintain good standing and deliverability.</p>
<ul>
<li><strong>CAN-SPAM Act</strong> (United States)</li>
<li><strong>GDPR</strong> (European Union)</li>
<li><strong>CASL</strong> (Canada)</li>
<li>Include proper unsubscribe mechanisms</li>
<li>Honor opt-out requests promptly</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/8588.md")
</aside>
