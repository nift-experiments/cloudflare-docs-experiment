<p>A ruleset is an ordered set of <a href="/ruleset-engine/about/rules/">rules</a> that you can apply to traffic on the Cloudflare global network. Rulesets belong to a phase and can only execute in the same phase. To deploy a ruleset to a phase, add a rule that executes the ruleset to the <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">phase entry point ruleset</a>.</p>
<p>Rulesets are versioned. Each ruleset modification creates a new version of the ruleset. You can have several versions of a ruleset in use at the same time. When you deploy a ruleset — that is, when you create a rule that executes the ruleset — the most recent version of the ruleset is selected by default.</p>
<p>There are several types of rulesets:</p>
<ul>
<li>Phases have their entry point rulesets.</li>
<li>Cloudflare provides managed rulesets you can deploy.</li>
<li>You can create and manage your own custom rulesets.</li>
</ul>
<p>Specific Cloudflare products may provide other types of rulesets.</p>
<h2 id="entry-point-ruleset">Entry point ruleset</h2>
<p>An entry point ruleset contains a list of ordered <a href="/ruleset-engine/about/rules/">rules</a> that run in a <a href="/ruleset-engine/about/phases/">phase</a> at the account or zone level. This ruleset is an entry point for all rules executed in a phase. Some of these rules may run other rulesets.</p>
<p>Each phase has at most one entry point ruleset at the account level and at the zone level.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13289.md")
</aside>
<h2 id="managed-rulesets">Managed rulesets</h2>
<p>Managed rulesets are preconfigured rulesets provided by Cloudflare that you can deploy to a phase. Only Cloudflare can modify these rulesets.</p>
<p>The rules in a managed ruleset have a default action and status. However, you can define <strong>overrides</strong> that change these defaults.</p>
<p>There are several Cloudflare products that provide you with managed rulesets. Check each product’s documentation for details on the available managed rulesets.</p>
<p>For more information on deploying managed rulesets and defining overrides, refer to <a href="/ruleset-engine/managed-rulesets/">Work with managed rulesets</a>.</p>
<h2 id="custom-rulesets">Custom rulesets</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13288.md")
</aside>
<p>Use custom rulesets to define your own sets of rules. After creating a custom ruleset, deploy it to a phase by creating a rule that executes the ruleset.</p>
<p>For more information on creating and deploying custom rulesets, refer to <a href="/ruleset-engine/custom-rulesets/">Work with custom rulesets</a>.</p>
