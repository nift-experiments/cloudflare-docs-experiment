<p>Prioritized traffic allows you to define which applications Cloudflare One Appliance (formerly Magic WAN Connector) should process first. Applications not in the list will be queued behind prioritized traffic.</p>
<p>Similarly to breakout traffic, prioritized traffic also works via DNS requests inspection.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5796.md")
</aside>
<h2 id="add-an-application-to-your-account">Add an application to your account</h2>
<p>Before you can add or remove Prioritized traffic applications to your Cloudflare One Appliance, you need to create an account-level list with the applications that you want to configure. Currently, adding to or modifying this list is only possible via API, through the <a href="/api/resources/magic_transit/subresources/apps/methods/create/"><code>managed_app_id</code></a> endpoint.</p>
<p>To add applications to your account:</p>
<p>Send a <code>POST</code> request to add new apps to your account.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/apps \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;managed_app_id&quot;: &quot;&lt;APP_ID&gt;&quot;,&#10;  &quot;name&quot;: &quot;&lt;APP_NAME&gt;&quot;,&#10;  &quot;type&quot;: &quot;&lt;APP_TYPE&gt;&quot;&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;account_app_id&quot;: &quot;eb09v665c0784618a3e4ba9809258fd4&quot;,&#10;		&quot;name&quot;: &quot;&lt;APP_NAME&gt;&quot;,&#10;		&quot;type&quot;: &quot;&lt;APP_TYPE&gt;&quot;,&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>You can now add this new app to the Prioritized traffic list in your Cloudflare One Appliance.</p>
<h3 id="add-an-application-to-cloudflare-one-appliance">Add an application to Cloudflare One Appliance</h3>
<p>You need to configure Prioritized traffic applications for each of your existing sites, as this is a per-site configuration.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5799.md")
</div></div>
<h3 id="delete-an-application-from-cloudflare-one-appliance">Delete an application from Cloudflare One Appliance</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5802.md")
</div></div>
