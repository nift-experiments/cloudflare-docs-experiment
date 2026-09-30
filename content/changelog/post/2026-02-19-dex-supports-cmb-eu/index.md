<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 19, 2026</time><h2 id="post-title">DEX Supports EU Customer Metadata Boundary</h2>
<div class="changelog-badges"><span>dex</span></div><div class="changelog-body"><p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into <a href="/warp-client/">WARP</a> device connectivity and performance to any internal or external application.</p>
<p>Now, all DEX logs are fully compatible with Cloudflare's <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary</a> (CMB) setting for the 'EU' (European Union), which ensures that DEX logs will not be stored outside the 'EU' when the option is configured.</p>
<p>If a Cloudflare One customer using DEX enables CMB 'EU', they will not see any DEX data in the Cloudflare One dashboard. Customers can ingest DEX data via <a href="/logs/logpush/">LogPush</a>, and build their own analytics and dashboards.</p>
<p>If a customer enables CMB in their account, they will see the following message in the Digital Experience dashboard: &quot;DEX data is unavailable because Customer Metadata Boundary configuration is on. Use Cloudflare LogPush to export DEX datasets.&quot;</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_supports_cmb.png" alt="Digital Experience Monitoring message when Customer Metadata Boundary for the EU is enabled" /></p>
</div></article></div>
