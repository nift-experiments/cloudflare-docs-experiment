---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/user-profiles/2fa/
  description: Set up and manage two-factor authentication on your Cloudflare account using security keys, TOTP apps, or email.
  full_title: Two-factor authentication · Cloudflare Fundamentals docs
  head_html: <title>Two-factor authentication · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up and manage two-factor authentication on your Cloudflare account using security keys, TOTP apps, or email."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/user-profiles/2fa/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/user-profiles/2fa/index.md"><meta property="og:title" content="Two-factor authentication · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up and manage two-factor authentication on your Cloudflare account using security keys, TOTP apps, or email."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/user-profiles/2fa/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/user-profiles/2fa/#page","headline":"Two-factor authentication \u00b7 Cloudflare Fundamentals docs","description":"Set up and manage two-factor authentication on your Cloudflare account using security keys, TOTP apps, or email.","url":"https://developers.cloudflare.com/fundamentals/user-profiles/2fa/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/user-profiles/2fa/
  schema: 1
---
<p>We recommend that all Cloudflare user account holders enable two-factor authentication (2FA) to keep your accounts secure. </p>
<p>2FA can only be enabled successfully on an account with a <a href="/fundamentals/user-profiles/verify-email-address/">verified email address</a>. If you do not verify your email address first, you may lock yourself out of your account.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8754.md")
</aside>
<p>To enable two-factor authentication for your Cloudflare login:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a>.</li>
<li>Under the <strong>My Profile</strong> dropdown, select <strong>My Profile</strong>.</li>
<li>Select <strong>Authentication</strong>. </li>
<li>Select <strong>Add</strong> next to <a href="/fundamentals/user-profiles/2fa/#configure-totp-mobile-application-authentication">Mobile App Authentication</a> or <a href="/fundamentals/user-profiles/2fa/#configure-security-key-authentication-for-two-factor-cloudflare-login">Security Key Authentication</a>, or <strong>Enable</strong> next to <a href="/fundamentals/user-profiles/2fa/#configure-email-two-factor-authentication">Email Authentication</a>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8753.md")
</aside>
<h2 id="configure-security-key-authentication-for-two-factor-cloudflare-login">Configure security key authentication for two-factor Cloudflare login</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8752.md")
</aside>
<p>A security key provides phishing-resistant multifactor authentication to your Cloudflare account using a built-in authenticator (Apple Touch ID, Android fingerprint, or Windows Hello) or an external hardware key (like <a href="https://www.yubico.com/works-with-yubikey/catalog/cloudflare/">YubiKey</a>) that connects to your computer through USB-A, USB-C, NFC, or Bluetooth.</p>
<p>Cloudflare recommends configuring multiple security keys. With multiple keys, you can still use 2FA if the primary key is unavailable or if you are working on a different device.</p>
<p>After <a href="/fundamentals/user-profiles/2fa/#configure-totp-mobile-application-authentication">enabling 2FA on your Cloudflare account</a>, you can select <strong>Manage</strong> to configure 2FA security key authentication.</p>
<h3 id="built-in-authenticators">Built-in authenticators</h3>
<p>You can configure a built-in authenticator such as Apple Touch ID, Android fingerprint, or Windows Hello.</p>
<ol>
<li>In <strong>Security Key Authentication</strong>, select <strong>Add</strong>.</li>
<li>On the <strong>Add a Security Key</strong>, enter your Cloudflare password and select <strong>Next</strong>.</li>
<li>Interact with your built-in authenticator to add it to your Cloudflare account.</li>
<li>Enter a name for the built-in authenticator. If this is the initial setup, you will be prompted to generate backup codes. If not, skip to Step 8.</li>
<li>Enter your Cloudflare password.</li>
<li>Select <strong>Next</strong> to review your backup codes. Backup codes can be used to access your user account without your mobile device.</li>
<li>Select <strong>Download</strong>, <strong>Print</strong>, or <strong>Copy</strong> to save your backup codes in a secure location.</li>
<li>Select <strong>Next</strong> to finish the configuration.</li>
</ol>
<h3 id="security-keys">Security keys</h3>
<p>You can configure a security key, such as a Yubikey, to use with your account. Before you begin, ensure your hardware security key is configured and plugged in.</p>
<p>On a Windows device, you may need to set up Windows Hello or register your security key to your Microsoft account. Review the Windows documentation for more details.</p>
<ol>
<li>Once your security key is plugged in, go to <strong>Profile</strong> &gt; <strong>Authentication</strong>.</li>
<li>From <strong>Two-Factor Authentication</strong>, select <strong>Set up</strong>.</li>
<li>From <strong>Security Key Authentication</strong>, select <strong>Add</strong>.</li>
<li>Enter your Cloudflare password on the <strong>Add a Security Key</strong> screen, then select <strong>Next</strong>.</li>
<li>Interact with your security key to add it to your Cloudflare account. Ensure that the dialog is for the security key setup. If the Windows Hello dialog appears on a Windows device, select <strong>Cancel</strong>. The security key dialog box will then appear. Depending on your system, you may be required to register a PIN for the security key.</li>
<li>Enter a name for the security key. If this is the initial setup, you will be prompted to generate backup codes. If not, skip to Step 8.</li>
<li>Enter your Cloudflare password.</li>
<li>Select <strong>Next</strong> to review your backup codes. Backup codes can be used to access your user account without your mobile device.</li>
<li>Select <strong>Download</strong>, <strong>Print</strong>, or <strong>Copy</strong> to save your backup codes in a secure location.</li>
<li>Select <strong>Next</strong> to finish the configuration.</li>
</ol>
<h2 id="configure-totp-mobile-application-authentication">Configure TOTP mobile application authentication</h2>
<p>Time-based one-time password (TOTP) authentication works by using an authenticatior app, such as Google Authenticator or Microsoft Authenticator, which generates a secret code shared between the app and a website. When you log in to the website, you enter your username, password, and the secret code generated from the authenticator app. The secret code is only valid for a short period of time, about 30 to 60 seconds, before a new code is generated.</p>
<ol>
<li>Once your security key is plugged in, go to <strong>Profile</strong> &gt; <strong>Authentication</strong>.</li>
<li>From <strong>Two-Factor Authentication</strong>, select <strong>Set up</strong>.</li>
<li>Under <strong>Mobile App Authentication</strong>, select <strong>Add</strong>.</li>
<li>Scan the QR code with your mobile device and enter the code from your authenticator application.</li>
<li>Enter your Cloudflare password, then select <strong>Next</strong>. If you cannot scan the QR code, select <strong>Can't scan QR code, Follow alternative steps</strong> to configure your authenticator application manually.</li>
</ol>
<p><img src="/assets/upstream/images/fundamentals/2FA_scan_QR_code.png" alt="You can enable 2FA by scanning a QR code with your mobile device." /></p>
<ol start="6">
<li>Enter your Cloudflare password again.</li>
<li>Select <strong>Next</strong> to review your backup codes. You can use backup codes to access your account without your mobile device.</li>
<li>Select <strong>Download</strong>, <strong>Print</strong>, or <strong>Copy</strong> to save your backup codes in a secure location.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8751.md")
</aside>
<ol start="9">
<li>Select <strong>Next</strong> on the backup code page to complete the recovery code setup.</li>
</ol>
<h3 id="reconfigure-totp-mobile-application-authentication">Reconfigure TOTP mobile application authentication</h3>
<p>You may need to reconfigure your mobile application authentication if you join a new organization or lose access to your mobile device. When you reconfigure your mobile application authentication, your previous TOTP codes are invalid.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8750.md")
</aside>
<p>To reconfigure, follow <a href="/fundamentals/user-profiles/2fa/#configure-totp-mobile-application-authentication">Steps 1-7</a> as detailed above.</p>
<h2 id="configure-email-two-factor-authentication">Configure email two factor authentication</h2>
<p>Email 2FA works by sending you a TOTP code to your email address. This is a good option particularly if you are concerned about losing a hardware based key.</p>
<ol>
<li>Navigate to <strong>User Profile</strong>, then <strong>Authentication</strong>.</li>
<li>Under <strong>Two-Factor Authentication</strong>, select <strong>Set up</strong>.</li>
<li>Under <strong>Email Authentication</strong>, select <strong>Enable</strong>.</li>
<li>You will be prompted to enter your password twice, and then be shown recovery codes. Save these somewhere safe like a password manager.</li>
</ol>
<h2 id="regenerate-backup-codes">Regenerate backup codes</h2>
<p>Each backup code is one-time use only, but you can always request a new set of backup codes using the Cloudflare dashboard. This is useful if you have lost access to or used all of your previous backup codes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8749.md")
</aside>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>My Profile</strong>.</li>
<li>Select <strong>Authentication</strong>.</li>
<li>For <strong>Two-Factor Authentication</strong>, select <strong>Manage</strong>.</li>
<li>For <strong>Backup codes</strong>, select <strong>Regenerate</strong> to generate and save a new set of two-factor backup codes.</li>
</ol>
<h2 id="disable-two-factor-authentication-for-your-cloudflare-account">Disable two-factor authentication for your Cloudflare account</h2>
<p>To disable 2FA for your Cloudflare account, you must delete all security keys and TOTP authenticators from your account.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8748.md")
</aside>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Profile</strong>.</li>
<li>Select the <strong>Authentication</strong>.
<ul>
<li>To remove your security key:
<ol>
<li>Select <strong>Edit</strong> in the <strong>Security Key Authentication</strong> card. A drop-down menu shows more details about your security key.</li>
<li>Select <strong>Delete</strong>.</li>
<li>Enter your Cloudflare password, then select <strong>Remove</strong>.</li>
</ol>
</li>
<li>To remove your TOTP mobile application authentication:
<ol>
<li>Select <strong>Delete method</strong> in the <strong>Mobile App Authentication</strong> card.</li>
<li>Enter your Cloudflare password, authenticator application code, or a recovery code, then select <strong>Disable</strong>.</li>
</ol>
</li>
</ul>
</li>
</ol>
<p><img src="https://developerdocsgifs.cloudflaretraining.com/resampled_5fps_disable_mobile_auth_v2_final.gif" alt="how to disable your TOTP mobile application authentication." /></p>
<h2 id="use-a-backup-code">Use a backup code</h2>
<p>If you lose access to a mobile device, security key, or authentication code, you can solve these issues by using a backup code or retrieving a backup code from your preferred authentication app.</p>
<p>Refer to Google's documentation to <a href="https://support.google.com/accounts/answer/1066447?co=GENIE.Platform%3DAndroid&amp;hl=en&amp;oco=0">transfer Google Authenticator codes from one Android device to another</a>.</p>
<p>When setting up 2FA, you should have saved your backup codes in a secure location. To restore lost access using a Cloudflare backup code:</p>
<ol>
<li>Retrieve the backup code from where you stored it.</li>
<li>Go to the <a href="https://dash.cloudflare.com/login">Cloudflare login page</a>, enter your username and password and select <strong>Log in</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>You should see a page titled <strong>Two-Factor Authentication</strong>
<ul>
<li>If it has a text box, enter one of your backup codes and select <strong>Log in</strong>.</li>
<li>If instead you see &quot;Insert your security key and touch it&quot;, cancel any prompts from your browser that appear and select <strong>try another authentication method or backup code</strong>. Proceed to enter one of your backup codes and select <strong>Log in</strong>.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8747.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://support.google.com/accounts/answer/1066447?hl=en&amp;ref_topic=2954345&amp;co=GENIE.Platform%3DiOS&amp;oco=0">Google Authentication documentation</a></li>
<li><a href="https://www.yubico.com/works-with-yubikey/catalog/cloudflare/">YubiKey documentation</a></li>
<li><a href="/fundamentals/manage-members/">Set up multi-user accounts on Cloudflare</a></li>
<li><a href="/fundamentals/user-profiles/account-recovery/">Account recovery</a></li>
</ul>
