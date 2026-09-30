<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 30, 2025</time><h2 id="post-title">Cloudflare One Agent for iOS (version 1.11)</h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the iOS Cloudflare One Agent is now available in the <a href="https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492">iOS App Store</a>. This release
contains improvements and new exciting features, including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum">post-quantum cryptography</a>.
By tunneling your corporate network traffic over Cloudflare, you can now gain the immediate <a href="https://blog.cloudflare.com/pq-2024/">protection of post-quantum cryptography</a> without needing to upgrade any of your individual corporate applications or systems.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>QLogs are now disabled by default and can be enabled in the app by turning on <strong>Enable qlogs</strong> under <strong>Settings</strong> &gt; <strong>Advanced</strong> &gt; <strong>Diagnostics</strong> &gt; <strong>Debug Logs</strong>. The QLog setting from previous releases will no longer be respected.</li>
<li>DNS over HTTPS traffic is now included in the WARP tunnel by default.</li>
<li>The WARP client now applies <a href="https://blog.cloudflare.com/pq-2024/">post-quantum cryptography</a> end-to-end on enabled devices accessing resources behind a Cloudflare Tunnel. This feature can be enabled by <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum">MDM</a>.</li>
</ul>
</div></article></div>
