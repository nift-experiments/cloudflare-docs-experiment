<p>The threat intelligence detection matches incoming requests against indicators in the <a href="/security-center/cloudforce-one/">Cloudforce One</a> threat intelligence database. The detection matches on client IP address. If the IP was involved in threat activity in the past seven days, Cloudflare populates <a href="/waf/detections/threat-intelligence/fields/">threat intelligence fields</a> you can use in WAF rule expressions.</p>
<p>You can use these fields in <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/rate-limiting-rules/">rate limiting rules</a> to match on:</p>
<ul>
<li>Known threat actor names (<code>cf.intel.ip.attacker_names</code>)</li>
<li>Industries the IP address has targeted (<code>cf.intel.ip.target_industries</code>)</li>
<li>Source and target countries of threat activity (<code>cf.intel.ip.attacker_countries</code>, <code>cf.intel.ip.target_countries</code>)</li>
<li>The dataset that flagged the IP address (<code>cf.intel.ip.datasets</code> — values: <code>ddos</code>, <code>waf</code>)</li>
</ul>
<p>You can review matches in <a href="/waf/analytics/security-analytics/">Security Analytics</a> to see which threat actors and campaigns are reaching your application.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15480.md")
</aside>
<h2 id="data-freshness">Data freshness</h2>
<p>The threat intelligence database reflects a rolling seven-day window:</p>
<ul>
<li>An IP address flagged earlier in the window still matches, even if the threat is no longer active.</li>
<li>An IP address ages out seven days after the last observed activity. Rules that matched it stop matching with no notification.</li>
</ul>
<h2 id="availability">Availability</h2>
<p>Requires an active <a href="/security-center/cloudforce-one/">Cloudforce One</a> subscription. Contact your account team for access.</p>
<p>The WAF must be enabled on your zone before threat intelligence fields can be used in rule expressions.</p>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="/waf/detections/threat-intelligence/fields/">Threat intelligence fields</a> — Available fields and matching behavior.</li>
<li><a href="/waf/detections/threat-intelligence/get-started/">Get started</a> — Create your first threat intelligence rule.</li>
<li><a href="/security-center/cloudforce-one/">Threat Events</a> — Investigate threats in the Cloudforce One dashboard.</li>
</ul>
