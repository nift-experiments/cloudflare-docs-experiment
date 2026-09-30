<p>HTTPS on Cloudflare involves two separate connections: visitor to Cloudflare, and Cloudflare to your origin server. Both must be encrypted for end-to-end security. This guide walks through five stages:</p>
<ol>
<li>Configure your SSL/TLS encryption mode.</li>
<li>Redirect all HTTP requests to HTTPS.</li>
<li>Harden your HTTPS setup with minimum TLS versions and HSTS.</li>
<li>Monitor third-party scripts on your pages.</li>
<li>Verify your configuration.</li>
</ol>
<p>The core workflow is available on Free, Pro, and Business plans.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15164.md")
</aside>
<h2 id="configure-your-ssl-tls-encryption-mode">Configure your SSL/TLS encryption mode</h2>
<p>Your SSL/TLS encryption mode controls how Cloudflare connects to your origin server. For end-to-end encryption, use <strong>Full (strict)</strong> — it encrypts both connections and verifies your origin certificate. For a detailed comparison of all available modes, refer to <a href="/ssl/origin-configuration/ssl-modes/">Encryption modes</a>.</p>
<h3 id="check-your-current-mode">Check your current mode</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15165.md")
</div>
<h3 id="install-a-cloudflare-origin-ca-certificate">Install a Cloudflare Origin CA certificate</h3>
<p>If your origin server does not have a valid SSL certificate, install a free Cloudflare Origin CA certificate. Origin CA certificates are valid for up to 15 years and are trusted by Cloudflare, which means you can set your encryption mode to Full (strict) after installing one.</p>
<p>If your origin already has a valid certificate from a publicly trusted certificate authority, skip to <a href="#set-your-encryption-mode-to-full-strict">Set your encryption mode to Full (strict)</a>.</p>
<h4 id="1-create-an-origin-ca-certificate"><ol>
<li>Create an Origin CA certificate</li>
</ol></h4>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15166.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15163.md")
</aside>
<h4 id="2-install-the-certificate-on-your-origin-server"><ol start="2">
<li>Install the certificate on your origin server</li>
</ol></h4>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15167.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15162.md")
</aside>
<h3 id="set-your-encryption-mode-to-full-strict">Set your encryption mode to Full (strict)</h3>
<p>After installing a valid certificate on your origin server, set the encryption mode to <strong>Full (strict)</strong> by following the steps below.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15170.md")
</div></div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15161.md")
</aside>
<h2 id="redirect-all-http-requests-to-https">Redirect all HTTP requests to HTTPS</h2>
<p>Even with an active edge certificate, visitors can still access resources over unsecured HTTP connections. Two settings work together to fix this:</p>
<ol>
<li>Always Use HTTPS redirects HTTP requests to HTTPS</li>
<li>Automatic HTTPS Rewrites fixes mixed content references in your page HTML</li>
</ol>
<h3 id="turn-on-always-use-https">Turn on Always Use HTTPS</h3>
<p>Always Use HTTPS redirects all HTTP requests to HTTPS before they reach your origin.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15160.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15175.md")
</div></div>
<h3 id="turn-on-automatic-https-rewrites">Turn on Automatic HTTPS Rewrites</h3>
<p>Automatic HTTPS Rewrites prevents mixed content errors by rewriting HTTP resource URLs in your page HTML to HTTPS. This is useful for sites where you do not control all asset URLs, such as CMS-hosted content or embedded third-party resources.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15179.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15159.md")
</aside>
<h2 id="harden-your-https-configuration">Harden your HTTPS configuration</h2>
<p>After your encryption mode is set and HTTP traffic is redirected, strengthen your configuration by setting a minimum TLS version, turning on HTTP Strict Transport Security (HSTS), and turning on TLS 1.3.</p>
<h3 id="set-your-minimum-tls-version">Set your minimum TLS version</h3>
<p>TLS 1.0 and 1.1 have known vulnerabilities and are no longer considered secure. Setting the minimum TLS version to 1.2 blocks connections from clients using older protocols. For guidance on which version to choose, refer to <a href="/ssl/reference/protocols/">TLS protocols</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15183.md")
</div></div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="per-hostname-minimum-tls-version-requires-advanced-certificate-manager">Per-hostname minimum TLS version requires Advanced Certificate Manager</h3>
@markup("md", "content/.markup/bodies/15158.md")
</aside>
<h3 id="turn-on-tls-1-3">Turn on TLS 1.3</h3>
<p>TLS 1.3 provides faster handshakes and improved security over TLS 1.2.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15187.md")
</div></div>
<h3 id="turn-on-hsts">Turn on HSTS</h3>
<p>HTTP Strict Transport Security (HSTS) adds a response header that tells browsers to connect to your site over HTTPS only, even if a link or redirect tries to send them over HTTP. HSTS protects against protocol downgrade attacks.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15157.md")
</aside>
<p>Before turning on HSTS, confirm these prerequisites:</p>
<ul>
<li>HTTPS is enabled and working on your domain.</li>
<li>Your DNS records are set to <a href="/dns/proxy-status/">Proxied</a>.</li>
<li>You are not redirecting HTTPS to HTTP anywhere.</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15191.md")
</div></div>
<h3 id="review-your-cipher-suites">Review your cipher suites</h3>
<p>Cloudflare's default cipher suites provide strong encryption for most sites. You do not need to change them unless a security audit or compliance requirement specifies particular cipher configurations.</p>
<p>For details on the default cipher suites and how to customize them, refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/">Cipher suites</a>. For compliance-specific cipher configurations, refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/">Customize cipher suites via API</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="custom-cipher-suites-require-advanced-certificate-manager">Custom cipher suites require Advanced Certificate Manager</h3>
@markup("md", "content/.markup/bodies/15156.md")
</aside>
<h2 id="monitor-third-party-scripts-with-client-side-security">Monitor third-party scripts with client-side security</h2>
<p>HTTPS encrypts data in transit, but third-party scripts loaded by your pages can still exfiltrate data from the browser. Client-side security monitors these scripts and alerts you to unexpected additions.</p>
<h3 id="turn-on-script-monitoring">Turn on script monitoring</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15192.md")
</div>
<h3 id="review-detected-resources">Review detected resources</h3>
<p>After turning on monitoring, it may take some time for Cloudflare to generate a list of detected scripts on your domain.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15193.md")
</div>
Depending on your Cloudflare plan, you may also be able to review connections made by scripts and check them for malicious activity. For setup details, refer to [Get started with client-side security](/client-side-security/get-started/).
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="content-security-rules-require-client-side-security-advanced">Content security rules require Client-Side Security Advanced</h3>
@markup("md", "content/.markup/bodies/15155.md")
</aside>
<h2 id="verify-your-configuration">Verify your configuration</h2>
<p>After completing the previous stages, verify that your HTTPS configuration works as expected.</p>
<h3 id="use-automatic-ssl-tls">Use Automatic SSL/TLS</h3>
<p>Cloudflare's Automatic SSL/TLS analyzes your origin server and selects the most secure encryption mode your origin supports. If your zone uses Automatic SSL/TLS (the default for new zones), Cloudflare adjusts the mode automatically and will not downgrade to a less secure mode if your origin certificate expires.</p>
<p>To check whether your zone uses Automatic SSL/TLS:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15194.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15154.md")
</aside>
<h3 id="test-with-external-tools">Test with external tools</h3>
<p>Use <a href="https://www.ssllabs.com/ssltest/">SSL Labs Server Test</a> to verify your HTTPS configuration from outside the Cloudflare network. Enter your domain and review the report. An A or A+ grade indicates that your TLS configuration, certificate chain, and protocol support meet current security standards.</p>
<p>To test supported TLS versions, attempt a request to your website or application while specifying a TLS version.</p>
<p>For example, to test TLS 1.1, use the <code>curl</code> command below. Replace <code>www.example.com</code> with your Cloudflare domain and hostname.</p>
<pre><code class="language-sh">curl https://www.example.com -svo /dev/null --tls-max 1.1&#10;</code></pre>
<p>If the TLS version you are testing is blocked by Cloudflare, the TLS handshake is not completed and returns an error:</p>
<p><code>* error:1400442E:SSL routines:CONNECT_CR_SRVR_HELLO:tlsv1 alert</code></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15153.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="pci-dss-compliance">PCI DSS compliance</h3>
@markup("md", "content/.markup/bodies/15152.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<p><strong>SSL/TLS</strong></p>
<ul>
<li><a href="/ssl/get-started/">Get started with SSL/TLS</a> — onboarding guide for edge certificates, encryption modes, and HTTPS enforcement</li>
<li><a href="/ssl/origin-configuration/ssl-modes/">Encryption modes</a> — detailed explanation of Off, Flexible, Full, and Full (strict) modes</li>
<li><a href="/ssl/origin-configuration/origin-ca/">Cloudflare Origin CA</a> — create free origin certificates trusted by Cloudflare</li>
<li><a href="/ssl/troubleshooting/mixed-content-errors/">Mixed content errors</a> — troubleshoot HTTP resources loaded on HTTPS pages</li>
<li><a href="/ssl/troubleshooting/too-many-redirects/">ERR_TOO_MANY_REDIRECTS</a> — fix redirect loops caused by encryption mode misconfigurations</li>
</ul>
<p><strong>Client-side security</strong></p>
<ul>
<li><a href="/client-side-security/get-started/">Get started with client-side security</a> — activate monitoring, review scripts, configure alerts, and create rules</li>
<li><a href="/client-side-security/reference/pci-dss/">Client-side security and PCI DSS compliance</a> — how client-side security maps to PCI DSS v4 requirements</li>
</ul>
