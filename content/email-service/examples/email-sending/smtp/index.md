<p class="article-summary">Send transactional emails over Cloudflare Email Service SMTP using curl, Nodemailer, Python smtplib, or PHPMailer.</p>
<p>Send transactional emails over Cloudflare Email Service <a href="/email-service/api/send-emails/smtp/">authenticated SMTP</a> (<code>smtp.mx.cloudflare.net:465</code>) from any SMTP-capable language or client.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A domain onboarded for <a href="/email-service/configuration/domains/">Email Sending</a>.</li>
<li>A <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> with the <strong>Email Sending: Edit</strong> permission. Set it as <code>CF_API_TOKEN</code> in your environment. The token is used as the SMTP password; the username is the literal string <code>api_token</code>.</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="smtp-language"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8670.md")
</div></div>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/email-service/api/send-emails/smtp/">SMTP reference</a> — connection details, authentication, response codes, and troubleshooting.</li>
<li><a href="/email-service/examples/email-sending/recipients/">Specify recipients</a> — multiple recipients, CC and BCC, and named addresses.</li>
<li><a href="/email-service/platform/limits/">Limits</a> — account, message, and session limits.</li>
</ul>
