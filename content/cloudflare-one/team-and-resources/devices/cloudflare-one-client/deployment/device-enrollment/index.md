<p>Device enrollment permissions determine which users can connect new devices to your organization's Cloudflare Zero Trust instance.</p>
<h2 id="set-device-enrollment-permissions">Set device enrollment permissions</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6155.md")
</div></div>
<p>Users can now <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">enroll their device</a> by logging in to your identity provider. To prevent users from logging out of your organization after they enroll, disable <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-device-to-leave-organization">Allow devices to leave organization</a> in your device client settings.</p>
<h2 id="example-policies">Example policies</h2>
<h3 id="check-for-service-token">Check for service token</h3>
<p>Instead of requiring users to authenticate with their credentials, you can use a <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service token</a> to enroll devices without any user interaction. Because users are not required to log in to an identity provider, identity-based policies cannot be enforced on these devices.</p>
<p>To enroll devices using a service token:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6158.md")
</div></div>
<p>When you deploy the Cloudflare One Client with your MDM provider, the Cloudflare One Client will automatically connect the device to your Zero Trust organization.</p>
<p>You can verify which devices have enrolled by going to <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong>. Devices that enrolled using a service token (or any other Service Auth policy) will have the <strong>Email</strong> field show as <code>non_identity@&lt;team-name&gt;.cloudflareaccess.com</code>.</p>
<h3 id="check-for-mtls-certificate">Check for mTLS certificate</h3>
<p>Enterprise customers can enforce <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">mutual TLS authentication</a> during device enrollment.</p>
<details class="nb-details"><summary>Certificate requirements</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6160.md")
</div></details>
<p>To check for an mTLS certificate:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6164.md")
</div></div>
<p>When users <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">log in to your Zero Trust organization</a> from the Cloudflare One Client, their device must present a valid client certificate in order to connect.</p>
