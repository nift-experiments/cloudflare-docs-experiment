<p>Applies one or more changes to an existing rule in a ruleset at the account or zone level.</p>
<p>Use one of the following API endpoints:</p>
<ul>
<li><a href="/api/resources/rulesets/subresources/rules/methods/edit/">Update an account ruleset rule</a><br/>
<code>PATCH /accounts/{account_id}/rulesets/{ruleset_id}/rules/{rule_id}</code></li>
<li><a href="/api/resources/rulesets/subresources/rules/methods/edit/">Update a zone ruleset rule</a><br/>
<code>PATCH /zones/{zone_id}/rulesets/{ruleset_id}/rules/{rule_id}</code></li>
</ul>
<p>You can update the definition of the rule, changing its fields, or change the order of the rule in the ruleset. Invoking this method creates a new version of the ruleset.</p>
<h2 id="update-the-definition-of-a-rule">Update the definition of a rule</h2>
<p>To update the definition of a rule, include the new rule definition in the request body. You must include all the rule fields that you want to be part of the new rule definition, even if you are not changing their values.</p>
<p>The response will include the complete ruleset after updating the rule.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{ruleset_id}/rules/{rule_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;action&quot;: &quot;js_challenge&quot;,&#10;  &quot;expression&quot;: &quot;(ip.src.country in {\&quot;GB\&quot; \&quot;FR\&quot;} and cf.bot_management.score &lt; 20 and not cf.bot_management.verified_bot)&quot;,&#10;  &quot;description&quot;: &quot;challenge GB and FR based on bot score&quot;&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Custom Ruleset 1&quot;,&#10;		&quot;description&quot;: &quot;My first custom ruleset&quot;,&#10;		&quot;kind&quot;: &quot;custom&quot;,&#10;		&quot;version&quot;: &quot;11&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID_1&gt;&quot;,&#10;				&quot;version&quot;: &quot;2&quot;,&#10;				&quot;action&quot;: &quot;js_challenge&quot;,&#10;				&quot;expression&quot;: &quot;(ip.src.country in {\&quot;GB\&quot; \&quot;FR\&quot;} and cf.bot_management.score &lt; 20 and not cf.bot_management.verified_bot)&quot;,&#10;				&quot;description&quot;: &quot;challenge GB and FR based on bot score&quot;,&#10;				&quot;last_updated&quot;: &quot;2023-03-22T12:54:58.144683Z&quot;,&#10;				&quot;ref&quot;: &quot;&lt;RULE_REF_1&gt;&quot;,&#10;				&quot;enabled&quot;: true&#10;			},&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID_2&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;challenge&quot;,&#10;				&quot;expression&quot;: &quot;not http.request.uri.path matches \&quot;^/api/.*$\&quot;&quot;,&#10;				&quot;last_updated&quot;: &quot;2022-11-23T11:36:24.192361Z&quot;,&#10;				&quot;ref&quot;: &quot;&lt;RULE_REF_2&gt;&quot;,&#10;				&quot;enabled&quot;: true&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2023-03-22T12:54:58.144683Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_custom&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="change-the-order-of-a-rule-in-a-ruleset">Change the order of a rule in a ruleset</h2>
<p>To reorder a rule in a list of ruleset rules, include a <code>position</code> object in the request, containing one of the following:</p>
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
@markup("md", "content/.markup/bodies/13239.md")
</aside>
<p>Reorder a rule without changing its definition by including only the <code>position</code> object in the <code>PATCH</code> request body. You can also update a rule definition and reorder it in the same <code>PATCH</code> request by including both the <code>rule</code> object and the <code>position</code> object.</p>
<h3 id="examples">Examples</h3>
<p>The following examples build upon the following (abbreviated) ruleset:</p>
<pre><code class="language-json">{&#10;	&quot;rules&quot;: [&#10;		{ &quot;id&quot;: &quot;&lt;RULE_ID_1&gt;&quot; },&#10;		{ &quot;id&quot;: &quot;&lt;RULE_ID_2&gt;&quot; },&#10;		{ &quot;id&quot;: &quot;&lt;RULE_ID_3&gt;&quot; },&#10;		{ &quot;id&quot;: &quot;&lt;RULE_ID_4&gt;&quot; }&#10;	]&#10;}&#10;</code></pre>
<h4 id="example-1">Example 1</h4>
<p>The following request with the <code>position</code> object places rule <code>$RULE_ID_2</code> as the first rule:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules/{rule_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;position&quot;: {&#10;    &quot;before&quot;: &quot;&quot;&#10;  }&#10;}&#x27;</code></pre>
<p>In this case, the new rule order would be:</p>
<p><code>&lt;RULE_ID_2&gt;</code>, <code>&lt;RULE_ID_1&gt;</code>, <code>&lt;RULE_ID_3&gt;</code>, <code>&lt;RULE_ID_4&gt;</code></p>
<h4 id="example-2">Example 2</h4>
<p>The following request with the <code>position</code> object places rule <code>$RULE_ID_2</code> after rule 3:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules/{rule_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;position&quot;: {&#10;    &quot;after&quot;: &quot;&lt;RULE_ID_3&gt;&quot;&#10;  }&#10;}&#x27;</code></pre>
<p>In this case, the new rule order would be:</p>
<p><code>&lt;RULE_ID_1&gt;</code>, <code>&lt;RULE_ID_3&gt;</code>, <code>&lt;RULE_ID_2&gt;</code>, <code>&lt;RULE_ID_4&gt;</code></p>
<h4 id="example-3">Example 3</h4>
<p>The following request with the <code>position</code> object places rule <code>$RULE_ID_1</code> in position 3, becoming the third rule in the ruleset:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules/{rule_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;position&quot;: {&#10;    &quot;index&quot;: 3&#10;  }&#10;}&#x27;</code></pre>
<p>In this case, the new rule order would be:</p>
<p><code>&lt;RULE_ID_2&gt;</code>, <code>&lt;RULE_ID_3&gt;</code>, <code>&lt;RULE_ID_1&gt;</code>, <code>&lt;RULE_ID_4&gt;</code></p>
