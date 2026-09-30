<p>By default, Cloudflare allows requests on a <a href="/fundamentals/reference/network-ports/">number of different HTTP ports</a>.</p>
<p>You can target requests based on their HTTP port with the <a href="/ruleset-engine/rules-language/fields/reference/cf.edge.server_port/"><code>cf.edge.server_port</code></a> field. Use the <code>in</code> <a href="/ruleset-engine/rules-language/operators/#comparison-operators">comparison operator</a> to target a set of ports.</p>
<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> blocks requests to <code>www.example.com</code> that are not on ports <code>80</code> or <code>443</code>:</p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Use the expression editor:<br/>
<code>(http.host eq &quot;www.example.com&quot; and not cf.edge.server_port in {80 443})</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Block</em></p>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="open-server-ports-and-blocked-traffic">Open server ports and blocked traffic</h3>
@markup("md", "content/.markup/bodies/15458.md")
</aside>
