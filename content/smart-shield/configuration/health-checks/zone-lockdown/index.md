<p>Currently, any Cloudflare customer on a paid plan can configure Health Checks against any host or IP. <a href="/waf/tools/zone-lockdown/">Zone Lockdown</a> specifies a list of one or more IP addresses, CIDR ranges, or networks that are the only IPs allowed to access a domain, subdomain, or URL. It allows multiple destinations in a single rule as well as IPv4 and IPv6 addresses. IP addresses not specified in the Zone Lockdown rule are denied access to the specified resources.</p>
<p>Customers who use zone lockdown and want their health checks to continue passing can use <a href="/waf/custom-rules/create-dashboard/">WAF custom rules</a> to bypass zone lockdown.</p>
<h2 id="bypass-zone-lockdown">Bypass zone lockdown</h2>
<p>To bypass zone lockdown using a WAF custom rule:</p>
<ol>
<li>
<p>Follow the steps to <a href="/waf/custom-rules/create-dashboard/">create a custom rule in the dashboard</a>.</p>
</li>
<li>
<p>Create a custom rule matching on <strong>user agent</strong>.</p>
<p>Cloudflare Health Checks have a user agent of the following format:
<code>Mozilla/5.0 (compatible;Cloudflare-Healthchecks/1.0;+https://www.cloudflare.com/; healthcheck-id: XXX)</code> where <code>XXX</code> is replaced with the first 16 characters of the Health Check ID.</p>
<p>To allow a specific Health Check, verify if the user agent contains the first 16 characters of the Health Check ID.</p>
</li>
<li>
<p>Set the action to <em>Skip</em> and the corresponding feature to <strong>Zone Lockdown</strong> under <strong>More components to skip</strong>.</p>
</li>
</ol>
<h3 id="via-the-api">Via the API</h3>
<p>This example adds a new WAF custom rule to the ruleset with ID <code>{ruleset_id}</code> that skips zone lockdown for incoming requests with a user agent containing <code>1234567890abcdef</code>:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/{zone_id}/rulesets/{ruleset_id}/rules&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;action&quot;: &quot;skip&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;products&quot;: [&#10;      &quot;zoneLockdown&quot;&#10;    ]&#10;  },&#10;  &quot;expression&quot;: &quot;http.user_agent contains \&quot;1234567890abcdef\&quot;&quot;,&#10;  &quot;description&quot;: &quot;bypass zone lockdown - specific healthcheck&quot;&#10;}&#x27;&#10;</code></pre>
