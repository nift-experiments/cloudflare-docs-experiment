<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8707.md")
</aside>
<h2 id="delete-multiple-rules">Delete multiple rules</h2>
<p>This example deletes firewall rules with IDs <code>{rule_id_1}</code> and <code>{rule_id_2}</code>.</p>
<pre><code class="language-bash">curl --request DELETE \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules?id={rule_id_1}&amp;id={rule_id_2}&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;&lt;RULE_ID_1&gt;&quot;&#10;		},&#10;		{&#10;			&quot;id&quot;: &quot;&lt;RULE_ID_2&gt;&quot;&#10;		}&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="delete-a-single-rule">Delete a single rule</h2>
<p>This example deletes the rule with ID <code>{rule_id}</code>.</p>
<pre><code class="language-bash">curl --request DELETE \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules/{rule_id}&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;&#10;		}&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
