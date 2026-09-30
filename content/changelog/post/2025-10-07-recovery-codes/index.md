<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 7, 2025</time><h2 id="post-title">Automated reminders for backup codes</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>The most common reason users contact Cloudflare support is lost two-factor authentication (2FA) credentials. Cloudflare supports both app-based and hardware keys for 2FA, but you could lose access to your account if you lose these. Over the past few weeks, we have been rolling out email and in-product reminders that remind you to also download backup codes (sometimes called recovery keys) that can get you back into your account in the event you lose your 2FA credentials. Download your backup codes now by logging into Cloudflare, then navigating to <strong>Profile</strong> &gt; <strong>Security &amp; Authentication</strong> &gt; <strong>Backup codes</strong>.</p>
<h4 id="sign-in-security-best-practices">Sign-in security best practices</h4>
<p>Cloudflare is critical infrastructure, and you should protect it as such. Please review the following best practices and make sure you are doing your part to secure your account.</p>
<ul>
<li>Use a unique password for every website, including Cloudflare, and store it in a password manager like 1Password or Keeper. These services are cross-platform and simplify the process of managing secure passwords.</li>
<li>Use 2FA to make it harder for an attacker to get into your account in the event your password is leaked</li>
<li>Store your backup codes securely. A password manager is the best place since it keeps the backup codes encrypted, but you can also print them and put them somewhere safe in your home.</li>
<li>If you use an app to manage your 2FA keys, enable cloud backup, so that you don't lose your keys in the event you lose your phone.</li>
<li>If you use a custom email domain to sign in, <a href="https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/">configure SSO</a>.</li>
<li>If you use a public email domain like Gmail or Hotmail, you can also use social login with Apple, GitHub, or Google to sign in.</li>
<li>If you manage a Cloudflare account for work:
<ul>
<li>Have at least two administrators in case one of them unexpectedly leaves your company</li>
<li>Use SCIM to automate permissions management for members in your Cloudflare account</li>
</ul>
</li>
</ul>
</div></article></div>
