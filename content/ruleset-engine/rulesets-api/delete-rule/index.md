<p>Deletes a single rule in a ruleset at the account or zone level.</p>
<p>Use one of the following API endpoints:</p>
<ul>
<li><a href="/api/resources/rulesets/subresources/rules/methods/delete/">Delete an account ruleset rule</a><br/>
<code>DELETE /accounts/{account_id}/rulesets/{ruleset_id}/rules/{rule_id}</code></li>
<li><a href="/api/resources/rulesets/subresources/rules/methods/delete/">Delete a zone ruleset rule</a><br/>
<code>DELETE /zones/{zone_id}/rulesets/{ruleset_id}/rules/{rule_id}</code></li>
</ul>
<p>If the delete operation succeeds, the API method call returns a <code>200 OK</code> HTTP status code with the complete ruleset in the response body.</p>
<h2 id="example">Example</h2>
<p>The following example deletes rule <code>$RULE_ID_1</code> belonging to ruleset <code>$RULESET_ID</code>.</p>
<p>The response will include the complete ruleset after deleting the rule.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{ruleset_id}/rules/{rule_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Custom Ruleset 1&quot;,&#10;		&quot;description&quot;: &quot;My first custom ruleset&quot;,&#10;		&quot;kind&quot;: &quot;custom&quot;,&#10;		&quot;version&quot;: &quot;12&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID_2&gt;&quot;,&#10;				&quot;version&quot;: &quot;2&quot;,&#10;				&quot;action&quot;: &quot;js_challenge&quot;,&#10;				&quot;expression&quot;: &quot;(ip.src.country in {\&quot;GB\&quot; \&quot;FR\&quot;} and cf.bot_management.score &lt; 20 and not cf.bot_management.verified_bot)&quot;,&#10;				&quot;description&quot;: &quot;challenge GB and FR based on bot score&quot;,&#10;				&quot;last_updated&quot;: &quot;2021-07-22T12:54:58.144683Z&quot;,&#10;				&quot;ref&quot;: &quot;&lt;RULE_REF_2&gt;&quot;,&#10;				&quot;enabled&quot;: true&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2021-07-22T12:54:58.144683Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_custom&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
