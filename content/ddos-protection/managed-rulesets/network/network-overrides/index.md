<p>When Cloudflare's DDoS Protection systems detect an attack, an ephemeral mitigation rule is created and installed in-line to mitigate the attack. A mitigation rule is generated based on the logic of the DDoS Protection managed ruleset. Each mitigation rule is generated from a single managed rule.</p>
<p>All mitigations and its associated managed rules are evaluated in order by the DDoS systems one by one. Cloudflare will go through all of the rule overrides defined in the ruleset overrides until one matches the managed rule, and apply the action and stop at that point. Otherwise, the evaluation will continue in order until a rule matches.</p>
<p>You can create only one ruleset override that can contain one or multiple rule overrides.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7543.md")
</aside>
<p>A rule override instructs the DDoS system on the action it should take against the attack according to its matching managed rule.</p>
<p>However, within a rule override, specificity matters and the DDoS system will choose the more specific configuration. A rule override takes precedence over the ruleset override.</p>
<h2 id="example">Example</h2>
<p>A DDoS managed ruleset contains the following managed rules:</p>
<ul>
<li><strong>Managed rule 1</strong></li>
<li><strong>Managed rule 2</strong></li>
<li><strong>Managed rule 3</strong></li>
</ul>
<p>The following ruleset overrides have been configured:</p>
<ul>
<li><strong>Ruleset override A</strong>
<ul>
<li><strong>Managed rule 1</strong> is set to <code>block</code></li>
</ul>
</li>
<li><strong>Ruleset override B</strong>
<ul>
<li>The action of the entire ruleset (or <em>all managed rules</em>) is set to <code>Managed Challenge</code></li>
<li><strong>Managed rule 1</strong> is set to <code>log</code></li>
<li><strong>Managed rule 2</strong> is set to <code>log</code></li>
</ul>
</li>
<li><strong>Ruleset override C</strong>
<ul>
<li><strong>Managed rule 3</strong> is set to <code>log</code></li>
</ul>
</li>
</ul>
<h3 id="use-case">Use case</h3>
<p>A DDoS attack was detected on <strong>managed rules 1</strong>, <strong>2</strong>, and <strong>3</strong>, and has generated a mitigation rule.</p>
<ul>
<li>
<p>Since <strong>managed rule 1</strong> matches <strong>ruleset override A</strong>, Cloudflare will <code>block</code> the attacks and not proceed with the rest of the rules.</p>
</li>
<li>
<p><strong>Managed rule 2</strong> does not match <strong>ruleset override A</strong>, so Cloudflare proceeds to <strong>ruleset override B</strong>. <br /> <strong>Ruleset override B</strong> matches both all managed rules and <strong>managed rule 2</strong>, but specificity takes precedence. It does not <code>challenge</code> and instead proceeds with <code>log</code> since it matches the most specific managed rule.</p>
</li>
<li>
<p><strong>Managed rule 3</strong> does not match <strong>ruleset override A</strong>, so Cloudflare proceeds to <strong>rule override B</strong>. Since <strong>ruleset override B</strong> sets <em>all managed rules</em> to <code>challenge</code>, then Cloudflare does not proceed to <strong>ruleset override C</strong>.</p>
</li>
</ul>
<p>An additional dimension to take into account is Cloudflare’s DDoS systems will apply a given rule override only if its conditions are met — which includes the Sensitivity level. So, while it needs to match and modify the correct managed rule (or everything in the case of all managed rules above), it also has to meet the specified Sensitivity level of the rule.</p>
<ul>
<li>
<p><strong>Rule override A</strong></p>
<ul>
<li><em>All managed rules</em> are set to <code>challenge</code> at low sensitivity</li>
</ul>
</li>
<li>
<p><strong>Rule override B</strong></p>
<ul>
<li><strong>Managed rule 1</strong> is set to <code>log</code> at default sensitivity</li>
</ul>
</li>
</ul>
<p>You receive a small attack below the threshold for low sensitivity, but above the threshold for high sensitivity on <strong>managed rule 1</strong>.</p>
<ul>
<li><strong>Rule override A</strong> does not meet the low sensitivity threshold. Therefore, we do not match the override and do not mitigate the attack, but proceed to evaluate the next managed rule in case the rule override instructs DoS to mitigate.</li>
<li><strong>Rule override B</strong> sets <code>log</code> at default visibility, which matches the condition. So, the defined action is applied and attack traffic is logged.</li>
</ul>
