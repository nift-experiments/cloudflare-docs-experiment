<p>There are several required steps before a custom hostname can become active. For more details, refer to our <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">Get started guide</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="zone-name-restriction">Zone name restriction</h3>
@markup("md", "content/.markup/bodies/4107.md")
</aside>
<p>To create a custom hostname:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4110.md")
</div></div>
<p>For each custom hostname, Cloudflare issues two certificates bundled in chains that maximize browser compatibility (unless you <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/uploading-certificates/">upload custom certificates</a>).</p>
<p>The primary certificate uses a <code>P-256</code> key, is <code>SHA-2/ECDSA</code> signed, and will be presented to browsers that support elliptic curve cryptography (ECC). The secondary or fallback certificate uses an <code>RSA 2048-bit</code> key, is <code>SHA-2/RSA</code> signed, and will be presented to browsers that do not support ECC.</p>
<h2 id="hostnames-over-64-characters">Hostnames over 64 characters</h2>
<p>The Common Name (CN) restriction establishes a limit of 64 characters (<a href="https://www.rfc-editor.org/rfc/rfc5280.html">RFC 5280</a>). If you have a hostname that exceeds this length, you can set <code>cloudflare_branding</code> to <code>true</code> when creating your custom hostnames <a href="/api/resources/custom_hostnames/methods/create/">via API</a>.</p>
<pre><code class="language-txt">&#10;&quot;ssl&quot;: {&#10;    &quot;cloudflare_branding&quot;: true&#10;  }&#10;</code></pre>
<p>Cloudflare branding means that <code>sni.cloudflaressl.com</code> will be added as the certificate Common Name (CN) and the long hostname will be included as a part of the Subject Alternative Name (SAN).</p>
