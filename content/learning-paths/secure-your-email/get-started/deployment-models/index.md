<p>Email security offers multiple deployment models:</p>
<ul>
<li>API for Microsoft 365 users.</li>
<li>BCC for Google Workspace users.</li>
<li>MX/Inline for all email providers.</li>
</ul>
<p>When you choose the <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/api/">API deployment</a>, Email security can both scan and take actions on emails after they have reached a user's inbox.</p>
<p>If you are a Google Workspace user, you can enable Email security via <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/gmail-bcc-setup/">BCC setup</a>. Email security scans a copy of your email after it lands in your inbox.</p>
<p><img src="/assets/upstream/email-security/Gmail_Deployment_BCC.png" alt="Google Workspace BCC deployment diagram" /></p>
<p>With MX/Inline, Email security scans your email before they land in your inbox, giving you the highest level of protection.</p>
<p><img src="/assets/upstream/email-security/Email_security_Deployment_Inline.png" alt="Microsoft 365 and Google Workspace MX/Inline" /></p>
<p>Refer to <a href="/cloudflare-one/email-security/setup/">Before you begin</a> for a comprehensive comparison of each deployment method, and <a href="/reference-architecture/architectures/email-security-deployments/">Understanding Email Security Deployments</a> to learn about each deployment method.</p>
