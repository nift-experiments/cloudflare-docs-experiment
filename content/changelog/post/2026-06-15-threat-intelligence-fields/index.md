<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 15, 2026</time><h2 id="post-title">Use Cloudforce One threat intelligence in WAF rules</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>You can now match incoming requests against Cloudforce One threat intelligence in your WAF rules. A new detection looks up the client IP address of each request against the threat intelligence database. If the IP was involved in threat activity in the past seven days, Cloudflare populates <code>cf.intel.ip.*</code> fields that you can use in <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/rate-limiting-rules/">rate limiting rules</a>.</p>
<p>The detection populates the following fields. Use the <a href="/ruleset-engine/rules-language/functions/#any"><code>any()</code></a> function with the <code>[*]</code> wildcard to match array values:</p>
<ul>
<li><code>cf.intel.ip.datasets</code> — the dataset that flagged the IP address (<code>ddos</code> or <code>waf</code>).</li>
<li><code>cf.intel.ip.target_industries</code> — industries the IP address has targeted.</li>
<li><code>cf.intel.ip.attacker_names</code> — known threat actors associated with the IP address.</li>
<li><code>cf.intel.ip.attacker_countries</code> — source countries of the threat activity.</li>
<li><code>cf.intel.ip.target_countries</code> — countries the IP address has targeted.</li>
</ul>
<p>For example, the following custom rule expression blocks requests from IP addresses associated with DDoS activity that have targeted France:</p>
<pre><code class="language-txt">any(cf.intel.ip.target_countries[*] == &quot;FR&quot;) and any(cf.intel.ip.datasets[*] == &quot;ddos&quot;)&#10;</code></pre>
<p>These fields work with the Cloudflare API and Terraform. Matches are logged in <a href="/waf/analytics/security-analytics/">Security Analytics</a>.</p>
<p>The threat intelligence detection is available to customers with an active <a href="/security-center/cloudforce-one/">Cloudforce One</a> subscription. For more information, refer to <a href="/waf/detections/threat-intelligence/">Threat intelligence</a>.</p>
</div></article></div>
