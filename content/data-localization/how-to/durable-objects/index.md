<p>The following sections describe how to configure Durable Objects with Regional Services and Customer Metadata Boundary to control where your Durable Objects run, persist data, and where logs are stored.</p>
<h2 id="regional-services">Regional Services</h2>
<p>To configure Regional Services for hostnames <a href="/dns/proxy-status/">proxied</a> (meaning traffic routes through Cloudflare) through Cloudflare and ensure that processing of a Durable Object (DO) occurs only in-region, follow these steps:</p>
<ol>
<li>Follow the steps in the Durable Objects <a href="/durable-objects/get-started/">Get Started</a> guide.</li>
<li><a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">Restrict Durable Objects to a jurisdiction</a>, in order to control where the DO itself runs and persists data, by creating a jurisidictional subnamespace in your Worker’s code.</li>
<li>Follow the <a href="/data-localization/how-to/workers/#regional-services">Workers guide</a> to configure a custom domain with Regional Services, in order to control the regions from which Cloudflare responds to requests.</li>
</ol>
<h2 id="customer-metadata-boundary">Customer Metadata Boundary</h2>
<p>DO Logs and Analytics are not available outside the US region when using Customer Metadata Boundary. With Customer Metadata Boundary set to <code>EU</code>, <strong>Workers &amp; Pages</strong> &gt; <strong>Workers</strong> &gt; <strong>Metrics</strong> tab related to DO in the zone dashboard will not be populated.</p>
<p>Refer to the <a href="/durable-objects/">Durable Objects documentation</a> for more information.</p>
