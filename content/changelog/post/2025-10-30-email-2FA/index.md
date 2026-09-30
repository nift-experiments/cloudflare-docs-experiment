<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 30, 2025</time><h2 id="post-title">Introducing email two-factor authentication</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Two-factor authentication (2FA) is one of the best ways to protect your account from the risk of account takeover. Cloudflare has offered phishing resistant 2FA options including hardware based keys (for example, a Yubikey) and app based TOTP (time-based one-time password) options which use apps like Google or Microsoft's Authenticator app. Unfortunately, while these solutions are very secure, they can be lost if you misplace the hardware based key, or lose the phone which includes that app. The result is that users sometimes get locked out of their accounts and need to contact support.</p>
<p>Today, we are announcing the addition of email as a 2FA factor for all Cloudflare accounts. Email 2FA is in wide use across the industry as a least common denominator for 2FA because it is low friction, loss resistant, and still improves security over username/password login only. We also know that most commercial email providers already require 2FA, so your email address is usually well protected already.</p>
<p>You can now enable email 2FA on the Cloudflare dashboard:</p>
<ol>
<li>Go to <strong>Profile</strong> at the top right corner.</li>
<li>Select <strong>Authentication</strong>.</li>
<li>Under <strong>Two-Factor Authentication</strong>, select <strong>Set up</strong>.</li>
</ol>
<h4 id="sign-in-security-best-practices">Sign-in security best practices</h4>
<p>Cloudflare is critical infrastructure, and you should protect it as such. Review the following best practices and make sure you are doing your part to secure your account:</p>
<ul>
<li>Use a unique password for every website, including Cloudflare, and store it in a password manager like 1Password or Keeper. These services are cross-platform and simplify the process of managing secure passwords.</li>
<li>Use 2FA to make it harder for an attacker to get into your account in the event your password is leaked.</li>
<li>Store your backup codes securely. A password manager is the best place since it keeps the backup codes encrypted, but you can also print them and put them somewhere safe in your home.</li>
<li>If you use an app to manage your 2FA keys, enable cloud backup, so that you don't lose your keys in the event you lose your phone.</li>
<li>If you use a custom email domain to sign in, <a href="/fundamentals/manage-members/dashboard-sso/">configure SSO</a>.</li>
<li>If you use a public email domain like Gmail or Hotmail, you can also use social login with Apple, GitHub, or Google to sign in.</li>
<li>If you manage a Cloudflare account for work:
<ul>
<li>Have at least two administrators in case one of them unexpectedly leaves your company.</li>
<li>Use SCIM to automate permissions management for members in your Cloudflare account.</li>
</ul>
</li>
</ul>
</div></article></div>
