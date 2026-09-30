<p>Cloudflare Access can use Cloudflare itself as an identity provider, allowing you to build Access policies that match on Cloudflare account membership. This is useful for scenarios where you want to restrict access to users who are members of a specific Cloudflare account, without requiring a third-party identity provider.</p>
<p>When a user authenticates through the Cloudflare identity provider, Access verifies their Cloudflare account membership and grants or denies access based on your policy configuration.</p>
<p>For newly created Zero Trust organizations, Cloudflare adds this identity provider automatically as the default login method, with <strong>Restrict to account members</strong> enabled. You do not need to set it up manually. The following steps describe how to add or reconfigure it.</p>
<h2 id="set-up-cloudflare-as-an-identity-provider">Set up Cloudflare as an identity provider</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5085.md")
</div></div>
<h2 id="configuration-options">Configuration options</h2>
<table>
<thead>
<tr>
<th>Option</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Restrict to account members</strong></td>
<td>When enabled, only users who are members of your Cloudflare account can authenticate. When disabled, any Cloudflare user can authenticate (subject to your Access policies).</td>
<td>Disabled</td>
</tr>
</tbody>
</table>
<p>The <strong>Default</strong> column reflects the value when you add this identity provider manually. When Cloudflare configures it automatically for a new organization, <strong>Restrict to account members</strong> is enabled.</p>
<h2 id="use-cloudflare-account-membership-in-policies">Use Cloudflare account membership in policies</h2>
<p>After configuring Cloudflare as an identity provider, you can use the <strong>Cloudflare Account Member</strong> selector in your <a href="/cloudflare-one/access-controls/policies/">Access policies</a>. This selector matches users based on their membership in a Cloudflare account.</p>
<ul>
<li>If you omit the account ID, the selector matches members of the current account (the account where the Access policy is configured).</li>
<li>If you specify an account ID, the selector matches members of that specific account.</li>
</ul>
<p>This is useful for cross-account access scenarios where you need to grant access to users from a different Cloudflare account.</p>
