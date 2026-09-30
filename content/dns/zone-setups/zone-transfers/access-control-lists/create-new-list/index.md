<p>You need to create an Access Control List (ACL) if Cloudflare is your <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">secondary DNS provider</a>. The ACL will specify additional NOTIFY IPs that Cloudflare should listen to.</p>
<p>An ACL is configured at the account level, which means that it will apply to every primary and secondary zone in your account.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8082.md")
</div></div>
