<h2 id="update-multiple-rules">Update multiple rules</h2>
<p>This example updates several firewall rules using a single API call.</p>
<p>You can include up to 25 rules in the JSON object array (<code>-d</code> flag) to update as a batch. The batch is handled as a transaction.</p>
<pre><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;[&#10;  {&#10;    &quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;    &quot;paused&quot;: false,&#10;    &quot;description&quot;: &quot;Challenge site&quot;,&#10;    &quot;action&quot;: &quot;challenge&quot;,&#10;    &quot;priority&quot;: null,&#10;    &quot;filter&quot;: {&#10;      &quot;id&quot;: &quot;&lt;FILTER_ID&gt;&quot;,&#10;      &quot;expression&quot;: &quot;not http.request.uri.path matches \&quot;^/api/.*$\&quot;&quot;,&#10;      &quot;paused&quot;: false,&#10;      &quot;description&quot;: &quot;not /api&quot;&#10;    }&#10;  }&#10;]&#x27;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8703.md")
</aside>
<pre><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;			&quot;paused&quot;: false,&#10;			&quot;description&quot;: &quot;Challenge site&quot;,&#10;			&quot;action&quot;: &quot;challenge&quot;,&#10;			&quot;priority&quot;: null,&#10;			&quot;filter&quot;: {&#10;				&quot;id&quot;: &quot;&lt;FILTER_ID&gt;&quot;,&#10;				&quot;expression&quot;: &quot;not http.request.uri.path matches \&quot;^/api/.*$\&quot;&quot;,&#10;				&quot;paused&quot;: false,&#10;				&quot;description&quot;: &quot;not /api&quot;&#10;			}&#10;		}&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="update-a-single-rule">Update a single rule</h2>
<p>This example updates the firewall rule with ID <code>{rule_id}</code>.</p>
<p>You must include the following fields in the request body:</p>
<ul>
<li><code>id</code></li>
<li><code>action</code></li>
<li><code>filter.id</code></li>
</ul>
<p>All other fields are optional.</p>
<pre><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules/{rule_id}&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;  &quot;paused&quot;: false,&#10;  &quot;description&quot;: &quot;Do not challenge login from office IPv6&quot;,&#10;  &quot;action&quot;: &quot;allow&quot;,&#10;  &quot;priority&quot;: null,&#10;  &quot;filter&quot;: {&#10;    &quot;id&quot;: &quot;&lt;FILTER_ID&gt;&quot;,&#10;    &quot;expression&quot;: &quot;ip.src in {2400:cb00::/32 2803:f800::/32 2c0f:f248::/32 2a06:98c0::/29} and (http.request.uri.path ~ \&quot;^.*/wp-login.php$\&quot; or http.request.uri.path ~ \&quot;^.*/xmlrpc.php$\&quot;)&quot;,&#10;    &quot;paused&quot;: false,&#10;    &quot;description&quot;: &quot;Login from office&quot;&#10;  }&#10;}&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;		&quot;paused&quot;: false,&#10;		&quot;description&quot;: &quot;Do not challenge login from office IPv6&quot;,&#10;		&quot;action&quot;: &quot;allow&quot;,&#10;		&quot;priority&quot;: null,&#10;		&quot;filter&quot;: {&#10;			&quot;id&quot;: &quot;&lt;FILTER_ID&gt;&quot;,&#10;			&quot;expression&quot;: &quot;ip.src in {2400:cb00::/32 2803:f800::/32 2c0f:f248::/32 2a06:98c0::/29} and (http.request.uri.path ~ \&quot;^.*/wp-login.php$\&quot; or http.request.uri.path ~ \&quot;^.*/xmlrpc.php$\&quot;)&quot;,&#10;			&quot;paused&quot;: false,&#10;			&quot;description&quot;: &quot;Login from office&quot;&#10;		}&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8702.md")
</aside>
