<p>If you have issues sending or receiving mail, follow these troubleshooting steps.</p>
<h2 id="are-your-records-correct">Are your records correct?</h2>
<p>To check that your MX records are resolving correctly, run the following <code>dig</code> command in your terminal (replace <code>example.com</code> with your domain):</p>
<pre><code class="language-sh">dig example.com mx +short&#10;</code></pre>
<p>Alternatively, you can use a third-party tool to look up your MX records. For a list of options, refer to <a href="/dns/reference/recommended-third-party-tools/">Recommended third-party tools</a>.</p>
<p>This returns a list of mail servers for your domain. Compare the output to the MX records on your Cloudflare DNS records page.</p>
<div class="nb-dash-button"></div>
<p>If the mail server listed does not match your email provider's expected value, update the MX record content to the correct value. Check your email provider's setup documentation for the correct MX record values.</p>
<p>If your DNS query returns records you do not recognize, such as <code>_dc-mx</code> or <code>dc-#####</code> subdomains, refer to <a href="/dns/manage-dns-records/troubleshooting/unexpected-dns-records/#_dc-mx-and-dc--subdomains">Unexpected DNS records</a>.</p>
<h2 id="are-dns-records-missing">Are DNS records missing?</h2>
<p>If <code>dig</code> returns no results for your domain's MX records, your records may not have been created or may have been accidentally deleted.</p>
<p>Even if your MX records are correct, missing email authentication records can cause delivery failures:</p>
<ul>
<li><strong>Missing <code>SPF</code> record:</strong> receiving servers cannot verify that your domain authorizes the sending server, which may cause messages to be rejected or marked as spam.</li>
<li><strong>Missing <code>DKIM</code> record:</strong> messages cannot be cryptographically verified as originating from your domain, which reduces trust with receiving servers.</li>
<li><strong>Missing <code>DMARC</code> record:</strong> receiving servers have no policy for handling messages that fail <code>SPF</code> or <code>DKIM</code> checks, which can lead to inconsistent delivery or spoofing of your domain.</li>
</ul>
<p>Refer to <a href="/dns/manage-dns-records/how-to/email-records/">Set up email records</a> to add missing records.</p>
<h2 id="do-your-mx-records-point-to-a-delegated-subdomain">Do your MX records point to a delegated subdomain?</h2>
<p><code>NS</code> records <a href="/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/#delegate-a-subdomain-outgoing">delegate a subdomain</a> to another DNS provider. If your MX record points to a subdomain that is delegated via <code>NS</code> records (for example, <code>mail.example.com</code>), the mail server records are managed by that external provider, not Cloudflare. Confirm that the external provider has the correct <code>A</code> or <code>AAAA</code> records for the mail subdomain.</p>
<h2 id="is-cname-flattening-turned-on">Is CNAME flattening turned on?</h2>
<p>Some email providers require <code>CNAME</code> records for features like DKIM authentication or autodiscover. When <a href="/dns/cname-flattening/">CNAME flattening</a> is turned on — either globally for all <code>CNAME</code> records or individually on a specific record — the <code>CNAME</code> is flattened to an <code>A</code> record, which can prevent email providers from reading the record correctly.</p>
<p>If your email provider requires <code>CNAME</code> records and those records are not resolving as expected, you may need to turn off <a href="/dns/cname-flattening/set-up-cname-flattening/">CNAME flattening</a>.</p>
<h2 id="is-your-mail-hostname-proxied">Is your mail hostname proxied?</h2>
<p>Mail protocols such as SMTP, IMAP, and POP3 do not work through Cloudflare's standard HTTP proxy.</p>
<p>If the hostname used for mail resolves to a Cloudflare IP address, the record is proxied and mail clients will not be able to connect correctly.</p>
<p>Common examples include:</p>
<ul>
<li><code>mail.example.com</code> used for SMTP, IMAP, or POP3</li>
<li>Any hostname targeted by your <code>MX</code> record</li>
<li>Autodiscover or mail service hostnames that must return the provider's actual DNS target</li>
</ul>
<p>To fix this issue:</p>
<ol>
<li>Go to the <strong>DNS Records</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Locate the mail-related hostname.</li>
<li>Change the <a href="/dns/proxy-status/">proxy status</a> to <strong>DNS only</strong>.</li>
</ol>
<p>Your <code>MX</code> record itself is always DNS-only, but the hostname it points to must also resolve to a DNS-only target.</p>
<h2 id="common-provider-record-values">Common provider record values</h2>
<p>If you are not sure whether the DNS content itself is correct, compare it with the values from your provider.</p>
<p>Common examples include:</p>
<table>
<thead>
<tr>
<th>Provider</th>
<th>MX records</th>
<th>SPF record</th>
</tr>
</thead>
<tbody>
<tr>
<td>Google Workspace</td>
<td><code>ASPMX.L.GOOGLE.COM</code> (priority <code>1</code>), <code>ALT1.ASPMX.L.GOOGLE.COM</code> and <code>ALT2.ASPMX.L.GOOGLE.COM</code> (priority <code>5</code>), <code>ALT3.ASPMX.L.GOOGLE.COM</code> and <code>ALT4.ASPMX.L.GOOGLE.COM</code> (priority <code>10</code>)</td>
<td><code>v=spf1 include:_spf.google.com ~all</code></td>
</tr>
<tr>
<td>Microsoft 365</td>
<td><code>&lt;your-domain&gt;.mail.protection.outlook.com</code> (priority <code>0</code>)</td>
<td><code>v=spf1 include:spf.protection.outlook.com -all</code></td>
</tr>
<tr>
<td>iCloud Mail</td>
<td><code>mx01.mail.icloud.com</code> and <code>mx02.mail.icloud.com</code> (priority <code>10</code>)</td>
<td><code>v=spf1 include:icloud.com ~all</code></td>
</tr>
<tr>
<td>Mailgun</td>
<td><code>mxa.mailgun.org</code> and <code>mxb.mailgun.org</code> (priority <code>10</code>)</td>
<td><code>v=spf1 include:mailgun.org ~all</code></td>
</tr>
</tbody>
</table>
<p>Always confirm the exact values with your provider before making changes.</p>
<h2 id="is-cloudflare-spectrum-turned-on">Is Cloudflare Spectrum turned on?</h2>
<p>Cloudflare does not proxy email traffic (SMTP, port 25) by default. Unless you have explicitly configured <a href="/spectrum/reference/configuration-options#smtp">Cloudflare Spectrum</a> to proxy SMTP traffic, email is delivered directly to your mail server and does not pass through the Cloudflare network. DNS records used for email should be set to <a href="/dns/proxy-status/">DNS only</a> to ensure mail traffic is not affected by the proxy.</p>
<div class="nb-dash-button"></div>
<h2 id="is-email-routing-turned-on">Is Email Routing turned on?</h2>
<p>If <a href="/email-service/">Email Routing</a> is turned on, Cloudflare manages your MX records and may create additional DNS records automatically.</p>
<div class="nb-dash-button"></div>
<p>If Email Routing is turned on but you use a different mail provider, the Email Routing MX records may conflict with your provider's records. You can <a href="/email-service/configuration/domains/#remove-a-domain-from-email-routing">turn off Email Routing</a> to remove the managed records and configure your own.</p>
<hr />
<h2 id="best-practices-for-mx-records-on-cloudflare">Best practices for MX records on Cloudflare</h2>
<p>If possible, do not host a mail service on the same server as the web resource you want to protect, since emails sent to non-existent addresses get bounced back to the attacker and reveal the mail server IP address.</p>
<p>Cloudflare recommends using non-contiguous IPs from different IP ranges.</p>
<hr />
<h2 id="contact-your-mail-provider-for-assistance">Contact your mail provider for assistance</h2>
<p>If your email does not work shortly after editing DNS records, contact your mail administrator or mail provider with the specific error or bounce message you are receiving. They can confirm whether the issue is with DNS resolution, mail server configuration, or message delivery.</p>
<p>If your provider confirms the issue is related to Cloudflare, <a href="/support/contacting-cloudflare-support/">contact Cloudflare support</a>.</p>
