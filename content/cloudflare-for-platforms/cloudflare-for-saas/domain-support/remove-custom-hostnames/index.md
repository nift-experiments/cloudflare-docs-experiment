<p>As a SaaS provider, your customers may decide to no longer participate in your service offering. If that happens, you need to stop routing traffic through those custom hostnames.</p>
<h2 id="domains-using-cloudflare">Domains using Cloudflare</h2>
<p>If your customer's domain is also using Cloudflare, they can stop routing their traffic through your custom hostname by updating their Cloudflare DNS.</p>
<p>If they update their <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#3-have-customer-create-cname-record"><code>CNAME</code> record</a> so that it no longer points to your <code>CNAME</code> target:</p>
<ul>
<li>The domain's traffic will not route through your custom hostname.</li>
<li>The custom hostname will enter into a <strong>Moved</strong> state.</li>
</ul>
<p>If the custom hostname is in a <strong>Moved</strong> state for seven days, it will transition into a <strong>Deleted</strong> state.</p>
<p>You should remove a customer's custom hostname from your zone if they decide to churn. This is especially important if your end customers are using Cloudflare because if the churned customer changes the DNS target to point away from your SaaS zone but you have not removed it, the custom hostname will continue to route to your service. This is a result of the <a href="/ssl/reference/certificate-and-hostname-priority/#hostname-priority">custom hostname priority logic</a>.</p>
<h2 id="domains-not-using-cloudflare">Domains not using Cloudflare</h2>
<p>If your customer's domain is not using Cloudflare, you must remove a customer's custom hostname from your zone if they decide to churn.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4098.md")
</div></div>
<h2 id="for-end-customers">For end customers</h2>
<p>If your SaaS domain is also a <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/">domain using Cloudflare</a>, you can use your Cloudflare DNS to remove your domain from your SaaS provider.</p>
<p>This means that - if you <a href="/dns/manage-dns-records/how-to/create-dns-records/#delete-dns-records">remove the DNS records</a> pointing to your SaaS provider - Cloudflare will stop routing domain traffic through your SaaS provider and the associated custom hostname will enter a <strong>Moved</strong> state.</p>
<p>This also means that you need to keep DNS records pointing to your SaaS provider for as long as you are a customer. Otherwise, you could accidentally remove your domain from their services.</p>
