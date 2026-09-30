<p>A phase defines a stage in the life of a request where you can execute <a href="/ruleset-engine/about/rulesets/">rulesets</a>. Phases are defined by Cloudflare and cannot be modified.</p>
<p>Phases exist at two levels:</p>
<ul>
<li>At the <a href="/fundamentals/concepts/accounts-and-zones/#accounts">account</a> level</li>
<li>At the <a href="/fundamentals/concepts/accounts-and-zones/#zones">zone</a> level</li>
</ul>
<p>For the same phase, rules defined at the account level are evaluated before the rules defined at the zone level.</p>
<p>Each phase has at most one <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">entry point ruleset</a> at the account and zone level.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13292.md")
</aside>
<p>The following diagram outlines the request handling process where requests go through the available phases:</p>
<p><img src="/assets/upstream/images/ruleset-engine/rulesets-phases.png" alt="Diagram showing the request handling process. The user request goes through several request phases until it eventually reaches the origin server (the request can also be blocked). The origin returns a response, which goes through several response phases until it reaches the user." /></p>
<p>Cloudflare products are specific to one or more phases, and they add support for different features. Check the documentation for each Cloudflare product for details on the applicable phases.</p>
<p>Refer to <a href="/ruleset-engine/reference/phases-list/">Phases list</a> for a list of phases and their corresponding Cloudflare products.</p>
