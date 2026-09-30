<p>A device profile defines <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/">Cloudflare One Client settings</a> for a specific set of devices in your organization. You can create multiple profiles and apply different settings based on the user's identity, the device's location, and other criteria.</p>
<p>For example, users in one identity provider group (signifying a specific office location) might have different routes that need to be excluded from their WARP tunnel, or some device types (like Linux) might need different DNS settings to accommodate local development services.</p>
<h2 id="configure-the-default-profile">Configure the default profile</h2>
<p>Set your default device profile to be applicable to a majority of your userbase, or any user without known explicit considerations.</p>
<p>To customize the default settings:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9950.md")
</div></div>
<h2 id="optional-create-an-office-profile">(Optional) Create an office profile</h2>
<p>You can configure a device settings profile to take effect when the device is connected to a trusted network such as an office. For example, you may wish to allow users in the office to access applications directly rather than route traffic through Cloudflare.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/managed-networks/">Add a managed network</a>.</p>
