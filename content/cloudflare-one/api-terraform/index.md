<p>You can manage your Cloudflare Zero Trust configuration using the API or Terraform. For more information, refer to the following links:</p>
<ul>
<li><a href="/api/">API reference</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider reference</a></li>
<li><a href="/terraform/">Terraform how-to documentation</a></li>
</ul>
<p>Detailed API and Terraform examples for Cloudflare Zero Trust are available in our <a href="/cloudflare-one/implementation-guides/">implementation guides</a> and throughout the Cloudflare Zero Trust documentation.</p>
<h2 id="set-dashboard-to-read-only">Set dashboard to read-only</h2>
<p>Super Administrators can lock all settings as read-only in the Cloudflare One dashboard. Read-only mode ensures that all updates for the account are made through the API or Terraform.</p>
<p>To enable read-only mode:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Settings</strong> &gt; <strong>Admin controls</strong>.</li>
<li>Enable <strong>Set dashboard to read-only</strong>.</li>
</ol>
<p>All users, regardless of <a href="/cloudflare-one/roles-permissions/">user permissions</a>, will be prevented from making configuration changes through the UI.</p>
<h2 id="scoped-api-tokens">Scoped API tokens</h2>
<p>The administrators managing policies and groups in Cloudflare Zero Trust might be different from those responsible for configuring WAF custom rules or other Cloudflare settings. You can configure scoped API tokens so that team members and automated systems can manage Cloudflare Zero Trust settings without having permission to modify other configurations in Cloudflare.</p>
<p>You can create a scoped API token <a href="/fundamentals/api/get-started/create-token/">via the dashboard</a> or <a href="/fundamentals/api/how-to/create-via-api/">via the API</a>. For a list of available token permissions, refer to <a href="/fundamentals/api/reference/permissions/">API token permissions</a>.</p>
