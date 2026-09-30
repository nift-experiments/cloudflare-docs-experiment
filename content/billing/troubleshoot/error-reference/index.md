<p>Use the tables below to find common billing error messages, understand what they mean, and go to the right solution.</p>
<p>When troubleshooting, start with the exact error message. Then confirm whether the account has an unpaid balance, an active subscription, a pending cancellation, or a pending payment transaction.</p>
<h2 id="error-messages">Error messages</h2>
<table>
<thead>
<tr>
<th>Error message</th>
<th>Cause</th>
<th>What to do first</th>
</tr>
</thead>
<tbody>
<tr>
<td>&quot;You cannot add or modify subscriptions or services until the outstanding balance is paid.&quot;</td>
<td>Your account has an unpaid balance.</td>
<td><a href="/billing/manage/pay-invoices-overdue-balances/">Pay the outstanding balance</a>.</td>
</tr>
<tr>
<td>&quot;The payment has failed. Please contact your bank or use a different payment method.&quot;</td>
<td>Your payment method was declined by your bank.</td>
<td>Check your card details and bank balance, then retry. Refer to <a href="/billing/troubleshoot/troubleshoot-failed-payments/">Resolve a payment failure</a>.</td>
</tr>
<tr>
<td>&quot;Payment error: authorization failed&quot;</td>
<td>Your bank declined the transaction, or 3DS authentication was not completed.</td>
<td>Contact your bank and retry the payment. Refer to <a href="/billing/troubleshoot/troubleshoot-failed-payments/">Resolve a payment failure</a>.</td>
</tr>
<tr>
<td>&quot;This zone cannot be upgraded&quot;</td>
<td>The account or a previous owner of the domain has an outstanding balance.</td>
<td>Pay the balance on all accounts you have access to, wait 24 hours, then retry. Refer to <a href="/billing/troubleshoot/resolve-zone-cannot-be-upgraded/">Resolve the zone cannot be upgraded error</a>.</td>
</tr>
<tr>
<td>&quot;There is a problem with your billing profile&quot;</td>
<td>Same as &quot;this zone cannot be upgraded&quot; — an unpaid balance exists.</td>
<td><a href="/billing/manage/pay-invoices-overdue-balances/">Pay the outstanding balance</a> and wait 24 hours.</td>
</tr>
<tr>
<td>&quot;You cannot modify this subscription since it is currently scheduled to be cancelled&quot;</td>
<td>You are trying to change a subscription that already has a pending cancellation.</td>
<td>Cancel the pending downgrade first, then make your change. Refer to <a href="/billing/troubleshoot/resolve-you-cannot-modify-this-subscription/">Resolve &quot;you cannot modify this subscription&quot;</a>.</td>
</tr>
<tr>
<td>&quot;You can't remove this payment method while it's linked to active subscriptions.&quot;</td>
<td>You are trying to delete a payment method that is still tied to paid services.</td>
<td>Cancel all paid subscriptions first, or add a replacement payment method. Refer to <a href="/billing/troubleshoot/resolve-cannot-remove-payment-method/">Resolve &quot;cannot remove payment method&quot;</a>.</td>
</tr>
<tr>
<td>&quot;You can't remove a payment method while there are transactions in progress.&quot;</td>
<td>A usage-based charge is pending, or a Registrar renewal is scheduled within 24 hours.</td>
<td>Wait for pending transactions to complete, then retry. Refer to <a href="/billing/troubleshoot/resolve-cannot-remove-payment-method/">Resolve &quot;cannot remove payment method&quot;</a>.</td>
</tr>
</tbody>
</table>
<h2 id="email-notifications">Email notifications</h2>
<table>
<thead>
<tr>
<th>Email subject</th>
<th>What it means</th>
<th>What to do first</th>
</tr>
</thead>
<tbody>
<tr>
<td>&quot;We couldn't process your renewal payment&quot;</td>
<td>A recurring subscription charge failed. Cloudflare will retry up to 5 times over 5 days.</td>
<td>Update your payment method or manually pay the invoice before the grace period ends. Refer to <a href="/billing/troubleshoot/troubleshoot-failed-payments/">Resolve a payment failure</a>.</td>
</tr>
</tbody>
</table>
<h2 id="still-stuck">Still stuck?</h2>
<p>If your error message is not listed above or the suggested solution does not resolve the issue, <a href="/support/contacting-cloudflare-support/">contact Cloudflare support</a>. Include the account ID, invoice number, exact error message, and the action you were trying to complete.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/troubleshoot/troubleshoot-failed-payments/">Resolve a payment failure</a> — Fix payment errors</li>
<li><a href="/billing/manage/pay-invoices-overdue-balances/">Pay an outstanding balance</a> — Resolve unpaid invoices</li>
<li><a href="/billing/understand/how-billing-works/">How Cloudflare billing works</a> — Billing lifecycle and charge types</li>
</ul>
