<p>Prioritized traffic allows you to define which applications Cloudflare One Appliance (formerly Magic WAN Connector) should process first. Applications not in the list will be queued behind prioritized traffic.</p>
<p>Similarly to breakout traffic, prioritized traffic also works via DNS requests inspection.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7036.md")
</aside>
<h2 id="add-an-application-to-your-account">Add an application to your account</h2>
<p>Before you can add or remove Prioritized traffic applications to your Cloudflare One Appliance, you need an account-level list with the applications that you want to configure. This list contains two kinds of applications:</p>
<ul>
<li><strong>Cloudflare-managed applications</strong> — Cloudflare's built-in catalog of recognized applications. These already exist in your account and do not need to be created. Select them directly when assigning application traffic.</li>
<li><strong>Custom applications</strong> — applications you define by <strong>hostname</strong>, <strong>IP subnet</strong>, and/or <strong>source subnet</strong>. You can create, edit, and delete custom applications directly from the dashboard or through the <a href="/api/resources/magic_transit/subresources/apps/methods/create/">Create an account app</a> endpoint.</li>
</ul>
<h3 id="create-edit-or-delete-a-custom-application">Create, edit, or delete a custom application</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7039.md")
</div></div>
<h3 id="add-an-application-to-cloudflare-one-appliance">Add an application to Cloudflare One Appliance</h3>
<p>You need to configure Prioritized traffic applications for each of your existing sites, as this is a per-site configuration.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7042.md")
</div></div>
<p>Custom applications defined with <strong>Source subnets</strong> can also be marked as prioritized this way. Refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source">Breakout by source</a> for the full set of source-based match criteria.</p>
<h3 id="delete-an-application-from-cloudflare-one-appliance">Delete an application from Cloudflare One Appliance</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7045.md")
</div></div>
