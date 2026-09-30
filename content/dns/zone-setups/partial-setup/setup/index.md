<p>A CNAME setup (also known as partial setup) allows you to use <a href="/fundamentals/concepts/how-cloudflare-works/">Cloudflare's reverse proxy</a> while maintaining your primary and authoritative DNS provider.</p>
<p>Use this option to <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7927.md")
</div> only individual subdomains through Cloudflare when you cannot change your authoritative DNS provider. You will be able to create A, AAAA, and CNAME records, which are the DNS record types that can be [proxied](/dns/proxy-status/).
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/7926.md")
</aside>
<hr />
<h2 id="before-you-begin">Before you begin</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7928.md")
</div>
<h2 id="1-convert-your-zone-and-review-dns-records"><ol>
<li>Convert your zone and review DNS records</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7932.md")
</div></div>
<h2 id="2-verify-ownership-for-your-domain"><ol start="2">
<li>Verify ownership for your domain</li>
</ol></h2>
<p>Add the <strong>Verification TXT Record</strong> at your authoritative DNS provider. Cloudflare will verify the TXT record and send a confirmation email. This can take up to a few hours.</p>
<details class="nb-details"><summary>Example verification record</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7933.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7924.md")
</aside>
<p>The verification record must remain in place for as long as your domain is active on a CNAME setup on Cloudflare.</p>
<p>If your organization has multiple Cloudflare accounts, also consider using zone holds to have more control over <a href="/dns/zone-setups/partial-setup/#domain-ownership">domain ownership</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7923.md")
</aside>
<h2 id="3-add-dns-records"><ol start="3">
<li>Add DNS records</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7935.md")
</div>
<hr />
<h2 id="other-record-types">Other record types</h2>
<p>If you are preparing a conversion from CNAME setup (partial) to primary setup (full), or if you have a more specific use case, you can use the <a href="/api/resources/dns/subresources/records/methods/create/">Create DNS Record</a> API endpoint to create DNS records of any supported type.</p>
