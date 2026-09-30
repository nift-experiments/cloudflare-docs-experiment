<h2 id="overview">Overview</h2>
<p>Cloudflare uses a Multi-Factor Email Authentication (MFA) method for increased account security. MFA prevents customer account takeovers when attackers gain unauthorized access to an account due to an exposed or easily guessed password.</p>
<p>Cloudflare will challenge any login attempt if the user provides the correct credentials from an unrecognized IP address.</p>
<p><img src="/assets/upstream/images/fundamentals/hc-import-account_access_email.png" alt="Cloudflare will send an email when your account is logged into from an unknown IP address." /></p>
<p>Cloudflare challenges the login by sending a one-time code that expires in 30 minutes to the email that we have on file for the account. Once the correct code is provided through the dashboard, your IP will be recorded and further login attempts from that IP address will not be challenged for 90 days.</p>
<p><img src="/assets/upstream/images/fundamentals/hc-import-login_authentication.png" alt="When your account is logged into from an unknown IP address, you have to enter an authentication token from an email sent to your email address on file." /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8735.md")
</aside>
<h2 id="troubleshoot-mfa">Troubleshoot MFA</h2>
<p>Cloudflare emails are sometimes flagged as spam by the recipient's email service. If you are expecting an authentication token, you should check the spam folder for any Cloudflare emails and configure a filter to allow Cloudflare emails from <em><a href="mailto:no-reply@notify.cloudflare.com">no-reply@notify.cloudflare.com</a></em>_<strong>.</strong>_</p>
<p>Other times, emails are rejected by the recipient email service. Cloudflare will try again it will flag your email address after several attempts and no further emails will be sent.</p>
<p>If you still do not receive an email after ensuring your email service is not flagging Cloudflare, contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/fundamentals/user-profiles/2fa/">Secure user access with two-factor authentication</a></li>
</ul>
