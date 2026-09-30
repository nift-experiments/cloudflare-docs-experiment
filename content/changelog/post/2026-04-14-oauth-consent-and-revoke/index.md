<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 14, 2026</time><h2 id="post-title">Improved OAuth experience for consent and management</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>OAuth allows third-party applications to access your Cloudflare account on your behalf — like when Wrangler deploys Workers or when monitoring tools read your analytics. You now have <strong>granular control</strong> over which accounts these applications can access, plus the ability to revoke access anytime.</p>
<h4 id="what-s-new">What's new</h4>
<h4 id="choose-which-accounts-to-authorize">Choose which accounts to authorize</h4>
When authorizing an OAuth application, you can now **select specific accounts** instead of granting access to all your accounts:
- **Account-by-account selection** — Choose exactly which accounts the application can access
- **"All accounts" option** — Still available for trusted tools like Wrangler
This gives you precise control who can access your data.
<h4 id="clear-consent-screens">Clear consent screens</h4>
The OAuth consent screen now shows:
- **What the application can access** — Explicit list of permissions being requested
- **Who created the application** — Application owner and contact information  
- **Which accounts you're authorizing** — Checkboxes for account selection
<h4 id="revoke-access-anytime">Revoke access anytime</h4>
Manage authorized OAuth applications from your profile:
- **See all connected apps** — View every OAuth application with access to your accounts
- **Review permissions and scope** — Check what each application can do and which accounts it can access
- **Revoke instantly** — Remove access with one click when you no longer need it
To manage your OAuth applications, navigate to **Profile** > **Access Management** > **[Connected Applications](https://dash.cloudflare.com/profile/access-management/authorization)**.
<h4 id="why-this-matters">Why this matters</h4>
These updates give you:
- **Granular control** — Authorize apps per-account instead of all-or-nothing
- **Transparency** — Know exactly what you're authorizing before you consent
- **Security** — Limit blast radius by restricting access to only necessary accounts
- **Easy cleanup** — Revoke access when applications are no longer needed
<h4 id="learn-more">Learn more</h4>
Read more about these improvements in our blog post: [Improving the OAuth consent experience](https://blog.cloudflare.com/improved-developer-security/#improving-the-oauth-consent-experience).
</div></article></div>
