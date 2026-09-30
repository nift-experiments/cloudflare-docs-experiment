<p>Cloudflare's IDS takes advantage of the threat intelligence powered by our global network and extends the capabilities of the Cloudflare Firewall to monitor and protect your network from malicious actors.</p>
<p>You can enable IDS through the dashboard or via the API.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4268.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4271.md")
</div></div>
<h2 id="ids-rules">IDS rules</h2>
<p>IDS rules are run on a subset of packets. IDS also supports the current flows:</p>
<ul>
<li>Cloudflare WAN to Cloudflare WAN.</li>
<li>Magic Transit ingress traffic (when egress traffic is handled through direct server return).</li>
<li>Magic Transit ingress and egress traffic when Magic Transit has the <a href="/reference-architecture/architectures/magic-transit/#magic-transit-with-egress-option-enabled">Egress option enabled</a>.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<p>You must configure Logpush to log detected risks. Refer to <a href="/cloudflare-network-firewall/how-to/use-logpush-with-ids/">Configure a Logpush destination</a> for more information. Additionally, all traffic that is analyzed can be accessed via <a href="/analytics/network-analytics/">network analytics</a>. Refer to <a href="/cloudflare-network-firewall/tutorials/graphql-analytics/">GraphQL Analytics</a> to query the analytics data.</p>
