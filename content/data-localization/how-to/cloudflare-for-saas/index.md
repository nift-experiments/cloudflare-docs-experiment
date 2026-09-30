<p>The following sections describe how to configure Cloudflare for SaaS with Regional Services and Customer Metadata Boundary to control where your custom hostnames are processed and where logs are stored.</p>
<h2 id="regional-services">Regional Services</h2>
<p>To configure Regional Services for both hostnames <a href="/dns/proxy-status/">proxied</a> (meaning traffic routes through Cloudflare) through Cloudflare and the fallback origin, follow these steps for the dashboard or API configuration:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7448.md")
</div></div>
<p>The Regional Services functionality can be extended to Custom Hostnames and this is dependent on the target of the alias.</p>
<p>Consider the following example.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7445.md")
</aside>
<p>Below you can find a breakdown of the different ways that you might configure Cloudflare for SaaS and the corresponding processing regions:</p>
<ul>
<li>No processing region: <code>fallback.saasprovider.com</code></li>
<li>Processing region is the <code>US</code>: <code>us.saasprovider.com</code></li>
<li>User location: <code>UK</code> (closest datacenter: <code>LHR</code>)</li>
</ul>
<table>
<thead>
<tr>
<th>Test</th>
<th>Custom Hostname</th>
<th>Target</th>
<th>Origin</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>​​<code>regionalservices-default.example.com</code></td>
<td><code>fallback.saasprovider.com</code></td>
<td>default (fallback)</td>
<td><code>LHR</code></td>
</tr>
<tr>
<td>2</td>
<td><code>regionalservices-default2.example.com</code></td>
<td><code>us.saasprovider.com</code></td>
<td>default (fallback)</td>
<td><code>EWR</code></td>
</tr>
<tr>
<td>3</td>
<td><code>regionalservices-custom.example.com</code></td>
<td><code>fallback.saasprovider.com</code></td>
<td><code>us.saasprovider.com</code> (custom)</td>
<td><code>LHR</code></td>
</tr>
<tr>
<td>4</td>
<td><code>regionalservices-custom2.example.com</code></td>
<td><code>us.saasprovider.com</code></td>
<td><code>us.saasprovider.com</code> (custom)</td>
<td><code>EWR</code></td>
</tr>
</tbody>
</table>
<ul>
<li>
<p>In order to set a processing region for the fallback record to any of the available regions for Regional Services, create a new regional hostname entry for the fallback via a <a href="/data-localization/regional-services/regional-hostnames/#configure-regional-services-via-api">POST</a> request.</p>
</li>
<li>
<p>To update the existing region (for example, from <code>EU</code> to <code>US</code>), make a <a href="/data-localization/regional-services/regional-hostnames/#configure-regional-services-via-api">PATCH</a> request for the fallback to update the processing region accordingly.</p>
</li>
<li>
<p>To remove the regional services processing region and set it back to <code>Earth</code>, make a <a href="/data-localization/regional-services/regional-hostnames/#configure-regional-services-via-api">DELETE</a> request to delete the region configuration.</p>
</li>
</ul>
<h2 id="customer-metadata-boundary">Customer Metadata Boundary</h2>
<p>Cloudflare for SaaS <a href="/cloudflare-for-platforms/cloudflare-for-saas/hostname-analytics/">Analytics</a> based on <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP requests</a> are fully supported by Customer Metadata Boundary.</p>
<p>Refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS documentation</a> for more information.</p>
