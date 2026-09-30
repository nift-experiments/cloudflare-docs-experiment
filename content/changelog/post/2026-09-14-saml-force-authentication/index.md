<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 14, 2026</time><h2 id="post-title">Require fresh authentication for SAML identity providers</h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access can now request fresh authentication from a SAML identity provider for every login. Turn on <strong>Require reauthentication</strong> in the Cloudflare dashboard, or set <code>force_authn</code> to <code>true</code> through the API. Access will then set <code>ForceAuthn</code> to <code>true</code> in signed and unsigned SAML authentication requests.</p>
<p>This option is useful when an application requires users to reauthenticate at the identity provider instead of relying on an existing identity provider session. The default value is <code>false</code>.</p>
<p>For configuration details, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#require-fresh-authentication-at-the-identity-provider">Require fresh authentication at the identity provider</a>.</p>
</div></article></div>
