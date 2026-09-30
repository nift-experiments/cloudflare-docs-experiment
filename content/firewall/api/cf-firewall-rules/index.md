<p>Use the Firewall Rules API to programmatically manage your rules.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/8705.md")
</aside>
<p>When working with the Firewall Rules API, refer to these topics for additional context:</p>
<ul>
<li><a href="/firewall/cf-firewall-rules/actions/">Firewall rules actions</a></li>
<li><a href="/firewall/api/cf-filters/">Cloudflare Filters API</a></li>
</ul>
<p>To get started with the API, review the Firewall Rules API <a href="/firewall/api/cf-firewall-rules/json-object/">JSON object</a> and <a href="/firewall/api/cf-firewall-rules/endpoints/">Endpoints</a>.</p>
<p>For more information on the Rules language used to write rule expressions, refer to <a href="/ruleset-engine/rules-language/">Rules language</a> in the Ruleset Engine documentation.</p>
<h2 id="differences-from-other-cloudflare-apis">Differences from other Cloudflare APIs</h2>
<p>The Firewall Rules API behaves differently from most Cloudflare APIs in two ways:</p>
<ul>
<li>API calls accept and return multiple items, and allow applying data changes to multiple items.</li>
<li>Although API calls return the <a href="/fundamentals/api/">standard response</a>, the error object follows the <a href="http://jsonapi.org/format/#errors">JSON API standard</a>, such that in an error condition, it is clear which item produced the error and why.</li>
</ul>
