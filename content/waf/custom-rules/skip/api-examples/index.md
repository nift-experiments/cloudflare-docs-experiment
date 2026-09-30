<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to configure custom rules via API.</p>
<p>The <code>skip</code> action supports different <a href="/waf/custom-rules/skip/options/">skip options</a>, according to the security features or products that you wish to skip.</p>
<h2 id="before-you-continue">Before you continue</h2>
<p>This page contains examples of different skip rule scenarios for custom rules. Take the following into account:</p>
<ul>
<li>
<p>The <code>$ZONE_ID</code> value is the <a href="/fundamentals/account/find-account-and-zone-ids/">ID of the zone</a> where you want to add the rule.</p>
</li>
<li>
<p>The <code>$RULESET_ID</code> value is the ID of the <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">entry point ruleset</a> of the <code>http_request_firewall_custom</code> phase. For details on obtaining this ruleset ID, refer to <a href="/ruleset-engine/rulesets-api/view/">List and view rulesets</a>. The API examples in this page add a skip rule to an existing ruleset using the <a href="/api/resources/rulesets/subresources/rules/methods/create/">Create a zone ruleset rule</a> operation.</p>
<p>However, the entry point ruleset may not exist yet. In this case, invoke the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> operation to create the entry point ruleset with a skip rule. Refer to <a href="/ruleset-engine/rulesets-api/create/#example---create-a-zone-level-phase-entry-point-ruleset">Create ruleset</a> for an example.</p>
</li>
<li>
<p>Although each example only includes one action parameter, you can use several skip options in the same rule by specifying the <code>ruleset</code>, <code>phases</code>, and <code>products</code> action parameters simultaneously.</p>
</li>
</ul>
<h2 id="skip-the-remaining-rules-in-the-current-ruleset">Skip the remaining rules in the current ruleset</h2>
<p>This example invokes the <a href="/api/resources/rulesets/subresources/rules/methods/create/">Create a zone ruleset rule</a> operation to add a skip rule to the existing <code>http_request_firewall_custom</code> phase entry point ruleset with ID <code>$RULESET_ID</code>. The rule will skip all remaining rules in the current ruleset for requests matching the rule expression.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;action&quot;: &quot;skip&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;ruleset&quot;: &quot;current&quot;&#10;  },&#10;  &quot;expression&quot;: &quot;http.request.uri.path contains \&quot;/skip-current-ruleset/\&quot;&quot;,&#10;  &quot;description&quot;: &quot;&quot;&#10;}&#x27;</code></pre>
<h2 id="skip-a-phase">Skip a phase</h2>
<p>This example invokes the <a href="/api/resources/rulesets/subresources/rules/methods/create/">Create a zone ruleset rule</a> operation to add a rule to the existing <code>http_request_firewall_custom</code> phase entry point ruleset with ID <code>$RULESET_ID</code>. The rule will skip the <code>http_ratelimit</code> phase for requests matching the rule expression.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;action&quot;: &quot;skip&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;phases&quot;: [&#10;      &quot;http_ratelimit&quot;&#10;    ]&#10;  },&#10;  &quot;expression&quot;: &quot;http.request.uri.path contains \&quot;/skip-phase/\&quot;&quot;,&#10;  &quot;description&quot;: &quot;&quot;&#10;}&#x27;</code></pre>
<p>Refer to <a href="/waf/custom-rules/skip/options/">Available skip options</a> for the list of phases you can skip.</p>
<h2 id="skip-a-phase-and-do-not-log-matching-requests">Skip a phase and do not log matching requests</h2>
<p>This example invokes the <a href="/api/resources/rulesets/subresources/rules/methods/create/">Create a zone ruleset rule</a> operation to add a rule that:</p>
<ul>
<li>Skips the <code>http_ratelimit</code> phase</li>
<li>Disables event logging for the current rule</li>
</ul>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;action&quot;: &quot;skip&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;phases&quot;: [&#10;      &quot;http_ratelimit&quot;&#10;    ]&#10;  },&#10;  &quot;logging&quot;: {&#10;    &quot;enabled&quot;: false&#10;  },&#10;  &quot;expression&quot;: &quot;http.request.uri.path contains \&quot;/disable-logging/\&quot;&quot;,&#10;  &quot;description&quot;: &quot;&quot;&#10;}&#x27;</code></pre>
<p>Refer to <a href="/waf/custom-rules/skip/options/#log-requests-matching-the-skip-rule">Available skip options</a> for more information on disabling logging for requests that match a skip rule.</p>
<h2 id="skip-security-products">Skip security products</h2>
<p>This example uses the <a href="/api/resources/rulesets/subresources/rules/methods/create/">Create a zone ruleset rule</a> operation to add a rule that skips the <a href="/waf/tools/zone-lockdown/">Zone Lockdown</a> and <a href="/waf/tools/user-agent-blocking/">User Agent Blocking</a> products for requests matching the rule expression.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;action&quot;: &quot;skip&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;products&quot;: [&#10;      &quot;zoneLockdown&quot;,&#10;      &quot;uaBlock&quot;&#10;    ]&#10;  },&#10;  &quot;expression&quot;: &quot;http.request.uri.path contains \&quot;/skip-products/\&quot;&quot;,&#10;  &quot;description&quot;: &quot;&quot;&#10;}&#x27;</code></pre>
<p>Refer to <a href="/waf/custom-rules/skip/options/#skip-products">Available skip options</a> for the list of products you can skip.</p>
<h2 id="skip-the-remaining-rules-in-the-current-phase">Skip the remaining rules in the current phase</h2>
<p>This example invokes the <a href="/api/resources/rulesets/subresources/rules/methods/create/">Create a zone ruleset rule</a> operation to add a skip rule to the existing <code>http_request_firewall_custom</code> phase entry point ruleset with ID <code>$RULESET_ID</code>. The rule will skip all remaining rules in the <code>http_request_firewall_custom</code> phase for requests matching the rule expression.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;action&quot;: &quot;skip&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;phase&quot;: &quot;current&quot;&#10;  },&#10;  &quot;expression&quot;: &quot;http.request.uri.path contains \&quot;/skip-current-ruleset/\&quot;&quot;,&#10;  &quot;description&quot;: &quot;&quot;&#10;}&#x27;</code></pre>
<p>Currently, this skip option is only available at the zone level. Refer to <a href="/waf/custom-rules/skip/options/#skip-the-remaining-custom-rules-current-phase">Available skip options</a> for more details.</p>
