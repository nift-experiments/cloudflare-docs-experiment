<p>The following sections describe how to configure Load Balancing with Regional Services and Customer Metadata Boundary to control where load balancing decisions and traffic processing occur.</p>
<h2 id="regional-services">Regional Services</h2>
<p>You can load balance traffic at different levels of the networking stack depending on the <a href="/load-balancing/understand-basics/proxy-modes/">proxy mode</a>: Layer 7 (<code>HTTP/S</code>) and Layer 4 (<code>TCP</code>) are supported; however, <code>DNS-only</code> is not supported, as it is not <a href="/dns/proxy-status/">proxied</a>.</p>
<p>To configure Regional Services for hostnames <a href="/dns/proxy-status/">proxied</a> (meaning traffic routes through Cloudflare) through Cloudflare and ensure that the Load Balancer is available only in-region, follow these steps for the dashboard or API configuration:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7444.md")
</div></div>
<h2 id="customer-metadata-boundary">Customer Metadata Boundary</h2>
<p><a href="/load-balancing/reference/load-balancing-analytics/">Load Balancing Analytics</a> are not available outside the US region when using Customer Metadata Boundary.</p>
<p>With Customer Metadata Boundary set to <code>EU</code>, <strong>Traffic</strong> &gt; <strong>Load Balancing Analytics</strong> &gt; <strong>Overview and Latency</strong> tab in the zone dashboard will not be populated.</p>
<p>Refer to the <a href="/load-balancing/">Load Balancing documentation</a> for more information.</p>
