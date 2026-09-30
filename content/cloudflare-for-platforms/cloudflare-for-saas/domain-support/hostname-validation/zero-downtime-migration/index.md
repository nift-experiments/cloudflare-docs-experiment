<p>When an end customer is already live on another CDN, switching their CNAME to your Cloudflare fallback origin causes a brief window where Cloudflare cannot yet proxy their traffic. Pre-validation lets you verify hostname ownership and optionally pre-issue the TLS certificate <em>before</em> the DNS cutover, so the migration is seamless.</p>
<h2 id="migration-sequence">Migration sequence</h2>
<ol>
<li>Create the custom hostname via API.</li>
<li>Pre-validate hostname ownership using an HTTP token or a DNS TXT record.</li>
<li>Pre-issue the TLS certificate before DNS cutover.</li>
<li>Confirm the hostname is <code>active</code>.</li>
<li>Update the end customer's CNAME - traffic cuts over with no downtime.</li>
</ol>
<hr />
<h2 id="step-1-create-the-custom-hostname">Step 1: Create the custom hostname</h2>
<p>Call the <a href="/api/resources/custom_hostnames/methods/create/">Create Custom Hostname</a> endpoint. Note the <code>ownership_verification</code> and <code>ownership_verification_http</code> fields in the response - you will need them in the next step.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_hostnames \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;hostname&quot;: &quot;app.example.com&quot;,&#10;    &quot;ssl&quot;: {&#10;      &quot;method&quot;: &quot;http&quot;,&#10;      &quot;type&quot;: &quot;dv&quot;,&#10;      &quot;settings&quot;: {&#10;        &quot;http2&quot;: &quot;on&quot;,&#10;        &quot;min_tls_version&quot;: &quot;1.2&quot;&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &quot;24c8c68e-bec2-49b6-868e-f06373780630&quot;,&#10;    &quot;hostname&quot;: &quot;app.example.com&quot;,&#10;    &quot;status&quot;: &quot;pending&quot;,&#10;    &quot;verification_errors&quot;: [&quot;custom hostname does not CNAME to this zone.&quot;],&#10;    &quot;ownership_verification&quot;: {&#10;      &quot;type&quot;: &quot;txt&quot;,&#10;      &quot;name&quot;: &quot;_cf-custom-hostname.app.example.com&quot;,&#10;      &quot;value&quot;: &quot;0e2d5a7f-1548-4f27-8c05-b577cb14f4ec&quot;&#10;    },&#10;    &quot;ownership_verification_http&quot;: {&#10;      &quot;http_url&quot;: &quot;http://app.example.com/.well-known/cf-custom-hostname-challenge/24c8c68e-bec2-49b6-868e-f06373780630&quot;,&#10;      &quot;http_body&quot;: &quot;48b409f6-c886-406b-8cbc-0fbf59983555&quot;&#10;    },&#10;    &quot;created_at&quot;: &quot;2020-03-04T20:06:04.117122Z&quot;&#10;  }&#10;}&#10;</code></pre>
<p>The <code>verification_errors</code> field will show <code>custom hostname does not CNAME to this zone</code> at this stage - that is expected. The error clears once pre-validation completes.</p>
<hr />
<h2 id="step-2-pre-validate-hostname-ownership">Step 2: Pre-validate hostname ownership</h2>
<p>Choose the method that fits your end customer's situation.</p>
<h3 id="option-a-http-token-end-customer-does-not-control-dns">Option A: HTTP token (end customer does not control DNS)</h3>
<p>Use this method when the end customer cannot update their authoritative DNS, or when you want to handle the verification yourself.</p>
<ol>
<li>
<p>Copy the <code>http_url</code> and <code>http_body</code> from the <code>ownership_verification_http</code> object in the Create Custom Hostname response.</p>
</li>
<li>
<p>Have the end customer serve the <code>http_body</code> value at the <code>http_url</code> path on their origin server. For example, in nginx:</p>
</li>
</ol>
<pre><code class="language-nginx">location /.well-known/cf-custom-hostname-challenge/24c8c68e-bec2-49b6-868e-f06373780630 {&#10;    return 200 &quot;48b409f6-c886-406b-8cbc-0fbf59983555\n&quot;;&#10;}&#10;</code></pre>
<p>Cloudflare crawls this URL using <code>User-Agent: Cloudflare Custom Hostname Verification</code>. The origin must respond with a <code>200</code> status and the exact token value in the body.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4113.md")
</aside>
<ol start="3">
<li>Wait a few minutes for Cloudflare to crawl the token. The hostname status will move from <code>pending</code> to <code>active</code> once ownership is confirmed.</li>
</ol>
<h3 id="option-b-txt-record-end-customer-controls-dns">Option B: TXT record (end customer controls DNS)</h3>
<p>Use this method when the end customer can add a DNS record at their authoritative DNS provider.</p>
<ol>
<li>
<p>Copy the <code>name</code> and <code>value</code> from the <code>ownership_verification</code> object in the Create Custom Hostname response.</p>
</li>
<li>
<p>Have the end customer add a <code>TXT</code> record at their DNS provider:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>TXT</code></td>
<td><code>_cf-custom-hostname.app.example.com</code></td>
<td><code>0e2d5a7f-1548-4f27-8c05-b577cb14f4ec</code></td>
</tr>
</tbody>
</table>
<ol start="3">
<li>
<p>Wait a few minutes for Cloudflare to detect the record. The hostname status will move to <code>active</code> once ownership is confirmed.</p>
</li>
<li>
<p>Once the hostname is active, the end customer can remove the TXT record.</p>
</li>
</ol>
<hr />
<h2 id="step-3-pre-issue-the-tls-certificate">Step 3: Pre-issue the TLS certificate</h2>
<p>Pre-issuing the certificate ensures there is no TLS error during cutover. Without this step, the certificate cannot issue until after the end customer's CNAME points to Cloudflare, which means <code>ssl.status</code> will remain <code>pending</code> through the DNS change. Choose one of these methods:</p>
<ul>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/"><strong>Delegated DCV</strong></a> - A one-time CNAME record delegates <code>_acme-challenge</code> to your SaaS zone, letting Cloudflare handle all future renewals automatically. The end customer can place the delegation CNAME at their own authoritative DNS, or if you host DNS for your customers directly, you can place it at your own zone instead.</li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/"><strong>TXT validation</strong></a> - Have the end customer add a <code>TXT</code> record to their authoritative DNS. Required for wildcard custom hostnames.</li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/#http-manual"><strong>Manual HTTP validation</strong></a> - Serve a DCV token file at a <code>/.well-known/</code> path on the origin. No action required from the end customer.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4112.md")
</aside>
<hr />
<h2 id="step-4-confirm-the-hostname-is-active">Step 4: Confirm the hostname is active</h2>
<p>Before updating DNS, verify that both the hostname and certificate are ready.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_hostnames/{custom_hostname_id} \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &quot;24c8c68e-bec2-49b6-868e-f06373780630&quot;,&#10;    &quot;hostname&quot;: &quot;app.example.com&quot;,&#10;    &quot;status&quot;: &quot;active&quot;,&#10;    &quot;ssl&quot;: {&#10;      &quot;status&quot;: &quot;active&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Wait until both <code>result.status</code> and <code>result.ssl.status</code> are <code>active</code> before proceeding. If either is still <code>pending</code>, wait and poll again.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4111.md")
</aside>
<hr />
<h2 id="step-5-update-the-end-customer-s-cname">Step 5: Update the end customer's CNAME</h2>
<p>Once <code>result.status</code> is <code>active</code> (and <code>ssl.status</code> is <code>active</code> too, if you pre-issued the certificate in Step 3), have the end customer update their CNAME to point to your fallback origin:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CNAME</code></td>
<td><code>app</code></td>
<td><code>fallback.yoursaaszone.com</code></td>
</tr>
</tbody>
</table>
<p>Traffic will begin proxying through Cloudflare as soon as DNS propagates. Because the hostname was already validated and the certificate was already issued, there is no downtime or certificate error during the transition.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/">Pre-validation methods</a></li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/">Certificate validation methods</a></li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/">Validation status</a></li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">Getting started with Cloudflare for SaaS</a></li>
</ul>
