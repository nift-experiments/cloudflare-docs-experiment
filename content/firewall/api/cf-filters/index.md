<p><strong>Cloudflare Filters</strong> is an API-only component of firewall rules for designing complex criteria that rely on boolean operators and other logic to examine incoming HTTP traffic and look for a match.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/8708.md")
</aside>
<p>For example, a filter matching:</p>
<ul>
<li>An HTTP user agent, and</li>
<li>The HTTP path, and</li>
<li>The source IP address</li>
</ul>
<p>Associate a filter with a firewall rule to define the scope of that rule.</p>
<p>Use IP lists within a filter to refer collectively to a group of IP addresses. Refer to the <a href="/waf/tools/lists/lists-api/">Lists API</a> for more information.</p>
<p>Before getting started with the Cloudflare Filters API, familiarize yourself with rule <a href="/ruleset-engine/rules-language/expressions/">expressions</a>. For a complete reference, refer to <a href="/ruleset-engine/rules-language/">Rules language</a>.</p>
<h2 id="differences-from-other-cloudflare-apis">Differences from other Cloudflare APIs</h2>
<p>The Firewall Rules API behaves differently from most Cloudflare APIs in two ways:</p>
<ul>
<li>API calls accept and return multiple items, and allow applying data changes to multiple items.</li>
<li>Although API calls return the <a href="/fundamentals/api/">standard response</a>, the error object follows the <a href="http://jsonapi.org/format/#errors">JSON API standard</a>, such that in an error condition, it is clear which item produced the error and why.</li>
</ul>
<p>To get started, review <a href="/firewall/api/cf-filters/what-is-a-filter/">What is a filter?</a>, followed by the Cloudflare Filters <a href="/firewall/api/cf-firewall-rules/json-object/">JSON object</a> and <a href="/firewall/api/cf-firewall-rules/endpoints/">Endpoints</a>.</p>
