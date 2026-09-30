<p>HTTP validation involves adding a DCV token to your customer's origin.</p>
<p>You choose one certificate validation method when you <a href="/api/resources/custom_hostnames/methods/create/">create a custom hostname</a>. The API accepts one <code>ssl.method</code> value: <code>http</code>, <code>txt</code>, or <code>email</code>.</p>
<hr />
<h2 id="non-wildcard-custom-hostnames">Non-wildcard custom hostnames</h2>
<p>If your custom hostname does not include a wildcard, Cloudflare attempts to complete DCV through <a href="#http-automatic">HTTP validation</a> after the hostname points to your SaaS target, even if you have selected <strong>TXT</strong> for your validation method.</p>
<p>This HTTP validation should succeed as long as your customer's hostname points to your SaaS target and they do not have any <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/#certificate-authority-authorization-caa-records">CAA records</a> blocking your chosen certificate authority.</p>
<h2 id="wildcard-custom-hostnames">Wildcard custom hostnames</h2>
<p>HTTP DCV validation is not allowed for wildcard certificates. Use <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/">TXT validation</a> instead. You can also configure <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/">Delegated DCV</a> to automate TXT-based validation.</p>
<hr />
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="dcv-records-are-generated-asynchronously">DCV records are generated asynchronously</h3>
@markup("md", "content/.markup/bodies/4159.md")
</aside>
<h2 id="validation-methods">Validation methods</h2>
<h3 id="http-automatic">HTTP (automatic)</h3>
<p>If you value simplicity and your customers can handle a few minutes of downtime, you can rely on Cloudflare automatic HTTP validation.</p>
<p>Once you <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/issue-certificates/">create a new hostname</a> and choose the <code>http</code> validation method, all your customers have to do is add a CNAME to your <code>$CNAME_TARGET</code> and Cloudflare will take care of the rest.</p>
<p>Automatic HTTP validation works on the fly. After your customer points the hostname to your SaaS target, Cloudflare can serve the CA's HTTP DCV token from the edge and complete certificate validation.</p>
<p>During that period, the hostname may route to Cloudflare before the certificate reaches <code>ssl.status: active</code>. If you need the certificate active before your customer changes DNS, use <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/">TXT validation</a> or <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/">Delegated DCV</a> instead.</p>
<details class="nb-details"><summary>What happens after you create the custom hostname</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4160.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4158.md")
</aside>
<p>If you would like to complete the issuance process before asking your customer to update their CNAME (or before changing the resolution of your target CNAME to be proxied by Cloudflare), choose another validation method.</p>
<h3 id="http-manual">HTTP (manual)</h3>
<p>Once you <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/issue-certificates/">create a new hostname</a> and choose this validation method, you will see the following values after a few seconds:</p>
<br />
<ul>
<li><a href="/api/resources/custom_hostnames/methods/get/"><strong>API</strong></a>: Within the <code>ssl</code> object, store the values present in the <code>validation_records</code> array (specifically <code>http_url</code> and <code>http_body</code>).</li>
<li><strong>Dashboard</strong>: When viewing an individual certificate on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/custom-hostnames"><strong>Custom Hostnames</strong></a> page, refer to the values for <strong>Certificate validation request</strong> and <strong>Certificate validation response</strong>.</li>
</ul>
<p>At your origin, make the <code>http_body</code> available in a TXT record at the path specified in <code>http_url</code>. This path should also be publicly accessible to anyone on the Internet so your CA can access it.</p>
<p>Here is an example NGINX configuration that would return a token:</p>
<pre><code class="language-txt">location &quot;/.well-known/pki-validation/ca3-0052344e54074d9693e89e27486692d6.txt&quot; {&#10;       return 200 &quot;ca3-be794c5f757b468eba805d1a705e44f6\n&quot;;&#10;}&#10;</code></pre>
<p>Once your configuration is live, test that the DCV text file is in place with <code>curl</code>:</p>
<pre><code class="language-sh">curl &quot;http://http-preval.example.com/.well-known/pki-validation/ca3-0052344e54074d9693e89e27486692d6.txt&quot;&#10;</code></pre>
<pre><code class="language-txt">ca3-be794c5f757b468eba805d1a705e44f6&#10;</code></pre>
<p>The token is valid for one check cycle. On the next check cycle, Cloudflare will ask the CA to recheck the URL, complete validation, and issue the certificate.</p>
<p>If you would like to request an immediate recheck, <a href="/ssl/edge-certificates/changing-dcv-method/validation-backoff-schedule/">rather than wait for the next retry</a>, send a <a href="/api/resources/custom_hostnames/methods/edit/">PATCH request</a> with the same values as your initial <code>POST</code> request.</p>
