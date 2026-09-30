<p>The <strong>Request rate analysis</strong> tab in <a href="/waf/analytics/security-analytics/">Security Analytics</a> displays data on the request rate for traffic matching the selected filters and time period. Use this tab to determine the most appropriate rate limit for incoming traffic matching the applied filters.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15365.md")
</aside>
<h2 id="user-interface-overview">User interface overview</h2>
<p>The <strong>Request rate analysis</strong> tab is available at the zone level in the <strong>Analytics</strong> page.</p>
<p><img src="/assets/upstream/images/waf/rate-limit-analytics.png" alt="Screenshot of the Request rate analysis tab in Security Analytics" /></p>
<p>The main chart displays the distribution of request rates for the top 50 unique clients observed during the selected time interval (for example, <code>1 minute</code>) in descending order. You can group the request rates by the following unique request properties:</p>
<ul>
<li><strong>IP address</strong></li>
<li><a href="/bots/additional-configurations/ja3-ja4-fingerprint/"><strong>JA3 fingerprint</strong></a> (only available to customers with Bot Management)</li>
<li><strong>IP &amp; JA3</strong> (only available to customers with Bot Management)</li>
<li><a href="/bots/additional-configurations/ja3-ja4-fingerprint/"><strong>JA4 fingerprint</strong></a> (only available to customers with Bot Management)</li>
<li><strong>IP &amp; JA4</strong> (only available to customers with Bot Management)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15364.md")
</aside>
<hr />
<h2 id="determine-an-appropriate-rate-limit">Determine an appropriate rate limit</h2>
<h3 id="1-define-the-scope"><ol>
<li>Define the scope</li>
</ol></h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15366.md")
</div>
<h3 id="2-find-the-rate"><ol start="2">
<li>Find the rate</li>
</ol></h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15367.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15363.md")
</aside>
<h3 id="3-validate-your-rate"><ol start="3">
<li>Validate your rate</li>
</ol></h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15368.md")
</div>
<h3 id="4-create-a-rate-limiting-rule"><ol start="4">
<li>Create a rate limiting rule</li>
</ol></h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15369.md")
</div>
