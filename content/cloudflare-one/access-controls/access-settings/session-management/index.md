<p>A user session determines how long a user can access an Access application without re-authenticating.</p>
<h2 id="session-durations">Session durations</h2>
<p>When a user logs in to an application protected by Access, Access validates their identity against your Access policies and generates two signed JSON Web Tokens (JWTs):</p>
<table>
<thead>
<tr>
<th>Token</th>
<th>Description</th>
<th>Expiration</th>
<th>Storage</th>
</tr>
</thead>
<tbody>
<tr>
<td>Global session token</td>
<td>Stores the user's identity from the IdP and provides single sign-on (SSO) functionality for all Access applications.</td>
<td><a href="#global-session-duration">Global session duration</a></td>
<td>Your Cloudflare <span class="nb-interactive-component" data-cf-component="GlossaryTooltip"></td>
</tr>
</tbody>
</table>
@markup("md", "content/.markup/bodies/4737.md")
</div> |
| [Application token](/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/) | Allows the user to access a specific Access application.                                                             | [Policy session duration](#policy-session-duration), which defaults to the [application session duration](#application-session-duration) | The hostname protected by the Access application                                  |
<p>The user can access the application for the entire duration of the application token's lifecycle. When the application token expires, Cloudflare will automatically issue a new application token if the global token is still valid (and the user's identity still passes your Access policies). If the global token has also expired, the user will be prompted to re-authenticate with the IdP.</p>
<p>The global token expiration is usually set to equal or exceed the application token expiration. Setting a longer global token provides a more secure way to allow for longer user sessions, since the global token cannot be used to directly access an application.</p>
<p>In summary, Access checks sessions from most specific to least specific:</p>
<ol>
<li><strong><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">Client session</a></strong> (if enabled) — Overrides all other durations. The user re-authenticates when this expires.</li>
<li><strong><a href="#policy-session-duration">Policy session</a></strong> — Controls access to a specific application for users matching a specific policy.</li>
<li><strong><a href="#application-session-duration">Application session</a></strong> — The default policy session duration for all policies in the application.</li>
<li><strong><a href="#global-session-duration">Global session</a></strong> — Controls how often the user must log in to the IdP across all applications.</li>
</ol>
<p>Refer to the <a href="#order-of-enforcement">Order of enforcement</a> flowchart for a visual representation.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4736.md")
</aside>
<h3 id="global-session-duration">Global session duration</h3>
<p>The global session duration determines how often Cloudflare Access prompts the user to log in to their identity provider. You can set a global session duration between 15 minutes and one month. The default value is 24 hours.</p>
<p>To set the global session duration:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Access settings</strong>.</li>
<li>Under <strong>Set your global session duration</strong>, select <strong>Edit</strong>,</li>
<li>Select the desired timeout duration from the dropdown menu.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>The user will be required to re-authenticate with the IdP after this period of time.</p>
<h3 id="policy-session-duration">Policy session duration</h3>
<p>The policy session duration determines how long the user can access a self-hosted Access application. When the user's session expires, Access rechecks their stored user identity against the application's Access policies.</p>
<p>By default, the policy session duration is equal to the <a href="#application-session-duration">application session duration</a>. To configure more granular permissions for specific users, you can change the policy session duration to a value ranging from immediate timeout to one month. For example, you may wish to set the application session duration to seven days for engineers, but set a policy session duration to 24 hours for contractors.</p>
<p>To set the policy session duration:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Policies</strong>.</li>
<li>Choose a policy and select <strong>Configure</strong>.</li>
<li>Select a <strong>Session Duration</strong> from the dropdown menu.</li>
<li>Save the policy.</li>
</ol>
<p>Users who match this policy will be issued an application token with this expiration time.</p>
<h3 id="application-session-duration">Application session duration</h3>
<p>The application session duration is the default <a href="#policy-session-duration">policy session duration</a> for all policies in an Access application. Available session durations range from immediate timeout to one month. The default value is 24 hours.</p>
<p>To set the application session duration:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Choose an application and select <strong>Configure</strong>.</li>
<li>Select a <strong>Session Duration</strong> from the dropdown menu.</li>
<li>Save the application.</li>
</ol>
<p>Users who match a policy configured with a <em>Same as application session timeout</em> duration will be issued an application token with this expiration time.</p>
<h4 id="saas-applications">SaaS applications</h4>
<p>Application session durations only control the front door to a SaaS app; Access does not control how long the user can stay in the SaaS app itself. For example, if the user logs out of the SaaS app and then comes back to it, a valid Access application token allows them to re-authenticate without another login. The SaaS app issues its own authorization cookie that manages the user's session within the app.</p>
<h4 id="ssh-rdp-and-vnc">SSH, RDP, and VNC</h4>
<p>Cloudflare does not control the length of an active SSH, VNC, or RDP session. <a href="/cloudflare-one/access-controls/access-settings/session-management/">Application session durations</a> determine the window in which a user can initiate a new connection or refresh an existing one.</p>
<h3 id="cloudflare-one-client-session-duration">Cloudflare One Client session duration</h3>
<p>When <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/#configure-client-sessions-in-access">Authenticate with Cloudflare One Client</a> is enabled for an Access application, the Cloudflare One Client session duration takes precedence over all other session durations (application, policy, and global). As long as the Cloudflare One Client session is valid and the user is running the Cloudflare One Client, the user will not be prompted to re-authenticate with the IdP — even if the global session has expired.</p>
<h4 id="return-401-responses-for-non-browser-traffic">Return 401 responses for non-browser traffic</h4>
<p>By default, failed Cloudflare One Client authentication requests return a <code>302</code> redirect to the Access login page. API clients, command-line tools, and automation often cannot complete this browser login flow. You can return a <code>401 Unauthorized</code> response for non-browser traffic instead so that these clients can detect the authentication failure directly.</p>
<p>To enable this behavior:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Access settings</strong>.</li>
<li>Under <strong>Cloudflare One Client authentication</strong>, ensure that <strong>Enable authentication using the Cloudflare One Client session</strong> is turned on.</li>
<li>Turn on <strong>Return 401 response for non-browser traffic</strong>.</li>
</ol>
<p>You can also set <code>warp_auth_non_browser_401</code> to <code>true</code> using the <a href="/api/resources/zero_trust/subresources/organizations/methods/update/">Update your Zero Trust organization</a> API.</p>
<p>This account setting only applies to failed Cloudflare One Client authentication. It is separate from <code>service_auth_401_redirect</code>, which controls Service Auth behavior for an individual Access application.</p>
<h3 id="mfa-session-duration">MFA session duration</h3>
<p>If you use <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">independent multi-factor authentication (MFA)</a>, the MFA session duration determines how long a user can log in to Cloudflare Access without being prompted for MFA. The MFA session is independent of the global, policy, and application session durations. When logging in to an Access app with <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#configure-independent-mfa-for-an-application">MFA enabled</a>, users must complete an MFA challenge if their last MFA authentication falls outside the configured session duration. After authenticating with their identity provider, users are prompted for MFA. The <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#cf_device"><code>CF_Device</code> cookie</a> ensures both authentication steps occur on the same device. MFA session durations do not affect how long a user has access to the application (that is controlled by the <a href="#session-durations">application token</a>).</p>
<h3 id="order-of-enforcement">Order of enforcement</h3>
<p>The following flowchart illustrates how Access enforces user sessions for a self-hosted application.</p>
<table>
<thead>
<tr>
<th>Flowchart setting</th>
<th>Dashboard location</th>
</tr>
</thead>
<tbody>
<tr>
<td>Authenticate with Cloudflare One Client</td>
<td><strong>Access controls</strong> &gt; <strong>Applications</strong> &gt; select an application &gt; <strong>Configure</strong> &gt; <strong>Authentication</strong> &gt; <strong>Authenticate with Cloudflare One Client</strong></td>
</tr>
<tr>
<td>Cloudflare One Client session duration</td>
<td><strong>Access controls</strong> &gt; <strong>Access settings</strong> &gt; <strong>Cloudflare One Client authentication</strong> &gt; <strong>Session duration</strong></td>
</tr>
<tr>
<td>Policy session duration</td>
<td><strong>Access controls</strong> &gt; <strong>Policies</strong> &gt; select a policy &gt; <strong>Configure</strong> &gt; <strong>Session duration</strong></td>
</tr>
<tr>
<td>Application session duration</td>
<td><strong>Access controls</strong> &gt; <strong>Applications</strong> &gt; select an application &gt; <strong>Configure</strong> &gt; <strong>Overview</strong> &gt; <strong>Session Duration</strong></td>
</tr>
<tr>
<td>Global session duration</td>
<td><strong>Access controls</strong> &gt; <strong>Access settings</strong> &gt; <strong>Set your global session duration</strong></td>
</tr>
</tbody>
</table>
<pre><code class="language-mermaid">flowchart TB&#10;    %% Accessibility&#10;    accTitle: Access session durations&#10;    accDescr: Flowchart describing the order of enforcement for Access sessions&#10;&#10;    %% In with user traffic&#10;    start[&quot;User goes to Access application&quot;]&#10;    start--&quot;Enabled for this application&quot; --&gt;warpsession[Cloudflare One Client session expired?]&#10;    start-- &quot;Disabled for this application&quot; --&gt; policysession[Policy session expired?]&#10;&#10;		warpsession--&quot;Yes&quot;--&gt;idp[Prompt to log in to IdP]&#10;		warpsession--&quot;No&quot;--&gt;accessgranted[Access granted]&#10;&#10;		policysession--&quot;Yes&quot;--&gt;globalsession[Global session expired?]&#10;		policysession--&quot;No&quot;--&gt;accessgranted&#10;&#10;		globalsession--&quot;Yes&quot;--&gt;idp&#10;		globalsession--&quot;No&quot;--&gt;refreshtoken[Check identity against Access policies]&#10;		refreshtoken--&gt;accessgranted&#10;		idp--&gt;refreshtoken&#10;&#10;</code></pre>
<h2 id="revoke-user-sessions">Revoke user sessions</h2>
<p>Access provides two options for revoking user sessions: per-application and per-user.</p>
<h3 id="per-application">Per-Application</h3>
<p>To immediately terminate all active sessions for a specific application:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Locate the application for which you would like to revoke active sessions and select <strong>Configure</strong>.</li>
<li>Select <strong>Revoke existing tokens</strong>.</li>
</ol>
<p>Unless there are changes to rules in the policy, users can start a new session if their profile in your identity provider is still active.</p>
<h3 id="per-user">Per-User</h3>
<p>Access can immediately revoke a single user session across all applications in your account. However, if the user's identity profile is still active, they can generate a new session.</p>
<p>If you want to permanently revoke a user's access:</p>
<ol>
<li>Disable their account in your identity provider so that they cannot authenticate.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Users</strong>.</li>
<li>Select the checkbox next to the user you want to revoke.</li>
<li>Select <strong>Action</strong> &gt; <strong>Revoke</strong>.</li>
</ol>
<p>The user will no longer be able to log in to any application protected by Access. The user will still count towards your seat subscription until you <a href="/cloudflare-one/team-and-resources/users/seat-management">remove the user</a> from your account.</p>
<h3 id="subsequent-logins">Subsequent Logins</h3>
<p>When administrators revoke a user's Cloudflare Access token, that user will not be able to log in again for up to 1 minute. If they attempt to do so, Cloudflare Access will display an error.</p>
<h2 id="log-out-as-a-user">Log out as a user</h2>
<p>To log out of Access, the end user can visit either of the following URLs:</p>
<ul>
<li><code>&lt;your-application-domain&gt;/cdn-cgi/access/logout</code></li>
<li><code>&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/logout</code></li>
</ul>
<p>This action <a href="#per-user">revokes the user's session</a> across all applications. Access will immediately clear the authorization cookie from the user's browser, and all previously issued tokens will stop being accepted in 20-30 seconds. The only difference between these two URLs is which domain the authorization cookie is deleted from. For example, going to <code>&lt;your-application-domain&gt;/cdn-cgi/access/logout</code> will remove the application cookie and make the logout action feel more instantaneous.</p>
<p>You can use these URLs to create custom logout buttons or links directly within your application.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4735.md")
</aside>
<h2 id="ajax">AJAX</h2>
<p>Pages that rely heavily on AJAX or single-page applications can block sub-requests due to an expired Access token without prompting the user to re-authenticate.</p>
<p>You can configure Access to provide a <code>401</code> response on sub-requests with an expired session token. We recommend using this response code to either force a page refresh or to display a message to the user that their session has expired.</p>
<p>In order to receive a <code>401</code> for an expired session, add the following header to all AJAX requests:</p>
<p><code>X-Requested-With: XMLHttpRequest</code></p>
