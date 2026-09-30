<p>The exact method for certificate renewal depends on whether that hostname is active<sup><a href="#footnote-1">1</a></sup> and whether it is a wildcard certificate.</p>
<p>Custom hostname certificates have a 90-day validity period and are available for renewal 30 days before their expiration.</p>
<h2 id="non-wildcard-hostnames">Non-wildcard hostnames</h2>
<p>If all of the following are true, Cloudflare will try to perform DCV automatically on the hostname's behalf by serving the <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/">HTTP token</a>.</p>
<ul>
<li>You are using a non-wildcard hostname.</li>
<li>The hostname is active.</li>
<li>You are not using <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/">Delegated DCV</a>.</li>
</ul>
<p>If the custom hostname is not active, then the custom hostname domain owner will need to add the TXT or HTTP DCV token for the new certificate to validate and issue. As the SaaS provider, you will be responsible for sharing this token with the custom hostname domain owner.</p>
<p>If you are using Delegated DCV, Cloudflare will continue to add TXT DCV tokens on your behalf as explained in <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/">Issue and validate certificates</a>.</p>
<h2 id="wildcard-hostnames">Wildcard hostnames</h2>
<p>With wildcard hostnames, you cannot use HTTP. In this case, you will have to use TXT DCV tokens.</p>
<p>These tokens can be fetched through the API or the dashboard when the certificates are in a <a href="/ssl/reference/certificate-statuses/#new-certificates">pending validation</a> state during custom hostname creation or during certificate renewals.</p>
<p>If your hostname is using another validation method, you will need to <a href="/api/resources/custom_hostnames/methods/edit/">update</a> the <code>&quot;method&quot;</code> field in the SSL object to be <code>&quot;txt&quot;</code>.</p>
<p>After this step, follow the normal steps for <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/">TXT validation</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4145.md")
</aside>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Meaning Cloudflare could verify your customer's ownership of the hostname and the [hostname status](/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/) is active.</li></ol></section>
