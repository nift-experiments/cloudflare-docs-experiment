<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 19, 2026</time><h2 id="post-title">Cloudflare as identity provider and account membership selector</h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access now supports using Cloudflare itself as an <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">identity provider</a>. If you publish an Access application and select Cloudflare as the login method, users can sign in with their existing Cloudflare account — no one-time PINs, no third-party IdP configuration, and no shared email inboxes. Authentication is backed by Cloudflare's own account security (including multi-factor authentication), making it both simpler to set up and more secure than OTP-based login for most use cases.</p>
<p>Cloudflare is now the <strong>default identity provider for all newly created Zero Trust accounts</strong>, replacing One-time PIN.</p>
<p>This also enables two new capabilities:</p>
<ul>
<li><strong>Cloudflare Account Member selector</strong> — A new <a href="/cloudflare-one/access-controls/policies/#cloudflare-access-selectors">policy selector</a> that matches users based on their membership in a Cloudflare account. You can target the current account or specify a different account ID for cross-account access scenarios.</li>
<li><strong>Restrict to account members</strong> — An identity provider configuration option that limits authentication to users who are members of your Cloudflare account.</li>
</ul>
<p>To get started, add Cloudflare as an <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">identity provider</a> in your Zero Trust settings.</p>
</div></article></div>
