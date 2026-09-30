<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 3, 2026</time><h2 id="post-title">Control authorization cookies for multi-domain Access applications</h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access administrators can now control whether a self-hosted application preemptively sets authorization cookies across its public hostnames.</p>
<p>Previously, Access automatically used eager redirects for applications with five or fewer hostnames. Applications with more than five hostnames received cookies as users visited each hostname. Administrators can now choose either behavior, regardless of the number of hostnames.</p>
<p>The new <strong>Eager redirect cookie</strong> setting is turned on by default for new applications. After a user signs in, Access redirects the browser through each hostname and sets a <code>CF_Authorization</code> cookie. This supports applications that need to make requests across hostnames before the user visits each one.</p>
<p>For applications with many hostnames, the redirect chain can cause sign-in loops in some browsers. Turn off the setting to issue the cookie only when a user visits each hostname.</p>
<p>To configure the setting, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#eager-redirect-cookie">Authorization cookie</a>.</p>
</div></article></div>
