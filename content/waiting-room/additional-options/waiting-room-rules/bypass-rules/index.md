<p>A Waiting Room Bypass Rule is a type of Waiting Room Rule built on Cloudflare’s Ruleset Engine and managed via the Waiting Room API. A Waiting Room Bypass Rule allows you to indicate specific traffic or areas of your site or application that you do not want a waiting room to apply to. Each bypass rule is created and managed at the individual waiting room level for precise control over your waiting room traffic.</p>
<p>To indicate where you want your bypass rules to apply, write <a href="/ruleset-engine/rules-language/">custom logic</a> using the <a href="/ruleset-engine/rules-language/fields/reference/">fields</a> available via the Cloudflare Ruleset Engine, except the following:</p>
<ul>
<li><code>cf.threat_score</code> and fields starting with <code>cf.bot_management</code></li>
<li>HTTP response fields</li>
</ul>
<p>Please be advised that the waiting room will not apply to all the traffic that matches the expressions written for bypass rules and will not be counted as active users. No Waiting Room features, including but not limited to, Event pre-queueing, Reject queueing method, or Queue-all will apply to this traffic. Be mindful of this when creating and enabling Bypass Waiting Room rules. Only use bypass rules for traffic you are confident will not overwhelm your origin or cause significant traffic surges.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15764.md")
</aside>
<h2 id="common-use-cases">Common Use Cases</h2>
<ul>
<li><strong>Path/URL Exclusion</strong>: Bypass specific paths or URLs under the path you have configured for your waiting room, if you do not want your waiting room to apply to these paths.</li>
<li><strong>Administrative Bypass</strong>: Allow internal site administrators to always bypass the waiting room, commonly identified by IP addresses.</li>
<li><strong>Geo-targeting</strong>: Exclude certain countries from being queued.</li>
<li><strong>Query String Exclusion</strong>: Exclude specific query strings under the path you have configured for your waiting room.</li>
<li><strong>Exclude file extensions</strong>: Prevent waiting room from applying to certain file extensions, such as <code>.js</code> that you utilize on your waiting room HTML template so that they render properly.</li>
</ul>
<h3 id="a-note-on-subrequests">A note on subrequests</h3>
<p>Along with the query string(s) or paths you would like to exclude, make sure to include in your expression any paths or file types that subrequests may be hitting so that these assets or paths do not have waiting room applied as well. Otherwise, these subrequests will be getting the waiting room cookie since they are still covered by the waiting room.</p>
<p>These could include anything like images, JavaScript files, CSS files, etc. You can also configure the rule to bypass the waiting room for any paths of a file type by bypassing if a request ends with <code>.js</code>, <code>.css</code>, <code>.png</code>, etc., so you do not have to manually configure each path those assets may be stored under.</p>
<p>Example condition: <code>ends_with(http.request.uri.path, &quot;.js&quot;)</code></p>
<h2 id="create-waiting-room-bypass-rules-in-the-dashboard">Create Waiting Room Bypass Rules in the dashboard</h2>
<p>To create a new bypass rule:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Waiting Room</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Expand a waiting room and select <strong>Manage rules</strong>.</li>
<li>Select <strong>Create new bypass rule</strong>.</li>
<li>Enter a descriptive name for the rule in <strong>Rule name</strong>.</li>
<li>Under <strong>When incoming requests match</strong>, define the rule expression. Use the <strong>Field</strong> drop-down list to choose an HTTP property. For each request, the value of the property you choose for <strong>Field</strong> is compared to the value you specify for <strong>Value</strong> using the operator selected in <strong>Operator</strong>.</li>
<li>Under <strong>Then</strong>, the Bypass Waiting Room action is automatically selected. Before saving, review your expression and ensure that the traffic that matches your expression is the traffic that you do not want the waiting room to apply to.</li>
<li>To save and deploy your rule, select <strong>Save and Deploy</strong>. If you are not ready to deploy your rule, select <strong>Save as Draft</strong>.</li>
</ol>
<h3 id="operators-and-grouping-symbols">Operators and grouping symbols</h3>
<ul>
<li>Comparison operators specify how values defined in an expression must relate to the actual HTTP request value for the expression to return true.</li>
<li>Logical operators combine two expressions to form a compound expression and use order of precedence to determine how an expression is evaluated.</li>
<li>Grouping symbols allows you to organize expressions, enforce operator precedence, and nest expressions.</li>
</ul>
<p>For examples and usage, refer to <a href="/ruleset-engine/rules-language/operators/">Operators and grouping symbols</a> in the Rules language documentation.</p>
<h2 id="manage-rules-via-the-waiting-room-api">Manage Rules via the Waiting Room API</h2>
<p>You can manage, delete, and create bypass rules for your waiting room via the <a href="/api/resources/waiting_rooms/subresources/rules/methods/get/">Waiting Room API’s</a>. A bypass rule is a Waiting Room Rule that utilizes the <code>bypass_waiting_room</code> action.</p>
<p>When creating a Bypass Waiting Room Rule via API, make sure you:</p>
<ul>
<li>Have already created and saved a waiting room you want the rule to apply to.</li>
<li>Define the expression to indicate which traffic you would like to bypass your waiting room.</li>
<li>Set the rule action to <code>bypass_waiting_room</code>.</li>
</ul>
<p>Create a waiting room rule by appending the following endpoint in the Waiting Room API to the Cloudflare API base URL. New waiting room rules will be added after any existing rules.</p>
<pre><code class="language-txt">POST zones/{zone_id}/waiting_rooms/{room_id}/rules&#10;</code></pre>
<p>Configure your bypass rule with the following required and optional parameters:</p>
<ul>
<li><strong>Description</strong> (optional) - Give your rule a description to help keep a record of the purpose of this bypass rule.</li>
<li><strong>Expression</strong> (required) - Define the rule expression indicating which traffic to apply the bypass rule to.</li>
<li><strong>Action</strong> (required) - Define the action to take when expression evaluates to true. Set this to <code>bypass_waiting_room</code>.</li>
<li><strong>Enabled</strong> (optional) - This will default to true. If you do not wish to deploy your rule, you must set this to false.</li>
</ul>
<h3 id="api-examples">​​API Examples</h3>
<details class="nb-details"><summary>Bypass a path under your waiting room and all of its subpaths</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15765.md")
</div></details>
<details class="nb-details"><summary>Allow a defined list of IPs to bypass the waiting room</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15766.md")
</div></details>
<h3 id="other-api-options-for-managing-bypass-rules">Other API options for managing bypass rules</h3>
<p>Through the Waiting Room API, you can also do the following to manage bypass rules by using the Waiting Room rules API calls:</p>
<ul>
<li><strong>List Waiting Room Rules</strong>:  Lists rules for a waiting room.</li>
<li><strong>Replace Waiting Room Rules</strong>:  Replaces all rules for a waiting room.</li>
<li><strong>Patch Waiting Room Rules</strong>:  Updates a rule for a waiting room.</li>
<li><strong>Delete Waiting Room Rules</strong>: Deletes a rule for a waiting room.</li>
</ul>
