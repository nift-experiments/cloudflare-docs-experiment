<p class="article-summary">Specify multiple recipients, CC and BCC, and named addresses when sending with Email Service.</p>
<p>Email Service lets you specify recipients in several ways — multiple recipients, CC and BCC, and named addresses — using the <a href="/email-service/api/send-emails/workers-api/">Workers binding</a>, the <a href="/email-service/api/send-emails/rest-api/">REST API</a>, or <a href="/email-service/api/send-emails/smtp/">SMTP</a>. The combined number of addresses across <code>to</code>, <code>cc</code>, and <code>bcc</code> must not exceed 50. See <a href="/email-service/platform/limits/">Limits</a>.</p>
<h2 id="multiple-recipients">Multiple recipients</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="send-method"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8675.md")
</div></div>
<h2 id="cc-and-bcc">CC and BCC</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="send-method"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8679.md")
</div></div>
<h2 id="named-recipients">Named recipients</h2>
<p>Provide a display name alongside the address for the sender and recipients.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="send-method"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8683.md")
</div></div>
<h2 id="mixed-plain-and-named-recipients">Mixed plain and named recipients</h2>
<p>Combine plain addresses and named addresses in the same <code>to</code> field.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="send-method"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8687.md")
</div></div>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/email-service/api/send-emails/workers-api/">Workers API</a> — full <code>send()</code> reference.</li>
<li><a href="/email-service/api/send-emails/rest-api/">REST API</a> — send over HTTPS.</li>
<li><a href="/email-service/api/send-emails/smtp/">SMTP</a> — send from any SMTP-capable client.</li>
<li><a href="/email-service/examples/email-sending/email-attachments/">Email attachments</a> — send PDFs, inline images, and uploads.</li>
</ul>
