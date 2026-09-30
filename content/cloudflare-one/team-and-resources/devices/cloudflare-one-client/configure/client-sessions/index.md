<p>Client sessions control how often users must re-authenticate with your identity provider (IdP) while using the Cloudflare One Client (formerly WARP). Unlike legacy VPNs, which enforce a single global session timeout, Cloudflare One allows you to set session timeouts per application or per policy. You can configure session timeouts for your <a href="#configure-warp-sessions-in-access">Access applications</a> or as part of your <a href="#configure-warp-sessions-in-gateway">Gateway policies</a>.</p>
<p>When a user goes to a protected application or website, Cloudflare checks their device client session duration against the configured session timeout. If the session has expired, the user will be prompted to re-authenticate with the identity provider (IdP) used to enroll in the Cloudflare One Client.</p>
<div class="small-img">
<p><img src="/assets/upstream/images/cloudflare-one/connections/warp-reauthenticate-session.png" alt="Cloudflare One Client prompts user to re-authenticate session." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
</div>
<p>A user's device client session duration resets to zero whenever they re-authenticate with the IdP, regardless of what triggered the authentication event.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Ensure that traffic can reach your IdP and <code>&lt;your-team-name&gt;.cloudflareaccess.com</code> through the Cloudflare One Client.</p>
<h2 id="configure-client-sessions-in-gateway">Configure client sessions in Gateway</h2>
<p>You can enforce device client session timeouts on any Gateway Network and HTTP policy that has an Allow action. If you do not specify a session timeout, the device client session will be unlimited by default.</p>
<p>Session timeouts have no impact on Gateway DNS policies. DNS policies remain active even when a user needs to re-authenticate.</p>
<p>To configure a session timeout for a Gateway policy:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6201.md")
</div></div>
<p>Session checks are now enabled for the application protected by this policy. Users can continue to reach applications outside of the policy definition.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="enforce-a-global-timeout">Enforce a global timeout</h3>
@markup("md", "content/.markup/bodies/6198.md")
</aside>
<h2 id="configure-client-sessions-in-access">Configure client sessions in Access <span class="nb-badge">Beta</span></h2>
<p>You can allow users to log in to Access applications using their device client session. <strong>Authenticate with Cloudflare One Client</strong> is only supported for Access applications protected by Allow or Block policies.</p>
<p>To configure device client sessions for Access applications:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Access settings</strong>.</li>
<li>Enable <strong>Authenticate with Cloudflare One Client</strong>.</li>
<li>Under <strong>Session duration</strong>, choose a session timeout value of up to 90 days. This timeout will apply to all Access applications that have <strong>Authenticate with Cloudflare One Client</strong> enabled.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6197.md")
</aside>
<ol start="4">
<li>(Optional) To enable <strong>Authenticate with Cloudflare One Client</strong> by default for all existing and new applications, select <strong>Apply to all Access applications</strong>. You can override this default setting on a per-application basis when you <a href="/cloudflare-one/access-controls/applications/http-apps/">create</a> or modify an Access application.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Users can now authenticate once with the Cloudflare One Client and have access to your Access applications for the configured period of time. The session timer resets when the user re-authenticates with the IdP used to enroll in the Cloudflare One Client.</p>
<h2 id="force-user-interaction-with-idp">Force user interaction with IdP</h2>
<p>If the user has an active browser session with the IdP, the Cloudflare One Client will use the existing browser cookies to re-authenticate and the user will not be prompted to re-enter their credentials. You can override this behavior to require explicit user interaction in the IdP.</p>
<h3 id="supported-idps">Supported IdPs</h3>
<ul>
<li><a href="/cloudflare-one/integrations/identity-providers/entra-id/#force-user-interaction-during-warp-reauthentication">Microsoft Entra ID</a></li>
</ul>
<h2 id="manually-reauthenticate">Manually reauthenticate</h2>
<p>To manually refresh your Cloudflare Access session and update your group information from your identity provider (IdP), go to the following URL in your browser and fill in your <a href="/cloudflare-one/faq/getting-started-faq/#what-is-a-team-domainteam-name">team name</a>:</p>
<p><code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/refresh-identity</code></p>
<p>Reauthenticating resets your <a href="/cloudflare-one/access-controls/access-settings/session-management/">session duration</a> and fetches the latest group information from the organization's IdP.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>
<p><strong>Only one user per device</strong> — If a device is already registered with User A, User B will not be able to log in on that device through the re-authentication flow. To switch the device registration to a different user, User A must first log out from Zero Trust (if <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-device-to-leave-organization">Allow device to leave organization</a> is enabled), or an admin can revoke the registration from <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong>. User B can then properly <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">enroll</a>.</p>
</li>
<li>
<p><strong>Active connections are not terminated</strong> — Active sessions such as SSH and RDP will remain connected beyond the timeout limit.</p>
</li>
<li>
<p><strong>Binding Cookie is not supported</strong> - <strong>Authenticate with Cloudflare One Client</strong> will not work for Access applications that have the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#binding-cookie">Binding Cookie</a> enabled.</p>
</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> - Learn about the status messages displayed by the Cloudflare One Client during its connection process, and understand each stage as the client establishes a secure tunnel to Cloudflare.</li>
</ul>
