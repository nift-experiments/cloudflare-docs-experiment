<p>Users can connect to Cloudflare Zero Trust services through an agent that runs on their device. Cloudflare previously bundled that functionality into the <a href="/warp-client/">WARP Client</a>, an application that also provides privacy-focused DNS and VPN services for consumers (known as 1.1.1.1 w/ WARP). Supporting both enterprise and consumer functionality in the same application allowed us to build Zero Trust upon the same foundation used by millions of consumers across the globe, but has limited the pace at which changes could be released. As a result, we are launching a dedicated Cloudflare One Agent that replaces the Cloudflare One Client for Zero Trust deployments.</p>
<p>The Cloudflare One Agent supports all existing Zero Trust functionality. The underlying connection technology remains the same, and improvements made to performance and reliability based on feedback from 1.1.1.1 w/ WARP users will continue to be built into the Cloudflare One Agent.</p>
<h2 id="macos-windows-and-linux">macOS, Windows, and Linux</h2>
<p>No action is required for desktop clients at this time. The existing Cloudflare One Client will continue to support both Zero Trust and 1.1.1.1 functionality.</p>
<h2 id="ios-and-android">iOS and Android</h2>
<p>Zero Trust users must migrate from the 1.1.1.1 app to the Cloudflare One Agent app. Cloudflare is no longer supporting customers using the 1.1.1.1 app for Zero Trust features.</p>
<p>Organizations can migrate their teams with minimal disruption in one of two modes: <a href="#migrate-manual-deployments">manually</a> or via a <a href="#migrate-managed-deployments">managed endpoint solution</a>.</p>
<h3 id="migrate-manual-deployments">Migrate manual deployments</h3>
<p>If you downloaded and installed the 1.1.1.1 app manually, here are the recommended migration steps:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6117.md")
</div></div>
<p>The 1.1.1.1 app will automatically log you out of Cloudflare Zero Trust and revert to consumer mode. Selecting <strong>Login to Cloudflare Zero Trust</strong> in 1.1.1.1 opens an onboarding screen where you can choose the Cloudflare One Agent app and log in to your Zero Trust organization.</p>
<h4 id="what-to-do-with-the-old-app">What to do with the old app</h4>
<p>While both 1.1.1.1 and Cloudflare One Agent can exist on the device, iOS and Android will only allow one of these applications to connect at a time.</p>
<p>To access your company's resources, you must use the Cloudflare One Agent app.</p>
<p>You can use the 1.1.1.1 app for personal browsing. When connected to 1.1.1.1 w/ WARP, your traffic will be encrypted and privately routed via Cloudflare's network, and your employer will not be able to see any of your browsing activity. To learn more about consumer WARP services, refer to <a href="/warp-client/">WARP client</a>.</p>
<p>If you do not wish to use the old 1.1.1.1 app for personal browsing, you may <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/uninstall/#ios-and-android">uninstall</a> it.</p>
<h3 id="migrate-managed-deployments">Migrate managed deployments</h3>
<p>If you deployed the 1.1.1.1 app with an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/">MDM provider</a>, perform the migration as follows:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6120.md")
</div></div>
<p>Once users have enrolled, the migration process is complete. The 1.1.1.1 app will revert to <a href="#what-to-do-with-the-old-app">consumer mode</a> and ignore the existing MDM configuration profile. If you do not wish to keep the 1.1.1.1 app, you may uninstall it and delete its MDM configuration.</p>
<h3 id="verify-migration">Verify migration</h3>
<p>To check whether a user has migrated, go to <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong>. A device enrolled through the Cloudflare One Agent will appear as a new device with a new device ID. Their old 1.1.1.1 registration will remain as an inactive device.</p>
