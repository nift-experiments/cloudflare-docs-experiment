<p>The version metadata binding can be used to access metadata associated with a <a href="/workers/versions-and-deployments/#versions">version</a> from inside the Workers runtime.</p>
<p>Worker version ID, version tag and timestamp of when the version was created are available through the version metadata binding. They can be used in events sent to <a href="/analytics/analytics-engine/">Workers Analytics Engine</a> or to any third-party analytics/metrics service in order to aggregate by Worker version.</p>
<p>To use the version metadata binding, update your Worker's Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17182.md")
</div>
<h3 id="interface">Interface</h3>
<p>An example of how to access the version ID and version tag from within a Worker to send events to <a href="/analytics/analytics-engine/">Workers Analytics Engine</a>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17185.md")
</div></div>
