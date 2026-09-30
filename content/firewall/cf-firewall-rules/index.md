<p>Cloudflare Firewall Rules is a flexible and intuitive framework for filtering HTTP requests. It gives you fine-grained control over which requests reach your applications, proactively inspecting incoming site traffic and automatically responding to threats.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/8693.md")
</aside>
<p>In a firewall rule you define an <a href="/ruleset-engine/rules-language/expressions/">expression</a> that tells Cloudflare what to look for in a request, and specify the appropriate <a href="/firewall/cf-firewall-rules/actions/">action</a> to take when those conditions are met. Expressions can reference <a href="/waf/tools/lists/custom-lists/#ip-lists">IP lists</a> - groups of IP addresses that you can reference collectively by name.</p>
<p>To write firewall rule expressions, use the <a href="/ruleset-engine/rules-language/">Rules language</a>, a powerful expression language inspired in the Wireshark Display Filter language.</p>
