<p>Cloudflare Email Service exposes an authenticated SMTP submission endpoint so you can send emails from any application, framework, or off-the-shelf mail client that speaks SMTP. Use SMTP when the <a href="/email-service/api/send-emails/rest-api/">REST API</a> and the <a href="/email-service/api/send-emails/workers-api/">Workers binding</a> are not a good fit — for example, when integrating an existing application that already speaks SMTP, or a language-native SMTP library (Nodemailer, <code>smtplib</code>, PHPMailer, JavaMail).</p>
<p>Emails submitted over SMTP enter the same delivery pipeline as the REST API and the Workers binding: they are subject to the same <a href="/email-service/platform/limits/">limits</a>, receive the same DKIM and ARC signing, and produce the same delivery logs.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">smtp.mx.cloudflare.net:465&#10;</code></pre>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td><code>smtp.mx.cloudflare.net</code></td>
</tr>
<tr>
<td>Port</td>
<td><code>465</code></td>
</tr>
<tr>
<td>Security</td>
<td>Implicit TLS (also called SMTPS)</td>
</tr>
<tr>
<td>SMTP <code>AUTH</code></td>
<td><code>PLAIN</code> or <code>LOGIN</code></td>
</tr>
<tr>
<td>Username</td>
<td>The literal string <code>api_token</code></td>
</tr>
<tr>
<td>Password</td>
<td>A Cloudflare API token (see below)</td>
</tr>
</tbody>
</table>
<p>Cloudflare only offers SMTP submission on port <code>465</code> with implicit TLS. Plaintext SMTP, opportunistic <code>STARTTLS</code> on port <code>587</code>, and unauthenticated relay on port <code>25</code> are not supported for outbound submission. Port <code>25</code> is reserved for inbound mail to <a href="/email-service/api/route-emails/">Email Routing</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you can send emails over SMTP, you need:</p>
<ol>
<li>An account with <a href="/email-service/">Email Sending</a> enabled.</li>
<li>At least one <a href="/email-service/configuration/domains/">domain onboarded</a> under <strong>Email Service &gt; Email Sending</strong> in the Cloudflare dashboard.</li>
<li>A <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> with the <strong>Email Sending: Edit</strong> permission. Both account-owned (recommended) and user-owned tokens are accepted; the token is used as the SMTP password.</li>
</ol>
<p>Treat this token as a credential. Anyone with it can send email from any onboarded domain on the matching account.</p>
<h2 id="quickstart">Quickstart</h2>
<p>Send an email with a single <code>curl</code> command. Replace <code>&lt;API_TOKEN&gt;</code> with a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> that has the <strong>Email Sending: Edit</strong> permission, and replace the <code>--mail-from</code> and <code>--mail-rcpt</code> addresses with your own.</p>
<pre><code class="language-sh">cat &gt; mail.txt &lt;&lt;EOF&#10;From: welcome@yourdomain.com&#10;To: recipient@example.com&#10;Subject: Welcome to our service!&#10;&#10;Thanks for signing up.&#10;EOF&#10;&#10;curl --ssl-reqd \&#10;  &#45;-url &quot;smtps://smtp.mx.cloudflare.net:465&quot; \&#10;  &#45;-user &quot;api_token:&lt;API_TOKEN&gt;&quot; \&#10;  &#45;-mail-from &quot;welcome@yourdomain.com&quot; \&#10;  &#45;-mail-rcpt &quot;recipient@example.com&quot; \&#10;  &#45;-upload-file mail.txt&#10;</code></pre>
<p>The sender domain (<code>welcome@yourdomain.com</code>) must be onboarded for <a href="/email-service/configuration/domains/">Email Sending</a> on the account that owns the API token.</p>
<h2 id="authentication">Authentication</h2>
<p>Cloudflare's SMTP endpoint supports two SASL mechanisms, both defined by <a href="https://datatracker.ietf.org/doc/html/rfc4954">RFC 4954</a>:</p>
<ul>
<li><code>AUTH PLAIN</code> — preferred. Single round trip, <a href="https://datatracker.ietf.org/doc/html/rfc4616">RFC 4616</a>.</li>
<li><code>AUTH LOGIN</code> — legacy <a href="https://datatracker.ietf.org/doc/html/draft-murchison-sasl-login-00">draft-murchison-sasl-login</a>. Supported for compatibility with older clients.</li>
</ul>
<p>In both cases, the username is the literal string <code>api_token</code> and the password is your Cloudflare API token.</p>
<h3 id="construct-an-auth-plain-payload">Construct an <code>AUTH PLAIN</code> payload</h3>
<p><code>AUTH PLAIN</code> sends <code>\0api_token\0&lt;API_TOKEN&gt;</code> encoded as base64:</p>
<pre><code class="language-sh">printf &#x27;\0api_token\0%s&#x27; &quot;&lt;API_TOKEN&gt;&quot; | base64&#10;</code></pre>
<h3 id="raw-smtp-transcript">Raw SMTP transcript</h3>
<p>The following transcript shows a complete authenticated submission using <code>openssl s_client</code>. Lines beginning with <code>&gt;</code> are sent by the client.</p>
<pre><code class="language-txt">$ openssl s_client -quiet -connect smtp.mx.cloudflare.net:465 -crlf&#10;220 mx.cloudflare.net Cloudflare Email ESMTP Service ready&#10;&gt; EHLO client.example.com&#10;250-mx.cloudflare.net greets client.example.com&#10;250-AUTH PLAIN LOGIN&#10;250-SIZE 5242880&#10;250-8BITMIME&#10;250 ENHANCEDSTATUSCODES&#10;&gt; AUTH PLAIN AGFwaV90b2tlbgBpd0RQLi5oZWw=&#10;235 2.7.0 Authentication successful&#10;&gt; MAIL FROM:&lt;welcome@yourdomain.com&gt;&#10;250 2.1.0 Ok&#10;&gt; RCPT TO:&lt;recipient@example.com&gt;&#10;250 2.1.5 Ok&#10;&gt; DATA&#10;354 Start mail input; end with &lt;CR&gt;&lt;LF&gt;.&lt;CR&gt;&lt;LF&gt;&#10;From: welcome@yourdomain.com&#10;To: recipient@example.com&#10;Subject: Welcome&#10;&#10;Thanks for signing up.&#10;.&#10;250 2.0.0 Ok &lt;jZTWt0pQO4p2LG7ByfkeSYUvT62k85Q12nCA@yourdomain.com&gt;&#10;&gt; QUIT&#10;221 mx.cloudflare.net Cloudflare Email ESMTP Service closing transmission channel&#10;</code></pre>
<p>A <code>250 2.0.0 Ok</code> response after the message body normally includes the assigned Message-ID. Use it to correlate the submission with delivery logs in the dashboard.</p>
<p>When <strong>Drop suppressed recipients</strong> is on and all recipients are suppressed, SMTP may return <code>250 2.0.0 Ok</code> without a Message-ID and deliver nothing. Refer to <a href="#suppressed-recipients">Suppressed recipients</a>.</p>
<h2 id="examples">Examples</h2>
<p>For language-specific examples — curl, Nodemailer, Python <code>smtplib</code>, and PHPMailer — see <a href="/email-service/examples/email-sending/smtp/">Send email over SMTP</a>.</p>
<h2 id="limits">Limits</h2>
<p>The following per-session limits apply to SMTP submission:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>RCPT TO</code> recipients</td>
<td>50 per session</td>
</tr>
<tr>
<td><code>SIZE</code> advertised in <code>EHLO</code></td>
<td>5 MiB</td>
</tr>
<tr>
<td><code>AUTH</code> command timeout</td>
<td>30 seconds</td>
</tr>
<tr>
<td><code>DATA</code> command timeout</td>
<td>300 seconds</td>
</tr>
</tbody>
</table>
<p>Account-wide quotas (daily sending limits, content limits, header limits) are shared with the REST API and the Workers binding. See <a href="/email-service/platform/limits/">Limits</a> for the full list.</p>
<h2 id="response-codes">Response codes</h2>
<p>Cloudflare's SMTP server returns standard <a href="https://datatracker.ietf.org/doc/html/rfc5321">RFC 5321</a> reply codes alongside <a href="https://datatracker.ietf.org/doc/html/rfc3463">RFC 3463</a> enhanced status codes.</p>
<table>
<thead>
<tr>
<th>Code</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>220</code></td>
<td>Service ready (greeting after the TLS handshake).</td>
</tr>
<tr>
<td><code>235 2.7.0</code></td>
<td>Authentication succeeded.</td>
</tr>
<tr>
<td><code>250</code></td>
<td><code>EHLO</code>, <code>MAIL FROM</code>, <code>RCPT TO</code>, or <code>DATA</code> completed successfully.</td>
</tr>
<tr>
<td><code>354</code></td>
<td>Ready to receive the message body — terminate with <code>&lt;CR&gt;&lt;LF&gt;.&lt;CR&gt;&lt;LF&gt;</code>.</td>
</tr>
<tr>
<td><code>421</code></td>
<td>Service temporarily unavailable. Retry later.</td>
</tr>
<tr>
<td><code>451 4.3.0</code></td>
<td>Local error — the message was accepted but deferred. Retry later.</td>
</tr>
<tr>
<td><code>452 4.5.3</code></td>
<td>Too many recipients in this session. Open a new session for the rest.</td>
</tr>
<tr>
<td><code>500</code> / <code>501</code></td>
<td>Syntax error in command or arguments.</td>
</tr>
<tr>
<td><code>503</code></td>
<td>Bad sequence of commands (for example, <code>MAIL FROM</code> before <code>AUTH</code>).</td>
</tr>
<tr>
<td><code>530 5.7.0</code></td>
<td>Authentication required.</td>
</tr>
<tr>
<td><code>535 5.7.8</code></td>
<td>Authentication failed. See <a href="#troubleshooting">Troubleshooting</a>.</td>
</tr>
<tr>
<td><code>550 5.7.1</code></td>
<td>Sender or relay denied — usually the <code>MAIL FROM</code> domain is not onboarded.</td>
</tr>
<tr>
<td><code>552 5.3.4</code></td>
<td>Message exceeds the 5 MiB <code>SIZE</code> limit.</td>
</tr>
<tr>
<td><code>554</code></td>
<td>Transaction failed — content rejected by policy.</td>
</tr>
</tbody>
</table>
<h2 id="suppressed-recipients">Suppressed recipients</h2>
<p>SMTP accepts a syntactically valid recipient with <code>250 2.1.5 Ok</code> during <code>RCPT TO</code>. Email Service checks the <a href="/email-service/concepts/suppressions/">suppression list</a> for the account after receiving the message body.</p>
<p>Behavior depends on the per-sending-domain <a href="/email-service/configuration/domains/#drop-suppressed-recipients"><strong>Drop suppressed recipients</strong> setting</a>. The setting is off by default.</p>
<p>When the setting is off, any suppressed recipient causes SMTP to reject the entire message. When the setting is on, Email Service removes suppressed recipients and continues processing the remaining recipients.</p>
<p>If all recipients are suppressed while dropping is on, SMTP may return <code>250 2.0.0 Ok</code> without a Message-ID. It delivers nothing in this case.</p>
<p>Use <a href="/email-service/observability/logs/">Email sending logs</a> to confirm delivery. Suppressed recipients appear with a <strong>Rejected</strong> result.</p>
<p>Suppression produces a <code>message.rejected</code> event in <a href="/email-service/platform/event-subscriptions/">Email Sending event subscriptions</a> with <code>rejection.reason</code> set to <code>suppressed</code>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="535-5-7-8-authentication-failed"><code>535 5.7.8 Authentication failed</code></h3>
<p>Possible causes:</p>
<ul>
<li>The username is not the literal string <code>api_token</code>. The API token goes in the <strong>password</strong> field.</li>
<li>The token does not have the <strong>Email Sending: Edit</strong> permission.</li>
<li>The token has been revoked or has expired.</li>
<li>For a user-owned token, the domain in <code>MAIL FROM</code> does not belong to an account the token can act on.</li>
</ul>
<h3 id="550-5-7-1-sender-denied"><code>550 5.7.1 Sender denied</code></h3>
<p>The address in <code>MAIL FROM</code> is on a domain that is not onboarded for Email Sending under the account that owns the API token. Onboard the domain under <strong>Email Service &gt; Email Sending</strong> in the dashboard, or change the sender address.</p>
<h3 id="552-5-3-4-message-too-big"><code>552 5.3.4 Message too big</code></h3>
<p>The message body (including attachments after MIME encoding) is larger than 5 MiB. Reduce the attachment size or split the message.</p>
<h3 id="tls-handshake-failures">TLS handshake failures</h3>
<p>Cloudflare's SMTP endpoint requires TLS from connect (implicit TLS). Make sure your client is configured for SSL/TLS on port <code>465</code>, not <code>STARTTLS</code> on port <code>587</code> (which is not supported).</p>
<p>For authentication problems related to SPF, DKIM, or DMARC on the recipient side, see <a href="/email-service/reference/troubleshooting/">Troubleshoot SPF, DKIM and DMARC</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/email-service/examples/email-sending/smtp/">Send email over SMTP</a> — examples for curl, Nodemailer, Python, and PHP.</li>
<li><a href="/email-service/api/send-emails/rest-api/">REST API</a> — send emails over HTTPS.</li>
<li><a href="/email-service/api/send-emails/workers-api/">Workers API</a> — send emails from a Cloudflare Worker using bindings.</li>
<li><a href="/email-service/configuration/domains/">Domain configuration</a> — onboard a domain for Email Sending.</li>
<li><a href="/email-service/configuration/mta-sts/">MTA-STS</a> — enforce TLS for incoming mail.</li>
<li><a href="/email-service/reference/headers/">Email headers</a> — supported headers and threading hints.</li>
<li><a href="/email-service/platform/limits/">Limits</a> — account, message, and session limits.</li>
</ul>
