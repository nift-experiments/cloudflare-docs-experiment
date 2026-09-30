<p>This page explains how you can manage client certificates that have not been issued by Cloudflare CA. For a broader overview, refer to the <a href="/learning-paths/mtls/concepts/">mTLS at Cloudflare learning path</a>.</p>
<p>Bring your own CA (BYOCA) is especially useful if you already have mTLS implemented and <a href="/ssl/client-certificates/#how-it-works">client certificates are already installed</a> on devices.</p>
<h2 id="availability">Availability</h2>
<ul>
<li>This feature is only available on Enterprise accounts.</li>
<li>Each Enterprise account can upload up to five CAs. This quota does not apply to CAs uploaded through <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">Cloudflare Access</a>.</li>
<li>The CA certificate quota is shared across <a href="/api-shield/security/mtls/configure/">API Shield</a>, <a href="/workers/runtime-apis/bindings/mtls/">Workers mTLS</a>, and <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>.</li>
<li>To increase this quota, contact your account team.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14036.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cloudflare-access-uses-a-separate-quota">Cloudflare Access uses a separate quota</h3>
@markup("md", "content/.markup/bodies/14035.md")
</aside>
<h2 id="when-to-use-byoca">When to use BYOCA</h2>
<p>BYOCA works well if:</p>
<ul>
<li>You already have an internal CA and client certificates are installed on your devices.</li>
<li>You issue certificates at high volume or high churn — for example, one certificate per ephemeral virtual machine, container, or device. With BYOCA, Cloudflare stores only your CA certificate, not individual issued certificates, so there is no per-certificate quota.</li>
<li>You want full control over certificate validity periods, key types, and revocation through your own CA tooling.</li>
</ul>
<p>If you only have a small, stable set of devices or services to authenticate, the <a href="/ssl/client-certificates/create-a-client-certificate/">Cloudflare-managed CA</a> is simpler to set up.</p>
<h2 id="ca-certificate-requirements">CA certificate requirements</h2>
<p>When you upload your CA, Cloudflare validates the certificate according to certain requirements.</p>
<ul>
<li>
<p>The CA certificate can be from a publicly trusted CA or self-signed.</p>
</li>
<li>
<p>In the certificate <code>Basic Constraints</code>, the attribute <code>CA</code> must be set to <code>TRUE</code>.</p>
</li>
<li>
<p>The certificate must use one of the signature algorithms listed below:</p>
  <details class="nb-details"><summary>Allowed signature algorithms</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/14037.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14034.md")
</aside>
<h2 id="set-up-mtls-with-your-ca">Set up mTLS with your CA</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14040.md")
</div></div>
<p>After uploading the CA and associating hostnames, create a custom rule to enforce client certificate validation.
You can do this <a href="/learning-paths/mtls/mtls-app-security/#3-validate-the-client-certificate-in-the-waf">via the dashboard</a> or <a href="/waf/custom-rules/create-api/">via API</a>.</p>
<pre><code class="language-txt">  &quot;expression&quot;: &quot;(http.host in {\&quot;&lt;HOSTNAME_1&gt;\&quot; \&quot;&lt;HOSTNAME_2&gt;\&quot;} and not cf.tls_client_auth.cert_verified)&quot;,&#10;  &quot;action&quot;: &quot;block&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14031.md")
</aside>
<h3 id="multiple-cas-for-one-hostname">Multiple CAs for one hostname</h3>
<p>There can be multiple CAs (Cloudflare-managed or BYOCA) associated with the same hostname. For BYOCA certificates, the most recently deployed certificate will be prioritized.</p>
<p>If you wish to remove the association from the Cloudflare-managed certificate and only use your BYOCA certificate(s):</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14043.md")
</div></div>
<h2 id="delete-an-uploaded-ca">Delete an uploaded CA</h2>
<p>If you want to remove a CA that you have previously uploaded, you must first remove any hostname associations that it has.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14046.md")
</div></div>
<h2 id="list-ca-hostname-associations">List CA hostname associations</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14049.md")
</div></div>
