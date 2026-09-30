<p>This page lists Cloudflare requirements for custom certificates and explains how to upload and update these certificates using Cloudflare dashboard or API.</p>
<h2 id="certificate-requirements">Certificate requirements</h2>
<p>Before accepting custom certificates, Cloudflare parses them and checks for validity according to a list of requirements.</p>
<details class="nb-details"><summary>Full list of requirements</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14079.md")
</div></details>
<hr />
<h2 id="upload-a-custom-certificate">Upload a custom certificate</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14078.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14083.md")
</div></div>
<hr />
<h2 id="update-or-renew-an-existing-custom-certificate">Update or renew an existing custom certificate</h2>
<p>To renew a custom certificate that is approaching expiry, or to replace a certificate with updated key material, follow the steps below. <strong>This is the recommended renewal path</strong> — it does not consume an additional certificate quota slot and avoids downtime.</p>
<p>Before you update an existing custom certificate, you might want to consider having active <a href="/ssl/edge-certificates/universal-ssl/">universal</a> or <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced</a> certificates as fallback options. Go to the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates"><strong>Edge Certificates</strong></a> page to check a list of hostnames and status of the edge certificates in your zone.</p>
<p>If you are on an Enterprise plan and want to update a custom (modern) certificate, also consider requesting access to <a href="/ssl/edge-certificates/staging-environment/">Staging environment (Beta)</a>.</p>
<p>Replacing a custom certificate following these steps does not lead to any downtime. No connections will be terminated and new connections will use the new certificate. The old certificate will only actually be deleted when the new certificate is uploaded and active.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14086.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14073.md")
</aside>
<hr />
<h2 id="delete-a-custom-certificate">Delete a custom certificate</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Edge Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Edge Certificates</strong>, locate a custom certificate and select it to expand.</li>
<li>Select the cross button.</li>
<li>Select <strong>Confirm</strong> to delete the certificate.</li>
</ol>
