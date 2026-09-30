<p>Device enrollment permissions determine which users can connect new devices to your organization's Cloudflare Zero Trust instance. Once the user registers their device, the Cloudflare One Client will store their identity token and use it to authenticate to services in your private network.</p>
<h2 id="set-device-enrollment-permissions">Set device enrollment permissions</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9955.md")
</div></div>
<h2 id="only-allow-corporate-devices">Only allow corporate devices</h2>
<p>Device posture evaluation happens after a device has already enrolled in your Zero Trust organization. If you want only specific devices to be able to enroll, we recommend adding a <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">mutual TLS authentication</a> rule to your device enrollment policy. This rule will check for the presence of a specific client certificate on the enrolling devices.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9951.md")
</aside>
<details class="nb-details"><summary>Certificate requirements</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9957.md")
</div></details>
<p>To check for an mTLS certificate:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9961.md")
</div></div>
<h2 id="best-practices">Best practices</h2>
<p>Most businesses use a single identity provider as the source of truth for their user directory. You should use this source of truth to onboard your corporate users to Zero Trust, for example by requiring company email addresses to login with your primary identity provider. Later on, you can add other login methods or identity providers as necessary for any contractors, vendors, or acquired corporations who may need access to your network.</p>
