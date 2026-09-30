<p>This tutorial explains how to deploy the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> on Linux devices using a service token and an installation script. This deployment workflow is designed for headless servers - that is, servers which do not have access to a browser for identity provider logins - and for situations where you want to fully automate the onboarding process. Because devices will not register through an identity provider, <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity-based policies</a> and logging will be unavailable.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4314.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li><a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Cloudflare Zero Trust account</a></li>
<li>Root or <code>sudo</code> access on a supported Linux device</li>
<li>Zero Trust team name</li>
<li>Service token Client ID and Client Secret</li>
</ul>
<h2 id="1-create-a-service-token"><ol>
<li>Create a service token</li>
</ol></h2>
<p>Fully automated deployments rely on a service token to enroll the Cloudflare One Client in your Zero Trust organization. You can use the same token to enroll multiple devices, or generate a unique token per device if they require different <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile settings</a>.</p>
<p>To create a service token:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4320.md")
</div></div>
<h2 id="2-configure-device-enrollment-permissions"><ol start="2">
<li>Configure device enrollment permissions</li>
</ol></h2>
<p>Device enrollment permissions determine the users and devices that can register WARP with your Zero Trust organization.</p>
<p>To allow devices to enroll using a service token:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4321.md")
</div>
<p>To configure service-token enrollment with Terraform, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/#check-for-service-token">Check for a service token</a>.</p>
<h2 id="3-create-an-installation-script"><ol start="3">
<li>Create an installation script</li>
</ol></h2>
<p>You can use a shell script to automate WARP installation and registration. The following example shows how to deploy the Cloudflare One Client on Ubuntu 24.04.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4323.md")
</div>
<h2 id="4-install-warp"><ol start="4">
<li>Install WARP</li>
</ol></h2>
<p>To install the Cloudflare One Client using the example script:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4324.md")
</div>
<p>The Cloudflare One Client is now deployed with the configuration parameters stored in the root-only <code>/var/lib/cloudflare-warp/mdm.xml</code>. Assuming <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#auto_connect"><code>auto_connect</code></a> is configured, the Cloudflare One Client will automatically connect to your Zero Trust organization.</p>
<p>Verify registration and connection:</p>
<pre><code class="language-sh">sudo warp-cli --accept-tos registration show&#10;sudo warp-cli --accept-tos status&#10;</code></pre>
<p>Successful enrollment creates a device in <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> with the email <code>non_identity@&lt;team-name&gt;.cloudflareaccess.com</code>. Verify that <code>status</code> reports <code>Connected</code>. A command completion or HTTP redirect alone does not prove registration or connectivity.</p>
<p>The registration and status commands verify enrollment and the connection to Cloudflare. To verify end-to-end traffic, connect to an included destination using the protocol you intend to use. For Cloudflare Mesh, follow <a href="/mesh/guides/connect-client-devices/#2-verify-connectivity">Verify connectivity</a>.</p>
<p>If the client reports <code>Registration Missing due to: Does not exist in API</code>, or the <code>warp-svc</code> logs show an HTTP <code>400</code> enrollment response, enrollment failed. Confirm that the service token policy uses the <em>Service Auth</em> action, the policy is attached to device enrollment permissions, and the MDM team name and token values are correct. After correcting or confirming the configuration, restart the service and repeat both verification commands:</p>
<pre><code class="language-sh">sudo systemctl restart warp-svc&#10;sudo warp-cli --accept-tos registration show&#10;sudo warp-cli --accept-tos status&#10;</code></pre>
