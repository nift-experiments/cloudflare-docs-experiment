<p>When you enable global Authenticated Origin Pulls (AOP), Cloudflare uses a Cloudflare-provided client certificate for all proxied traffic to your zone. This certificate is shared across all Cloudflare accounts and guarantees that the request is coming from the Cloudflare network.</p>
<p>Global, <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/">zone-level</a>, and <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">per-hostname</a> AOP are independent configurations. Enabling or disabling one does not affect the others.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>
<p>Make sure your zone is using an <a href="/ssl/origin-configuration/ssl-modes/">SSL/TLS encryption mode</a> of <strong>Full</strong> or higher.</p>
</li>
<li>
<p>Consider your security and certificate needs:</p>
<ul>
<li>
<p>The Cloudflare-provided certificate is not exclusive to your account. It only guarantees that a request is coming from the Cloudflare network. If you need stricter security, set up <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/">zone-level</a> or <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">per-hostname</a> AOP with your own certificate instead.</p>
</li>
<li>
<p>Global AOP is applied to all proxied hostnames on your zone, including <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">custom hostnames</a> configured on a Cloudflare for SaaS zone. If you need a different AOP certificate for different custom hostnames, use <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">per-hostname AOP</a>.</p>
</li>
</ul>
</li>
</ul>
<h2 id="1-download-the-cloudflare-certificate"><ol>
<li>Download the Cloudflare certificate</li>
</ol></h2>
<p><a href="/ssl/static/authenticated_origin_pull_ca.pem">Download the Cloudflare authenticated origin pull certificate (.PEM)</a> and upload it to your origin server. This certificate is <strong>not</strong> the same as the <a href="/ssl/origin-configuration/origin-ca/">Cloudflare Origin CA certificate</a>.</p>
<h2 id="2-configure-origin-to-accept-client-certificates"><ol start="2">
<li>Configure origin to accept client certificates</li>
</ol></h2>
<p>With the certificate installed, set up your origin web server to accept client certificates.</p>
<p>Check the examples below for Apache and NGINX or refer to your origin web server documentation - for example, <a href="https://www.haproxy.com/documentation/hapee/latest/security/authentication/client-certificate-authentication/">HAProxy</a>, <a href="https://doc.traefik.io/traefik/https/tls/#client-authentication-mtls">Traefik</a>, <a href="https://caddyserver.com/docs/json/apps/http/servers/tls_connection_policies/client_authentication/mode/">Caddy</a>.</p>
<details class="nb-details"><summary>Apache example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14320.md")
</div></details>
<details class="nb-details"><summary>NGINX example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14321.md")
</div></details>
<p>At this point, you may also want to enable logging on your origin so that you can verify the configuration is working.</p>
<h2 id="3-enable-global-authenticated-origin-pulls"><ol start="3">
<li>Enable global Authenticated Origin Pulls</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14324.md")
</div></div>
<h2 id="4-enforce-validation-check-on-your-origin"><ol start="4">
<li>Enforce validation check on your origin</li>
</ol></h2>
<p>Once you can confirm everything is working as expected for your specific origin setup, configure your origin to enforce the authentication.</p>
<details class="nb-details"><summary>Apache example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14325.md")
</div></details>
<details class="nb-details"><summary>NGINX example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14326.md")
</div></details>
<p>After completing the process, you can use <code>curl</code> to send requests directly to your origin IPs, verifying that the requests fail due to certificate validation being enforced.</p>
