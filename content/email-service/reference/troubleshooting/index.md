<p>Email authentication is critical for successful email delivery. This guide helps you troubleshoot common SPF, DKIM, and DMARC issues with Email Service.</p>
<h2 id="spf-sender-policy-framework-issues">SPF (Sender Policy Framework) issues</h2>
<h3 id="multiple-spf-records">Multiple SPF records</h3>
<p>Having multiple SPF records on your domain is not allowed and will prevent Email Service from working properly. If your domain has multiple SPF records:</p>
<ol>
<li>Log in to the Cloudflare dashboard, select your account and domain, then go to <strong>DNS</strong> &gt; <strong>Records</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Look for multiple TXT records starting with <code>v=spf1</code>.</li>
<li>Delete the incorrect SPF record.</li>
<li>Ensure you have the correct SPF records:
<ul>
<li>For <strong>Email Routing</strong> (root domain): <code>v=spf1 include:_spf.mx.cloudflare.net ~all</code></li>
<li>For <strong>Email Sending</strong> (<code>cf-bounce</code> subdomain): <code>v=spf1 include:_spf.mx.cloudflare.net ~all</code></li>
</ul>
</li>
</ol>
<p>If you are unsure which SPF record is the correct one to keep, you can remove all of them and let Cloudflare regenerate the required records:</p>
<ol>
<li>In <strong>DNS</strong> &gt; <strong>Records</strong>, delete every TXT record starting with <code>v=spf1</code> on the affected name.</li>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> and re-onboard or re-enable the affected service. Cloudflare adds the correct SPF record back automatically.</li>
</ol>
<h3 id="missing-spf-record">Missing SPF record</h3>
<p>If emails are being rejected due to SPF failures:</p>
<ol>
<li>Log in to the Cloudflare dashboard, select your account and domain, then go to <strong>DNS</strong> &gt; <strong>Records</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Add TXT records for the appropriate service:
<ul>
<li>For <strong>Email Routing</strong>: <strong>Name</strong>: <code>@</code> (root domain), <strong>Content</strong>: <code>v=spf1 include:_spf.mx.cloudflare.net ~all</code></li>
<li>For <strong>Email Sending</strong>: <strong>Name</strong>: <code>cf-bounce</code>, <strong>Content</strong>: <code>v=spf1 include:_spf.mx.cloudflare.net ~all</code></li>
</ul>
</li>
<li>If you already have an SPF record on the root domain, modify it to include <code>include:_spf.mx.cloudflare.net</code></li>
</ol>
<h3 id="spf-record-syntax-errors">SPF record syntax errors</h3>
<p>Common SPF record syntax issues:</p>
<ul>
<li><strong>Missing version</strong>: SPF records must start with <code>v=spf1</code></li>
<li><strong>Multiple includes</strong>: Combine multiple services using separate <code>include:</code> statements</li>
<li><strong>Too many DNS lookups</strong>: SPF records are limited to 10 DNS lookups total</li>
<li><strong>Incorrect all mechanism</strong>: Use <code>~all</code> (SoftFail) or <code>-all</code> (Fail), not <code>+all</code></li>
</ul>
<p><strong>Correct format:</strong></p>
<pre><code class="language-txt">v=spf1 include:_spf.mx.cloudflare.net include:other-service.com ~all&#10;</code></pre>
<h3 id="checking-spf-records">Checking SPF records</h3>
<p>Verify your SPF record is configured correctly:</p>
<pre><code class="language-sh">dig TXT example.com +short | grep spf&#10;</code></pre>
<p>Expected result should include:</p>
<pre><code class="language-txt">&quot;v=spf1 include:_spf.mx.cloudflare.net ~all&quot;&#10;</code></pre>
<h2 id="dkim-domainkeys-identified-mail-issues">DKIM (DomainKeys Identified Mail) issues</h2>
<h3 id="missing-dkim-records">Missing DKIM records</h3>
<p>Email Service automatically generates DKIM keys for your domain, but the DNS records must be properly configured. Email Sending and Email Routing use separate DKIM selectors:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Compute</strong> &gt; <strong>Email Service</strong>.</li>
<li>Select your domain.</li>
<li>Check the <strong>Settings</strong> page for the appropriate service:
<ul>
<li><strong>Email Sending</strong>: Go to <strong>Email Sending</strong> &gt; <strong>Settings</strong> to find the sending DKIM record (<code>cf-bounce._domainkey</code>).</li>
<li><strong>Email Routing</strong>: Go to <strong>Email Routing</strong> &gt; <strong>Settings</strong> to find the routing DKIM record (<code>cf2024-1._domainkey</code>).</li>
</ul>
</li>
<li>Copy the DKIM record details.</li>
<li>Go to <strong>DNS</strong> &gt; <strong>Records</strong> and add the DKIM TXT record with the correct selector name and public key.</li>
</ol>
<h3 id="dkim-key-rotation">DKIM key rotation</h3>
<p>If you need to rotate DKIM keys:</p>
<ol>
<li>Contact Cloudflare support to request key rotation.</li>
<li>Update your DNS records with the new DKIM key when provided.</li>
<li>Monitor email delivery during the transition period.</li>
</ol>
<h3 id="checking-dkim-records">Checking DKIM records</h3>
<p>Verify your DKIM records are configured correctly:</p>
<pre><code class="language-sh">&#35; Check Email Sending DKIM&#10;dig TXT cf-bounce._domainkey.example.com +short&#10;&#10;&#35; Check Email Routing DKIM&#10;dig TXT cf2024-1._domainkey.example.com +short&#10;</code></pre>
<p>Expected result for either:</p>
<pre><code class="language-txt">&quot;v=DKIM1; h=sha256; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...&quot;&#10;</code></pre>
<h3 id="dkim-signature-validation-failures">DKIM signature validation failures</h3>
<p>If DKIM validation is failing:</p>
<ol>
<li>Verify the DKIM record exists in DNS</li>
<li>Check that the record name matches the correct selector:
<ul>
<li>Email Sending: <code>cf-bounce._domainkey.yourdomain.com</code></li>
<li>Email Routing: <code>cf2024-1._domainkey.yourdomain.com</code></li>
</ul>
</li>
<li>Ensure there are no extra spaces or characters in the DNS record</li>
<li>Wait for DNS propagation (up to 48 hours)</li>
<li>Use online DKIM validators to test your configuration</li>
</ol>
<h2 id="dmarc-domain-based-message-authentication-reporting-conformance-issues">DMARC (Domain-based Message Authentication, Reporting &amp; Conformance) issues</h2>
<h3 id="missing-dmarc-policy">Missing DMARC policy</h3>
<p>While not required, DMARC significantly improves email deliverability:</p>
<ol>
<li>Go to <strong>DNS</strong> &gt; <strong>Records</strong> in the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Add a TXT record:
<ul>
<li><strong>Name</strong>: <code>_dmarc</code></li>
<li><strong>Content</strong>: <code>v=DMARC1; p=quarantine; rua=mailto:dmarc@example.com</code></li>
</ul>
</li>
</ol>
<h3 id="dmarc-policy-too-strict">DMARC policy too strict</h3>
<p>If a strict DMARC policy is causing delivery issues:</p>
<ol>
<li>Start with a lenient policy: <code>p=none</code> (monitor only)</li>
<li>Monitor DMARC reports for several weeks</li>
<li>Gradually increase strictness: <code>p=quarantine</code> then <code>p=reject</code></li>
<li>Ensure both SPF and DKIM are properly aligned</li>
</ol>
<h3 id="dmarc-alignment-issues">DMARC alignment issues</h3>
<p>DMARC requires either SPF or DKIM alignment:</p>
<p><strong>SPF alignment</strong>: The domain in the <code>Mail From</code> header must align with the domain in the <code>From</code> header
<strong>DKIM alignment</strong>: The DKIM signature domain must align with the domain in the <code>From</code> header</p>
<p>Email Service ensures proper alignment automatically.</p>
<h3 id="checking-dmarc-records">Checking DMARC records</h3>
<p>Verify your DMARC record:</p>
<pre><code class="language-sh">dig TXT _dmarc.example.com +short&#10;</code></pre>
<p>Example result:</p>
<pre><code class="language-txt">&quot;v=DMARC1; p=quarantine; rua=mailto:dmarc@example.com; ruf=mailto:dmarc@example.com; sp=quarantine&quot;&#10;</code></pre>
<h2 id="local-development-issues">Local development issues</h2>
<h3 id="cannot-serialize-value-object-arraybuffer">&quot;Cannot serialize value: [object ArrayBuffer]&quot;</h3>
<p>This error occurs when passing <code>ArrayBuffer</code> content in attachment fields during local development with <code>wrangler dev</code>. The local email binding simulator cannot serialize <code>ArrayBuffer</code> values.</p>
<p><strong>Solution:</strong> Deploy your Worker with <code>npx wrangler deploy</code> and test binary attachments (images, PDFs) against the deployed version. String content for text-based attachments works normally in local development. Refer to <a href="/email-service/local-development/sending/#known-limitations">local development for email sending</a> for more details.</p>
<h2 id="common-delivery-issues">Common delivery issues</h2>
<h3 id="email-going-to-spam">Email going to spam</h3>
<p>If emails are going to spam folders:</p>
<ol>
<li>Check authentication: Ensure SPF, DKIM, and DMARC are properly configured</li>
<li>Domain reputation: New domains may have lower reputation initially</li>
<li>Content quality: Avoid spam trigger words and excessive HTML formatting</li>
<li>Sender reputation: Monitor bounce rates and complaint rates</li>
<li>List hygiene: Remove bounced and invalid email addresses</li>
</ol>
<h3 id="high-bounce-rates">High bounce rates</h3>
<p>To reduce bounce rates:</p>
<ol>
<li>Validate email addresses: Use real-time validation</li>
<li>Maintain clean lists: Remove hard bounces immediately</li>
<li>Monitor feedback loops: Subscribe to ISP feedback loops</li>
<li>Gradual warm-up: For new domains, start with small volumes</li>
</ol>
<h3 id="suppressed-recipient">Suppressed recipient</h3>
<p>Each sending domain has a <a href="/email-service/configuration/domains/#drop-suppressed-recipients"><strong>Drop suppressed recipients</strong> setting</a>. The setting is off by default.</p>
<p>When the setting is off, the REST API returns <code>400</code>, the Workers binding throws <code>E_RECIPIENT_SUPPRESSED</code>, and SMTP rejects the message. Any suppressed recipient causes the send to fail.</p>
<p>When the setting is on, Email Service removes suppressed recipients and processes the remaining recipients. If none remain, SMTP may return <code>250 2.0.0 Ok</code> without a Message-ID and deliver nothing.</p>
<p>To investigate a suppressed recipient:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8583.md")
</div>
<h3 id="recipient-blocked-after-expiration-or-deletion">Recipient blocked after expiration or deletion</h3>
<p>Expired entries stop appearing in the public list after their <code>expires_at</code> timestamp passes. Delivery enforcement can take additional time to stop.</p>
<p>Updates and deletions also propagate asynchronously. The management list and delivery enforcement can briefly differ.</p>
<p>To investigate delayed enforcement:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8584.md")
</div>
<h3 id="bounces-before-suppression-enforcement">Bounces before suppression enforcement</h3>
<p>Bounce suppressions are created through background delivery processing. Messages already in progress can bounce before a new suppression takes effect.</p>
<h3 id="complaint-suppression-does-not-appear">Complaint suppression does not appear</h3>
<p>Complaint suppressions appear after Cloudflare receives and validates the provider report. The provider determines when that report arrives.</p>
<h3 id="missing-suppression-after-a-bounce">Missing suppression after a bounce</h3>
<p>Not every failure results in a suppression. Email Service creates automatic entries only for eligible recipient-side failures. Sender authentication, sender reputation, and unrelated infrastructure failures do not suppress the recipient. Check <a href="/email-service/observability/logs/">Email sending logs</a> for the specific failure.</p>
<h3 id="isp-specific-issues">ISP-specific issues</h3>
<p>Different ISPs have specific requirements:</p>
<ul>
<li>Gmail: Requires strong domain reputation and authentication</li>
<li>Outlook/Hotmail: Sensitive to content and sender reputation</li>
<li>Yahoo: Strict DMARC enforcement</li>
<li>Corporate: Often have strict filtering rules</li>
</ul>
<h2 id="testing-tools">Testing tools</h2>
<p>Use these tools to validate your email authentication setup:</p>
<ol>
<li>MX Toolbox: Check SPF, DKIM, and DMARC records</li>
<li>DMARC Analyzer: Validate DMARC policy and alignment</li>
<li>Mail Tester: Test email deliverability and authentication</li>
<li>Google Admin Toolbox: Google's email authentication checker</li>
</ol>
<h2 id="getting-help">Getting help</h2>
<p>If you continue to experience authentication issues:</p>
<ol>
<li>Check the <a href="/email-service/observability/metrics-analytics/">Email Service analytics</a> for delivery metrics</li>
<li>Review bounce messages for specific error codes</li>
<li>Contact <a href="https://dash.cloudflare.com/?to=/:account/support">Cloudflare Support</a> with:
<ul>
<li>Domain name</li>
<li>Example email headers</li>
<li>Specific error messages</li>
<li>SPF, DKIM, and DMARC record configurations</li>
</ul>
</li>
</ol>
