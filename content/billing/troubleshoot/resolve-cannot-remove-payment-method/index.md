<p>When attempting to remove a payment method, you may see one of the following error messages:</p>
<ul>
<li>&quot;You can't remove this payment method while it's linked to active subscriptions. Go to Billing to manage subscriptions.&quot;</li>
<li>&quot;You can't remove a payment method while there are transactions in progress. Make sure all transactions are completed and all subscriptions are cancelled.&quot;</li>
</ul>
<h2 id="causes">Causes</h2>
<ul>
<li>You still have active paid subscriptions.</li>
<li>You have canceled your paid subscriptions, but a usage-based charge is still scheduled.</li>
<li>You have an upcoming Registrar domain registration renewal within the next 24 hours.</li>
</ul>
<h2 id="solutions">Solutions</h2>
<h3 id="check-for-active-paid-subscriptions">Check for active paid subscriptions</h3>
<p>You can only remove a payment method after all paid subscriptions are canceled and outstanding charges are settled.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3389.md")
</div>
<p>Repeat this for all active paid subscriptions before attempting to remove the payment method.</p>
<h3 id="check-for-usage-based-products">Check for usage-based products</h3>
<p>If you have canceled all paid subscriptions, any usage-based products canceled within the last 30 days may still generate charges. Your payment method must remain on file until those charges are processed. If you recently canceled any of the following products, wait 30 days before removing your payment method:</p>
<table>
<thead>
<tr>
<th>Product</th>
<th>Billable metric</th>
<th>Free tier or included usage</th>
<th>Pricing details</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/workers/platform/pricing/">Workers</a></td>
<td>Requests and CPU time</td>
<td>10M requests and 30M CPU-ms</td>
<td><a href="/workers/platform/pricing/">Workers pricing</a></td>
</tr>
<tr>
<td><a href="/r2/pricing/">R2</a></td>
<td>Storage and operations</td>
<td>10 GB storage, 1M Class A operations, and 10M Class B operations</td>
<td><a href="/r2/pricing/">R2 pricing</a></td>
</tr>
<tr>
<td><a href="/argo-smart-routing/">Argo Smart Routing</a></td>
<td>Data transfer</td>
<td>First 1 GB</td>
<td><a href="/argo-smart-routing/">Argo Smart Routing</a></td>
</tr>
<tr>
<td><a href="/cache/advanced-configuration/cache-reserve/">Cache Reserve</a></td>
<td>Reads, writes, and storage</td>
<td>None</td>
<td><a href="/cache/advanced-configuration/cache-reserve/">Cache Reserve</a></td>
</tr>
<tr>
<td><a href="/load-balancing/">Load Balancing</a></td>
<td>DNS queries</td>
<td>First 500K queries</td>
<td><a href="/load-balancing/">Load Balancing</a></td>
</tr>
<tr>
<td><a href="/stream/pricing/">Stream</a></td>
<td>Minutes stored and minutes viewed</td>
<td>Varies by plan</td>
<td><a href="/stream/pricing/">Stream pricing</a></td>
</tr>
<tr>
<td><a href="/images/pricing/">Images</a></td>
<td>Transformations and storage</td>
<td>Varies by plan</td>
<td><a href="/images/pricing/">Images pricing</a></td>
</tr>
<tr>
<td><a href="/spectrum/">Spectrum</a></td>
<td>Data transfer</td>
<td>None</td>
<td><a href="/spectrum/">Spectrum</a></td>
</tr>
<tr>
<td><a href="/waf/rate-limiting-rules/">Rate Limiting</a></td>
<td>Rule requests</td>
<td>Varies by plan</td>
<td><a href="/waf/rate-limiting-rules/">Rate Limiting</a></td>
</tr>
<tr>
<td><a href="/log-explorer/pricing/">Log Explorer</a></td>
<td>Log storage and queries</td>
<td>Varies by plan</td>
<td><a href="/log-explorer/pricing/">Log Explorer pricing</a></td>
</tr>
<tr>
<td><a href="/cloudflare-one/">Zero Trust</a></td>
<td>Seats and usage-based services</td>
<td>Varies by plan</td>
<td><a href="/cloudflare-one/">Zero Trust</a></td>
</tr>
<tr>
<td><a href="/vectorize/platform/pricing/">Vectorize</a></td>
<td>Stored dimensions and queried vectors</td>
<td>Varies by plan</td>
<td><a href="/vectorize/platform/pricing/">Vectorize pricing</a></td>
</tr>
<tr>
<td><a href="/analytics/analytics-engine/pricing/">Analytics Engine</a></td>
<td>Data points read and written</td>
<td>Varies by plan</td>
<td><a href="/analytics/analytics-engine/pricing/">Analytics Engine pricing</a></td>
</tr>
</tbody>
</table>
<p>After the next monthly invoice is generated, you can remove the payment method.</p>
<h3 id="check-for-an-upcoming-registrar-renewal">Check for an upcoming Registrar renewal</h3>
<p>For Registrar domains scheduled for auto-renewal, we will attempt to renew approximately 30 days before your renewal date. In the 24 hours prior to that, we will automatically process a payment hold using your payment method. During this time you will be unable to remove your payment method.</p>
<p>To check if any of your domains are in the renewal process:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3390.md")
</div>
<p>If you have any domains with auto-renewal turned on that are expiring in 31 days or less, wait for them to renew before you remove your payment method. To understand more about this process, refer to <a href="/registrar/account-options/renew-domains/">Renew domains</a>.</p>
<h2 id="verify-the-fix">Verify the fix</h2>
<p>After you clear active subscriptions, pending usage-based charges, and upcoming Registrar renewals, return to <strong>Payment</strong> &gt; <strong>Payment methods</strong> and try to remove the payment method again.</p>
<h2 id="if-none-of-the-above-apply">If none of the above apply</h2>
<p>If none of the above apply and you still receive an error, <a href="/support/contacting-cloudflare-support/">contact Cloudflare support</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/get-started/update-billing-info/">Update billing information</a> — Add a replacement payment method</li>
<li><a href="/billing/manage/cancel-subscription/">Cancel subscriptions</a> — Cancel subscriptions before removing a payment method</li>
<li><a href="/billing/troubleshoot/error-reference/">Error reference</a> — Look up other billing error messages</li>
</ul>
