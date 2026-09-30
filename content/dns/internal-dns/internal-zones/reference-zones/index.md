<p>During an <a href="/dns/internal-dns/#architecture-overview">internal DNS query resolution</a>, if no internal record is found within a matching internal zone, Cloudflare will check if the matching internal zone is referencing another internal zone. Successive references can be followed with a maximum of five references in a chain.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7755.md")
</aside>
<h2 id="configuration-conditions">Configuration conditions</h2>
<ul>
<li>Each internal zone can only reference one other zone.</li>
<li>The same zone can be referenced by multiple internal zones.</li>
<li>Public zones cannot be used as reference zones.</li>
<li>Reference zones do not have to be linked to the same <a href="/dns/internal-dns/dns-views/">DNS view</a> as the zone referencing them. They may also not be linked to any view at all.</li>
</ul>
<h2 id="set-up">Set up</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7759.md")
</div></div>
