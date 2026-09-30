<p>Refer to the sections below to learn about common actions you might want to take when managing your data in Secrets Store.</p>
<p>You must have a <a href="/secrets-store/access-control/">Super Administrator or Secrets Store Admin role</a> within your Cloudflare account.</p>
<h2 id="manage-via-wrangler">Manage via Wrangler</h2>
<p><a href="/workers/wrangler/">Wrangler</a> is a command-line interface (CLI) that allows you to manage <a href="/workers/">Cloudflare Workers</a> projects. Refer to <a href="/workers/wrangler/commands/secrets-store/#secrets-store-secret">Wrangler commands</a> for guidance on how to use it with Secrets Store.</p>
<h2 id="create-a-secret">Create a secret</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13788.md")
</div></div>
<h2 id="duplicate-a-secret">Duplicate a secret</h2>
<p>Duplicate a secret to keep the same secret value but change name, scope, or comments.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13791.md")
</div></div>
<h2 id="edit-a-secret">Edit a secret</h2>
<p>Edit a secret to replace an existing value with a new one.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13783.md")
</aside>
<p>You can also edit the secret <strong>Permission scope</strong> and <strong>Comment</strong>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13794.md")
</div></div>
<h2 id="delete-a-secret">Delete a secret</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13782.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13797.md")
</div></div>
