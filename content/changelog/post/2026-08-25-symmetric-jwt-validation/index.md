<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 25, 2026</time><h2 id="post-title">Symmetric key support for JWT validation</h2>
<div class="changelog-badges"><span>api-shield</span></div><div class="changelog-body"><p>API Shield <a href="/api-shield/security/jwt-validation/">JSON Web Token validation</a> now supports symmetric keys that use the <code>HS256</code>, <code>HS384</code>, and <code>HS512</code> algorithms. You can configure HMAC verification keys in the Cloudflare dashboard or with the Cloudflare API.</p>
<p>Cloudflare never stores symmetric credentials in plaintext. API responses do not include the credential.</p>
<p>Refer to <a href="/api-shield/security/jwt-validation/api/#credentials">Configure JWT validation via the API</a> for supported key formats and credential requirements.</p>
</div></article></div>
