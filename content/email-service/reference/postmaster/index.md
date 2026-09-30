<p>This page provides technical information about Email Service to professionals who administer email systems, and other email providers.</p>
<p>Here you will find information regarding Email Service, along with best practices, rules, guidelines, troubleshooting tools, as well as configuration details for Email Service.</p>
<h2 id="postmaster">Postmaster</h2>
<h3 id="contact-information">Contact information</h3>
<p>The best way to contact us is using our <a href="https://community.cloudflare.com/new-topic?category=Feedback/Previews%20%26%20Betas&amp;tags=email">community forum</a> or our <a href="https://discord.cloudflare.com">Discord server</a>.</p>
<p>To report email abuse, contact us at <a href="mailto:mailabuse@cloudflare.com">mailabuse@cloudflare.com</a>.</p>
<h3 id="authenticated-received-chain-arc">Authenticated Received Chain (ARC)</h3>
<p>Email Service supports <a href="https://arc-spec.org/">Authenticated Received Chain (ARC)</a>. ARC allows intermediate email servers, such as forwarders, to attach a record of the original authentication results to a message. The destination server can then verify the authenticity of forwarded messages even when SPF or DKIM would otherwise fail due to forwarding. Major providers, including Google, also support ARC.</p>
<h3 id="dkim-signature">DKIM signature</h3>
<p><a href="https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail">DKIM (DomainKeys Identified Mail)</a> ensures that email messages are not altered in transit between the sender and the recipient's SMTP servers through public-key cryptography.</p>
<p>Through this standard, the sender publishes its public key to a domain's DNS once, and then signs the body of each message before it leaves the server. The recipient server reads the message, gets the domain public key from the domain's DNS, and validates the signature to ensure the message was not altered in transit.</p>
<p>Email Service adds DKIM signatures to outgoing emails on behalf of the customer's sending domain to ensure email authenticity and improve deliverability.</p>
<p>Email Sending and Email Routing use separate DKIM selectors. You can find the DKIM keys for your domain by querying the following:</p>
<pre><code class="language-sh">&#35; Email Sending DKIM&#10;dig TXT cf-bounce._domainkey.example.com +short&#10;&#10;&#35; Email Routing DKIM&#10;dig TXT cf2024-1._domainkey.example.com +short&#10;</code></pre>
<p>For forwarded emails, Email Routing adds two DKIM signatures: one for <code>email.cloudflare.net</code>, which covers <a href="#sender-rewriting">sender rewriting</a>, and one for the recipient domain configured by the customer. You can query the Cloudflare sender rewriting key directly:</p>
<pre><code class="language-sh">dig TXT cf2024-1._domainkey.email.cloudflare.net +short&#10;</code></pre>
<h3 id="dmarc-enforcing">DMARC enforcing</h3>
<p>Email Service supports Domain-based Message Authentication, Reporting &amp; Conformance (DMARC). When sending emails, Email Service ensures proper SPF and DKIM alignment to pass DMARC authentication. For Email Routing, incoming emails are rejected if they fail authentication according to the sender's DMARC policy. Refer to <a href="https://dmarc.org/">dmarc.org</a> for more information on this protocol.</p>
<p>It is recommended that all domains implement the DMARC protocol for optimal email deliverability.</p>
<h3 id="mail-authentication-requirement">Mail authentication requirement</h3>
<p>Cloudflare requires incoming emails to pass some form of authentication. The email must either pass SPF or be correctly signed with DKIM. Emails that fail both checks are rejected.</p>
<p>Outbound emails sent through Email Service are always authenticated with both SPF and DKIM to maximize deliverability and maintain sender reputation.</p>
<h3 id="ipv6-support">IPv6 support</h3>
<p>Email Service supports IPv6 for both inbound and outbound email delivery. For outbound, the service connects to recipient SMTP servers over IPv6 when the recipient has AAAA records for their MX servers, and falls back to IPv4 otherwise. For inbound, Email Routing accepts mail over IPv6 on its MX servers.</p>
<p>You can verify IPv6 connectivity for any destination using <code>dig</code>:</p>
<pre><code class="language-sh">dig mx gmail.com&#10;dig AAAA gmail-smtp-in.l.google.com&#10;</code></pre>
<h3 id="mx-and-spf-records">MX and SPF records</h3>
<p>When using Email Service for sending emails, no special MX records are required on your domain. However, if you are also using Email Routing for inbound emails, the appropriate MX records are configured automatically.</p>
<p>For SPF records, Email Service uses <code>_spf.mx.cloudflare.net</code>. Email Sending configures SPF on the <code>cf-bounce</code> subdomain, while Email Routing configures SPF on the root domain:</p>
<pre><code class="language-txt">v=spf1 include:_spf.mx.cloudflare.net ~all&#10;</code></pre>
<p>For inbound mail, Email Routing announces multiple MX servers under the <code>*.mx.cloudflare.net</code> zone with different priorities. For example:</p>
<pre><code class="language-txt">example.com.    IN    MX    13 amir.mx.cloudflare.net.&#10;example.com.    IN    MX    86 linda.mx.cloudflare.net.&#10;example.com.    IN    MX    24 isaac.mx.cloudflare.net.&#10;</code></pre>
<h3 id="outbound-prefixes">Outbound prefixes</h3>
<p>Email Service sends its traffic using both IPv4 and IPv6 prefixes, when supported by the recipient SMTP server.</p>
<p>If you are a postmaster and are having trouble receiving Email Service emails, allow the following outbound IP addresses in your server configuration:</p>
<p><strong>IPv4</strong></p>
<p><code>104.30.0.0/19</code></p>
<p><strong>IPv6</strong></p>
<p><code>2405:8100:c000::/38</code></p>
<p>To verify the current authoritative ranges, query the SPF record directly:</p>
<pre><code class="language-sh">dig TXT _spf.mx.cloudflare.net +short&#10;</code></pre>
<h3 id="outbound-hostnames">Outbound hostnames</h3>
<p>Email Service will use the following outbound domains for the <code>HELO/EHLO</code> command:</p>
<ul>
<li><code>cloudflare-email.net</code></li>
<li><code>cloudflare-email.org</code></li>
<li><code>cloudflare-email.com</code></li>
</ul>
<p>PTR records (reverse DNS) ensure that each hostname has a corresponding IP. For example:</p>
<pre><code class="language-sh">dig a-h.cloudflare-email.net +short&#10;</code></pre>
<pre><code class="language-sh">104.30.0.7&#10;</code></pre>
<pre><code class="language-sh">dig -x 104.30.0.7 +short&#10;</code></pre>
<pre><code class="language-sh">a-h.cloudflare-email.net.&#10;</code></pre>
<h3 id="sender-rewriting">Sender rewriting</h3>
<p>For forwarded emails, Email Routing uses the <a href="https://en.wikipedia.org/wiki/Sender_Rewriting_Scheme">Sender Rewriting Scheme</a> to rewrite the envelope sender (the SMTP <code>MAIL FROM</code> address) to a Cloudflare-controlled forwarding domain. This rewriting allows SPF to pass at the destination server even though the message is being relayed. The <code>From:</code> header of the message is not modified.</p>
<h3 id="smtp-errors">SMTP errors</h3>
<p>Email Service provides detailed SMTP error responses to help diagnose delivery issues. For Email Routing, upstream SMTP errors returned by the destination mail server are forwarded back to the sending server in-session rather than as a separate bounce message.</p>
<h3 id="realtime-block-lists">Realtime Block Lists</h3>
<p>Email Service monitors sender reputation and may temporarily delay or block emails from IPs that appear on Realtime Block Lists (RBLs). This helps maintain the service's overall reputation and deliverability.</p>
<p>For Email Routing, inbound mail from senders on RBLs is rejected with an SMTP error similar to:</p>
<pre><code class="language-txt">554 &lt;YOUR_IP_ADDRESS&gt; found on one or more RBLs (abusixip). Refer to https://developers.cloudflare.com/email-service/reference/postmaster/#realtime-block-lists&#10;</code></pre>
<p>You can use tools like <a href="https://mxtoolbox.com/blacklists.aspx">MxToolbox</a> to check a sending IP against multiple block lists at once. If you believe your emails are being incorrectly blocked, contact the RBL maintainer directly or reach out through Cloudflare support channels.</p>
<h3 id="spf-record-breakdown">SPF record breakdown</h3>
<p>Email Service publishes its SPF data under <code>_spf.mx.cloudflare.net</code>. You can resolve the underlying record directly:</p>
<pre><code class="language-sh">dig TXT _spf.mx.cloudflare.net +short&#10;</code></pre>
<p>The record uses the format defined in <a href="https://datatracker.ietf.org/doc/html/rfc7208">RFC 7208</a>:</p>
<pre><code class="language-txt">&quot;v=spf1 ip4:104.30.0.0/20 ~all&quot;&#10;</code></pre>
<p>The <code>~all</code> mechanism is a SoftFail. Receiving servers should treat mail from IPs not listed in the record as suspicious but should not reject it outright on SPF alone.</p>
<hr />
<h2 id="related-configuration">Related configuration</h2>
<p>For full configuration details, refer to:</p>
<ul>
<li><a href="/email-service/configuration/domains/">Domain configuration</a> — DNS records, sending and routing setup</li>
<li><a href="/email-service/platform/limits/">Limits</a> — rate limits, sending quotas, and message size limits</li>
<li><a href="/email-service/concepts/deliverability/">Deliverability</a> — bounce handling and reputation management</li>
<li><a href="/email-service/concepts/suppressions/">Suppression lists</a> — automatic and manual suppression management</li>
</ul>
<hr />
<h2 id="known-limitations">Known limitations</h2>
<p>Below, you will find information regarding known limitations for Email Service, particularly Email Routing functionality.</p>
<h3 id="email-address-internationalization-eai">Email address internationalization (EAI)</h3>
<p>Email Routing does not support <a href="https://en.wikipedia.org/wiki/International_email">internationalized email addresses</a>. Email Routing only supports <a href="https://en.wikipedia.org/wiki/Internationalized_domain_name">internationalized domain names</a>.</p>
<p>This means that you can have email addresses with an internationalized domain, but not an internationalized local-part (the first part of your email address, before the @ symbol). Refer to the following examples:</p>
<ul>
<li><code>info@piñata.es</code> - <strong>Supported</strong></li>
<li><code>piñata@piñata.es</code> - <strong>Not supported</strong></li>
</ul>
<h3 id="non-delivery-reports-ndrs">Non-delivery reports (NDRs)</h3>
<p>Email Routing does not forward non-delivery reports to the original sender. This means the sender will not receive a notification indicating that the email did not reach the intended destination.</p>
<h3 id="restrictive-dmarc-policies-can-make-forwarded-emails-fail">Restrictive DMARC policies can make forwarded emails fail</h3>
<p>Due to the nature of email forwarding, restrictive DMARC policies might make forwarded emails fail to be delivered. Refer to <a href="https://dmarc.org/">dmarc.org</a> for more information.</p>
<h3 id="sending-or-replying-to-an-email-from-your-cloudflare-domain">Sending or replying to an email from your Cloudflare domain</h3>
<p>Email Routing does not support sending or replying from your Cloudflare domain. When you reply to emails forwarded by Email Routing, the reply will be sent from your destination address (like <code>my-name@gmail.com</code>), not from the email pattern of the routing rule that delivered the message (like <code>info@yourdomain.com</code>).</p>
<h3 id="is-treated-as-a-normal-character-in-email-patterns">&quot;.&quot; is treated as a normal character in email patterns</h3>
<p>The <code>.</code> character, which performs special actions in email providers like Gmail, is treated as a normal character in routing rule email patterns.</p>
