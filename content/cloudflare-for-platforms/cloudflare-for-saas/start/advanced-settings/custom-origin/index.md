<p>A <strong>custom origin server</strong> lets you send traffic from one or more custom hostnames to somewhere besides your default proxy fallback, such as:</p>
<ul>
<li><code>soap.stores.com</code> goes to <code>origin1.com</code></li>
<li><code>towel.stores.com</code> goes to <code>origin2.com</code></li>
</ul>
<h2 id="requirements">Requirements</h2>
<p>To use a custom origin server, you need to meet the following requirements:</p>
<ul>
<li>Each custom origin needs to be a valid hostname with a proxied (orange-clouded) A, AAAA, or CNAME record in your account's DNS. You cannot use an IP address.</li>
<li>The DNS record for the custom origin server does not currently support wildcard values.</li>
</ul>
<h2 id="use-a-custom-origin">Use a custom origin</h2>
<p>To use a custom origin, select that option when <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/">creating a new custom hostname</a> in the dashboard or include the <code>&quot;custom_origin_server&quot;: your_custom_origin_server</code> parameter when using the API <a href="/api/resources/custom_hostnames/methods/create/">POST command</a>.</p>
<h2 id="cloud-provider-origins-azure-aws-gcp">Cloud provider origins (Azure, AWS, GCP)</h2>
<p>When using a cloud provider endpoint as a custom origin (for example, Azure App Service, AWS ALB, or GCP Cloud Run), the provider may reject requests with a <code>404</code> or <code>400</code> error if the <code>Host</code> header does not match a domain configured on that endpoint.</p>
<p>By default, Cloudflare sends the original custom hostname as the <code>Host</code> header. If your cloud provider expects a different hostname:</p>
<ol>
<li>Configure the cloud provider to accept the custom hostname as a valid domain, or</li>
<li>Use an <a href="/rules/origin-rules/">Origin Rule</a> to override the <code>Host</code> header to match the hostname your cloud provider expects.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4167.md")
</aside>
<h2 id="sni-rewrites">SNI rewrites</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4166.md")
</aside>
<p>When Cloudflare establishes a connection to your default origin server, the <code>Host</code> header and <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/4168.md")
</div> will both be the value of the original custom hostname.
<p>However, if you configure that custom hostname with a custom origin, the value of the SNI will be that of the custom origin and the <code>Host</code> header will be the original custom hostname. Since these values will not match, you will not be able to use the <a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict)</a> on your origins.</p>
<p>To solve this problem, you can contact your account team to request an entitlement for <strong>SNI rewrites</strong>.</p>
<h3 id="sni-rewrite-options">SNI rewrite options</h3>
<p>Choose how your custom hostname populates the SNI value with SNI rewrites:</p>
<ul>
<li>
<p><strong>Origin server name</strong> (default): Set SNI to the custom origin</p>
<ul>
<li>If custom origin is <code>custom-origin.example.com</code>, then the SNI is <code>custom-origin.example.com</code>.</li>
</ul>
</li>
<li>
<p><strong>Host header</strong>: Set SNI to the host header (or a host header override)</p>
<ul>
<li>If wildcards are not enabled and the hostname is <code>example.com</code>, then the SNI is <code>example.com</code>.</li>
<li>If wildcards are enabled, the hostname is <code>example.com</code>, and a request comes to <code>www.example.com</code>, then the SNI is <code>www.example.com</code>.</li>
</ul>
</li>
<li>
<p><strong>Subdomain of zone</strong>: Choose what to set as the SNI value (custom hostname or any subdomain)</p>
<ul>
<li>If wildcards are not enabled and a request comes to <code>example.com</code>, choose whether to set the SNI as <code>example.com</code> or <code>www.example.com</code>.</li>
<li>If wildcards are enabled, you set the SNI to <code>example.com</code>, and a request comes to <code>www.example.com</code>, then the SNI is <code>example.com</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/4165.md")
</aside>
<h3 id="set-an-sni-rewrite">Set an SNI rewrite</h3>
<p>To set an SNI rewrite in the dashboard, choose your preferred option from <strong>Origin SNI value</strong> when <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/">creating a custom hostname</a>.</p>
<p>To set an SNI rewrite via the API, set the <code>custom_origin_sni</code> parameter when <a href="/api/resources/custom_hostnames/methods/create/">creating a custom hostname</a>:</p>
<ul>
<li><strong>Custom origin name</strong> (default): Applies if you do not set the parameter</li>
<li><strong>Host header</strong>: Specify <code>&quot;:request_host_header:&quot;</code></li>
<li><strong>Subdomain of zone</strong>: Set to <code>&quot;example.com&quot;</code> or another subdomain of the custom hostname</li>
</ul>
