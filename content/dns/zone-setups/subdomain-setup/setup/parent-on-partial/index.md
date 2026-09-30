<p>When the parent zone is using a <a href="/dns/zone-setups/partial-setup/">CNAME setup (partial)</a><sup><a href="#footnote-2">2</a></sup>, the steps to set up your child zone depend on whether the subdomain already exists in the parent domain.</p>
<h2 id="subdomain-does-not-exist">Subdomain does not exist</h2>
<p>If you have not yet created a DNS record covering your subdomain in the parent zone:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8014.md")
</div></div>
<h2 id="subdomain-already-exists">Subdomain already exists</h2>
<p>If you have already created a DNS record covering your subdomain in the parent zone:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8019.md")
</div></div>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-2">Meaning that another DNS provider - not Cloudflare - maintains your Authoritative DNS.</li></ol></section>
