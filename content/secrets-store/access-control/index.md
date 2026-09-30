<p>Secrets Store allows security administrators to have more control by implementing role-based access. For details about roles at Cloudflare, refer to <a href="/fundamentals/manage-members/">Fundamentals</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/382.md")
</aside>
<p>Access to a secret is controlled by two independent checks that must both pass:</p>
<ol>
<li><strong>Authorization</strong> — the caller must have permission to perform the action. The permission comes from either a <a href="#relevant-roles">user role</a> (when the dashboard authenticates the request) or an <a href="#api-token-permissions">API token permission</a> (when the request is made with an API token). A given request is evaluated against one or the other, not both.</li>
<li><strong>Secret scope</strong> — the <a href="#secret-scopes">scope list</a> on the secret must include the consuming service.</li>
</ol>
<p>For example, deploying a Worker that binds a secret requires a role or API token that can bind secrets, and a secret whose scope includes <code>workers</code>.</p>
<h2 id="relevant-roles">Relevant roles</h2>
<p>Refer to the list below for default role definitions.</p>
<h4 id="super-administrator">Super Administrator</h4>
<ul>
<li>Can create, edit, duplicate, delete, and view secrets metadata.</li>
<li>Can <a href="/secrets-store/integrations/workers/">add a Secrets Store binding to a Worker</a>.</li>
<li>Can <a href="/ai-gateway/configuration/bring-your-own-keys/">create an association between a secret and an AI gateway</a>.</li>
</ul>
<h4 id="secrets-store-admin">Secrets Store Admin</h4>
<ul>
<li>Can create, edit, duplicate, delete, and view secrets metadata.</li>
</ul>
<h4 id="secrets-store-deployer">Secrets Store Deployer</h4>
<ul>
<li>Can view secrets metadata but cannot create, edit, duplicate, nor delete secrets.</li>
<li>Can <a href="/secrets-store/integrations/workers/">add a Secrets Store binding to a Worker</a>.</li>
<li>Can <a href="/ai-gateway/configuration/bring-your-own-keys/">create an association between a secret and an AI gateway</a>.</li>
</ul>
<h4 id="secrets-store-reporter">Secrets Store Reporter</h4>
<ul>
<li>Can view secrets metadata.</li>
<li>Cannot perform any actions (create, edit, duplicate, delete secrets), nor use Secrets Store integrations with other Cloudflare products.</li>
</ul>
<h2 id="api-token-permissions">API token permissions</h2>
<p><a href="/fundamentals/api/get-started/create-token/">API tokens</a> have two Secrets Store permission levels: <strong>Read</strong> and <strong>Edit</strong>. The permission you need depends on what the token is doing, not on whether you intend to modify the secret itself.</p>
<ul>
<li><strong>Account Secrets Store Read</strong>: Allows the caller to view metadata for secrets (for example, listing secrets or fetching the name, ID, scopes, and comments of a secret). This permission does not grant access to the value of a secret, and does not allow binding a secret to another resource.</li>
<li><strong>Account Secrets Store Edit</strong>: Allows the caller to create, edit, duplicate, or delete secrets. <strong>Edit is also required to bind a secret to another Cloudflare resource</strong>, such as adding a Secrets Store binding to a Worker or associating a secret with an AI Gateway. Attaching a secret to a resource is treated as a write against the secret.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deploying-workers-from-ci-cd">Deploying Workers from CI/CD</h3>
@markup("md", "content/.markup/bodies/381.md")
</aside>
<h2 id="secret-scopes">Secret scopes</h2>
<p>Each secret has a list of <strong>scopes</strong> that determine which Cloudflare services are allowed to consume it. Scopes are set when a secret is created, and can be updated later by editing the secret.</p>
<p>The currently supported scopes are:</p>
<ul>
<li><code>workers</code> — allows the secret to be <a href="/secrets-store/integrations/workers/">bound to a Worker</a>.</li>
<li><code>ai-gateway</code> — allows the secret to be <a href="/ai-gateway/configuration/bring-your-own-keys/">associated with an AI Gateway</a>.</li>
</ul>
<p>A request to bind or associate a secret with a service will be rejected if that service is not in the scope list, even if the caller has the correct role or API token permission. Deploying a Worker with a Secrets Store binding therefore requires both:</p>
<ul>
<li>A user role or API token that can bind secrets (Super Administrator or Secrets Store Deployer role, or <strong>Account Secrets Store Edit</strong> API token permission).</li>
<li>A scope list on the secret that includes <code>workers</code>.</li>
</ul>
<p>You can set scopes when <a href="/secrets-store/manage-secrets/">creating a secret</a> using the dashboard, the API (<code>scopes</code> field), or Wrangler (<code>--scopes</code> flag).</p>
