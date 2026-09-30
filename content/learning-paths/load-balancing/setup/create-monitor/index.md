<p>Instead of starting on your production domain, you likely should create a load balancer on a test or staging domain. This may involve temporary changes to your monitors and pools, depending on your infrastructure setup.</p>
<p>Starting with a test domain allows you to verify everything is working correctly before routing production traffic.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9809.md")
</div></div>
<details class="nb-details"><summary>Example monitor configuration</summary><div class="nb-details-body">
@input("content/.markup/bodies/9810.md")
</div></details>
