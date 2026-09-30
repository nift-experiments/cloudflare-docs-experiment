<p>The following sections describe how to configure Cloudflare Pages with Regional Services and Customer Metadata Boundary to control where your Pages project is processed and where logs are stored.</p>
<h2 id="regional-services">Regional Services</h2>
<p>To configure Regional Services for hostnames <a href="/dns/proxy-status/">proxied</a> (meaning traffic routes through Cloudflare) through Cloudflare and ensure that processing of a Pages project occurs only in-region, follow these steps for the dashboard or API configuration:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7441.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7438.md")
</aside>
<h2 id="customer-metadata-boundary">Customer Metadata Boundary</h2>
<p>Customer Metadata Boundary applies to the Custom Domain configured, as well as the <a href="/pages/configuration/preview-deployments/">*.pages.dev</a> subdomain. You also have the option to disable access to the <a href="/pages/configuration/custom-domains/#disable-access-to-pagesdev-subdomain"><code>.dev</code> domain</a>.</p>
<p>For information on available Analytics and Metrics, review the <a href="/data-localization/compatibility/">Cloudflare product compatibility</a> page.</p>
<p>It is recommended not to store any Personally Identifiable Information (PII) in the Pages project's static assets.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7437.md")
</aside>
<p>Refer to the <a href="/pages">Pages documentation</a> for more information.</p>
