<p>Web Analytics relies on the <code>performance.getEntriesByType('navigation')</code> object to collect metrics about page load performance. If Navigation Timing Level 2 is not supported, then <a href="https://developer.mozilla.org/en-US/docs/Web/API/Performance/timing"><code>performance.timing</code> (Level 1)</a> is used.</p>
<p>Refer to the <a href="https://www.w3.org/TR/navigation-timing-2/#processing-model">W3C Processing Model</a> for a visual depiction of the sequence of timing events for web page loads.</p>
<h2 id="data-collection-and-reporting">Data collection and reporting</h2>
<p>Web Analytics collects the minimum amount of information - timing metrics - to show customers how their websites perform. Cloudflare does not track individual end users across our customers’ Internet properties.</p>
<p>The Web Analytics performance beacon loads from <code>https://static.cloudflareinsights.com/beacon.min.js</code>. You may need to update your <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15777.md")
</div> settings to load this script.
<p>Beacon data is sent to <code>https://&lt;yourdomainname&gt;/cdn-cgi/rum</code> for sites proxied through Cloudflare or <code>https://cloudflareinsights.com/cdn-cgi/rum</code> for sites not proxied through Cloudflare. Core Web Vital metrics are reported when the <code>visibilityState</code> is hidden for the first time after the page load event is triggered.</p>
