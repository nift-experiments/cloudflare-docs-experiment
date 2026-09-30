<p><a href="/waf/custom-rules/">Custom rule</a> and <a href="/waf/rate-limiting-rules/">rate limiting rule</a> examples using <a href="/waf/detections/threat-intelligence/fields/">threat intelligence fields</a>. All fields are arrays — use <a href="/ruleset-engine/rules-language/functions/#any"><code>any()</code></a> with <code>[*]</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15488.md")
</aside>
<h2 id="log-matches-before-blocking">Log matches before blocking</h2>
<p>Deploy with <em>Log</em> (Enterprise plans) to review matches before enforcing:</p>
<ul>
<li><strong>Expression:</strong><br/>
<code>any(cf.intel.ip.attacker_names[*] != &quot;&quot;)</code></li>
<li><strong>Action:</strong> <em>Log</em></li>
</ul>
<p>Review matches in <a href="/waf/analytics/security-events/">Security Events</a>, then change the action to <em>Block</em> or <em>Managed Challenge</em>.</p>
<h2 id="block-ddos-participants-targeting-your-region">Block DDoS participants targeting your region</h2>
<ul>
<li><strong>Expression:</strong><br/>
<code>any(cf.intel.ip.target_countries[*] == &quot;FR&quot;) and any(cf.intel.ip.datasets[*] == &quot;ddos&quot;)</code></li>
<li><strong>Action:</strong> <em>Block</em></li>
</ul>
<h2 id="challenge-a-threat-actor-targeting-the-finance-sector">Challenge a threat actor targeting the finance sector</h2>
<ul>
<li><strong>Expression:</strong><br/>
<code>any(cf.intel.ip.target_industries[*] == &quot;Banking &amp; Financial Services&quot;) and any(cf.intel.ip.attacker_names[*] == &quot;BLACKBASTA&quot;)</code></li>
<li><strong>Action:</strong> <em>Managed Challenge</em></li>
</ul>
<h2 id="filter-by-attacker-country">Filter by attacker country</h2>
<ul>
<li><strong>Expression:</strong><br/>
<code>any(cf.intel.ip.attacker_countries[*] == &quot;CN&quot;)</code></li>
<li><strong>Action:</strong> <em>Block</em></li>
</ul>
<h2 id="combine-with-attack-score">Combine with attack score</h2>
<p>Block requests flagged by the WAF threat intelligence dataset that also have a low <a href="/waf/detections/attack-score/">attack score</a>:</p>
<ul>
<li><strong>Expression:</strong><br/>
<code>any(cf.intel.ip.datasets[*] == &quot;waf&quot;) and cf.waf.score lt 20</code></li>
<li><strong>Action:</strong> <em>Block</em></li>
</ul>
<h2 id="rate-limit-threat-actors-on-api-paths">Rate limit threat actors on API paths</h2>
<p><a href="/waf/rate-limiting-rules/">Rate limiting rule</a> applying a stricter rate to flagged IPs on your API:</p>
<ul>
<li><strong>Expression:</strong><br/>
<code>any(cf.intel.ip.datasets[*] == &quot;ddos&quot;) and starts_with(http.request.uri.path, &quot;/api/&quot;)</code></li>
<li><strong>Action:</strong> <em>Block</em> when the rate is exceeded.</li>
</ul>
