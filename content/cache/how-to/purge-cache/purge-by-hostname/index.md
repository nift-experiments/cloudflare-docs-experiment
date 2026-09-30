<p>Purging by hostname means that all assets at URLs with a host that matches one of the provided values will be instantly purged from the cache.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configuration</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under <strong>Purge Cache</strong>, select <strong>Custom Purge</strong>. The <strong>Custom Purge</strong> window appears.</li>
<li>Under <strong>Purge by</strong>, select <strong>Hostname</strong>.</li>
<li>Follow the syntax instructions:
<ul>
<li>One hostname per line.</li>
<li>Separated by commas.</li>
<li>You can purge up to 100 hostnames at a time.</li>
</ul>
</li>
<li>Enter the appropriate value(s) in the text field using the format shown in the example.</li>
<li>Select <strong>Purge</strong>.</li>
</ol>
<p>For information on rate limits, refer to the <a href="/cache/how-to/purge-cache/#availability-and-limits">Availability and limits</a> section.</p>
<h2 id="resulting-cache-status">Resulting cache status</h2>
<p>Purging by hostname deletes the resource, resulting in the <code>CF-Cache-Status</code> header being set to <a href="/cache/concepts/cache-responses/#miss"><code>MISS</code></a> for subsequent requests.</p>
<p>If <a href="/cache/how-to/tiered-cache/">tiered cache</a> is used, purging by hostname may return <code>EXPIRED</code>, as the lower tier tries to revalidate with the upper tier to reduce load on the latter.
Depending on whether the upper tier has the resource or not, and whether the end user is reaching the lower tier or the upper tier, <code>EXPIRED</code> or <code>MISS</code> are returned.</p>
