<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 9, 2025</time><h2 id="post-title">Expanded CT log activity insights on Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> has expanded its Certificate Transparency (CT) log insights with new stats that provide greater visibility into log activity:</p>
<ul>
<li><strong>Log growth rate</strong>: The average throughput of the CT log over the past 7 days, measured in certificates per hour.</li>
<li><strong>Included certificate count</strong>: The total number of certificates already included in this CT log.</li>
<li><strong>Eligible-for-inclusion certificate count</strong>: The number of certificates eligible for inclusion in this log but not yet included. This metric is based on certificates signed by trusted root CAs within the log’s accepted date range.</li>
<li><strong>Last update</strong>: The timestamp of the most recent update to the CT log.</li>
</ul>
<p>These new statistics have been added to the response of the <a href="/api/resources/radar/subresources/ct/subresources/logs/methods/get/">Get Certificate Log Details</a> API endpoint, and are displayed on the <a href="https://radar.cloudflare.com/certificate-transparency/log/nimbus2025#log-activity">CT log information page</a>.</p>
<p><img src="/assets/upstream/images/radar/ct-log-activity.png" alt="Screenshot of the CT log activity card on the CT log information page" /></p>
</div></article></div>
