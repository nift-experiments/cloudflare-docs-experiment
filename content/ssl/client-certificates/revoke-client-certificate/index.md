<p>You can revoke a client certificate you previously generated with the default <a href="/ssl/client-certificates/">Cloudflare-managed CA</a>.</p>
<p>It is not possible to permanently delete client certificates generated with the default Cloudflare-managed CA. Once revoked, these client certificates will still be listed on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/client-certificates"><strong>Client Certificates</strong></a> page, and can be restored at any time.</p>
<h2 id="steps">Steps</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Client Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the certificate you want to revoke.</li>
<li>Select <strong>Revoke</strong> and confirm the operation.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="effect-on-quota">Effect on quota</h3>
@markup("md", "content/.markup/bodies/14014.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/14013.md")
</aside>
