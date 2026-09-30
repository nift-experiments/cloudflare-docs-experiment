<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6324.md")
</div></details>
<p>With Cloudflare Zero Trust, you can use an on-premise Active Directory (or similar) server to validate a remote user's Windows login credentials. Before the user enters their Windows login information for the first time, the Cloudflare One Client (formerly WARP) establishes a connection using a service token. This initial connection is not associated with a user identity. Once the user completes the Windows login, the Cloudflare One Client switches to an identity-based session and applies the user registration to all future logins.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Active Directory resources are <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">connected to Cloudflare</a>.</li>
</ul>
<h2 id="1-create-a-service-token"><ol>
<li>Create a service token</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6330.md")
</div></div>
<h2 id="2-create-a-device-enrollment-policy"><ol start="2">
<li>Create a device enrollment policy</li>
</ol></h2>
<p>In your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/#set-device-enrollment-permissions">device enrollment permissions</a>, create the following policy:</p>
<table>
<thead>
<tr>
<th>Rule Action</th>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Service Auth</td>
<td>Include</td>
<td>Service Token</td>
<td><code>&lt;TOKEN-NAME&gt;</code></td>
</tr>
</tbody>
</table>
<h2 id="2-optional-restrict-access-during-pre-login"><ol start="2">
<li>(Optional) Restrict access during pre-login</li>
</ol></h2>
<p>Devices enrolled via a service token are identified by the email address <code>non_identity@&lt;team-name&gt;.cloudflareaccess.com</code>. Using this email address, you can apply specific <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile settings</a> and <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a> during the pre-login state. For example, you could provide access to only those resources necessary to complete the Windows login and/or device management activities.</p>
<details class="nb-details"><summary>Example device profile rule</summary><div class="nb-details-body">
@input("content/.markup/bodies/6331.md")
</div></details>
<details class="nb-details"><summary>Example Gateway network policy</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6332.md")
</div></details>
<h2 id="3-configure-the-mdm-file"><ol start="3">
<li>Configure the MDM file</li>
</ol></h2>
<p>To enable the Windows pre-login feature, an MDM file in the following format must be <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/#windows">deployed</a> on the device. In the following example, the <code>pre_login</code> key allows the device to connect using the service token, while <code>configs</code> contains your default Zero Trust configuration.</p>
<pre><code class="language-xml">&lt;dict&gt;&#10;  &lt;key&gt;pre_login&lt;/key&gt;&#10;  &lt;dict&gt;&#10;    &lt;key&gt;organization&lt;/key&gt;&#10;    &lt;string&gt;mycompany&lt;/string&gt;&#10;    &lt;key&gt;auth_client_id&lt;/key&gt;&#10;    &lt;string&gt;TOKEN-ID&lt;/string&gt;&#10;    &lt;key&gt;auth_client_secret&lt;/key&gt;&#10;    &lt;string&gt;TOKEN-SECRET&lt;/string&gt;&#10;  &lt;/dict&gt;&#10;  &lt;key&gt;configs&lt;/key&gt;&#10;  &lt;array&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;organization&lt;/key&gt;&#10;      &lt;string&gt;mycompany&lt;/string&gt;&#10;      &lt;key&gt;display_name&lt;/key&gt;&#10;      &lt;string&gt;Default&lt;/string&gt;&#10;    &lt;/dict&gt;&#10;  &lt;/array&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<p>The Cloudflare One Client will apply the pre-login configuration when no other Cloudflare One Client registration exists and the user has not yet logged into Windows. When the pre-login configuration is in effect, the device will appear on <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> with the email <code>non_identity@&lt;team-name&gt;.cloudflareaccess.com</code>.</p>
<p>After the user logs into Windows, the Cloudflare One Client will automatically switch to the default MDM configuration and prompt the user to authenticate with the IdP. Once authenticated, the Cloudflare One Client registers and connects with the user identity. The <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> page will now show a new device associated with the user's email.</p>
<p>If <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/">multi-user mode</a> is turned off, this user registration will be used for any subsequent connections, including before the next Windows user login. Deleting the user registration would cause the Cloudflare One Client to switch back to the pre-login configuration as soon as the user logs out of Windows.</p>
<p>To learn how the pre-login configuration works with <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/">multi-user mode</a>, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/#cloudflare-one-client-registration-logic">Cloudflare One Client registration flowchart</a>.</p>
