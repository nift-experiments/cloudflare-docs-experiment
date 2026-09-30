<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to configure payload logging for a managed ruleset via API.</p>
<h2 id="configure-and-enable-payload-logging">Configure and enable payload logging</h2>
<ol>
<li>
<p>Use the <a href="/api/resources/rulesets/subresources/phases/methods/get/">Get a zone entry point ruleset</a> operation to obtain the following IDs:</p>
<ul>
<li>The ID of the <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">entry point ruleset</a> of the <code>http_request_firewall_managed</code> <a href="/ruleset-engine/about/phases/">phase</a>.</li>
<li>The ID of the <code>execute</code> rule deploying the WAF managed ruleset, for which you want to configure payload logging.</li>
</ul>
</li>
<li>
<p>Use the <a href="/api/resources/rulesets/methods/update/">Update a zone ruleset rule</a> operation to update the rule you identified in the previous step.</p>
<p>Include a <code>matched_data</code> object in the rule's <code>action_parameters</code> object to configure payload logging. The <code>matched_data</code> object has the following structure:</p>
</li>
</ol>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  // ...&#10;  &quot;matched_data&quot;: {&#10;    &quot;public_key&quot;: &quot;&lt;PUBLIC_KEY_VALUE&gt;&quot;&#10;  }&#10;}&#10;</code></pre>
<p>Replace <code>&lt;PUBLIC_KEY_VALUE&gt;</code> with the public key you want to use for payload logging. You can generate a public key <a href="/waf/managed-rules/payload-logging/command-line/generate-key-pair/">in the command line</a> or <a href="/waf/managed-rules/payload-logging/configure/">in the Cloudflare dashboard</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="account-level-configuration">Account-level configuration</h3>
@markup("md", "content/.markup/bodies/15636.md")
</aside>
<h3 id="example">Example</h3>
<p>This example configures payload logging for the <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare Managed Ruleset</a>, which is already deployed for a zone with ID <code>$ZONE_ID</code>.</p>
<ol>
<li>Invoke the <a href="/api/resources/rulesets/subresources/phases/methods/get/">Get a zone entry point ruleset</a> operation to obtain the rules currently configured in the entry point ruleset of the <code>http_request_firewall_managed</code> phase.</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;060013b1eeb14c93b0dcd896537e0d2c&quot;, // entry point ruleset ID&#10;		&quot;name&quot;: &quot;default&quot;,&#10;		&quot;description&quot;: &quot;&quot;,&#10;		&quot;source&quot;: &quot;firewall_managed&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;version&quot;: &quot;3&quot;,&#10;		&quot;rules&quot;: [&#10;			// (...)&#10;			{&#10;				&quot;id&quot;: &quot;1bdb49371c1f46958fc8b985efcb79e7&quot;, // `execute` rule ID&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;execute&quot;,&#10;				&quot;expression&quot;: &quot;true&quot;,&#10;				&quot;last_updated&quot;: &quot;2024-01-20T14:21:28.643979Z&quot;,&#10;				&quot;ref&quot;: &quot;1bdb49371c1f46958fc8b985efcb79e7&quot;,&#10;				&quot;enabled&quot;: true,&#10;				&quot;action_parameters&quot;: {&#10;					&quot;id&quot;: &quot;efb7b8c949ac4650a09736fc376e9aee&quot;, // &quot;Cloudflare Managed Ruleset&quot; ID&#10;					&quot;version&quot;: &quot;latest&quot;&#10;				}&#10;			}&#10;			// (...)&#10;		],&#10;		&quot;last_updated&quot;: &quot;2024-01-20T14:29:00.190643Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<ol start="2">
<li>
<p>Save the following IDs for the next step:</p>
<ul>
<li>The ID of the entry point ruleset: <code>060013b1eeb14c93b0dcd896537e0d2c</code></li>
<li>The ID of the <code>execute</code> rule deploying the Cloudflare Managed Ruleset: <code>1bdb49371c1f46958fc8b985efcb79e7</code></li>
</ul>
<p>To find the correct rule in the <code>rules</code> array, search for an <code>execute</code> rule containing the ID of the Cloudflare Managed Ruleset (<code class="nb-rule-id" title="efb7b8c949ac4650a09736fc376e9aee">376e9aee</code>) in <code>action_parameters</code> &gt; <code>id</code>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15635.md")
</aside>
<ol start="3">
<li>Invoke the <a href="/api/resources/rulesets/methods/update/">Update a zone ruleset rule</a> operation to update the configuration of the rule you identified. The rule will now include the payload logging configuration (<code>matched_data</code> object).</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules/{rule_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;action&quot;: &quot;execute&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;id&quot;: &quot;efb7b8c949ac4650a09736fc376e9aee&quot;,&#10;    &quot;matched_data&quot;: {&#10;      &quot;public_key&quot;: &quot;Ycig/Zr/pZmklmFUN99nr+taURlYItL91g+NcHGYpB8=&quot;&#10;    }&#10;  },&#10;  &quot;expression&quot;: &quot;true&quot;&#10;}&#x27;</code></pre>
<p>The response will include the complete ruleset after updating the rule.</p>
<p>For more information on deploying managed rulesets via API, refer to <a href="/ruleset-engine/managed-rulesets/deploy-managed-ruleset/">Deploy a managed ruleset</a> in the Ruleset Engine documentation.</p>
<hr />
<h2 id="disable-payload-logging">Disable payload logging</h2>
<p>To disable payload logging for a managed ruleset:</p>
<ol>
<li>
<p>Use the <a href="/api/resources/rulesets/methods/update/">Update a zone ruleset rule</a> operation to update the rule deploying the managed ruleset (a rule with <code>&quot;action&quot;: &quot;execute&quot;</code>).</p>
</li>
<li>
<p>Modify the rule definition so that there is no <code>matched_data</code> object in <code>action_parameters</code>.</p>
</li>
</ol>
<p>For example, the following <code>PATCH</code> request updates the rule with ID <code>$RULE_ID</code> deploying the <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare Managed Ruleset</a> so that payload logging is disabled:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules/{rule_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;action&quot;: &quot;execute&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;id&quot;: &quot;efb7b8c949ac4650a09736fc376e9aee&quot;&#10;  },&#10;  &quot;expression&quot;: &quot;true&quot;&#10;}&#x27;</code></pre>
<p>For details on obtaining the entry point ruleset ID and the ID of the rule to update, refer to <a href="/waf/managed-rules/payload-logging/configure-api/#configure-and-enable-payload-logging">Configure and enable payload logging</a>.</p>
