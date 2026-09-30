<p>Adds a single rule to an existing ruleset. Use this endpoint to add a rule without having to include all the existing ruleset rules in the request.</p>
<p>Use one of the following API endpoints:</p>
<ul>
<li><a href="/api/resources/rulesets/subresources/rules/methods/create/">Create an account ruleset rule</a><br/>
<code>POST /accounts/{account_id}/rulesets/{ruleset_id}/rules</code></li>
<li><a href="/api/resources/rulesets/subresources/rules/methods/create/">Create a zone ruleset rule</a><br/>
<code>POST /zones/{zone_id}/rulesets/{ruleset_id}/rules</code></li>
</ul>
<p>Include the rule definition in the request body.</p>
<p>By default, the rule will be added to the end of the existing list of rules in the ruleset. To define a specific position for the rule, include a <code>position</code> object in the request body according to the guidelines in <a href="/ruleset-engine/rulesets-api/update-rule/#change-the-order-of-a-rule-in-a-ruleset">Change the order of a rule in a ruleset</a>.</p>
<p>Invoking this method creates a new version of the ruleset.</p>
<h2 id="example">Example</h2>
<p>The following <code>POST</code> request adds a rule to ruleset <code>$RULESET_ID</code> of zone <code>$ZONE_ID</code>. The ruleset ID was previously obtained using the <a href="/api/resources/rulesets/methods/list/">List zone rulesets</a> operation, and corresponds to the entry point ruleset for the <code>http_request_firewall_custom</code> phase.</p>
<p>The response will include the complete ruleset after adding the rule.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;action&quot;: &quot;js_challenge&quot;,&#10;  &quot;expression&quot;: &quot;(ip.src.country in {\&quot;GB\&quot; \&quot;FR\&quot;} and cf.bot_management.score &lt; 20 and not cf.bot_management.verified_bot)&quot;,&#10;  &quot;description&quot;: &quot;challenge GB and FR based on bot score&quot;&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Zone Ruleset 1&quot;,&#10;		&quot;description&quot;: &quot;My phase entry point ruleset at the zone level&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;version&quot;: &quot;11&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID_1&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;challenge&quot;,&#10;				&quot;expression&quot;: &quot;not http.request.uri.path matches \&quot;^/api/.*$\&quot;&quot;,&#10;				&quot;last_updated&quot;: &quot;2023-11-23T11:36:24.192361Z&quot;,&#10;				&quot;ref&quot;: &quot;&lt;RULE_REF_1&gt;&quot;,&#10;				&quot;enabled&quot;: true&#10;			},&#10;			{&#10;				&quot;id&quot;: &quot;&lt;NEW_RULE_ID&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;js_challenge&quot;,&#10;				&quot;expression&quot;: &quot;(ip.src.country in {\&quot;GB\&quot; \&quot;FR\&quot;} and cf.bot_management.score &lt; 20 and not cf.bot_management.verified_bot)&quot;,&#10;				&quot;description&quot;: &quot;challenge GB and FR based on bot score&quot;,&#10;				&quot;last_updated&quot;: &quot;2024-06-22T12:35:58.144683Z&quot;,&#10;				&quot;ref&quot;: &quot;&lt;NEW_RULE_REF&gt;&quot;,&#10;				&quot;enabled&quot;: true&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2024-06-22T12:35:58.144683Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_custom&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="define-the-rule-position-in-the-ruleset">Define the rule position in the ruleset</h2>
<p>To define the position of the new rule in the ruleset, include a <code>position</code> object in the request, containing one of the following:</p>
<ul>
<li>
<p><code>&quot;before&quot;: &quot;&lt;RULE_ID&gt;&quot;</code> — Places the rule before rule <code>&lt;RULE_ID&gt;</code>. Use this argument with an empty rule ID value (<code>&quot;&quot;</code>) to set the rule as the first rule in the ruleset.</p>
</li>
<li>
<p><code>&quot;after&quot;: &quot;&lt;RULE_ID&gt;&quot;</code> — Places the rule after rule <code>&lt;RULE_ID&gt;</code>. Use this argument with an empty rule ID value (<code>&quot;&quot;</code>) to set the rule as the last rule in the ruleset.</p>
</li>
<li>
<p><code>&quot;index&quot;: &lt;POSITION_NUMBER&gt;</code> — Places the rule in the exact position specified by the integer number <code>&lt;POSITION_NUMBER&gt;</code>. Position numbers start with <code>1</code>. Existing rules in the ruleset from the specified position number onward are shifted one position (no rule is overwritten). For example, when you place a rule in position <var>n</var> using <code>index</code>, existing rules with index <var>n</var>, <var>n</var>+1, <var>n</var>+2, and so on, are shifted one position — their new position will be <var>n</var>+1, <var>n</var>+2, <var>n</var>+3, and so forth. If the index is out of range, the method returns a <code>400</code> HTTP status code.</p>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/13246.md")
</aside>
<p>For examples of using a <code>position</code> object, refer to <a href="/ruleset-engine/rulesets-api/update-rule/#examples">Update a rule in a ruleset</a>.</p>
