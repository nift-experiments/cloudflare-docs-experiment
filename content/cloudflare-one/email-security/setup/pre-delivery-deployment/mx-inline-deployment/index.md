<p>With pre-delivery deployment, also known as Inline deployment, Email security evaluates email messages before they reach a user's inbox.</p>
<p><img src="/assets/upstream/email-security/Email_security_Deployment_Inline.png" alt="Inline deployment diagram" /></p>
<p>Before you change your MX records, you will have to set up the <a href="/dns/manage-dns-records/reference/ttl/">Time to Live (TTL)</a> on your DNS records. If you do not set up the TTL, the DNS propagation will take longer to happen.</p>
<p>Cloudflare recommends to decrease the TTL to five minutes (also known as <a href="/dns/manage-dns-records/reference/ttl/#proxied-records">Auto</a>) 3 to 5 days prior to the planned MX record change. Reducing the TTL allows the DNS record to propagate ahead of time, so changes take effect rapidly. Once you have completed your onboarding process, you can choose to increase the TTL.</p>
<p>When you have configured your TTL, you can deploy Email security via MX/Inline. An MX record is a <a href="/dns/manage-dns-records/">DNS record</a>.</p>
<p>If your DNS records are hosted by Cloudflare (or any other provider, except for Google), you can <a href="/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records">edit your DNS records</a> via the dashboard or the API to point your MX records to Cloudflare.</p>
<p>By changing your MX records, Email security will be positioned between your incoming emails and Microsoft 0365 or Gmail.</p>
<p>Email security becomes a hop in the <a href="https://www.cloudflare.com/en-gb/learning/email-security/what-is-smtp/">SMTP</a> processing chain and physically interacts with incoming email messages. Based on your policies, various messages are blocked before reaching the inbox.</p>
<p>When you choose an inline deployment, you get the following benefits:</p>
<ul>
<li>Messages are processed and physically blocked before arriving in a user's mailbox.</li>
<li>Your deployment is simpler, because any complex processing can happen downstream and without modification.</li>
<li>Email security can modify delivered messages, adding subject or body mark-ups.</li>
<li>Email security can offer high availability and adaptive message pooling.</li>
<li>You can set up advanced handling downstream for non-quarantined messages with added X-headers.</li>
</ul>
