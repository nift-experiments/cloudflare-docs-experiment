<p>Public Bucket is a feature that allows users to expose the contents of their R2 buckets directly to the Internet. By default, buckets are never publicly accessible and will always require explicit user permission to enable.</p>
<p>Public buckets can be set up in either of two ways:</p>
<ul>
<li>Expose your bucket as a custom domain under your control.</li>
<li>Expose your bucket using a Cloudflare-managed <code>https://r2.dev</code> subdomain for non-production use cases.</li>
</ul>
<p>These options can be used independently. Enabling custom domains does not require enabling <code>r2.dev</code> access.</p>
<p>To use features like <a href="/waf/custom-rules/">WAF custom rules</a>, caching, access controls, or <a href="/bots/get-started/bot-management/">Bot Management</a>, you must configure your bucket behind a custom domain. These capabilities are not available when using the <code>r2.dev</code> development url.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11482.md")
</aside>
<h2 id="custom-domains">Custom domains</h2>
<h3 id="caching">Caching</h3>
<p>Domain access through a custom domain allows you to use <a href="/cache/">Cloudflare Cache</a> to accelerate access to your R2 bucket.</p>
<p>Configure your cache to use <a href="/cache/how-to/tiered-cache/#smart-tiered-cache">Smart Tiered Cache</a> to have a single upper-tier data center next to your R2 bucket.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11481.md")
</aside>
<h3 id="access-control">Access control</h3>
<p>To restrict access to your custom domain's bucket, use Cloudflare's existing security products.</p>
<ul>
<li><a href="/cloudflare-one/access-controls/">Cloudflare Zero Trust Access</a>: Protects buckets that should only be accessible by your teammates. Refer to <a href="/r2/tutorials/cloudflare-access/">Protect an R2 Bucket with Cloudflare Access</a> tutorial for more information.</li>
<li><a href="/waf/custom-rules/use-cases/configure-token-authentication/">Cloudflare WAF Token Authentication</a>: Restricts access to documents, files, and media to selected users by providing them with an access token.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11480.md")
</aside>
<h3 id="minimum-tls-version-cipher-suites">Minimum TLS Version &amp; Cipher Suites</h3>
<p>To customise the minimum TLS version or cipher suites of a custom hostname of an R2 bucket, you can issue an API call to edit <a href="/api/resources/r2/subresources/buckets/subresources/domains/subresources/custom/methods/update/">R2 custom domain settings</a>. You will need to add the optional <code>minTLS</code> and <code>ciphers</code> parameters to the request body. For a list of the cipher suites you can specify, refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/">Supported cipher suites</a>.</p>
<h2 id="add-your-domain-to-cloudflare">Add your domain to Cloudflare</h2>
<p>The domain being used must have been added as a <a href="/fundamentals/concepts/accounts-and-zones/#zones">zone</a> in the same account as the R2 bucket.</p>
<ul>
<li>If your domain is already managed by Cloudflare, you can proceed to <a href="/r2/buckets/public-buckets/#connect-a-bucket-to-a-custom-domain">Connect a bucket to a custom domain</a>.</li>
<li>If your domain is not managed by Cloudflare, you need to set it up using a <a href="/dns/zone-setups/partial-setup/">partial (CNAME) setup</a> to add it to your account.</li>
</ul>
<p>Once the domain exists in your Cloudflare account (regardless of setup type), you can link it to your bucket.</p>
<h2 id="connect-a-bucket-to-a-custom-domain">Connect a bucket to a custom domain</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your bucket.
3. Select **Settings**.
4. Under **Custom Domains**, select **Add**.
5. Enter the domain name you want to connect to and select **Continue**.
6. Review the new record that will be added to the DNS table and select **Connect Domain**.
<p>Your domain is now connected. The status takes a few minutes to change from <strong>Initializing</strong> to <strong>Active</strong>, and you may need to refresh to review the status update. If the status has not changed, select the <em>...</em> next to your bucket and select <strong>Retry connection</strong>.</p>
<p>To view the added DNS record, select <strong>...</strong> next to the connected domain and select <strong>Manage DNS</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11479.md")
</aside>
<h2 id="disable-domain-access">Disable domain access</h2>
<p>Disabling a domain will turn off public access to your bucket through that domain. Access through other domains or the managed <code>r2.dev</code> subdomain are unaffected.
The specified domain will also remain connected to R2 until you remove it or delete the bucket.</p>
<p>To disable a domain:</p>
<ol>
<li>In <strong>R2</strong>, select the bucket you want to modify.</li>
<li>On the bucket page, Select <strong>Settings</strong>, go to <strong>Custom Domains</strong>.</li>
<li>Next to the domain you want to disable, select <strong>...</strong> and <strong>Disable domain</strong>.</li>
<li>The badge under <strong>Access to Bucket</strong> will update to <strong>Not allowed</strong>.</li>
</ol>
<h2 id="remove-domain">Remove domain</h2>
<p>Removing a custom domain will disconnect it from your bucket and delete its configuration from the dashboard. Your bucket will remain publicly accessible through any other enabled access method, but the domain will no longer appear in the connected domains list.</p>
<p>To remove a domain:</p>
<ol>
<li>In <strong>R2</strong>, select the bucket you want to modify.</li>
<li>On the bucket page, Select <strong>Settings</strong>, go to <strong>Custom Domains</strong>.</li>
<li>Next to the domain you want to disable, select <strong>...</strong> and <strong>Remove domain</strong>.</li>
<li>Select <strong>Remove domain</strong> in the confirmation window. This step also removes the CNAME record pointing to the domain. You can always add the domain again.</li>
</ol>
<h2 id="public-development-url">Public development URL</h2>
<p>Expose the contents of this R2 bucket to the internet through a Cloudflare-managed r2.dev subdomain. This endpoint is intended for non-production traffic.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11478.md")
</aside>
<h3 id="enable-public-development-url">Enable public development URL</h3>
<p>When you enable public development URL access for your bucket, its contents become available on the internet through a Cloudflare-managed <code>r2.dev</code> subdomain.</p>
<p>To enable access through <code>r2.dev</code> for your buckets:</p>
<ol>
<li>In <strong>R2</strong>, select the bucket you want to modify.</li>
<li>On the bucket page, select <strong>Settings</strong>.</li>
<li>Under <strong>Public Development URL</strong>, select <strong>Enable</strong>.</li>
<li>In <strong>Allow Public Access?</strong>, confirm your choice by typing <code>allow</code> to confirm and select <strong>Allow</strong>.</li>
<li>You can now access the bucket and its objects using the Public Bucket URL.</li>
</ol>
<p>To verify that your bucket is publicly accessible, check that <strong>Public URL Access</strong> shows <strong>Allowed</strong> in you bucket settings.</p>
<h3 id="disable-public-development-url">Disable public development URL</h3>
<p>Disabling public development URL access removes your bucket's exposure through the <code>r2.dev</code> subdomain. The bucket and its objects will no longer be accessible via the Public Bucket URL.</p>
<p>If you have connected other domains, the bucket will remain accessible for those domains.</p>
<p>To disable public access for your bucket:</p>
<ol>
<li>In <strong>R2</strong>, select the bucket you want to modify.</li>
<li>On the bucket page, select <strong>Settings</strong>.</li>
<li>Under <strong>Public Development URL</strong>, select <strong>Disable</strong>.</li>
<li>In <strong>Disallow Public Access?</strong>, type <code>disallow</code> to confirm and select <strong>Disallow</strong>.</li>
</ol>
