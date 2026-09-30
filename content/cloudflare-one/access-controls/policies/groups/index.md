<p>A rule group is a collection of Access rules that can be configured once and then quickly applied across many Access policies. Rule groups use the same <a href="/cloudflare-one/access-controls/policies/#rule-types">rule types</a> and <a href="/cloudflare-one/access-controls/policies/#selectors">selectors</a> shown in the Access policy builder.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4589.md")
</aside>
<h2 id="create-a-rule-group">Create a rule group</h2>
<p>To create an Access rule group:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4592.md")
</div></div>
<p>You can now add this group to an Access policy using the <em>Rule groups</em> selector.</p>
<h2 id="use-cases">Use cases</h2>
<h3 id="ip-based-rules">IP-based rules</h3>
<p>We recommend using rule groups to define any IP address-based rules you configure in policies. Keeping IP addresses in one place allows you to modify or remove addresses once, rather than in each policy, and reduces the potential for mistakes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4588.md")
</aside>
<h3 id="country-requirements">Country requirements</h3>
<p>You can create a rule group that consists of countries to allow or block. Access will treat the countries in the Include rule with an OR logical operator. When building policies for an Access application, you can assign this rule group to a Require policy to require at least one of the countries inside of the group. For an example policy, refer to <a href="/cloudflare-one/access-controls/policies/#require-rules-with-or-operators">Require rules with OR operators</a>.</p>
