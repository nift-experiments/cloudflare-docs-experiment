<p>To ensure that your Cloudflare Workers code runs only within a specific geographic region, configure Regional Services on the Workers custom domain. This restricts where TLS termination (traffic decryption) and code execution occur.</p>
<h2 id="regional-services">Regional Services</h2>
<p>To configure Regional Services for hostnames <a href="/dns/proxy-status/">proxied</a> (meaning traffic routes through Cloudflare rather than directly to your origin server) through Cloudflare and ensure that processing of a Workers project occurs only in-region, follow these steps:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Workers project.</li>
<li>Follow the steps to <a href="/workers/configuration/routing/custom-domains/">create a custom domain</a>.</li>
<li>Run the <a href="/data-localization/regional-services/regional-hostnames/#configure-regional-services-via-api">API POST</a> command on the configured Workers Custom Domain to create a <code>regional_hostnames</code> with a specific region.</li>
</ol>
<h3 id="caveats">Caveats</h3>
<p>Regional Services only applies to the custom domain configured for a Workers project. Therefore, it will run only in-region Cloudflare locations.</p>
<p>Regional Services restricts where Workers are executed (where requests are processed). However, Workers code and secrets are deployed globally to all Cloudflare data centers. Regional Services does not prevent the code itself from being present outside the configured region — only its execution is regionalized.</p>
<p>Requests reaching your regionalized hostname from another zone or domain are regionalized according to your hostname's Regional Services configuration, regardless of the originating zone. Regional Services does not extend to outgoing <a href="/workers/platform/limits/#subrequests">subrequests</a> from Workers to other services — refer to <a href="/data-localization/limitations/#regional-services">Limitations</a> for details.</p>
<p>Regional Services does not apply to other Worker triggers, like <a href="/queues/">Queues</a> or <a href="/workers/configuration/cron-triggers/">Cron Triggers</a>.</p>
<h2 id="customer-metadata-boundary">Customer Metadata Boundary</h2>
<p>Customer Metadata Boundary applies to the custom domain configured, as well as the <a href="/workers/configuration/routing/workers-dev/"><code>*.workers.dev</code></a> subdomain.</p>
<p>Workers <a href="/workers/observability/metrics-and-analytics/">Metrics and Analytics</a> are not available outside the US region when using Customer Metadata Boundary.</p>
<p>With Customer Metadata Boundary set to <code>EU</code>, <strong>Workers &amp; Pages</strong> &gt; <strong>Workers</strong> &gt; <strong>Metrics</strong> tab the zone dashboard will not be populated.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7433.md")
</aside>
<p>Refer to the <a href="/workers/">Workers documentation</a> for more information.</p>
