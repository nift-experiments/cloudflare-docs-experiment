<p>In order to enable automatic mitigation of <a href="/dns/dns-firewall/random-prefix-attacks/about/">random prefix attacks</a>:</p>
<ol>
<li>Set up <a href="/dns/dns-firewall/setup/">DNS Firewall</a>.</li>
<li>Enable attack mitigation on your DNS Firewall cluster.</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7737.md")
</div></div>
<p>Once you turn on attack mitigation, Cloudflare returns a <code>REFUSED</code> response to queries that are part of a random prefix attack.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7734.md")
</aside>
