<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 29, 2025</time><h2 id="post-title">Smart Tiered Cache Fallback to Generic</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p><a href="/cache/how-to/tiered-cache/#smart-tiered-cache">Smart Tiered Cache</a> now falls back to <a href="/cache/how-to/tiered-cache/#generic-global-tiered-cache">Generic Tiered Cache</a> when the origin location cannot be determined, improving cache precision for your content.</p>
<p>Previously, when Smart Tiered Cache was unable to select the optimal upper tier (such as when origins are masked by Anycast IPs), latency could be negatively impacted. This fallback now uses Generic Tiered Cache instead, providing better performance and cache efficiency.</p>
<h4 id="how-it-works">How it works</h4>
<p>When Smart Tiered Cache falls back to Generic Tiered Cache:</p>
<ol>
<li><strong>Multiple upper-tiers</strong>: Uses all of Cloudflare's global data centers as a network of upper-tiers instead of a single optimal location.</li>
<li><strong>Distributed cache requests</strong>: Lower-tier data centers can query any available upper-tier for cached content.</li>
<li><strong>Improved global coverage</strong>: Provides better cache hit ratios across geographically distributed visitors.</li>
<li><strong>Automatic fallback</strong>: Seamlessly transitions when origin location cannot be determined, such as with Anycast-masked origins.</li>
</ol>
<h4 id="benefits">Benefits</h4>
<ul>
<li><strong>Preserves high performance during fallback</strong>: Smart Tiered Cache now maintains strong cache efficiency even when optimal upper tier selection is not possible.</li>
<li><strong>Minimizes latency impact</strong>: Automatically uses Generic Tiered Cache topology to keep performance high when origin location cannot be determined.</li>
<li><strong>Seamless experience</strong>: No configuration changes or intervention required when fallback occurs.</li>
<li><strong>Improved resilience</strong>: Smart Tiered Cache remains effective across diverse origin infrastructure, including Anycast-masked origins.</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>This improvement is automatically applied to all zones using <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a>. No action is required on your part.</p>
</div></article></div>
