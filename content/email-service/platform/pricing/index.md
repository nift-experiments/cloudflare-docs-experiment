<p>Cloudflare Email Service pricing is based on your Cloudflare plan and email usage.</p>
<h2 id="plan-pricing">Plan pricing</h2>
<p>Email Routing is available on both the Workers Free and Workers Paid plans. Sending to arbitrary recipients requires the Workers Paid plan. Sending to <a href="/email-service/configuration/email-routing-addresses/#destination-addresses">verified destination addresses</a> in your account is free on all plans, including when only Email Routing is configured.</p>
<table>
<thead>
<tr>
<th></th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Outbound emails (Email Sending)</strong></td>
<td>Not available</td>
<td>3,000 included per month, then $0.35 per 1,000 emails</td>
</tr>
<tr>
<td><strong>Inbound emails (Email Routing)</strong></td>
<td>Unlimited</td>
<td>Unlimited</td>
</tr>
</tbody>
</table>
<p>The 3,000 included emails apply per account, per month, aligned with your Cloudflare subscription billing cycle. Emails that hard-bounce or are otherwise accepted by Email Service count toward the quota. Emails rejected at the API boundary, including sends blocked by the <a href="/email-service/concepts/suppressions/">suppression list</a>, do not count toward the quota.</p>
<p>Sends to verified destination addresses are free and do not count toward the included quota.</p>
<p>Email Routing Workers is billed according to <a href="/workers/platform/pricing/">Workers pricing</a>.</p>
