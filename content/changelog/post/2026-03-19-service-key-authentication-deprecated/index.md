<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 19, 2026</time><h2 id="post-title">Service Key authentication deprecated</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Service Key authentication for the Cloudflare API is deprecated. Service Keys will stop working on September 30, 2026.</p>
<p><a href="/fundamentals/api/get-started/create-token/">API Tokens</a> replace Service Keys with fine-grained permissions, expiration, and revocation.</p>
<h4 id="what-you-need-to-do">What you need to do</h4>
<p>Replace any use of the <code>X-Auth-User-Service-Key</code> header with an <a href="/fundamentals/api/get-started/create-token/">API Token</a> scoped to the permissions your integration requires.</p>
<p>If you use <code>cloudflared</code>, update to a version from November 2022 or later. These versions already use API Tokens.</p>
<p>If you use <a href="https://github.com/cloudflare/origin-ca-issuer">origin-ca-issuer</a>, update to a version that supports API Token authentication.</p>
<p>For more information, refer to <a href="/fundamentals/api/reference/deprecations/">API deprecations</a>.</p>
</div></article></div>
