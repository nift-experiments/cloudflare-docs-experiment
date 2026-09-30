<p>Below you will find answers to the most commonly asked questions regarding Origin Rules.</p>
<h2 id="what-happens-if-i-use-both-an-origin-rule-and-a-page-rule-to-perform-a-host-header-dns-record-override">What happens if I use both an origin rule and a page rule to perform a Host header/DNS record override?</h2>
<p>In this situation the origin rule parameters will override the <a href="/rules/page-rules/">page rule</a> parameters.</p>
<p>Consider the following example scenarios:</p>
<ul>
<li>A page rule defines a Host header override, but not a resolve override (or DNS record override). An origin rule defines a DNS record override, but not a Host header override. The resulting request will have the <code>Host</code> header defined by the page rule and the origin hostname defined by the origin rule.</li>
<li>A page rule defines a Host header override, and an origin rule also defines a Host header override. The resulting request will have the <code>Host</code> header defined by the origin rule.</li>
</ul>
<h2 id="will-cloudflare-automatically-migrate-my-page-rules-with-host-header-and-dns-record-overrides-to-origin-rules">Will Cloudflare automatically migrate my Page Rules with Host header and DNS record overrides to origin rules?</h2>
<p>Yes. Refer to the <a href="/rules/reference/page-rules-migration/">Page Rules migration guide</a> for any updates on the migration process.</p>
<h2 id="what-happens-if-more-than-one-origin-rule-matches-the-current-request">What happens if more than one origin rule matches the current request?</h2>
<p>If two or more origin rules match a request, the configuration of those rules is merged. While merging two configurations, the settings of later rules will override the settings defined in previous rules, updating or adding configuration properties. The final configuration applied by Cloudflare will be this merged version.</p>
<p>For example, if you configure the following two <a href="/rules/origin-rules/">origin rules</a> and both rules match, Cloudflare will use the destination port set by the first rule, and the DNS hostname override and <code>Host</code> header value set by the second rule.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/12963.md")
</div>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/12964.md")
</div>
<details class="nb-details"><summary>JSON example for API users</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/12965.md")
</div></details>
<p>The merged configuration to apply would be the following:</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set <code>Host</code> header</td>
<td><code>example.net</code></td>
</tr>
<tr>
<td>Set destination port</td>
<td><code>8081</code></td>
</tr>
<tr>
<td>Set DNS hostname</td>
<td><code>example.net</code></td>
</tr>
</tbody>
</table>
<p>If you also configured a destination port in rule #2, that value would override the <code>8081</code> destination port defined in rule #1.</p>
