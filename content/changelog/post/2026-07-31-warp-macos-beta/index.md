<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 31, 2026</time><h2 id="post-title">Cloudflare One Client for macOS (version 2026.7.1210.1)</h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release includes the following changes and improvements:</p>
<ul>
<li>Improved connection reliability: the client now swaps protocol order after repeated connectivity-check failures, which helps when HTTP/3 is blocked after the QUIC handshake.</li>
<li>Fixed issue where a certificate error could be incorrectly displayed right after the connection is established.</li>
<li>A <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search domain</a> parsing failure no longer prevents connection.</li>
<li>Fixed a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">MASQUE</a> issue where the tunnel could stall while uploading at a high rate.</li>
<li>Fixed being unable to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/">switch organizations</a> when the client was stuck in the &quot;Device not in organization&quot; state.</li>
<li>Fixed the Home Screen dropdown popup not anchoring correctly.</li>
<li>Fixed a crash during dialog dismissal.</li>
<li>Increased tolerance for configurations with a large number of <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">local domain fallback</a> resolver IPs, so DNS resolution behaves correctly even when more fallback resolvers are configured than recommended.</li>
<li>Fixed the WARP client stealing window focus (for example, during reauth).</li>
<li>Fixed a client crash when connecting to a captive portal over Wi-Fi.</li>
<li>Fixed the system tray icon showing &quot;disconnected&quot; while the UI showed &quot;connected&quot;.</li>
<li>A successful re-authentication will cause the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> to be re-evaluated.</li>
<li>Improved <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">dashboard-managed client updates</a> by running the updater only when needed.</li>
</ul>
</div></article></div>
