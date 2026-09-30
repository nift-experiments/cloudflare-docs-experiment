<p>When you set your encryption mode to <strong>Full (strict)</strong>, Cloudflare does everything in <a href="/ssl/origin-configuration/ssl-modes/full/">Full mode</a> but also enforces more stringent requirements for origin certificates.</p>
<pre><code class="language-mermaid">flowchart LR&#10;    accTitle: Full - Strict SSL/TLS Encryption&#10;    accDescr: With an encryption mode of Full (strict), your application encrypts traffic going to and coming from Cloudflare.&#10;    A[Visitor] &lt;--Encrypted--&gt; B((Cloudflare))&lt;--Encrypted--&gt; C[(&quot;Origin server (verified) #9989;&quot;)]&#10;</code></pre>
<h2 id="use-when">Use when</h2>
<p>For the best security, choose <strong>Full (strict)</strong> mode whenever possible (unless you are an <a href="/ssl/origin-configuration/ssl-modes/ssl-only-origin-pull/">Enterprise customer</a>).</p>
<p>Your origin needs to be able to support an SSL certificate that is:</p>
<ul>
<li>Unexpired, meaning the certificate presents <code>notBeforeDate &lt; now() &lt; notAfterDate</code>.</li>
<li>Issued by a <a href="https://github.com/cloudflare/cfssl_trust">publicly trusted certificate authority</a> or <a href="/ssl/origin-configuration/origin-ca/">Cloudflare’s Origin CA</a>.</li>
<li>Contains a Common Name (CN) or Subject Alternative Name (SAN) that matches the requested or target hostname.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14263.md")
</aside>
<h2 id="required-setup">Required setup</h2>
<h3 id="prerequisites">Prerequisites</h3>
<p>Before enabling <strong>Full (strict)</strong> mode, make sure your origin:</p>
<ul>
<li>Allows HTTPS connections on port <code>443</code>.</li>
<li>Presents a certificate matching the requirements above.</li>
</ul>
<p>Otherwise, your visitors may experience a <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/">526 error</a>.</p>
<h3 id="process">Process</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14266.md")
</div></div>
<h2 id="limitations">Limitations</h2>
<p>Depending on your origin configuration, you may have to adjust settings to avoid <a href="/ssl/troubleshooting/mixed-content-errors/">Mixed Content errors</a> or <a href="/ssl/troubleshooting/too-many-redirects/">redirect loops</a>.</p>
