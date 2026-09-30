<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7709.md")
</aside>
<h2 id="for-your-zone-apex">For your zone apex</h2>
<p>CNAME flattening occurs by default for all plans when your domain uses a CNAME record for its zone apex (<code>example.com</code>, meaning the record <strong>Name</strong> is set to <code>@</code>).</p>
<h2 id="for-all-cname-records">For all CNAME records</h2>
<p>For zones on paid plans, you can choose to flatten all CNAME records. This option is useful for <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7710.md")
</div> CNAME records. [Proxied records](/dns/proxy-status/) are flattened by default as they return Cloudflare anycast IPs.
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7713.md")
</div></div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7708.md")
</aside>
<h2 id="per-record">Per record</h2>
<p>Paid zones also have the option of flattening specific CNAME records.</p>
<p>If you use this option, a special <a href="/dns/manage-dns-records/reference/record-attributes/">tag</a> <code>cf-flatten-cname</code> will be added to the respective flattened CNAME records in your zone file, allowing you to <a href="/dns/manage-dns-records/how-to/import-and-export/">export and import records</a> without losing this configuration.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7716.md")
</div></div>
