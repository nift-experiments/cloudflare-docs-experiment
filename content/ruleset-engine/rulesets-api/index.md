<p>The Rulesets API provides an interface for managing and configuring the execution of rulesets, supporting different Cloudflare products powered by the Ruleset Engine.</p>
<h2 id="get-started">Get started</h2>
<p>To get started, review the <a href="/ruleset-engine/rulesets-api/json-object/">JSON objects</a> and the available <a href="/ruleset-engine/rulesets-api/endpoints/">endpoints</a>.</p>
<hr />
<h2 id="limits">Limits</h2>
<p>You should avoid making concurrent updates to the same ruleset. There are rate limits in place to prevent the same ruleset from being concurrently updated too many times. The exact limits depend on the size of the ruleset and volume of requests, and can be different for each ruleset.</p>
<p>The rate limits are most frequently hit when concurrently modifying several rules in the same ruleset. To avoid this, you should <a href="/ruleset-engine/rulesets-api/update/">update the entire ruleset in a single operation</a> instead.</p>
