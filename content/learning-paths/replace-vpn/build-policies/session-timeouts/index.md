<p>Most legacy VPNs have a global timeout setting that requires end users to log in every X hours or resets VPN profiles at a certain frequency. By doing continuous identity evaluation, a Zero Trust security model eliminates the need for most of the user-interrupting workflows triggered by session timeouts. However, there can still be valid reasons to want users to reauthenticate, either on a recurring basis or to access specific, highly-sensitive or regulated internal services.</p>
<p>To enforce Cloudflare One Client reauthentication, you can configure the Cloudflare One Client session timeouts on a per-application basis in your Gateway network policies.
When a user goes to a protected application or website, Cloudflare checks their device client session duration against the configured session timeout. If the session has expired, the user will be prompted to re-authenticate with the identity provider (IdP) used to enroll in the Cloudflare One Client.</p>
<div class="small-img">
<p><img src="/assets/upstream/images/cloudflare-one/connections/warp-reauthenticate-session.png" alt="Cloudflare One Client prompts user to re-authenticate session." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
</div>
<p>A user's device client session duration resets to zero whenever they re-authenticate with the IdP, regardless of what triggered the authentication event.</p>
<h2 id="configure-cloudflare-one-client-session-timeout">Configure Cloudflare One Client session timeout</h2>
<p>You can enforce device client session timeouts on any Gateway Network and HTTP policy that has an Allow action. If you do not specify a session timeout, the device client session will be unlimited by default.</p>
<p>Session timeouts have no impact on Gateway DNS policies. DNS policies remain active even when a user needs to re-authenticate.</p>
<p>To configure a session timeout for a Gateway policy:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9966.md")
</div></div>
<p>Session checks are now enabled for the application protected by this policy. Users can continue to reach applications outside of the policy definition.</p>
<h2 id="global-timeouts">Global timeouts</h2>
<p>To set a global reauthentication event, similar to a global timeout on a traditional VPN, we recommend setting all of your Gateway Network Allow policies to the same baseline Cloudflare One Client session duration (typically between 3-7 days). This will ensure that whenever your user tries to access any application on the private network within that window, they will be forced to reauthenticate with your identity provider when they have not logged in for your chosen number of days.</p>
<p>If a specific application requires a more stringent reauthentication timeline, users accessing that application will not have to complete the baseline reauthentication event because they are already in compliance with the baseline policy.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9963.md")
</aside>
<h3 id="common-mistake">Common mistake</h3>
<p>When configuring a global Cloudflare One Client session duration, a common mistake is to build a single policy that covers your entire private network range. An example would be an Allow policy that requires reauthentication every 7 days for all users with traffic to a destination IP in <code>10.0.0.0/8</code>. This type of global policy may result in a suboptimal user experience because an expired session blocks the user from the entire internal network (including private DNS functionality) instead of specific applications. If a user misses the one-time reauth notification, they may not know that they need to manually go into their Cloudflare One Client settings to reauthenticate.</p>
