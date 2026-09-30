<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 28, 2026</time><h2 id="post-title">Account-level enforce DNS-only</h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>You can now disable Cloudflare's reverse proxy across all zones in your account simultaneously using the new <code>enforce_dns_only</code> setting. When enabled, Cloudflare responds to DNS queries for all proxied records with your origin IP addresses instead of Cloudflare's anycast IPs.
This account-level kill switch is designed for incident response scenarios where you need to quickly route traffic directly to your origin servers.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17717.md")</aside>
<h4 id="key-characteristics">Key characteristics</h4>
<ul>
<li><strong>Account-level</strong> — Affects all zones in the account simultaneously with a single API call.</li>
<li><strong>Non-destructive</strong> — Does not modify your DNS records. Disabling the setting restores normal proxy behavior.</li>
<li><strong>API-only</strong> — Available through the API only, not in the Cloudflare dashboard.</li>
</ul>
<h4 id="what-s-affected">What's affected</h4>
<p><strong>Included:</strong> Standard proxied A, AAAA, and CNAME records, Load Balancing records, and records matching Worker routes.</p>
<p><strong>Excluded:</strong> Spectrum applications, Cloudflare Tunnel CNAMEs, R2 custom domains, Web3 gateways, and Workers custom domains continue to operate normally.</p>
<h4 id="before-you-enable">Before you enable</h4>
<ul>
<li>Verify your origin servers can handle direct traffic without Cloudflare's caching and filtering.</li>
<li>Review which origin IPs will become publicly visible through DNS queries.</li>
<li>Test the API in a staging account before relying on it for incident response.</li>
</ul>
<h4 id="availability">Availability</h4>
<p>Available via API to all Cloudflare customers.</p>
<p>For information on how to use it, refer to <a href="/dns/proxy-status/enforce-dns-only/">Enforce DNS-only developer documentation</a> .</p>
</div></article></div>
