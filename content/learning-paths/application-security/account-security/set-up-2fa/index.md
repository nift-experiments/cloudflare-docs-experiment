<p>Two-factor authentication (2FA) allows user account owners to add an additional layer of login security to Cloudflare accounts. This additional authentication step requires you to provide both something you know, such as a Cloudflare password, and something you have, such as an authentication code from a mobile device.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9632.md")
</aside>
<p>Cloudflare offers the option to use either a phishing-resistant security key, like a YubiKey, or a Time-Based One-Time password (TOTP) mobile app for authentication, like Google Authenticator, or both. If you add both of these authentication methods to your account, you are initially prompted to log in with the security key, but can opt-out and use TOTP instead.</p>
<p>To ensure that you can securely access your account even without your mobile device or security keys, Cloudflare also provides backup codes for download.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="tip">Tip</h3>
@markup("md", "content/.markup/bodies/9631.md")
</aside>
<p>As the user account owner, you are automatically assigned the <a href="/fundamentals/manage-members/">Super Administrator</a> role. Once 2FA is enabled, all Cloudflare account members are required to configure 2FA on their mobile devices.</p>
<hr />
<h2 id="enable-2fa">Enable 2FA</h2>
<p>We recommend that all Cloudflare user account holders enable two-factor authentication (2FA) to keep your accounts secure. </p>
<p>2FA can only be enabled successfully on an account with a <a href="/fundamentals/user-profiles/verify-email-address/">verified email address</a>. If you do not verify your email address first, you may lock yourself out of your account.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/9630.md")
</aside>
<p>To enable two-factor authentication for your Cloudflare login:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a>.</li>
<li>Under the <strong>My Profile</strong> dropdown, select <strong>My Profile</strong>.</li>
<li>Select <strong>Authentication</strong>. </li>
<li>Select <strong>Add</strong> next to <a href="/fundamentals/user-profiles/2fa/#configure-totp-mobile-application-authentication">Mobile App Authentication</a> or <a href="/fundamentals/user-profiles/2fa/#configure-security-key-authentication-for-two-factor-cloudflare-login">Security Key Authentication</a>, or <strong>Enable</strong> next to <a href="/fundamentals/user-profiles/2fa/#configure-email-two-factor-authentication">Email Authentication</a>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9629.md")
</aside>
<h2 id="additional-configurations">Additional configurations</h2>
<p>Cloudflare also supports 2FA with device built-in authenticators (Apple Touch ID, Android fingerprint, or Windows Hello), Yubikeys and TOTP mobile applications.</p>
