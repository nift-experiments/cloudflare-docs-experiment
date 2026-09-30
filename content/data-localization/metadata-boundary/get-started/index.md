<p>You can configure the Customer Metadata Boundary to select the region where your logs and analytics are stored. This setting controls where Cloudflare stores traffic metadata that could identify your end users. You can configure it via API or the dashboard.</p>
<p>Currently, this can only be applied at the account-level. If you only want the Metadata Boundary to be applied on a portion of zones beneath the same account, you will have to <a href="/fundamentals/manage-domains/move-domain/">move the rest of zones to a new account</a>.</p>
<h2 id="configure-customer-metadata-boundary-in-the-dashboard">Configure Customer Metadata Boundary in the dashboard</h2>
<p>To configure Customer Metadata Boundary in the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Customer Metadata Boundary</strong>, select the region you want to use: <code>eu</code> or <code>us</code>. Selecting <code>Global</code> applies no metadata boundary — the default — meaning Customer Logs may be stored in Cloudflare's core data centers globally.</li>
</ol>
<h2 id="configure-customer-metadata-boundary-via-api">Configure Customer Metadata Boundary via API</h2>
<p>You can also configure Customer Metadata Boundary via API.</p>
<p>Currently, only SuperAdmins and Admin roles can edit DLS configurations. Use the <strong>Account-level Logs:Read/Write</strong> API permissions for the <code>/logs/control/cmb</code> endpoint to read/write Customer Metadata Boundary configurations.</p>
<p>These are some examples of API requests.</p>
<details class="nb-details"><summary>Get current regions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7429.md")
</div></details>
<details class="nb-details"><summary>Setting regions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7430.md")
</div></details>
<details class="nb-details"><summary>Delete regions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7431.md")
</div></details>
<h2 id="view-or-change-settings">View or change settings</h2>
<p>To view or change your Customer Metadata Boundary setting:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Preferences</strong>.</li>
<li>Locate the <strong>Customer Metadata Boundary</strong> section.</li>
</ol>
