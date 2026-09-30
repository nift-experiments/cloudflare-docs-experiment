<p>Each customer or team that uses Cloudflare should have their own account. This ensures proper security and access of resources. Each account acts as a container of zones and other resources. Depending on your needs, you may even provision multiple accounts for a single customer or team.</p>
<p>When you create an account with the Tenant API, your Cloudflare user owns that account from creation, ongoing management, and finally deletion.</p>
<h2 id="create-account">Create account</h2>
<p>Each customer or team that uses Cloudflare should have their own account. This ensures proper security and access of resources. Each account acts as a container of zones and other resources. Depending on your needs, you may even provision multiple accounts for a single customer or team.</p>
<p>When you create an account with the Tenant API, your Cloudflare user owns that account from creation, ongoing management, and finally deletion.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14748.md")
</div></div>
<h2 id="view-accounts">View accounts</h2>
<p>When you create an account with the Tenant API, your Cloudflare user owns that account from creation, ongoing management, and finally deletion.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14751.md")
</div></div>
<h2 id="update-account">Update account</h2>
<p>To update an account, send a <a href="/api/resources/accounts/methods/update/"><code>PUT</code></a> request to the <code>/accounts/{account_id}</code> endpoint.</p>
<h2 id="delete-account">Delete account</h2>
<p>To delete an account you have created, send a <code>DELETE</code> request to the <code>/accounts/{account_id}</code> endpoint.</p>
<p>Account deletion is permanent and will delete any zones or other resources under the account.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="some-resources-require-manual-deletion">Some resources require manual deletion</h3>
@markup("md", "content/.markup/bodies/14745.md")
</aside>
<pre><code class="language-bash">curl --request DELETE \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id} \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<p>A successful request will return the id to confirm the operation:</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;1b16db169c9cb7853009857198fae1b9&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
