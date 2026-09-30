<p>You can enable mutual Transport Layer Security (mTLS) for any hostname. For more information, refer to the <a href="/ssl/client-certificates/">Client certificates overview</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cloudflare-issued-or-byoca">Cloudflare-issued or BYOCA</h3>
@markup("md", "content/.markup/bodies/14026.md")
</aside>
<p>To enable mTLS for a host from the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Client Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>On the <strong>Hosts</strong> section of the <strong>Client Certificates</strong> card, select <strong>Edit</strong>.</li>
<li>Enter the name of a host in your current domain.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14025.md")
</aside>
4. Select **Save** to confirm.
<h2 id="cas-in-use">CAs in use</h2>
<p>As explained in the <a href="/ssl/client-certificates/#how-it-works">Client certificates overview</a>, Cloudflare validates client certificates against CAs set at account level. This means that these certificates can be used for validation across multiple zones/domains (<code>example.com</code>), as long as the zones are under the same Cloudflare account and you have enabled mTLS for the host.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="bring-your-own-ca">Bring your own CA</h3>
@markup("md", "content/.markup/bodies/14024.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<p>After enabling mTLS for your host, you can:</p>
<ul>
<li>Enforce mTLS with a WAF custom rule. Select <strong>Create mTLS Rule</strong> on the dashboard to use a template, or refer to our <a href="/learning-paths/mtls/mtls-app-security/#3-validate-the-client-certificate-in-the-waf">mTLS at Cloudflare learning path</a> for further guidance.</li>
<li>Enforce mTLS with <a href="/api-shield/security/mtls/configure/">API Shield</a>. While API Shield is <strong>not required</strong> to use mTLS, many teams may use mTLS to protect their APIs.</li>
</ul>
