<p>Cloudflare Access allows you to require Access protection for all hostnames in your account. When this setting is turned on, traffic to any hostname without a matching <a href="/cloudflare-one/access-controls/applications/">Access application</a> is automatically blocked.</p>
<p>This deny-by-default approach prevents accidental exposure of internal resources to the public Internet. Without this setting, a developer could deploy a new application or create a DNS record and inadvertently expose the resource before configuring an Access application.</p>
<h2 id="turn-on-access-protection">Turn on Access protection</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4739.md")
</aside>
<ol>
<li>
<p>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Access settings</strong>.</p>
</li>
<li>
<p>Turn on <strong>Block traffic to all domains in this account</strong>. You will see a dialog confirming you understand the scope of this change. Select <strong>Confirm</strong>.</p>
<p>Traffic to all hostnames in the account is now blocked unless an Access application exists for the hostname.</p>
</li>
<li>
<p>(Optional) Under <strong>Hostnames to Exempt</strong>, select specific domains to exempt from the <strong>Block traffic to all domains in this account</strong> setting. Traffic to exempted hostnames is allowed even if no Access application exists.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4738.md")
</aside>
<h2 id="allow-traffic-to-a-hostname">Allow traffic to a hostname</h2>
<p>To allow traffic to a hostname when <strong>Block traffic to all domains in this account</strong> is turned on:</p>
<ol>
<li><a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Create an Access application</a> for the hostname.</li>
<li>Add an <a href="/cloudflare-one/access-controls/policies/#allow">Allow policy</a> to grant access to authorized users.</li>
<li>(Optional) Add a <a href="/cloudflare-one/access-controls/policies/#bypass">Bypass policy</a> if the hostname should be publicly accessible without authentication.</li>
</ol>
<h2 id="blocked-request-behavior">Blocked request behavior</h2>
<p>When a user attempts to access a hostname without an Access application, Cloudflare displays a block page with <code>Error 1050: This resource is blocked by this account's Default-Deny policy.</code> The user cannot proceed until an administrator creates an Access application for that hostname.</p>
