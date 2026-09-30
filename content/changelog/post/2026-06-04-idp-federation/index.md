<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 4, 2026</time><h2 id="post-title">Share identity providers across accounts with IdP federation</h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access now supports <a href="/cloudflare-one/integrations/identity-providers/idp-federation/">IdP federation</a>, which allows organizations to share a single identity provider across multiple Cloudflare accounts.</p>
<p>Instead of configuring the same IdP (for example, Okta or Entra ID) separately in every account, you configure it once in a source account and share it with the other accounts in your organization. Each recipient account gets a read-only IdP connection that routes authentication back to the source account through a bridge — a hidden application in the source account that brokers the cross-account login. End users sign in with their existing IdP credentials, and each account's Access policies evaluate the resulting identity just like any other IdP login.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>One IdP, many accounts</strong> — Configure your IdP once and share it with all accounts in your organization.</li>
<li><strong>Lifecycle management</strong> — As accounts join or leave your Cloudflare organization, their IdP connections are provisioned and removed automatically — no manual cleanup required.</li>
<li><strong>Immutable recipient connections</strong> — IdP connections in recipient accounts cannot be accidentally modified or deleted.</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/integrations/identity-providers/idp-federation/">IdP federation</a>.</p>
</div></article></div>
