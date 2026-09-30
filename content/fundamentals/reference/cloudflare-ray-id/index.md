<p>A <strong>Cloudflare Ray ID</strong> is an identifier given to every request that goes through Cloudflare.</p>
<p>Ray IDs are particularly useful when evaluating Security Events for patterns or false positives or more generally understanding your application traffic.</p>
<p>Ray IDs are added as a <a href="/fundamentals/reference/http-headers/#cf-ray">request header, cf-ray</a>, to the connection from Cloudflare to the origin web server.
As such the Ray IDs can be found using the Developer Tools in your browser or using curl with the <code>-v</code> option to show the headers.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8807.md")
</aside>
<h2 id="look-up-ray-ids">Look up Ray IDs</h2>
<h3 id="security-events">Security events</h3>
<p>All customers can view Ray IDs and associated information — IP address, user agent, ASN, etc. — by looking through <a href="/waf/analytics/security-events/#sampled-logs">sampled logs</a> in Security Events.</p>
<p><img src="/assets/upstream/images/fundamentals/ray-id.png" alt="Example list of events in sampled logs, with the Ray ID highlighted from one of the expanded events to show its details" /></p>
<p>Additionally, you can <a href="/waf/analytics/security-events/#adjust-displayed-data">add filters</a> to look for specific Ray IDs.</p>
<p><img src="/assets/upstream/images/waf/events-add-filter.png" alt="Example of adding a new filter in Security Events for the Block action" /></p>
<p>Please note that Security Events may use sampled data to improve performance. If sampled data is applied to your search, you might not see all events, and filters might not return the expected results. To display more events, select a smaller timeframe.</p>
<h3 id="log-explorer">Log Explorer</h3>
<p><a href="/log-explorer/">Log Explorer</a> provides access to Cloudflare logs with all the context available within the Cloudflare platform.
You can monitor security and performance issues with custom dashboards or investigate and troubleshoot issues with log search.
Log explorer allows you to <a href="/log-explorer/log-search/">build queries</a> for filtering specific Ray IDs.</p>
<h3 id="logs">Logs</h3>
<p>Enterprise customers can enable Ray ID as a field in their <a href="/logs/">Cloudflare Logs</a>.</p>
<h3 id="server-logs">Server logs</h3>
<p>For more details about sending Ray IDs to your server logs, refer to the <a href="/fundamentals/reference/http-headers/#cf-ray">Cf-Ray</a> header.</p>
