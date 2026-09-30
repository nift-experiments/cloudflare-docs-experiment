<p>Custom rules allow you to control incoming traffic by filtering requests to a zone. They work as customized web application firewall (WAF) rules that you can use to perform actions like <em>Block</em> or <em>Managed Challenge</em> on incoming requests. You can also use the <em>Skip</em> action in a custom rule to <a href="/waf/custom-rules/skip/">skip one or more Cloudflare security features</a>.</p>
<p>In the <a href="/security/">new security dashboard</a>, custom rules are one of the available types of <a href="/security/rules/">security rules</a>. Security rules perform security-related actions on incoming requests that match specified filters.</p>
<p>Like other rules evaluated by Cloudflare's <a href="/ruleset-engine/">Ruleset Engine</a>, custom rules have the following basic parameters:</p>
<ul>
<li>An <a href="/ruleset-engine/rules-language/expressions/">expression</a> that specifies the criteria you are matching traffic on using the <a href="/ruleset-engine/rules-language/">Rules language</a>.</li>
<li>An <a href="/ruleset-engine/rules-language/actions/">action</a> that specifies what to perform when there is a match for the rule.</li>
</ul>
<p>The <a href="/waf/custom-rules/">custom rules documentation</a> includes examples for common use cases.</p>
<h2 id="skip-rules">Skip rules</h2>
<p>You can skip one or more Cloudflare security features using a custom rule <a href="/waf/custom-rules/skip/">configured with the <em>Skip</em> action</a>. These rules are also known as skip rules. Refer to <a href="/waf/custom-rules/skip/options/">Skip options</a> for more information on the features you can skip.</p>
