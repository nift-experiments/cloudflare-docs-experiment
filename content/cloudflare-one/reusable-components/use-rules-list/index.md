<p><a href="/waf/tools/lists/custom-lists/#ip-lists">IP lists</a> are a part of Cloudflare's custom lists. Custom lists contain one or more items of the same type — IP addresses, hostnames or ASNs — that you can reference in rule expressions.</p>
<p>IP lists are defined at the account level and can be used to match against <code>ip.src</code> and <code>ip.dst</code> fields. Currently, Cloudflare Network Firewall only supports IPv4 addresses in these lists, not IPv6.</p>
<p>To use this feature:</p>
<h2 id="1-create-a-new-ip-list-api-resources-rules-subresources-lists-methods-create"><ol>
<li>Create a <a href="/api/resources/rules/subresources/lists/methods/create/">new IP list</a>.</li>
</ol></h2>
<p>For example:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/rules/lists \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;iplist&quot;,&#10;  &quot;description&quot;: &quot;This contains IPs that should be allowed.&quot;,&#10;  &quot;kind&quot;: &quot;ip&quot;&#10;}&#x27;&#10;</code></pre>
<h2 id="2-add-ips-to-the-list"><ol start="2">
<li>Add IPs to the list</li>
</ol></h2>
<p>Next, <a href="/api/resources/rules/subresources/lists/subresources/items/methods/create/">create list items</a>. This will add elements to the current list.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/rules/lists/{list_id}/items \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;[&#10;  {&quot;ip&quot;:&quot;10.0.0.1&quot;},&#10;  {&quot;ip&quot;:&quot;10.10.0.0/24&quot;}&#10;]&#x27;&#10;</code></pre>
<h2 id="3-use-the-list-in-a-rule"><ol start="3">
<li>Use the list in a rule</li>
</ol></h2>
<p>Finally, add a Cloudflare Network Firewall rule referencing the list into an existing ruleset:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{ruleset_id}/rules \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;action&quot;: &quot;skip&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;ruleset&quot;: &quot;current&quot;&#10;  },&#10;  &quot;expression&quot;: &quot;ip.src in $iplist&quot;,&#10;  &quot;description&quot;: &quot;Allowed IPs from iplist&quot;,&#10;  &quot;enabled&quot;: true&#10;}&#x27;&#10;</code></pre>
<h2 id="managed-lists">Managed lists</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4433.md")
</aside>
<p>You can create rules with managed lists. Managed IP Lists are <a href="/waf/tools/lists/managed-lists/#managed-ip-lists">lists of IP addresses</a> maintained by Cloudflare and updated frequently.</p>
<p>You can access these managed lists when you create rules with either <em>IP destination address</em> or <em>IP source address</em> in the <strong>Field</strong> dropdown, and <em>is in list</em> or <em>is not in list</em> in the <strong>Operator</strong> dropdown.</p>
<p>For example:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>IP destination address</em></td>
<td><em>is in list</em></td>
<td><em>Anonymizers</em></td>
</tr>
</tbody>
</table>
<h2 id="list-types">List types</h2>
<h3 id="threat-intelligence">Threat intelligence</h3>
<p>Cloudflare handles millions of HTTP requests each second and blocks billions of cyber threats each day. Cloudflare uses that data to detect malicious actors on the Internet and turns that information into a list of known malicious IP addresses. Cloudflare also integrates with a number of third-party vendors to augment the coverage.</p>
<p>The threat intelligence feed categories are described in <a href="/waf/tools/lists/managed-lists/#managed-ip-lists">Managed IP Lists</a>. All of these lists are compatible with Cloudflare Network Firewall.</p>
<h3 id="ip-lists">IP lists</h3>
<p>Use <a href="/waf/tools/lists/custom-lists/#ip-lists">IP lists</a> to group services in networks, like web servers, or for lists of known bad IP addresses to make managing good network endpoints easier. IP lists are helpful for users with very expansive firewall rules with many IP lists. By default, you can add up to 10,000 IPs across all lists. Refer to <a href="/cloudflare-one/traffic-policies/packet-filtering/add-policies/#use-an-ip-list">Use an IP list</a> to check an example of how to use an IP list.</p>
<h3 id="geo-blocking">Geo-blocking</h3>
<p>Geo-blocking enables you to selectively allow or block traffic to any country. Refer to <a href="/cloudflare-one/traffic-policies/packet-filtering/add-policies/#block-a-country">Block a country</a> to check an example of how to block a country.</p>
