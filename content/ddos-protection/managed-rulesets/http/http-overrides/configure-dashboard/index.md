<p>Configure the HTTP DDoS Attack Protection managed ruleset by defining <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">overrides</a> in the Cloudflare dashboard. DDoS overrides allow you to customize the <strong>action</strong> and <strong>sensitivity</strong> of one or more rules in the managed ruleset.</p>
<p>For more information on the available parameters and allowed values, refer to <a href="/ddos-protection/managed-rulesets/http/override-parameters/">Ruleset parameters</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="number-of-available-overrides">Number of available overrides</h3>
@markup("md", "content/.markup/bodies/7531.md")
</aside>
<p>Create multiple rules in the <code>ddos_l7</code> phase entry point ruleset to define different overrides for different sets of incoming requests. Set each rule expression according to the traffic whose HTTP DDoS protection you wish to customize.</p>
<p>Rules in the phase entry point ruleset, where you create overrides, are evaluated in order until there is a match for a rule expression and sensitivity level, and Cloudflare will apply the first rule that matches the request. Therefore, the rule order in the entry point ruleset is very important.</p>
<h2 id="access">Access</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7532.md")
</div>
<h3 id="create-a-ddos-override">Create a DDoS override</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7535.md")
</div>
<h3 id="delete-a-ddos-override">Delete a DDoS override</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7536.md")
</div>
