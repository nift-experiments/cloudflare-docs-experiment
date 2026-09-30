<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 8, 2026</time><h2 id="post-title">Authenticated SMTP submission now available in beta</h2>
<div class="changelog-badges"><span>email-service</span></div><div class="changelog-body"><p>You can now send emails through <strong>Cloudflare Email Service</strong> using authenticated <a href="/email-service/api/send-emails/smtp/">SMTP submission</a> on <code>smtp.mx.cloudflare.net:465</code>. SMTP joins the <a href="/email-service/api/send-emails/rest-api/">REST API</a> and the <a href="/email-service/api/send-emails/workers-api/">Workers binding</a> as a third way to send transactional email — useful for existing applications that already speak SMTP and language-native SMTP libraries (Nodemailer, <code>smtplib</code>, PHPMailer, JavaMail).</p>
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
<td><code>465</code> (implicit TLS)</td>
</tr>
<tr>
<td>AUTH</td>
<td><code>PLAIN</code> or <code>LOGIN</code></td>
</tr>
<tr>
<td>Username</td>
<td><code>api_token</code></td>
</tr>
<tr>
<td>Password</td>
<td>A Cloudflare API token (account-owned or user-owned) with <strong>Email Sending: Edit</strong></td>
</tr>
</tbody>
</table>
<p>Submissions enter the same delivery pipeline as the REST API and Workers binding: identical <a href="/email-service/platform/limits/">limits</a>, automatic DKIM and ARC signing, and shared dashboard logs.</p>
<p>Send your first email with a single command:</p>
<pre><code class="language-sh">curl --ssl-reqd \&#10;  &#45;-url &quot;smtps://smtp.mx.cloudflare.net:465&quot; \&#10;  &#45;-user &quot;api_token:&lt;API_TOKEN&gt;&quot; \&#10;  &#45;-mail-from &quot;welcome@yourdomain.com&quot; \&#10;  &#45;-mail-rcpt &quot;user@example.com&quot; \&#10;  &#45;-upload-file mail.txt&#10;</code></pre>
<p>Refer to the <a href="/email-service/api/send-emails/smtp/">SMTP reference</a> for authentication details, response codes, and language-specific examples.</p>
</div></article></div>
