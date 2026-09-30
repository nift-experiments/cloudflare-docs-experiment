<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8811.md")
</aside>
<p>Organizations allows you to create security policies in one account and share them across other accounts in your Organization. This ensures consistent security posture across all accounts without manually duplicating configurations.</p>
<p>Policy sharing works the same way for both <a href="/fundamentals/organizations/for-enterprise/">Enterprise</a> and <a href="/fundamentals/organizations/for-mssp-distributors/">MSSP/Distributor</a> Organizations.</p>
<p>In addition to WAF and Gateway policies, Organizations supports <a href="/cloudflare-one/integrations/identity-providers/idp-federation/">IdP federation</a>, which lets you configure a single identity provider (such as Okta or Entra ID) in one account and share it across all accounts in your Organization. Shared IdP connections are read-only in recipient accounts and are automatically provisioned or removed as accounts join or leave the Organization.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Policy sharing requires the appropriate product entitlements on the accounts involved. Organizations does not grant access to WAF or Gateway features — your accounts must already have the required SKUs.</p>
<ul>
<li><strong>WAF policy sharing</strong> requires Enterprise WAF entitlements on both the source and destination accounts.</li>
<li><strong>Gateway policy sharing</strong> requires Zero Trust Gateway entitlements on both the source and destination accounts.</li>
</ul>
<h2 id="waf-policy-sharing">WAF policy sharing</h2>
<p>Create WAF custom rulesets in one account and share them to other accounts within your Organization.</p>
<h3 id="how-it-works">How it works</h3>
<ol>
<li>Create a WAF custom ruleset in a <strong>source account</strong> — this is the account where you author and manage the rules.</li>
<li>Share the ruleset to one or more <strong>destination accounts</strong> within your Organization.</li>
<li>The shared ruleset appears in the destination accounts as a <strong>read-only</strong> policy.</li>
<li>Changes made to the ruleset in the source account automatically propagate to all destination accounts.</li>
</ol>
<h3 id="key-behaviors">Key behaviors</h3>
<ul>
<li><strong>Read-only in destination accounts</strong>: Shared WAF policies cannot be edited in the receiving accounts. To modify the rules, update them in the source account.</li>
<li><strong>Source account owns the policy</strong>: If the source account is removed from the Organization, the shared policy is removed from all destination accounts.</li>
<li><strong>No cross-Organization sharing</strong>: Policies can only be shared within a single Organization. You cannot share policies between different Organizations.</li>
<li><strong>Multiple rulesets</strong>: You can share multiple WAF custom rulesets from the same or different source accounts.</li>
</ul>
<h3 id="share-a-waf-custom-ruleset">Share a WAF custom ruleset</h3>
<ol>
<li>In the source account, go to <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Custom rules</strong>.</li>
<li>Create or select a custom ruleset.</li>
<li>From the ruleset action menu, select <strong>Share</strong>.</li>
<li>In the sharing dialog, select one or more destination accounts.</li>
<li>Select <strong>Share</strong>.</li>
</ol>
<p>The shared ruleset now appears in the destination accounts under their WAF custom rules.</p>
<h2 id="gateway-policy-sharing">Gateway policy sharing</h2>
<p>Share Zero Trust Gateway policies across accounts in your Organization. Gateway policy sharing supports the following policy types:</p>
<ul>
<li><strong>DNS policies</strong> — Filter and block DNS queries.</li>
<li><strong>Network policies</strong> — Control network-level traffic.</li>
<li><strong>HTTP policies</strong> — Inspect and filter HTTP traffic.</li>
<li><strong>Resolver policies</strong> — Customize DNS resolution behavior.</li>
</ul>
<h3 id="how-it-works-1">How it works</h3>
<ol>
<li>Create a Gateway policy in a <strong>source account</strong>.</li>
<li>Share the policy to one or more <strong>destination accounts</strong> within your Organization.</li>
<li>The shared policy appears in the destination accounts as a <strong>read-only</strong> policy.</li>
<li>Changes made to the policy in the source account automatically propagate to all destination accounts.</li>
</ol>
<h3 id="key-behaviors-1">Key behaviors</h3>
<ul>
<li><strong>Read-only in destination accounts</strong>: Shared Gateway policies cannot be edited in the receiving accounts. To modify the policy, update it in the source account.</li>
<li><strong>Source account owns the policy</strong>: If the source account is removed from the Organization, the shared policy is removed from all destination accounts.</li>
<li><strong>All Gateway policy types supported</strong>: DNS, Network, HTTP, and Resolver policies can all be shared.</li>
<li><strong>Zero Trust seat requirements</strong>: Destination accounts must have their own Zero Trust seats and Gateway entitlements.</li>
</ul>
<h2 id="manage-shared-policies">Manage shared policies</h2>
<h3 id="view-shared-policies">View shared policies</h3>
<p>From the Organization overview, you can see which policies are shared and to which accounts. Shared policies are marked with a sharing indicator in the destination account's policy list.</p>
<h3 id="remove-a-shared-policy">Remove a shared policy</h3>
<p>To stop sharing a policy with a destination account:</p>
<ol>
<li>In the source account, go to the shared policy.</li>
<li>Select <strong>Manage sharing</strong>.</li>
<li>Remove the destination account from the sharing list.</li>
</ol>
<p>The policy is immediately removed from the destination account.</p>
<h3 id="best-practices">Best practices</h3>
<ul>
<li><strong>Centralize policy authoring</strong>: Designate one or two accounts as your policy source accounts. This simplifies management and ensures consistency.</li>
<li><strong>Use descriptive names</strong>: Name shared policies clearly (for example, &quot;Org-Wide OWASP Rules&quot; or &quot;Global DNS Block List&quot;) so destination account admins understand what the policy does.</li>
<li><strong>Test before sharing</strong>: Validate policies in the source account before sharing to all destination accounts to avoid unintended blocks or rule conflicts.</li>
<li><strong>Monitor shared policy coverage</strong>: Regularly review which accounts have shared policies applied to ensure no accounts are missing critical security rules.</li>
</ul>
