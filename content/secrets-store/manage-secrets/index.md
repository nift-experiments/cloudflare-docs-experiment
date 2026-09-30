<p>Secrets can be API tokens, public/private keys, authorization keys, passwords, or even code variables. The only limitation is that a secret must be a string that does not exceed 1024 bytes.</p>
<p>Once a secret is added to the Secrets Store, it can no longer be decrypted or accessed via API or on the dashboard. Only the service associated with a given secret will be able to access it.</p>
<h2 id="limits">Limits</h2>
<p>Customers who create a secrets store in the open beta can have up to 100 secrets per account. Also, there can only be one store per account.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="production-secrets">Production secrets</h3>
@markup("md", "content/.markup/bodies/13781.md")
</aside>
<h2 id="resources">Resources</h2>
<ul>
<li><a href="/workers/wrangler/commands/secrets-store/#secrets-store-secret">Manage via Wrangler</a></li>
<li><a href="/secrets-store/manage-secrets/how-to/#create-a-secret">Create a secret</a></li>
<li><a href="/secrets-store/manage-secrets/how-to/#duplicate-a-secret">Duplicate a secret</a></li>
<li><a href="/secrets-store/manage-secrets/how-to/#edit-a-secret">Edit a secret</a></li>
<li><a href="/secrets-store/manage-secrets/how-to/#delete-a-secret">Delete a secret</a></li>
</ul>
