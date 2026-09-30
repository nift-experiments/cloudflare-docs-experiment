<p>Some customers may need to manage their own SSL certificates or rely on specific Certificate Authorities.</p>
<p>If you disable your domain's Universal SSL certificate, Cloudflare removes that certificate from our network and will not order or renew any additional Universal SSL certificates.</p>
<p>Disabling Universal SSL will not cause any interruption to ongoing TLS connections to your domain on Cloudflare's network, they will continue to be served according to the Universal SSL certificate used when they were first established. Eventually these connections will naturally end.</p>
<p>New TLS connections are expected to succeed as long as you have another valid certificate active, such as a <a href="/ssl/edge-certificates/custom-certificates/">custom</a>) or <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced</a> certificate. New TLS connections will receive the highest priority certificate from our edge as per our <a href="/ssl/reference/certificate-and-hostname-priority/">certificate and hostname priority</a>. If a valid certificate is not active before disabling, TLS connections will fail. For more information, refer to <a href="#potential-errors">Potential errors</a> below.</p>
<h2 id="potential-errors">Potential errors</h2>
<p>To avoid errors with your domain, either <a href="/ssl/edge-certificates/custom-certificates/">upload a custom certificate</a> or purchase <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a> before disabling Universal SSL.</p>
<p>If you disable Universal SSL, you may experience errors with the following scenarios:</p>
<ul>
<li>
<p><strong>Enabled features</strong>:</p>
<ul>
<li><a href="/ssl/edge-certificates/additional-options/http-strict-transport-security/">HTTP Strict Transport Security (HSTS)</a></li>
<li><a href="/ssl/edge-certificates/additional-options/always-use-https/">Always Use HTTPS</a></li>
<li><a href="/ssl/edge-certificates/additional-options/opportunistic-encryption/">Opportunistic Encryption</a></li>
</ul>
</li>
<li>
<p><strong>Other setups</strong>:</p>
<ul>
<li><a href="/rules/page-rules/">Page Rules</a> that redirect traffic to HTTPS</li>
<li>HTTP to HTTPS redirects at your origin web server</li>
</ul>
</li>
</ul>
<h2 id="disable-universal-ssl-certificate">Disable Universal SSL certificate</h2>
<p>Before you disable Universal SSL/TLS, make sure you have <a href="/ssl/edge-certificates/custom-certificates/">uploaded a custom certificate</a> or purchased <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a> to protect your domain.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14056.md")
</div></div>
<h2 id="re-enable-universal-ssl">Re-enable Universal SSL</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14059.md")
</div></div>
