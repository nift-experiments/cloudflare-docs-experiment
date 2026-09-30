<p class="article-summary">Configure domains for Cloudflare Email Service, manage DNS records, and verify domain setup for both email sending and routing.
</p>
<p>Configure your domains to work with Cloudflare Email Service. This includes DNS record management, domain verification, and advanced domain settings.</p>
<h2 id="automatic-dns-configuration">Automatic DNS configuration</h2>
<p>Cloudflare can configure all required DNS records for you when you onboard a domain onto Email Sending or Email Routing.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8627.md")
</div></div>
<h2 id="dns-record-configuration-details">DNS record configuration details</h2>
<p>Cloudflare automatically configures required DNS records for both email sending and routing when you onboard a domain onto Email Service.
Here are the specific details of the DNS records configured:</p>
<h3 id="sending-records">Sending records</h3>
<p>These records authenticate your outbound emails. Email Sending creates DNS records on a <code>cf-bounce.</code> subdomain of your domain to handle bounce processing. These are separate from the records used by Email Routing.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8632.md")
</div></div>
<h3 id="routing-records">Routing records</h3>
<p>These records route incoming emails to Cloudflare and authenticate forwarded emails. Email Routing DNS records are configured on the root domain.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8636.md")
</div></div>
<h2 id="domain-verification">Domain verification</h2>
<p>Email Sending and Email Routing have separate DNS records and separate settings pages where you can verify their status.</p>
<h3 id="verify-email-sending-records">Verify Email Sending records</h3>
<ol>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Sending</strong> &gt; <strong>Settings</strong>.</li>
<li>The <strong>DNS records</strong> section shows all sending-related records:
<ul>
<li><strong>MX records</strong> on <code>cf-bounce.yourdomain.com</code></li>
<li><strong>SPF record</strong> on <code>cf-bounce.yourdomain.com</code></li>
<li><strong>DKIM record</strong> on <code>cf-bounce._domainkey.yourdomain.com</code></li>
<li><strong>DMARC record</strong> on <code>_dmarc.yourdomain.com</code></li>
</ul>
</li>
<li>Each record shows either a <strong>Locked</strong> or <strong>Unlocked</strong> status. Both states indicate the record is configured correctly; the status reflects whether Email Service is managing the record. Refer to <a href="#locked-dns-records">Locked DNS records</a> for more information.</li>
</ol>
<h3 id="verify-email-routing-records">Verify Email Routing records</h3>
<ol>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Routing</strong> &gt; <strong>Settings</strong>.</li>
<li>The <strong>DNS records</strong> section shows all routing-related records:
<ul>
<li><strong>MX records</strong> on <code>yourdomain.com</code></li>
<li><strong>SPF record</strong> on <code>yourdomain.com</code></li>
<li><strong>DKIM record</strong> on <code>cf2024-1._domainkey.yourdomain.com</code></li>
</ul>
</li>
<li>Each record shows either a <strong>Locked</strong> or <strong>Unlocked</strong> status. Both states indicate the record is configured correctly; the status reflects whether Email Service is managing the record. Refer to <a href="#locked-dns-records">Locked DNS records</a> for more information.</li>
</ol>
<h3 id="if-records-are-not-configured">If records are not configured</h3>
<ul>
<li>Wait 5-15 minutes for DNS propagation.</li>
<li>Check DNS configuration in your domain's <strong>DNS</strong> &gt; <strong>Records</strong> settings.</li>
</ul>
<h3 id="locked-dns-records">Locked DNS records</h3>
<p>When Email Service onboarding succeeds, the DNS records it manages are locked to prevent accidental changes that would break mail flow. Locked records show a <strong>Locked</strong> status in the dashboard and cannot be edited or deleted from <strong>DNS</strong> &gt; <strong>Records</strong> until they are unlocked.</p>
<p>Only Email Routing records on the root domain (MX, SPF, and DKIM) support unlocking. Email Sending records on the <code>cf-bounce</code> subdomain stay managed by Email Service for the lifetime of the domain configuration.</p>
<p>To unlock an Email Routing record:</p>
<ol>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Routing</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the domain, then open <strong>Settings</strong>.</li>
<li>Locate the record in the <strong>DNS records</strong> section and select <strong>Unlock</strong>.</li>
</ol>
<p>If you want to migrate to a different email provider without immediately interrupting service, unlock the routing records first, add the new provider's records alongside them, then remove the Email Service records once the new setup is verified.</p>
<h3 id="dc-mx-dns-responses"><code>_dc-mx</code> DNS responses</h3>
<p>This section applies only if your MX records point to hostnames that are proxied through Cloudflare.</p>
<p>When an MX record on your domain points to a hostname that is proxied through Cloudflare, mail delivery to that hostname would normally fail because the Cloudflare proxy does not handle SMTP. To avoid this, Cloudflare automatically inserts a <code>_dc-mx.&lt;hash&gt;.example.com</code> record that resolves directly to the origin IP. Sending mail servers follow this record to bypass the proxy and reach the origin.</p>
<p>For more information, refer to <a href="/dns/manage-dns-records/troubleshooting/unexpected-dns-records/#dc--and-_dc-mx-subdomains">DNS troubleshooting: <code>_dc-</code> and <code>_dc-mx</code> subdomains</a>.</p>
<h3 id="verification-troubleshooting">Verification troubleshooting</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8639.md")
</div></div>
<h2 id="domain-management">Domain management</h2>
<p>Email Sending and Email Routing are managed separately. Removing one does not affect the other.</p>
<h3 id="remove-a-domain-from-email-sending">Remove a domain from Email Sending</h3>
<ol>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Sending</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the domain to remove, then open <strong>Settings</strong>.</li>
<li>Select <strong>Remove Domain</strong> and confirm the action.</li>
</ol>
<p>Removing a domain from Email Sending deletes the <code>cf-bounce</code> MX, SPF, DKIM, and DMARC records that Email Service created on the domain, and stops all outbound email sending from the domain.</p>
<h3 id="remove-a-domain-from-email-routing">Remove a domain from Email Routing</h3>
<ol>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Routing</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the domain to remove, then open <strong>Settings</strong>.</li>
<li>Select <strong>Disable Email Routing</strong> and confirm the action.</li>
</ol>
<p>Disabling Email Routing on a domain stops processing incoming emails and removes every routing-related DNS record (MX, SPF, DKIM) that Email Service added to the root domain. If you plan to switch to a different email provider, <a href="#locked-dns-records">unlock the records</a> and add the new provider's records before disabling Email Routing so that mail flow is not interrupted.</p>
<h3 id="transfer-domain-ownership">Transfer domain ownership</h3>
<ol>
<li>The domain must remain in the same Cloudflare account.</li>
<li>DNS records are tied to the account, not to specific users.</li>
<li>Use Cloudflare account-level permissions to manage access.</li>
</ol>
<h2 id="drop-suppressed-recipients">Drop suppressed recipients</h2>
<p><strong>Drop suppressed recipients</strong> controls suppression handling for one sending domain. The setting is off by default.</p>
<p>When the setting is off, a message containing any <a href="/email-service/concepts/suppressions/">suppressed recipient</a> fails. The REST API returns <code>400</code>, the Workers binding throws <code>E_RECIPIENT_SUPPRESSED</code>, and SMTP rejects the message.</p>
<p>When the setting is on, Email Service removes suppressed recipients and processes the remaining recipients.</p>
<p>To turn on the setting:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8640.md")
</div>
<h2 id="email-preview">Email preview</h2>
<p>Turn on <strong>Email preview</strong> to store sent messages so you can inspect their content in the <a href="/email-service/observability/logs/#message-preview">Activity log</a>. Previews cover messages sent while the setting is turned on and are retained for about seven days.</p>
<p>New sending domains have <strong>Email preview</strong> turned on automatically. To change the setting for a domain:</p>
<ol>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Sending</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the domain, then open <strong>Settings</strong>.</li>
<li>Toggle <strong>Enable email preview</strong>.</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><strong><a href="/email-service/api/send-emails/">Send emails API</a></strong>: Workers binding and REST API reference</li>
<li><strong><a href="/email-service/concepts/email-authentication/">Domain authentication (DKIM and SPF)</a></strong>: Learn about SPF, DKIM, and DMARC</li>
<li><strong><a href="/email-service/concepts/deliverability/">Deliverability</a></strong>: Optimize email delivery</li>
</ul>
