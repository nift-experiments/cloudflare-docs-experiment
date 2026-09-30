<p>The following sections describe how to configure R2 Object Storage with Regional Services and Customer Metadata Boundary to control where object requests are processed and where logs are stored.</p>
<h2 id="regional-services">Regional Services</h2>
<p>To configure Regional Services for hostnames <a href="/dns/proxy-status/">proxied</a> (meaning traffic routes through Cloudflare) through Cloudflare and ensure that processing of requests to an <a href="/r2/buckets/">R2 Bucket</a> occurs only in-region, follow these steps:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Follow the steps to <a href="/r2/buckets/create-buckets/">create a Bucket</a>.</li>
<li><a href="/r2/buckets/public-buckets/#connect-a-bucket-to-a-custom-domain">Connect a bucket to a custom domain</a>.</li>
<li>Run the <a href="/data-localization/regional-services/regional-hostnames/#configure-regional-services-via-api">API POST</a> command on the configured bucket custom domain to create a <code>regional_hostnames</code> with a specific region.</li>
</ol>
<p>Regional Services only applies to the custom domain configured for an R2 Bucket.</p>
<h3 id="send-logs-to-r2-via-s3-compatible-endpoint">Send logs to R2 via S3-Compatible endpoint</h3>
<p>The following instructions will show you how to set up a Logpush job using an S3-compatible endpoint to store logs in an R2 bucket in the jurisdiction of your choice.</p>
<ol>
<li>
<p>Create an <a href="/r2/get-started/">R2 bucket</a> in your Cloudflare account and select the <a href="/r2/reference/data-location/#set-jurisdiction-via-the-cloudflare-dashboard">jurisdiction</a> you would like to use.</p>
</li>
<li>
<p>Generate an API token for your R2 bucket. You have the following two options:</p>
</li>
</ol>
<details class="nb-details"><summary>Generate a token for a specific bucket (recommended)</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7435.md")
</div></details>
<details class="nb-details"><summary>Generate a token for all buckets</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7436.md")
</div></details>
<ol start="3">
<li>Set up a Logpush destination using <a href="/logs/logpush/logpush-job/enable-destinations/s3-compatible-endpoints/">S3-compatible endpoint</a> and fill in the following fields:</li>
</ol>
<ul>
<li><strong>Bucket</strong>: Enter the name of the R2 bucket you created with the jurisdiction you would like to use.</li>
<li><strong>Path</strong> (optional): If you want, you can specify a folder path to organize your logs.</li>
<li><strong>Endpoint URL</strong>: Provide the S3 API endpoint for your bucket in the format <code>&lt;account-id&gt;.eu.r2.cloudflarestorage.com</code>. Do not include the bucket name, as it was set in the first field.</li>
<li><strong>Bucket Region</strong>: For instance, use <code>WEUR</code> to specify the EU region.</li>
<li><strong>Access Key ID</strong>: Enter the Token ID created previously (<code>325xxxxcd</code>).</li>
<li><strong>Secret Access Key</strong>: Use the SHA-256 hash of the token (<code>dxxxx391b</code>).</li>
</ul>
<p>Complete the configuration by selecting the fields you want to push to your R2 bucket.</p>
<h2 id="customer-metadata-boundary">Customer Metadata Boundary</h2>
<p>With Customer Metadata Boundary set to <code>EU</code>, <strong>R2</strong> &gt; <strong>Bucket</strong> &gt; <a href="/r2/platform/metrics-analytics/"><strong>Metrics</strong></a> tab in the account dashboard will be populated.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7434.md")
</aside>
<p>Refer to the <a href="/r2/">R2 documentation</a> for more information.</p>
