<p class="article-summary">Learn about SPF, DKIM, and DMARC for secure and deliverable email sending.</p>
<p>Email authentication verifies sender identity and improves deliverability. <strong>Cloudflare Email Service handles authentication automatically</strong>, but understanding these concepts helps troubleshoot issues.</p>
<h2 id="spf-sender-policy-framework">SPF (Sender Policy Framework)</h2>
<p>SPF ensures that no one else can send emails with your domain by authorizing which mail servers are allowed to send on your behalf.</p>
<p>Email Service configures separate SPF records for sending and routing:</p>
<ul>
<li><strong>Email Sending</strong> SPF record on <code>cf-bounce.yourdomain.com</code>:</li>
</ul>
<pre><code class="language-txt">TXT cf-bounce.yourdomain.com &quot;v=spf1 include:_spf.mx.cloudflare.net ~all&quot;&#10;</code></pre>
<ul>
<li><strong>Email Routing</strong> SPF record on the root domain:</li>
</ul>
<pre><code class="language-txt">TXT yourdomain.com &quot;v=spf1 include:_spf.mx.cloudflare.net ~all&quot;&#10;</code></pre>
<p>SPF works by:</p>
<ol>
<li>Publishing authorized IP addresses in DNS</li>
<li>Recipient servers checking your SPF record</li>
<li>Comparing the sending IP against authorized IPs</li>
<li>Passing or failing based on the result</li>
</ol>
<h2 id="dkim-domainkeys-identified-mail">DKIM (DomainKeys Identified Mail)</h2>
<p>DKIM ensures that emails have not been tampered during transit by cryptographically signing them with your domain's private key.</p>
<p><strong>How DKIM works:</strong></p>
<ol>
<li>Email headers and body are signed with a private key</li>
<li>DKIM-Signature header is added to the email</li>
<li>Public key is published in DNS</li>
<li>Recipients use the public key to verify the signature</li>
</ol>
<p>Email Service uses separate DKIM selectors for sending and routing:</p>
<ul>
<li><strong>Email Sending</strong>: <code>cf-bounce._domainkey.yourdomain.com</code></li>
<li><strong>Email Routing</strong>: <code>cf2024-1._domainkey.yourdomain.com</code></li>
</ul>
<p>Cloudflare automatically generates and manages DKIM keys. You add the provided DNS records from the dashboard.</p>
<h2 id="dmarc-domain-based-message-authentication-reporting-conformance">DMARC (Domain-based Message Authentication, Reporting &amp; Conformance)</h2>
<p>DMARC ensures that emails claiming to be from your domain actually pass SPF and DKIM checks, telling recipients what to do with emails that fail authentication.</p>
<p><strong>DMARC record example:</strong></p>
<pre><code class="language-txt">TXT _dmarc.yourdomain.com &quot;v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8641.md")
</aside>
<p><strong>DMARC policies:</strong></p>
<ul>
<li><code>p=none</code> - Monitor only (recommended to start)</li>
<li><code>p=quarantine</code> - Quarantine suspicious emails</li>
<li><code>p=reject</code> - Reject unauthenticated emails</li>
</ul>
<p><strong>Deployment strategy:</strong></p>
<ol>
<li>Start with <code>p=none</code> to monitor authentication</li>
<li>Gradually increase to <code>p=quarantine</code></li>
<li>Finally implement <code>p=reject</code> after confirming legitimate mail authenticates</li>
</ol>
<h2 id="key-benefits">Key benefits</h2>
<p>Email authentication provides:</p>
<ul>
<li><strong>Deliverability</strong>: Improves inbox placement</li>
<li><strong>Security</strong>: Protects your domain from spoofing</li>
<li><strong>Reputation</strong>: Maintains good sender reputation with ISPs</li>
</ul>
<p>Cloudflare Email Service handles authentication automatically, but you need to configure the DNS records for SPF, DKIM, and DMARC as provided in your dashboard. Email Sending and Email Routing use separate DNS records -- refer to <a href="/email-service/configuration/domains/">Domain configuration</a> for the full details.</p>
