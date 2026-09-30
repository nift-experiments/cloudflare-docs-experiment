<p>Targeting rules let you serve different flag values to different users based on their attributes. Each flag can have zero or more rules.</p>
<p>Rules are evaluated in sequential order, from top to bottom. The first rule whose conditions match is used, and its configured variant is returned. If no rule matches, Flagship returns the flag's default variant.</p>
<p>When a flag is disabled, the default variant is always returned regardless of rules.</p>
<p>Place more specific rules before broader rules. A broad catch-all rule can prevent later rules from running.</p>
<h2 id="how-rules-work">How rules work</h2>
<p>A rule consists of:</p>
<ul>
<li><strong>Conditions</strong> — One or more attribute comparisons that must be satisfied. For example, <code>country equals &quot;US&quot;</code> or <code>plan in [&quot;enterprise&quot;, &quot;business&quot;]</code>.</li>
<li><strong>Serve variant</strong> — The variant to return when the rule matches.</li>
<li><strong>Rollout</strong> (optional) — A percentage-based gradual release. Only the specified percentage of matching users receive the rule's variant. The rest continue to the next rule.</li>
</ul>
<h2 id="condition-structure">Condition structure</h2>
<p>Each condition compares an attribute from the evaluation context against a value using an operator:</p>
<ul>
<li><strong>Attribute</strong> — The context key to evaluate (for example, <code>userId</code>, <code>country</code>, <code>plan</code>).</li>
<li><strong>Operator</strong> — The comparison to perform. Flagship supports <a href="/flagship/targeting/operators/">11 operators</a>.</li>
<li><strong>Value</strong> — The value to compare against. Can be a string, number, or array depending on the operator.</li>
</ul>
<p>If the evaluation context does not include the attribute referenced by a condition, that condition does not match.</p>
<h2 id="logical-grouping">Logical grouping</h2>
<p>Conditions within a rule can be grouped with <code>AND</code>/<code>OR</code> operators and nested up to five levels deep.</p>
<p>For example, to target enterprise users in the US or Canada:</p>
<ul>
<li><code>AND</code>:
<ul>
<li><code>plan equals &quot;enterprise&quot;</code></li>
<li><code>OR</code>:
<ul>
<li><code>country equals &quot;US&quot;</code></li>
<li><code>country equals &quot;CA&quot;</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>Use the smallest set of context attributes necessary to express the rule. This keeps rule behavior easier to reason about and avoids sending unnecessary user data in evaluation context.</p>
<h2 id="learn-more">Learn more</h2>
<ul class="directory-listing"><li><a href="/flagship/targeting/operators/">Operators</a></li><li><a href="/flagship/targeting/percentage-rollouts/">Percentage rollouts</a></li></ul>
