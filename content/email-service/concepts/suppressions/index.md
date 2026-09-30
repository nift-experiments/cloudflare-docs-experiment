<p class="article-summary">Suppression lists prevent Email Service from sending to recipients who should not receive mail. Cloudflare adds entries after eligible bounces and spam complaints. You can also add entries manually.
</p>
<p>An Email Sending suppression list contains recipients that Email Service does not contact. Suppressions protect your sender reputation and help prevent sending unwanted mail.</p>
<p>Cloudflare creates suppressions after eligible delivery failures and spam complaints. You can also add entries for recipients who should not receive mail.</p>
<p>To add or remove entries, refer to <a href="/email-service/configuration/suppressions/">Manage suppressions</a>. Suppressions only apply to Email Sending.</p>
<h2 id="suppression-scope">Suppression scope</h2>
<p>Suppressions are account-scoped. Once an email address is on the suppression list, Email Service suppresses sends to that address from every domain in your account.</p>
<p>If you need separate suppression lists for different use cases, consider using separate Cloudflare accounts.</p>
<h2 id="suppression-rules">Suppression rules</h2>
<p>The following table describes automatic and manual creation rules and expiration:</p>
<table>
<thead>
<tr>
<th>Reason</th>
<th>Created when</th>
<th>Expiration</th>
</tr>
</thead>
<tbody>
<tr>
<td>Manual (<code>manual</code>)</td>
<td>You add the recipient through the dashboard or API</td>
<td>The time you choose, or no expiration</td>
</tr>
<tr>
<td>Spam complaint (<code>complaint</code>)</td>
<td>Cloudflare receives and validates a complaint from the recipient's email provider</td>
<td>No expiration</td>
</tr>
<tr>
<td>Hard bounce (<code>hard_bounce</code>)</td>
<td>Any other eligible recipient-side permanent rejection occurs</td>
<td>7 days</td>
</tr>
<tr>
<td>Hard bounce (<code>hard_bounce</code>)</td>
<td>The recipient mailbox or domain does not exist, or a recipient-side issue persists across repeated delivery attempts</td>
<td>No expiration</td>
</tr>
<tr>
<td>Soft bounce (<code>soft_bounce</code>)</td>
<td>An eligible recipient-side temporary failure occurs, such as a full mailbox or rate limit</td>
<td>24 hours by default</td>
</tr>
</tbody>
</table>
<p>The <a href="/api/resources/email_sending/subresources/suppressions/">account Email Sending suppression management REST API</a> can return Cloudflare-managed entries with a <code>policy</code> reason. Clients must use <code>read_only</code> to determine mutability, not infer it from <code>reason</code>.</p>
<p>You cannot update or delete an entry when <code>read_only</code> is <code>true</code>. To investigate one, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a>.</p>
<h3 id="manual-suppressions">Manual suppressions</h3>
<p>Manual suppressions allow you to add application-level decisions that Email Service cannot observe. For example, if a user manually unsubscribes from emails in your app, you can add their email to your Email Service suppression list.</p>
<p>You select the expiration when creating the entry. An entry without an expiration remains active until you delete it.</p>
<h3 id="spam-complaints">Spam complaints</h3>
<p>Email providers send feedback reports when recipients mark messages as spam. Cloudflare validates these reports before creating complaint suppressions.</p>
<p>Complaint suppressions are created without an expiration. You can change or delete one when <code>read_only</code> is <code>false</code>.</p>
<p>We recommend changing or deleting one only after the recipient opts in again through your application.</p>
<h3 id="hard-bounces">Hard bounces</h3>
<p>A hard bounce is a permanent rejection of one delivery attempt. Some addresses become valid again after their owner fixes the mailbox or domain.</p>
<p>Email Service creates a suppression without an expiration when the mailbox or domain does not exist. It also does this when a recipient-side issue persists across repeated delivery attempts without a successful delivery.</p>
<p>Other eligible hard-bounce suppressions last seven days.</p>
<h3 id="soft-bounces">Soft bounces</h3>
<p>A soft bounce is a temporary recipient-side failure. Examples include a full mailbox, a temporarily unavailable server, or recipient-side rate limiting.</p>
<p>Eligible soft-bounce suppressions last 24 hours by default. Email Service resumes sending after the suppression expires.</p>
<p>Not every temporary delivery failure creates a suppression. For example, Email Service does not suppress a recipient for a sender-side authentication or reputation problem.</p>
<h2 id="enforcement-by-sending-method">Enforcement by sending method</h2>
<p>Each sending domain has a <a href="/email-service/configuration/domains/#drop-suppressed-recipients"><strong>Drop suppressed recipients</strong> setting</a>. The setting is off by default.</p>
<table>
<thead>
<tr>
<th>Sending method</th>
<th>Setting off</th>
<th>Setting on</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/email-service/api/send-emails/rest-api/">REST API</a></td>
<td>Returns <code>400</code> and rejects the request when any recipient is suppressed.</td>
<td>Removes suppressed recipients and processes the remaining recipients.</td>
</tr>
<tr>
<td><a href="/email-service/api/send-emails/workers-api/">Workers binding</a></td>
<td>Throws <code>E_RECIPIENT_SUPPRESSED</code> and rejects the <code>send()</code> call when any recipient is suppressed.</td>
<td>Removes suppressed recipients and processes the remaining recipients.</td>
</tr>
<tr>
<td><a href="/email-service/api/send-emails/smtp/">SMTP</a></td>
<td>Rejects the message when any recipient is suppressed.</td>
<td>Removes suppressed recipients and processes the remaining recipients. If none remain, SMTP may return <code>250 2.0.0 Ok</code> without a Message-ID and delivers nothing.</td>
</tr>
</tbody>
</table>
<p>Suppressed recipients do not count toward your <a href="/email-service/platform/pricing/">monthly quota</a> or daily sending limits. They appear as <strong>Rejected</strong> in <a href="/email-service/observability/logs/">Email sending logs</a>.</p>
<h2 id="best-practices">Best practices</h2>
<ul>
<li>Add manual suppressions for unsubscribes.</li>
<li>Require recipients to opt in again through your application.</li>
<li>Verify addresses before deleting suppressions.</li>
<li>Investigate patterns across repeated bounces.</li>
<li>Let temporary suppressions expire automatically.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Use <a href="/email-service/configuration/suppressions/">Manage suppressions</a> to manage entries through the dashboard or API.</li>
<li>Review <a href="/email-service/concepts/deliverability/">Email deliverability</a> to understand bounce and complaint effects.</li>
<li>Follow <a href="/email-service/concepts/email-lifecycle/">Email lifecycle</a> to locate suppression checks in the sending flow.</li>
<li>Review <a href="/email-service/platform/limits/#suppression-list-limits">Suppression list limits</a> for API limits.</li>
<li>Use <a href="/email-service/observability/logs/">Email sending logs</a> to investigate rejected sends.</li>
</ul>
