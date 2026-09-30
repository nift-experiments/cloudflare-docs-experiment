<p>Use the following workflow to deploy a custom ruleset:</p>
<ol>
<li><a href="/ruleset-engine/custom-rulesets/create-custom-ruleset/">Create a custom ruleset</a>, optionally providing a list of rules to include in the custom ruleset.</li>
<li>(Optional) <a href="/ruleset-engine/custom-rulesets/add-rules-ruleset/">Add rules to your custom ruleset</a>.</li>
<li><a href="/ruleset-engine/custom-rulesets/deploy-custom-ruleset/">Deploy the custom ruleset</a> by adding an <code>execute</code> rule to a phase entry point ruleset. If you skip this step, the rules of the custom ruleset will not run.</li>
</ol>
<p>Currently, custom rulesets are only supported by the <a href="/waf/">Cloudflare WAF</a>, both at the account and the zone level.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13277.md")
</aside>
<h2 id="change-the-behavior-of-a-custom-ruleset">Change the behavior of a custom ruleset</h2>
<p>To modify custom ruleset behavior, Cloudflare recommends <a href="/ruleset-engine/custom-rulesets/create-custom-ruleset/">creating a new custom ruleset</a> or <a href="/ruleset-engine/custom-rulesets/add-rules-ruleset/">editing the custom ruleset</a> instead of using overrides.</p>
