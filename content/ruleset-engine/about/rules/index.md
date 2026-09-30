<p>A rule defines a filter and an action to perform on the incoming requests that match the filter.</p>
<ul>
<li>The rule <a href="/ruleset-engine/rules-language/expressions/">expression</a>, also called filter expression, defines the scope of the rule.</li>
<li>The rule <a href="/ruleset-engine/rules-language/actions/">action</a> defines what happens when there is a match for the expression.</li>
</ul>
<p>Rule expressions are defined using the <a href="/ruleset-engine/rules-language/">Rules language</a>.</p>
<p>For example, consider the following ruleset with four rules (R1, R2, R3, and R4). For a given incoming request, the expression of the first two rules matches the request properties. Therefore, the action for these rules runs (<em>Execute</em> and <em>Log</em>, respectively). The action of the first rule executes a managed ruleset, which means that every rule in the managed ruleset is evaluated. The action of the second rule logs an event associated with the current phase. There is no match for the expressions of rules 3 and 4, so their actions do not run. Since no rule blocks the request, it proceeds to the next phase.</p>
<p><img src="/assets/upstream/images/ruleset-engine/rulesets-rules-example.png" alt="Example of a rule execution scenario. Defines a ruleset with four rules, where the first rule executes a managed ruleset." /></p>
<p>Rules can have additional features through specific Cloudflare products. You may have more fields available for rule expressions, perform different actions, or configure additional behavior in a given phase.</p>
<h2 id="rule-evaluation">Rule evaluation</h2>
<p>When evaluating a rule, Cloudflare compares the values of request/response properties or derived values (obtained through <a href="/ruleset-engine/rules-language/fields/">fields</a>) to those defined in the rule's filter expression.</p>
<p>If the entire expression evaluates to <code>true</code>, there is a rule match and Cloudflare triggers the <a href="/ruleset-engine/rules-language/actions/">action</a> configured in the rule. If the expression evaluates to <code>false</code>, the rule does not match and its configured action is not applied.</p>
<p>Generally speaking, for <a href="/ruleset-engine/rules-language/actions/">non-terminating actions</a> the last change made by rules in the same <a href="/ruleset-engine/about/phases/">phase</a> will win (later rules can overwrite changes done by previous rules). However, for terminating actions (<em>Block</em>, <em>Redirect</em>, or one of the challenge actions), rule evaluation will stop and the action will be executed immediately.</p>
<p>For example, if multiple rules with the <em>Redirect</em> action match, Cloudflare will always use the URL redirect of the first rule that matches. Also, if you configure URL redirects using different Cloudflare products (Single Redirects and Bulk Redirects), the product executed first will apply, if there is a rule match (in this case, Single Redirects).</p>
<p>Refer to the <a href="/ruleset-engine/reference/phases-list/">Phases list</a> for the product execution order.</p>
<p>When you use <code>true</code> as the rule filter expression, this means &quot;apply the rule to every incoming request&quot; at the current <a href="/ruleset-engine/about/phases/">phase</a> level, which can be zone or account.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/13291.md")
</aside>
<h3 id="field-values-during-rule-evaluation">Field values during rule evaluation</h3>
<p>While evaluating rules for a given request/response, the values of all request and response <a href="/ruleset-engine/rules-language/fields/">fields</a> are immutable within each phase. However, field values may change between phases.</p>
<p>For example:</p>
<ul>
<li>If a <a href="/rules/transform/url-rewrite/">URL rewrite rule</a> #1 updates the URI path or the query string of a request, URL rewrite rule #2 will not take these earlier changes into consideration.</li>
<li>If a <a href="/rules/transform/request-header-modification/">request header transform rule</a> #1 sets the value of an HTTP request header, request header transform rule #2 will not be able to read or evaluate this new value.</li>
<li>If a URL rewrite rule updates the URI path or query string of a request, the <code>http.request.uri</code>, <code>http.request.uri.*</code>, and <code>http.request.full_uri</code> fields will have a different value in phases after the <code>http_request_transform</code> phase (where URL Rewrite Rules are executed).</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13290.md")
</aside>
