<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 1, 2026</time><h2 id="post-title">Independent MFA for infrastructure applications</h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a> now supports independent multi-factor authentication (MFA) for SSH connections using YubiKey PIV keys. This adds a hardware-backed second factor to SSH access, ensuring that a compromised device session alone is not sufficient to reach your servers.</p>
<p>With per-application and per-policy configuration, you can enforce PIV key authentication for sensitive usernames (for example, <code>root</code>) while applying different requirements for other usernames. You can also set an MFA session duration to control how often users must re-authenticate.</p>
<h4 id="enrollment">Enrollment</h4>
<p>Users enroll their YubiKey PIV key through the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a>. For enrollment instructions and SSH client setup, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-piv-key-for-infrastructure-apps">Enroll a PIV key for infrastructure apps</a>.</p>
<h4 id="configuration">Configuration</h4>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications">Enforce MFA for infrastructure applications</a>.</p>
</div></article></div>
