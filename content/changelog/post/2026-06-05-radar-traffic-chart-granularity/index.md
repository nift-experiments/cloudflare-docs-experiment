<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 5, 2026</time><h2 id="post-title">Finer-grained chart granularity on Cloudflare Radar for longer time ranges</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now provides finer-grained traffic charts for longer time ranges. Previously, selecting a 1-3 month view on HTTP and NetFlows charts defaulted to weekly aggregation, which was too coarse to surface meaningful trends. Views longer than 3 months defaulted to monthly aggregation, returning as few as 7 data points for a 6-month range.</p>
<p>The new defaults are:</p>
<ul>
<li><strong>1-3 months</strong>: daily granularity (7x more data points)</li>
<li><strong>Longer than 3 months</strong> (HTTP and NetFlows): weekly granularity (4x more data points)</li>
</ul>
<p>For example, a 12-week traffic view previously showed weekly data:</p>
<p><img src="/assets/upstream/images/radar/traffic-granularity-12w-before.png" alt="Traffic trends chart with weekly granularity for a 12-week view" /></p>
<p>The same view now shows daily data:</p>
<p><img src="/assets/upstream/images/radar/traffic-granularity-12w-after.png" alt="Traffic trends chart with daily granularity for a 12-week view" /></p>
<p>Similarly, a 1-year HTTP traffic view that previously showed just 12 monthly data points now provides 52 weekly data points.</p>
<p>Visit <a href="https://radar.cloudflare.com/?dateRange=12w#traffic-trends">Cloudflare Radar</a> to explore the new granular views.</p>
</div></article></div>
