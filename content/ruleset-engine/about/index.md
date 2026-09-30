<p>The Cloudflare Ruleset Engine allows you to create and deploy rules and rulesets. The engine syntax, inspired by the Wireshark Display Filter language, is defined by the <a href="/ruleset-engine/rules-language/">Rules language</a>. Cloudflare uses the Ruleset Engine in different products, allowing you to configure several products using the same basic syntax.</p>
<p>There are several elements involved in the configuration and use of the Ruleset Engine. These elements are:</p>
<ul>
<li><a href="/ruleset-engine/about/phases/"><strong>Phase</strong></a>: Defines a stage in the life of a request where you can execute rulesets.</li>
<li><a href="/ruleset-engine/about/rulesets/"><strong>Ruleset</strong></a>: Defines a versioned set of rules. You deploy rulesets to a phase, where they execute.</li>
<li><a href="/ruleset-engine/about/rules/"><strong>Rule</strong></a>: Defines a filter and an action to perform on incoming requests that match the filter expression. A rule with an <code>execute</code> action executes a ruleset.</li>
</ul>
<hr />
<h2 id="get-started">Get started</h2>
<p>To view existing rulesets and their properties, refer to <a href="/ruleset-engine/basic-operations/view-rulesets/">View rulesets</a>.</p>
<p>For more information on deploying managed rulesets and defining overrides, refer to <a href="/ruleset-engine/managed-rulesets/">Work with managed rulesets</a>.</p>
<p>For more information on creating and deploying custom rulesets, refer to <a href="/ruleset-engine/custom-rulesets/">Work with custom rulesets</a>.</p>
