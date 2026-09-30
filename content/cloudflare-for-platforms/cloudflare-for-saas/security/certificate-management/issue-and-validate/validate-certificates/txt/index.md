<p>TXT record validation requires the creation of a TXT record in the hostname's authoritative DNS.
<br /></p>
<p>You choose one certificate validation method when you <a href="/api/resources/custom_hostnames/methods/create/">create a custom hostname</a>. The API accepts one <code>ssl.method</code> value: <code>http</code>, <code>txt</code>, or <code>email</code>.</p>
<h2 id="when-to-use">When to use</h2>
<p>Generally, you should use TXT-based DCV when you cannot use <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/">HTTP validation</a> or <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/">Delegated DCV</a>, or when you need the certificate active before your customer changes DNS.</p>
<h3 id="non-wildcard-custom-hostnames">Non-wildcard custom hostnames</h3>
<p>If your custom hostname does not include a wildcard, Cloudflare always attempts to complete DCV through <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/#http-automatic">HTTP validation</a> after the hostname points to your SaaS target, even if you have selected <strong>TXT</strong> for your validation method.</p>
<p>This HTTP validation should succeed as long as your customer's hostname points to your SaaS target and they do not have any <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/#certificate-authority-authorization-caa-records">CAA records</a> blocking your chosen certificate authority.</p>
<p>This automatic HTTP attempt does not mean that the Create Custom Hostname API accepts both HTTP and TXT validation methods in one request. The <code>ssl.method</code> field accepts one value.</p>
<h3 id="wildcard-custom-hostnames">Wildcard custom hostnames</h3>
<p>To validate a certificate on a wildcard custom hostname, you should either set up <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/">Delegated DCV</a> or <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/">TXT-based DCV</a>.</p>
<p>Cloudflare recommends Delegated DCV as it is much simpler for you and your customers.</p>
<p>If you choose TXT-based DCV, Cloudflare requires two TXT DCV tokens - one for the apex and one for the wildcard - to be placed at your customer’s authoritative DNS provider in order for the wildcard certificate to issue or renew.</p>
<p>These two tokens are required because Let’s Encrypt and Google Trust Services follow the <a href="https://datatracker.ietf.org/doc/html/rfc8555">ACME Protocol</a>, which requires one DCV token to be placed for every hostname on the certificate.</p>
<p>This means that - if you choose to use wildcard custom hostnames - you will need a way to share these DCV tokens with your customer.</p>
<hr />
<h3 id="1-get-txt-tokens"><ol>
<li>Get TXT tokens</li>
</ol></h3>
<p>Once you <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/issue-certificates/">create a new hostname</a> and choose this validation method, your tokens will be ready after a few seconds.</p>
<p>These tokens can be fetched through the API or the dashboard when the certificates are in a <a href="/ssl/reference/certificate-statuses/#new-certificates">pending validation</a> state during custom hostname creation or during certificate renewals.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4157.md")
</div></div>
<h3 id="2-share-with-your-customer"><ol start="2">
<li>Share with your customer</li>
</ol></h3>
<p>You will then need to share these TXT tokens with your customers.</p>
<h3 id="3-add-dns-records-customer"><ol start="3">
<li>Add DNS records (customer)</li>
</ol></h3>
<p>Your customers should place these at their authoritative DNS provider under the <code>&quot;_acme-challenge&quot;</code> DNS label. Once these TXT records are in place, validation and certificate issuance will automatically complete.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4154.md")
</aside>
<p>If you would like to request an immediate recheck, <a href="/ssl/edge-certificates/changing-dcv-method/validation-backoff-schedule/">rather than wait for the next retry</a>, send a <a href="/api/resources/custom_hostnames/methods/edit/">PATCH request</a> with the same values as your initial <code>POST</code> request.</p>
<h3 id="4-optional-fetch-new-tokens"><ol start="4">
<li>(Optional) Fetch new tokens</li>
</ol></h3>
<p>Your DCV tokens expire after a <a href="/cloudflare-for-platforms/cloudflare-for-saas/reference/token-validity-periods/">certain amount of time</a>, depending on your certificate authority.</p>
<p>This means that, if your customers take too long to place their tokens at their authoritative DNS provider, you may need to <a href="#1-get-txt-tokens">get new tokens</a> and re-share them with your customer.</p>
