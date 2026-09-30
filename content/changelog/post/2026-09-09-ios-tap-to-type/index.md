<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 9, 2026</time><h2 id="post-title">Improved iOS tap-to-type experience for Browser Isolation</h2>
<div class="changelog-badges"><span>browser-isolation</span><span>cloudflare-one</span></div><div class="changelog-body"><p><a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> has improved the tap-to-type experience for users on iOS devices.</p>
<p>Previously, Browser Isolation displayed a full-screen overlay with the message <code>tap to type</code> when users focused a text field. The prompt now appears inline over the focused text field, reducing disruption when users enter text in isolated sessions.</p>
<p>If the focused text field is too small to display the full prompt, Browser Isolation displays a keyboard icon in the center of the text field instead.</p>
<p><img src="/assets/upstream/images/cloudflare-one/rbi/tap-to-type.jpg" alt="Inline tap-to-type prompt over a focused text field in Browser Isolation" /></p>
<p>iOS users should tap twice to begin entering text. This update applies automatically to Browser Isolation sessions on iOS.</p>
<p>For more information on why this interaction is required, refer to <a href="/cloudflare-one/remote-browser-isolation/known-limitations/#ios">iOS limitations</a>.</p>
</div></article></div>
